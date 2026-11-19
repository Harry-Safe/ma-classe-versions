# Films et images de la page de présentation

Ces outils fabriquent ce que `index.html` montre de Glacis : six films et quelques captures, pris dans la **vraie
application** ouverte dans sa classe de démonstration (prénoms fictifs, rien d'enregistré). Rien n'est retouché ni
généré ; seul un point bleu montre où l'on clique.

| Fichier | Rôle |
|---|---|
| `commun.py` | où est la page de Glacis (`stable/Glacis.html`, sinon `essai/Glacis.html`), dossier de travail |
| `filmer.py` | le moteur (horloge pilotée, 30 images par seconde) et les six scénarios : `journee`, `rituels`, `numeration`, `balance`, `monnaie`, `reglettes` |
| `captures.py` | captures fixes (`accueil`, `soir`, `semaine`, `ops`, `geo`, `ecriture`…) ; `icones` relève dans le menu Outils le nom, les couleurs et le dessin SVG de chaque tuile (`_travail/captures/icones.json`) |
| `ranger.py` | conversion (MP4, WebP) et rangement dans `vitrine/films/` et `vitrine/images/` ; écrit les tuiles des outils dans `index.html` (entre `<!--TUILES-->` et `<!--/TUILES-->`), en vectoriel, avec les règles de tuile de Glacis |

```
python outils/vitrine/filmer.py [noms]     # sans nom : les six films
python outils/vitrine/captures.py [noms]
python outils/vitrine/ranger.py [films]
```

Il faut Playwright et son Chromium (`CHROME=…` pour en désigner un autre), `ffmpeg` (libx264) et Pillow. Le dossier
`_travail/` (images intermédiaires) est ignoré par Git. Procédure et précautions : `DOCUMENTATION.md` § 1 bis.
