"""Filme la vraie application, image par image, dans sa classe de démonstration (prénoms fictifs).
L'horloge de la page est pilotée (30 images par seconde) : le film est fluide quel que soit le poste qui le fabrique.
Usage : python outils/vitrine/filmer.py [ouverture document accueil appel assistant problemes numeration geometrie lignages
        operations minuteur balancenb droite fractions reglettes]   (voir LISEZ-MOI.md ; BROUILLON=1 : une image sur dix)"""
import sys, os
import asyncio, pathlib, shutil, subprocess, datetime, math
from playwright.async_api import async_playwright
from commun import DEMO, CACHE, TRAVAIL, lancer
FPS=30; DT=1000/FPS
BROUILLON=bool(os.environ.get("BROUILLON"))
CURSEUR="""
(()=>{const c=document.createElement('div');c.id='__cur';c.style.cssText='position:fixed;left:0;top:0;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:rgba(47,79,168,.28);border:2px solid rgba(255,255,255,.95);box-shadow:0 2px 8px rgba(31,45,85,.35);pointer-events:none;z-index:2147483647;opacity:0;will-change:transform';
document.documentElement.appendChild(c);
const p=e=>{c.style.transform=`translate(${e.clientX}px,${e.clientY}px) scale(${e.buttons? .78:1})`;c.style.opacity=1;c.style.background=e.buttons?'rgba(47,79,168,.5)':'rgba(47,79,168,.28)'};
for(const t of ['pointermove','pointerdown','pointerup'])window.addEventListener(t,p,true);})()
"""
AVANCE="""(dt)=>{for(const a of document.getAnimations()){try{if(a.playState==='finished')continue;if(!a.__f){a.__f=1;a.pause();}
 const fin=a.effect&&a.effect.getComputedTiming().endTime;const t=(a.currentTime||0)+dt;
 if(Number.isFinite(fin)&&t>=fin){a.finish();}else a.currentTime=t;}catch(e){}}}"""
