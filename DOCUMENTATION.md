# Documentation du site des mises à jour

**En bref.** Ce dépôt **public** est le **seul** point de distribution de « Ma classe » (logiciel de classe de Franck
VARAULT). Il contient les éditions construites, leurs fiches, la « coquille » de l'application Windows et l'action qui
**fabrique l'installateur, vérifie, signe et publie** le site `https://harry-safe.github.io/ma-classe-versions/`
(GitHub Pages). Il ne contient **aucune donnée d'élève**, aucun autre code source de l'application que cette coquille
(§ 3 bis), et **aucune clé privée** : les clés de signature vivent seulement dans les secrets
GitHub du dépôt. Seuls Franck (et les assistants qui travaillent avec lui, sur son autorisation) le modifient.

> Le code source et la procédure complète (numéros de version, CHANGELOG, essais, publication pas à pas) sont dans le
> dépôt privé de Ma classe : `docs/VERSIONS_ET_PUBLICATION.md` et `docs/APPLICATION_WINDOWS.md`.
>
> **Numéros** (versionnage sémantique, depuis le 17 novembre 2026) : une version publiée s'écrit `6.0.0` ; les essais
> qui la préparent, `6.0.0-beta.1`, `6.0.0-beta.2`… (affichés « 6.0 · essai 1, 2… »), éventuellement `6.0.0-rc.1`.
> Ordre : `5.2.51 < 6.0.0-beta.2 < 6.0.0-beta.10 < 6.0.0-rc.1 < 6.0.0`. Les outils de ce dépôt acceptent ce suffixe
> dans les fiches et dans les noms d'installateurs (`Ma-classe_6.0.0-beta.1_x64-setup-essai.exe`).

---

## 0. Passage à Glacis (branche `claude/glacis-site`, préparée et réunie dans `main` le 18 novembre 2026 avec le premier essai de Glacis, 6.0.0-beta.12)

Décision de Franck du 18 novembre 2026 : le logiciel devient « **Glacis – Ma classe** », une nouvelle application
(identifiant, clés et nom d'installateur nouveaux) ; ses mises à jour et sa page de présentation sont servies par
**`https://glacis-classe.fr`** (Cloudflare Pages, projet `glacis-classe`, envoi direct). Ce dépôt reste la fabrique
(installateur Windows, signatures) ; seule la destination change.

| Avant (Ma classe) | Après (Glacis) |
|---|---|
| site `harry-safe.github.io/ma-classe-versions` (GitHub Pages) | `glacis-classe.fr` (Cloudflare Pages) : l'ancienne adresse n'est plus mise à jour |
| `stable/Ma classe.html`, `Ma classe - Remplaçant.html` | `stable/Glacis.html`, `Glacis - Remplaçant.html` (balise `glacis-version`) |
| `Ma-classe_<v>_x64-setup*.exe` | `Glacis_<v>_x64-setup*.exe` (l'application refuse un installateur d'un autre nom) |
| `index.html` : page des mises à jour | page de présentation de Glacis, `icone.svg`, `_headers` |
| déploiement : `configure-pages`, `deploy-pages` | `outils/deploiement/` (wrangler à version et empreintes fixées, `npm ci --ignore-scripts`), puis `wrangler pages deploy _site --project-name=glacis-classe --branch=main` |
| secrets `MAJ_CLE_PRIVEE`, `TAURI_SIGNING_PRIVATE_KEY` | les mêmes (**mêmes clés**), plus `CLOUDFLARE_API_TOKEN` (jeton « Cloudflare Pages : Edit ») et `CLOUDFLARE_ACCOUNT_ID` |

Les étapes de signature de l'application tournent dès qu'une des deux fiches (`appli/latest.json`, `appli/essai/latest.json`) existe.
Inchangés : formats `ma-classe-versions` et `ma-classe-applis`, clés de signature, outils de signature et de
fabrication (qui acceptent la balise `glacis-version` comme `ma-classe-version`). Un canal `stable` n'est plus
obligatoire : tant que Glacis n'a que des essais, `versions.json` ne porte que le canal `essai` (avertissement dans le
journal de l'action) et la page de présentation propose l'installateur d'essai.

**Ordre des opérations** (chacune sur une phrase explicite de Franck) :

1. *Écartée par Franck* (« passerelle non ») : la **passerelle**, dernière version de « Ma classe » (branche
   `claude/ma-classe-passerelle` du dépôt source), publiée depuis `main` **tel qu'il est** (GitHub Pages à réactiver :
   Settings › Pages › Source : GitHub Actions). Elle annonce Glacis aux postes installés.
