# Site gelé

**Décision de Franck du 21 novembre 2026, 13 h 43** : « je ne veux plus que les prochains essais apparaissent sur le
site internet : on le gèle tel quel. »

- **glacis-classe.fr reste tel qu'il est** : page de présentation publiée le 21 novembre 2026 (commit `77600f3`), essai
  6.0.0-beta.28 en téléchargement, `versions.json` et `applis.json` inchangés.
- **Dégel ponctuel du 22 novembre 2026** (Franck, 11 h 10 : « Publie la mention de marque ») : seule la mention de la
  marque Glacis™ a été ajoutée à la page (commit `9cdf17f`, action 45011178325) ; aucun nouvel essai ; site regelé aussitôt.
- **Dégel ponctuel du 22 novembre 2026, 16 h 41** (« Publie les fichiers pour les moteurs de recherche ») : `robots.txt`, `sitemap.xml` et adresse canonique (commit `a341866`, action 45039713776) ; aucun nouvel essai ; site regelé aussitôt.
- Tant que ce fichier existe, l'action « Publier les mises à jour » **échoue sur `main` avant toute fabrication,
  signature ou mise en ligne** (étape « Site gelé ? » de `.github/workflows/publier.yml`).
- Les essais suivants ne sont **plus publiés ici** : ils restent dans la branche `essai` du dépôt source et sont livrés
  à Franck en fichier (« Glacis - essai.html »). Les postes où un essai est installé ne reçoivent plus de mise à jour
  automatique tant que le site est gelé.
- Ne pas retirer ce fichier, ne pas contourner la garde (déploiement à la main, autre branche, `wrangler` lancé
  ailleurs) : le **dégel** se fait seulement sur une phrase explicite de Franck, en retirant ce fichier dans un envoi
  sur `main`.