class Film:
    def __init__(s,nom,w=1280,h=720,dsf=1.5,url=None): s.nom=nom;s.w=w;s.h=h;s.dsf=dsf;s.n=0;s.clip=None;s.x=w*.5;s.y=h*.6;s.url=url
    async def __aenter__(s):
        s.p=await async_playwright().start()
        s.b=await lancer(s.p)
        s.c=await s.b.new_context(viewport={"width":s.w,"height":s.h},device_scale_factor=s.dsf)
        s.pg=await s.c.new_page(); s.errs=[]
        s.pg.on("pageerror",lambda e:s.errs.append(str(e)))
        await s.pg.clock.install()
        await s.pg.goto(s.url or DEMO); await s.pg.wait_for_timeout(2500)
        await s.pg.add_style_tag(content=CACHE)
        await s.pg.evaluate(CURSEUR)
        s.dir=TRAVAIL/"images"/s.nom
        shutil.rmtree(s.dir,ignore_errors=True); s.dir.mkdir(parents=True)
        s.fige=False
        return s
    async def figer(s):
        if not s.fige:
            await s.pg.clock.pause_at(datetime.datetime.now()+datetime.timedelta(seconds=1)); s.fige=True
            await s.pg.evaluate(AVANCE,0)
    async def js(s,code): return await s.pg.evaluate(code)
    async def pas(s,n=1,photo=True):
        await s.figer()
        for _ in range(n):
            s.k=getattr(s,'k',0)+1; d=round(s.k*DT)-round((s.k-1)*DT)
            await s.pg.clock.run_for(d)
            await s.pg.evaluate(AVANCE,d)
            if photo and BROUILLON and s.k % 10: s.n+=0; continue      # brouillon : une image sur dix, pour régler un scénario
            if photo:
                kw={"clip":s.clip} if s.clip else {}
                await s.pg.screenshot(path=str(s.dir/f"{s.n:05d}.jpg"),type="jpeg",quality=93,**kw); s.n+=1
    async def avancer(s,ms): await s.pas(round(ms/DT),photo=False)   # sans filmer
    async def attendre(s,ms): await s.pas(round(ms/DT))
    async def vers(s,x,y,ms=600):
        n=max(2,round(ms/DT)); x0,y0=s.x,s.y
        for i in range(1,n+1):
            t=i/n; e=t*t*(3-2*t)
            s.x,s.y=x0+(x-x0)*e,y0+(y-y0)*e
            await s.pg.mouse.move(s.x,s.y); await s.pas()
    async def centre(s,sel,dx=.5,dy=.5):
        bb=await s.pg.locator(sel).first.bounding_box(); return bb["x"]+bb["width"]*dx,bb["y"]+bb["height"]*dy
    async def cadrer(s,sel,marge=28,ratio=1.5):
        bb=await s.pg.locator(sel).first.bounding_box()
        w=bb["width"]+2*marge; h=bb["height"]+2*marge
        if w/h<ratio: w=h*ratio
        else: h=w/ratio
        w=min(w,s.w); h=min(h,s.h)
        cx=bb["x"]+bb["width"]/2; cy=bb["y"]+bb["height"]/2
        x=min(max(0,cx-w/2),s.w-w); y=min(max(0,cy-h/2),s.h-h)
        s.clip={"x":round(x),"y":round(y),"width":2*round(w/2),"height":2*round(h/2)}; print(s.nom,"cadre",s.clip)
    async def plein(s): s.clip=None
    async def fichier(s,sel,chemin,ms=700):
        """Clic sur un bouton qui ouvre le choix d'un fichier : le fichier est fourni sans montrer la fenêtre du système."""
        await s.vers(*(await s.centre(sel)),ms); await s.attendre(150)
        for essai in range(3):
            try:
                async with s.pg.expect_file_chooser(timeout=6000) as fc:
                    await s.pg.mouse.down(); await s.pg.mouse.up(); await s.pas(8)
                break
            except Exception:
                if essai==2: raise
                await s.pg.mouse.move(*(await s.centre(sel))); await s.pas(4,photo=False)
        await (await fc.value).set_files(str(chemin)); await s.pas(12,photo=False)
    async def svgpt(s,expr,x,y):
        """Point d'un dessin SVG (coordonnées du dessin) vers l'écran."""
        return tuple(await s.pg.evaluate(f"([x,y])=>{{const p=new DOMPoint(x,y).matrixTransform(({expr}).getScreenCTM());return [p.x,p.y]}}",[x,y]))
    async def tracer(s,pts,ms=900):
        await s.vers(*pts[0],500); await s.attendre(100); await s.bas()
        for q in pts[1:]: await s.vers(*q,ms)
        await s.attendre(80); await s.haut()
    async def taper(s,texte,ms=70):
        for c in texte: await s.pg.keyboard.type(c); await s.attendre(ms)
    async def bas(s): await s.pg.mouse.down(); await s.pas(2)
    async def haut(s): await s.pg.mouse.up(); await s.pas(2)
    async def clic(s,sel=None,ms=600,apres=250):
        if sel: await s.vers(*(await s.centre(sel)),ms)
        await s.attendre(120); await s.bas(); await s.haut(); await s.attendre(apres)
    async def glisser(s,a,b,ms=800):
        await s.vers(*a,500); await s.attendre(100); await s.bas(); await s.vers(*b,ms); await s.attendre(80); await s.haut()
    async def __aexit__(s,*a):
        await s.b.close(); await s.p.stop()
        print(s.nom,s.n,"images",round(s.n/FPS,1),"s","erreurs:",s.errs[:3])
