"""Réécrit les chiffres et les cartes des applis de la page de présentation (_site/index.html), à chaque publication.

Règle (Franck, 21 novembre 2026) : la page ne parle que de la version publiée, et ses chiffres suivent chaque publication.
Dès qu'une version stable existe (entrees/stable.json), on ne parle que d'elle et de son poids ; avant, de la version
d'essai.

Sources, pour le canal retenu :
  · version : entrees/<canal>.json ;
  · poids de l'installateur Windows : _site/appli/<sous-dossier>/*.exe, rangé par « Ranger les installateurs fabriqués »
    (lancer ce script APRÈS cette étape) ; affiché en Mo comme Windows le montre (1 Mo = 1 048 576 octets) ;
  · outils, rituels, applis : vitrine/donnees/<canal>.json, écrit avec la page par la publication du dépôt source
    ({"version", "outils", "rituels", "applis": [{id, nom, version, description, couleur, categorie, icone (SVG)}]}).
Une source absente ou d'une autre version : la valeur déjà écrite dans index.html reste, avec un avertissement
(l'action continue : la page reste en ligne).

Le lien de téléchargement (repères TELECHARGER) et l'empreinte SHA-256 de l'installateur (repères EMPREINTE) sont écrits
aussi dans la page : sans script (robots, assistants qui lisent la page), on voit le vrai lien, pas « Bientôt disponible ».

Repères dans index.html : <!--C:nom-->valeur<!--/C--> (nom : version, poids, outils, rituels), <!--APPLIS-->…<!--/APPLIS-->,
<!--TELECHARGER-->…<!--/TELECHARGER--> et <!--EMPREINTE-->…<!--/EMPREINTE-->.
Ils sont hors des scripts : les empreintes de la politique de contenu (_headers, outils/signer.py) ne changent pas, et ce
script le vérifie.

Usage : python outils/chiffres.py [--site _site] [--montrer]   (--montrer : affiche les valeurs sans rien écrire)
"""
import argparse, base64, hashlib, html, json, re, sys
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
    icone = "data:image/svg+xml;base64," + base64.b64encode(a["icone"].encode("utf-8")).decode()
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
    f = ICI / "vitrine" / "donnees" / f"{canal}.json"
    d = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else None
    if d is None: avertir(f"vitrine/donnees/{canal}.json absent : outils, rituels et applis inchangés")
    elif d.get("version") != entree["version"]: avertir(f"vitrine/donnees/{canal}.json est celui de la {d.get('version')}, pas de la {entree['version']} : outils, rituels et applis inchangés")
    else:
        for k in ("outils", "rituels"):
            if isinstance(d.get(k), int) and d[k] > 0: v[k] = str(d[k])
        if isinstance(d.get("applis"), list): v["applis"] = d["applis"]
    return v


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
    if "applis" in v:
        s, n = re.subn(r"<!--APPLIS-->.*?<!--/APPLIS-->", lambda m: "<!--APPLIS-->" + "".join(map(carte_appli, v["applis"])) + "\n      <!--/APPLIS-->", s, flags=re.S)
        if n != 1: sys.exit("index.html : repères <!--APPLIS--> absents ou en double")
    if re.findall(r"<script>(.*?)</script>", s, re.S) != scripts: sys.exit("chiffres : un script de la page a changé (politique de contenu)")
    page.write_text(s, encoding="utf-8")
    print(f"{page.relative_to(ICI) if page.is_relative_to(ICI) else page} : chiffres de la version {v['version']} ({v['canal']}) écrits")


if __name__ == "__main__":
    main()
