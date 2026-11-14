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

/// Version d'un installateur, lue dans le nom de fichier du commentaire signé (« timestamp:…\tfile:Ma-classe_5.2.33_x64-setup-essai.exe »).
pub fn version_signee(commentaire: &str) -> Option<Vec<u64>> {
    let fichier = commentaire.split('\t').find_map(|x| x.strip_prefix("file:"))?;
    let v = fichier.split('_').find(|x| !x.is_empty() && x.chars().all(|c| c.is_ascii_digit() || c == '.') && x.contains('.'))?;
    v.split('.').map(|n| n.parse::<u64>().ok()).collect()
}

/// « 5.2.33 » → [5, 2, 33] ; comparaison nombre par nombre (5.2.10 > 5.2.9).
pub fn numeros(v: &str) -> Option<Vec<u64>> {
    v.trim().split('.').map(|n| n.parse::<u64>().ok()).collect()
}

pub fn plus_ancienne(a: &[u64], b: &[u64]) -> bool {
    let n = a.len().max(b.len());
    for i in 0..n {
        let (x, y) = (a.get(i).copied().unwrap_or(0), b.get(i).copied().unwrap_or(0));
        if x != y {
            return x < y;
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
        assert_eq!(version_signee("timestamp:1731500000\tfile:Ma-classe_5.2.33_x64-setup-essai.exe"), Some(vec![5, 2, 33]));
        assert_eq!(version_signee("timestamp:1731500000\tfile:Ma-classe_5.2.0_x64-setup.exe"), Some(vec![5, 2, 0]));
        assert_eq!(version_signee("timestamp:1731500000"), None);
        assert_eq!(numeros("5.2.33"), Some(vec![5, 2, 33]));
        assert!(plus_ancienne(&[5, 2, 9], &[5, 2, 10]));
        assert!(!plus_ancienne(&[5, 2, 33], &[5, 2, 33]));
        assert!(!plus_ancienne(&[5, 3], &[5, 2, 33]));
        assert!(plus_ancienne(&[5, 2], &[5, 2, 1]));
    }
}

// essai de fabrication seulement (branche claude/fabrication-node24) : oblige une fabrication complète
