//! Ma classe — application de bureau (Tauri 2).
//! La page (tauri/www/index.html, construite par build/construire-appli.py) est la même que dans le
//! navigateur. Ce fichier ne fait que ce qu'une page ne peut pas faire seule :
//!  · lire et écrire dans le dossier « Ma classe » choisi une fois (son chemin est retenu par la page,
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
//!  · servir les applis HTML du dossier « Ma classe/Applis » à l'adresse appli:// (http://appli.localhost/ sous
//!    Windows), avec le pont /_ma-classe/pont.js (src/applis/pont-applis.js) ; jamais leurs dossiers « donnees »,
//!    que chaque appli ne lit et n'écrit que par le pont, pour elle seule (module Applis de la page).
//! Les fenêtres de sites n'ont accès à aucune de ces commandes (capabilities/default.json : « main » seule) ; les
//! applis, d'une autre origine (appli.localhost) et dans un cadre « sandbox », non plus.

use percent_encoding::percent_decode_str;
use serde::Serialize;
use std::{fs, io::ErrorKind, path::{Path, PathBuf}, time::UNIX_EPOCH};
use tauri::{
    ipc::{InvokeBody, Request, Response},
    AppHandle, Manager, Url, WebviewUrl, WebviewWindow, WebviewWindowBuilder,
};
use tauri_plugin_dialog::DialogExt;
use tauri_plugin_opener::OpenerExt;
use base64::{engine::general_purpose::STANDARD, Engine};
use minisign_verify::{PublicKey, Signature};

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

/// Contenu d'un dossier (noms et nature).
#[tauri::command]
fn lister(chemin: String) -> Result<Vec<Entree>, String> {
    let mut v = Vec::new();
    for e in fs::read_dir(&chemin).map_err(texte)? {
        let e = e.map_err(texte)?;
        let dossier = e.path().is_dir();
        v.push(Entree { nom: e.file_name().to_string_lossy().into_owned(), dossier });
    }
    Ok(v)
}

/// Nature, taille et date d'un fichier ou d'un dossier ; rien s'il n'existe pas.
#[tauri::command]
fn infos(chemin: String) -> Option<Infos> {
    let m = fs::metadata(&chemin).ok()?;
    let modif = m
        .modified()
        .ok()
        .and_then(|t| t.duration_since(UNIX_EPOCH).ok())
        .map(|d| d.as_millis() as u64)
        .unwrap_or(0);
    Some(Infos { dossier: m.is_dir(), taille: m.len(), modif })
}

/// Octets d'un fichier (rendus tels quels à la page, sans conversion).
#[tauri::command]
fn lire(chemin: String) -> Result<Response, String> {
    fs::read(&chemin).map(Response::new).map_err(texte)
}

/// Écrit un fichier : le chemin est dans l'en-tête « chemin », les octets dans le corps.
/// Écriture dans un fichier temporaire à côté, puis remplacement : un fichier n'est jamais à moitié écrit.
#[tauri::command]
fn ecrire(request: Request<'_>) -> Result<(), String> {
    let brut = request
        .headers()
        .get("chemin")
        .and_then(|v| v.to_str().ok())
        .ok_or("chemin manquant")?;
    let chemin = percent_decode_str(brut).decode_utf8().map_err(texte)?.into_owned();
    let InvokeBody::Raw(octets) = request.body() else {
        return Err("contenu attendu en octets".into());
    };
    let p = PathBuf::from(&chemin);
    let nom = p.file_name().map(|n| n.to_string_lossy().into_owned()).unwrap_or_default();
    let tmp = p.with_file_name(format!(".{nom}.ecriture"));
    fs::write(&tmp, octets).map_err(texte)?;
    if let Err(e) = fs::rename(&tmp, &p) {
        let _ = fs::remove_file(&tmp);
        fs::write(&p, octets).map_err(|e2| format!("{e} / {e2}"))?;
    }
    Ok(())
}

/// Crée UN dossier (son parent doit exister : un dossier « Ma classe » absent n'est jamais recréé vide).
#[tauri::command]
fn creer_dossier(chemin: String) -> Result<(), String> {
    match fs::create_dir(&chemin) {
        Err(e) if e.kind() != ErrorKind::AlreadyExists => Err(texte(e)),
        _ => Ok(()),
    }
}

#[tauri::command]
fn supprimer(chemin: String, recursif: bool) -> Result<(), String> {
    let p = PathBuf::from(&chemin);
    let r = if p.is_dir() {
        if recursif { fs::remove_dir_all(&p) } else { fs::remove_dir(&p) }
    } else {
        fs::remove_file(&p)
    };
    r.map_err(texte)
}

