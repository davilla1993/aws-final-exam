# TASKS.md

## Objectif

Réaliser et déployer un pipeline IoT serverless AWS conforme au sujet d'examen.

---

# Phase 1 - Analyse ✅

* [x] Lire complètement le sujet.
* [x] Identifier toutes les ressources AWS requises.
* [x] Vérifier la compatibilité avec AWS Academy Learner Lab.
* [x] Lister les permissions AWS éventuellement bloquantes.

Livrable :

* Architecture validée. ✅

---

# Phase 2 - Infrastructure CloudFormation ✅

Créer le fichier :

* [x] template.yaml (SAM)

Ressources créées :

* [x] S3 Data Lake
* [x] DynamoDB
* [x] IAM Role Lambda
* [x] Lambda Function (AWS::Serverless::Function)
* [x] API Gateway HTTP API (AWS::Serverless::HttpApi)
* [x] Lambda Permission (géré automatiquement par SAM)
* [x] CloudFront Ingestion

Documentation :

* [x] Bucket S3 Documentation
* [x] CloudFront Documentation
* [x] OAC configuré et déployé

Outputs :

* [x] CloudFrontIngestionURL
* [x] CloudFrontDocURL
* [x] S3BucketName
* [x] DynamoDBTableName

Validation :

* [x] Stack CREATE_COMPLETE (eu-west-3, fgbossou-iot-stack)

Captures :

* [x] 01-cloudformation-stack-create-complete.png
* [x] 02-cloudformation-outputs.png
* [x] 03-s3-buckets-list.png
* [x] 04-s3-tech-doc-block-public-access.png
* [x] 05-dynamodb-table.png
* [x] 06a-lambda-function-overview.png
* [x] 06b-lambda-env-vars.png
* [x] 07-apigateway-routes.png
* [x] 08-cloudfront-distributions-list.png
* [x] 09-cloudfront-doc-origin-oac.png
* [x] 10-iam-lambda-role.png

---

# Phase 3 - Développement Lambda ✅

Créer :

* [x] index.py

Fonctionnalités :

* [x] Lecture du body HTTP
* [x] Parsing JSON
* [x] Validation du payload
* [x] Génération request_id
* [x] Calcul température moyenne
* [x] Comptage des statuts ERROR
* [x] Sauvegarde S3
* [x] Partitionnement temporel
* [x] Écriture DynamoDB
* [x] Retour HTTP 201

Gestion des erreurs :

* [x] Payload invalide
* [x] JSON invalide
* [x] Champ manquant
* [x] Exception AWS

Logging :

* [x] Logs CloudWatch structurés

---

# Phase 4 - Script Client ✅

Créer :

* [x] test_client.py

Fonctionnalités :

* [x] Utilisation de requests
* [x] Envoi POST
* [x] 4 mesures minimum
* [x] Affichage réponse HTTP
* [x] Affichage corps réponse

Validation :

* [x] HTTP 201

---

# Phase 5 - Documentation Technique ✅

Créer :

* [x] index.html

Contenu :

* [x] Titre du cours
* [x] Description architecture
* [x] Description du pipeline
* [x] Description des services AWS

Déploiement :

* [x] Upload vers bucket documentation
* [x] Validation Access Denied sur URL S3
* [x] Validation accès via CloudFront (https://d3l8f210waz845.cloudfront.net)

---

# Phase 6 - Validation Fonctionnelle ✅

Tester un payload valide :

* [x] Exécution réussie (HTTP 201)
* [x] Fichier créé dans S3 (raw-zone/year=2026/month=06/day=10/)
* [x] Ligne créée dans DynamoDB (avg_temp=31.1, error_count=2)

Tester un payload invalide :

* [x] Exception générée (HTTP 400)
* [x] Logs visibles dans CloudWatch

Captures :

* [x] 11-s3-raw-data-file.png
* [x] 12-dynamodb-item.png
* [x] 13-s3-direct-access-denied.png
* [x] 14-cloudfront-doc-access-ok.png
* [x] 15-cloudwatch-success.png
* [x] 16-cloudwatch-error.png

---

# Phase 7 - Réponses Théoriques ✅

Préparer les réponses :

* [x] Question 1
* [x] Question 2
* [x] Question 3
* [x] Question 4
* [x] Question 5
* [x] Question 6
* [x] Question 7
* [x] Question 8

Objectif :

* Réponses courtes
* Réponses précises
* Niveau universitaire

---

# Phase 8 - Rapport Final ✅

Créer :

* [x] rapport.html → rapport.pdf

Inclure :

* [x] Introduction
* [x] Architecture
* [x] Réponses théoriques (8 questions)
* [x] Captures CloudFormation (Captures 1 et 2)
* [x] Captures S3 (Captures 11, 12, 13)
* [x] Captures DynamoDB (Captures 14 et 15)
* [x] Captures CloudWatch succès (Capture 16)
* [x] Captures CloudWatch erreur (Capture 17)
* [x] Conclusion

Bonus :

* [x] README.md (guide complet pour correcteur novice)

---

# Phase 9 - Livraison Finale ← EN COURS

## 9.1 Ressources AWS

* [x] Stack fgbossou-iot-stack supprimée
* [x] Bucket data-lake vidé et supprimé
* [x] Bucket tech-doc vidé et supprimé

## 9.2 Préparation du ZIP

* [ ] Copier template.yaml depuis infrastructure/ à la racine du ZIP
* [ ] Inclure index.py
* [ ] Inclure test_client.py
* [ ] Inclure index.html
* [ ] Inclure rapport.pdf
* [ ] Créer fgbossou-iot-pipeline.zip avec ces 5 fichiers uniquement

## 9.3 Vérification avant soumission

* [ ] Ouvrir le ZIP et vérifier les 5 fichiers présents
* [ ] Vérifier que test_client.py contient la bonne URL CloudFront
* [ ] Vérifier que rapport.pdf s'ouvre correctement
* [ ] Relire rapidement le README.md

## 9.4 Soumission

* [ ] Déposer fgbossou-iot-pipeline.zip sur Google Classroom

---

# Contraintes AWS Academy Learner Lab

Toujours vérifier :

* Permissions IAM disponibles
* Création CloudFront autorisée
* Création OAC autorisée
* Création API Gateway autorisée
* Création Lambda autorisée

Si une ressource est refusée :

1. Identifier la permission manquante.
2. Documenter le problème.
3. Proposer une alternative compatible.
4. Ne jamais bloquer l'avancement du projet.

---

# Définition de Terminé

Le projet est terminé lorsque :

* [x] Stack CREATE_COMPLETE
* [x] Lambda fonctionnelle
* [x] Upload S3 fonctionnel
* [x] DynamoDB alimentée
* [x] CloudFront accessible
* [x] Documentation accessible
* [x] Captures réalisées
* [x] Rapport PDF terminé
* [ ] ZIP prêt pour Google Classroom