def encoder(nom,larg=1600,crf=27):
    from PIL import Image
    src=TRAVAIL/"images"/nom; out=TRAVAIL/"films"; out.mkdir(parents=True,exist_ok=True)
    larg=min(larg,Image.open(sorted(src.glob("*.jpg"))[0]).width)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(src/"%05d.jpg"),"-vf",f"scale={larg}:-2:flags=lanczos","-c:v","libx264","-preset","veryslow","-crf",str(crf),"-pix_fmt","yuv420p","-movflags","+faststart","-an",str(out/f"{nom}.mp4")],check=True)
    print(nom,(out/f"{nom}.mp4").stat().st_size//1024,"Ko")


# ---------- les scénarios ----------
ICI=pathlib.Path(__file__).resolve().parent
FICHE=ICI/"exemples"/"Compléments à 10.pdf"            # fiche d'exemple faite pour la démonstration (exemples/fiche.html)

async def ouverture():
    """Le film d'ouverture : l'écran d'accueil (la classe de démonstration l'attend avec « &depart », Glacis 6.0.0-beta.23
    et suivants), « Commencer », puis tout au même endroit, dans l'ordre d'une matinée : l'appel, un problème des rituels,
    le tableau de numération, le minuteur de la boîte à outils lancé puis réduit (il continue de tourner), l'Atelier,
    Préparer, et retour à l'Accueil. La navigation est épinglée (réglage du poste) : le nom de chaque fonction est écrit
    sous sa tuile. Sur la page, ce film se dépose sur le voile qui recouvre le tableau blanc (index.html, .ouv)."""
    async with Film("ouverture", url=DEMO + "&depart") as f:
        await f.js("(g=>{let x=g;Math.random=()=>(x=(x*1664525+1013904223)%4294967296)/4294967296})(7),"
                   "(Navigation.epinglee()||Navigation.basculerEpingle()),Tableau.regler(t=>t.type='maths'),0")
        if await f.js("demarre"): raise SystemExit("ouverture : la page démarre seule (Glacis 6.0.0-beta.23 ou plus récent nécessaire)")
        f.x,f.y=880,640
        await f.attendre(800)                                              # l'écran d'accueil, immobile : raccord avec le voile
        await f.clic("#btnStart",ms=800,apres=1000)                        # « Commencer » : l'Accueil
        await f.clic("#chipPresents",ms=600,apres=800)                     # l'appel, depuis la barre du haut
        await f.clic("#p-appel .tag:has-text('Chloé')",ms=450,apres=350)
        await f.clic("#apVal",ms=450,apres=300)
        await f.clic('#p-appel button[title="Fermer"]',ms=450,apres=250)
        await f.clic('#side [data-act="rituels"]',ms=550,apres=350)        # les rituels : un problème du jour
        await f.clic('[data-o="pb"]',ms=450,apres=1100)
        await f.clic('#side [data-act="tableau"]',ms=550,apres=1000)       # les tableaux : la numération
        await f.clic("#boPoignee",ms=550,apres=450)                        # la boîte à outils : le minuteur
        await f.clic('#p-outils [data-o="minuteur"]',ms=450,apres=450)
        await f.clic("#mnGo",ms=400,apres=600)
        await f.clic("#p-minuteur .pRed",ms=400,apres=400)                 # réduit, il continue de tourner
        await f.clic('#side [data-act="atelier"]',ms=550,apres=1000)       # l'Atelier
        await f.clic('#side [data-act="preparer"]',ms=500,apres=900)       # Préparer
        await f.clic('#side [data-act="journee"]',ms=550,apres=1500)       # retour à l'Accueil
    encoder("ouverture")

async def document():
    """Un document joint à une activité dans Préparer : il s'ouvre d'un clic, au bon moment, sur l'Accueil."""
    async with Film("document") as f:
        await f.js("Preparer.ouvrir('jour', new Date(2026,10,9)),0"); await f.avancer(1500)
        i=await f.js("[...document.querySelectorAll('#apPrep .jxR')].find(r=>r.textContent.replace(/\\s+/g,' ').trim().startsWith('10 h 30 Maths')).dataset.i")
        L=f'#apPrep .jxR[data-i="{i}"]'
        await f.js(f"document.querySelector('{L}').scrollIntoView({{block:'center'}}),0"); await f.avancer(400)
        f.x,f.y=640,560; await f.attendre(600)
        await f.fichier(L+' [data-ra="doc"]',FICHE,900)
        await f.js(f"document.querySelector('{L}').scrollIntoView({{block:'center'}}),0"); await f.attendre(1500)
        await f.clic('#side [data-act="journee"]',ms=900,apres=1300)
        await f.clic("#nowMat .nowRess .rsN",ms=900,apres=2600)
        await f.clic(".panel[id^=p-doc-] button[title^='Plein cadre']",ms=900,apres=2600)
    encoder("document")

async def accueil():
    """L'Accueil se compose : changer une taille, ajouter des widgets."""
    async with Film("accueil") as f:
        await f.attendre(500)
        await f.clic("#wgModifier",ms=900,apres=700)
        await f.clic('.wg-maintenant .wgTailles [data-taille="moyen"]',ms=800,apres=800)
        await f.clic("#wgAjouter",ms=800,apres=900)
        for w in ("horloge","date"):
            await f.js(f"document.querySelector('#p-widgets [data-ajout=\"{w}\"]').scrollIntoView({{block:'center'}}),0"); await f.pas(4)
            await f.clic(f'#p-widgets [data-ajout="{w}"]',ms=600,apres=700)
        await f.clic("#p-widgets .pClose, #p-widgets button[title^=Fermer]",ms=600,apres=600)
        h=await f.centre(".wg-horloge"); d=await f.centre(".wg-date")
        await f.glisser(h,d,900); await f.attendre(700)
        await f.clic("button:has-text('Terminé')",ms=700,apres=2200)
    encoder("accueil")

async def appel():
    """L'activité validée, puis l'appel et la cantine depuis la barre du haut."""
    async with Film("appel") as f:
        await f.attendre(500)
        await f.clic("#chipPresents",ms=1000,apres=1100)
        await f.clic("#p-appel .tag:has-text('Chloé')",ms=800,apres=600)
        await f.clic("#apVal",ms=800,apres=1200)
        await f.clic("#chipCantine",ms=900,apres=1200)
        await f.clic("#p-cantine .tag:has-text('David'), #p-cantine button:has-text('David'), #p-cantine :text-is('David')",ms=800,apres=600)
        await f.clic("#cnOk",ms=800,apres=1800)
    encoder("appel")

async def assistant():
    """L'assistant : il s'ouvre au survol et propose les tutoriels de l'écran affiché."""
    async with Film("assistant") as f:
        await f.js("Tableau.ouvrir('maths'),0"); await f.avancer(1400)
        f.x,f.y=500,420; await f.attendre(500)
        await f.vers(*(await f.centre("#asPoignee")),900); await f.attendre(1500)
        await f.bas(); await f.haut(); await f.attendre(1200)
        await f.clic("#asGuides :text('Manipuler unités et dizaines')",ms=800,apres=2200)
        print("tutoriel :",await f.js("[...document.querySelectorAll('button')].filter(b=>b.offsetParent&&/Suivant|Terminer|Précédent|Quitter/.test(b.textContent)).map(b=>(b.id||b.className)+'/'+b.textContent.trim()).join(' ; ')"))
        for _ in range(2):
            try: await f.clic("button:has-text('Suivant'):visible",ms=700,apres=2000)
            except Exception as e: print("suivant",str(e)[:80]); break
    encoder("assistant")

async def problemes():
    """Un problème : manipuler, se le représenter, puis corriger."""
    async with Film("problemes") as f:
        graine=int(os.environ.get("GRAINE","7"))
        await f.js("(g=>{let x=g;Math.random=()=>(x=(x*1664525+1013904223)%4294967296)/4294967296})("+str(graine)+"),Rituels.ouvrir(),0"); await f.avancer(1000)
        await f.pg.locator("button:has-text('Problèmes')").first.click(); await f.avancer(1200)
        print("énoncé :",await f.js("document.querySelector('.pbEnonce, .pbTexte, #ritZone')?.textContent.trim().replace(/\\s+/g,' ').slice(0,160)"))
        f.x,f.y=640,560; await f.attendre(700)
        await f.clic("#pbManip",ms=900,apres=1100)
        z=await f.js("(()=>{const r=document.querySelector('#pbMpZone').getBoundingClientRect();return [r.x,r.y,r.width,r.height]})()")
        j=await f.js("[...document.querySelectorAll('#pbMpZone .mnpI')].map(e=>{const r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]})")
        print("zone",z,"jetons",len(j),j[:4])
        n=min(3,max(1,len(j)-2))
        for k in range(n):
            cible=(z[0]+70+k*52,z[1]+z[3]-48) if z else (j[k][0]-150+k*48,j[k][1]+80)
            await f.glisser(tuple(j[k]),cible,650); await f.attendre(250)
        await f.attendre(500)
        await f.clic("button:has-text('Représentation')",ms=900,apres=1400)
        await f.clic("#pbIllu",ms=700,apres=1500)
        await f.clic("button:has-text('Correction')",ms=800,apres=2600)
    encoder("problemes")

async def numeration():
    """Casser une dizaine en dix unités, puis refaire un paquet de dix en l'entourant."""
    async with Film("numeration") as f:
        await f.js("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('maths'),0"); await f.avancer(1500)
        await f.attendre(500)
        bb=await f.js("(()=>{const e=document.querySelector('.mnp').children[1].getBoundingClientRect();return [e.x,e.y,e.width,e.height]})()")   # la dizaine de droite : de la place autour pour l'entourer
        c=(bb[0]+bb[2]/2,bb[1]+bb[3]/2)
        await f.vers(*c,800); await f.attendre(150); await f.bas(); await f.haut(); await f.attendre(400)
        await f.clic("#acCasser",ms=900,apres=2300)
        await f.clic("#acPaquet",ms=700,apres=500)
        bb=await f.js("(()=>{const r=[...document.querySelector('.mnp').children].map(e=>e.getBoundingClientRect()).filter(r=>r.width<40&&r.width>4);const x0=Math.min(...r.map(a=>a.left)),y0=Math.min(...r.map(a=>a.top)),x1=Math.max(...r.map(a=>a.right)),y1=Math.max(...r.map(a=>a.bottom));return [x0,y0,x1-x0,y1-y0,r.length]})()")
        print("unités à entourer",bb)
        zn=await f.pg.locator("#tbFond .mnp").bounding_box()       # le tracé doit commencer et rester dans la zone du matériel
        m=18; x0,y0,x1,y1=max(bb[0]-m,zn["x"]+4),max(bb[1]-m,zn["y"]+4),bb[0]+bb[2]+m,bb[1]+bb[3]+m
        tour=[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0+4)]
        await f.vers(*tour[0],700); await f.attendre(100); await f.bas()
        for q in tour[1:]: await f.vers(*q,420)
        await f.haut(); await f.attendre(2600)
    encoder("numeration")

