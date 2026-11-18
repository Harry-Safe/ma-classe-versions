"""Range les médias dans le dépôt du site : films MP4 et leurs affiches, images WebP, tuiles des outils."""
import shutil, pathlib, sys
from PIL import Image
from commun import TRAVAIL, VITRINE as D
F=D/"films"; I=D/"images"; F.mkdir(parents=True,exist_ok=True); I.mkdir(parents=True,exist_ok=True)
T=TRAVAIL
AFF={"journee":20,"rituels":118,"numeration":95,"balance":-1,"monnaie":150,"reglettes":-1}
tailles={}
for nom,k in AFF.items():
    mp4=T/"films"/f"{nom}.mp4"
    if not mp4.exists(): print("manque",nom); continue
    shutil.copyfile(mp4,F/f"{nom}.mp4")
    fs=sorted((T/"images"/nom).glob("*.jpg"))
    if len(fs)<=abs(k) or (len(sys.argv)>1 and nom not in sys.argv[1:]): print("attente",nom); continue
    im=Image.open(fs[k]).convert("RGB")
    larg=min(1600 if nom in("journee","rituels","numeration") else 1400, im.width)
    im=im.resize((larg,round(larg*im.height/im.width/2)*2),Image.LANCZOS); im.save(F/f"{nom}.webp",quality=80,method=6)
    tailles[nom]=im.size
print(tailles)
for src,dst in {"accueil":"accueil","semaine":"semaine","soir":"soir","ops":"operations","geo":"geometrie","ecriture":"ecriture"}.items():
    Image.open(T/"captures"/f"{src}.png").convert("RGB").resize((1920,1080),Image.LANCZOS).save(I/f"{dst}.webp",quality=80,method=6)
fs=sorted((T/"images"/"journee").glob("*.jpg"))
Image.open(fs[-1]).convert("RGB").save(I/"eleves.webp",quality=80,method=6)
# image de partage (1200 x 630) : l'accueil de Glacis sur le fond du site
a=Image.open(T/"captures"/"accueil.png").convert("RGB").resize((1120,630),Image.LANCZOS)
p=Image.new("RGB",(1200,630),"#e6edfb"); p.paste(a,(40,0)); p.save(I/"partage.jpg",quality=84,optimize=True)
for f in sorted((T/"captures").glob("ico-*.png")):
    Image.open(f).convert("RGBA").resize((144,144),Image.LANCZOS).save(I/f"outil-{f.stem[4:].lower()}.webp",quality=88,method=6)
tot=0
for f in sorted(D.rglob("*")):
    if f.is_file(): tot+=f.stat().st_size
print("total",tot//1024,"Ko")
for f in sorted(F.glob("*"))+sorted(I.glob("*.webp"))[:8]: print(f.name,f.stat().st_size//1024,"Ko")
