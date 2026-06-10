**Responsable du cours:** Mofiala Hervé LOKOSSOU **Cours:** Introduction à AWS **Durée:** 48h 

## Devoir final: Pipeline d'Ingestion de Données IoT en Temps Réel (Serverless) 

## **Instructions:** 

Suivez les étapes ci-dessous pour configurer votre infrastructure Cloud sur AWS et créer un pipeline d'ingestion opérationnel. Assurez-vous de documenter chaque étape de votre travail. Vous serez évalué sur la précision de votre configuration CloudFormation, la qualité de votre code de traitement Python, ainsi que la viabilité de votre architecture. 

À la fin du projet, soumettez sur google Classroom le rendu en pièce jointe un dossier compressé ( .zip ) contenant : 

- Le fichier d'infrastructure template.yaml (CloudFormation). 

- Le fichier de code index.py (Lambda). 

- Le script de test client test_client.py . 

- Un rapport PDF contenant les réponses aux questions théoriques et les captures d'écran requises : l'interface CloudFormation avec la pile créée 

   - ( CREATE_COMPLETE ), l'arborescence des fichiers dans S3, la table DynamoDB avec les lignes insérées, et une capture des logs CloudWatch (une exécution en succès et une exécution en échec). 

## **Contexte:** 

Vous travaillez en tant qu'Ingénieur Big Data & IA pour une entreprise industrielle qui déploie des milliers de capteurs IoT. Votre tâche est de mettre en place une architecture hautement disponible, capable de capter les flux de données envoyés par requêtes HTTP POST en temps réel. En parallèle, pour l'équipe de Data Scientists, vous devez déployer un site web statique contenant la documentation technique du projet. 

Toute l'infrastructure doit être automatisée avec **CloudFormation** . Le traitement de données à la volée s'appuiers sur **AWS Lambda (Python 3.11)** pour alimenter un Data Lake brut sur **Amazon S3** et mettre à jour un Feature Store analytique sur **Amazon DynamoDB** , le tout accéléré par un premier CDN **Amazon CloudFront** . La documentation technique sera quant 

à elle isolée dans un second bucket S3 privé, rendu accessible au public de manière sécurisée uniquement à travers une seconde distribution **Amazon CloudFront** via le mécanisme **OAC (Origin Access Control)** . 

## **Questions à se poser:** 

- **Question 1 :** Expliquez le concept d'Infrastructure as Code (IaC) et décrivez brièvement le rôle d'AWS CloudFormation dans la gestion d'un cycle de vie applicatif. 

- **Question 2 :** Qu'est-ce qu'une fonction AWS Lambda ? En quoi son approche "Serverless" se distingue-t-elle d'une architecture classique basée sur des instances virtuelles Amazon EC2 ? 

- **Question 3 :** Quel est l'intérêt architectural d'adosser une distribution Amazon CloudFront devant un point d'entrée Amazon API Gateway pour une collecte globale de données IoT ? 

- **Question 4 :** Dans un écosystème Big Data, pourquoi choisit-on de stocker les données brutes sur Amazon S3 (Data Lake) et les indicateurs agrégés sur Amazon DynamoDB (Serving Layer) plutôt que de tout centraliser dans une unique base de données relationnelle ? 

- **Question 5 :** Expliquez le principe du modèle de responsabilité partagée d'AWS concernant la sécurité des données stockées dans Amazon S3. 

- **Question 6 :** Pourquoi est-il fortement déconseillé d'activer le "Static Website Hosting" public sur un bucket S3 pour héberger une documentation interne ? En quoi l'utilisation d'une distribution CloudFront combinée avec un **Origin Access Control (OAC)** améliore-t-elle la sécurité ? 

- **Question 7 :** Comment Amazon CloudWatch permet-il de superviser et de déboguer le code d'une application serverless ? Que se passe-t-il au niveau des logs si la fonction Lambda lève une exception non gérée ? 

- **Question 8 :** Imaginons qu'un fichier de données de 50 Go soit déposé d'un coup. Pourquoi l'architecture AWS Lambda actuelle va-t-elle atteindre ses limites ? Quel service managé d'AWS orienté Big Data devrions-nous utiliser pour traiter ce volume de données ? 

## **Configuration et Déploiement de l'Infrastructure (CloudFormation):** 

**a.** Créez un fichier d'infrastructure nommé template.yaml 

