//! Glacis — application de bureau (Tauri 2).
//! La page (tauri/www/index.html, construite par build/construire-appli.py) est la même que dans le
//! navigateur. Ce fichier ne fait que ce qu'une page ne peut pas faire seule :
//!  · lire et écrire dans le dossier « Glacis » choisi une fois (son chemin est retenu par la page,
//!    il n'y a donc plus d'autorisation à redonner à chaque démarrage) : lister, infos, lire, ecrire,
//!    creer_dossier, supprimer — voir src/coeur/appli-bureau.js, qui les présente comme les dossiers
//!    du navigateur ;
//!  · choisir ce dossier (fenêtre de Windows) ;
//!  · plein écran de la fenêtre ;
//!  · ouvrir un site dans une fenêtre de l'application, ou dans le navigateur ;
//!  · se mettre à jour : la page lit appli/latest.json et télécharge l'installateur sur le site public
//!    (par le réseau de Windows, comme le navigateur : proxy et certificats de l'école compris), puis
//!    installer_paquet vérifie la signature (CLE_MAJ ; clé privée seulement dans le secret du dépôt public)
//!    et lance l'installation.
//!  · donner à la page les licences de Tauri et des bibliothèques Rust (licences_rust : fichier écrit par
//!    build/licences-rust.py avec cargo-about, lu dans Réglages › À propos › Licences des composants) ;
//!  · servir les applis HTML du dossier « Glacis/Applis » à l'adresse appli:// (http://appli.localhost/ sous
//!    Windows), avec le pont /_ma-classe/pont.js (src/applis/pont-applis.js) ; jamais leurs dossiers « donnees »,
//!    que chaque appli ne lit et n'écrit que par le pont, pour elle seule (module Applis de la page).
//! Les fenêtres de sites n'ont accès à aucune de ces commandes (capabilities/default.json : « main » seule) ; les
//! applis, d'une autre origine (appli.localhost) et dans un cadre « sandbox », non plus.
//! Depuis le 13 novembre 2026 (lot B de l'audit de sécurité), les commandes de fichiers n'agissent que DANS le dossier
//! retenu (src/chemins.rs) : même un code glissé dans la page ne pourrait rien toucher d'autre sur l'ordinateur ; le
//! dossier lui-même n'est jamais supprimé ni recréé, et un installateur plus ancien que l'application est refusé.

mod appli;
mod chemins;

use base64::{engine::general_purpose::STANDARD, Engine};
use minisign_verify::{PublicKey, Signature};
use percent_encoding::percent_decode_str;
use serde::Serialize;
use std::{
    fs,
    io::ErrorKind,
    path::{Path, PathBuf},
    sync::Mutex,
    time::UNIX_EPOCH,
};
use tauri::{
    ipc::{InvokeBody, Request, Response},
    AppHandle, Manager, Url, WebviewUrl, WebviewWindow, WebviewWindowBuilder,
};
use tauri_plugin_dialog::DialogExt;
use tauri_plugin_opener::OpenerExt;

fn texte<E: std::fmt::Display>(e: E) -> String {
    e.to_string()
}

#[derive(Serialize)]
struct Entree {
    nom: String,
    dossier: bool,
}

#[derive(Serialize)]
struct Infos {
    dossier: bool,
    taille: u64,
    modif: u64,
}

/// Le dossier « Glacis » retenu sur ce poste (gardé en mémoire après la première lecture du fichier du profil).
static RACINE: Mutex<Option<String>> = Mutex::new(None);

fn racine(app: &AppHandle) -> Result<PathBuf, String> {
    if let Some(r) = RACINE.lock().map_err(texte)?.clone() {
        return Ok(PathBuf::from(r));
    }
    let r = dossier_retenu(app.clone()).ok_or("aucun dossier « Glacis » choisi sur ce poste")?;
    *RACINE.lock().map_err(texte)? = Some(r.clone());
    Ok(PathBuf::from(r))
}

