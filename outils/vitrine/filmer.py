"""Filme la vraie application, image par image, dans sa classe de démonstration (prénoms fictifs).
L'horloge de la page est pilotée (30 images par seconde) : le film est fluide quel que soit le poste qui le fabrique.
Usage : python outils/vitrine/filmer.py [journee rituels numeration balance monnaie reglettes]   (voir LISEZ-MOI.md)"""
import sys
import asyncio, pathlib, shutil, subprocess, datetime, math
from playwright.async_api import async_playwright
from commun import DEMO, CACHE, TRAVAIL, lancer
FPS=30; DT=1000/FPS
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
    def __init__(s,nom,w=1280,h=720,dsf=1.5): s.nom=nom;s.w=w;s.h=h;s.dsf=dsf;s.n=0;s.clip=None;s.x=w*.5;s.y=h*.6
    async def __aenter__(s):
        s.p=await async_playwright().start()
        s.b=await lancer(s.p)
        s.c=await s.b.new_context(viewport={"width":s.w,"height":s.h},device_scale_factor=s.dsf)
        s.pg=await s.c.new_page(); s.errs=[]
        s.pg.on("pageerror",lambda e:s.errs.append(str(e)))
        await s.pg.clock.install()
        await s.pg.goto(DEMO); await s.pg.wait_for_timeout(2500)
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

async def journee():
    async with Film("journee") as f:
        await f.attendre(700)
        await f.clic("button.prim:has-text('Valider')",ms=900,apres=1500)
        await f.vers(*(await f.centre(".sbtn:has-text('Élèves')")),900); await f.attendre(350)
        await f.bas(); await f.haut(); await f.attendre(1100)
        await f.clic("button:has-text('Tirer au sort')",ms=800,apres=3000)
        await f.attendre(600)
    encoder("journee")

async def rituels():
    async with Film("rituels") as f:
        await f.js("Rituels.ouvrir(),0"); await f.avancer(1500)
        await f.attendre(600)
        await f.clic("#flSuiv",ms=900,apres=1900)
        for _ in range(3): await f.clic("#flSuiv",ms=200,apres=1900)
        await f.attendre(400)
    encoder("rituels")

async def numeration():
    async with Film("numeration") as f:
        await f.js("Store.get('prefs').dockEpingle=true;Tableau.ouvrir('maths'),0"); await f.avancer(1500)
        await f.attendre(500)
        await f.vers(*(await f.centre('[data-pr="u"][data-s="1"]')),800)
        for _ in range(4): await f.bas(); await f.haut(); await f.attendre(330)
        await f.attendre(400)
        bb=await f.pg.evaluate("(()=>{const e=document.querySelector('.mnp').firstElementChild.getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]})()")
        await f.vers(*bb,800); await f.attendre(150); await f.bas(); await f.haut(); await f.attendre(400)
        await f.clic("#acCasser",ms=900,apres=3000)
    encoder("numeration")

async def balance():
    async with Film("balance",dsf=2) as f:
        await f.js("Balance.g=[];Balance.d=[];Balance.regler(x=>{x.mode='masses';x.totaux=true;});Balance.ouvrir(),0")
        await f.avancer(1300); await f.cadrer("#p-balance")
        sc=await f.pg.locator("#p-balance .balScene").bounding_box()
        G=(sc["x"]+sc["width"]*.25,sc["y"]+sc["height"]*.45); D=(sc["x"]+sc["width"]*.75,sc["y"]+sc["height"]*.45)
        f.x,f.y=sc["x"]+sc["width"]*.5,sc["y"]+sc["height"]*.8
        await f.attendre(400)
        await f.glisser(await f.centre('#p-balance .balJt[data-bp="6"]'),G); await f.attendre(1700)
        await f.glisser(await f.centre('#p-balance .balJt[data-bp="5"]'),D); await f.attendre(1300)
        await f.glisser(await f.centre('#p-balance .balJt[data-bp="5"]'),D); await f.attendre(2800)
    encoder("balance",1400)

async def monnaie():
    async with Film("monnaie",dsf=2) as f:
        await f.js("Monnaie.regler(x=>{x.centimes=false;x.grands=false;x.total=true;});Monnaie.tapis=[];Monnaie.ouvrir(),0")
        await f.avancer(1300); await f.cadrer("#p-monnaie")
        z=await f.pg.locator("#mnTapis").bounding_box(); f.x,f.y=z["x"]+z["width"]*.5,z["y"]+z["height"]*.7
        await f.attendre(300)
        await f.vers(*(await f.centre('.mnR[data-v="100"]')),700)
        for _ in range(10): await f.bas(); await f.haut(); await f.attendre(170)
        await f.attendre(900)
        await f.clic("#mnEch",ms=700,apres=3400)
    encoder("monnaie",1400)

async def reglettes():
    async with Film("reglettes",dsf=2) as f:
        await f.js("Outils.ouvrir(),0"); await f.avancer(700)
        await f.pg.click('#p-outils [data-o="reglettes"]'); await f.avancer(1500)
        await f.cadrer("#p-reglettes")
        async def prendre(v):
            bb=await f.pg.locator(f".rgPioche[data-v='{v}'] .rgR").bounding_box(); return (bb["x"]+bb["height"]/2,bb["y"]+bb["height"]/2)
        async def case(x,y,dx=.5):
            return tuple(await f.pg.evaluate(f"(()=>{{const r=Reglettes.plan().getBoundingClientRect(),G=Reglettes.geo;return [r.left+G.ox+({x}+{dx})*G.u,r.top+G.oy+({y}+.5)*G.u]}})()"))
        f.x,f.y=await case(8,6)
        await f.attendre(300)
        await f.glisser(await prendre(10),await case(1,1),900); await f.attendre(700)
        await f.glisser(await prendre(6),await case(1,3),900); await f.attendre(600)
        await f.glisser(await prendre(4),await case(7,3),900); await f.attendre(900)
        await f.clic("#rgCalc",ms=700,apres=1400)
        await f.clic("#rgEsc",ms=600,apres=3200)
    encoder("reglettes",1400)

FILMS={"journee":journee,"rituels":rituels,"numeration":numeration,"balance":balance,"monnaie":monnaie,"reglettes":reglettes}
if __name__=="__main__":
    for nom in sys.argv[1:] or FILMS: asyncio.run(FILMS[nom]())
