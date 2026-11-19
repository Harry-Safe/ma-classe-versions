"""Captures fixes de l'application (classe de démonstration) et tuiles des outils. Usage : python outils/vitrine/captures.py [noms]"""
import asyncio, re, sys
from playwright.async_api import async_playwright
from commun import *
W,H,D=1440,810,2
async def prise(p,nom,fn,url=None):
    b,c,pg=await ouvrir(p,W,H,D,url=url)
    try:
        await fn(pg); await pg.wait_for_timeout(900)
        await pg.screenshot(path=str(TRAVAIL/"captures"/f"{nom}.png")); print(nom,"ok",pg.errs[:2])
    except Exception as e: print(nom,"ERR",str(e)[:300])
    await b.close()
async def semaine(pg): await pg.evaluate("Preparer.ouvrir('semaine'),0"); await pg.wait_for_timeout(1500)
async def appel(pg): await pg.evaluate("PanneauAppel.ouvrir(),0"); await pg.wait_for_timeout(1200)
async def rien(pg): await pg.wait_for_timeout(500)
async def ops(pg):
    await pg.evaluate("Tableau.ouvrir('ops'),0"); await pg.wait_for_timeout(1200)
    for _ in range(3): await pg.click("button:has-text('Étape suivante')"); await pg.wait_for_timeout(500)
async def geo(pg):
    await pg.evaluate("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('geometrie'),0"); await pg.wait_for_timeout(1200)
    await pg.evaluate("document.querySelector('#geo-regle').click()"); await pg.wait_for_timeout(400)
    await pg.evaluate("document.querySelector('.geoPalette [data-taille=\"15\"]').click()"); await pg.wait_for_timeout(500)
    await pg.mouse.move(720,440); await pg.mouse.down(); await pg.mouse.move(800,600,steps=12); await pg.mouse.up(); await pg.wait_for_timeout(400)
    await pg.evaluate("document.querySelector('#geo-equerre').click()"); await pg.wait_for_timeout(400)
    await pg.evaluate("document.querySelector('.geoPalette [data-taille=\"10\"]').click()"); await pg.wait_for_timeout(500)
    await pg.mouse.move(40,300); await pg.wait_for_timeout(300)
async def ecriture(pg):
    await pg.click('.sbtn:has-text("Préparer")'); await pg.wait_for_timeout(700)
    await pg.click('[data-pt="ecriture"]'); await pg.wait_for_timeout(1200)
    await pg.locator(".meLi input").nth(0).fill("Le chat dort sur le tapis."); await pg.wait_for_timeout(600)
async def outils(pg): await pg.evaluate("Outils.ouvrir(),0"); await pg.wait_for_timeout(1500)
async def lignes(pg): await pg.evaluate("Tableau.ouvrir('lignes'),0"); await pg.wait_for_timeout(1200)
async def minuteur(pg): await pg.evaluate("Minuteur.ouvrir(),0"); await pg.wait_for_timeout(1000)
async def icones(pg):
    """Tuiles des outils : relevées dans le menu Outils (nom, couleurs du fond, dessin SVG de outils/icones-illustrees.js),
    pas photographiées ; la page les redessine avec les mêmes règles que Glacis (voir ranger.py)."""
    import json
    await pg.evaluate("Outils.ouvrir(),0"); await pg.wait_for_timeout(1500)
    r=await pg.evaluate("""[...document.querySelectorAll('#p-outils [data-o]')].map(b=>{const t=b.querySelector('.outIllu');if(!t)return null;
      return {o:b.dataset.o,nom:b.querySelector('b').textContent.trim(),g1:t.style.getPropertyValue('--g1').trim(),g2:t.style.getPropertyValue('--g2').trim(),
      dessin:t.querySelector('svg').innerHTML}}).filter(Boolean)""")
    assert r and all(x["g1"] and x["g2"] and x["dessin"] for x in r), "tuiles des outils introuvables dans le menu Outils"
    assert not any(re.search(r'\bid=|url\(#', x["dessin"]) for x in r), "un dessin porte un identifiant : il ne peut pas être inséré tel quel"
    (TRAVAIL/"captures"/"icones.json").write_text(json.dumps(r,ensure_ascii=False,indent=1),encoding="utf-8")
    print("ICONES",len(r),[x["o"] for x in r])
async def main():
    (TRAVAIL/"captures").mkdir(parents=True,exist_ok=True)
    async with async_playwright() as p:
        todo=sys.argv[1:] or ["accueil","soir","semaine","icones"]        # les autres (appel, ops, geo…) restent disponibles à la demande
        f={"accueil":rien,"semaine":semaine,"appel":appel,"ops":ops,"geo":geo,"ecriture":ecriture,"outils":outils,"lignes":lignes,"minuteur":minuteur,"icones":icones}
        for n in todo:
            if n=="soir": await prise(p,"soir",rien,url=DEMO+"=1&t=2026-11-09T16:45")
            else: await prise(p,n,f[n])
asyncio.run(main())
