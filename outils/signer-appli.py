"""Signe l'installateur de l'application Windows pour le module de mise à jour de Tauri (action « Publier les
mises à jour », après outils/signer.py qui a copié appli/ dans _site/appli/).

La clé privée vient seulement du secret TAURI_SIGNING_PRIVATE_KEY (sans mot de passe) : jamais dans un fichier.
La signature est écrite dans _site/appli/latest.json (versions publiées) et _site/appli/essai/latest.json (versions
d'essai, lues par l'application réglée sur « d'essai ») ; l'application refuse un installateur dont la signature
ne correspond pas à sa clé publique.
"""
import json, os, subprocess, sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "_site" / "appli"
CLI = "@tauri-apps/cli@2.12.4"


def signer(fiche):
    f = json.loads(fiche.read_text(encoding="utf-8"))
    for nom, p in f["platforms"].items():
        exe = fiche.parent / p["url"].rsplit("/", 1)[-1]
        if not exe.exists(): sys.exit(f"{exe.name} manquant dans {fiche.parent.relative_to(SITE.parent)}/")
        subprocess.run(["npx", "--yes", CLI, "signer", "sign", str(exe)], check=True, env={**os.environ, "TAURI_SIGNING_PRIVATE_KEY_PASSWORD": ""})
        p["signature"] = (exe.parent / (exe.name + ".sig")).read_text(encoding="utf-8").strip()
        print(f"{fiche.parent.name} · {nom} : {exe.name} signé")
    fiche.write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    fiches = [x for x in (SITE / "latest.json", SITE / "essai" / "latest.json") if x.exists()]
    if not fiches: return print("pas d'application à signer")
    if not os.environ.get("TAURI_SIGNING_PRIVATE_KEY"): sys.exit("secret TAURI_SIGNING_PRIVATE_KEY absent : l'application ne peut pas être publiée")
    for fiche in fiches: signer(fiche)


if __name__ == "__main__":
    main()