fn retenir(app: &AppHandle, chemin: &str) -> Result<(), String> {
    fs::write(fichier_dossier(app)?, chemin).map_err(texte)?;
    *RACINE.lock().map_err(texte)? = Some(chemin.to_string());
    Ok(())
}

/// Le chemin demandé par la page, s'il est dans le dossier retenu ; sinon une erreur (rien n'est fait).
/// « E: » seul (la page retire la barre finale : dossier retenu à la racine d'une clé USB) vaut « E:/ ».
fn permis(app: &AppHandle, chemin: &str) -> Result<PathBuf, String> {
    let c = chemins::avec_barre_de_lecteur(chemin);
    chemins::dans_racine(&racine(app)?, Path::new(&c))
}

/// Contenu d'un dossier (noms et nature).
#[tauri::command]
fn lister(app: AppHandle, chemin: String) -> Result<Vec<Entree>, String> {
    let p = permis(&app, &chemin)?;
    let mut v = Vec::new();
    for e in fs::read_dir(&p).map_err(texte)? {
        let e = e.map_err(texte)?;
        let dossier = e.path().is_dir();
        v.push(Entree {
            nom: e.file_name().to_string_lossy().into_owned(),
            dossier,
        });
    }
    Ok(v)
}

/// Nature, taille et date d'un fichier ou d'un dossier ; rien s'il n'existe pas (ou s'il est hors du dossier retenu).
#[tauri::command]
fn infos(app: AppHandle, chemin: String) -> Option<Infos> {
    let p = permis(&app, &chemin).ok()?;
    let m = fs::metadata(&p).ok()?;
    let modif = m
        .modified()
        .ok()
        .and_then(|t| t.duration_since(UNIX_EPOCH).ok())
        .map(|d| d.as_millis() as u64)
        .unwrap_or(0);
    Some(Infos {
        dossier: m.is_dir(),
        taille: m.len(),
        modif,
    })
}

/// Octets d'un fichier (rendus tels quels à la page, sans conversion).
#[tauri::command]
fn lire(app: AppHandle, chemin: String) -> Result<Response, String> {
    fs::read(permis(&app, &chemin)?).map(Response::new).map_err(texte)
}

/// Écrit un fichier : le chemin est dans l'en-tête « chemin », les octets dans le corps.
/// Écriture dans un fichier temporaire à côté, puis remplacement : un fichier n'est jamais à moitié écrit.
#[tauri::command]
fn ecrire(app: AppHandle, request: Request<'_>) -> Result<(), String> {
    let brut = request
        .headers()
        .get("chemin")
        .and_then(|v| v.to_str().ok())
        .ok_or("chemin manquant")?;
    let chemin = percent_decode_str(brut).decode_utf8().map_err(texte)?.into_owned();
    let InvokeBody::Raw(octets) = request.body() else {
        return Err("contenu attendu en octets".into());
    };
    let p = permis(&app, &chemin)?;
    if chemins::est_racine(&racine(&app)?, &p) {
        return Err("le dossier « Glacis » n'est pas un fichier".into());
    }
    let nom = p
        .file_name()
        .map(|n| n.to_string_lossy().into_owned())
        .unwrap_or_default();
    let tmp = p.with_file_name(format!(".{nom}.ecriture"));
    fs::write(&tmp, octets).map_err(texte)?;
    if let Err(e) = fs::rename(&tmp, &p) {
        let _ = fs::remove_file(&tmp);
        fs::write(&p, octets).map_err(|e2| format!("{e} / {e2}"))?;
    }
    Ok(())
}

/// Crée UN dossier (son parent doit exister : un dossier « Glacis » absent n'est jamais recréé vide).
#[tauri::command]
fn creer_dossier(app: AppHandle, chemin: String) -> Result<(), String> {
    match fs::create_dir(permis(&app, &chemin)?) {
        Err(e) if e.kind() != ErrorKind::AlreadyExists => Err(texte(e)),
        _ => Ok(()),
    }
}

