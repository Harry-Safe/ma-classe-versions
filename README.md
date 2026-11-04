# ma-classe-versions

Site public des mises à jour de **Ma classe** (logiciel de classe conçu par Franck VARAULT), servi par GitHub Pages.
Aucune donnée d'élève : seulement les éditions construites, leurs empreintes et une fiche signée.

- `entrees/<canal>.json` : version, date, nouveautés, empreinte SHA-256 de chaque fichier (écrit par `build/publier-version.py` du dépôt Ma classe) ;
- `stable/`, `essai/` : les fichiers « Ma classe.html » et « Ma classe - Remplaçant.html » ;
- à chaque envoi, `.github/workflows/publier.yml` vérifie les empreintes, signe la fiche (`outils/signer.py`, secret `MAJ_CLE_PRIVEE`) et publie `versions.json`.

© 2026 Franck VARAULT. Tous droits réservés.
