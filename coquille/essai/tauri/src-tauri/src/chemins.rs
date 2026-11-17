//! Chemins permis aux commandes de fichiers (lot B de l'audit de sécurité, 13 novembre 2026).
//!
//! La page ne peut lire, écrire, lister ou supprimer que DANS le dossier « Ma classe » retenu par l'application
//! (choisi dans la fenêtre de Windows). Même si un fichier piégé arrivait à exécuter du code dans la page, il ne
//! pourrait rien toucher d'autre sur l'ordinateur.
//!
//! Deux contrôles :
//!  1. sur le texte du chemin : absolu, sans « .. » (un « . » au milieu est sans effet), sans « : » après le lecteur (flux cachés de Windows),
//!     et commençant par le dossier retenu (sans tenir compte des majuscules sous Windows) ;
//!  2. sur le disque : le plus proche parent existant, une fois les liens résolus, reste dans le dossier retenu
//!     (un lien ou une jonction qui mènerait ailleurs est refusé). Si le système de fichiers ne sait pas résoudre
//!     les chemins (certains lecteurs réseau ou virtuels), le contrôle 1 suffit.
//!
//! Module sans dépendance : testé seul par `rustc --test src/chemins.rs` (voir tauri/LISEZ-MOI.md).

use std::fs;
use std::path::{Component, Path, PathBuf};

/// Les morceaux d'un chemin absolu, comparables entre eux ; erreur s'il n'est pas absolu ou s'il contient « .. »
/// (un « . » au milieu est retiré par Rust lui-même, comme par Windows).
fn morceaux(p: &Path) -> Result<Vec<String>, String> {
    if !p.is_absolute() {
        return Err("chemin refusé : il doit être complet".into());
    }
    let mut v = Vec::new();
    for c in p.components() {
        match c {
            Component::Prefix(x) => v.push(comparable(&x.as_os_str().to_string_lossy())),
            Component::RootDir => v.push("/".into()),
            Component::Normal(x) => {
                let s = x.to_string_lossy();
                if cfg!(windows) && s.contains(':') {
                    return Err("chemin refusé : « : » interdit dans un nom".into());
                }
                v.push(comparable(&s));
            }
            Component::CurDir | Component::ParentDir => return Err("chemin refusé : « . » ou « .. »".into()),
        }
    }
    Ok(v)
}

/// Sous Windows, les noms ne tiennent pas compte des majuscules ; ailleurs, si.
fn comparable(s: &str) -> String {
    if cfg!(windows) { s.to_lowercase() } else { s.to_string() }
}

/// Le chemin `cible` est-il le dossier `racine` lui-même ? (comparaison du texte, après contrôle)
pub fn est_racine(racine: &Path, cible: &Path) -> bool {
    matches!((morceaux(racine), morceaux(cible)), (Ok(a), Ok(b)) if a == b)
}

/// Le plus proche parent existant (ou la cible elle-même), sans sortir au-dessus de la racine du disque.
fn parent_existant(p: &Path) -> Option<&Path> {
    let mut q = Some(p);
    while let Some(x) = q {
        if fs::symlink_metadata(x).is_ok() {
            return Some(x);
        }
        q = x.parent();
    }
    None
}

/// Rend `cible` si elle est dans `racine` (ou est `racine`), sinon une erreur. `racine` doit exister.
pub fn dans_racine(racine: &Path, cible: &Path) -> Result<PathBuf, String> {
    let r = morceaux(racine)?;
    let c = morceaux(cible)?;
    if c.len() < r.len() || c[..r.len()] != r[..] {
        return Err("chemin refusé : hors du dossier « Ma classe »".into());
    }
    if !racine.is_dir() {
        return Err("dossier « Ma classe » introuvable".into());
    }
    if let Ok(vraie) = fs::canonicalize(racine) {
        if let Some(p) = parent_existant(cible) {
            if let Ok(vrai) = fs::canonicalize(p) {
                if !vrai.starts_with(&vraie) {
                    return Err("chemin refusé : un lien mène hors du dossier « Ma classe »".into());
                }
            }
        }
    }
    Ok(cible.to_path_buf())
}

/// Numéro de version façon « versionnage sémantique » (docs/VERSIONS_ET_PUBLICATION.md § 1) : nombres, et un suffixe
/// de pré-version pour les essais (« 6.0.0-beta.3 » → n = [6, 0, 0], pre = ["beta", "3"]).
/// Même ordre que MiseAJour.comparer (page) et build/numeros.py : 5.2.51 < 6.0.0-beta.2 < 6.0.0-beta.10 < 6.0.0-rc.1 < 6.0.0.
#[derive(Debug, Default, PartialEq, Eq, Clone)]
pub struct Numero {
    pub n: Vec<u64>,
    pub pre: Vec<String>,
}