/// Supprime un fichier ou un dossier du dossier retenu ; jamais le dossier « Glacis » lui-même.
#[tauri::command]
fn supprimer(app: AppHandle, chemin: String, recursif: bool) -> Result<(), String> {
    let p = permis(&app, &chemin)?;
    if chemins::est_racine(&racine(&app)?, &p) {
        return Err("le dossier « Glacis » lui-même ne se supprime pas".into());
    }
    let r = if p.is_dir() {
        if recursif {
            fs::remove_dir_all(&p)
        } else {
            fs::remove_dir(&p)
        }
    } else {
        fs::remove_file(&p)
    };
    r.map_err(texte)
}

/// Le chemin du dossier « Glacis » est retenu dans un petit fichier du profil de l'application
/// (%APPDATA%\\fr.glacis-classe.glacis\\dossier-glacis.txt) : il survit aux redémarrages et aux mises à jour.
fn fichier_dossier(app: &AppHandle) -> Result<PathBuf, String> {
    let d = app.path().app_config_dir().map_err(texte)?;
    fs::create_dir_all(&d).map_err(texte)?;
    Ok(d.join("dossier-glacis.txt"))
}

#[tauri::command]
fn dossier_retenu(app: AppHandle) -> Option<String> {
    let c = fs::read_to_string(fichier_dossier(&app).ok()?).ok()?;
    let c = c.trim();
    (!c.is_empty()).then(|| c.to_string())
}

/// Fenêtre de Windows pour choisir le dossier « Glacis » (souvent dans Google Drive) ; le choix est retenu.
#[tauri::command]
async fn choisir_dossier(app: AppHandle) -> Result<Option<String>, String> {
    let a = app.clone();
    let choix = tauri::async_runtime::spawn_blocking(move || {
        a.dialog()
            .file()
            .set_title("Choisir le dossier « Glacis »")
            .blocking_pick_folder()
    })
    .await
    .map_err(texte)?;
    let chemin = choix
        .and_then(|f| f.into_path().ok())
        .map(|p| p.to_string_lossy().replace('\\', "/"));
    if let Some(c) = &chemin {
        retenir(&app, c)?;
    }
    Ok(chemin)
}

/// Poste équipé avant que l'application retienne le dossier : son chemin n'était connu que de la page (stockage du
/// navigateur intégré), et les applis du Store (adresse appli://) ne le trouvaient pas (« Dossier « Glacis »
/// introuvable », essai 5.2.34). La page le transmet au démarrage ; depuis le lot B de l'audit de sécurité (toutes les
/// commandes de fichiers limitées au dossier retenu), il n'est retenu que si rien ne l'est encore et s'il ressemble à
/// un dossier « Glacis » (chemin complet, sous-dossier « reglages ») : une page piégée ne peut pas faire retenir un
/// autre dossier, et un dossier déjà choisi n'est jamais remplacé par cette voie. Rend vrai si c'est le dossier retenu.
#[tauri::command]
fn reprendre_dossier(app: AppHandle, chemin: String) -> Result<bool, String> {
    if let Some(r) = dossier_retenu(app.clone()) {
        return Ok(chemins::est_racine(Path::new(&r), Path::new(&chemin)));
    }
    let p = Path::new(&chemin);
    if !p.is_absolute() || !p.is_dir() || !p.join("reglages").is_dir() || chemins::dans_racine(p, p).is_err() {
        return Ok(false);
    }
    retenir(&app, &chemin.replace('\\', "/"))?;
    Ok(true)
}

/// Plein écran de la fenêtre : etat vrai / faux, ou bascule ; rend l'état d'avant.
#[tauri::command]
fn plein_ecran(window: WebviewWindow, etat: Option<bool>) -> Result<bool, String> {
    let avant = window.is_fullscreen().map_err(texte)?;
    window.set_fullscreen(etat.unwrap_or(!avant)).map_err(texte)?;
    Ok(avant)
}

fn adresse_web(url: &str) -> Result<Url, String> {
    let u: Url = url.parse().map_err(texte)?;
    if appli::schema_web_permis(u.scheme()) {
        Ok(u)
    } else {
        Err("adresse refusée".into())
    }
}

