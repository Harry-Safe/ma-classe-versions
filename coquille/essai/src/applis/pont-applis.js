/* =====================================================================
   PONT « Ma classe » POUR LES APPLIS HTML (application Windows) — novembre 2026
   Ce fichier n'est pas assemblé dans la page de Ma classe : l'application le sert aux applis à l'adresse
   /_ma-classe/pont.js (src-tauri/src/lib.rs). Une appli l'ajoute dans sa page :
       <script src="/_ma-classe/pont.js"></script>
   puis enregistre ses données dans « Ma classe/Applis/<son dossier>/donnees/ » (synchronisé par Google Drive) :
       if (await MaClasse.pret) { await MaClasse.ecrireJSON("progres.json", {...}); }
       const p = await MaClasse.lireJSON("progres.json", {});            // valeur par défaut si absent
       await MaClasse.ecrire("voix/a.webm", blob);                        // sous-dossiers créés au besoin
   Hors de Ma classe (page ouverte seule), le script est absent ou MaClasse.pret vaut false : l'appli garde
   alors son propre enregistrement. Toutes les fonctions rendent une promesse. Guide : docs/APPLIS.md.
   ===================================================================== */
(() => {
  if (window.MaClasse) return;
  const dansCadre = window.parent !== window, attente = new Map();
  let n = 0;
  addEventListener("message", ev => {
    const m = ev.data;
    if (ev.source !== window.parent || !m || m.pont !== "ma-classe" || !attente.has(m.reponse)) return;
    const a = attente.get(m.reponse); attente.delete(m.reponse); clearTimeout(a.t);
    m.ok ? a.ok(m.resultat) : a.ko(new Error(m.resultat));
  });
  const appeler = (op, donnees = {}, delai = 60000) => new Promise((ok, ko) => {
    if (!dansCadre) return ko(new Error("Cette appli n'est pas ouverte dans Ma classe."));
    const id = ++n, t = setTimeout(() => { attente.delete(id); ko(new Error("Ma classe ne répond pas.")); }, delai);
    attente.set(id, {ok, ko, t});
    window.parent.postMessage({pont:"ma-classe", n:id, op, ...donnees}, "*");
  });
  const api = window.MaClasse = {
    version:1,
    appli:null,                       // {id, nom} une fois le pont établi
    /* vrai quand Ma classe répond et que son dossier est connecté */
    pret:dansCadre ? appeler("bonjour", {}, 3000).then(r => { api.appli = r.appli; api.maClasse = r.maClasse; return !!r.dossier; }, () => false) : Promise.resolve(false),
    lire:chemin => appeler("lire", {chemin}),                                    // texte, ou null si absent
    lireOctets:chemin => appeler("lireOctets", {chemin}),                        // ArrayBuffer, ou null
    async lireJSON(chemin, defaut = null){ const t = await appeler("lire", {chemin}); if (t == null) return defaut; try { return JSON.parse(t); } catch { return defaut; } },
    ecrire:(chemin, contenu) => appeler("ecrire", {chemin, contenu}),            // texte, Blob, ArrayBuffer ou tableau d'octets
    ecrireJSON:(chemin, valeur) => appeler("ecrire", {chemin, contenu:JSON.stringify(valeur, null, 1)}),
    lister:(chemin = "") => appeler("lister", {chemin}),                         // [{nom, dossier}]
    supprimer:chemin => appeler("supprimer", {chemin}),                          // vrai si supprimé, faux si absent
    fermer:() => appeler("fermer"),                                              // revient au panneau des applis
  };
})();
