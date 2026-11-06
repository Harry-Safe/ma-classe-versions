# Documentation du site des mises à jour

**En bref.** Ce dépôt **public** est le **seul** point de distribution de « Ma classe » (logiciel de classe de Franck
VARAULT). Il contient les éditions construites, leurs fiches et l'action qui **vérifie, signe et publie** le site
`https://harry-safe.github.io/ma-classe-versions/` (GitHub Pages). Il ne contient **aucune donnée d'élève** ni aucun
code source de l'application, et **aucune clé privée** : les clés de signature vivent seulement dans les secrets
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
| `appli/latest.json`, `appli/Ma-classe_<v>_x64-setup.exe` | `build/publier-appli.py` | application Windows publiée (fiche lue par l'application) |
| `appli/essai/latest.json`, `appli/essai/Ma-classe_<v>_x64-setup-essai.exe` | idem, `--canal essai` | application d'essai |
| `index.html` | à la main | page publique : explication et lien vers l'installateur Windows (`#appli`) |
| `outils/signer.py` | — | vérifie les fichiers annoncés, signe `versions.json` (Ed25519), prépare `_site/` |
| `outils/signer-appli.py` | — | signe chaque installateur (Minisign, `@tauri-apps/cli` 2.12.4) et écrit la signature dans les `latest.json` de `_site/appli/` |
| `.github/workflows/publier.yml` | — | action « Publier les mises à jour » |
| `_site/` (ignoré) | l'action | site réellement déployé |

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

### `appli/latest.json` et `appli/essai/latest.json`

```json
{"version": "5.0.2", "notes": "ligne 1\nligne 2", "pub_date": "2026-11-06T12:21:13Z",
 "platforms": {"windows-x86_64": {"signature": "", "url": "https://harry-safe.github.io/ma-classe-versions/appli/Ma-classe_5.0.2_x64-setup.exe"}}}
```

Dans le dépôt, `signature` est **vide** : l'action la remplit dans la copie déployée (`_site/appli/…`). Les anciens
installateurs du même dossier sont retirés à chaque publication (ils restent dans l'historique Git).

## 3. L'action « Publier les mises à jour »

Déclenchée par **tout envoi sur `main`** (et à la main) :

1. Python 3.12 + `cryptography` ;
2. `outils/signer.py` : pour chaque `entrees/*.json`, vérifie que chaque fichier existe et a la taille et l'empreinte
   annoncées (sinon **échec, rien n'est publié**), assemble et signe `versions.json` avec le secret **`MAJ_CLE_PRIVEE`**
   (clé Ed25519 brute, 32 octets en base64), copie les canaux, `index.html` et `appli/` dans `_site/` ;
3. Node 20 + `outils/signer-appli.py` (si `appli/latest.json` existe) : signe chaque installateur avec le secret
   **`TAURI_SIGNING_PRIVATE_KEY`** (sans mot de passe) ; échoue si le secret ou l'installateur manquent ;
4. déploiement GitHub Pages (`_site/`). Le journal de l'action affiche « versions.json signé : essai X, stable Y ».

Une branche autre que `main` ne déclenche **rien** : c'est l'endroit pour préparer ou relire un changement sans le publier.

## 4. Règles

1. **Publier seulement avec l'accord explicite de Franck**, pour le canal qu'il a demandé (« en essai » ≠ « publie »).
   Un envoi sur `main` **est** une publication.
2. Un essai ne modifie **que** `essai/`, `entrees/essai.json` et `appli/essai/` ; vérifier le diff avant l'envoi
   (`git diff --stat`) : le canal stable doit rester intact.
3. Les pages publiées sont construites **sans aucune donnée de classe** (configuration d'exemple vide).
4. Jamais de clé privée, de jeton, de prénom d'élève, de lien de conversation dans ce dépôt (il est public).
5. Jamais de réécriture d'historique ni d'envoi forcé sur `main`.
6. Les postes n'installent qu'une version **plus grande** : pour revenir en arrière, publier une version corrective de
   numéro supérieur.
7. Commits en français (« Ma classe 5.0.2 : … ») avec l'identité du projet (Franck VARAULT).

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