/// Un site dans le navigateur de l'ordinateur (comptes Google, téléchargements).
#[tauri::command]
fn ouvrir_url(app: AppHandle, url: String) -> Result<(), String> {
    let u = adresse_web(&url)?;
    app.opener().open_url(u.as_str(), None::<&str>).map_err(texte)
}

/// Un site dans une fenêtre de l'application (une par site ; rouverte si elle existe déjà).
#[tauri::command]
async fn ouvrir_site(app: AppHandle, url: String, titre: String) -> Result<(), String> {
    let u = adresse_web(&url)?;
    let label = appli::etiquette_fenetre_site(u.host_str());
    if let Some(w) = app.get_webview_window(&label) {
        let _ = w.unminimize();
        return w.set_focus().map_err(texte);
    }
    WebviewWindowBuilder::new(&app, label, WebviewUrl::External(u))
        .title(format!("{titre} — Glacis"))
        .inner_size(1280.0, 800.0)
        .maximized(true)
        .build()
        .map_err(texte)?;
    Ok(())
}

/// Pont des applis (src/applis/pont-applis.js), intégré à l'application.
const PONT_APPLIS: &str = include_str!("../../../src/applis/pont-applis.js");

/// Licences de Tauri et des bibliothèques Rust de l'application (licences/licences-rust.txt, écrit par
/// build/licences-rust.py avec cargo-about ; le même fichier est installé dans le dossier de l'application).
const LICENCES_RUST: &str = include_str!("../licences/licences-rust.txt");

/// Texte des licences des bibliothèques Rust, pour Réglages › À propos › Licences des composants.
#[tauri::command]
fn licences_rust() -> &'static str {
    LICENCES_RUST
}

fn reponse_appli(statut: u16, type_: &str, corps: Vec<u8>) -> tauri::http::Response<Vec<u8>> {
    tauri::http::Response::builder()
        .status(statut)
        .header("Content-Type", type_)
        .header("Cache-Control", "no-store")
        .header("X-Content-Type-Options", "nosniff")
        .body(corps)
        .unwrap_or_else(|_| tauri::http::Response::new(Vec::new()))
}

/// Adresse appli://localhost/<appli>/<fichier> : un fichier du dossier « Glacis/Applis ».
/// Refusés : « . » et « .. », lecteurs (« C: »), fichiers cachés, le dossier « donnees » d'une appli, et tout
/// ce qui sortirait du dossier « Applis » (vérifié sur le chemin réel, liens compris).
fn servir_appli(app: &AppHandle, uri_chemin: &str) -> tauri::http::Response<Vec<u8>> {
    const TEXTE: &str = "text/plain; charset=utf-8";
    let chemin = percent_decode_str(uri_chemin).decode_utf8_lossy().into_owned();
    if chemin == "/_ma-classe/pont.js" {
        return reponse_appli(200, "text/javascript; charset=utf-8", PONT_APPLIS.as_bytes().to_vec());
    }
    let Some(dossier) = dossier_retenu(app.clone()) else {
        return reponse_appli(404, TEXTE, "Dossier « Glacis » introuvable".into());
    };
    let racine = PathBuf::from(dossier).join("Applis");
    let parts = appli::parties_du_chemin(&chemin);
    if parts.is_empty() {
        return reponse_appli(404, TEXTE, "Appli introuvable".into());
    }
    if appli::acces_refuse(&parts) {
        return reponse_appli(403, TEXTE, "Accès refusé".into());
    }
    let mut p = racine.clone();
    for x in &parts {
        p.push(x);
    }
    if p.is_dir() {
        p.push("index.html");
    }
    match (fs::canonicalize(&racine), fs::canonicalize(&p)) {
        (Ok(r), Ok(c)) if c.starts_with(&r) && c.is_file() => match fs::read(&c) {
            Ok(o) => reponse_appli(200, appli::type_fichier(&c), o),
            Err(_) => reponse_appli(404, TEXTE, "Fichier illisible".into()),
        },
        _ => reponse_appli(404, TEXTE, "Fichier introuvable".into()),
    }
}

