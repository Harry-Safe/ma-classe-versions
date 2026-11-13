"""Signe l'installateur de l'application Windows pour le module de mise à jour de Tauri (action « Publier les
mises à jour », après outils/signer.py qui a copié appli/ dans _site/appli/).

La clé privée vient seulement du secret TAURI_SIGNING_PRIVATE_KEY (sans mot de passe) : jamais dans un fichier.
La signature est écrite dans _site/appli/latest.json (versions publiées) et _site/appli/essai/latest.json (versions
d'essai, lues par l'application réglée sur « d'essai ») ; l'application refuse un installateur dont la signature
ne correspond pas à sa clé publique.

Chaîne de signature (lot C de l'audit de sécurité, 13 novembre 2026) :
  · l'outil (Tauri) est installé AVANT que la clé soit dans l'environnement, depuis outils/signature/ (version et
    empreintes fixées par package-lock.json, « npm ci --ignore-scripts ») : plus rien n'est téléchargé au moment de
    signer, et aucun script d'installation ne tourne ;
  · chaque signature est revérifiée ici comme le fait l'application (minisign-verify dans installer_paquet) : clé
    publique CLE_MAJ de la coquille du canal, signature de l'installateur, signature du commentaire, nom et version
    du fichier signé ; une signature que l'application refuserait n'est jamais publiée.

    python outils/signer-appli.py              # publication (secret TAURI_SIGNING_PRIVATE_KEY)
    python outils/signer-appli.py --a-blanc    # branches claude/fabrication-* : clé jetable, rien n'est écrit
"""
import base64, hashlib, json, os, re, subprocess, sys, tempfile
from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ICI = Path(__file__).resolve().parent.parent
SITE = ICI / "_site" / "appli"
OUTILS = ICI / "outils" / "signature"
CANAUX = {"": "stable", "essai": "essai"}          # dossier de _site/appli/ -> canal (coquille/<canal>/)


def outil():
    """L'outil installé par « npm ci » dans outils/signature/, à la version fixée par son package-lock.json."""
    lot = json.loads((OUTILS / "package-lock.json").read_text(encoding="utf-8"))
    attendue = lot["packages"]["node_modules/@tauri-apps/cli"]["version"]
    exe = OUTILS / "node_modules" / ".bin" / ("tauri.cmd" if os.name == "nt" else "tauri")
    if not exe.exists(): sys.exit("outil de signature absent : « npm ci --ignore-scripts » dans outils/signature/ d'abord")
    v = subprocess.run([str(exe), "--version"], capture_output=True, text=True, check=True).stdout.split()[-1]
    if v != attendue: sys.exit(f"outil de signature en {v}, {attendue} attendue (outils/signature/package-lock.json)")
    return str(exe)


def lignes(b64):
    return base64.b64decode(b64.strip()).decode("utf-8").splitlines()


def cle_application(canal):
    """Clé publique CLE_MAJ écrite dans le code Rust de la coquille du canal (celle avec laquelle l'application vérifie)."""
    rs = (ICI / "coquille" / canal / "tauri" / "src-tauri" / "src" / "lib.rs").read_text(encoding="utf-8")
    m = re.search(r'const CLE_MAJ: &str = "([A-Za-z0-9+/=]+)";', rs)
    if not m: sys.exit(f"{canal} : clé publique CLE_MAJ introuvable dans coquille/{canal}/tauri/src-tauri/src/lib.rs")
    return m.group(1)


