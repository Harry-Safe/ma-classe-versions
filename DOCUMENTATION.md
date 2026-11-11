# Documentation du site des mises à jour

**En bref.** Ce dépôt **public** est le **seul** point de distribution de « Ma classe » (logiciel de classe de Franck
VARAULT). Il contient les éditions construites, leurs fiches, la « coquille » de l'application Windows et l'action qui
**fabrique l'installateur, vérifie, signe et publie** le site `https://harry-safe.github.io/ma-classe-versions/`
(GitHub Pages). Il ne contient **aucune donnée d'élève**, aucun autre code source de l'application que cette coquille
(§ 3 bis), et **aucune clé privée** : les clés de signature vivent seulement dans les secrets
GitHub du dépôt. Seuls Franck (et les assistants qui travaillent avec lui, sur son autorisation) le modifient.

> Le code source et la procédure complète (numéros de version, CHANGELOG, essais, publication pas à pas) sont dans le
> dépôt privé de Ma classe : `docs/VERSIONS_ET_PUBLICATION.md` et `docs/APPLICATION_WINDOWS.md`.

---

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
| `index.html` | à la main | page publique : explication et lien vers l'installateur Windows (`#appli`) |
| `outils/signer.py` | — | vérifie les fichiers annoncés, signe `versions.json` et le catalogue du Store `applis.json` (Ed25519, même clé), prépare `_site/` |
| `outils/fabriquer-appli.py` | — | fabrique l'installateur d'un canal (coquille + page publiée), le range dans `_site/appli/` |
| `outils/signer-appli.py` | — | signe chaque installateur (Minisign, `@tauri-apps/cli` 2.12.4) et écrit la signature dans les `latest.json` de `_site/appli/` |
| `.github/workflows/publier.yml` | — | action « Publier les mises à jour » |
| `_site/`, `construction/`, `paquet/`, `paquets/` (ignorés) | l'action | site déployé ; fabrication de l'installateur |

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
1. Python 3.12 + `cryptography` ;
2. `outils/signer.py` : pour chaque `entrees/*.json`, vérifie que chaque fichier existe et a la taille et l'empreinte
   annoncées (sinon **échec, rien n'est publié**), assemble et signe `versions.json` avec le secret **`MAJ_CLE_PRIVEE`**
   (clé Ed25519 brute, 32 octets en base64), copie les canaux, `index.html` et `appli/` dans `_site/` ; puis
   `fabriquer-appli.py --placer` range les installateurs fabriqués à côté de leur `latest.json` ;
3. Node 20 + `outils/signer-appli.py` (si `appli/latest.json` existe) : signe chaque installateur avec le secret
   **`TAURI_SIGNING_PRIVATE_KEY`** (sans mot de passe) ; échoue si le secret ou l'installateur manquent ;
4. déploiement GitHub Pages (`_site/`). Le journal de l'action affiche « versions.json signé : essai X, stable Y ».

Une branche autre que `main` ne déclenche **rien**, sauf `claude/fabrication-*` : l'installateur y est fabriqué et
rangé pour contrôle, **sans signature ni publication** (essayer une nouvelle coquille). C'est l'endroit pour préparer ou
relire un changement sans le publier.

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
   sous sa direction) ; Réglages › À propos garde sa mention générale, que Franck ne veut pas modifier. Les anciens commits et journaux, les références techniques et les crédits/licences tiers sont conservés.
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

© 2026 Franck VARAULT. Tous droits réservés.
