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

# Phase 3 - Développement Lambda

Créer :

* [ ] index.py

Fonctionnalités :

* [ ] Lecture du body HTTP
* [ ] Parsing JSON
* [ ] Validation du payload
* [ ] Génération request_id
* [ ] Calcul température moyenne
* [ ] Comptage des statuts ERROR
* [ ] Sauvegarde S3
* [ ] Partitionnement temporel
* [ ] Écriture DynamoDB
* [ ] Retour HTTP 201

Gestion des erreurs :

* [ ] Payload invalide
* [ ] JSON invalide
* [ ] Champ manquant
* [ ] Exception AWS

Logging :

* [ ] Logs CloudWatch structurés

---

# Phase 4 - Script Client

Créer :

* [ ] test_client.py

Fonctionnalités :

* [ ] Utilisation de requests
* [ ] Envoi POST
* [ ] 4 mesures minimum
* [ ] Affichage réponse HTTP
* [ ] Affichage corps réponse

Validation :

* [ ] HTTP 201

---

# Phase 5 - Documentation Technique

Créer :

* [ ] index.html

Contenu :

* [ ] Titre du cours
* [ ] Description architecture
* [ ] Description du pipeline
* [ ] Description des services AWS

Déploiement :

* [ ] Upload vers bucket documentation
* [ ] Validation Access Denied sur URL S3
* [ ] Validation accès via CloudFront

---

# Phase 6 - Validation Fonctionnelle

Tester un payload valide :

* [ ] Exécution réussie
* [ ] Fichier créé dans S3
* [ ] Ligne créée dans DynamoDB

Tester un payload invalide :

* [ ] Exception générée
* [ ] Logs visibles dans CloudWatch

Captures :

* [ ] Succès
* [ ] Erreur

---

# Phase 7 - Réponses Théoriques

Préparer les réponses :

* [ ] Question 1
* [ ] Question 2
* [ ] Question 3
* [ ] Question 4
* [ ] Question 5
* [ ] Question 6
* [ ] Question 7
* [ ] Question 8

Objectif :

* Réponses courtes
* Réponses précises
* Niveau universitaire

---

# Phase 8 - Rapport Final

Créer :

* [ ] rapport.pdf

Inclure :

* [ ] Introduction
* [ ] Architecture
* [ ] Réponses théoriques
* [ ] Captures CloudFormation
* [ ] Captures S3
* [ ] Captures DynamoDB
* [ ] Captures CloudWatch succès
* [ ] Captures CloudWatch erreur
* [ ] Conclusion

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
* [ ] Lambda fonctionnelle
* [ ] Upload S3 fonctionnel
* [ ] DynamoDB alimentée
* [ ] CloudFront accessible
* [ ] Documentation accessible
* [ ] Captures réalisées
* [ ] Rapport PDF terminé
* [ ] ZIP prêt pour Google Classroom
