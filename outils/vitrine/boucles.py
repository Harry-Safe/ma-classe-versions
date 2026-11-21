"""Boucles courtes des outils (section « les outils » de la page de présentation) : un geste par boucle, découpé dans
un film déjà rangé dans vitrine/films/ (outils/vitrine/filmer.py puis ranger.py), recadré sur l'outil, avec un fondu
d'entrée et de sortie couleur papier pour que la boucle reprenne sans à-coup. Écrit vitrine/boucles/<nom>.mp4 (H.264,
sans son) et son affiche <nom>.webp (l'état final du geste, montrée sans script et en mouvements réduits).

Usage : python outils/vitrine/boucles.py [nom …]   (sans nom : toutes les boucles)
À relancer quand le film d'origine change ; vérifier le cadrage sur les affiches.
"""
import subprocess, sys
from pathlib import Path

ICI = Path(__file__).resolve().parents[2]
FILMS, SORTIE = ICI / "vitrine" / "films", ICI / "vitrine" / "boucles"
PAPIER = "0xfcfaf4"
# nom : (film, recadrage x, y, largeur, hauteur dans le film 1600 × 900, taille finale, début, fin en secondes)
BOUCLES = {
    "balancenb": ("balancenb", 305, 175, 990, 557, (960, 540), 7.0, 13.0),   # un poids sur le 2, puis sur le 4 : 6 = 2 + 4
    "reglettes": ("reglettes", 220, 150, 1040, 585, (960, 540), 4.0, 10.5),  # 10, puis 6 et 4 aimantées dessous
    "fractions": ("fractions", 260, 165, 1040, 585, (960, 540), 2.5, 9.5),   # trois quarts en bande, en disque, deux quarts
    "droite":    ("droite", 290, 330, 1020, 300, (1200, 352), 4.5, 10.5),    # bonds de 4 à 10, puis de 10 à 13
}


def ffmpeg(*a): subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *a], check=True)


def boucle(nom):
    film, x, y, w, h, (W, H), a, b = BOUCLES[nom]
    d, cadre = b - a, f"crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos"
    SORTIE.mkdir(exist_ok=True)
    ffmpeg("-ss", str(a), "-t", str(d), "-i", str(FILMS / f"{film}.mp4"),
           "-vf", f"{cadre},fade=t=in:st=0:d=0.35:color={PAPIER},fade=t=out:st={d - .35:.2f}:d=0.35:color={PAPIER}",
           "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "27", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
           str(SORTIE / f"{nom}.mp4"))
    ffmpeg("-ss", str(b - .5), "-i", str(FILMS / f"{film}.mp4"), "-frames:v", "1", "-vf", cadre, "-c:v", "libwebp", "-quality", "82",
           str(SORTIE / f"{nom}.webp"))
    print(f"{nom} : {(SORTIE / f'{nom}.mp4').stat().st_size // 1024} Ko, affiche {(SORTIE / f'{nom}.webp').stat().st_size // 1024} Ko")


if __name__ == "__main__":
    for n in sys.argv[1:] or BOUCLES: boucle(n)