/// Clé publique des mises à jour (la clé privée n'est que dans le secret TAURI_SIGNING_PRIVATE_KEY de ma-classe-versions).
const CLE_MAJ: &str = "dW50cnVzdGVkIGNvbW1lbnQ6IG1pbmlzaWduIHB1YmxpYyBrZXk6IEJBMUYyOUYwQTU4RUMwNDMKUldSRHdJNmw4Q2tmdWw0SkQ5VEx4Z3MrRnQ1SXJET3pOejhQbjNTVCs2YUpTQzJ3VzFWNTk4a04K";

fn texte_b64(s: &str) -> Result<String, String> {
    String::from_utf8(STANDARD.decode(s.trim()).map_err(texte)?).map_err(texte)
}

fn entete(request: &Request<'_>, nom: &str) -> Result<String, String> {
    let brut = request
        .headers()
        .get(nom)
        .and_then(|v| v.to_str().ok())
        .ok_or(format!("{nom} manquant"))?;
    Ok(percent_decode_str(brut).decode_utf8().map_err(texte)?.into_owned())
}

/// Installe une nouvelle version téléchargée par la page : signature vérifiée (sinon refus), installateur écrit dans
/// le dossier temporaire puis lancé en mode « passif » (barre de progression, pas de questions) avec relance de
/// Glacis, comme le module de mise à jour de Tauri (/P /UPDATE /R) ; l'application se ferme aussitôt.
#[tauri::command]
fn installer_paquet(app: AppHandle, request: Request<'_>) -> Result<(), String> {
    let signature = entete(&request, "signature")?;
    let version = entete(&request, "version")?;
    // chiffres et points, et un suffixe d'essai (« 6.0.0-beta.3 ») : rien qui puisse sortir du dossier temporaire
    if !chemins::version_installable(&version) {
        return Err("numéro de version invalide".into());
    }
    let InvokeBody::Raw(octets) = request.body() else {
        return Err("installateur attendu en octets".into());
    };
    let cle = PublicKey::decode(&texte_b64(CLE_MAJ)?).map_err(texte)?;
    let sig = Signature::decode(&texte_b64(&signature)?).map_err(texte)?;
    cle.verify(octets, &sig, true)
        .map_err(|e| format!("signature refusée ({e}) : installateur non installé"))?;
    // la version vient du commentaire signé (nom du fichier signé), pas de ce que dit la page : pas de retour en arrière
    let signee = chemins::version_signee(sig.trusted_comment())
        .ok_or("installateur sans numéro de version signé : non installé")?;
    let courante = chemins::numeros(&app.package_info().version.to_string()).unwrap_or_default();
    if chemins::plus_ancienne(&signee, &courante) {
        return Err(format!(
            "installateur plus ancien ({signee}) que l'application ({}) : non installé",
            app.package_info().version
        ));
    }
    let p = std::env::temp_dir().join(format!("Glacis_{version}_x64-setup.exe"));
    fs::write(&p, octets).map_err(texte)?;
    std::process::Command::new(&p)
        .args(["/P", "/UPDATE", "/R"])
        .spawn()
        .map_err(texte)?;
    app.exit(0);
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        // une seule « Glacis » ouverte : un 2e lancement ramène la fenêtre déjà ouverte
        .plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            if let Some(w) = app.get_webview_window("main") {
                let _ = w.unminimize();
                let _ = w.set_focus();
            }
        }))
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_opener::init())
        // applis du dossier « Glacis/Applis » (module Applis de la page)
        .register_uri_scheme_protocol("appli", |ctx, requete| {
            servir_appli(ctx.app_handle(), requete.uri().path())
        })
        .invoke_handler(tauri::generate_handler![
            lister,
            infos,
            lire,
            ecrire,
            creer_dossier,
            supprimer,
            choisir_dossier,
            dossier_retenu,
            reprendre_dossier,
            plein_ecran,
            ouvrir_url,
            ouvrir_site,
            installer_paquet,
            licences_rust
        ])
        .run(tauri::generate_context!())
        .expect("impossible de lancer Glacis");
}