def verifier(exe, signature, cle, version):
    """Même contrôle que l'application : minisign (Ed25519 ; « ED » = empreinte BLAKE2b-512 du fichier), puis
    signature du commentaire de confiance, qui doit nommer ce fichier ; version du nom = version annoncée."""
    k = base64.b64decode(lignes(cle)[1])
    sig = lignes(signature)
    if len(sig) < 4 or not sig[2].startswith("trusted comment: "): raise ValueError("signature mal formée")
    s, g = base64.b64decode(sig[1]), base64.b64decode(sig[3])
    if k[:2] != b"Ed" or len(k) != 42 or len(s) != 74 or len(g) != 64: raise ValueError("clé ou signature mal formée")
    if s[2:10] != k[2:10]: raise ValueError("signée avec une autre clé que celle de l'application")
    pub = Ed25519PublicKey.from_public_bytes(k[10:])
    octets = exe.read_bytes()
    if s[:2] == b"ED": octets = hashlib.blake2b(octets).digest()
    elif s[:2] != b"Ed": raise ValueError("algorithme de signature inconnu")
    commentaire = sig[2][len("trusted comment: "):]
    try:
        pub.verify(s[10:], octets)
        pub.verify(g, s[10:] + commentaire.encode("utf-8"))
    except InvalidSignature:
        raise ValueError("signature invalide") from None
    if f"file:{exe.name}" not in commentaire.split("\t"): raise ValueError(f"commentaire signé sans le nom {exe.name}")
    m = re.search(r"_(\d+(?:\.\d+)*)_", exe.name)
    if not m or m.group(1) != version: raise ValueError(f"version du fichier signé ({m and m.group(1)}) différente de {version}")


def signer(fiche, tauri, env, cle, ecrire=True):
    f = json.loads(fiche.read_text(encoding="utf-8"))
    for nom, p in f["platforms"].items():
        exe = fiche.parent / p["url"].rsplit("/", 1)[-1]
        if not exe.exists(): sys.exit(f"{exe.name} manquant dans {fiche.parent.relative_to(SITE.parent)}/")
        subprocess.run([tauri, "signer", "sign", str(exe)], check=True, env=env)
        sigf = exe.parent / (exe.name + ".sig")
        signature = sigf.read_text(encoding="utf-8").strip()
        try: verifier(exe, signature, cle, f["version"])
        except ValueError as e: sys.exit(f"{exe.name} : {e} : rien n'est publié")
        print(f"{fiche.parent.name} · {nom} : {exe.name} signé, signature vérifiée comme dans l'application")
        if ecrire: p["signature"] = signature
        else: sigf.unlink()
    if ecrire: fiche.write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fiches():
    return [(x, CANAUX[d]) for d, x in ((d, SITE / d / "latest.json") for d in CANAUX) if x.exists()]


def a_blanc(tauri):
    """Branches de fabrication : toute la chaîne (outil installé, signature, contrôle) avec une clé jetable ; le
    contrôle doit aussi refuser cette signature avec la vraie clé de l'application. Rien n'est écrit dans les fiches."""
    with tempfile.TemporaryDirectory() as t:
        k = Path(t) / "jetable.key"
        subprocess.run([tauri, "signer", "generate", "--ci", "-p", "", "-w", str(k)], check=True, capture_output=True)
        env = {**os.environ, "TAURI_SIGNING_PRIVATE_KEY": k.read_text(encoding="utf-8").strip(), "TAURI_SIGNING_PRIVATE_KEY_PASSWORD": ""}
        jetable = (Path(t) / "jetable.key.pub").read_text(encoding="utf-8").strip()
        for fiche, canal in fiches():
            signer(fiche, tauri, env, jetable, ecrire=False)
            f = json.loads(fiche.read_text(encoding="utf-8"))
            for p in f["platforms"].values():
                exe = fiche.parent / p["url"].rsplit("/", 1)[-1]
                subprocess.run([tauri, "signer", "sign", str(exe)], check=True, env=env, capture_output=True)
                sigf = exe.parent / (exe.name + ".sig")
                try: verifier(exe, sigf.read_text(encoding="utf-8"), cle_application(canal), f["version"])
                except ValueError: print(f"{canal} : clé jetable bien refusée par la clé de l'application")
                else: sys.exit(f"{canal} : une signature de clé jetable passe le contrôle : contrôle défaillant")
                finally: sigf.unlink()
    print("chaîne de signature à blanc : bonne")


def main():
    tauri = outil()
    if "--a-blanc" in sys.argv: return a_blanc(tauri)
    if not fiches(): return print("pas d'application à signer")
    if not os.environ.get("TAURI_SIGNING_PRIVATE_KEY"): sys.exit("secret TAURI_SIGNING_PRIVATE_KEY absent : l'application ne peut pas être publiée")
    env = {**os.environ, "TAURI_SIGNING_PRIVATE_KEY_PASSWORD": ""}
    for fiche, canal in fiches(): signer(fiche, tauri, env, cle_application(canal))


if __name__ == "__main__":
    main()
