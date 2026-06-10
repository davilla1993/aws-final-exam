# Pipeline d'Ingestion de Données IoT en Temps Réel (Serverless)

**Cours :** Introduction à AWS  
**Étudiant :** GBOSSOU Folly S. Carlo (`fgbossou`)  
**Région AWS :** eu-west-3 (Paris)

---

## Description du Projet

Ce projet déploie un pipeline serverless complet sur AWS permettant d'ingérer en
temps réel des données envoyées par des capteurs IoT via des requêtes HTTP POST.

L'infrastructure est entièrement automatisée avec **AWS SAM** et se déploie en
une seule commande. Aucune action manuelle dans la console AWS n'est nécessaire.

---

## Architecture

```
Client IoT (test_client.py)
        │  HTTP POST
        ▼
Amazon CloudFront  ──►  Amazon API Gateway  ──►  AWS Lambda (Python 3.11)
                                                       ├──► S3 Data Lake
                                                       └──► DynamoDB

Navigateur
        │  HTTPS
        ▼
Amazon CloudFront  ──►  S3 Bucket privé (OAC)  ──►  index.html
```

**10 ressources AWS créées automatiquement :**

| Ressource | Rôle |
|---|---|
| S3 Data Lake | Stockage brut des payloads IoT (partitionnement temporel) |
| DynamoDB | Feature Store : métriques agrégées par requête |
| IAM Role | Permissions minimales pour la Lambda |
| API Gateway HTTP API | Point d'entrée REST — route POST / |
| Lambda Python 3.11 | Validation, calcul, écriture S3 + DynamoDB |
| CloudFront Ingestion | CDN mondial devant API Gateway |
| S3 Documentation | Hébergement privé de la doc technique |
| OAC | Contrôle d'accès sécurisé S3 via SigV4 |
| CloudFront Documentation | CDN sécurisé devant S3 doc |
| Bucket Policy | Restreint l'accès S3 à CloudFront uniquement |

---

## Prérequis

Avant de commencer, installer les outils suivants sur votre machine :

### 1. AWS CLI

Télécharger et installer : https://aws.amazon.com/cli/

Vérifier l'installation :
```bash
aws --version
```

### 2. AWS SAM CLI

Télécharger et installer : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

Vérifier l'installation :
```bash
sam --version
```

### 3. Python 3.11+

Télécharger : https://www.python.org/downloads/

Vérifier :
```bash
python --version
```

### 4. Bibliothèque requests (pour le script de test)

```bash
pip install requests
```

---

## Configuration des Credentials AWS

### Si vous utilisez AWS Academy Learner Lab

1. Ouvrez votre session Learner Lab
2. Cliquez sur **AWS Details** en haut à droite
3. Cliquez sur **Show** à côté de *AWS CLI*
4. Copiez les trois lignes (`aws_access_key_id`, `aws_secret_access_key`, `aws_session_token`)
5. Collez-les dans le fichier `~/.aws/credentials` :

```
[default]
aws_access_key_id = VOTRE_ACCESS_KEY
aws_secret_access_key = VOTRE_SECRET_KEY
aws_session_token = VOTRE_SESSION_TOKEN
```

> **Important :** Ces credentials expirent à chaque fin de session Learner Lab.
> Il faudra les renouveler à chaque nouvelle session.

---

## Déploiement de l'Infrastructure

### Étape 1 — Cloner ou décompresser le projet

```bash
cd aws-final-exam
```

### Étape 2 — Déployer avec SAM

```bash
sam deploy \
  --template-file infrastructure/template.yaml \
  --stack-name fgbossou-iot-stack \
  --capabilities CAPABILITY_NAMED_IAM \
  --resolve-s3 \
  --region eu-west-3
```

**Explication des paramètres :**
- `--template-file` : chemin vers le template CloudFormation/SAM
- `--stack-name` : nom donné à l'ensemble des ressources créées
- `--capabilities CAPABILITY_NAMED_IAM` : autorise la création du rôle IAM nommé
- `--resolve-s3` : SAM crée automatiquement un bucket S3 pour packager le code Lambda
- `--region eu-west-3` : région AWS Paris

### Étape 3 — Attendre CREATE_COMPLETE

Le déploiement prend **3 à 5 minutes** (les distributions CloudFront prennent plus de temps à se propager).

Vous verrez en fin de déploiement :
```
Successfully created/updated stack - fgbossou-iot-stack in eu-west-3
```

### Étape 4 — Récupérer les URLs

```bash
aws cloudformation describe-stacks \
  --stack-name fgbossou-iot-stack \
  --query "Stacks[0].Outputs" \
  --region eu-west-3
```

Vous obtenez :

| Output | Description |
|---|---|
| `CloudFrontIngestionURL` | URL pour envoyer les données IoT (POST) |
| `CloudFrontDocURL` | URL pour accéder à la documentation |
| `S3BucketName` | Nom du bucket Data Lake |
| `DynamoDBTableName` | Nom de la table DynamoDB |

---

## Déploiement de la Documentation

Une fois la stack déployée, uploader la page de documentation dans S3 :

```bash
aws s3 cp index.html \
  s3://$(aws cloudformation describe-stacks \
    --stack-name fgbossou-iot-stack \
    --query "Stacks[0].Outputs[?OutputKey=='S3BucketName'].OutputValue" \
    --output text \
    --region eu-west-3 | sed 's/data-lake/tech-doc/') \
  --region eu-west-3
```

