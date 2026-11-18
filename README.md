# ma-classe-versions — site de Glacis – Ma classe

Fabrique et source du site public **https://glacis-classe.fr** (Cloudflare Pages) de **Glacis – Ma classe**, logiciel de
classe conçu par Franck VARAULT (appelé « Ma classe » jusqu'au 18 novembre 2026). Aucune donnée d'élève : seulement les
éditions construites, leurs empreintes, l'application Windows et des fiches signées.

« Glacis – Ma classe » est conçu et développé par Franck VARAULT, enseignant de CP : conception pédagogique, choix des fonctionnalités, architecture, tests en classe et validation de chaque version. Le code a été écrit avec l’aide d’assistants de programmation par IA, sous sa direction.

Consignes de contribution : [AGENTS.md](AGENTS.md). Fonctionnement détaillé (formats, action de publication, règles,
vérifications, clés) : **[DOCUMENTATION.md](DOCUMENTATION.md)**.

- `index.html`, `icone.svg`, `_headers` : la page de présentation de Glacis et les en-têtes du site ;
- `entrees/<canal>.json` : version, date, nouveautés, empreinte SHA-256 de chaque fichier (écrit par `build/publier-version.py` du dépôt source) ;
- `stable/`, `essai/` : les pages « Glacis.html » et « Glacis - Remplaçant.html » de chaque canal ;
- `appli/` : l'application Windows (`latest.json` ; `appli/essai/` pour les versions d'essai) et `coquille/<canal>/` (la coquille Tauri), écrits par `build/publier-appli.py` ; l'action fabrique l'installateur à partir de la coquille et de la page du canal (`outils/fabriquer-appli.py`) et le signe (`outils/signer-appli.py`) ;
- `applis/` : le Store des applis (entrées et paquets, écrits par `outils/publier.py` du dépôt des applis) ;
- à chaque envoi sur `main`, `.github/workflows/publier.yml` vérifie les empreintes, signe `versions.json` et `applis.json` (`outils/signer.py`), signe les installateurs, puis met le site en ligne sur glacis-classe.fr (`wrangler pages deploy`, outil fixé dans `outils/deploiement/`).

## Licence

© 2026 Franck VARAULT.

- **Glacis – Ma classe** (pages `stable/` et `essai/`, application Windows, coquille, scripts de ce dépôt) : logiciel libre
  sous licence **GNU GPL version 3 ou ultérieure** (`GPL-3.0-or-later`, texte complet dans `LICENSE`). Chacun peut
  l'utiliser, l'étudier, le modifier et le redistribuer, en gardant le nom de l'auteur et en partageant ses
  modifications sous la même licence. Aucune garantie. Composants tiers intégrés aux pages (pdf.js, polices Glacis
  Lecture — d'après Andika — et Marelle, OpenMoji, données des cartes, Tauri) : chacun sous sa propre licence, citée
  dans Réglages › À propos.
- **Documentation** : licence CC BY-SA 4.0.
- **Applis du Store** (`applis/`) : chacune sous sa propre licence, indiquée dans son paquet (Échecs : GPL-3.0-or-later).