async def geometrie():
    """On sort une règle, on la déplace, on trace un trait le long de son bord."""
    async with Film("geometrie") as f:
        await f.js("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('geometrie'),0"); await f.avancer(1500)
        f.x,f.y=640,380; await f.attendre(500)
        await f.clic("#geo-regle",ms=900,apres=500)
        await f.clic('.geoPalette [data-taille="15"]',ms=500,apres=900)
        fig=await f.js("Geometrie.p().figures.at(-1)"); print("regle",fig)
        S="Geometrie.svg"
        a=await f.svgpt(S,fig["x"]+380,fig["y"]+35); b=await f.svgpt(S,fig["x"]+520,fig["y"]-150)
        await f.glisser(a,b,900); await f.attendre(600)
        fig=await f.js("Geometrie.p().figures.at(-1)"); print("regle déplacée",fig)
        await f.clic("#geoCrayon",ms=900,apres=500)
        await f.clic('.geoPalette [data-geo-c="#2f6fd6"]',ms=500,apres=500)
        d=await f.svgpt(S,fig["x"]+75,fig["y"]-3); e=await f.svgpt(S,fig["x"]+650,fig["y"]-3)
        await f.tracer([d,e],1300); await f.attendre(400)
        print("figures",await f.js("Geometrie.p().figures.map(x=>x.type).join()+' | '+Object.keys(Geometrie.p()).join()"))
        g=await f.svgpt(S,fig["x"]+380,fig["y"]+35); h=await f.svgpt(S,fig["x"]+330,fig["y"]+250)
        await f.glisser(g,h,1000); await f.attendre(1800)          # la règle s'écarte : le trait reste
    encoder("geometrie")

