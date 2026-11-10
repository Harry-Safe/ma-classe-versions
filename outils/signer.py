"""Assemble et signe versions.json à partir de entrees/*.json, puis prépare le site (dossier _site).
Assemble et signe aussi applis.json, le catalogue du Store des applis, à partir de applis/entrees/*.json.

Lancé par GitHub Actions à chaque envoi (voir .github/workflows/publier.yml) ; la clé privée Ed25519
(base64, 32 octets) est lue dans la variable d'environnement MAJ_CLE_PRIVEE (secret du dépôt).
Vérifie que chaque fichier annoncé existe et a bien l'empreinte annoncée avant de signer.
"""
import base64, hashlib, json, os, re, shutil, sys
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

ICI = Path(__file__).resolve().parent.parent
SITE = ICI / "_site"


def verifier_fichier(origine, x):
    p = ICI / x["url"]
    if not p.is_file(): sys.exit(f"{origine} : fichier absent {x['url']}")
    b = p.read_bytes()
    if hashlib.sha256(b).hexdigest() != x["sha256"] or len(b) != x["taille"]: sys.exit(f"{origine} : {x['url']} ne correspond pas à son empreinte")


def catalogue_applis(k):
    """Store des applis : applis/entrees/<id>.json (écrits par build/publier-applis.py du dépôt source) -> applis.json
    signé, au même format que versions.json mais de type « applis » ; seuls les paquets annoncés sont mis en ligne."""
    applis, paquets, resume = [], set(), []
    dossier = ICI / "applis" / "entrees"
    for f in sorted(dossier.glob("*.json")) if dossier.is_dir() else []:
        e = json.loads(f.read_text(encoding="utf-8"))
        if e.get("id") != f.stem or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,40}", f.stem): sys.exit(f"{f.name} : identifiant d'appli invalide")
        for canal, c in (e.get("canaux") or {}).items():
            if canal not in ("stable", "essai"): sys.exit(f"{f.name} : canal inconnu {canal}")
            x = c["fichier"]
            if not x["url"].startswith("applis/paquets/"): sys.exit(f"{f.name} : paquet hors de applis/paquets/")
            verifier_fichier(f.name, x); paquets.add(x["url"])
            resume.append(f"{e['id']} {c['version']} ({canal})")
        if e.get("canaux"): applis.append(e)
    contenu = json.dumps({"type": "applis", "applis": applis}, ensure_ascii=False, separators=(",", ":"))
    fiche = {"format": "ma-classe-applis", "contenu": contenu,
             "signature": base64.b64encode(k.sign(contenu.encode("utf-8"))).decode()}
    for u in sorted(paquets):
        (SITE / u).parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ICI / u, SITE / u)
    (SITE / "applis.json").write_text(json.dumps(fiche, ensure_ascii=False), encoding="utf-8")
    print("applis.json signé :", ", ".join(resume) or "aucune appli")


def main():
    cle = os.environ.get("MAJ_CLE_PRIVEE", "").strip()
    if not cle: sys.exit("Secret MAJ_CLE_PRIVEE absent : Settings › Secrets and variables › Actions")
    k = Ed25519PrivateKey.from_private_bytes(base64.b64decode(cle))
    canaux = {}
    for f in sorted((ICI / "entrees").glob("*.json")):
        e = json.loads(f.read_text(encoding="utf-8"))
        for ed, x in e["fichiers"].items(): verifier_fichier(f.name, x)
        canaux[f.stem] = e
    if "stable" not in canaux: sys.exit("aucune version stable (entrees/stable.json)")
    contenu = json.dumps({"canaux": canaux}, ensure_ascii=False, separators=(",", ":"))
    fiche = {"format": "ma-classe-versions", "contenu": contenu,
             "signature": base64.b64encode(k.sign(contenu.encode("utf-8"))).decode()}
    shutil.rmtree(SITE, ignore_errors=True); SITE.mkdir()
    for c in canaux: shutil.copytree(ICI / c, SITE / c)
    shutil.copyfile(ICI / "index.html", SITE / "index.html")
    if (ICI / "appli").is_dir(): shutil.copytree(ICI / "appli", SITE / "appli")   # application Windows (latest.json + installateur signé)
    (SITE / "versions.json").write_text(json.dumps(fiche, ensure_ascii=False), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print("versions.json signé :", ", ".join(f"{c} {e['version']}" for c, e in canaux.items()))
    catalogue_applis(k)


if __name__ == "__main__":
    main()
