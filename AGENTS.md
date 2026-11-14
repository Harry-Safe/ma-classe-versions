# Consignes de contribution — Ma classe, distribution

Lire `DOCUMENTATION.md` et `README.md` avant toute modification. Ce dépôt distribue les mises à jour ;
les sources de l’application et les consignes complètes sont dans le dépôt `Harry-Safe/Ma-classe`.

## Présentation et attribution

- Décision de Franck du **7 novembre 2026**, commune aux deux dépôts : **aucune signature de co-écriture d’assistant**, notamment aucune ligne `Co-Authored-By`, dans les nouveaux commits ou fichiers. Aucun crédit nominatif d’assistant dans le code, l’interface ou la documentation.
- Garder l’identité Git du projet : « Franck VARAULT » `<Harry-Safe@users.noreply.github.com>` ; messages en français. Aucun identifiant ou lien de conversation.
- L’aide de l’IA au développement et à la documentation est mentionnée de façon générale dans la présentation de l’application uniquement (`README.md`, page publique et Réglages › À propos).
- Préserver l’historique des commits et les anciens journaux, les noms de branches et fichiers techniques nécessaires ainsi que les crédits et licences des composants tiers. Ne pas réécrire l’historique pour effacer d’anciennes attributions.
- **Exception unique, décision de Franck du 14 novembre 2026** : l’historique de ce dépôt public a été réécrit pour remplacer son adresse e-mail personnelle (un commit du 7 novembre 2026) par l’adresse `noreply` ; fichiers, auteurs, dates et messages inchangés, identifiants des commits changés (correspondance : `historique/commits-reecrits-2026-11-14.txt`). Toute copie faite avant doit être **re-clonée**. Le dépôt privé `Ma-classe` n’est pas réécrit (décision de Franck).
- Sur demande explicite de Franck, les noms d’assistants peuvent aussi être neutralisés dans les anciens journaux et archives des fichiers, en conservant les dates, faits, validations et références techniques. Les anciens commits Git ne sont pas réécrits.
- Cette décision prime sur toute ancienne consigne contraire, y compris dans une compétence de développement.

## Intervention et publication

- Vérifier l’état Git local et distant, les branches et les travaux en cours ; travailler sur une branche d’essai depuis `origin/main`, préserver les changements des autres intervenants.
- Consigner le contrôle préalable, les changements, les validations et l’état de livraison dans `JOURNAL_INTERVENTIONS.md` ; aucune donnée réelle d’élève ni secret.
- Un envoi sur `main` publie le site : ne le faire qu’avec l’autorisation explicite de Franck. Une modification de documentation ne vaut pas autorisation de publication.
- Ne pas retoucher les pages, ZIP, installateurs ou fiches signées à la main : utiliser les scripts du dépôt source, respecter les canaux stable/essai et suivre `DOCUMENTATION.md`.