async def lignages():
    """Les lignages : la réglure grandit, le support change (tableau, cahier, feuille)."""
    async with Film("lignages") as f:
        await f.js("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('lignes'),0"); await f.avancer(1500)
        f.x,f.y=640,420; await f.attendre(600)
        cur=await f.pg.locator("#tbOpts input[type=range]").first.bounding_box()
        y=cur["y"]+cur["height"]/2
        await f.glisser((cur["x"]+cur["width"]*.42,y),(cur["x"]+cur["width"]*.92,y),1200); await f.attendre(900)
        await f.clic("#tbOpts button:has-text('Cahier A5')",ms=800,apres=1500)
        await f.clic("#tbOpts button:has-text('Feuille A4')",ms=600,apres=1500)
        await f.clic("#tbOpts button:has-text('Tableau')",ms=600,apres=1200)
    encoder("lignages")

async def operations():
    """Une soustraction par dégroupement, avec le matériel de numération qui suit chaque étape."""
    async with Film("operations") as f:
        await f.js("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('ops'),0"); await f.avancer(1200)
        await f.js("OpsTab.regler(x=>{x.op='cas';x.a='342';x.b='165';x.illus=true;x.explic=false;x.taille=7}),OpsTab.options(document.querySelector('#tbOpts')),OpsTab.rendre(),0"); await f.avancer(800)
        n=await f.js("OpsTab.g.etapes.length"); print("étapes",n)
        f.x,f.y=640,600; await f.attendre(900)
        for k in range(n):
            await f.pg.keyboard.press("Space"); await f.attendre(1150)
        await f.attendre(1500)
    encoder("operations")

