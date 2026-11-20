"""Range les médias dans le dépôt du site : films MP4 et leurs affiches, images WebP, tuiles des outils."""
import shutil, pathlib, sys
from PIL import Image
from commun import TRAVAIL, VITRINE as D
F=D/"films"; I=D/"images"; F.mkdir(parents=True,exist_ok=True); I.mkdir(parents=True,exist_ok=True)
T=TRAVAIL
# l'affiche de chaque film : l'image prise à cette fraction de sa durée (0 : début, 1 : fin) ; ouverture : sa première image,
# car elle sert aussi de fond sous le film quand il se dépose sur le voile (index.html, .ouvAppli)
AFF={"ouverture":0,"document":.98,"accueil":.98,"appel":.42,"assistant":.98,"problemes":.98,"numeration":.4,"geometrie":.98,"lignages":.45,"operations":.98,
     "minuteur":.5,"balancenb":.78,"droite":.74,"fractions":.78,"reglettes":.82}
choix=sys.argv[1:]
for f in list(F.glob("*.mp4"))+list(F.glob("*.webp")):                # films retirés de la page
    if f.stem not in AFF: f.unlink()
for nom,part in AFF.items():
    if choix and nom not in choix: continue
    mp4=T/"films"/f"{nom}.mp4"; fs=sorted((T/"images"/nom).glob("*.jpg"))
    if not mp4.exists() or not fs: print("manque",nom); continue
    shutil.copyfile(mp4,F/f"{nom}.mp4")
    im=Image.open(fs[min(len(fs)-1,round(part*(len(fs)-1)))]).convert("RGB")
    im=im.resize((1600,round(1600*im.height/im.width/2)*2),Image.LANCZOS); im.save(F/f"{nom}.webp",quality=80,method=6)
    print(nom,(F/f"{nom}.mp4").stat().st_size//1024,"Ko")
FIXES={"accueil":"accueil","semaine":"semaine","soir":"soir"}
if choix:                                                              # des films nommés : les captures fixes et les tuiles ne bougent pas
    for f in sorted(F.glob("*")): print(f.name,f.stat().st_size//1024,"Ko")
    sys.exit(0)
for f in I.glob("*.webp"):                                             # images retirées de la page
    if f.stem not in FIXES.values(): f.unlink()
for src,dst in FIXES.items():
    Image.open(T/"captures"/f"{src}.png").convert("RGB").resize((1920,1080),Image.LANCZOS).save(I/f"{dst}.webp",quality=80,method=6)
# image de partage (1200 x 630) : l'accueil de Glacis sur le fond du site
a=Image.open(T/"captures"/"accueil.png").convert("RGB").resize((1120,630),Image.LANCZOS)
p=Image.new("RGB",(1200,630),"#e6edfb"); p.paste(a,(40,0)); p.save(I/"partage.jpg",quality=84,optimize=True)
# tuiles des outils : dessins relevés dans Glacis (captures.py icones), écrits dans index.html entre <!--TUILES--> et <!--/TUILES-->
import json, html, re
def melange(a, b, k):                                            # color-mix(in srgb, a k, b) : précalculé pour tous les navigateurs
    a, b = (tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for c in (a, b))
    return "#" + "".join(f"{round(x * k + y * (1 - k)):02x}" for x, y in zip(a, b))
ic = T/"captures"/"icones.json"
if ic.exists():
    tuiles = json.loads(ic.read_text(encoding="utf-8"))
    li = "".join(f'\n        <li><span class="tuile" style="--h:{melange(t["g1"], "#ffffff", .85)};--g2:{t["g2"]};--go:{melange(t["g2"], "#202b37", .4)}">'
                 f'<svg viewBox="0 0 64 64" aria-hidden="true">{t["dessin"]}</svg></span>{html.escape(t["nom"])}</li>' for t in tuiles)
    page = D.parent/"index.html"; s = page.read_text(encoding="utf-8")
    s, n = re.subn(r"<!--TUILES-->.*?<!--/TUILES-->", lambda m: "<!--TUILES-->" + li + "\n      <!--/TUILES-->", s, flags=re.S)
    assert n == 1, "repères <!--TUILES--> absents de index.html"
    page.write_text(s, encoding="utf-8")
    for f in I.glob("outil-*.webp"): f.unlink()                 # anciennes tuiles photographiées
    print("tuiles des outils :", len(tuiles))
tot=0
for f in sorted(D.rglob("*")):
    if f.is_file(): tot+=f.stat().st_size
print("total",tot//1024,"Ko")
for f in sorted(F.glob("*"))+sorted(I.glob("*.webp"))[:8]: print(f.name,f.stat().st_size//1024,"Ko")
