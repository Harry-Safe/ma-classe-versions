# Site gelé

**Décision de Franck du 21 novembre 2026, 13 h 43** : « je ne veux plus que les prochains essais apparaissent sur le
site internet : on le gèle tel quel. »

- **glacis-classe.fr reste tel qu'il est** : page de présentation publiée le 21 novembre 2026 (commit `77600f3`), essai
  6.0.0-beta.28 en téléchargement, `versions.json` et `applis.json` inchangés.
- Tant que ce fichier existe, l'action « Publier les mises à jour » **échoue sur `main` avant toute fabrication,
  signature ou mise en ligne** (étape « Site gelé ? » de `.github/workflows/publier.yml`).
- Les essais suivants ne sont **plus publiés ici** : ils restent dans la branche `essai` du dépôt source et sont livrés
  à Franck en fichier (« Glacis - essai.html »). Les postes où un essai est installé ne reçoivent plus de mise à jour
  automatique tant que le site est gelé.
- Ne pas retirer ce fichier, ne pas contourner la garde (déploiement à la main, autre branche, `wrangler` lancé
  ailleurs) : le **dégel** se fait seulement sur une phrase explicite de Franck, en retirant ce fichier dans un envoi
  sur `main`.
