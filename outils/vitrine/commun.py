"""Réglages communs aux outils de la vitrine (voir LISEZ-MOI.md) : où est la page de Glacis, où travailler."""
import os, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
TRAVAIL = pathlib.Path(__file__).resolve().parent / "_travail"          # images intermédiaires, ignoré par Git
VITRINE = RACINE / "vitrine"                                            # ce que le site publie
CHROME = os.environ.get("CHROME")                                       # chemin d'un Chromium particulier (facultatif)
_page = next((RACINE / c / "Glacis.html" for c in ("stable", "essai") if (RACINE / c / "Glacis.html").is_file()), None)
PAGE = _page.as_uri() if _page else None
DEMO = PAGE and PAGE + "?classe-demo"                                   # classe de démonstration : prénoms fictifs, rien d'enregistré
CACHE = "#demoRuban{display:none!important}.toast{display:none!important}"   # ruban de la démonstration et messages, hors champ
ARGS = ["--allow-file-access-from-files", "--force-color-profile=srgb"]

def lancer(p):
    return p.chromium.launch(executable_path=CHROME, args=ARGS) if CHROME else p.chromium.launch(args=ARGS)

async def ouvrir(p, w=1440, h=810, dsf=1, url=None, **kw):
    b = await lancer(p)
    c = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=dsf, **kw)
    pg = await c.new_page(); pg.errs = []
    pg.on("pageerror", lambda e: pg.errs.append(str(e)))
    await pg.goto(url or DEMO); await pg.wait_for_timeout(2200)
    await pg.add_style_tag(content=CACHE)
    return b, c, pg
