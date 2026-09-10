---
role: brique
nom: Databricks
alias: [databricks, Azure Databricks, Databricks Lakehouse]
pitch: "Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement."
categorie: ml/plateforme
famille: saas
domaines: [data-eng, data-sci, mlops]
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Dataiku]]", "[[Snowflake]]", "[[AWS SageMaker]]", "[[Google Cloud Vertex AI]]", "[[Microsoft Azure Machine Learning]]"]
complements: ["[[Spark]]", "[[MLflow]]"]
tags: [ml-platform, lakehouse, distributed, data-governance, data-pipeline, olap]
url_docs: https://docs.databricks.com/
url_repo: 
---

# Databricks

<!-- AUTO:BANDEAU:START -->
> Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'analytique et d'IA bâtie autour de l'architecture **lakehouse** : les données
restent sur du stockage objet, dans un format de table transactionnel — Delta Lake — et le
même jeu sert au SQL analytique, aux pipelines et à l'entraînement, sans copie vers un
entrepôt séparé. Le moteur est [[Spark]], dont les créateurs de Databricks sont aussi les
auteurs ; la gouvernance passe par Unity Catalog, qui porte le catalogue, le lignage et les
droits. Elle se déploie **dans le compte cloud du client**, sur AWS, Azure ou GCP, ce qui
n'est pas de l'auto-hébergement : un compte Databricks reste obligatoire, et il n'existe
aucune installation sur des serveurs qu'on possède.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Gros volumes et data engineering écrit en code, par une équipe technique | **Aucun déploiement sur site n'existe** : c'est éliminatoire dès que les données ne peuvent pas partir chez un fournisseur |
| Un seul jeu de données doit servir le SQL, les pipelines et le ML sans être recopié | La facturation à l'usage de calcul se pilote mal : un cluster oublié coûte, et la maîtrise du coût est un travail à part entière |
| L'équipe connaît déjà Spark, ou le volume justifie de l'apprendre | Une équipe d'analystes métier sans Python ni SQL avancé → [[Alteryx]] ou [[Dataiku]] |
| Il faut un catalogue et un lignage communs à la donnée et aux modèles | Le centre de gravité est un entrepôt SQL et le restera → [[Snowflake]] |
| Le client est déjà sur AWS, Azure ou GCP et veut une couche unique par-dessus | Le besoin tient dans un seul poste et quelques fichiers → [[DuckDB]] ou [[Polars]] |

## Mise en œuvre

- Installation — souscription Databricks, puis déploiement de l'espace de travail dans le compte cloud AWS, Azure ou GCP
- Point d'entrée — notebooks et éditeur SQL de l'espace de travail ; API REST et SDK pour l'automatisation
- Prérequis — un compte chez l'un des trois fournisseurs, et la maîtrise des coûts de calcul dès la mise en service
- Exécution — managé, distribué ; clusters Spark dimensionnés à la charge, options serverless selon les services
- Coût — à l'usage, en unités de calcul facturées par-dessus la facture du fournisseur cloud

## Écosystème

### Alternatives

- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — la suite comparable, mais installable sur site et ouverte aux non-codeurs.
- [[Snowflake]] — Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement. — le concurrent frontal : l'arbitrage se joue sur le point de départ, entrepôt SQL contre lac de fichiers.
- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts. — l'option native quand on ne veut pas de couche par-dessus le cloud.
- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud. — idem chez Google.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc. — idem chez Microsoft.

### Compléments

- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — le moteur de la plateforme, écrit par les mêmes auteurs ; les compétences se transfèrent dans les deux sens.
- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud. — né chez Databricks, qui en propose une édition managée intégrée à l'authentification et au catalogue.

## Ressources

- Documentation — https://docs.databricks.com/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Apache Iceberg]] — le format de table concurrent de Delta Lake
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
