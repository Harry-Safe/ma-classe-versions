# ma-classe-versions

Site public des mises à jour de **Ma classe** (logiciel de classe conçu par Franck VARAULT), servi par GitHub Pages.
Aucune donnée d'élève : seulement les éditions construites, leurs empreintes et une fiche signée.

Fonctionnement détaillé (formats, action de publication, règles, vérifications, clés) : **[DOCUMENTATION.md](DOCUMENTATION.md)**.

- `entrees/<canal>.json` : version, date, nouveautés, empreinte SHA-256 de chaque fichier (écrit par `build/publier-version.py` du dépôt Ma classe) ;
- `stable/`, `essai/` : les fichiers « Ma classe.html » et « Ma classe - Remplaçant.html » ;
- `appli/` : l'application Windows (`latest.json` lu par l'application et son installateur ; `appli/essai/` : la version d'essai, lue par l'application réglée sur « d'essai »), écrit par `build/publier-appli.py [--canal essai]` du dépôt Ma classe ; l'action signe l'installateur (`outils/signer-appli.py`, secret `TAURI_SIGNING_PRIVATE_KEY`, sans mot de passe) et met la signature dans `latest.json` du site ;
- à chaque envoi, `.github/workflows/publier.yml` vérifie les empreintes, signe la fiche (`outils/signer.py`, secret `MAJ_CLE_PRIVEE`) et publie `versions.json`.

© 2026 Franck VARAULT. Tous droits réservés.