/// Le chemin du dossier « Ma classe » est retenu dans un petit fichier du profil de l'application
/// (%APPDATA%\\fr.franckvarault.maclasse\\dossier-ma-classe.txt) : il survit aux redémarrages et aux mises à jour.
fn fichier_dossier(app: &AppHandle) -> Result<PathBuf, String> {
    let d = app.path().app_config_dir().map_err(texte)?;
    fs::create_dir_all(&d).map_err(texte)?;
    Ok(d.join("dossier-ma-classe.txt"))
}

#[tauri::command]
fn dossier_retenu(app: AppHandle) -> Option<String> {
    let c = fs::read_to_string(fichier_dossier(&app).ok()?).ok()?;
    let c = c.trim();
    (!c.is_empty()).then(|| c.to_string())
}

/// Poste équipé avant que l'application retienne le dossier : son chemin n'était connu que de la page (stockage du
/// navigateur intégré), et les applis du Store (adresse appli://) ne le trouvaient pas (« Dossier « Ma classe »
/// introuvable »). La page le transmet au démarrage ; il n'est retenu que si rien ne l'est encore et si c'est bien un
/// dossier existant : un dossier déjà choisi n'est jamais remplacé par cette voie.
#[tauri::command]
fn reprendre_dossier(app: AppHandle, chemin: String) -> Result<bool, String> {
    if dossier_retenu(app.clone()).is_some() || !Path::new(&chemin).is_dir() {
        return Ok(false);
    }
    fs::write(fichier_dossier(&app)?, chemin.replace('\\', "/")).map_err(texte)?;
    Ok(true)
}

/// Fenêtre de Windows pour choisir le dossier « Ma classe » (souvent dans Google Drive) ; le choix est retenu.
#[tauri::command]
async fn choisir_dossier(app: AppHandle) -> Result<Option<String>, String> {
    let a = app.clone();
    let choix = tauri::async_runtime::spawn_blocking(move || {
        a.dialog().file().set_title("Choisir le dossier « Ma classe »").blocking_pick_folder()
    })
    .await
    .map_err(texte)?;
    let chemin = choix
        .and_then(|f| f.into_path().ok())
        .map(|p| p.to_string_lossy().replace('\\', "/"));
    if let Some(c) = &chemin {
        fs::write(fichier_dossier(&app)?, c).map_err(texte)?;
    }
    Ok(chemin)
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
    if matches!(u.scheme(), "http" | "https") { Ok(u) } else { Err("adresse refusée".into()) }
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
    let hote: String = u
        .host_str()
        .unwrap_or("site")
        .chars()
        .map(|c| if c.is_ascii_alphanumeric() { c } else { '-' })
        .collect();
    let label = format!("site-{hote}");
    if let Some(w) = app.get_webview_window(&label) {
        let _ = w.unminimize();
        return w.set_focus().map_err(texte);
    }
    WebviewWindowBuilder::new(&app, label, WebviewUrl::External(u))
        .title(format!("{titre} — Ma classe"))
        .inner_size(1280.0, 800.0)
        .maximized(true)
        .build()
        .map_err(texte)?;
    Ok(())
}

/// Pont des applis (src/applis/pont-applis.js), intégré à l'application.
const PONT_APPLIS: &str = include_str!("../../../src/applis/pont-applis.js");

fn reponse_appli(statut: u16, type_: &str, corps: Vec<u8>) -> tauri::http::Response<Vec<u8>> {
    tauri::http::Response::builder()
        .status(statut)
        .header("Content-Type", type_)
        .header("Cache-Control", "no-store")
        .header("X-Content-Type-Options", "nosniff")
        .body(corps)
        .unwrap_or_else(|_| tauri::http::Response::new(Vec::new()))
}

fn type_fichier(p: &Path) -> &'static str {
    let ext = p.extension().map(|e| e.to_string_lossy().to_lowercase()).unwrap_or_default();
    match ext.as_str() {
        "html" | "htm" => "text/html; charset=utf-8",
        "js" | "mjs" => "text/javascript; charset=utf-8",
        "css" => "text/css; charset=utf-8",
        "json" => "application/json; charset=utf-8",
        "txt" | "md" => "text/plain; charset=utf-8",
        "svg" => "image/svg+xml",
        "png" => "image/png",
        "jpg" | "jpeg" => "image/jpeg",
        "gif" => "image/gif",
        "webp" => "image/webp",
        "avif" => "image/avif",
        "ico" => "image/x-icon",
        "mp3" => "audio/mpeg",
        "wav" => "audio/wav",
        "ogg" | "oga" => "audio/ogg",
        "m4a" => "audio/mp4",
        "webm" => "audio/webm",
        "mp4" => "video/mp4",
        "woff" => "font/woff",
        "woff2" => "font/woff2",
        "ttf" => "font/ttf",
        "otf" => "font/otf",
        "pdf" => "application/pdf",
        "wasm" => "application/wasm",
        _ => "application/octet-stream",
    }
}