Ou directement avec le nom du bucket (remplacer `ACCOUNT_ID`) :

```bash
aws s3 cp index.html \
  s3://ACCOUNT_ID-fgbossou-iot-pipeline-tech-doc/index.html \
  --region eu-west-3
```

---

## Test du Pipeline

### Configurer l'URL

Ouvrir `test_client.py` et remplacer la ligne 5 :

```python
CLOUDFRONT_INGESTION_URL = "https://VOTRE_URL.cloudfront.net"
```

avec la valeur de `CloudFrontIngestionURL` récupérée à l'étape 4.

### Lancer les tests

```bash
python test_client.py
```

**Résultats attendus :**

```
TEST : Payload valide — HTTP 201 attendu
Statut HTTP : 201
{
  "message": "Data ingested successfully",
  "request_id": "...",
  "average_temperature": 31.1,
  "error_count": 2
}

TEST : Payload invalide (temperature manquant) — HTTP 400 attendu
Statut HTTP : 400
{
  "message": "Missing field \"temperature\" in measurement at index 0"
}

TEST : JSON malformé — HTTP 400 attendu
Statut HTTP : 400
{
  "message": "Invalid JSON"
}
```

---

## Format du Payload IoT

La Lambda accepte uniquement ce format JSON :

```json
{
  "measurements": [
    {
      "sensor_id": "sensor-1",
      "temperature": 22.5,
      "status": "OK"
    },
    {
      "sensor_id": "sensor-2",
      "temperature": 37.8,
      "status": "ERROR"
    }
  ]
}
```

**Champs obligatoires par mesure :** `sensor_id`, `temperature`, `status`

**Codes de retour :**

| Code | Signification |
|---|---|
| `201` | Données ingérées avec succès |
| `400` | Payload invalide ou JSON malformé |
| `500` | Erreur interne AWS (S3 ou DynamoDB) |

---

## Vérification des Données

### Dans S3

```
AWS Console → S3 → ACCOUNT_ID-fgbossou-iot-pipeline-data-lake
→ raw-zone/year=2026/month=06/day=10/
```

Un fichier JSON est créé pour chaque appel réussi.

### Dans DynamoDB

```
AWS Console → DynamoDB → Tables → fgbossou-iot-pipeline-iot-metrics
→ Explorer les éléments → Requête sur request_id
```

### Dans CloudWatch Logs

```
AWS Console → CloudWatch → Log groups
→ /aws/lambda/fgbossou-iot-pipeline-ingestion
```

---

## Suppression des Ressources

Pour supprimer toutes les ressources créées (éviter les coûts) :

> ⚠️ **Attention :** vider d'abord les buckets S3 avant de supprimer la stack,
> sinon la suppression échouera.

### Étape 1 — Vider les buckets S3

```bash
aws s3 rm s3://ACCOUNT_ID-fgbossou-iot-pipeline-data-lake --recursive --region eu-west-3
aws s3 rm s3://ACCOUNT_ID-fgbossou-iot-pipeline-tech-doc --recursive --region eu-west-3
```

### Étape 2 — Supprimer la stack

```bash
aws cloudformation delete-stack \
  --stack-name fgbossou-iot-stack \
  --region eu-west-3
```

### Étape 3 — Vérifier la suppression

```bash
aws cloudformation describe-stacks \
  --stack-name fgbossou-iot-stack \
  --region eu-west-3
```

Quand la stack n'existe plus, la commande retourne une erreur `Stack with id fgbossou-iot-stack does not exist` — c'est normal, cela confirme la suppression.

---

## Structure du Projet

```
aws-final-exam/
├── infrastructure/
│   └── template.yaml        # Template SAM / CloudFormation (10 ressources)
├── rapport/
│   ├── rapport.html         # Rapport de projet (ouvrir dans navigateur → PDF)
│   └── *.png                # Captures d'écran AWS Console
├── index.py                 # Code de la fonction Lambda Python 3.11
├── test_client.py           # Script de test HTTP (3 scénarios)
├── index.html               # Documentation technique (uploadée dans S3)
├── TASKS.md                 # Suivi des phases du projet
└── README.md                # Ce fichier
```

---

## Dépannage

### La stack ne se crée pas

- Vérifier que les credentials AWS sont valides : `aws sts get-caller-identity`
- Vérifier la région : `--region eu-west-3`
- Relancer la session Learner Lab si les credentials ont expiré

### HTTP 403 sur l'URL CloudFront

- CloudFront prend 5 à 15 minutes à se propager après création
- Attendre et réessayer

### DynamoDB : Accès refusé sur Scan

- Utiliser **Query** dans la console avec le `request_id` exact
- Ou utiliser la CLI : `aws dynamodb get-item --table-name fgbossou-iot-pipeline-iot-metrics --key '{"request_id": {"S": "VOTRE_ID"}}' --region eu-west-3`

### La documentation ne s'affiche pas via CloudFront

- Vérifier que `index.html` a bien été uploadé dans le bucket `tech-doc`
- Invalider le cache : `aws cloudfront create-invalidation --distribution-id ID --paths "/index.html"`
