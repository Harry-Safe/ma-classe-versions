//! Règles de l'application qui ne dépendent pas de Tauri : le type des fichiers servis aux applis (adresse
//! appli://), les chemins qu'une appli n'a pas le droit de demander, le nom des fenêtres de sites et les adresses
//! web permises. Sorties de `lib.rs` au lot 14 de la restructuration (26 novembre 2026) pour être testées seules,
//! comme `chemins.rs` : `cd src-tauri && rustc --edition 2021 --test src/appli.rs -o /tmp/appli && /tmp/appli`.
//! Aucun changement de comportement : le code est celui qui était dans `lib.rs`.

use std::path::Path;

/// Type MIME d'un fichier d'appli, d'après son extension (sans tenir compte des majuscules).
pub fn type_fichier(p: &Path) -> &'static str {
    let ext = p
        .extension()
        .map(|e| e.to_string_lossy().to_lowercase())
        .unwrap_or_default();
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

/// Les morceaux non vides d'un chemin d'adresse appli:// (« /echecs/index.html » → [« echecs », « index.html »]).
pub fn parties_du_chemin(chemin: &str) -> Vec<&str> {
    chemin.split('/').filter(|s| !s.is_empty()).collect()
}

/// Vrai si une appli n'a pas le droit de demander ce chemin : « . » et « .. », fichiers cachés, barres inverses,
/// lecteurs (« C: »), et le dossier « donnees » d'une appli (que seul le pont lit et écrit, pour elle seule).
pub fn acces_refuse(parties: &[&str]) -> bool {
    let refuse = parties
        .iter()
        .any(|x| *x == "." || *x == ".." || x.starts_with('.') || x.contains('\\') || x.contains(':'));
    refuse || (parties.len() > 1 && parties[1].eq_ignore_ascii_case("donnees"))
}

/// Nom de la fenêtre d'un site : une par site (« www.google.fr » → « site-www-google-fr »), rouverte si elle existe déjà.
pub fn etiquette_fenetre_site(hote: Option<&str>) -> String {
    let hote: String = hote
        .unwrap_or("site")
        .chars()
        .map(|c| if c.is_ascii_alphanumeric() { c } else { '-' })
        .collect();
    format!("site-{hote}")
}

/// Seules les adresses « http » et « https » s'ouvrent (jamais « file », « javascript »…).
pub fn schema_web_permis(schema: &str) -> bool {
    matches!(schema, "http" | "https")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn types_des_fichiers_servis() {
        assert_eq!(type_fichier(Path::new("index.html")), "text/html; charset=utf-8");
        assert_eq!(type_fichier(Path::new("a/b/page.HTM")), "text/html; charset=utf-8");
        assert_eq!(type_fichier(Path::new("app.mjs")), "text/javascript; charset=utf-8");
        assert_eq!(type_fichier(Path::new("style.css")), "text/css; charset=utf-8");
        assert_eq!(
            type_fichier(Path::new("donnees.json")),
            "application/json; charset=utf-8"
        );
        assert_eq!(type_fichier(Path::new("LISEZ-MOI.md")), "text/plain; charset=utf-8");
        assert_eq!(type_fichier(Path::new("icone.svg")), "image/svg+xml");
        assert_eq!(type_fichier(Path::new("PHOTO.PNG")), "image/png");
        assert_eq!(type_fichier(Path::new("photo.jpeg")), "image/jpeg");
        assert_eq!(type_fichier(Path::new("police.woff2")), "font/woff2");
        assert_eq!(type_fichier(Path::new("moteur.wasm")), "application/wasm");
    }

    #[test]
    fn type_inconnu_ou_sans_extension() {
        assert_eq!(type_fichier(Path::new("fichier.xyz")), "application/octet-stream");
        assert_eq!(type_fichier(Path::new("Makefile")), "application/octet-stream");
        assert_eq!(type_fichier(Path::new("")), "application/octet-stream");
    }

    #[test]
    fn parties_sans_morceaux_vides() {
        assert_eq!(parties_du_chemin("/echecs/index.html"), vec!["echecs", "index.html"]);
        assert_eq!(parties_du_chemin("//a///b/"), vec!["a", "b"]);
        assert_eq!(parties_du_chemin("/"), Vec::<&str>::new());
        assert_eq!(parties_du_chemin(""), Vec::<&str>::new());
    }

    #[test]
    fn chemins_permis_a_une_appli() {
        assert!(!acces_refuse(&["echecs"]));
        assert!(!acces_refuse(&["echecs", "index.html"]));
        assert!(!acces_refuse(&["echecs", "images", "roi.png"]));
        // seul le deuxième morceau nomme le dossier de données d'une appli
        assert!(!acces_refuse(&["donnees", "index.html"]));
        assert!(!acces_refuse(&["echecs", "donnees-autres"]));
    }

    #[test]
    fn chemins_refuses_a_une_appli() {
        assert!(acces_refuse(&[".."]));
        assert!(acces_refuse(&["echecs", ".."]));
        assert!(acces_refuse(&["."]));
        assert!(acces_refuse(&["echecs", ".cache"]));
        assert!(acces_refuse(&[".git", "config"]));
        assert!(acces_refuse(&["C:"]));
        assert!(acces_refuse(&["echecs", "a:b"]));
        assert!(acces_refuse(&["echecs", "a\\b"]));
        assert!(acces_refuse(&["echecs", "donnees"]));
        assert!(acces_refuse(&["echecs", "DONNEES", "echecs.json"]));
        assert!(acces_refuse(&["echecs", "Donnees"]));
    }

    #[test]
    fn nom_de_la_fenetre_d_un_site() {
        assert_eq!(etiquette_fenetre_site(Some("www.google.fr")), "site-www-google-fr");
        assert_eq!(
            etiquette_fenetre_site(Some("solaire.eduplateforme.com")),
            "site-solaire-eduplateforme-com"
        );
        assert_eq!(etiquette_fenetre_site(Some("localhost")), "site-localhost");
        assert_eq!(etiquette_fenetre_site(None), "site-site");
        // deux sites différents ne partagent jamais le même nom
        assert_ne!(
            etiquette_fenetre_site(Some("a.fr")),
            etiquette_fenetre_site(Some("b.fr"))
        );
    }

    #[test]
    fn seules_les_adresses_web_s_ouvrent() {
        assert!(schema_web_permis("http"));
        assert!(schema_web_permis("https"));
        assert!(!schema_web_permis("file"));
        assert!(!schema_web_permis("javascript"));
        assert!(!schema_web_permis("ftp"));
        assert!(!schema_web_permis(""));
    }
}
