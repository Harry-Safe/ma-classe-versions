"""Réécrit les chiffres et les cartes des applis de la page de présentation (_site/index.html), à chaque publication.

Règle (Franck, 21 novembre 2026) : la page ne parle que de la version publiée, et ses chiffres suivent chaque publication.
Dès qu'une version stable existe (entrees/stable.json), on ne parle que d'elle et de son poids ; avant, de la version
d'essai.

Sources, pour le canal retenu :
  · version : entrees/<canal>.json ;
  · poids de l'installateur Windows : _site/appli/<sous-dossier>/*.exe, rangé par « Ranger les installateurs fabriqués »
    (lancer ce script APRÈS cette étape) ; affiché en Mo comme Windows le montre (1 Mo = 1 048 576 octets) ;
  · outils, rituels, applis : comptés dans la page publiée elle-même (entrees/<canal>.json, fichier « classe ») :
    les applis rangées dans Glacis sont lues dans APPLIS_INTEGREES ; les outils (OUTILS) et les rituels (RITUELS) sont
    comptés en ouvrant une copie de la page dans Chrome sans fenêtre (google-chrome des machines de GitHub, ou CHROME=…).
Une source illisible : la valeur déjà écrite dans index.html reste, avec un avertissement (l'action continue : la page
reste en ligne). La section « les applis » reste cachée tant qu'aucune appli n'est rangée dans la page.

Le lien de téléchargement (repères TELECHARGER) et l'empreinte SHA-256 de l'installateur (repères EMPREINTE) sont écrits
aussi dans la page : sans script (robots, assistants qui lisent la page), on voit le vrai lien, pas « Bientôt disponible ».

Repères dans index.html : <!--C:nom-->valeur<!--/C--> (nom : version, poids, outils, rituels), <!--APPLIS-->…<!--/APPLIS-->,
<!--TELECHARGER-->…<!--/TELECHARGER--> et <!--EMPREINTE-->…<!--/EMPREINTE-->.
Ils sont hors des scripts : les empreintes de la politique de contenu (_headers, outils/signer.py) ne changent pas, et ce
script le vérifie.

Usage : python outils/chiffres.py [--site _site] [--montrer]   (--montrer : affiche les valeurs sans rien écrire)
"""
import argparse, base64, hashlib, html, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent.parent
SOUS = {"stable": "", "essai": "essai"}          # dossiers des installateurs, comme outils/fabriquer-appli.py


def avertir(m): print(f"::warning::chiffres : {m}")


def court(v):
    """6.0.0 -> 6.0 ; 6.0.0-beta.28 -> 6.0 · essai 28 ; 6.0.0-rc.1 -> 6.0 · version candidate 1 (comme la page et Glacis)."""
    v = re.sub(r"^(\d+\.\d+)\.0(?=$|-)", r"\1", str(v))
    v = re.sub(r"-beta\.(\d+)$", r" · essai \1", v)
    return re.sub(r"-rc\.(\d+)$", r" · version candidate \1", v)


def nombre(x, decimales=0):
    return f"{x:.{decimales}f}".replace(".", ",")


def carte_appli(a):
    icone = a["icone"] if str(a.get("icone", "")).startswith("data:image/") else "data:image/svg+xml;base64," + base64.b64encode(str(a.get("icone", "")).encode("utf-8")).decode()
    c = a.get("couleur") or "#2f4fa8"
    if not re.fullmatch(r"#[0-9a-fA-F]{3,8}", c): c = "#2f4fa8"
    e = lambda t: html.escape(str(t or ""), quote=True)
    return (f'\n        <li class="appli" style="--c:{c}"><img src="{icone}" alt="" width="76" height="76">'
            f'<h3>{e(a["nom"])}</h3><span class="cat">{e(a.get("categorie"))}</span><p>{e(a.get("description"))}</p></li>')


def valeurs(site):
    canal = "stable" if (ICI / "entrees" / "stable.json").is_file() else "essai"
    entree = json.loads((ICI / "entrees" / f"{canal}.json").read_text(encoding="utf-8"))
    v = {"canal": canal, "version": court(entree["version"])}
    exe = sorted((site / "appli" / SOUS[canal]).glob("*.exe")) if (site / "appli").is_dir() else []
    fiche = site / "appli" / SOUS[canal] / "latest.json"
    if exe:
        v["poids"] = nombre(exe[-1].stat().st_size / 1048576, 1)
        v["sha256"] = hashlib.sha256(exe[-1].read_bytes()).hexdigest()
        url = json.loads(fiche.read_text(encoding="utf-8"))["platforms"]["windows-x86_64"]["url"] if fiche.is_file() else ""
        if url.rsplit("/", 1)[-1] == exe[-1].name: v["lien"] = url
        else: avertir(f"{fiche.name} n'annonce pas {exe[-1].name} : lien de téléchargement inchangé")
    else: avertir(f"aucun installateur dans {site.name}/appli/{SOUS[canal]} : poids et lien inchangés")
    page = ICI / entree["fichiers"]["classe"]["url"]
    v["applis"] = applis(page)
    v.update(compter(page))
    return v


