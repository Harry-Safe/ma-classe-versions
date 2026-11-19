"""Assemble et signe versions.json à partir de entrees/*.json, puis prépare le site (dossier _site).
Assemble et signe aussi applis.json, le catalogue du Store des applis, à partir de applis/entrees/*.json.

Le site est celui de Glacis, https://glacis-classe.fr (Cloudflare Pages) : page de présentation (index.html, icone.svg, vitrine/),
fiches signées, pages et installateurs. Les formats « ma-classe-versions » et « ma-classe-applis » gardent leur nom.
Lancé par GitHub Actions à chaque envoi (voir .github/workflows/publier.yml) ; la clé privée Ed25519
(base64, 32 octets) est lue dans la variable d'environnement MAJ_CLE_PRIVEE (secret du dépôt).
Vérifie que chaque fichier annoncé existe et a bien l'empreinte annoncée avant de signer.

L'essai suit la stable (19 novembre 2026) : quand la version stable est au moins aussi récente que la version d'essai,
le canal « essai » de la fiche annonce la version stable (pages comme applis du Store ; pour l'application Windows :
outils/signer-appli.py). Les essais installés jusqu'à la 6.0.0-beta.13 ne lisent que le canal d'essai : ils reçoivent
ainsi la version stable dès sa sortie, et personne ne reste sur une ancienne version d'essai.
"""
import base64, hashlib, json, os, re, shutil, sys
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

ICI = Path(__file__).resolve().parent.parent
SITE = ICI / "_site"


def cle(v):
    """Ordre des versions, le même que l'application (MiseAJour.comparer, build/numeros.py) : nombre par nombre, puis une
    version publiée après ses essais (6.0.0 > 6.0.0-rc.1 > 6.0.0-beta.13 > 6.0.0-beta.2)."""
    base, _, pre = str(v).partition("-")
    n = [int(x) for x in base.split(".")]
    n += [0] * (3 - len(n))
    parts = [(0, int(x), "") if x.isdigit() else (1, 0, x) for x in pre.split(".")] if pre else []
    return n, 0 if pre else 1, parts


def essai_suit_stable(canaux, quoi):
    """Canal d'essai remplacé par la version stable quand celle-ci est au moins aussi récente (voir l'en-tête)."""
    st, es = canaux.get("stable"), canaux.get("essai")
    if st and (not es or cle(st["version"]) >= cle(es["version"])):
        canaux["essai"] = st
        if es: print(f"{quoi} : le canal d'essai annonce la version stable {st['version']} (essai {es['version']} dépassé)")
    return canaux


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
        if e.get("canaux"): applis.append({**e, "canaux": essai_suit_stable(dict(e["canaux"]), e["id"])})
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
    if not canaux: sys.exit("aucune version à publier (entrees/*.json)")
    if "stable" not in canaux: print("::warning::pas encore de version stable (entrees/stable.json) : seuls les essais sont publiés")
    dossiers = list(canaux)                                   # dossiers à mettre en ligne : ceux des fiches entrees/
    canaux = essai_suit_stable(dict(canaux), "versions.json")
    contenu = json.dumps({"canaux": canaux}, ensure_ascii=False, separators=(",", ":"))
    fiche = {"format": "ma-classe-versions", "contenu": contenu,
             "signature": base64.b64encode(k.sign(contenu.encode("utf-8"))).decode()}
    shutil.rmtree(SITE, ignore_errors=True); SITE.mkdir()
    for c in dossiers: shutil.copytree(ICI / c, SITE / c)
    for nom in ("index.html", "icone.svg", "_headers"):          # page de présentation, son icône, en-têtes de Cloudflare Pages
        if (ICI / nom).is_file(): shutil.copyfile(ICI / nom, SITE / nom)
    if (ICI / "vitrine").is_dir(): shutil.copytree(ICI / "vitrine", SITE / "vitrine")   # images, films et polices de la page de présentation
    if (ICI / "appli").is_dir(): shutil.copytree(ICI / "appli", SITE / "appli")   # application Windows (latest.json + installateur signé)
    (SITE / "versions.json").write_text(json.dumps(fiche, ensure_ascii=False), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print("versions.json signé :", ", ".join(f"{c} {e['version']}" for c, e in canaux.items()))
    catalogue_applis(k)


if __name__ == "__main__":
    main()