async def _outil(f,o,panneau):
    await f.js("Outils.ouvrir(),0"); await f.avancer(900)
    await f.attendre(400)
    await f.clic(f'#p-outils [data-o="{o}"]',ms=800,apres=1200)
    return await f.pg.locator(panneau).bounding_box()

async def _reduire(f,panneau):
    await f.clic(panneau+" .pRed",ms=800,apres=1500)

async def minuteur():
    """Le minuteur : une durée, on démarre, on le réduit en bas de l'écran, on le rouvre."""
    async with Film("minuteur") as f:
        f.x,f.y=640,520
        await _outil(f,"minuteur","#p-minuteur")
        await f.clic("#p-minuteur button:text-is('5 min')",ms=800,apres=700)
        await f.clic("#mnGo",ms=700,apres=3400)
        await _reduire(f,"#p-minuteur"); await f.attendre(1800)
        await f.clic("#fenRed .fenP",ms=800,apres=2000)
    encoder("minuteur")

async def balancenb():
    """La balance des nombres : 6 d'un côté, 2 et 4 de l'autre, le fléau revient à l'équilibre."""
    async with Film("balancenb") as f:
        f.x,f.y=640,560
        await _outil(f,"balanceNb","#p-balanceNb")
        async def reserve():
            r=await f.pg.locator("#p-balanceNb .blRes").bounding_box(); return (r["x"]+r["width"]/2,r["y"]+r["height"]*.4)
        async def crochet(k):
            c=await f.js("[...document.querySelectorAll('#p-balanceNb .blCr')].map(e=>{const r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height*.7]}).sort((a,b)=>a[0]-b[0])")
            return tuple(c[k])
        for k,pause in ((4,1700),(11,1500),(13,2600)):       # 6 à gauche ; 2 puis 4 à droite
            await f.glisser(await reserve(),await crochet(k),850); await f.attendre(pause)
        await _reduire(f,"#p-balanceNb"); await f.attendre(1200)
    encoder("balancenb")