def applis(page):
    """Les applis rangées dans la page : le tableau APPLIS_INTEGREES (écrit par build/construire.py du dépôt source)."""
    s = page.read_text(encoding="utf-8")
    m = re.search(r"const APPLIS_INTEGREES = (?:/\*.*?\*/)?", s)
    if not m: return []
    try: liste, _ = json.JSONDecoder().raw_decode(s[m.end():])
    except ValueError: avertir("APPLIS_INTEGREES illisible : applis inchangées"); return []
    sortie = []
    for a in liste:
        try: cat = json.loads(a.get("fiche") or "{}").get("categorie", "")
        except ValueError: cat = ""
        sortie.append({"id": a.get("id"), "nom": a.get("nom"), "version": a.get("version"), "description": a.get("description"),
                       "couleur": a.get("couleur"), "categorie": cat, "icone": a.get("icone", "")})
    return sortie


def compter(page):
    """Outils et rituels : comptés par la page elle-même, ouverte dans Chrome sans fenêtre (une copie, avec quelques lignes
    ajoutées à la fin qui écrivent les comptes dans la page)."""
    chrome = os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if not chrome: avertir("Chrome introuvable : outils et rituels inchangés"); return {}
    sonde = ('<script>document.body.insertAdjacentHTML("beforeend", "<pre id=glacis-chiffres>" + JSON.stringify({'
             'outils: typeof OUTILS !== "undefined" ? OUTILS.length : 0, rituels: typeof RITUELS !== "undefined" ? RITUELS.length : 0'
             '}) + "</pre>")</script>')
    s = page.read_text(encoding="utf-8")
    i = s.rfind("</body>")
    with tempfile.TemporaryDirectory() as t:
        copie = Path(t) / "page.html"; copie.write_text(s[:i] + sonde + s[i:] if i >= 0 else s + sonde, encoding="utf-8")
        try:
            r = subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-first-run", f"--user-data-dir={t}/profil",
                                "--virtual-time-budget=8000", "--dump-dom", copie.as_uri()], capture_output=True, text=True, timeout=120)
        except (OSError, subprocess.TimeoutExpired) as e: avertir(f"Chrome : {e} ; outils et rituels inchangés"); return {}
    m = re.search(r'<pre id="glacis-chiffres">(.*?)</pre>', r.stdout)
    if not m: avertir("comptes absents de la page ouverte dans Chrome : outils et rituels inchangés"); return {}
    d = json.loads(html.unescape(m.group(1)))
    return {k: str(d[k]) for k in ("outils", "rituels") if isinstance(d.get(k), int) and d[k] > 0}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--site", default="_site"); ap.add_argument("--montrer", action="store_true")
    a = ap.parse_args()
    site = (ICI / a.site) if not Path(a.site).is_absolute() else Path(a.site)
    page = site / "index.html"
    v = valeurs(site)
    print("chiffres :", ", ".join(f"{k} = {len(x) if k == 'applis' else x[:16] if k == 'sha256' else x}" for k, x in v.items()))
    if a.montrer: return
    s = page.read_text(encoding="utf-8")
    scripts = re.findall(r"<script>(.*?)</script>", s, re.S)
    inconnus = set()
    def remplacer(m):
        if m.group(1) not in v: inconnus.add(m.group(1)); return m.group(0)
        return f"<!--C:{m.group(1)}-->{html.escape(v[m.group(1)])}<!--/C-->"
    s = re.sub(r"<!--C:(\w+)-->(.*?)<!--/C-->", remplacer, s, flags=re.S)
    if inconnus - {"poids", "outils", "rituels"}: sys.exit(f"index.html : repères inconnus {sorted(inconnus)}")
    def bloc(nom, contenu):
        nonlocal s
        s, n = re.subn(f"<!--{nom}-->.*?<!--/{nom}-->", lambda m: f"<!--{nom}-->{contenu}<!--/{nom}-->", s, flags=re.S)
        if n != 1: sys.exit(f"index.html : repères <!--{nom}--> absents ou en double")
    if "lien" in v:
        bloc("TELECHARGER", f'<a class="bouton" href="{html.escape(v["lien"], quote=True)}">Télécharger Glacis {html.escape(v["version"])} pour Windows</a>'
             + ('<span class="pastille essai">Version d\'essai</span>' if v["canal"] == "essai" else ""))
        bloc("EMPREINTE", f'Glacis {html.escape(v["version"])} · {v["poids"]}&nbsp;Mo · empreinte SHA-256&nbsp;: <code>{v["sha256"]}</code>')
    if v["applis"]:
        s, n = re.subn(r"<!--APPLIS-->.*?<!--/APPLIS-->", lambda m: "<!--APPLIS-->" + "".join(map(carte_appli, v["applis"])) + "\n      <!--/APPLIS-->", s, flags=re.S)
        if n != 1: sys.exit("index.html : repères <!--APPLIS--> absents ou en double")
        s, n = re.subn(r'<section id="applis" hidden>', '<section id="applis">', s)
        if n != 1: sys.exit('index.html : <section id="applis" hidden> absent')
    if re.findall(r"<script>(.*?)</script>", s, re.S) != scripts: sys.exit("chiffres : un script de la page a changé (politique de contenu)")
    page.write_text(s, encoding="utf-8")
    print(f"{page.relative_to(ICI) if page.is_relative_to(ICI) else page} : chiffres de la version {v['version']} ({v['canal']}) écrits")


if __name__ == "__main__":
    main()