2. **Bascule** : réunir `claude/glacis-site` dans `main` **dans le même envoi que la première publication de Glacis** ;
   retirer d'abord ce qui appartient à Ma classe (`git rm -r stable essai appli coquille entrees` et, dans `applis/`,
   les entrées et paquets autres que `echecs` : seul Échecs est repris), puis lancer `build/publier-version.py` et
   `build/publier-appli.py` du dépôt source (branche renommée) et `outils/publier.py echecs` d'Applis-classe.
3. Avant cet envoi : les deux secrets Cloudflare existent, et le domaine `glacis-classe.fr` est **actif** sur le projet
   Pages (le 18 novembre 2026 au soir, `glacis-classe.fr` et `www.glacis-classe.fr` étaient encore « pending »).

## 1. Contenu

| Chemin | Écrit par | Rôle |
|---|---|---|
| `entrees/stable.json`, `entrees/essai.json` | `build/publier-version.py` (dépôt Ma classe) | version, date, titre, nouveautés, fichiers (adresse, taille, SHA-256) d'un **canal** |
| `stable/Ma classe.html`, `stable/Ma classe - Remplaçant.html` | idem | pages publiées (édition Classe, édition Remplaçant) |
| `essai/…` | idem, `--canal essai` | pages d'essai |
| `appli/latest.json` | `build/publier-appli.py` | application Windows publiée (fiche lue par l'application) |
| `appli/essai/latest.json` | idem, `--canal essai` | application d'essai |
| `coquille/stable/`, `coquille/essai/` | idem | coquille Tauri du canal, avec les chemins du dépôt source : `tauri/package.json`, `tauri/src-tauri/` sans `target/`, et les fichiers de la page que le code Rust intègre (`src/applis/pont-applis.js`…) : l'action en fait l'installateur |
| `appli/…/Ma-classe_<v>_x64-setup*.exe` | ancien fonctionnement (avant le 9 novembre 2026) | installateur fabriqué dans le dépôt privé ; s'il est présent, l'action le prend tel quel au lieu de fabriquer |
| `applis/entrees/<id>.json` | `outils/publier.py` du dépôt privé `Applis-classe` (référence, avec garde ; ou `build/publier-applis.py` du dépôt Ma classe) | une appli du **Store** : nom, description, couleur, icône intégrée, et pour chaque canal version, date, notes, paquet (adresse, taille, SHA-256) |
| `applis/paquets/<id>-<version>.zip` | idem | paquet d'une appli (sans son dossier `donnees`) ; une version publiée ne change plus |
| `index.html`, `icone.svg` | à la main | page de présentation de Glacis (vitrine animée, § 1 bis) et lien vers l'installateur Windows (`#telecharger`) : la version publiée, sinon la version d'essai |
| `vitrine/films/`, `vitrine/images/` | `outils/vitrine/` (§ 1 bis) | films MP4 et images WebP de la page, pris dans la **vraie application** (classe de démonstration, prénoms fictifs) |
| tuiles des outils (dans `index.html`, entre `<!--TUILES-->` et `<!--/TUILES-->`) | `outils/vitrine/ranger.py` | dessins SVG relevés dans le menu Outils de l'application (`outils/icones-illustrees.js`), redessinés par les règles de tuile de Glacis : jamais photographiés (les coins garderaient le fond de la fenêtre) |
| `vitrine/polices/` | copie de `vendor/polices/` du dépôt source | polices de la page (Glacis Lecture, Marelle) et leurs licences OFL |
| `outils/vitrine/` | — | fabrique des films et des images de la page (§ 1 bis) ; `_travail/` est ignoré par Git |
| `outils/signer.py` | — | vérifie les fichiers annoncés, signe `versions.json` et le catalogue du Store `applis.json` (Ed25519, même clé), prépare `_site/` |
| `outils/fabriquer-appli.py` | — | fabrique l'installateur d'un canal (coquille + page publiée), le range dans `_site/appli/` |
| `outils/signer-appli.py` | — | signe chaque installateur (Minisign, `@tauri-apps/cli` installé depuis `outils/signature/`), **revérifie** chaque signature comme l'application (clé `CLE_MAJ` de la coquille du canal, nom et version du fichier signé) et l'écrit dans les `latest.json` de `_site/appli/` ; `--a-blanc` : toute la chaîne avec une clé jetable (branches de fabrication) |
| `outils/signature/package.json`, `package-lock.json` | — | l'outil de signature, à version et empreintes fixées ; installé par `npm ci --ignore-scripts` avant que la clé soit dans l'environnement |
| `outils/exigences.txt` | — | paquets Python de l'action (`cryptography` et ses dépendances), versions et empreintes SHA-256 fixées (`pip install --require-hashes`) |
| `.github/workflows/publier.yml` | — | action « Publier les mises à jour » |
| `.github/workflows/nettoyer-branches.yml` | — | action « Nettoyer les branches », **lancée à la main par Franck** (liste d'abord, « oui » pour supprimer) : branches contenues dans `main`, de fabrication seule et anciennes préparations de publication ; les assistants n'ont pas le droit de supprimer une branche (lot D de l'audit, 13 novembre 2026) |
| `_site/`, `construction/`, `paquet/`, `paquets/` (ignorés) | l'action | site déployé ; fabrication de l'installateur |

## 1 bis. La page de présentation et ses images

`index.html` est une page sans dépendance extérieure (aucun script, police ou image d'un autre site, aucun traceur) :
elle fonctionne aussi sans JavaScript (tout est alors visible et immobile) et respecte « réduire les animations »
(rien ne bouge, les films attendent un clic sur leur bouton lecture). `outils/signer.py` copie `index.html`,
`icone.svg`, `_headers` et le dossier `vitrine/` dans `_site/`.

Sur un téléphone, la barre du haut ne flotte pas : elle reste en haut de la page et part avec elle (demande de Franck
du 19 novembre 2026).

**L'ouverture** (Franck, 20 novembre 2026) : un tableau blanc de classe, un voile de tissu très fin (le glacis) qui tombe
en ondulant et s'y dépose (calculé en direct en WebGL ; sans WebGL, un voile simple descend), puis Glacis s'y imprime et le film « ouverture » démarre : l'écran d'accueil, « Commencer », puis tout
au même endroit (appel, rituels, tableaux, boîte à outils, Atelier, Préparer). Le tableau et le voile sont **dessinés dans
la page** (CSS, SVG et WebGL, style et script `.ouv`) ; tout ce qui apparaît sur le voile vient du film, pris dans la vraie application.
Le film ouvre la classe de démonstration avec `&depart` (l'écran d'accueil attend « Commencer »), ce que Glacis sait
faire depuis l'essai 6.0.0-beta.23. Sans script : le film seul, avec les commandes du navigateur ; mouvements réduits :
rien ne bouge, il attend un clic. L'ancien film d'ouverture (`document` : une fiche PDF d'exemple jointe à une séance,
`outils/vitrine/exemples/`) est gardé de côté, hors de la page.

**Nouveautés du 21 novembre 2026** : l'accroche « Tout ce qu'il faut au tableau, en un Glacis. » s'écrit au tableau en deux
temps (la première ligne, puis le voile tombe, et « en un Glacis. » arrive quand il se pose : `data-accroche="deux"`) ;
la brosse et l'auget passent devant le voile ; un bandeau **en chiffres** sous l'en-tête ; les outils en **boucles
courtes** (`outils/vitrine/boucles.py`, découpées dans les films, rangées dans `vitrine/boucles/`) ; une section
**les applis** ; une section **questions** ; configuration requise et avertissement de Windows expliqué.

**Les chiffres suivent chaque publication** (Franck, 21 novembre 2026 : quand la version stable sortira, on ne parle que
d'elle et de son poids). `outils/chiffres.py`, lancé par l'action après le rangement des installateurs, réécrit dans
`_site/index.html` : les valeurs entre les repères `C:version`, `C:poids`, `C:outils`, `C:rituels`, les cartes entre les
repères `APPLIS` (la section reste cachée sans appli), le lien de téléchargement (repères `TELECHARGER` : visible même
sans script, par les robots et les assistants qui lisent la page) et l'empreinte SHA-256 de l'installateur (repères
`EMPREINTE`). Le canal est la version stable dès que `entrees/stable.json` existe, sinon l'essai. Version, poids et
lien viennent de `entrees/<canal>.json` et de l'installateur rangé ; les applis sont lues dans la page publiée
(`APPLIS_INTEGREES`) ; outils et rituels sont comptés en ouvrant une copie de la page publiée dans Chrome sans fenêtre
(`google-chrome` des machines de GitHub, ou `CHROME=…`). Une source illisible : la valeur écrite dans `index.html`
reste, et l'action l'écrit en avertissement (à relire après chaque publication). Les repères sont hors des scripts :
les empreintes de la politique de contenu ne changent pas (le script le vérifie). Essai à blanc :
`python outils/chiffres.py --site <copie du site> --montrer`.

Les films et les images montrent la **vraie application**, ouverte dans sa classe de démonstration
(`Glacis.html?classe-demo` : prénoms fictifs, lundi 9 novembre 2026, rien d'enregistré). **Aucune image n'est retouchée
ni générée** ; seul un point bleu est ajouté pour montrer où l'on clique. Pour les refaire après une nouvelle version
(Chromium de Playwright, `ffmpeg` et Pillow nécessaires ; `CHROME=…` pour un Chromium particulier) :

```
python outils/vitrine/filmer.py            # les quinze films, image par image (environ 4 min chacun)
python outils/vitrine/captures.py          # les captures fixes et les dessins des tuiles des outils (icones.json)
python outils/vitrine/ranger.py            # conversion, rangement dans vitrine/films et vitrine/images, tuiles écrites dans index.html
```

`filmer.py` pilote l'horloge de la page (30 images par seconde, minuteries, `requestAnimationFrame` et animations CSS
avancées pas à pas) : le film est fluide même sur une machine lente. Un scénario qui ne trouve plus son bouton après
un changement de l'application s'arrête avec une erreur : corriger le scénario (fin de `filmer.py`), pas l'image.
Relire chaque film avant de l'envoyer (une planche d'images suffit) : aucun prénom réel, aucun message d'erreur.

## 2. Formats

### `entrees/<canal>.json`

```json
{
  "version": "5.0.2",
  "date": "2026-11-06",
  "titre": "Préparer, doubles créneaux, Tableaux, canal d'essai de l'application",
  "notes": ["Préparer : …", "Tableaux : …", "Validation : deux éditions construites, 57 scénarios."],
  "fichiers": {
    "classe":     {"url": "stable/Ma classe.html",               "taille": 4366567, "sha256": "…"},
    "remplacant": {"url": "stable/Ma classe - Remplaçant.html",  "taille": 4366520, "sha256": "…"}
  }
}
```

Les nouveautés viennent de la section `## <version> — <date> · <titre>` du CHANGELOG de Ma classe : elles sont affichées
telles quelles dans Réglages › Mises à jour, à écrire pour des enseignants.

### `versions.json` (seulement sur le site, produit par l'action)

```json
{"format": "ma-classe-versions", "contenu": "<texte JSON : {\"canaux\": {\"stable\": {…}, \"essai\": {…}}}>", "signature": "<Ed25519, base64>"}
```

La signature porte sur le **texte exact** de `contenu`. L'application refuse une fiche dont la signature ne correspond
pas à sa clé publique, puis refuse un fichier dont la taille ou le SHA-256 diffèrent de la fiche. Un canal `stable` est
obligatoire.

### `applis.json` (catalogue du Store des applis, 10 novembre 2026)

```json
{"format": "ma-classe-applis", "contenu": "<texte JSON : {\"type\": \"applis\", \"applis\": [{\"id\", \"nom\", …, \"canaux\": {\"stable\": {…}, \"essai\": {…}}}]}>", "signature": "<Ed25519, base64>"}
```

Assemblé à partir de `applis/entrees/*.json`, signé avec la **même clé** que `versions.json` ; seuls les paquets annoncés
sont copiés dans `_site/applis/paquets/`. L'onglet Store de Ma classe refuse un catalogue mal signé ou d'un autre `type`,
puis un paquet dont la taille ou le SHA-256 diffèrent, ou qui contient un chemin dangereux. Détails côté application :
`docs/APPLIS.md` § 5 du dépôt source. Le journal de l'action affiche « applis.json signé : … ».

### `appli/latest.json` et `appli/essai/latest.json`

```json
{"version": "5.0.2", "notes": "ligne 1\nligne 2", "pub_date": "2026-11-06T12:21:13Z",
 "platforms": {"windows-x86_64": {"signature": "", "url": "https://harry-safe.github.io/ma-classe-versions/appli/Ma-classe_5.0.2_x64-setup.exe"}}}
```

Dans le dépôt, `signature` est **vide** : l'action la remplit dans la copie déployée (`_site/appli/…`). Les anciens
installateurs du même dossier sont retirés à chaque publication (ils restent dans l'historique Git).

## 3. L'action « Publier les mises à jour »

Déclenchée par **tout envoi sur `main`** (et à la main) :

0. **Application Windows** (un travail Windows par canal, `outils/fabriquer-appli.py`) : si l'installateur annoncé par
   `appli/<…>/latest.json` n'est pas dans le dépôt, il est fabriqué à partir de `coquille/<canal>/` et de la page
   publiée sur le canal (`<canal>/Ma classe.html`, après contrôle de son empreinte et de sa version) ; une fabrication
   est gardée en cache et réutilisée tant que la coquille, la page et la version ne changent pas ;
1. Python 3.12 + `cryptography`, `cffi`, `pycparser` aux versions et empreintes de `outils/exigences.txt` ;
2. `outils/signer.py` : pour chaque `entrees/*.json`, vérifie que chaque fichier existe et a la taille et l'empreinte
   annoncées (sinon **échec, rien n'est publié**), assemble et signe `versions.json` avec le secret **`MAJ_CLE_PRIVEE`**
   (clé Ed25519 brute, 32 octets en base64), copie les canaux, `index.html` et `appli/` dans `_site/` ; **l'essai suit
   la stable** (19 novembre 2026) : quand la version stable est au moins aussi récente que la version d'essai, le canal
   `essai` de `versions.json` (et celui de chaque appli de `applis.json`) annonce la version stable, pour que les essais
   installés jusqu'à la 6.0.0-beta.13, qui ne lisent que le canal d'essai, reçoivent la stable dès sa sortie ; `_headers` est
   écrit avec les empreintes des scripts de `index.html` (politique de contenu de la page de présentation) ; puis
   `fabriquer-appli.py --placer` range les installateurs fabriqués à côté de leur `latest.json` ;
3. Node 20, `npm ci --ignore-scripts` dans `outils/signature/` (la clé n'est pas encore dans l'environnement), puis
   `outils/signer-appli.py` (si `appli/latest.json` existe) : signe chaque installateur avec le secret
   **`TAURI_SIGNING_PRIVATE_KEY`** (sans mot de passe), revérifie la signature avec la clé publique de l'application ;
   échoue si le secret ou l'installateur manquent, ou si l'application refuserait la signature (**rien n'est publié**) ;
   même règle ensuite pour l'application : `_site/appli/essai/latest.json` reprend la fiche signée de la version stable
   quand celle-ci est au moins aussi récente (« appli/essai/latest.json : annonce la version stable X ») ;
4. déploiement GitHub Pages (`_site/`). Le journal de l'action affiche « versions.json signé : essai X, stable Y ».

Une branche autre que `main` ne déclenche **rien**, sauf `claude/fabrication-*` : l'installateur y est fabriqué et
rangé pour contrôle, **sans signature ni publication** (essayer une nouvelle coquille), puis la chaîne de signature est
essayée avec une clé jetable (`signer-appli.py --a-blanc` : la signature jetable doit passer le contrôle, et être
refusée par la clé de l'application). C'est l'endroit pour préparer ou relire un changement sans le publier.

**Dépendances fixées** (lot C de l'audit de sécurité, 13 novembre 2026) : chaque action est désignée par son commit
(étiquette en commentaire ; nouveau commit : `git ls-remote https://github.com/<action> refs/tags/<étiquette>` ; dernières versions, Node 24, depuis le 14 novembre 2026) ;
paquets Python par `outils/exigences.txt` ; outil de signature par `outils/signature/package-lock.json` ; fabrication
par `npm ci --ignore-scripts` (le `package-lock.json` de la coquille, copié par `build/publier-appli.py`) et
`cargo --locked` (son `Cargo.lock`, dont `fabriquer-appli.py` reporte le numéro de version). Une coquille publiée
avant ce lot n'a pas de `package-lock.json` : `npm install`, avec un avertissement.

**Changement de la clé des installateurs** (décision de Franck) : la version qui apporte la nouvelle `CLE_MAJ` est encore
signée avec l'ancienne clé, que vérifient les applications installées ; le contrôle de `signer-appli.py` la refuserait.
Pendant ce passage seulement, écrire l'**ancienne clé publique** (texte base64 de `CLE_MAJ`) dans
`outils/cle-precedente.txt`, puis retirer ce fichier une fois le secret changé.

## 3 bis. Pourquoi l'installateur est fabriqué ici

Décision de Franck du **9 novembre 2026** : les minutes GitHub du dépôt privé `Ma-classe` sont limitées, celles d'un
dépôt public ne le sont pas. Le dépôt privé ne fabrique donc plus l'installateur à chaque envoi : à la publication,
`build/publier-appli.py` dépose ici la **coquille** (la petite application Tauri qui affiche la page : `lib.rs`, la
configuration, les icônes), et l'action l'assemble avec la page déjà publiée sur le canal. La page étant déjà publique,
seule la coquille s'ajoute au contenu public. Elle ne contient que la **clé publique** de vérification des mises à jour.

## 4. Règles

1. **Publier seulement avec l'accord explicite de Franck**, pour le canal qu'il a demandé (« en essai » ≠ « publie »).
   Un envoi sur `main` **est** une publication.
2. Un essai ne modifie **que** `essai/`, `entrees/essai.json`, `appli/essai/`, `coquille/essai/` et, pour une appli du Store, la
   partie `essai` de `applis/entrees/<id>.json` et ses paquets ; vérifier le diff avant l'envoi
   (`git diff --stat`) : le canal stable doit rester intact.
3. Les pages publiées sont construites **sans aucune donnée de classe** (configuration d'exemple vide).
4. Jamais de clé privée, de jeton, de prénom d'élève, de lien de conversation dans ce dépôt (il est public).
5. Jamais de réécriture d'historique ni d'envoi forcé sur `main`.
6. Les postes n'installent qu'une version **plus grande** : pour revenir en arrière, publier une version corrective de
   numéro supérieur.
7. Commits en français (« Ma classe 5.0.2 : … ») avec l’identité du projet (Franck VARAULT,
   `Harry-Safe@users.noreply.github.com`). **Aucune signature de co-écriture d’assistant**, notamment aucune ligne
   `Co-Authored-By`, dans les nouveaux commits ou fichiers ; aucun crédit nominatif d’assistant ni lien de conversation.
   Cette décision de Franck du **7 novembre 2026** vaut pour les deux dépôts et remplace toute ancienne consigne contraire.
   Voir [AGENTS.md](AGENTS.md).
8. L’aide de l’IA au développement et à la documentation est mentionnée de façon générale dans la présentation
   uniquement. Depuis le 8 novembre 2026, `index.html` et `README.md` portent la formulation de Franck (« Ma classe »
   est conçu et développé par Franck VARAULT […] ; le code a été écrit avec l’aide d’assistants de programmation par IA,
   sous sa direction) ; depuis le 15 novembre 2026 (décision de Franck), l'application ne mentionne plus l'aide de l'IA (Réglages › À propos) : la mention figure seulement sur la page de présentation et dans le README. Les anciens commits et journaux, les références techniques et les crédits/licences tiers sont conservés.
   Ne pas retoucher les HTML, ZIP ou installateurs distribués à la main : leur mise à jour passe par les scripts
   de publication du dépôt source et une autorisation de publication.

## 5. Vérifier ce qui est en ligne

```bash
curl -s https://harry-safe.github.io/ma-classe-versions/versions.json \
  | python3 -c "import json,sys; f=json.load(sys.stdin); c=json.loads(f['contenu']); print({k: v['version'] for k, v in c['canaux'].items()})"
curl -s https://harry-safe.github.io/ma-classe-versions/appli/latest.json \
  | python3 -c "import json,sys; f=json.load(sys.stdin); print(f['version'], 'signé' if f['platforms']['windows-x86_64']['signature'] else 'NON SIGNÉ')"
```

Contrôles complets : signature Ed25519 de `contenu` avec la clé publique de l'application ; taille et SHA-256 des pages
téléchargées ; installateur identique au paquet construit ; signature Minisign de l'installateur.

## 6. Clés

| Usage | Privée (secret de ce dépôt) | Publique (dans l'application) |
|---|---|---|
| Fiche des pages | `MAJ_CLE_PRIVEE` (Ed25519) | liste `MiseAJour.CLES` de la page (plusieurs clés possibles) |
| Installateur Windows | `TAURI_SIGNING_PRIVATE_KEY` (Minisign) | `CLE_MAJ` de l'application (une seule) |

Changer une clé est une décision de Franck : publier d'abord une version de l'application qui accepte la nouvelle clé,
attendre qu'elle soit installée, puis seulement remplacer le secret.

© 2026 Franck VARAULT. Ma classe : licence GNU GPL version 3 ou ultérieure (`LICENSE`) ; documentation : CC BY-SA 4.0 ; applis du Store : licence propre à chacune.
