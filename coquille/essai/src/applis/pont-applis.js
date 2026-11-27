/* Pont « Glacis » pour les applis HTML (application Windows) — novembre 2026.
   Couche : hors de la page de Glacis (script servi aux applis, sans import ni export) ; le côté Glacis du pont est
     applis/applis-pont.js.
   Données : aucune qui lui soit propre : il demande à Glacis de lire et écrire « Glacis/Applis/<son dossier>/donnees/ ».
   Accroches : écoute « message » (réponses de Glacis) ; offre window.MaClasse à l'appli ; build/construire.py le range
     dans la page (repère PONT_APPLIS) pour les applis intégrées, et l'application le sert sous /_ma-classe/pont.js.
   Ce fichier n'est pas assemblé dans la page de Glacis : l'application le sert aux applis à l'adresse
   /_ma-classe/pont.js (src-tauri/src/lib.rs). Une appli l'ajoute dans sa page :
       <script src="/_ma-classe/pont.js"></script>
   puis enregistre ses données dans « Glacis/Applis/<son dossier>/donnees/ » (synchronisé par Google Drive) :
       if (await MaClasse.pret) { await MaClasse.ecrireJSON("progres.json", {...}); }
       const p = await MaClasse.lireJSON("progres.json", {});            // valeur par défaut si absent
       await MaClasse.ecrire("voix/a.webm", blob);                        // sous-dossiers créés au besoin
   Hors de Glacis (page ouverte seule), le script est absent ou MaClasse.pret vaut false : l'appli garde
   alors son propre enregistrement. Toutes les fonctions rendent une promesse. Guide : docs/APPLIS.md.
   Version 2 (20 novembre 2026, canevas commun des applis) : l'appli déclare son en-tête, que Glacis pose dans sa barre
   de menus, et écoute les clics qui la concernent :
       await MaClasse.barre({modes:[{id:"jouer", nom:"Jouer", icone:"lectureMedia"}], mode:"jouer", reglages:"Règles du jeu", aide:null});
       MaClasse.sur("mode", d => …d.id…);  MaClasse.sur("reglages", d => …d.x…);  MaClasse.sur("aide", d => …);
   (le canevas de l'atelier des applis, _canevas/canevas.js, le fait pour elle). */
(() => {
  if (window.MaClasse) return;
  const dansCadre = window.parent !== window,
    attente = new Map(),
    ecoutes = new Map();
  let n = 0;
  addEventListener("message", ev => {
    const m = ev.data;
    if (ev.source !== window.parent || !m || m.pont !== "ma-classe") return;
    /* un événement de Glacis (clic dans sa barre de menus) : à ceux qui l'écoutent */
    if (typeof m.evenement === "string") {
      (ecoutes.get(m.evenement) || []).forEach(f => {
        try {
          f(m.donnees || {});
        } catch (e) {
          console.error(e);
        }
      });
      return;
    }
    if (!attente.has(m.reponse)) return;
    const a = attente.get(m.reponse);
    attente.delete(m.reponse);
    clearTimeout(a.t);
    m.ok ? a.ok(m.resultat) : a.ko(new Error(m.resultat));
  });
  const appeler = (op, donnees = {}, delai = 60000) =>
    new Promise((ok, ko) => {
      if (!dansCadre) return ko(new Error("Cette appli n'est pas ouverte dans Glacis."));
      const id = ++n,
        t = setTimeout(() => {
          attente.delete(id);
          ko(new Error("Glacis ne répond pas."));
        }, delai);
      attente.set(id, { ok, ko, t });
      window.parent.postMessage({ pont: "ma-classe", n: id, op, ...donnees }, "*");
    });
  const api = (window.MaClasse = {
    version: 2,
    appli: null, // {id, nom} une fois le pont établi
    /* vrai quand Glacis répond et que son dossier est connecté */
    pret: dansCadre
      ? appeler("bonjour", {}, 3000).then(
          r => {
            api.appli = r.appli;
            api.maClasse = r.maClasse;
            return !!r.dossier;
          },
          () => false
        )
      : Promise.resolve(false),
    lire: chemin => appeler("lire", { chemin }), // texte, ou null si absent
    lireOctets: chemin => appeler("lireOctets", { chemin }), // ArrayBuffer, ou null
    async lireJSON(chemin, defaut = null) {
      const t = await appeler("lire", { chemin });
      if (t == null) return defaut;
      try {
        return JSON.parse(t);
      } catch {
        return defaut;
      }
    },
    ecrire: (chemin, contenu) => appeler("ecrire", { chemin, contenu }), // texte, Blob, ArrayBuffer ou tableau d'octets
    ecrireJSON: (chemin, valeur) => appeler("ecrire", { chemin, contenu: JSON.stringify(valeur, null, 1) }),
    lister: (chemin = "") => appeler("lister", { chemin }), // [{nom, dossier}]
    supprimer: chemin => appeler("supprimer", { chemin }), // vrai si supprimé, faux si absent
    fermer: () => appeler("fermer"), // revient au panneau des applis
    barre: d => appeler("barre", { barre: d }), // en-tête : modes, mode, réglages, aide
    sur(nom, f) {
      if (typeof f === "function") ecoutes.set(nom, [...(ecoutes.get(nom) || []), f]);
    }, // « mode », « reglages », « aide »
  });
})();
