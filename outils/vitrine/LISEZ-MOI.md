# Films et images de la page de présentation

Ces outils fabriquent ce que `index.html` montre de Glacis : quinze films et quelques captures, pris dans la **vraie
application** ouverte dans sa classe de démonstration (prénoms fictifs, rien d'enregistré). Rien n'est retouché ni
généré ; seul un point bleu montre où l'on clique.

| Fichier | Rôle |
|---|---|
| `commun.py` | où est la page de Glacis (`stable/Glacis.html`, sinon `essai/Glacis.html`), dossier de travail |
| `filmer.py` | le moteur (horloge pilotée, 30 images par seconde) et les quinze scénarios : `ouverture` (le film qui se dépose sur le voile de l'ouverture : l'écran d'accueil, « Commencer », puis tout au même endroit ; il ouvre la classe de démonstration avec `&depart`, ce que Glacis sait faire depuis l'essai 6.0.0-beta.23), `document` (une fiche jointe à une séance, ancien film d'ouverture, gardé de côté), `accueil`, `appel`, `assistant`, `problemes`, `numeration`, `geometrie`, `lignages`, `operations`, `minuteur`, `balancenb`, `droite`, `fractions`, `reglettes` |
| `exemples/` | la fiche PDF jointe dans le film d'ouverture (« Compléments à 10 », faite pour la démonstration : `fiche.html` l'a produite) |
| `captures.py` | captures fixes (`accueil`, `soir`, `semaine`, `ops`, `geo`, `ecriture`…) ; `icones` relève dans le menu Outils le nom, les couleurs et le dessin SVG de chaque tuile (`_travail/captures/icones.json`) |
| `ranger.py` | conversion (MP4, WebP) et rangement dans `vitrine/films/` et `vitrine/images/` ; écrit les tuiles des outils dans `index.html` (entre `<!--TUILES-->` et `<!--/TUILES-->`), en vectoriel, avec les règles de tuile de Glacis |
| `boucles.py` | boucles courtes des outils (section « les outils ») : un geste découpé dans un film de `vitrine/films/`, recadré sur l'outil, fondu couleur papier ; écrit `vitrine/boucles/<nom>.mp4` et son affiche `<nom>.webp` |

```
python outils/vitrine/filmer.py [noms]     # sans nom : les quinze films (environ une heure)
BROUILLON=1 python outils/vitrine/filmer.py appel   # une image sur dix : pour régler un scénario en une minute
GLACIS_PAGE=../Ma-classe/dist/Glacis.html python outils/vitrine/filmer.py   # une page construite, avant sa publication
python outils/vitrine/captures.py [noms]
python outils/vitrine/ranger.py [films]     # des films nommés : seulement eux (les captures et les tuiles ne bougent pas)
```

Il faut Playwright et son Chromium (`CHROME=…` pour en désigner un autre), `ffmpeg` (libx264) et Pillow. Le dossier
`_travail/` (images intermédiaires) est ignoré par Git. Procédure et précautions : `DOCUMENTATION.md` § 1 bis.