impl std::fmt::Display for Numero {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let n = self.n.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(".");
        if self.pre.is_empty() { write!(f, "{n}") } else { write!(f, "{n}-{}", self.pre.join(".")) }
    }
}

/// Version d'un installateur, lue dans le nom de fichier du commentaire signé
/// (« timestamp:…\tfile:Ma-classe_5.2.33_x64-setup-essai.exe », « …file:Ma-classe_6.0.0-beta.1_x64-setup-essai.exe »).
pub fn version_signee(commentaire: &str) -> Option<Numero> {
    let fichier = commentaire.split('\t').find_map(|x| x.strip_prefix("file:"))?;
    fichier.split('_').find_map(|x| if x.contains('.') && x.starts_with(|c: char| c.is_ascii_digit()) { numeros(x) } else { None })
}

/// « 5.2.33 » → [5, 2, 33] ; « 6.0.0-beta.3 » → [6, 0, 0] et ["beta", "3"] ; un numéro de build (« +42 ») est ignoré.
pub fn numeros(v: &str) -> Option<Numero> {
    let v = v.trim().split('+').next()?;
    let (base, pre) = match v.split_once('-') { Some((b, p)) => (b, Some(p)), None => (v, None) };
    let n = base.split('.').map(|x| x.parse::<u64>().ok()).collect::<Option<Vec<_>>>()?;
    let pre = match pre {
        None => vec![],
        Some(p) => {
            let p: Vec<String> = p.split('.').map(String::from).collect();
            if p.iter().any(|x| x.is_empty() || !x.chars().all(|c| c.is_ascii_alphanumeric())) { return None; }
            p
        }
    };
    Some(Numero { n, pre })
}