/// Adresse appli://localhost/<appli>/<fichier> : un fichier du dossier « Ma classe/Applis ».
/// Refusés : « . » et « .. », lecteurs (« C: »), fichiers cachés, le dossier « donnees » d'une appli, et tout
/// ce qui sortirait du dossier « Applis » (vérifié sur le chemin réel, liens compris).
fn servir_appli(app: &AppHandle, uri_chemin: &str) -> tauri::http::Response<Vec<u8>> {
    const TEXTE: &str = "text/plain; charset=utf-8";
    let chemin = percent_decode_str(uri_chemin).decode_utf8_lossy().into_owned();
    if chemin == "/_ma-classe/pont.js" {
        return reponse_appli(200, "text/javascript; charset=utf-8", PONT_APPLIS.as_bytes().to_vec());
    }
    let Some(dossier) = dossier_retenu(app.clone()) else {
        return reponse_appli(404, TEXTE, "Dossier « Ma classe » introuvable".into());
    };
    let racine = PathBuf::from(dossier).join("Applis");
    let parts: Vec<&str> = chemin.split('/').filter(|s| !s.is_empty()).collect();
    if parts.is_empty() {
        return reponse_appli(404, TEXTE, "Appli introuvable".into());
    }
    let refuse = parts.iter().any(|x| *x == "." || *x == ".." || x.starts_with('.') || x.contains('\\') || x.contains(':'));
    if refuse || (parts.len() > 1 && parts[1].eq_ignore_ascii_case("donnees")) {
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
            Ok(o) => reponse_appli(200, type_fichier(&c), o),
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
    let brut = request.headers().get(nom).and_then(|v| v.to_str().ok()).ok_or(format!("{nom} manquant"))?;
    Ok(percent_decode_str(brut).decode_utf8().map_err(texte)?.into_owned())
}

/// Installe une nouvelle version téléchargée par la page : signature vérifiée (sinon refus), installateur écrit dans
/// le dossier temporaire puis lancé en mode « passif » (barre de progression, pas de questions) avec relance de
/// Ma classe, comme le module de mise à jour de Tauri (/P /UPDATE /R) ; l'application se ferme aussitôt.
#[tauri::command]
fn installer_paquet(app: AppHandle, request: Request<'_>) -> Result<(), String> {
    let signature = entete(&request, "signature")?;
    let version = entete(&request, "version")?;
    if version.is_empty() || !version.chars().all(|c| c.is_ascii_digit() || c == '.') {
        return Err("numéro de version invalide".into());
    }
    let InvokeBody::Raw(octets) = request.body() else {
        return Err("installateur attendu en octets".into());
    };
    let cle = PublicKey::decode(&texte_b64(CLE_MAJ)?).map_err(texte)?;
    let sig = Signature::decode(&texte_b64(&signature)?).map_err(texte)?;
    cle.verify(octets, &sig, true).map_err(|e| format!("signature refusée ({e}) : installateur non installé"))?;
    let p = std::env::temp_dir().join(format!("Ma-classe_{version}_x64-setup.exe"));
    fs::write(&p, octets).map_err(texte)?;
    std::process::Command::new(&p).args(["/P", "/UPDATE", "/R"]).spawn().map_err(texte)?;
    app.exit(0);
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        // une seule « Ma classe » ouverte : un 2e lancement ramène la fenêtre déjà ouverte
        .plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            if let Some(w) = app.get_webview_window("main") {
                let _ = w.unminimize();
                let _ = w.set_focus();
            }
        }))
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_opener::init())
        // applis du dossier « Ma classe/Applis » (module Applis de la page)
        .register_uri_scheme_protocol("appli", |ctx, requete| servir_appli(ctx.app_handle(), requete.uri().path()))
        .invoke_handler(tauri::generate_handler![
            lister, infos, lire, ecrire, creer_dossier, supprimer, choisir_dossier, dossier_retenu, reprendre_dossier, plein_ecran, ouvrir_url, ouvrir_site,
            installer_paquet
        ])
        .run(tauri::generate_context!())
        .expect("impossible de lancer Ma classe");
}