**b.** Déployez ce template via la console AWS CloudFormation. Assurez-vous que le statut final passe à CREATE_COMPLETE et récupérez les deux URLs CloudFront générées dans l'onglet _Outputs_ . 

**c.** Écrivez le code complet de la fonction Lambda dans un fichier séparé index.py . Le code doit remplacer le message par défaut par un algorithme d'ingestion réel utilisant le SDK boto3. 

d . Votre script Python doit accomplir les tâches suivantes : 

- Extraire et analyser (parser) le corps JSON de la requête HTTP entrante. 

- Sauvegarder l'intégralité du payload brut sous forme de fichier JSON dans le bucket S3 référencé par la variable d'environnement S3_BUCKET . Vous devez appliquer une stratégie de partitionnement temporel dans la clé de stockage 

   - ( raw-zone/year=YYYY/month=MM/ ). 

- Calculer à la volée la température moyenne de la série reçue ainsi que le nombre total d'enregistrements présentant un statut "ERROR" . 

- Enregistrer un rapport d'exécution condensé dans la table DynamoDB ( DYNAMODB_TABLE ) incluant l'ID de la requête, l'horodatage, le chemin d'accès S3 du fichier brut, la température moyenne calculée et le compte des anomalies. 

## e. Simulation d'Injection et Script Client 

   - Créez un script Python local nommé test_client.py . 

   - Utilisez la bibliothèque requests pour envoyer un payload de test contenant au moins 4 mesures structurées (avec des clés sensor_id , temperature , et status ) via une requête HTTP POST dirigée vers l'URL CloudFrontIngestionURL de votre architecture. 

   - Le script doit intercepter et afficher la réponse renvoyée par AWS (Statut HTTP 201 ). 

- f. Déploiement du Site de Documentation Technique 

   - Créez sur votre machine locale un fichier HTML simple nommé index.html . Ce fichier doit contenir le titre complet du cours ainsi que la description textuelle de l'architecture Big Data mise en place. 

   - **b.** Connectez-vous à la console AWS, accédez au bucket de documentation ( -tech-doc ) créé par votre pile, puis importez ce fichier index.html à la racine via la CLI; la commande doit etre visible dans votre documentation. 

   - **c.** Tentez d'accéder à ce fichier via son URL S3 directe pour valider le blocage des accès publics ( Access Denied ), puis ouvrez l'URL CloudFrontDocURL récupérée dans vos _Outputs_ pour valider l'affichage correct du site web via le CDN sécurisé. 

## g. Vérification, Monitoring et Gestion des Échecs : 

- Exécutez votre script client avec un jeu de données valide. Allez vérifier et capturer la présence du fichier JSON dans Amazon S3 ainsi que l'insertion des métriques agrégées dans Amazon DynamoDB. 

- Modifiez votre script client pour envoyer un payload délibérément corrompu (par exemple, un JSON mal formé ou des valeurs de température manquantes) afin de lever une exception dans votre fonction Lambda. 

- Accédez au service **Amazon CloudWatch Logs** . Identifiez le groupe de logs associé à votre fonction Lambda. Analysez le comportement de la plateforme en localisant d'une part la trace d'une exécution réussie, et d'autre part le rapport d'erreur complet (Stack Trace Python) généré lors de la soumission du payload corrompu. 

## **Documentation du Rapport :** 

- Produisez une documentation structurée décrivant l'ensemble de votre démarche d'implémentation. 

- Intégrez de manière claire toutes les captures d'écran requises dans les instructions initiales afin de prouver le bon fonctionnement de chaque brique de l'architecture 

## **Critères d'Évaluation :** 

- **Validation de l'infrastructure CloudFormation :** Pile déployée sans erreur et structure des ressources respectée pour les deux sous-systèmes. 

- **Qualité et robustesse du code Python (Lambda) :** Utilisation correcte du SDK boto3 , gestion des variables d'environnement, calcul exact des métriques et mise en place efficace du partitionnement S3. 

- **Sécurisation des accès Web :** Isolation stricte du bucket de documentation validée par un blocage direct et un fonctionnement via CloudFront OAC. 

- **Validation de bout en bout :** Preuve d'intégration fonctionnelle entre CloudFront, l'API, la Lambda et les couches de stockage. 

- **Clarté du rapport et pertinence des réponses :** Justesse technique des explications théoriques et rigueur de la documentation fournie. 