/// a est-elle plus ancienne que b ? Nombre par nombre (5.2.10 > 5.2.9, 5.2 = 5.2.0), puis une pré-version passe
/// avant sa version finale, et les pré-versions se comparent morceau par morceau (nombres entre eux, sinon texte).
pub fn plus_ancienne(a: &Numero, b: &Numero) -> bool {
    use std::cmp::Ordering::*;
    let len = a.n.len().max(b.n.len());
    for i in 0..len {
        let (x, y) = (a.n.get(i).copied().unwrap_or(0), b.n.get(i).copied().unwrap_or(0));
        if x != y {
            return x < y;
        }
    }
    match (a.pre.is_empty(), b.pre.is_empty()) {
        (true, _) => return false,
        (false, true) => return true,
        _ => {}
    }
    for i in 0..a.pre.len().max(b.pre.len()) {
        let (p, q) = match (a.pre.get(i), b.pre.get(i)) {
            (None, _) => return true,
            (_, None) => return false,
            (Some(p), Some(q)) => (p, q),
        };
        let o = match (p.parse::<u64>(), q.parse::<u64>()) {
            (Ok(x), Ok(y)) => x.cmp(&y),
            (Ok(_), Err(_)) => Less,
            (Err(_), Ok(_)) => Greater,
            _ => p.cmp(q),
        };
        if o != Equal {
            return o == Less;
        }
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    fn tmp(nom: &str) -> PathBuf {
        let d = std::env::temp_dir().join(format!("mc-chemins-{}-{}", nom, std::process::id()));
        let _ = fs::remove_dir_all(&d);
        fs::create_dir_all(d.join("Ma classe/reglages")).unwrap();
        fs::create_dir_all(d.join("ailleurs")).unwrap();
        fs::write(d.join("ailleurs/secret.txt"), "x").unwrap();
        d
    }

    #[test]
    fn dedans_et_dehors() {
        let d = tmp("base");
        let r = d.join("Ma classe");
        assert!(dans_racine(&r, &r).is_ok(), "la racine elle-même");
        assert!(dans_racine(&r, &r.join("reglages/preferences.json")).is_ok(), "fichier à créer");
        assert!(dans_racine(&r, &r.join("nouveau/sous/dossier/x.json")).is_ok(), "dossiers à créer");
        assert!(dans_racine(&r, &d.join("ailleurs/secret.txt")).is_err(), "voisin");
        assert!(dans_racine(&r, &d.join("Ma classe/../ailleurs/secret.txt")).is_err(), "remontée « .. »");
        assert!(dans_racine(&r, &d.join("Ma classe/./reglages")).is_ok(), "« . » au milieu : sans effet (Rust et Windows l'ignorent)");
        assert!(dans_racine(&r, &d.join("Ma classe 2/x")).is_err(), "nom qui commence pareil");
        assert!(dans_racine(&r, &d).is_err(), "parent");
        assert!(dans_racine(&r, Path::new("reglages/x.json")).is_err(), "chemin relatif");
        assert!(dans_racine(&r, Path::new("/etc/passwd")).is_err(), "système");
        let _ = fs::remove_dir_all(&d);
    }

    #[test]
    fn racine_absente() {
        let d = tmp("absente");
        let r = d.join("Pas là");
        assert!(dans_racine(&r, &r).is_err(), "jamais recréée vide");
        assert!(dans_racine(&r, &r.join("reglages")).is_err());
        let _ = fs::remove_dir_all(&d);
    }

    #[test]
    fn racine_et_separateurs() {
        let d = tmp("racine");
        let r = d.join("Ma classe");
        assert!(est_racine(&r, &r));
        assert!(!est_racine(&r, &r.join("reglages")));
        let texte = format!("{}/reglages/x.json", r.to_string_lossy());
        assert!(dans_racine(&r, Path::new(&texte)).is_ok(), "barres obliques de la page");
        let _ = fs::remove_dir_all(&d);
    }

    #[cfg(unix)]
    #[test]
    fn lien_vers_ailleurs() {
        let d = tmp("lien");
        let r = d.join("Ma classe");
        std::os::unix::fs::symlink(d.join("ailleurs"), r.join("raccourci")).unwrap();
        assert!(dans_racine(&r, &r.join("raccourci/secret.txt")).is_err(), "lien vers un fichier existant");
        assert!(dans_racine(&r, &r.join("raccourci/nouveau.txt")).is_err(), "lien vers un dossier, fichier à créer");
        std::os::unix::fs::symlink(r.join("reglages"), r.join("interne")).unwrap();
        assert!(dans_racine(&r, &r.join("interne/x.json")).is_ok(), "lien qui reste dedans");
        let _ = fs::remove_dir_all(&d);
    }

    #[test]
    fn versions() {
        let v = |s: &str| numeros(s).unwrap();
        assert_eq!(version_signee("timestamp:1731500000\tfile:Ma-classe_5.2.33_x64-setup-essai.exe"), Some(v("5.2.33")));
        assert_eq!(version_signee("timestamp:1731500000\tfile:Ma-classe_5.2.0_x64-setup.exe"), Some(v("5.2.0")));
        assert_eq!(version_signee("timestamp:1731500000\tfile:Ma-classe_6.0.0-beta.1_x64-setup-essai.exe"), Some(v("6.0.0-beta.1")));
        assert_eq!(version_signee("timestamp:1731500000"), None);
        assert_eq!(numeros("5.2.33").map(|x| x.n), Some(vec![5, 2, 33]));
        assert_eq!(numeros("6.0.0-beta.3").map(|x| (x.n, x.pre)), Some((vec![6, 0, 0], vec!["beta".to_string(), "3".to_string()])));
        assert_eq!(numeros("6.0.0-beta.3").unwrap().to_string(), "6.0.0-beta.3");
        assert_eq!(numeros("6.0.0-"), None);
        assert_eq!(numeros("6.0.0-be/ta"), None);
        assert!(plus_ancienne(&v("5.2.9"), &v("5.2.10")));
        assert!(!plus_ancienne(&v("5.2.33"), &v("5.2.33")));
        assert!(!plus_ancienne(&v("5.3"), &v("5.2.33")));
        assert!(plus_ancienne(&v("5.2"), &v("5.2.1")));
        // pré-versions : 5.2.51 < 6.0.0-beta.2 < 6.0.0-beta.10 < 6.0.0-rc.1 < 6.0.0 < 6.0.1 < 6.1.0-beta.1
        let ordre = ["5.2.51", "6.0.0-beta.2", "6.0.0-beta.10", "6.0.0-rc.1", "6.0.0", "6.0.1", "6.1.0-beta.1"];
        for (i, a) in ordre.iter().enumerate() {
            for (j, b) in ordre.iter().enumerate() {
                assert_eq!(plus_ancienne(&v(a), &v(b)), i < j, "{a} / {b}");
            }
        }
        assert!(plus_ancienne(&v("6.0.0-beta"), &v("6.0.0-beta.1")));
        assert!(!plus_ancienne(&v("6.0"), &v("6.0.0")));
    }
}
