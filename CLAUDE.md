# CLAUDE.md

## Contexte

Je suis Carlo, ingénieur logiciel spécialisé Java, Spring Boot et Angular.

Je travaille actuellement sur mon examen final AWS intitulé :

**Pipeline d'Ingestion de Données IoT en Temps Réel (Serverless)**

L'objectif est de produire une solution complète, fonctionnelle et déployable sur AWS.

Les livrables attendus sont :

* template.yaml (CloudFormation)
* index.py (AWS Lambda Python 3.11)
* test_client.py
* index.html
* rapport PDF

Le projet doit être réalisable intégralement avec les services AWS demandés dans le sujet.

---

## Règles générales

* Toujours privilégier les bonnes pratiques AWS.
* Générer du code prêt à exécuter.
* Ne jamais utiliser de pseudo-code.
* Toujours fournir des explications courtes et concrètes.
* Lorsque tu proposes une modification, expliquer brièvement pourquoi.
* Respecter strictement les exigences du sujet.
* Si une information est manquante, faire l'hypothèse la plus raisonnable puis la documenter.

---

## Architecture cible

Le pipeline doit respecter cette architecture :

Internet
↓
CloudFront (Ingestion)
↓
API Gateway HTTP API
↓
Lambda Python 3.11
↓
S3 Raw Data Lake

Lambda
↓
DynamoDB

Documentation
↓
S3 privé
↓
CloudFront
↓
Origin Access Control (OAC)

---

## Ressources AWS attendues

CloudFormation doit créer :

### Ingestion

* Bucket S3 Data Lake
* Table DynamoDB
* Fonction Lambda
* IAM Role Lambda
* API Gateway HTTP API
* Intégration API Gateway → Lambda
* Permission Lambda Invoke
* Distribution CloudFront pour l'API

### Documentation

* Bucket S3 privé
* Bucket Policy
* Origin Access Control
* Distribution CloudFront Documentation

### Monitoring

* CloudWatch Logs

### Outputs

Exposer :

* CloudFrontIngestionURL
* CloudFrontDocURL
* S3BucketName
* DynamoDBTableName

---

## Contraintes Lambda

La Lambda doit :

1. Recevoir une requête HTTP POST.
2. Parser le JSON reçu.
3. Valider les données.
4. Générer un request_id unique.
5. Calculer :

   * température moyenne
   * nombre d'anomalies (status = ERROR)
6. Sauvegarder le payload brut dans S3.
7. Utiliser un partitionnement :

raw-zone/year=YYYY/month=MM/day=DD/

8. Enregistrer dans DynamoDB :

* request_id
* timestamp
* s3_path
* average_temperature
* error_count

9. Retourner HTTP 201 en cas de succès.

10. Retourner HTTP 400 ou 500 selon l'erreur.

---

## Format attendu du payload

```json
{
  "measurements": [
    {
      "sensor_id": "sensor-1",
      "temperature": 24.5,
      "status": "OK"
    }
  ]
}
```

---

## Bibliothèques autorisées

Lambda :

* boto3
* json
* uuid
* datetime
* os
* logging

Client :

* requests
* json

---

## Gestion des erreurs

Toujours :

* logger les erreurs dans CloudWatch
* utiliser try/catch
* retourner un message JSON explicite
* lever les exceptions pertinentes

Exemple :

```json
{
  "message": "Invalid payload"
}
```

---

## Style CloudFormation

* Utiliser YAML.
* Nommer clairement chaque ressource.
* Ajouter des Outputs utiles.
* Utiliser Ref et GetAtt correctement.
* Éviter les hardcodes.
* Utiliser des variables d'environnement Lambda.

---

## Lorsque je demande du code

Je veux :

* le fichier complet
* pas seulement un extrait
* compatible AWS Free Tier autant que possible
* prêt à être copié/collé

---

## Lorsque je demande une revue

Analyse :

1. Conformité au sujet.
2. Sécurité.
3. Coût AWS.
4. Maintenabilité.
5. Risques de déploiement.

Puis propose les corrections nécessaires.