async def droite():
    """La droite graduée : des bonds tracés d'une graduation à l'autre."""
    async with Film("droite") as f:
        f.x,f.y=640,560
        await _outil(f,"droite","#p-droite")
        await f.clic('#p-droite [data-dm="bonds"]',ms=800,apres=600)
        async def grad(n):
            r=await f.pg.locator("#p-droite .drHit").nth(n).bounding_box(); return (r["x"]+r["width"]/2,r["y"]+r["height"]/2)
        await f.glisser(await grad(4),await grad(10),1000); await f.attendre(900)
        await f.glisser(await grad(10),await grad(13),800); await f.attendre(1600)
        await _reduire(f,"#p-droite"); await f.attendre(1200)
    encoder("droite")

async def fractions():
    """Les fractions : la bande, le disque, puis deux fractions à comparer."""
    async with Film("fractions") as f:
        f.x,f.y=640,560
        await _outil(f,"fractions","#p-fractions")
        await f.attendre(600)
        await f.clic("#p-fractions .btn:has-text('Disque')",ms=800,apres=1300)
        await f.clic("#p-fractions .btn.mini:has-text('−')",ms=700,apres=900)
        await f.clic("#p-fractions .btn:has-text('Bande')",ms=700,apres=900)
        await f.clic("#frCmp",ms=700,apres=2400)
        await _reduire(f,"#p-fractions"); await f.attendre(1200)
    encoder("fractions")

async def reglettes():
    async with Film("reglettes") as f:
        f.x,f.y=640,520
        await _outil(f,"reglettes","#p-reglettes")
        async def prendre(v):
            bb=await f.pg.locator(f".rgPioche[data-v='{v}'] .rgR").bounding_box(); return (bb["x"]+bb["height"]/2,bb["y"]+bb["height"]/2)
        async def case(x,y,dx=.5):
            return tuple(await f.pg.evaluate(f"(()=>{{const r=Reglettes.plan().getBoundingClientRect(),G=Reglettes.geo;return [r.left+G.ox+({x}+{dx})*G.u,r.top+G.oy+({y}+.5)*G.u]}})()"))
        await f.glisser(await prendre(10),await case(1,1),900); await f.attendre(500)
        await f.glisser(await prendre(6),await case(1,3),900); await f.attendre(400)
        await f.glisser(await prendre(4),await case(7,3),900); await f.attendre(800)
        await f.clic("#rgCalc",ms=700,apres=1300)
        await f.clic("#rgEsc",ms=600,apres=2600)
        await _reduire(f,"#p-reglettes"); await f.attendre(1200)
    encoder("reglettes")

FILMS={"ouverture":ouverture,"document":document,"accueil":accueil,"appel":appel,"assistant":assistant,"problemes":problemes,"numeration":numeration,"geometrie":geometrie,"lignages":lignages,"operations":operations,"minuteur":minuteur,"balancenb":balancenb,"droite":droite,"fractions":fractions,"reglettes":reglettes}
if __name__=="__main__":
    for nom in sys.argv[1:] or FILMS: asyncio.run(FILMS[nom]())
