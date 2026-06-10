# TASKS.md

## Objectif

Réaliser et déployer un pipeline IoT serverless AWS conforme au sujet d'examen.

---

# Phase 1 - Analyse

* [ ] Lire complètement le sujet.
* [ ] Identifier toutes les ressources AWS requises.
* [ ] Vérifier la compatibilité avec AWS Academy Learner Lab.
* [ ] Lister les permissions AWS éventuellement bloquantes.

Livrable :

* Architecture validée.

---

# Phase 2 - Infrastructure CloudFormation

Créer le fichier :

* [ ] template.yaml

Ressources minimales :

* [ ] S3 Data Lake
* [ ] DynamoDB
* [ ] IAM Role Lambda
* [ ] Lambda Function
* [ ] API Gateway HTTP API
* [ ] Lambda Permission
* [ ] CloudFront Ingestion

Documentation :

* [ ] Bucket S3 Documentation
* [ ] CloudFront Documentation
* [ ] OAC si autorisé
* [ ] Alternative documentée si OAC refusé

Outputs :

* [ ] CloudFrontIngestionURL
* [ ] CloudFrontDocURL
* [ ] S3BucketName
* [ ] DynamoDBTableName

Validation :

* [ ] Stack CREATE_COMPLETE

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

* [ ] Stack CREATE_COMPLETE
* [ ] Lambda fonctionnelle
* [ ] Upload S3 fonctionnel
* [ ] DynamoDB alimentée
* [ ] CloudFront accessible
* [ ] Documentation accessible
* [ ] Captures réalisées
* [ ] Rapport PDF terminé
* [ ] ZIP prêt pour Google Classroom
