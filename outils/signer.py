"""Assemble et signe versions.json à partir de entrees/*.json, puis prépare le site (dossier _site).

Lancé par GitHub Actions à chaque envoi (voir .github/workflows/publier.yml) ; la clé privée Ed25519
(base64, 32 octets) est lue dans la variable d'environnement MAJ_CLE_PRIVEE (secret du dépôt).
Vérifie que chaque fichier annoncé existe et a bien l'empreinte annoncée avant de signer.
"""
import base64, hashlib, json, os, shutil, sys
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

ICI = Path(__file__).resolve().parent.parent
SITE = ICI / "_site"


def main():
    cle = os.environ.get("MAJ_CLE_PRIVEE", "").strip()
    if not cle: sys.exit("Secret MAJ_CLE_PRIVEE absent : Settings › Secrets and variables › Actions")
    k = Ed25519PrivateKey.from_private_bytes(base64.b64decode(cle))
    canaux = {}
    for f in sorted((ICI / "entrees").glob("*.json")):
        e = json.loads(f.read_text(encoding="utf-8"))
        for ed, x in e["fichiers"].items():
            p = ICI / x["url"]
            if not p.exists(): sys.exit(f"{f.name} : fichier absent {x['url']}")
            b = p.read_bytes()
            if hashlib.sha256(b).hexdigest() != x["sha256"] or len(b) != x["taille"]: sys.exit(f"{f.name} : {x['url']} ne correspond pas à son empreinte")
        canaux[f.stem] = e
    if "stable" not in canaux: sys.exit("aucune version stable (entrees/stable.json)")
    contenu = json.dumps({"canaux": canaux}, ensure_ascii=False, separators=(",", ":"))
    fiche = {"format": "ma-classe-versions", "contenu": contenu,
             "signature": base64.b64encode(k.sign(contenu.encode("utf-8"))).decode()}
    shutil.rmtree(SITE, ignore_errors=True); SITE.mkdir()
    for c in canaux: shutil.copytree(ICI / c, SITE / c)
    shutil.copyfile(ICI / "index.html", SITE / "index.html")
    (SITE / "versions.json").write_text(json.dumps(fiche, ensure_ascii=False), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print("versions.json signé :", ", ".join(f"{c} {e['version']}" for c, e in canaux.items()))


if __name__ == "__main__":
    main()
