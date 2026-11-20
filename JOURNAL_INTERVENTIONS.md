# Journal des interventions — distribution de Ma classe

Les entrées récentes sont en tête. Une entrée sur une branche d’essai ne signifie pas que le site a été publié.

## 2026-11-20 — Claude — Essai 6.0.0-beta.19 publié (accueil : chargement et aperçus de fichier)

- **Demande / Autorisation** : Franck, 20 novembre, 13 h 10 (écran d'accueil figé dans l'aperçu de l'iPad) ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `092d4c4` ; dépôt source : `essai` à `d42b609`, garde de publication satisfaite.
- **Réalisation** : `build/publier-version.py --canal essai` et `build/publier-appli.py --canal essai` du dépôt source ; commit `647fe1c`, envoyé sur `main` par avance rapide.
- **Validation** : action `44739928125` réussie : « versions.json signé : essai 6.0.0-beta.19 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.19_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Deployment complete » ; Cloudflare Pages : déploiement `f2a0b66d`, production, commit `647fe1c`, succès.
- **Livraison / état** : publié sur glacis-classe.fr, canal d'essai seulement ; canal stable inchangé.

## 2026-11-20 — Claude — Essai 6.0.0-beta.18 publié (l'Atelier, logo de la boîte à outils)

- **Demande / Autorisation** : Franck, 20 novembre, 11 h 23 (« Je n'ai pas vu l'atelier avec son logo intégré », « La boîte à outils doit avoir un logo et une languette bien différenciée ») ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `38bba78` ; dépôt source : `essai` à `2079241`, garde de publication satisfaite.
- **Réalisation** : `build/publier-version.py --canal essai` et `build/publier-appli.py --canal essai` du dépôt source ; commit `ca3a0b0`, envoyé sur `main` par avance rapide.
- **Validation** : action `44727581855` réussie : « versions.json signé : essai 6.0.0-beta.18 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.18_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Deployment complete » ; Cloudflare Pages : déploiement `6749403b`, production, commit `ca3a0b0`, succès.
- **Livraison / état** : publié sur glacis-classe.fr, canal d'essai seulement ; canal stable inchangé.

## 2026-11-20 — Claude — Essai 6.0.0-beta.17 publié (démarrage sur tablette, Explorer simplifié, boîte à outils à gauche)

- **Demande / Autorisation** : Franck, 20 novembre, 9 h 37 (« Glacis HTML bloque sur le bouton commencer ») et 9 h 42 ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `9e51713` ; dépôt source : `essai` à `13adfb1`, garde de publication satisfaite.
- **Réalisation** : `build/publier-version.py --canal essai` et `build/publier-appli.py --canal essai` du dépôt source ; commit `d85c155`, envoyé sur `main` par avance rapide.
- **Validation** : action `44713263546` réussie : « versions.json signé : essai 6.0.0-beta.17 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.17_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Deployment complete » ; Cloudflare Pages : déploiement `ca7decd1`, production, commit `d85c155`, succès. Le blocage signalé sur l'iPad et sur Android n'a pas été reproduit : cet essai porte des parades et un message à l'accueil, pas une correction prouvée.
- **Livraison / état** : publié sur glacis-classe.fr, canal d'essai seulement ; canal stable inchangé.

## 2026-11-20 — Claude — Essai 6.0.0-beta.16 publié (applis intégrées et boîte à outils)

- **Demande / Autorisation** : lot 4 des demandes de Franck du 19 novembre (23 h 46), « Vas-y » le 20 novembre (7 h 52) ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `aef99f5` ; dépôt source : `essai` à `8015dd0`, garde de publication satisfaite.
- **Réalisation** : `build/publier-version.py --canal essai` et `build/publier-appli.py --canal essai` du dépôt source (`essai/Glacis.html`, `essai/Glacis - Remplaçant.html`, `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json`) ; commit `ba30cb6`, envoyé sur `main` par avance rapide. Le dossier `applis/` n'est pas modifié : Glacis n'a plus de Store à partir de cet essai (les applis sont dans la page), le catalogue `applis.json` reste servi pour les versions antérieures.
- **Validation** : action `44697934620` réussie : « versions.json signé : essai 6.0.0-beta.16 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.16_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Deployment complete » ; Cloudflare Pages : déploiement `e4414b5d`, production, commit `ba30cb6`, succès. Les fichiers du site n'ont pas été relus un à un.
- **Livraison / état** : publié sur glacis-classe.fr, canal d'essai seulement ; canal stable inchangé.

## 2026-11-20 — Claude — Essai 6.0.0-beta.15 publié (Préparer, emploi du temps et cours double)

- **Demande / Autorisation** : lots 1 à 3 des demandes de Franck du 19 novembre (23 h 46), « un par un puis un test unique » ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `85e79a3` ; dépôt source : `essai` à `3aba99b`, garde de publication satisfaite.
- **Réalisation** : `build/publier-version.py --canal essai` et `build/publier-appli.py --canal essai` du dépôt source (`essai/Glacis.html`, `essai/Glacis - Remplaçant.html`, `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json`) ; commit `34cc120`, envoyé sur `main` par avance rapide.
- **Validation** : action `44689933653` réussie : « versions.json signé : essai 6.0.0-beta.15 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.15_x64-setup-essai.exe signé », « signature vérifiée comme dans l'application », « Deployment complete » ; Cloudflare Pages : déploiement `11bb1f7e`, production, commit `34cc120`, succès.
- **Livraison / état** : publié sur glacis-classe.fr, canal d'essai seulement ; canal stable inchangé.

## 2026-11-19 — Claude — Page « introuvable » (`404.html`) : un vrai 404 pour les adresses inconnues

- **Demande / Autorisation** : captures des statistiques Cloudflare envoyées par Franck à 18 h 58, dans la suite de « Fais 2 et 4 » (sécurité du site).
- **Constat** : un analyseur de vulnérabilités (« TLM-Audit-Scanner/2.0 », une adresse aux Pays-Bas, 4 491 requêtes le 18 novembre) a cherché des fichiers secrets (`/live/.env`, `/web.config`, `/cache/laravel.log`…) : réponse **200**, car sans `404.html` Cloudflare Pages renvoie la page d'accueil pour toute adresse inconnue. Rien n'a fuité (le site ne contient aucun de ces fichiers), mais l'application, qui attend un 404 pour `appli/latest.json` tant qu'aucune version stable n'existe (essai 6.0.0-beta.14, case des essais décochée), recevait la page d'accueil à la place.
- **Réalisation** : `404.html` (page sobre aux couleurs de Glacis, sans script, `noindex`), copiée par `outils/signer.py`.
- **Livraison / état** : action `44583037419` réussie ; URL Scanner sur le site en ligne : `/live/.env` et `/appli/latest.json` répondent **404**.

## 2026-11-19 — Claude — Sécurité du site : HTTPS durci (zone Cloudflare) et en-têtes de sécurité (`_headers`)

- **Demande / Autorisation** : Franck, 18 h 49 : « Fais 2 et 4 » (réglages HTTPS de la zone, en-têtes de la page), après le bilan de sécurité du site ; DMARC (point 3) laissé de côté : Franck veut pouvoir envoyer des courriels depuis le domaine.
- **Contrôle préalable** : `main` à `9fc79ad` ; zone `glacis-classe.fr` (offre gratuite) : TLS minimal 1.0, HTTPS non forcé, HSTS absent, SSL « Full » ; DNSSEC actif ; analyse URL Scanner de Cloudflare : aucun verdict, aucun cookie.
- **Réalisation** : zone (API, 18 h 50) : TLS minimal 1.2, « Always Use HTTPS », SSL « Full (strict) », HSTS 6 mois avec sous-domaines (sans preload) et nosniff. `_headers` : `X-Frame-Options: DENY`, `Permissions-Policy`, `Cross-Origin-Opener-Policy`, `Referrer-Policy`, `nosniff` partout ; politique de contenu sur `/` et `/index.html` (scripts de la page par empreinte, mesure d'audience Cloudflare, rien d'autre) ; `outils/signer.py` (`entetes()`) calcule les empreintes à chaque publication et refuse un script en ligne avec attributs ou un gestionnaire d'événement dans une balise.
- **Validation** : après les réglages de zone, URL Scanner : 200, TLS 1.3, `max-age=15552000; includeSubDomains`. `signer.py` sur une copie avec une clé jetable : 2 scripts autorisés par empreinte ; page servie localement avec la politique de contenu dans Chromium (1366 et 390 px) : aucune violation, polices chargées, 15 films présents (lecture identique sans la politique).
- **Livraison / état** : `main` `02969c8`, action `44581616221` réussie (« _headers : 2 script(s) en ligne autorisé(s) par empreinte », « Deployment complete ») ; URL Scanner sur le site en ligne : 200, politique de contenu, `X-Frame-Options: DENY`, HSTS, `Permissions-Policy` et `Cross-Origin-Opener-Policy` présents, aucune violation dans la console.

## 2026-11-19 — Claude — Essai 6.0.0-beta.14 publié ; l'essai suit la stable (`outils/signer.py`, `outils/signer-appli.py`)

- **Demande / Autorisation** : Franck, 11 h 28 : « Empêche la recherche de mise à jour d'essai sauf en cochant une case. Trouve un moyen pour que ce soit toujours la version stable qui soit priorisée » ; 12 h 10 : « L'objectif étant aussi que ceux qui ont actuellement la version essai prise sur le site puisse avoir directement la stable quand elle sort et qu'un collègue ne reste pas coincé avec les versions d'essai ». Publication d'essai : autorisation permanente (`AGENTS.md` de `Ma-classe`).
- **Contrôle préalable** : `main` distant à `933de75` (journal de la vitrine), avance rapide de `publication` ; aucune action en cours.
- **Réalisation** : pages et application 6.0.0-beta.14 sur le canal d'essai (`build/publier-version.py`, `build/publier-appli.py --canal essai`, commit source `d8f637a` de `essai`). **L'essai suit la stable** : `signer.py` (fonction `cle`, ordre des versions de l'application ; `essai_suit_stable`) annonce la version stable sur le canal d'essai de `versions.json` et de chaque appli de `applis.json` quand elle est au moins aussi récente ; `signer-appli.py` fait de même pour `_site/appli/essai/latest.json` après la signature. Sans version stable (aujourd'hui), rien ne change. But : les essais 6.0.0-beta.12 et 13 ne lisent que le canal d'essai ; ils recevront la 6.0 dès sa sortie. `DOCUMENTATION.md` § publication.
- **Validation** : `signer.py` lancé sur une copie du dépôt avec une clé jetable : sans stable, « versions.json signé : essai 6.0.0-beta.13 » inchangé ; avec une stable 6.0.0 simulée, canal d'essai = 6.0.0 (`stable/Glacis.html`) et appli Échecs simulée 9.0.0 sur ses deux canaux ; `essai_suit_stable` de `signer-appli.py` : rien sans stable, fiche stable recopiée quand elle est plus récente, essai 6.1.0-beta.1 plus récent gardé ; ordre des versions vérifié (6.0.0 > 6.0.0-rc.1 > 6.0.0-beta.13 > 6.0.0-beta.2, 6.0 = 6.0.0). Côté `Ma-classe` : suite complète 106 sur 106 sur la page numérotée.
- **Livraison / état** : `main` `788b7c0`, action `44516422153` **réussie** (« versions.json signé : essai 6.0.0-beta.14 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.14_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Deployment complete ») ; Cloudflare : déploiement `43c387fe`, production, succès. Aucune version stable : la règle « l'essai suit la stable » n'a encore rien changé.

## 2026-11-19 — Claude — Vitrine refaite publiée sur glacis-classe.fr (réunion de `claude/vitrine-2`)

- **Demande / Autorisation** : Franck, 10 h 27 : « Publie la vitrine. »
- **Contrôle préalable** : `main` distant à `7b0c5ee` (journal de l'essai 6.0.0-beta.13), contenu dans `claude/vitrine-2` (`25a292b`) : avance rapide, sans forçage ; aucune pull request ; aucune action en cours (dernière : `44493706315`, réussie).
- **Réalisation** : réunion de la refonte (entrée suivante) et de cette entrée ; aucune page, fiche, coquille ni paquet de l'application modifié : l'essai 6.0.0-beta.13 et Échecs 1.1.0 restent tels quels.
- **Validation** : contrôles de la page : entrée suivante. Action `44496683216` **réussie** : « versions.json signé : essai 6.0.0-beta.13 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.13_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Uploaded 35 files (14 already uploaded) », « Deployment complete ». Cloudflare (connecteur) : déploiement de production `571b642a`, branche `main`, commit `14bb735`, « deploy success », alias `glacis-classe.fr` et `www.glacis-classe.fr`. Non relu de l'extérieur (l'outil de lecture rend une copie ancienne de la page d'accueil et refuse les autres fichiers).
- **Livraison / état** : `main` `14bb735` ; `claude/vitrine-2` et `claude/site-vitrine` identiques à des états réunis, à supprimer par Franck (action « Nettoyer les branches »).

## 2026-11-19 — Claude — Vitrine refaite selon les remarques de Franck : quatorze nouveaux films (`claude/vitrine-2`, site non publié)

- **Demande / Autorisation** : Franck, 8 h 16 : « A refaire : la partie "Les tableaux" (casser un paquet, puis refaire un paquet de 10 ; une règle sortie et un trait tracé ; Lignages à la place d'Écriture ; soustraction par dégroupement avec la représentation, sans explication) ; rituels : les problèmes, manipuler, visualiser, corriger ; la première partie, "un truc plus Whaou", par exemple l'intégration d'un fichier dans le cahier journal ; la personnalisation de l'accueil ; l'assistant ; l'appel et la cantine plutôt que le tirage au sort ; les outils à mettre en avant, en montrant qu'on peut les réduire : Minuteur, balance des nombres, droite graduée, fraction et cuisenaire » ; 8 h 20 : « Je trouve aussi trop présent l'onglet flottant sur la version mobile », « Celui pour télécharger ». Aucune phrase de publication du site : branche et aperçu privé.
- **Contrôle préalable** : `main` à `6394de5` au départ, puis `edc5f49` (essai 6.0.0-beta.13, entrée suivante) ; aucune pull request ; branche partie de `origin/main` et reposée sur `edc5f49`.
- **Périmètre / chevauchements** : `index.html`, `vitrine/films/`, `vitrine/images/`, `outils/vitrine/`, `DOCUMENTATION.md` ; aucune page, fiche, coquille ni paquet de l'application.
- **Réalisation**
  - **Ouverture** : nouvelle accroche (« Votre journée de classe, prête d'un clic. ») et film `document` : dans Préparer › Le jour, une fiche PDF est jointe à la séance de maths ; sur l'Accueil, à 10 h 30, un clic l'ouvre, puis « Plein cadre » la met au tableau.
  - **La journée** : le pas « Les élèves » (tirage au sort) est remplacé par « L'appel et la cantine » (film `appel` dans l'écran épinglé) ; nouveau chapitre « Votre accueil » (film `accueil` : taille d'une carte, horloge et date ajoutées puis échangées).
  - **Les rituels** : film `problemes` (trois objets mis de côté, schéma en barres, illustration, correction).
  - **Les tableaux** : quatre films, `numeration` (une dizaine cassée, puis dix unités entourées qui refont un paquet), `geometrie` (règle sortie, déplacée, trait bleu tracé le long du bord, règle écartée), `operations` (342 − 165 par dégroupement, illustration affichée, explications masquées), `lignages` (taille de la réglure, tableau, cahier, feuille) ; l'onglet « Écriture » est retiré.
  - **Les outils** : cinq films en plein écran de l'application, chacun réduit en bas de l'écran à la fin (le minuteur est rouvert) : `minuteur`, `balancenb`, `droite`, `fractions`, `reglettes` ; balance à plateaux et monnaie retirées de la page.
  - **L'assistant** : nouveau chapitre et film `assistant` (ouverture au survol, tutoriels de l'écran, trois pas d'un tutoriel).
  - **Téléphone** : la barre du haut ne flotte plus (elle reste en haut de la page), sans fond, « Télécharger » en simple lien.
  - **Fabrique** : `filmer.py` réécrit (14 scénarios ; choix d'un fichier sans montrer la fenêtre du système, tracé, points d'un dessin SVG, mode `BROUILLON`, `GLACIS_PAGE`) ; `ranger.py` (affiche prise à une fraction de la durée, médias retirés supprimés) ; `exemples/` (fiche PDF « Compléments à 10 » faite pour la démonstration).
- **Images** : pris sur la page construite de l'essai 6.0.0-beta.13 (même source que `essai/Glacis.html` publié), classe de démonstration, prénoms fictifs ; aucune image retouchée ni générée. `vitrine/` : 7,5 Mo (films de 94 à 853 Ko, chargés seulement quand ils arrivent à l'écran).
- **Validation** : page servie en local et pilotée dans Chromium, 25 contrôles verts deux fois (dont : film de l'appel joué puis arrêté dans l'écran épinglé, passage automatique des onglets, clavier, bouton pause, 17 tuiles, mouvements réduits, barre non flottante à 390 px et partie avec la page) ; aucune erreur JavaScript ; seule réponse en erreur `appli/latest.json` (pas de version stable) ; pas de défilement horizontal à 390, 1366, 1440 et 1920 px ; chaque film relu sur planche d'images. **Non vérifié** : Safari, Firefox, un vrai téléphone.
- **Livraison / état** : poussé sur `claude/vitrine-2` ; aperçu privé mis à jour ; publication du site sur une phrase de Franck.
## 2026-11-19 — Claude — Essai 6.0.0-beta.13 publié (pages et application)

- **Demande / Autorisation** : Franck, 8 h 16 : quatre retouches du logiciel (Piano de lecture retiré, soustraction par dégroupement, piles lisibles dans l'illustration des opérations, erreur d'enregistrement dans les rituels) ; publication sur le canal d'essai : règle permanente.
- **Contrôle préalable** : `main` à `6394de5`, aucune pull request, aucune action en cours ; dépôt source : `essai` à `2bd678f`, contenant l'essai publié précédent (garde de `publier-version.py` passée sans `--forcer`).
- **Réalisation** : `build/publier-version.py` et `build/publier-appli.py --canal essai` depuis le dépôt source : `essai/Glacis.html`, `essai/Glacis - Remplaçant.html`, `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json` ; coquille inchangée ; la page de présentation n'est pas touchée (sa refonte est sur `claude/vitrine-2`).
- **Validation** : action `44493706315` réussie : « versions.json signé : essai 6.0.0-beta.13 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.13_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Uploaded 6 files (31 already uploaded) », « Deployment complete ». Cloudflare (connecteur) : déploiement de production `71c2c2cc`, commit `edc5f49`, « deploy success », alias `glacis-classe.fr` et `www.glacis-classe.fr`. Non relu de l'extérieur. Tests de l'application : journal du dépôt source (104 scénarios verts sur 106 dans la suite, les deux autres corrigés et repassés seuls).
- **Livraison / état** : `main` `edc5f49` ; essai proposé d'office aux postes qui suivent les essais.

## 2026-11-19 — Claude — Nouvelle page de présentation publiée sur glacis-classe.fr (réunion de `claude/site-vitrine`)

- **Demande / Autorisation** : Franck, 1 h 04 : « Publie » (après « Je valide » à 0 h 59, sur la maquette et ses tuiles corrigées).
- **Contrôle préalable** : `main` distant à `490ea60`, contenu dans `claude/site-vitrine` (`7670552`) : avance rapide, sans forçage ; aucune pull request ; aucune action en cours (dernière : `44415823662`, réussie).
- **Réalisation** : réunion des deux commits de la maquette (page, films, captures, polices, fabrique `outils/vitrine/`, copie de `vitrine/` par `outils/signer.py`) et de cette entrée ; aucune page, fiche, coquille ni paquet de l'application modifié : l'essai 6.0.0-beta.12 et Échecs 1.1.0 restent tels quels.
- **Validation** : contrôles de la page et répétition à blanc de `signer.py` : voir les deux entrées suivantes. Action `44426166717` **réussie** (travaux « Application Windows » repris du cache, « publier » réussi) : « versions.json signé : essai 6.0.0-beta.12 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.12_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Uploaded 29 files (8 already uploaded) », « Deployment complete ». Cloudflare (connecteur) : déploiement de production `bee3bbe2`, branche `main`, commit `1cdee99`, état « deploy success », alias `glacis-classe.fr` et `www.glacis-classe.fr` ; zone sans règle de page ni règle de cache (niveau de cache par défaut : les pages HTML ne sont pas gardées). **Non relu de l'extérieur** : l'outil de lecture de l'environnement de travail rend encore l'ancienne page d'accueil (copie en cache de l'outil, vraisemblablement) et refuse les autres fichiers du site ; le shell n'a pas accès au site (refus du mandataire). À confirmer par Franck dans un navigateur (actualiser).
- **Livraison / état** : `main` `1cdee99` ; site en ligne sur https://glacis-classe.fr ; `claude/site-vitrine` identique à `main`, à supprimer par Franck (action « Nettoyer les branches »).

## 2026-11-19 — Claude — Page de présentation : tuiles des outils en vectoriel (`claude/site-vitrine`, rien de publié)

- **Demande / Autorisation** : Franck, 0 h 59 : « Je valide. Petit détail, le détourage des icônes qui apparaissent à la section outil n'est pas très propre. » Pas de phrase de publication : `main` et le site inchangés.
- **Contrôle préalable** : `claude/site-vitrine` à `360821a` ; `main` à `490ea60` ; aucune pull request.
- **Cause** : les tuiles étaient des photos prises dans la fenêtre Outils ; leurs coins gardaient le fond crème opaque de la fenêtre, d'où un liseré clair autour de l'arrondi sur le fond du site.
- **Réalisation** : `captures.py icones` relève dans le menu Outils le nom, les deux couleurs et le dessin SVG de chaque tuile (aucun identifiant, contrôlé) ; `ranger.py` les écrit dans `index.html` (repères `<!--TUILES-->`), redessinées avec les règles de tuile de Glacis (dégradé éclairci à 85 %, arrondi 23 %, liserés, reflets, ombre teintée ; mélanges de couleurs précalculés) ; chiffres des tuiles dans la police Glacis Lecture, comme dans l'application ; 17 images `vitrine/images/outil-*.webp` retirées. `numeration.mp4` refait à l'identique par la fabrique du dépôt (même scénario, relu sur planche).
- **Validation** : capture des tuiles à 3 fois la résolution, bords nets sans liseré ; contrôles de la page repassés (aucun « ERR », aucune erreur JavaScript, seule réponse en erreur `appli/latest.json`, attendue).
- **Livraison / état** : poussé sur `claude/site-vitrine` ; aperçu privé mis à jour.

## 2026-11-19 — Claude — Maquette de la nouvelle page de présentation, animée, avec de vraies images de Glacis (`claude/site-vitrine`, rien de publié)

- **Demande / Autorisation** : Franck, 19 novembre, 0 h 21 : « J'aimerais juste qu'on revoit cette vitrine qu'est le site pour que les visiteurs aient un réel aperçu, voir des animations pour présenter l'appli. Un peu à la manière des présentations sur Apple. » Aucune phrase de publication : maquette sur une branche, `main` et le site inchangés.
- **Contrôle préalable** : `main` à `490ea60` (identique à `claude/glacis-site`) ; aucune pull request dans les deux dépôts ; aucune action en cours. Dépôt source : `essai` `7dfe084` (6.0.0-beta.12), `build/inventaire.py` : aucune branche non inscrite, seul chantier « En cours » : `claude/ma-classe-passerelle` (écartée par Franck) ; rien n'y est modifié. Non observable : un travail local non poussé d'un autre intervenant.
- **Périmètre / chevauchements** : `index.html` (réécrit), `outils/signer.py` (une ligne : copie de `vitrine/`), `DOCUMENTATION.md` (§ 1 et nouveau § 1 bis), `.gitignore` ; nouveaux dossiers `vitrine/` et `outils/vitrine/`. Aucune page, fiche, coquille ni paquet publié n'est touché.
- **Réalisation**
  - **Page** (`index.html`, 46 Ko, aucune dépendance extérieure) : barre en capsule de verre ; en-tête avec l'écran de Glacis qui se redresse au défilement et un reflet en biais (le « glacis ») ; chapitres La journée (texte qui défile, écran épinglé, quatre images), Les rituels, Les tableaux et Les outils (onglets en pilules qui passent seuls au suivant jusqu'au premier clic), grille des 17 outils, Vos données (cartes de verre), Télécharger sur une feuille de cahier (même lecture de `appli/latest.json` puis `appli/essai/latest.json` qu'avant), « Vous utilisiez Ma classe ? » replié, Un logiciel libre (texte de Franck sur l'aide de l'IA conservé mot pour mot). Polices de Glacis (Glacis Lecture, Marelle) servies par le site, avec leurs licences OFL. Thème clair seulement (les images de l'application sont claires).
  - **Images** (`vitrine/`, 2,8 Mo) : six films MP4 (journée, rituels, numération, balance, monnaie, réglettes ; 135 à 331 Ko, 9 à 14 s) et sept captures, pris dans la **vraie application** de l'essai 6.0.0-beta.12 ouverte en classe de démonstration (`essai/Glacis.html?classe-demo`, prénoms fictifs) ; aucune image retouchée ni générée, un point bleu montre les clics ; tuiles des outils photographiées dans le menu Outils.
  - **Fabrique** (`outils/vitrine/` : `filmer.py`, `captures.py`, `ranger.py`, `commun.py`, `LISEZ-MOI.md`) : films pris image par image avec l'horloge de la page pilotée (30 images par seconde), à relancer après une nouvelle version.
  - **Accessibilité** : sans JavaScript, tout est visible (commandes vidéo du navigateur) ; « réduire les animations » : rien ne bouge, films à l'arrêt avec bouton lecture ; bouton pause sur chaque film ; onglets au clavier.
- **Validation** : page servie en local et pilotée dans Chromium, 20 contrôles verts deux fois de suite (écran du haut redressé au défilement, films qui jouent visibles et s'arrêtent hors champ, pas de la journée, passage automatique des onglets puis arrêt au premier clic, clavier, bouton pause, lien « Télécharger Glacis 6.0 · essai 12 pour Windows » lu dans la fiche, 17 tuiles, toutes les images chargées, mouvements réduits) ; aucune erreur JavaScript ; seule réponse en erreur : `appli/latest.json` absent (pas encore de version stable, comme avant) ; pas de défilement horizontal à 390, 1366, 1440 et 1920 px ; captures regardées à 390, 1440 et 1920 px et sans JavaScript ; chaque film relu sur planche d'images. `outils/signer.py` répété à blanc avec une clé jetable : « versions.json signé : essai 6.0.0-beta.12 », « applis.json signé : echecs 1.1.0 (essai) », `_site/vitrine/` présent (43 fichiers), `_site/index.html` identique. `outils/vitrine/filmer.py numeration` et `captures.py accueil` relancés depuis le dépôt (276 images, 137 Ko). **Non vérifié** : Safari, Firefox et un vrai téléphone ; le déploiement Cloudflare (rien n'est envoyé sur `main`) ; les en-têtes de cache des films.
- **Livraison / état** : poussé sur `claude/site-vitrine` ; aperçu privé remis à Franck. À décider par lui avant toute publication : accroches et textes, thème clair seul, mention « environ 3 Mo », choix des films.

## 2026-11-18 — Claude — Rangement de l'installateur quand un seul canal est fabriqué (action 44414904869 en échec)

- **Constat** : action `44414904869` (commit `1235593`) : installateur `Glacis_6.0.0-beta.12_x64-setup-essai.exe` fabriqué (3 177 441 octets), `versions.json` et `applis.json` signés, mais **« manquant dans appli/essai/ »** à la signature : avec un seul installateur téléchargé (plus de canal stable), `actions/download-artifact` le pose directement dans `paquets/`, sans le sous-dossier `appli-essai`. Rien n'a été mis en ligne (le site garde la page d'attente).
- **Correction** : `outils/fabriquer-appli.py --placer` cherche l'installateur dans `paquets/appli-<canal>/` puis dans `paquets/` ; essayé à blanc (installateur factice rangé dans `_site/appli/essai/`). La fabrication est en cache : la nouvelle action la réutilise.
- **Livraison / état** : `main` `b569f4f` ; action `44415823662` **réussie** : fabrication reprise du cache, « versions.json signé : essai 6.0.0-beta.12 », « applis.json signé : echecs 1.1.0 (essai) », « Glacis_6.0.0-beta.12_x64-setup-essai.exe signé, signature vérifiée comme dans l'application », « Success! Uploaded 11 files », « Deployment complete » ; Cloudflare : déploiement de production `b9e96382` (branche `main`, commit `b569f4f`), domaines `glacis-classe.fr` et `www.glacis-classe.fr` actifs. Page d'accueil du site lue de l'extérieur (titre et sections) ; `latest.json` et l'installateur pas lisibles depuis l'environnement de travail (adresse refusée) : non relus.

## 2026-11-18 — Claude — Premier essai de Glacis publié sur glacis-classe.fr : 6.0.0-beta.12 et Échecs 1.1.0

- **Demande / Autorisation** : Franck, 23 h 11 : « Les secrets Cloudflare sont créés dans ma-classe-versions et glacis-classe.fr est actif sur le projet Pages. Choix validés, passerelle non. Tu peux lancer l'étape 3 : réunir le renommage dans essai, suite complète, publier Glacis en essai sur glacis-classe.fr, puis Échecs 1.1.0. »
- **Contrôle préalable** : `main` à `3e2bd45`, aucune pull request, aucune action en cours ; branche `claude/glacis-site` (`ba6af89`) réunie ici par avance rapide. Source : `Ma-classe` `essai` `de28282` (6.0.0-beta.12) ; `Applis-classe` `main` `e291299` (Échecs 1.1.0).
- **Réalisation** : retrait de tout ce qui appartenait à « Ma classe » (`stable/`, `essai/`, `appli/`, `coquille/`, `entrees/`) ; `publier-version.py` et `publier-appli.py --canal essai` (pages `Glacis.html`, `Glacis - Remplaçant.html`, coquille, `appli/essai/latest.json` vers `https://glacis-classe.fr/appli/essai/Glacis_6.0.0-beta.12_x64-setup-essai.exe`) ; Store : `publier.py echecs` (1.1.0, essai), `--retirer evar` et `--retirer dizaines-unites` (décision de Franck : seule Échecs est reprise) ; action : la signature de l'application tourne aussi quand seul le canal d'essai existe (`hashFiles` sur les deux fiches) ; README et consignes au nom de Glacis.
- **Validation** : suite complète de Ma-classe (deux moitiés parallèles) : 105 sur 106, `outils` en échec sous cette charge puis vert deux fois seul ; répétition à blanc ici (`signer.py` avec une clé jetable : « versions.json signé : essai 6.0.0-beta.12 », « applis.json signé : echecs 1.1.0 (essai) » ; `fabriquer-appli.py essai --plan` : à fabriquer ; `stable --plan` : rien).
- **Livraison / état** : envoyé sur `main` (avance rapide, sans forçage) ; action « Publier les mises à jour » : voir l'entrée suivante.

## 2026-11-18 — Claude — Passage à Glacis préparé : site sur glacis-classe.fr (`claude/glacis-site`, rien de publié)

- **Demande / Autorisation** : Franck, 18 novembre : « Les mises à jour et la page de présentation passent sur glacis-classe.fr (Cloudflare Pages) » ; « Publier seulement sur une phrase explicite de Franck ». Aucun envoi sur `main`.
- **Contrôle préalable** : `main` à `3e2bd45` ; aucune pull request ; dernière action (`44381803860`) en échec à `configure-pages` (GitHub Pages désactivé). Cloudflare (lecture seule) : projet Pages `glacis-classe` en envoi direct, branche de production `main` ; domaines `glacis-classe.fr` et `www.glacis-classe.fr` encore « pending ».
- **Réalisation** : action de publication : mise en ligne par `wrangler pages deploy` (outil fixé dans `outils/deploiement/`, secrets `CLOUDFLARE_API_TOKEN` et `CLOUDFLARE_ACCOUNT_ID` à créer) à la place de GitHub Pages ; `outils/signer.py` : canal stable facultatif, copie de `index.html`, `icone.svg`, `_headers` ; `outils/fabriquer-appli.py` : balise `glacis-version` acceptée ; page de présentation de Glacis (`index.html`, `icone.svg`) ; `DOCUMENTATION.md` § 0 (tableau avant / après, ordre des opérations).
- **Validation** : YAML de l'action relu par un analyseur (trois travaux, étapes de mise en ligne en fin de « publier ») ; `npm ci --ignore-scripts` puis `wrangler --version` (4.164.0) dans `outils/deploiement/` ; page de présentation ouverte dans Chromium sans erreur JavaScript, capture regardée. **Non essayé** : l'action elle-même (elle ne tourne que sur `main`), la mise en ligne, la fabrication d'un installateur « Glacis_… ».
- **Livraison / état** : poussé sur `claude/glacis-site` ; `main` et le site inchangés.

## 2026-11-18 — Claude — Essai 6.0.0-beta.11 « Vers Glacis » (site bloqué par GitHub Pages)

- **Demande / Autorisation** : Franck : « Oui, publier l'essai » (réunion des branches terminées : contenus neutres, crédits et licences, export La Forge, thème Glacis seul).
- **Réalisation** : `publier-version.py` et `publier-appli.py --canal essai` depuis `essai` (`f8a0fa1`) de Ma-classe ; commit `66dc45a`.
- **Validation** : suite complète de Ma-classe : 106 scénarios sur 106. Action `44381803860` : installateurs fabriqués et signés, **échec à `configure-pages`** (GitHub Pages désactivé sur ce dépôt) : le site reste à l'essai 8.
- **État** : à la réactivation de Pages (Settings › Pages › Source : GitHub Actions), relancer l'action `44381803860`. Les mises à jour passeront ensuite par glacis-classe.fr (renommage à venir).

## 2026-11-18 — Essai 6.0.0-beta.10 sur le canal d'essai (pages et application) : outils vivants, site non mis à jour (GitHub Pages désactivé)

- **Autorisation :** Franck, 17 novembre, 22 h 40 (« Lance les lots 1 à 3 séparément mais en parallèle. On ne fera pas le lot 4. ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `f96e005` ; aucune pull request ; aucune action en cours ; dernière action (`44202387233`, essai 6.0.0-beta.9) en échec à `configure-pages` (« Not Found ») ; `has_pages` faux. Source : `Ma-classe` `essai` `3d046d3` (contient l'essai 6.0.0-beta.9) ; suite complète locale 105 sur 105.
- **Contenu :** Balance à plateaux et Monnaie (chute, échanger, casser), Tableau de numération en mode Matériel (réserve de blocs à glisser), Droite graduée (pion, bonds au doigt, étiquettes) et Tableau des nombres (puzzle, croix). Coquille inchangée.
- **Livraison :** avance rapide `f96e005..55b5c4f`, sans forçage ; action `44210254629` : `Ma-classe_6.0.0-beta.10_x64-setup-essai.exe` fabriqué (3 104 Ko) et signé, signatures vérifiées comme dans l'application, « versions.json signé : essai 6.0.0-beta.10, stable 5.2.0 » ; **échec de la publication du site** à `configure-pages` (« Get Pages site failed … Not Found »), comme pour l'essai 9 : le site reste à l'essai 8. **À faire par Franck :** réactiver GitHub Pages (Settings › Pages › Source : GitHub Actions), puis relancer l'action `44210254629` (« Re-run all jobs ») : elle publie l'essai 10, qui contient aussi l'essai 9.

## 2026-11-18 — Essai 6.0.0-beta.9 sur le canal d'essai : Ma classe devient un logiciel libre (publication du site bloquée)

- **Autorisation :** Franck, 18 novembre, 0 h (« Oui et complète les crédits », après le choix de la GPL) ; canal d'essai : autorisation permanente du 8 novembre 2026.
- **Contrôle préalable :** `main` à `2802c80` ; aucune action en cours. Source : `Ma-classe` `essai` `aee92a1`.
- **Contenu :** licence GNU GPL version 3 ou ultérieure (`LICENSE`), section Licence du `README.md` (applis du Store sous leur propre licence), pied de page de `index.html` et de `DOCUMENTATION.md` ; pages et coquille 6.0.0-beta.9.
- **Livraison :** avance rapide `2802c80..75c8115`, sans forçage. L'action « Publier les mises à jour » **échoue deux fois** à `configure-pages` (« Get Pages site failed … Not Found ») : GitHub Pages semble désactivé dans les réglages du dépôt ; site non mis à jour, stable inchangé (5.2.0). À réactiver par Franck (Settings › Pages › Source : GitHub Actions), puis relancer l'action (run `44202387233`).

## 2026-11-17 — Essai 6.0.0-beta.8 sur le canal d'essai (pages et application) : pièces et billets dessinés

- **Autorisation :** Franck, 17 novembre, 22 h 58 (« génère les pièces et billets pour qu'ils ressemblent à peu près ») ; canal d'essai : autorisation permanente du 8 novembre 2026.
- **Contrôle préalable :** `main` à `12ed48e` ; aucune action en cours. Source : `Ma-classe` `essai` `0f5a43c` ; suite complète locale 102 sur 102 (avant numérotation), scénarios de version repassés après.
- **Contenu :** pièces et billets de l'outil Monnaie redessinés pour le projet (SVG en aplats, monuments inventés), à la place des reproductions officielles.
- **Livraison :** avance rapide `12ed48e..44b3384`, sans forçage ; action « Publier les mises à jour » réussie ; canal stable inchangé (5.2.0).

## 2026-11-17 — Essai 6.0.0-beta.7 sur le canal d'essai (pages et application) : réglettes Cuisenaire

- **Autorisation :** Franck, 17 novembre, 19 h 36 (« Fais un outil drag and drop avec effets visuels pour avoir un rendu smooth et plus naturel (comme la balance des nombres), qui reprend les cuisenaires avec toutes les fonctions conseillées ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `c04a72d` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `79e7f4c` (réunit les essais 6.0.0-beta.5 et 6.0.0-beta.6) ; suite complète locale 102 sur 102. Coquille inchangée.
- **Contenu :** outil « Réglettes Cuisenaire » dans le menu Outils (glisser-déposer sur le module commun de physique, trains aimantés, Comparer et écarts, Escalier, règle graduée, calculs) ; fenêtre d'outil à manipuler rouverte aussitôt.
- **Livraison :** avance rapide `c04a72d..b5c0646`, sans forçage ; action `44179812414` réussie (« versions.json signé : essai 6.0.0-beta.7, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.7_x64-setup-essai.exe` signé, signature vérifiée comme dans l'application ; stable `Ma-classe_5.2.0_x64-setup.exe` inchangé).

## 2026-11-17 — Essai 6.0.0-beta.6 sur le canal d'essai (pages et application) : outils à manipuler, un même toucher, secousse de refus

- **Autorisation :** Franck, 17 novembre, 19 h 43 (« Fais le lot 0 ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `0c48067` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `7751457` (réunit l'essai 6.0.0-beta.5) ; suite complète locale 101 sur 101 sur la page numérotée.
- **Contenu :** module commun de physique (`coeur/physique.js`) pour les outils à manipuler ; Balance des nombres et Boîtes de 10 branchées dessus, boîte pleine et crochet plein secoués. Coquille inchangée.
- **Livraison :** avance rapide `0c48067..a9b9575`, sans forçage ; action `44170243838` réussie (« versions.json signé : essai 6.0.0-beta.6, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.6_x64-setup-essai.exe` fabriqué (3 234 Ko), signé, signature vérifiée comme dans l'application ; pages publiées).

## 2026-11-17 — Essai 6.0.0-beta.5 sur le canal d'essai (pages et application) : pastilles aux couleurs de Ma classe

- **Autorisation :** Franck, 17 novembre, 19 h 32 (« Oui », à la proposition de passer les pastilles dans une palette propre) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `774f316` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `ae069d7` ; suite complète locale 101 sur 101. Coquille inchangée.
- **Livraison :** avance rapide `774f316..99e4516`, sans forçage ; action `44157449102` réussie (« versions.json signé : essai 6.0.0-beta.5, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.5_x64-setup-essai.exe` fabriqué (3 233 Ko), signé, signature vérifiée comme dans l'application ; pages publiées).

## 2026-11-17 — Essai 6.0.0-beta.4 sur le canal d'essai (pages et application) : fenêtre de l'application aux couleurs de Ma classe

- **Autorisation :** Franck, 17 novembre, 17 h 16 (« Oui, je veux que tu intègres la barre du haut dans le design. J'ai envie que l'encadré dans lequel se trouve l'appli soit en accord avec tout le reste ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `1eb8eef` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `6ed75b7` ; suite complète locale 101 sur 101 (nouveau scénario `cadre_fenetre`).
- **Coquille modifiée :** `tauri.conf.json` (fenêtre principale sans barre de titre : `decorations: false`, `shadow: true`) et `capabilities/default.json` (permissions `minimize`, `toggle-maximize`, `close`, `start-dragging`).
- **Livraison :** avance rapide `1eb8eef..b304761`, sans forçage ; action `44134525761` réussie (« versions.json signé : essai 6.0.0-beta.4, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.4_x64-setup-essai.exe` fabriqué (3 233 Ko) avec la coquille modifiée, signé ; pages publiées).

## 2026-11-17 — Essai 6.0.0-beta.3 sur le canal d'essai (pages et application) : mode TBI/ENI, écrire au tableau et par-dessus l'écran

- **Autorisation :** demande de Franck du 17 novembre, 15 h 27 (« Fais ce mode pour les tableaux, avec mémorisation de l'écriture comme pour les éléments des tableaux. Puis ajoute un mode pour écriture par dessus les autres rituels ou application (comme une surcouche), activable rapidement. Ces modes ne viendraient que en mode tbi. ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `a547929` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `b4bf35c` ; suite complète locale 100 sur 100 (nouveau scénario `mode_tbi` ; `reprise_ecriture` relancé seul après un échec sous la charge).
- **Livraison :** avance rapide `a547929..213270a`, sans forçage ; action `44125041476` réussie (« versions.json signé : essai 6.0.0-beta.3, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.3_x64-setup-essai.exe` fabriqué (3 231 Ko), signé, signature vérifiée comme dans l'application ; pages publiées).

## 2026-11-17 — Essai 6.0.0-beta.2 sur le canal d'essai (pages et application) : outils à manipuler dans le menu Outils

- **Autorisation :** Franck, 17 novembre, 12 h 35 (« Ils doivent être dans Outils pas un tableau à part ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `d31a374` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `1afd051` ; suite complète locale 99 sur 99.
- **Livraison :** avance rapide `d31a374..2a0afdb`, sans forçage ; action `44090545283` réussie (« versions.json signé : essai 6.0.0-beta.2, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.2_x64-setup-essai.exe` signé, signature vérifiée comme dans l'application ; pages publiées).

## 2026-11-17 — Essai 6.0.0-beta.1 sur le canal d'essai (pages et application) : casse en forme de paquet, tableau « Manipuler »

- **Autorisation :** demande de Franck du 17 novembre, 10 h 32 (casse des barres de 10 : « la forme globale du paquet est conservée, mais seulement, les unités sont espacées » ; nouveaux outils à glisser-déposer : boîtes de 10 jetons, balance des nombres, triangle des opérations) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `c90cfa3` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `66e113f` ; suite complète locale 99 sur 99 (nouveau scénario `manipuler`).
- **Premier numéro en versionnage sémantique :** `6.0.0-beta.1` (« 6.0 · essai 1 »), lu par la coquille 5.2.51 publiée juste avant.
- **Livraison :** avance rapide `c90cfa3..0d5cedc`, sans forçage ; action `44069168136` réussie (« versions.json signé : essai 6.0.0-beta.1, stable 5.2.0 » ; `Ma-classe_6.0.0-beta.1_x64-setup-essai.exe` signé, signature vérifiée comme dans l'application ; pages publiées).

## 2026-11-17 — Essai 5.2.51 sur le canal d'essai (pages et application) : numéros de version vers la 6.0, outils prêts pour les pré-versions

- **Autorisation :** Franck, 17 novembre, 0 h 28 (« Go option b alors » : versionnage sémantique, essais `6.0.0-beta.N`) ; règle permanente du canal d'essai (8 novembre).
- **Contrôle préalable :** `main` à `5f36e3f` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `4da565f` ; suite complète locale 98 sur 98.
- **Outils :** `outils/signer-appli.py` lit un numéro avec suffixe dans le nom de l'installateur (`Ma-classe_6.0.0-beta.1_x64-setup-essai.exe`) ; `outils/fabriquer-appli.py` (`trois`) garde le suffixe ; `DOCUMENTATION.md` : numéros et ordre. Vérifié : expression du nom sur 5.2.51, 6.0.0-beta.1 et 6.0.0.
- **Essai de transition :** la coquille 5.2.51 apprend à l'application installée les numéros `6.0.0-beta.N` ; l'essai suivant portera ce numéro.
- **Livraison :** avance rapide `5f36e3f..79ef7ad`, sans forçage ; action `43989759974` réussie (« versions.json signé : essai 5.2.51, stable 5.2.0 », installateur d'essai 5.2.51 fabriqué avec la nouvelle coquille, signé et vérifié comme dans l'application ; stable inchangé).

## 2026-11-17 — Essai 5.2.50 sur le canal d'essai (pages et application) : couleurs et forme des unités (Tableaux › Numération), séries de calcul complètes

- **Autorisation :** demande de Franck du 16 novembre, 23 h 04 (couleurs des unités, forme des paquets défaits, option debout / couché, Calcul mental figé en CP, contrôle hors CP) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `b550dd2` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `336a0d5` ; suite complète locale 98 sur 98.
- **Livraison :** avance rapide `b550dd2..4d389cc`, sans forçage ; action `43976782590` réussie (« versions.json signé : essai 5.2.50, stable 5.2.0 », installateur d'essai 5.2.50 signé et vérifié, pages publiées).

## 2026-11-16 — Essai 5.2.49 sur le canal d'essai (pages et application) : outil Tableau de numération animé

- **Autorisation :** réponse de Franck du 16 novembre, 19 h 01 (« Ca me va. Applique ça dans l'application », sur la proposition d'animer l'outil Tableau de numération) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `6358e1e` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `6d00aa8` ; suite complète locale 98 sur 98.
- **Livraison :** avance rapide `6358e1e..52415aa`, sans forçage ; action `43933584643` réussie (« versions.json signé : essai 5.2.49, stable 5.2.0 », installateur d'essai 5.2.49 signé et vérifié, pages publiées).

## 2026-11-16 — Essai 5.2.48 sur le canal d'essai (pages et application) : paquet et casse animés (Tableaux › Numération)

- **Autorisation :** demandes de Franck du 16 novembre, 16 h 19 et 17 h 07 (« un effet visuel plus rapide et qui fonctionne avec les représentations déjà utilisées sur le tableau numération ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `0d079cc` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `27e1ecd` ; suite complète locale 98 sur 98.
- **Livraison :** avance rapide `0d079cc..d7cd1ea`, sans forçage ; action `43913914056` réussie (« versions.json signé : essai 5.2.48, stable 5.2.0 », installateur d'essai 5.2.48 signé et vérifié, pages publiées).

## 2026-11-15 — Essai 5.2.47 sur le canal d'essai (pages et application) : pauses déplaçables, À propos sans IA, lecteur audio retiré

- **Autorisation :** demandes de Franck du 15 novembre, 16 h 27 à 16 h 40 (mention de l'IA retirée de Réglages › À propos, présentation seulement ; lecteur audio retiré ; erreur « fichier illisible reglages/postes/._… » ; récréations et pause méridienne déplaçables) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `9298e6a` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `42eea93` ; suite complète locale 98 sur 98.
- **Documentation :** `DOCUMENTATION.md`, point 8 : l'application ne mentionne plus l'aide de l'IA ; la mention reste sur la page de présentation et dans le README (inchangés).
- **Livraison :** avance rapide `9298e6a..61ac3ab`, sans forçage ; action `43736332836` réussie (« versions.json signé : essai 5.2.47, stable 5.2.0 », installateur d'essai 5.2.47 signé et vérifié, pages publiées).

## 2026-11-15 — Essai 5.2.46 sur le canal d'essai (pages et application) : rituels en cartes, lots 2 et 3, corrigé du plan

- **Autorisation :** demande de Franck du 15 novembre, 10 h 37 (plan du Nombre du jour, corrigé du plan au tableau, « Puis fais les derniers lots ») ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `b9a8132` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `72a4f67` ; suite complète locale 97 sur 97.
- **Livraison :** avance rapide `b9a8132..42ec6e2`, sans forçage ; action `43704752920` réussie (« versions.json signé : essai 5.2.46, stable 5.2.0 », installateur d'essai 5.2.46 signé et vérifié, pages publiées).

## 2026-11-15 — Essai 5.2.45 sur le canal d'essai (pages et application) : rituels en cartes, lot 1

- **Autorisation :** demande de Franck du 15 novembre, 8 h 22 et 8 h 38 (enrichir les rituels comme le Calcul mental ; lot 1 : Fluence, Nombre du jour, Date du jour, plans sans prénom) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `1a7ea76` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `b2122a8` ; suite complète locale 96 sur 97 (`ergonomie`, fragile sous charge, vert seul et après numérotation).
- **Livraison :** avance rapide `1a7ea76..e442d70`, sans forçage ; action `43695559864` réussie (« versions.json signé : essai 5.2.45, stable 5.2.0 », installateur d'essai 5.2.45 signé et vérifié, pages publiées).

## 2026-11-15 — Essai 5.2.44 sur le canal d'essai (pages et application) : journée validée par l'enseignant, calcul mental

- **Autorisation :** demande de Franck du 14 novembre, 23 h 30 (le créneau de la journée ne change qu'à la validation de l'enseignant, l'assistant propose de valider ; démonstration de fin de journée sans ½ ni ✕ ; Calcul mental : 6 à 12 calculs, minuteur avec la nouvelle série, couleurs des lignes, plan à plastifier) ; règle permanente du canal d'essai. Stable inchangé.
- **Contrôle préalable :** `main` à `21a85f0` ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `a42611e` ; suite complète locale 96 sur 96.
- **Livraison :** avance rapide `21a85f0..05c8426`, sans forçage ; action `43656934139` réussie (« versions.json signé : essai 5.2.44, stable 5.2.0 », installateur d'essai 5.2.44 signé et vérifié, pages publiées).

## 2026-11-14 — Essai 5.2.43 (pages et application) ; actions de publication sur leurs dernières versions (Node 24)

- **Autorisation :** Franck, 21 h 48 : « Fais : Deux postes ouverts en même temps, Lecteur PDF, lot 4, Petite dette » (la petite dette comprend les actions encore en Node 20) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` à `b93740e` (historique réécrit) ; aucune pull request ; aucune action en cours. Source : `Ma-classe` `essai` `3cb08d2` ; suite complète locale 95 sur 95.
- **Actions :** checkout 7.0.1, setup-python 7.1.0, setup-node 7.1.0, cache 6.1.0, upload-artifact 7.0.2, download-artifact 8.0.2, configure-pages 6.0.0, upload-pages-artifact 5.0.0 (fichiers cachés exclus : le site n'en a pas), deploy-pages 5.0.1, rust-cache 2.9.3, toutes désignées par leur commit ; Node 24 pour les outils (`DOCUMENTATION.md`). Essai préalable sur la branche de fabrication seule `claude/fabrication-node24` (action `43640091211`, réussie : installateur recompilé, `npm ci`, `--locked`, chaîne de signature à blanc bonne).
- **Livraison :** avance rapide `b93740e..ee4da6f`, sans forçage ; action `43646060907` réussie avec les nouvelles actions (« versions.json signé : essai 5.2.43, stable 5.2.0 », installateur 5.2.43 signé et vérifié, pages déployées) ; plus d'avertissement Node 20.
- **Reste :** branche `claude/fabrication-node24` (fabrication seule) à supprimer avec les autres par l'action « Nettoyer les branches ». Avis de GitHub : `ubuntu-latest` passe à Ubuntu 26 progressivement ; rien à faire tant que la publication réussit.

## 2026-11-14 — Historique du dépôt public réécrit : adresse e-mail personnelle remplacée (S4 de l'audit)

- **Autorisation :** Franck, 14 novembre, 21 h 25 : « Ne réécris pas l'historique si c'est en privé, mais en public oui. »
- **Contrôle préalable :** `main` à `097a815` (journal de l'essai 5.2.42, publié par une autre conversation à 21 h 19) ; aucune action en cours sur `main` ; aucune pull request. Adresse personnelle trouvée dans **un seul commit** (`0accc7a`, 7 novembre 2026, « Ma classe 5.0.4 : assistant sans IA sur le canal d'essai », auteur et committer), contenu dans les 15 branches.
- **Réalisation :** copie miroir, `git filter-repo --mailmap` (adresse personnelle → `Harry-Safe@users.noreply.github.com`, nom « Franck VARAULT ») ; rien d'autre changé (les commits signés « Claude » et les anciennes lignes de co-écriture restent, comme le veut `AGENTS.md`). Contrôle : pour chacune des 15 branches, l'arbre de fichiers réécrit est **identique** à l'ancien ; plus aucune adresse personnelle dans l'historique. Envoi forcé de chaque branche avec `--force-with-lease` (ancien identifiant exigé) ; les 15 branches distantes vérifiées une à une. `main` : `097a815` → `11eb908`.
- **Publication :** l'envoi de `main` a relancé l'action `43637597753` : réussie (« versions.json signé : essai 5.2.42, stable 5.2.0 », installateurs stable et d'essai signés et vérifiés) ; aucun contenu changé.
- **Suites :** correspondance ancien → nouvel identifiant dans `historique/commits-reecrits-2026-11-14.txt` (les journaux gardent les anciens identifiants) ; exception notée dans `AGENTS.md` ; **toute copie de ce dépôt faite avant doit être re-clonée** (une conversation qui garderait l'ancienne copie verrait son envoi refusé, sans perte). Limite : GitHub peut encore montrer l'ancien commit à qui connaît son identifiant exact, jusqu'à son nettoyage ; seul le support de GitHub peut l'accélérer.

## 2026-11-14 — Essai 5.2.42 sur le canal d'essai (pages et application) : fichiers et sites dans le dock, nouveau site

- **Autorisation :** demande de Franck du 14 novembre, 20 h 12 (fichiers et sites gardés dans le dock, ampoule plus rentrée, « Nouveau site » ouvert dans le navigateur par défaut, tutoriels à jour) ; règle permanente du canal d'essai.
- **Contrôle préalable :** `main` à `cea3bbf` ; aucune pull request. Source : `Ma-classe` `essai` `e0ea4d1` ; suite complète locale 90 sur 94 avant numérotation, les 4 scénarios en échec corrigés (textes des tutoriels, tests mis à jour) puis verts relancés seuls ; scénarios sensibles à la version relancés après.
- **Livraison :** avance rapide `cea3bbf..4caedfc`, sans forçage ; action `43636536987` réussie (installateur d'essai 5.2.42 signé et vérifié, pages publiées).

## 2026-11-14 — Essai 5.2.41 sur le canal d'essai (pages et application) : séances rangées et notes sur l'Accueil

- **Autorisation :** demande de Franck du 14 novembre, 18 h 29 (séances des Tableaux et des Rituels rangées, assistant plus discret, widget Notes lié aux Rappels) ; règle permanente du canal d'essai.
- **Contrôle préalable :** `main` à `59fc44f` ; aucune pull request. Source : `Ma-classe` `essai` `2eab2fb` ; suite complète locale 92 sur 93 avant numérotation, le scénario en échec mis à jour pour le menu commun puis vert ; scénarios sensibles à la version relancés après.
- **Livraison :** avance rapide `59fc44f..cea3bbf`, sans forçage ; action `43627101673` réussie (installateur d'essai 5.2.41 signé et vérifié, pages publiées).

## 2026-11-14 — Essai 5.2.40 sur le canal d'essai (pages et application) : icônes, dock et problèmes à manipuler

- **Autorisation :** Franck, 14 novembre, 17 h 06 : correction illustrée, « Manipuler », cadran dans le sens des aiguilles, et « j'aimerais que tu mixtes avec la mise à jour de design (icone et barre qu'on a fait dans une autre conversation) » ; règle permanente du canal d'essai.
- **Contrôle préalable :** `main` à `1c9f747` ; aucune pull request. Source : `Ma-classe` `essai` `e57aba2` (réunit `claude/icones-dock` et `claude/illustrer-manipuler`) ; suite complète locale 92 sur 92 avant numérotation, scénarios sensibles à la version relancés après.
- **Livraison :** avance rapide `1c9f747..ed85f2b`, sans forçage ; action `43619347297` réussie (installateur d'essai 5.2.40 signé et vérifié, pages publiées).

## 2026-11-14 — Essai 5.2.39 sur le canal d'essai (pages et application) : balance, minuteur et schémas illustrés

- **Autorisation :** demande de Franck du 14 novembre (balance en glisser-déposer, minuteur affiné aux durées modulables, option « Illustrer » des schémas de problèmes) ; règle permanente du canal d'essai.
- **Contrôle préalable :** `main` à `0d6bf4a` ; aucune pull request. Source : `Ma-classe` `essai` `667f8ef` ; suite complète locale 90 sur 91 avant les derniers correctifs (ordre d'une étape du tutoriel du minuteur, sens du widget Minuteur), scénarios concernés relancés ensuite (voir le journal de `Ma-classe`).
- **Livraison :** avance rapide `0d6bf4a..d4e47f9`, sans forçage ; action `43607501146` réussie (installateur d'essai 5.2.39 signé et vérifié, pages publiées).

## 2026-11-13 — Essai 5.2.38 sur le canal d'essai (pages et application) : micro et caméra des anciens sites coupés

- **Autorisation :** Franck : « Oui, couper » (micro et caméra des sites enregistrés avant le 5 novembre) ; règle permanente du canal d'essai. Stable non concerné : Franck prévoit une **version 6.0** de référence (« on cumule les nouveaux en beta »), sans stable intermédiaire.
- **Contrôle préalable :** `main` à `dd4d923` ; aucune pull request. Source : `Ma-classe` `essai` `c1d658f` ; suite complète locale 90 sur 90 avant numérotation, scénarios sensibles à la version relancés après.
- **Livraison :** avance rapide `dd4d923..5309881`, sans forçage ; action `43514850423` réussie (« versions.json signé : essai 5.2.38, stable 5.2.0 », installateur 5.2.38 signé et vérifié).

## 2026-11-13 — Essai 5.2.37 (pages et application) : remise en ordre et fiabilité ; « Essai du pont » retiré du Store

- **Autorisation :** Franck : « Fais les trois derniers lots » (lots D, E, F de l'audit) ; règle permanente du canal d'essai. Stable non publié (lot E préparé, en attente de Franck).
- **Contrôle préalable :** `main` à `9625e72` (journal de l'essai 5.2.36) ; aucune pull request. Source : `Ma-classe` `essai` `91aaee7` (5.2.36 + `claude/lots-d-e-f`), numérotée par `build/numeroter-essai.py` ; suite complète locale 89 sur 90 (`reprise_ecriture`, course de minutage connue, verte seule et sous charge 8 fois sur 8), scénarios sensibles à la version relancés après numérotation.
- **Préparation :** `publier-version.py --canal essai`, `publier-appli.py --canal essai` ; `outils/publier.py --retirer essai-pont … --canal essai` d'`Applis-classe` (entrée et paquet retirés) ; nouvelle action `.github/workflows/nettoyer-branches.yml`, **à lancer à la main** (la suppression de branches est refusée aux assistants) ; `DOCUMENTATION.md`.
- **Livraison :** avance rapide `9625e72..38e3827`, sans forçage ; action `43504076972` réussie (« versions.json signé : essai 5.2.37, stable 5.2.0 », catalogue sans `essai-pont`, installateur 5.2.37 signé et vérifié).
- **À faire par Franck :** Actions › Nettoyer les branches › Run workflow : d'abord « non » (liste), puis « oui ».

## 2026-11-13 — Lot C de l'audit de sécurité : chaîne de signature fixée, puis essai 5.2.36 (pages et application)

- **Autorisation :** Franck : « Fais le lot C », en réponse au plan qui annonçait que ce lot modifie ce dépôt et qu'un envoi sur `main` republie le site ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` à `77a21a6` (journal de l'essai 5.2.35) ; aucune pull request. Source de l'essai : `Ma-classe` `essai` `cf0291a` (5.2.35 + `claude/lot-c-signature`), numérotée par `build/numeroter-essai.py` ; suite complète locale 90 verts sur 90.
- **Chaîne de signature (S6) :** actions désignées par leur commit ; `outils/exigences.txt` (`cryptography` 50.0.2, `cffi` 2.1.1, `pycparser` 3.12, empreintes exigées) ; outil de signature installé par `npm ci --ignore-scripts` depuis `outils/signature/package-lock.json` avant que la clé soit dans l'environnement ; `signer-appli.py` revérifie chaque signature avec la `CLE_MAJ` de la coquille (ancienne clé seulement par `outils/cle-precedente.txt`, pendant un changement de clé) et essaie toute la chaîne avec une clé jetable sur les branches de fabrication (`--a-blanc`) ; fabrication par `npm ci --ignore-scripts` et `cargo --locked` (numéro reporté dans `Cargo.lock`). Documentation : `DOCUMENTATION.md`.
- **Essais avant publication :** branche de fabrication seule `claude/fabrication-lot-c` (action `43487615070`, réussie) : installateur d'essai recompilé avec `npm ci` et `--locked`, chaîne à blanc bonne pour les deux canaux.
- **Livraison 1, chaîne seule :** avance rapide de `main` `77a21a6..6549802`, sans forçage ; action `43488323351` réussie : « signature vérifiée comme dans l'application » pour 5.2.0 et 5.2.35 avec la vraie clé.
- **Livraison 2, essai 5.2.36 :** `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (coquille avec `package-lock.json`, 18 fichiers) ; avance rapide `6549802..f8ce401` ; action `43494284901` réussie (installateur 5.2.36 fabriqué par `npm ci` et `cargo --locked`, « versions.json signé : essai 5.2.36, stable 5.2.0 », signature vérifiée avant publication).
- **Reste :** branches de fabrication `claude/fabrication-lot-b`, `-lot-b-2` et `-lot-c` non supprimées (accès en écriture refusé) ; sans effet sur les publications. Les actions annoncent la fin de Node 20 sur les runners (forcées en Node 24) : à suivre lors d'une prochaine mise à jour des actions.
- **À vérifier sur le PC :** la mise à jour vers 5.2.36 s'installe ; un site épinglé (Solaire) s'affiche et se connecte toujours dans Ma classe.

## 2026-11-13 — Essai 5.2.35 sur le canal d'essai (pages et application) : sécurité de l'application Windows

- **Autorisation :** Franck : « Corrigé ce qu'il faut et fait le lot b » (lot B de l'audit de sécurité) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `1800ffc` (journal de l'essai 5.2.34) ; aucune pull request. Source : `Ma-classe` `essai` `994ac0b` (5.2.34 + `claude/lot-b-application`, réunie avec la 5.2.34 publiée entre-temps), numérotée par `build/numeroter-essai.py` ; suite complète locale 90 verts sur 90 ; coquille compilée pour Windows au préalable par la branche de fabrication seule `claude/fabrication-lot-b-2` (action `43458300778`, rien de signé ni publié).
- **Préparation :** `publier-version.py --canal essai` puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`994ac0b`), `appli/essai/latest.json`, coquille d'essai (`lib.rs`, `tauri.conf.json`, `chemins.rs` nouveau).
- **Livraison :** avance rapide de `main` `1800ffc..b239835`, sans forçage. Action « Publier les mises à jour » `43464627231` réussie (« versions.json signé : essai 5.2.35, stable 5.2.0 », `Ma-classe_5.2.35_x64-setup-essai.exe` fabriqué et signé, pages déployées).
- **Reste :** branches `claude/fabrication-lot-b` et `claude/fabrication-lot-b-2` (fabrication seule) non supprimées, l'accès en écriture le refusant ; sans effet sur les publications.
- **À vérifier sur le PC :** après la mise à jour, l'application s'ouvre sur le dossier « Ma classe » sans le redemander ; PDF, Word, images, Accueil et applis du Store fonctionnent ; un site extérieur s'ouvre toujours dans sa fenêtre.

## 2026-11-13 — Essai 5.2.34 sur le canal d'essai (pages et application) : applis du Store, dossier retrouvé

- **Autorisation :** Franck, en classe, après « Dossier « Ma classe » introuvable » à l'ouverture d'une appli du Store : « Oui rapidement s'il te plait » (correctif en essai) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `017588b` (journal de l'essai 5.2.33) ; aucune pull request. Source : `Ma-classe` `essai` `d131409` (5.2.33 + `claude/dossier-retenu-applis`), numérotée par `build/numeroter-essai.py` ; suite complète locale 89 verts sur 89 sur la branche de travail.
- **Préparation :** `publier-version.py --canal essai` (garde passée, configuration d'exemple seule) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`d131409`), `appli/essai/latest.json`, `coquille/essai/…/lib.rs` (commande `reprendre_dossier`) ; stable et coquille stable inchangés.
- **Livraison :** avance rapide de `main` `017588b..9e6a2ed`, sans forçage. Action « Publier les mises à jour » `43453894238` réussie (installateur d'essai 5.2.34 fabriqué et signé, pages déployées) ; `appli/latest.json` et `entrees/stable.json` toujours en 5.2.0.
- **À vérifier sur le PC :** après la mise à jour de l'application d'essai, une appli du Store s'ouvre sans avoir à rechoisir le dossier.

## 2026-11-13 — Essai 5.2.33 sur le canal d'essai (pages et application) : sécurité, fichiers piégés

- **Autorisation :** Franck : « Fais le lot a » (lot A de l'audit de sécurité) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `e15bb15` (journal de l'essai 5.2.32) ; aucune pull request. Source : `Ma-classe` `essai` `d61f95e` (5.2.32 + `claude/fichiers-pieges` + `claude/donnees-personnelles`), numérotée par `build/numeroter-essai.py` ; suite complète locale 88 verts sur 89, l'échec (`accueil_widgets_culture`, fenêtre d'accueil du remplaçant ouverte en retard sur une machine chargée) sans fichier commun avec le lot, scénario rendu patient et vert seul deux fois.
- **Préparation :** `publier-version.py --canal essai` (garde passée, configuration d'exemple seule) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`d61f95e`), `appli/essai/latest.json` ; stable, coquille et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `e15bb15..280c44e`, sans forçage. Action « Publier les mises à jour » `43433790967` réussie (« versions.json signé : essai 5.2.33, stable 5.2.0 », `Ma-classe_5.2.33_x64-setup-essai.exe` signé).
- **À vérifier sur le PC :** ouvrir une séance de tableau enregistrée et un Word des Documents (rien ne doit être refusé à tort).

## 2026-11-13 — Essai 5.2.32 sur le canal d'essai (pages et application) : billets sans la mention SPECIMEN

- **Autorisation :** Franck : « Pas de mention spécimen, car c'est pour afficher au tableau seulement, pour des enfants. » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `2589475` (journal de l'essai 5.2.31). Source : `Ma-classe` `essai` `e833c82` (5.2.31 + `claude/billets-sans-specimen`), numérotée par `build/numeroter-essai.py` ; suite complète locale 88 verts sur 88.
- **Préparation :** `publier-version.py --canal essai` (garde passée, configuration d'exemple seule) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`e833c82`), `appli/essai/latest.json` ; stable, coquille stable et catalogue inchangés.
- **Livraison :** avance rapide de `main` `2589475..b9fad11`, sans forçage. Action « Publier les mises à jour » `43389457124` réussie (« versions.json signé : essai 5.2.32, stable 5.2.0 »).

## 2026-11-13 — Essai 5.2.31 sur le canal d'essai (pages et application) : Accueil, mot et phrase du jour, ce jour-là, carte et œuvre

- **Autorisation :** Franck : « Lance les deux lots en parallèle » (lots 3 et 4 des widgets de l'Accueil) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `96cd9df` (journal de l'essai 5.2.30). Source : `Ma-classe` `essai` `8e9cddc` (5.2.30 + `claude/accueil-widgets-lot3` + `claude/accueil-widgets-lot4`), numérotée par `build/numeroter-essai.py` ; suite complète locale 87 verts sur 88, le test en échec (attente trop courte sous charge) vert seul et rendu plus patient, voir le journal du dépôt source.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`8e9cddc`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `96cd9df..5d64b0a`, sans forçage. Action « Publier les mises à jour » `43385277864` réussie (« versions.json signé : essai 5.2.31, stable 5.2.0 », `Ma-classe_5.2.31_x64-setup-essai.exe`).
- **À vérifier sur le PC :** lisibilité au vidéoprojecteur de la phrase analysée et de la carte.

## 2026-11-13 — Essai 5.2.30 sur le canal d'essai (pages et application) : outils plus légers et plus justes

- **Autorisation :** Franck : « Fais ça, lance les en parallèle chacune sur sa branche. On garde le lot 5 pour la fin. » (lots 1 à 3 de l'audit des outils) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `01a5db6` (journal de l'essai 5.2.29). Source : `Ma-classe` `essai` `435eecb` (5.2.29 + audit des outils + `claude/outils-lot1-vieux-pc`, `claude/outils-lot2-exactitude`, `claude/outils-lot3-billets`), numérotée par `build/numeroter-essai.py` ; suite complète locale 86 verts sur 86.
- **Préparation :** `publier-version.py --canal essai` (garde passée, configuration d'exemple seule) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`435eecb`), `appli/essai/latest.json` ; stable, coquille stable et catalogue inchangés.
- **Livraison :** avance rapide de `main` `01a5db6..0f89144`, sans forçage. Action « Publier les mises à jour » `43378928960` : installateurs fabriqués, mais déploiement des pages refusé par GitHub (« Fetching artifact metadata failed », puis, à la relance du seul travail, « Multiple artifacts named github-pages ») ; nouveau lancement manuel `43379463463` : même refus ; troisième lancement `43379811497`, deux minutes plus tard : réussi (« versions.json signé : essai 5.2.30, stable 5.2.0 », `Ma-classe_5.2.30_x64-setup-essai.exe`). Aucun fichier retouché entre les lancements.
- **À vérifier sur le PC :** fluidité de l'Accueil et des fenêtres sur le PC de classe (gain mesuré seulement en simulation) ; billets marqués SPECIMEN dans la Monnaie et la numération des Tableaux.

## 2026-11-13 — Essai 5.2.29 sur le canal d'essai (pages et application) : Accueil, widgets de tous niveaux

- **Autorisation :** Franck : « Fais les lots 1 et 2 » (widgets de l'Accueil utiles jusqu'au CM2) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `3fd107c` (journal de l'essai 5.2.28). Source : `Ma-classe` `essai` `0e49999` (5.2.28 + `claude/accueil-widgets-niveaux`), numérotée par `build/numeroter-essai.py` ; suite complète locale sur l'essai réuni : 84 verts sur 84.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`0e49999`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `3fd107c..4726223`, sans forçage. Action « Publier les mises à jour » `43331081410` réussie (« versions.json signé : essai 5.2.29, stable 5.2.0 », `Ma-classe_5.2.29_x64-setup-essai.exe`).
- **À vérifier sur le PC :** les cinq nouveaux widgets au vidéoprojecteur (lisibilité du calcul mental en petite taille).

## 2026-11-12 — Essai 5.2.28 sur le canal d'essai (pages et application) : l'assistant s'occupe de la fin de semaine, de la fin de période et de l'entretien

- **Autorisation :** Franck : « Fais le lot 6 » (audit de l'assistant) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `eac37c2` (journal de l'essai 5.2.27, source `cf0fe1a`). Source : `Ma-classe` `essai` `85bf16c` (5.2.27 + `claude/assistant-lot-6`), numérotée par `build/numeroter-essai.py` ; suite complète locale 84 verts sur 84 sur la branche de travail (`436ce6c`), scénarios rapides relancés sur l'essai numéroté.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques), `entrees/essai.json`, `entrees/essai.source` (`85bf16c`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `eac37c2..4d29bb4`, sans forçage. Action « Publier les mises à jour » `43320918571` réussie (« versions.json signé : essai 5.2.28, stable 5.2.0 », `Ma-classe_5.2.28_x64-setup-essai.exe` signé).
- **À vérifier sur le PC :** la carte « Applis à mettre à jour » (testée avec un catalogue simulé dans le navigateur).

## 2026-11-12 — Essai 5.2.27 sur le canal d'essai (pages et application) : classe de démonstration et tutoriels où l'on fait le geste

- **Autorisation :** Franck : « Fais le lot 5 » (audit de l'assistant) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `1f8418b` (journal de l'essai 5.2.26, source `b4b11c6`). Source : `Ma-classe` `essai` `cf0fe1a` (5.2.26 + `claude/assistant-lot-5`), numérotée par `build/numeroter-essai.py` ; suite complète locale 83 verts sur 83 sur la branche de travail (`8284288`), scénarios rapides relancés sur l'essai numéroté.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques), `entrees/essai.json`, `entrees/essai.source` (`cf0fe1a`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `1f8418b..2626c79`, sans forçage. Action « Publier les mises à jour » `43310288322` réussie (« versions.json signé : essai 5.2.27, stable 5.2.0 », `Ma-classe_5.2.27_x64-setup-essai.exe` signé).
- **À vérifier sur le PC :** la classe de démonstration s'ouvre dans un cadre ; elle n'a été testée que dans le navigateur, pas dans l'application Windows.

## 2026-11-12 — Essai 5.2.26 sur le canal d'essai (pages et application) : recherche dans Ma classe (Ctrl K) et vingt nouveaux tutoriels

- **Autorisation :** Franck : « Fais les lots 3 et 4 » (audit de l'assistant) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `cbe4390` (journal de l'essai 5.2.25, source `870963c`). Source : `Ma-classe` `essai` `b4b11c6` (5.2.25 + `claude/assistant-lots-3-4`), numérotée par `build/numeroter-essai.py` ; suite complète locale 81 verts sur 82 sur la branche de travail, le 82e (`assistant_sonde`) adapté dans le scénario seul et vert sur la même page ; après numérotation, `mises_a_jour`, `chargement`, `assistant_recherche`, `assistant_sonde` et `applis` verts.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques), `entrees/essai.json`, `entrees/essai.source` (`b4b11c6`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `cbe4390..36d1c8d`, sans forçage. Action « Publier les mises à jour » `43298839628` réussie (« versions.json signé : essai 5.2.26, stable 5.2.0 », `Ma-classe_5.2.26_x64-setup-essai.exe` signé).

## 2026-11-12 — Essai 5.2.25 sur le canal d'essai (pages et application) : l'assistant agit (bilan, reports, cantine, métiers, rapport)

- **Autorisation :** Franck : « Prends en compte les derniers changements opérés et fais le lot 2 » (audit de l'assistant) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `0317943` (journal de l'essai 5.2.24, source `f3de8d3`). Source : `Ma-classe` `essai` `870963c` (5.2.24 + `claude/assistant-lot-2`), numérotée par `build/numeroter-essai.py` ; suite complète locale 81 sur 81 sur la branche de travail, « Tout est bon. » ; après numérotation, `mises_a_jour`, `chargement`, `assistant_actions` et `assistant` verts.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques), `entrees/essai.json`, `entrees/essai.source` (`870963c`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `0317943..e2bfac7`, sans forçage. Action « Publier les mises à jour » `43282328765` réussie (« versions.json signé : essai 5.2.25, stable 5.2.0 », `Ma-classe_5.2.25_x64-setup-essai.exe` signé).

## 2026-11-12 — Essai 5.2.24 sur le canal d'essai (pages et application) : fiches de préparation ; « En ce moment » et « Consignes » lisent la fiche

- **Autorisation :** Franck, 12 novembre, 16 h 58 : « Je veux que le widget En ce moment ainsi que Consigne change. Les deux doivent désormais partager la même chose : une fiche de préparation simplifiée. » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `a7cec66` (journal de l'essai 5.2.23, source `96e875a`). Source : `Ma-classe` `essai` `f3de8d3` (5.2.23 + `claude/fiches-preparation` + le commit de journal de l'essai 5.2.23), numérotée par `build/numeroter-essai.py` ; suite complète locale sur l'essai numéroté : 79 verts sur les 79 lancés, le 80e (`fiches_preparation`, coupé par la limite de temps de la suite) vert 2 fois sur 2 seul, sur la même page.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques entre elles et à la page testée, même empreinte), `entrees/essai.json`, `entrees/essai.source` (`f3de8d3`), `appli/essai/latest.json` ; stable, coquille et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `a7cec66..e3d3761`, sans forçage. Action « Publier les mises à jour » `43268821796` réussie (« versions.json signé : essai 5.2.24, stable 5.2.0 », `Ma-classe_5.2.24_x64-setup-essai.exe` signé ; stable `Ma-classe_5.2.0_x64-setup.exe` inchangé).

## 2026-11-12 — Essai 5.2.23 sur le canal d'essai (pages et application) : assistant, point du jour, pastille du robot et sonde

- **Autorisation :** Franck : « Je te donne mon accord, effectue les lots 0 et 1 » (audit de l'assistant) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `10771ee` (journal de l'essai 5.2.22, source `85f99f1`). Source : `Ma-classe` `essai` `96e875a` (5.2.22 + `claude/assistant-lots-0-1`), numérotée par `build/numeroter-essai.py` ; suite complète locale 79 sur 79 sur la branche de travail, « Tout est bon. » ; après numérotation, `mises_a_jour`, `chargement` et `assistant_sonde` verts.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, identiques), `entrees/essai.json`, `entrees/essai.source` (`96e875a`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `10771ee..02f98e3`, sans forçage. L'action « Publier les mises à jour » `43259542845` a échoué sans rien publier : GitHub n'a pas attribué de machine Windows (« The job was not acquired by Runner of type hosted even after multiple attempts »). Nouvelle exécution lancée à la main (`gh workflow run publier.yml`), `43262378946` réussie : « versions.json signé : essai 5.2.23, stable 5.2.0 », `Ma-classe_5.2.23_x64-setup-essai.exe` signé, déploiement `github-pages` réussi.

## 2026-11-12 — Essai 5.2.22 sur le canal d'essai (pages et application) : lecteur PDF, séances liées, Explorer, une seule page pour le remplaçant, calendrier 2027-2028

- **Autorisation :** Franck : « Finis avec le dernier lot » (lot D de l'audit d'ergonomie) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `1c6ff42` (journal des essais 5.2.20 et 5.2.21). Source : `Ma-classe` `essai` `85f99f1` (5.2.21 + cadrage + `claude/lot-d`), numérotée par `build/numeroter-essai.py` ; suite complète locale 77 sur 78, le 78e (`tableaux_traces`) corrigé dans le scénario seul et vert 2 fois sur 2 (page inchangée).
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages, **identiques** : depuis cette version, la classe et le remplaçant utilisent la même page ; le nom « Ma classe - Remplaçant.html » est gardé pour les mises à jour des anciennes copies du remplaçant, que ce nom fait démarrer en édition remplaçant), `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json`.
- **Livraison :** avance rapide de `main` `1c6ff42..3174442`, sans forçage. Action « Publier les mises à jour » `43235550605` réussie (« versions.json signé : essai 5.2.22, stable 5.2.0 », `Ma-classe_5.2.22_x64-setup-essai.exe` signé).

## 2026-11-12 — Essais 5.2.20 et 5.2.21 sur le canal d'essai (pages et application) : boutons et champs harmonisés, onglets de Préparer et des Résultats dans la barre de menus ; pastilles sans objet estompées

- **Autorisation :** Franck : « Fait le lot c » (lot C de l'audit d'ergonomie) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `c248ded` (essai 5.2.19, source `2d5f282`). Sources : `Ma-classe` `essai` `77c0256` (5.2.19 + `claude/lot-c-composants`), puis `daf8a5a` (correctif de la même branche), numérotées par `build/numeroter-essai.py` ; suite complète locale 77 sur 77 pour chacun.
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule), deux fois ; diff : `essai/` (deux pages, identiques aux pages testées), `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json`.
- **Livraison :** avances rapides de `main` `c248ded..58817a9` puis `..9516adb`, sans forçage. Actions « Publier les mises à jour » `43215310646` et `43220490730` réussies (« versions.json signé : essai 5.2.20, stable 5.2.0 », puis « essai 5.2.21 » ; `Ma-classe_5.2.20_x64-setup-essai.exe` et `Ma-classe_5.2.21_x64-setup-essai.exe` signés). La 5.2.20 rendait une case désactivée mais cochée comme une pastille allumée (Préparer › Cartes) : la 5.2.21 la corrige une demi-heure plus tard.

## 2026-11-12 — Essai 5.2.19 sur le canal d'essai (pages et application) : fenêtres plus lisibles, barre de menus et navigation plus faciles à viser

- **Autorisation :** Franck : « Fais le lot b » (lot B de l'audit d'ergonomie) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `96bc6b0` (essai 5.2.18, source `4ce8f46`). Source : `Ma-classe` `essai` `a0ac92d` (5.2.18 + documentation harmonisée + `claude/lot-b-verre`), numérotée par `build/numeroter-essai.py`, suite complète locale 76/76, « Tout est bon. ».
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`a0ac92d`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `96bc6b0..db6c04c`, sans forçage. Action « Publier les mises à jour » `43175996612` réussie (« versions.json signé : essai 5.2.19, stable 5.2.0 », « Ma-classe_5.2.19_x64-setup-essai.exe signé »). Site servi non relu directement.

## 2026-11-11 — Essai 5.2.18 sur le canal d'essai (pages et application) : Échap, raccourcis, robot qui ne cache plus rien, Rétablir dans Préparer

- **Autorisation :** Franck : « fais le lot a » (lot A de l'audit d'ergonomie) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `ba204a9` (essai 5.2.17, source `ab916bf` ; Store : Dizaines et unités en essai). Source : `Ma-classe` `essai` `4ce8f46` (5.2.17 + `claude/audit-ergonomie` + `claude/lot-a-ergonomie`), numérotée par `build/numeroter-essai.py`, suite complète locale 75/75, « Tout est bon. ».
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` (configuration d'exemple seule) ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`4ce8f46`), `appli/essai/latest.json` ; stable, coquille stable et catalogue des applis inchangés.
- **Livraison :** avance rapide de `main` `ba204a9..22da284`, sans forçage. Action « Publier les mises à jour » `43102115039` réussie (« versions.json signé : essai 5.2.18, stable 5.2.0 », « Ma-classe_5.2.18_x64-setup-essai.exe signé »). Site servi non relu directement.

## 2026-11-11 — Store : Dizaines et unités 1.0.0 sur le canal d'essai

- **Autorisation :** Franck : « Transforme la diapo en application de store pour Ma Classe pour travailler sur dizaines et unités » ; règle permanente du canal d'essai (publication en essai sans redemander). Stable non concerné.
- **Contrôle préalable :** `main` public à `93eeb93` (essai 5.2.17 de Ma classe publié par une autre conversation ; catalogue : Échecs, Essai du pont, EVAR 1.0.0 en essai ; pas d'entrée `dizaines-unites`). Source : `Applis-classe` `main` à `eaefed3` (poussé ; branche `claude/dizaines-unites`), 254 contrôles Chromium sans erreur (voir `JOURNAL.md` d'Applis-classe).
- **Préparation :** `python outils/publier.py dizaines-unites ../ma-classe-versions` (canal essai) : 4 fichiers, paquet `applis/paquets/dizaines-unites-1.0.0.zip` de 62 Ko, SHA-256 `0c90ac84…`, `source` `applis-classe@eaefed3`. Diff limité à `applis/entrees/dizaines-unites.json` et au paquet.
- **Livraison :** avance rapide de `main` `93eeb93..96835ab`, sans forçage. Action « Publier les mises à jour » `43086398988` réussie : « versions.json signé : essai 5.2.17, stable 5.2.0 », « applis.json signé : dizaines-unites 1.0.0 (essai), echecs 1.0.0 (essai), essai-pont 1.0.0 (essai), evar 1.0.0 (essai) » ; déploiement `github-pages` `7719444144` : `success`. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.17 sur le canal d'essai (pages et application) : style « verre »

- **Autorisation :** Franck, après la maquette : « Au top ! Plusieurs choses à ajouter […] » (enregistrement et écrou à côté de « Séances », dock des tableaux qui survole, assistant modernisé) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `a1e34b4` (essai 5.2.16, source `c1b0a42`). Source : `Ma-classe` `essai` `ab916bf` (essai 5.2.16 + `claude/verre-liquide-maquette`), numérotée par `build/numeroter-essai.py`, suite complète locale 74/74, « Tout est bon. ».
- **Préparation :** `publier-version.py --canal essai` (garde passée) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`ab916bf`), `appli/essai/latest.json` ; stable et coquille inchangés.
- **Livraison :** avance rapide de `main` `a1e34b4..93eeb93`, sans forçage. Action « Publier les mises à jour » `43085906861` réussie (« versions.json signé : essai 5.2.17, stable 5.2.0 », « Ma-classe_5.2.17_x64-setup-essai.exe signé »). Un envoi d'une autre intervention (`96835ab`, Store) a suivi : son déploiement, qui reprend ce contenu, était en cours à la rédaction. Site servi non relu directement (réseau de la session limité).

## 2026-11-11 — Essai 5.2.16 sur le canal d'essai (pages et application) : barre de menus en haut de l'écran ; les Échecs quittent les Tableaux

- **Autorisation :** Franck : « Je voudrais revoir l'ergonomie dans l'application Ma Classe, notamment en s'inspirant de la barre d'option de Mac […] », puis « Tu enlèveras les échecs des tableaux. La fonction a rejoint une appli dans le store. » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `b3a9537` (essai 5.2.15 de Ma classe, source `13db222`). Source : `Ma-classe` `essai` `c1b0a42` (essai 5.2.15 + `claude/barre-de-menus`), numérotée par `build/numeroter-essai.py`, suite complète locale 74/74, « Tout est bon. ».
- **Préparation :** `publier-version.py --canal essai` (garde passée : `essai` à jour et poussée, 5.2.15 publiée contenue) puis `publier-appli.py --canal essai` ; diff : `essai/` (deux pages), `entrees/essai.json`, `entrees/essai.source` (`c1b0a42`), `appli/essai/latest.json` ; stable et coquille inchangés.
- **Livraison :** avance rapide de `main` `b3a9537..7d0cc03`, sans forçage. Action « Publier les mises à jour » `43053235094` réussie (« essai · windows-x86_64 : Ma-classe_5.2.16_x64-setup-essai.exe signé » ; stable 5.2.0 inchangé) ; déploiement `github-pages` réussi (`7d0cc03`). Site servi non relu directement (réseau de la session limité).

## 2026-11-11 — Essai 5.2.15 sur le canal d'essai (pages et application) : Le jour et l'Accueil harmonisés avec la grille

- **Autorisation :** Franck : « Le jour n'a pas la même présentation/nomenclature que le reste. Idem pour le widget de l'accueil », puis, sur maquettes, « A · Liste harmonisée » et « Oui, comme la maquette » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `3b9ff19` (stable 5.2.0, essai 5.2.14 publié par la conversation de l'Accueil pendant notre suite de tests). Source : `Ma-classe` branche `essai` `13db222` (5.2.14 + harmonisation, réunion refaite sur la 5.2.14), suite complète locale 74/74, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.15` ; `publier-version.py --canal essai` (garde : `essai` poussée et à jour, numéro supérieur, commit de l'essai 5.2.14 `a0a2606` contenu) puis `publier-appli.py --canal essai` (configuration d'exemple seule ; aucun prénom de la classe). Diff : `essai/`, `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json` ; `stable/` inchangé ; coquille inchangée.
- **Livraison :** avance rapide de `main` `3b9ff19..c2bdb68`, sans forçage. Action « Publier les mises à jour » `43046123116` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.15_x64-setup-essai.exe`), « versions.json signé : essai 5.2.15, stable 5.2.0 ».

## 2026-11-11 — Essai 5.2.14 sur le canal d'essai (pages et application) : Accueil, les outils de la classe en widgets

- **Autorisation :** Franck : « Prends connaissance de la dernière version et ajoute le lot 2 » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `619e9f5` (essai 5.2.13 de Ma classe ; Échecs 1.0.0 publiée en essai dans le Store juste avant, par une autre conversation). Source : `Ma-classe` `essai` `a0a2606` (essai 5.2.13 + `claude/accueil-widgets-lot2`), numérotée par `build/numeroter-essai.py`, suite complète locale 73/73, « Tout est bon. ».
- **Préparation :** `publier-version.py --canal essai` (garde passée : `essai` à jour et poussée, 5.2.13 publiée contenue) puis `publier-appli.py --canal essai` ; diff : `essai/`, `entrees/essai.json`, `entrees/essai.source` (`a0a2606`), `appli/essai/latest.json` ; stable et coquille inchangés.
- **Livraison :** avance rapide de `main` `619e9f5..114b78e`, sans forçage. Action « Publier les mises à jour » `43040494823` réussie (installateur `Ma-classe_5.2.14_x64-setup-essai.exe`, 3 007 Ko ; « versions.json signé : essai 5.2.14, stable 5.2.0 ») ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session limité).

## 2026-11-11 — Store : Échecs 1.0.0 sur le canal d'essai

- **Autorisation :** Franck : « Prends le tableau "échecs" et mets en en appli pour le dépot » ; règle permanente du canal d'essai (publication en essai sans redemander). Stable non concerné.
- **Contrôle préalable :** `main` public à `54ade0e` (stable 5.2.0, essai 5.2.13 ; catalogue : « Essai du pont » et EVAR 1.0.0 en essai, pas d'entrée `echecs`). Source : `Applis-classe` `main` à `d048cb8` (poussé ; branche `claude/echecs`), contrôles Chromium sans erreur (voir `JOURNAL.md` d'Applis-classe).
- **Préparation :** `python outils/publier.py echecs ../ma-classe-versions` (canal essai) : 4 fichiers, paquet `applis/paquets/echecs-1.0.0.zip` de 64 Ko, SHA-256 `5a5caf4c…`, `source` `applis-classe@d048cb8`. Diff limité à `applis/entrees/echecs.json` et au paquet.
- **Livraison :** avance rapide de `main` `54ade0e..61eadfe`, sans forçage. Action « Publier les mises à jour » `43037303067` réussie : « versions.json signé : essai 5.2.13, stable 5.2.0 », « applis.json signé : echecs 1.0.0 (essai), essai-pont 1.0.0 (essai), evar 1.0.0 (essai) » ; déploiement `github-pages` `7712519135` : `success`. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.13 sur le canal d'essai (pages et application) : emploi du temps, horaires officiels à la demande, impression, semaines A et B en option

- **Autorisation :** Franck : « Fais les vérifications horaires en fonction des niveaux, mais (D4) n'affiche l'écart horaire qu'à la demande. L'alternance semaines A/B doit être une option (désactivée par défaut). » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `3bc67e0` (stable 5.2.0, essai 5.2.12 ; EVAR 1.0.0 publiée en essai par une autre conversation, sans rapport). Source : `Ma-classe` branche `essai` `f3b88df` (5.2.12 + documentation du Store + lot 6 de l'emploi du temps), suite complète locale 73/73, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.13` ; `publier-version.py --canal essai` (garde : branche `essai` poussée et à jour, numéro supérieur, commit de l'essai 5.2.12 contenu) puis `publier-appli.py --canal essai` (configuration d'exemple seule ; aucun prénom de la classe dans les pages). Diff : `essai/`, `entrees/essai.json`, `entrees/essai.source`, `appli/essai/latest.json` ; `stable/` et `entrees/stable.json` inchangés ; coquille inchangée.
- **Livraison :** avance rapide de `main` `3bc67e0..6ae1c4e`, sans forçage. Action « Publier les mises à jour » `43031003028` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.13_x64-setup-essai.exe`, 3 003 Ko), « versions.json signé : essai 5.2.13, stable 5.2.0 ».

## 2026-11-11 — Store : EVAR 1.0.0 sur le canal d'essai

- **Autorisation :** Franck : « Publie dans le store » (appli EVAR, vie affective et relationnelle) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `e2bbbed` ; catalogue : « Essai du pont » 1.0.0 (essai) seule, pas d'entrée `evar`. Source : `Applis-classe` `main` à `becb103` (poussé ; branche `claude/evar`), contrôles Chromium sans erreur (voir `JOURNAL.md` d'Applis-classe).
- **Préparation :** branche `claude/store-evar` ; `python outils/publier.py evar ../ma-classe-versions` (canal essai) : 108 fichiers, paquet `applis/paquets/evar-1.0.0.zip` de 9 274 Ko, SHA-256 `da5fb7f2…`, `source` `applis-classe@becb103`. Diff limité à `applis/entrees/evar.json` et au paquet.
- **Livraison :** avance rapide de `main` `e2bbbed..5b34962`, sans forçage. Action « Publier les mises à jour » `43026110003` réussie : « versions.json signé : essai 5.2.12, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai), evar 1.0.0 (essai) » ; déploiement `github-pages` `7710879479` : `success`. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Sources des applis du Store : dépôt privé `Applis-classe` (documentation)

- **Demande :** Franck a créé le dépôt privé `Harry-Safe/Applis-classe` pour ses applis (« Paramètre-le ») ; ce dépôt-ci reste la vitrine publique du Store.
- **Réalisation :** `DOCUMENTATION.md` : `applis/entrees/<id>.json` est écrit par `outils/publier.py` d'`Applis-classe` (référence, avec garde ; les entrées notent désormais le commit source dans `source`, champ ignoré par Ma classe). Aucune publication : catalogue inchangé (« Essai du pont » 1.0.0, paquet identique à celui fabriqué depuis `Applis-classe`).
- **Livraison :** commit de documentation sur `main` (`[skip ci]`, rien à signer).

## 2026-11-11 — Essai 5.2.12 sur le canal d'essai (pages et application) : périodes terminées modifiables ; tout le travail réuni

- **Autorisation :** Franck : « tout ce qui a été fait ou enregistré dans l'appli doit pouvoir être modifié » et « Harmonise » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `da0731e` (stable 5.2.0, essai 5.2.11 publié par la conversation de l'Accueil). Source : `Ma-classe` `claude/essai-harmonise-5.2.11` (5.2.11 publiée + périodes terminées modifiables + entrées de journal d'autres branches), suite complète locale 72/72, « Tout est bon. ». La 5.2.11 publiée est contenue dans cette version : rien de publié n'est perdu.
- **Préparation :** branche `claude/essai-5.2.12` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule ; aucun prénom de la classe dans les pages). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/stable/` inchangés.
- **Livraison :** avance rapide de `main` `da0731e..b794090`, sans forçage. Action « Publier les mises à jour » `43015373582` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.12_x64-setup-essai.exe`, 2 994 Ko), « versions.json signé : essai 5.2.12, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.11 sur le canal d'essai (pages et application) : l'Accueil à widgets, plus de barre du bas

- **Autorisation :** Franck : « Je partage ta vision des widgets, prépare un essai » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `b3a3df6` (stable 5.2.0, essai 5.2.10 publié à 12 h 04 par une autre session) ; aucune autre publication depuis. Source : `Ma-classe` `claude/appli-essai-accueil` `ad057d3` (essai 5.2.10 + Accueil à widgets `claude/accueil-widgets`), suite complète locale 72/72, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.11` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule, listes d'élèves vides). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/latest.json` inchangés ; coquille inchangée.
- **Livraison :** avance rapide de `main` `b3a3df6..fc76910`, sans forçage. Action « Publier les mises à jour » `43012500127` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.11_x64-setup-essai.exe`, 2 992 Ko), « versions.json signé : essai 5.2.11, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session limité).

## 2026-11-11 — Essai 5.2.10 sur le canal d'essai (pages et application) : emploi du temps, périodes particulières (lot 5)

- **Autorisation :** Franck : « Pour D3 : de base un emploi du temps pour l'année avec des périodes particulières. » ; travail en autonomie jusqu'au résultat final ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `689bb44` (stable 5.2.0, essai 5.2.9) ; aucune autre publication depuis. Source : `Ma-classe` `claude/appli-essai-edt6` `4105e09` (essai 5.2.9 + lot 5), suite complète locale 71/71, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.10` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule ; aucun prénom de la classe dans les pages). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/stable/` inchangés. Numéro 5.2.10 : comparaisons de versions numériques (gestionnaire de mises à jour, programme d'installation).
- **Livraison :** avance rapide de `main` `689bb44..47094f0`, sans forçage. Action « Publier les mises à jour » `43008900660` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.10_x64-setup-essai.exe`, 2 984 Ko), « versions.json signé : essai 5.2.10, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.9 sur le canal d'essai (pages et application) : emploi du temps, la grille seule

- **Autorisation :** Franck, après l'essai 5.2.8 : « On ne garde que la vue grille qui est plus moderne. » ; travail en autonomie jusqu'au résultat final ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `3499d65` (stable 5.2.0, essai 5.2.8) ; aucune autre publication depuis. Source : `Ma-classe` `claude/appli-essai-edt5` `9256a01` (essai 5.2.8 + la grille seule), suite complète locale 70/70, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.9` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule ; aucun prénom de la classe dans les pages). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/stable/` inchangés.
- **Livraison :** avance rapide de `main` `3499d65..0003110`, sans forçage. Action « Publier les mises à jour » `43004662228` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.9_x64-setup-essai.exe`, 2 981 Ko), « versions.json signé : essai 5.2.9, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.8 sur le canal d'essai (pages et application) : emploi du temps en grille horaire (lot 4)

- **Autorisation :** Franck : « Fais le lot 4 », puis maquette validée (« Oui, on code ») et décision D2 (bascule, grille par défaut) ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `c911a4d` (stable 5.2.0, essai 5.2.7) ; aucune autre publication depuis. Source : `Ma-classe` `claude/appli-essai-edt4` (essai 5.2.7 + lot 4), suite complète locale 70/70, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.8` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/stable/` inchangés.
- **Livraison :** avance rapide de `main` `c911a4d..89514e9`, sans forçage. Action « Publier les mises à jour » `42993828520` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.8_x64-setup-essai.exe`, 2 982 Ko), « versions.json signé : essai 5.2.8, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session).

## 2026-11-11 — Essai 5.2.7 sur le canal d'essai (pages et application) : emploi du temps, Excel à la demande (lot 3)

- **Autorisation :** règle permanente du canal d'essai ; Franck a laissé la session travailler seule (« Je vais devoir te laisser travailler seul et ne pourrais être là que pour le résultat final »). Stable non concerné.
- **Contrôle préalable :** `main` public à `cc652a1` (stable 5.2.0, essai 5.2.6) ; aucune autre publication depuis. Source : `Ma-classe` `claude/appli-essai-edt3` `8ffce05` (essai 5.2.6 + lot 3), suite complète locale 69/69, « Tout est bon. ».
- **Préparation :** branche `claude/essai-5.2.7` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/stable/` inchangés.
- **Livraison :** avance rapide de `main` `cc652a1..6c8ee95`, sans forçage. Action « Publier les mises à jour » `42923952712` réussie : installateur d'essai fabriqué ici (`Ma-classe_5.2.7_x64-setup-essai.exe`, 2 971 Ko), « versions.json signé : essai 5.2.7, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` réussi. Site servi non relu directement (réseau de la session).

## 2026-11-10 — Essai 5.2.6 sur le canal d'essai (pages et application) : emploi du temps réorganisé (lot 2)

- **Autorisation :** Franck : « Fais le lot 2 » ; règle permanente du canal d'essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `c2ca859` (stable 5.2.0, essai 5.2.5 du Store des applis, publié à 22 h 33 par une autre session : publication attendue jusqu'à son journal) ; la publication stable 5.2.4 annoncée par le `main` source `70fc2a8` n'y est toujours pas. Source : `Ma-classe` `claude/appli-essai-edt2` `0395776` (5.2.6 = essai 5.2.5 + lot 2 `claude/edt-lot2-structure`), suite complète locale 68/68.
- **Préparation :** branche `claude/essai-5.2.6` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule, listes d'élèves vides vérifiées). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; `stable/`, `entrees/stable.json`, `appli/latest.json` et `applis/` intacts (catalogue du Store inchangé).
- **Livraison :** avance rapide de `main` `c2ca859..e0505b3`, sans forçage. Action « Publier les mises à jour » `42909955594` réussie : installateur d'essai **fabriqué ici** (`Ma-classe_5.2.6_x64-setup-essai.exe`, 2 965 Ko), « versions.json signé : essai 5.2.6, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) » ; déploiement `github-pages` de `e0505b3`. Site servi non relu directement. **Publié sur le canal d'essai, pages et application Windows.**

## 2026-11-10 — Essai 5.2.5 sur le canal d'essai (pages et application) et Store des applis

- **Autorisation :** Franck : « Développe ce store » ; règle permanente du canal d'essai. Le Store est public pour commencer (question du chiffrement restée ouverte).
- **Contrôle préalable :** `main` public à `6d42db9` (stable 5.2.0, essai 5.2.4 ; la publication stable 5.2.4 annoncée par le `main` source `70fc2a8` n'y est pas encore) ; aucune PR ouverte. Source : `Ma-classe` `claude/store-applis` `22fc678` (5.2.5 = 5.2.4 + Store), suite complète locale 68/68.
- **Préparation :** branche `claude/store-applis` ; `outils/signer.py` assemble et signe aussi `applis.json` (catalogue du Store, même clé, `type:"applis"`) à partir de `applis/entrees/*.json` et ne met en ligne que les paquets annoncés ; essayé avec une clé jetable. `publier-version.py` et `publier-appli.py --canal essai` (configuration d'exemple seule), puis `publier-applis.py exemples/applis/essai-pont --canal essai` : `applis/entrees/essai-pont.json`, `applis/paquets/essai-pont-1.0.0.zip`. Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json`, `applis/`, `outils/signer.py`, `publier.yml` (commentaire et nom d'étape), `DOCUMENTATION.md` ; stable intact.
- **Premier envoi :** `main` `6d42db9..dc38bde` ; action `42906262601` en échec à « Signer versions.json et applis.json » : « fichier absent applis/paquets/essai-pont-1.0.0.zip » — le paquet n'avait pas été commité, la règle `paquets/` de `.gitignore` (dossier de fabrication) l'ignorait aussi dans `applis/`. Rien de déployé : le site est resté sur le déploiement précédent (stable 5.2.0, essai 5.2.4). Correction : règles de `.gitignore` limitées à la racine (`/construction/`, `/paquet/`, `/paquets/`), paquet ajouté.
- **Livraison :** avance rapide de `main` `dc38bde..8186d78`, sans forçage. Action « Publier les mises à jour » `42907049738` réussie : « versions.json signé : essai 5.2.5, stable 5.2.0 », « applis.json signé : essai-pont 1.0.0 (essai) », « Ma-classe_5.2.5_x64-setup-essai.exe signé » (installateur fabriqué ici à l'exécution précédente, repris du cache) ; déploiement `github-pages` de `8186d78` réussi. Site servi non relu directement (hors de portée de cet environnement). **Publié sur le canal d'essai (pages, application, Store)** ; stable intact.

## 2026-11-10 — Essai 5.2.4 sur le canal d'essai (pages et application) : ↶ ↷ et corbeille rouge sur tous les tableaux

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; demande du jour : « je veux les boutons retour et l'autre sur tous les tableaux avec un icone corbeille rouge pour tout supprimer (sans message de confirmation). Enlève également les boutons "tout supprimer" de tous les tableaux ». Stable non concerné (reste en 5.2.0).
- **Contrôle préalable :** `main` public à `9c9b6f3` (stable 5.2.0, essai 5.2.3) ; aucune PR ouverte. Source : `Ma-classe` `claude/tableaux-selection-instruments` `62113c8` (5.2.4 = 5.2.3 + ↶ ↷ et corbeille), suite complète locale 67/67 ; `main` source inchangé à `163717e`.
- **Préparation :** branche `claude/essai-5.2.4` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; stable intact.
- **Livraison :** avance rapide de `main` `9c9b6f3..6783d2c`, sans forçage. Action « Publier les mises à jour » `42895071494` réussie : installateur d'essai **fabriqué ici** (`Ma-classe_5.2.4_x64-setup-essai.exe`, 2 959 Ko), « versions.json signé : essai 5.2.4, stable 5.2.0 » ; déploiement `github-pages` `7693417527` de `6783d2c` réussi. Site servi non relu directement. **Publié sur le canal d'essai, pages et application Windows.**

## 2026-11-10 — Essai 5.2.3 sur le canal d'essai (pages et application) : plus de messages en bandeau noir

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; demande du jour : « Je ne veux plus de ces messages […] tous ces messages qui apparaissent dans des bandeaux noirs ». Stable non concerné (reste en 5.2.0).
- **Contrôle préalable :** `main` public à `9b763b4` (stable 5.2.0, essai 5.2.2) ; aucune PR. Source : `Ma-classe` `claude/tableaux-selection-instruments` `3befc6d` (5.2.3 = 5.2.2 + messages), suite complète locale 67/67 ; `main` source inchangé à `163717e`.
- **Préparation :** branche `claude/essai-5.2.3` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; stable intact.
- **Livraison :** avance rapide de `main` `9b763b4..25a1bfb`, sans forçage. Action « Publier les mises à jour » `42877496409` réussie : installateur d'essai **fabriqué ici** (`Ma-classe_5.2.3_x64-setup-essai.exe`, 2 957 Ko), « versions.json signé : essai 5.2.3, stable 5.2.0 » ; déploiement `github-pages` `7691034657` de `25a1bfb` réussi. Site servi non relu directement. **Publié sur le canal d'essai, pages et application Windows.**

## 2026-11-10 — Essai 5.2.2 sur le canal d'essai (pages et application) : tableaux, sélection sans outil, instruments, bulles et flèches

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; demande du jour sur les tableaux (Géométrie : instruments toujours saisissables, palettes de longueur et d'écartement, Crayon unique, zoom ; Numération, Tableau blanc et Géométrie : sélection sans outil ; Tableau blanc : bulles lignées en fenêtres, flèches à la Word ; tutoriels). Stable non concerné (reste en 5.2.0).
- **Contrôle préalable :** `main` public à `2b49a1d` (stable 5.2.0, essai 5.2.1) ; aucune PR. Source : `Ma-classe` `claude/tableaux-selection-instruments` `90e8cb6` (5.2.2 = 5.2.1 + tableaux) ; `main` source inchangé à `163717e`.
- **Préparation :** branche `claude/essai-5.2.2` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule, aucun prénom dans `essai/`). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; coquille inchangée ; stable intact.
- **Livraison :** avance rapide de `main` `2b49a1d..5032c51`, sans forçage. Action « Publier les mises à jour » `42863390524` réussie : installateur d'essai **fabriqué ici** (`Ma-classe_5.2.2_x64-setup-essai.exe`, 2 956 Ko), « versions.json signé : essai 5.2.2, stable 5.2.0 » ; déploiement `github-pages` `7689077342` de `5032c51` réussi. Site servi non relu directement. **Publié sur le canal d'essai, pages et application Windows.**

## 2026-11-10 — Essai 5.2.1 sur le canal d'essai (pages et application) : Numération, formes du paquet et nouvelles représentations

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; demande du jour sur la Numération (formes de « Faire un paquet », bouton « Formes et couleurs », nouvelles représentations). Stable non concerné (reste en 5.2.0).
- **Contrôle préalable :** `main` public à `02b0ca5` (stable et essai 5.2.0) ; aucune PR. Source : `Ma-classe` `claude/numeration-formes-representations` `cea7e83` (5.2.1 = 5.2.0 + Numération), suite complète locale 67/67 ; `main` source inchangé à `163717e`.
- **Préparation :** branche `claude/essai-5.2.1` ; `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (configuration d'exemple seule, aucun prénom dans `essai/`). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` ; stable intact.
- **Livraison :** avance rapide de `main` `02b0ca5..f10df8f`, sans forçage. Action « Publier les mises à jour » `42833187033` réussie : installateur d'essai **fabriqué ici** (`Ma-classe_5.2.1_x64-setup-essai.exe`, 2 947 Ko), « versions.json signé : essai 5.2.1, stable 5.2.0 », installateurs signés ; déploiement `github-pages` `7684681673` de `f10df8f` réussi. Site servi non relu directement. **Publié sur le canal d'essai, pages et application Windows.**

## 2026-11-10 — Publication stable 5.2.0 (et essai 5.2.0), application Windows fabriquée ici

- **Autorisation :** Franck : « Push sur main quand t'as fini (j'ai ajouter des crédits actions sur Github au besoin) », puis, à la question sur la publication stable : « Main et stable 5.2.0 ».
- **Contrôle préalable :** `main` public à `43e6740` (stable 5.1.0, essai 5.1.5) ; aucune PR. Source : `Ma-classe` `main` `87036b1` (5.2.0 = essais 5.1.1 à 5.1.6), « Validation de Ma classe » `42817799496` **réussie** sur ce commit (67 scénarios, « Tout est bon. »), « Documentation de Ma classe » `42817799570` réussie.
- **Préparation :** branche `claude/stable-5.2.0` ; `publier-version.py` puis `publier-appli.py` pour le canal stable, puis les deux avec `--canal essai` (pages construites avec la configuration d’exemple seule, aucun prénom dans `stable/` ni `essai/`). Diff : `stable/`, `essai/`, `entrees/stable.json`, `entrees/essai.json`, `appli/latest.json`, `appli/essai/latest.json`, nouvelle `coquille/stable/` ; ancien installateur stable 5.1.0 retiré par le script.
- **Livraison :** avance rapide de `main` `43e6740..ae847ff`, sans forçage. Action « Publier les mises à jour » `42821224978` réussie : installateurs **fabriqués ici** — essai `Ma-classe_5.2.0_x64-setup-essai.exe` (2 945 Ko) et stable `Ma-classe_5.2.0_x64-setup.exe` (2 945 Ko) ; « versions.json signé : essai 5.2.0, stable 5.2.0 » ; les deux installateurs signés ; déploiement `github-pages` `7682972868` de `ae847ff` à l’état `success`. Site servi non relu directement (adresse hors de portée de cet environnement). **Publié : stable et essai en 5.2.0, pages et application Windows.**

## 2026-11-10 — Fabrication par ce dépôt passée sur `main`, et essai 5.1.5 (pages et application Windows) : lot A, recherche et assistant

- **Autorisation :** Franck : « Oui, option 2 puis 5.1.4 en essai » (fabrication de l’application par ce dépôt sur `main`, puis publication de l’essai ; le numéro est devenu 5.1.5 car 5.1.4 venait d’être publié pour les pages). Règle permanente du canal d’essai. Stable non concerné.
- **Contrôle préalable :** `main` public à `b879ddb` (stable 5.1.0, essai 5.1.4 pages, application d’essai 5.1.3) ; branche `claude/fabrication-publique` `87ce819` partie de `35edc86`, donc plus en avance rapide : réunie à `main` sur `claude/essai-5.1.5` (conflit seulement dans ce journal, les deux entrées gardées). Aucune PR. Source : `Ma-classe` `claude/lot-a-recherche` `739d978` = essai 5.1.3 + fabrication publique + essai 5.1.4 (lot 1 de l’emploi du temps) + lot A, version 5.1.5 ; `main` source inchangé à `40148d4`.
- **Préparation :** `publier-version.py --canal essai` puis `publier-appli.py --canal essai` (nouveau script du 9 novembre), pages construites avec la configuration d’exemple seule (aucun prénom dans `essai/`). Diff : `essai/`, `entrees/essai.json`, `appli/essai/latest.json` (5.1.5) ; coquille `coquille/essai/` identique à celle de la fusion ; `stable/`, `entrees/stable.json`, `appli/latest.json` et l’installateur 5.1.0 intacts.
- **Livraison :** avance rapide de `main` `b879ddb..ed49822`, sans forçage. Action « Publier les mises à jour » `42809981245` réussie : « Application Windows (essai) » **fabriquée ici** (`ma-classe v5.1.5`, `Ma-classe_5.1.5_x64-setup-essai.exe`, 2 943 Ko, 6 min 13 s) ; stable « déjà dans le dépôt » (20 s) ; « versions.json signé : essai 5.1.5, stable 5.1.0 », installateurs signés (stable 5.1.0, essai 5.1.5) ; déploiement `github-pages` `7681288007` de `ed49822` à l’état `success`. Site servi non relu directement (adresse hors de portée de cet environnement). **Publié sur le canal d’essai, pages et application Windows.**
- **Suite :** les publications d’essai suivantes passent par ce chemin ; une publication stable fabriquera aussi son installateur ici. Syllamons et Vocabulaire ont encore l’ancien schéma.

## 2026-11-10 — Essai 5.1.4 sur le canal d'essai (pages) : emploi du temps plus sûr

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; Franck : « Lance le premier lot » (lot 1 du plan de l'emploi du temps). Stable non concerné.
- **Contrôle préalable :** `main` public à `35edc86` (stable 5.1.0, essai 5.1.3) ; branches distantes relues, aucune PR. Source : `claude/appli-essai-edt` = essai 5.1.3 + lot 1 (`claude/edt-lot1-fiabilite`), version 5.1.4 ; `main` source inchangé à `40148d4`.
- **Préparation :** branche `claude/essai-5.1.4` ; `publier-version.py --canal essai` seulement (pages construites avec la configuration d'exemple, listes d'élèves vides vérifiées). Diff limité à `essai/` et `entrees/essai.json` ; `stable/`, `entrees/stable.json` et `appli/` intacts.
- **Validation source :** suite complète locale 66/67, `applis` (fermeture animée) réussi deux fois à la relance isolée ; documentation cohérente.
- **Livraison :** avance rapide de `main` `35edc86..fd99120`, sans forçage. Action « Publier les mises à jour » `42801886243` réussie : « versions.json signé : essai 5.1.4, stable 5.1.0 » ; installateurs inchangés re-signés (stable 5.1.0, essai 5.1.3) ; déploiement `github-pages` de `fd99120`. Site servi non relu directement. **Publié sur le canal d'essai pour les pages** ; l'application Windows d'essai reste en 5.1.3 (fabrication en attente de la décision de Franck sur `claude/fabrication-publique`).

## 2026-11-09 — Fabrication de l'application Windows par ce dépôt (branche `claude/fabrication-publique`)

- **Demande / Autorisation :** quota de minutes GitHub du dépôt privé épuisé ; Franck choisit de faire fabriquer l'installateur par ce dépôt public : « Mets l'option 2 en route » (mise en place sur des branches d'essai). **Rien n'est publié** : `main` attend sa phrase explicite.
- **Contrôle préalable :** `main` public à `35edc86` (stable 5.1.0, essai 5.1.3) ; branches distantes `claude/documentation`, `claude/essai-5.1.1` à `5.1.3`, `codex/publication-5.1`, `essai-presentation`, toutes antérieures ; aucune PR. Source : `main` privé `40148d4`, essai `claude/appli-essai-tutoriels` `bd2ede0` (coquille de l'essai).
- **Réalisation :** `outils/fabriquer-appli.py` (plan, préparation, compilation, rangement) ; action « Publier les mises à jour » : un travail Windows par canal qui fabrique l'installateur à partir de `coquille/<canal>/` et de la page publiée du canal (empreinte et version contrôlées), le garde en cache tant que rien ne change, puis le travail de publication le range dans `_site/appli/`, le signe et publie comme avant ; installateur encore présent dans le dépôt pris tel quel (ancien fonctionnement, ici le stable 5.1.0). Branches `claude/fabrication-*` : fabrication et contrôle du rangement, sans signature ni publication. `.gitattributes` (`* -text`) : sans lui, la machine Windows convertissait les fins de ligne de la page et son empreinte ne correspondait plus (premier essai refusé à juste titre). Essai 5.1.3 repassé par le nouveau chemin (`publier-appli.py` du 9 novembre lancé depuis la branche d'essai source) : `coquille/essai/` (16 fichiers, dont `src/applis/pont-applis.js` intégré par `lib.rs`), `appli/essai/latest.json`, installateur 5.1.3 retiré du dépôt. Documentation (`DOCUMENTATION.md` § 1, 3, 3 bis, 4), `README.md`, `.gitignore`.
- **Validation :** action `42697621362` sur `a9cd904` : stable « déjà dans le dépôt » (16 s) ; essai **fabriqué** (compilation 4 min 29 s, `Ma-classe_5.1.3_x64-setup-essai.exe`, 3 008 667 octets contre 3 007 266 pour celui du dépôt privé) ; rangement contrôlé (`_site/appli/essai : 5.1.3 -> …`). Actions précédentes `42696497778` (empreinte refusée, fins de ligne) et `42696858769` (fichier intégré absent de la coquille) en échec, corrigées. Signature non essayée sur branche (secrets et environnement Pages réservés à `main`).
- **Livraison / état :** poussé sur `claude/fabrication-publique` seulement. Au passage sur `main` (autorisation de Franck requise) : l'essai 5.1.3 sera reconstruit par l'action, signé et republié à l'identique (même version, aucun poste n'est relancé) ; stable inchangé jusqu'à la prochaine publication stable.

## 2026-11-09 — Essai 5.1.3 sur le canal d'essai : des tutoriels qui montrent ce qu'ils décrivent

- **Autorisation :** règle permanente de Franck pour le canal d'essai ; revue des tutoriels demandée par Franck (« vérifie les tutos pour que les pages mentionnées s'affichent et correspondent bien aux actions possibles »). Stable non concerné.
- **Contrôle préalable :** `main` public à `8fb1507` (stable 5.1.0, essai 5.1.2) ; aucune PR. Source : `claude/appli-essai-tutoriels` `9a32b69` = essai 5.1.2 + revue des tutoriels (`claude/tutoriels-fiables` `f30a6fe`), version 5.1.3 ; `main` source inchangé à `40148d4`.
- **Préparation :** branche `claude/essai-5.1.3` ; `publier-version.py --canal essai` (configuration d'exemple seule, listes d'élèves vides vérifiées) et `publier-appli.py --canal essai` (installateur 5.1.3 de `appli-paquets-essai`, action « Application Windows » `42634116629` réussie, blob `488256b9b536b77f7c5a07c2bc39a13250f771f7`). Diff limité à `essai/`, `entrees/essai.json`, `appli/essai/` ; installateur 5.1.2 retiré par le script ; stable intact.
- **Validation source :** suite complète locale 66/66 « Tout est bon. » ; « Documentation de Ma classe » `42634116686` réussie ; « Validation de Ma classe » `42634116490` : premier passage en échec sur `assistant_bulle` (« page redimensionnée », échec intermittent connu), **réussie à la relance**.
- **Livraison :** avance rapide de `main` `8fb1507..95eb48f`, sans forçage. Action « Publier les mises à jour » `42642374884` réussie : « versions.json signé : essai 5.1.3, stable 5.1.0 », « Ma-classe_5.1.3_x64-setup-essai.exe signé » ; déploiement `github-pages` de `95eb48f` à l'état `success`. Site servi non relu directement (hors de portée de cet environnement). **Publié sur le canal d'essai, pages et application Windows** ; stable inchangé.

## 2026-11-09 — Essai 5.1.2 sur le canal d'essai : tutoriels fiables (phase 0 de l'assistant)

- **Autorisation :** règle permanente de Franck pour le canal d'essai (« Fais le toujours à l'avenir », 8 novembre) ; Franck valide la phase 0 de l'assistant : « Oui faisons cela ». Stable non concerné.
- **Contrôle préalable :** `main` public à `0d2e354` (stable 5.1.0, essai 5.1.1) ; seule branche distante `main` ; aucune PR. Source : branche de réunion `claude/appli-essai-tutoriels` `ee1f036` = essai 5.1.1 (`claude/appli-applis`) + phase 0 (`claude/tutoriels-fiables` `df02932`), version 5.1.2 ; `main` source inchangé à `40148d4`.
- **Préparation :** branche `claude/essai-5.1.2` ; `publier-version.py --canal essai` (pages construites avec la seule configuration d'exemple, listes d'élèves vides vérifiées) et `publier-appli.py --canal essai` (installateur 5.1.2 de `appli-paquets-essai` `36270fe`, action « Application Windows » `42612118367` réussie, blob `f122553dc3cc2be6c549ca377be1480562c6a071`). Diff limité à `essai/`, `entrees/essai.json`, `appli/essai/` : canal stable intact ; installateur 5.1.1 retiré par le script.
- **Validation source :** suite complète 66/66 « Tout est bon. » en local ; « Validation de Ma classe » `42612118373` et « Documentation de Ma classe » `42612118297` réussies sur `ee1f036`.
- **Livraison :** avance rapide de `main` `0d2e354..17b7941`, sans forçage. Action « Publier les mises à jour » `42615187660` réussie : journal « versions.json signé : essai 5.1.2, stable 5.1.0 », « Ma-classe_5.1.2_x64-setup-essai.exe signé » ; déploiement `github-pages` de `17b7941` à l'état `success`. Fichiers en ligne non relus directement (site hors de portée de cet environnement). **Publié sur le canal d'essai, pages et application Windows** ; stable inchangé.

## 2026-11-08 — Formulation de l’aide de l’IA sur la page de présentation

- **Autorisation :** Franck : « Ne touche pas au A propos dans l'application. La nouvelle formulation devra être simplement présente sur la page de présentation de l'appli. Vérifie le dépot puis publie dessus ».
- **Contrôle préalable :** `main` public à `82c1d6c` (stable 5.1.0, essai 5.1.1) ; branches distantes relues (`claude/documentation`, `claude/essai-5.1.1`, `codex/publication-5.1`, toutes contenues dans main ou plus anciennes) ; aucune PR. Travaux locaux non partagés de l’autre intervenant (ancienne branche `codex/mentions-ia`) non observables, non touchés. Source `main` `f7840dc` inchangé.
- **Réalisation :** phrase de présentation remplacée dans `index.html` (page publique, rédigée à la main selon `DOCUMENTATION.md`) et `README.md` ; règle 8 de `DOCUMENTATION.md` précisée. Aucune page d’édition, fiche, ZIP ni installateur touché ; canaux stable et essai inchangés.
- **Validation :** diff limité à `index.html`, `README.md`, `DOCUMENTATION.md` et ce journal ; `git diff --check` propre ; page relue en HTML.
- **Livraison :** avance rapide de `main` `82c1d6c..519e8a3`, sans forçage. Action « Publier les mises à jour » `42511258825` réussie (déploiement GitHub Pages). Page en ligne non relue directement (site hors de portée de cet environnement). **Publié** ; canaux stable 5.1.0 et essai 5.1.1 inchangés.

## 2026-11-08 — Essai 5.1.1 sur le canal d'essai : panneau Applis

- **Autorisation :** Franck : « Mets le en essai pour le gestionnaire. C'est le principe même d'avoir une fonction d'essai. Fais le toujours à l'avenir » (règle permanente pour le seul canal d'essai, consignée dans `AGENTS.md` du dépôt source).
- **Contrôle préalable :** `main` public à `ed52b44` (stable 5.1.0, essai 5.0.4) ; source `claude/appli-applis` à `2314977` (version 5.1.1, suite 66/66), `main` source inchangé à `f7840dc`.
- **Préparation :** branche `claude/essai-5.1.1` ; `publier-version.py --canal essai` (pages construites avec la configuration d'exemple) et `publier-appli.py --canal essai` (installateur 5.1.1 de `appli-paquets-essai`, action « Application Windows » `42495332745`). Diff limité à `essai/`, `entrees/essai.json`, `appli/essai/` : canal stable intact ; ancien installateur 5.0.4 retiré par le script.
- **Livraison :** avance rapide de `main` `ed52b44..658975e`, sans forçage. Action « Publier les mises à jour » `42497035088` réussie : journal « versions.json signé : essai 5.1.1, stable 5.1.0 », « Ma-classe_5.1.1_x64-setup-essai.exe signé », déploiement GitHub Pages. Fichiers en ligne non relus directement (site hors de portée de cet environnement). **Publié sur le canal d'essai, pages et application Windows** ; stable inchangé.

## 2026-11-08 — Publication stable 5.1.0

- **Autorisation :** Franck demande le passage sur main puis confirme la fin du lot de l’autre conversation et donne la main pour la réunion et la publication proposées. Distribution stable des pages et de l’application Windows après validation des deux lots. Aucun changement prévu du canal d’essai.
- **Contrôle préalable :** main public GitHub et local `0accc7a`, stable 5.0.2, essai 5.0.4. Nouveau travail isolé sur `codex/publication-5.1` depuis main ; espace principal de distribution sur `codex/mentions-ia` à `92ed69d`, avec journal non enregistré, préservé. Documentation, consignes et présentation générale préparées dans ce lot repris ici, sans ses anciens paquets 5.0.5/5.0.6 ni modification des fichiers d’essai. Historique et crédits tiers conservés.
- **Source :** main source à `be2123a` depuis la branche `codex/integration-5.1`, réunion de la bulle et des derniers instruments, figures, rotations et retraits. Version 5.1.0, 51 parcours ; 65/65 scénarios locaux réussis et documentation cohérente. Documentation GitHub main `42488838703`, suite des **65 scénarios** `42488838647` et fabrication Windows `42488838661` toutes réussies.
- **Préparation :** `publier-version.py` et `publier-appli.py` officiels utilisés, construction avec listes d’élèves vides. Paquet Windows 5.1.0 de main fabriqué avec succès (`42488838661`), branche `appli-paquets` à `5faacd9`, métadonnée du commit compilé `be2123a` vérifiée sur GitHub puis dans les objets récupérés par GitHub Desktop. Le script officiel reçoit un transport Git local alimenté par cette récupération authentifiée ; aucun script modifié ni identifiant extrait. Installateur identique au blob Git `6e3fb3d90d600b32e240d335a273df59a64a4386`, SHA-256 `3fb20e273255d47836d2799abd9079e300186faebc66823b52f219c5641895db`, 2 984 496 octets. Pages et fiches contrôlées ; canal d’essai inchangé. Tests GitHub réussis avant l’envoi public. Clés de signature gardées dans GitHub, aucune clé privée locale.
- **Publication :** préparation `7d2d4fa`, arbre distant/local identique `de56430c98a17d9513d64166140bcfce76b2fbaa`, puis avance rapide sans forçage de main public depuis `0accc7a`. Action « Publier les mises à jour » `42490503684` réussie. Fiche Ed25519 réellement servie valide, stable 5.1.0, essai 5.0.4 inchangé ; tailles, SHA-256 et octets des deux pages conformes. Installateur servi identique au paquet de main, signature Minisign principale et commentaire de confiance vérifiés avec la clé publique Rust.
- **État final :** **publié sur le canal stable, pages et application Windows**. Cette confirmation ne change que le journal ; `[skip ci]` évite un déploiement supplémentaire, les fichiers servis restent identiques. Anciennes branches de préparation et journaux non enregistrés dans le dossier principal préservés.

## 2026-11-07 — Reconstruction des deux canaux sans mentions nominatives d’assistants

- **Autorisation / contrôle préalable :** Franck demande l’envoi GitHub après nettoyage et choisit de nettoyer aussi les versions distribuées. Dépôt local initialement propre à `f5ede3c` sur `codex/mentions-ia` ; `main` distant relu à `0accc7a`, main source à `c8c56e2`, aucune PR ouverte. Derniers travaux partagés : essai 5.0.4 et documentation ; travaux non partagés hors des dossiers accessibles non observables.
- **Sources / versions :** stable préparée en 5.0.5 depuis 5.0.2, source `b4b96fb`, branche `claude/appli-nettoyage-stable-5.0.5` ; essai préparé en 5.0.6 depuis 5.0.4, source `43c3c15`, branche `claude/appli-nettoyage-essai-5.0.6`. Seuls les textes de présentation, du rapport et le numéro changent dans l’application. Aucun ajout de l’essai à la stable ; crédits de Franck et licences tierces conservés.
- **Construction / validation :** workflows Windows `42363623155` (stable) et `42363647459` (essai) réussis ; suites complètes GitHub de 57 et 59 scénarios et documentation réussies pour les deux sources. ZIP des artefacts vérifiés par leur SHA-256, puis installateurs extraits ; correspondance versions/commits contrôlée. Les pages embarquées proviennent des sources nettoyées des workflows, aucun essai manuel sur un poste Windows dans cette session.
- **Fichiers / scripts :** quatre HTML et `entrees/{stable,essai}.json` préparés par `publier-version.py` ; EXE 5.0.5 et 5.0.6 et `appli/{,essai/}latest.json` préparés par `publier-appli.py`, alimenté par les artefacts vérifiés comme transport (script inchangé). Les deux anciens EXE sont retirés du nouvel arbre, conservés dans l’historique. Empreintes des nouveaux EXE : stable `6f7915d0e66c60399ab4bfd90ab658699757a7b5ff9171e8e7054566d1b36f68`, essai `aeda15f3f4d5ba90903249393765d80b765a3c258581c43a1ca38bd8a09166cb`. Signatures des fiches sources vides comme prévu : signature et déploiement par l’action publique après autorisation.
- **Contrôles / état :** recherche nominative complète des fichiers texte, pages et sources : aucun nom d’assistant hors références techniques ; versions, SHA-256, tailles et correspondance des EXE avec les artefacts validés contrôlés. Modifications sur la branche préparatoire uniquement ; ancien historique et noms techniques conservés.
- **Publication :** l’intégration sur `main` de la source stable a été refusée par le contrôle automatique, faute d’autorisation explicite de publication sur la branche par défaut. Aucun contournement ni déplacement de `main` des deux dépôts. Envoi de cette branche nettoyée autorisé ; publication du site en attente de confirmation explicite pour `main`. Les versions en ligne restent 5.0.2 stable et 5.0.4 essai jusqu’à cette confirmation.

## 2026-11-07 — Neutralisation des anciennes mentions nominatives (`codex/mentions-ia`)

- **Demande / intervenant :** Franck demande de supprimer aussi les anciennes mentions nominatives de l’autre assistant dans les fichiers. Intervention documentaire, sans signature de co-écriture.
- **Contrôle préalable :** dépôt propre sur `codex/mentions-ia` à `ebd2d42`, source propre à `92e62ad`. GitHub relu par le connecteur : distribution `main` à `0accc7a`, main source à `c8c56e2`, essai terminé à `9f4863c` ; branches et derniers commits consultés, aucune PR ouverte. Les travaux non partagés hors des dossiers accessibles restent non observables.
- **Réalisation / fichiers :** recherche dans tous les fichiers suivis : aucune attribution nominative de cet assistant dans le contenu du dépôt public ; seules des références techniques à des branches subsistent dans ce journal. `AGENTS.md` précise que les anciens journaux peuvent être neutralisés sur demande de Franck, en conservant leurs faits. Cette entrée assure la trace de l’intervention dans les deux dépôts.
- **Préservation :** aucun changement du code, de la présentation, des pages, fiches, installateurs, signatures de distribution ou licences ; aucun historique Git réécrit.
- **Validation / livraison :** relecture, `git diff --check` sans erreur et liens Markdown locaux valides ; recherche exhaustive des fichiers suivis : aucune mention nominative de cet assistant, seules les références techniques de branches restent dans le journal. Modifications exclusivement documentaires ; aucun test fonctionnel relancé. Changements enregistrés sur la branche locale existante, aucun envoi ni déploiement.

## 2026-11-07 — Intégration de la distribution d’essai 5.0.4 (`codex/mentions-ia`)

- **Demande / intervenant :** après « Le précédent travail est terminé », l’assistant de développement reprend l’intégration locale des changements d’attribution.
- **Contrôle préalable :** dépôt principal propre sur `main` à `0accc7a`, même référence que le dernier commit de distribution relu par le connecteur ; source sur l’essai terminé `9f4863c`, main source à `c8c56e2`. Branches et derniers commits consultés, aucune PR ouverte dans les deux dépôts. Les changements non partagés hors des dossiers accessibles restent non observables.
- **Réalisation :** fusion sans conflit de `main` dans la branche documentaire locale `codex/mentions-ia` (`020f139` avant intégration), afin de conserver les pages et l’application d’essai 5.0.4. Le dossier principal sera placé sur cette branche pour rendre les nouvelles consignes directement lisibles. Aucun déplacement de `main` et aucune modification des paquets, fiches ou signatures de distribution ; seuls la documentation et le texte de la page de présentation diffèrent de `0accc7a`.
- **Validation :** relecture, liens locaux Markdown et diff contrôlés ; comparaison à `0accc7a` sans différence dans `stable/`, `essai/`, `entrees/`, `appli/` ou `versions.json`. Aucun test fonctionnel relancé pour cette intégration documentaire ; les contrôles de présentation précédents restent applicables.
- **Livraison / état :** intégration sur la branche locale `codex/mentions-ia` et placement du dossier principal sur cette branche ; aucun déplacement de `main`, aucun envoi ni déploiement. L’échec d’authentification Git HTTPS déjà consigné n’a pas été retenté sans changement de configuration.

## 2026-11-07 — Présentation de l’aide de l’IA et fin des signatures de co-écriture (`codex/mentions-ia`)

- **Demande :** supprimer les signatures de co-écriture d’assistants pour les futurs commits et fichiers des deux dépôts ; réserver une mention générale de l’aide de l’IA à la présentation de l’application.
- **Intervenant :** assistant de développement ; trace de travail sans signature de co-écriture.
- **Contrôle préalable :** clone de distribution propre sur `main`, `2857fe9`, identique au dernier commit GitHub consulté. Branches et derniers commits des deux dépôts vérifiés par le connecteur le 7 novembre 2026 ; aucune PR ouverte. Source `main` à `c8c56e2` ; son dossier principal contient un autre travail et une fusion non terminée, laissés intacts. Les travaux des autres intervenants non partagés ne sont pas tous observables.
- **Base / branche :** dossier isolé depuis `origin/main` à `2857fe9`, branche `codex/mentions-ia` ; aucun fichier stable ou d’essai, fiche, ZIP, installateur ou signature de mise à jour modifié.
- **Réalisation / fichiers :** `README.md` et `index.html` : mention générale de l’aide de l’IA au développement et à la documentation sous la direction de Franck VARAULT ; `DOCUMENTATION.md` : nouvelle règle d’attribution et procédure de mise à jour des prochaines pages depuis le dépôt source ; nouveaux `AGENTS.md` et `CLAUDE.md` : consignes communes applicables aux prochains intervenants ; ce journal : traçabilité. Historique et crédits/licences tiers conservés. Aucun changement de licence.
- **Validation :** relecture et contrôle du diff, `git diff --check` sans erreur, liens Markdown valides ; page de présentation contrôlée dans Chromium avec une fiche Windows simulée : mention visible et lien de téléchargement conservé. Première tentative de ce contrôle avec une URL de fichier local non adaptée au chargement de la fiche ; contrôle repris avec une origine de test entièrement simulée. Aucun changement dans `stable/`, `essai/`, `entrees/`, `appli/` ou `versions.json`. Aucun test fonctionnel de distribution relancé pour ces changements de documentation et présentation.
- **Livraison / état :** commit local `44a1c5a`, identité « Franck VARAULT » et adresse publique du projet, sans signature de co-écriture ; branche isolée `codex/mentions-ia`, dossier `/private/tmp/ma-classe-versions-mentions-ia`. Envoi de la branche tenté : échec d’authentification HTTPS (`could not read Username`, invites désactivées) ; branche **non partagée**. Le connecteur reste disponible pour la lecture mais son outil de création de commit n’expose pas l’identité Git à spécifier ; les commits locaux n’ont pas été recréés par cet outil. Aucun envoi sur `main`, aucune validation GitHub déclenchée, aucun déploiement. Commit source associé : `20e1d7b`. La mention « À propos » et les textes du rapport des pages déjà distribuées seront mis à jour lors d’une prochaine publication autorisée depuis les sources corrigées.
