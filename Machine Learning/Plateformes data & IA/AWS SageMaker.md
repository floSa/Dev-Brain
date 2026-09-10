---
role: brique
nom: AWS SageMaker
alias: [SageMaker, Amazon SageMaker, SageMaker AI, SageMaker Unified Studio]
pitch: "Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts."
categorie: ml/plateforme
famille: saas
domaines: [mlops, ml-eng, data-sci]
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Google Cloud Vertex AI]]", "[[Microsoft Azure Machine Learning]]", "[[Dataiku]]", "[[Databricks]]", "[[DataRobot]]"]
complements: []
tags: [ml-platform, model-serving, model-registry, ml-pipeline, automl, distributed]
url_docs: https://docs.aws.amazon.com/sagemaker/
url_repo: 
---

# AWS SageMaker

<!-- AUTO:BANDEAU:START -->
> Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

L'écosystème de machine learning d'AWS, c'est-à-dire un ensemble de services managés plutôt
qu'un produit unique : environnements de travail et notebooks, entraînement distribué sur des
instances louées à la minute, réglage d'hyperparamètres, registre de modèles, pipelines, et
endpoints d'inférence avec leur mise à l'échelle. Depuis 2025, **SageMaker Unified Studio**
réunit ces briques avec les services data d'AWS — Glue, Athena, EMR, Redshift, Bedrock — dans
une console commune. L'exécution sur site est possible, mais par **Outposts** : des baies
AWS livrées et exploitées par AWS dans la salle machine du client, ce qui n'est pas de
l'auto-hébergement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le client est déjà sur AWS : identités, réseau et stockage sont en place et se réutilisent | **Un compte AWS reste obligatoire**, Outposts compris : il n'existe pas d'installation sur du matériel qu'on possède |
| Il faut de l'entraînement distribué ou des GPU à la demande, sans acheter de machines | La surface est **large et morcelée** : le nombre de services et leur imbrication rendent le démarrage lent |
| L'inférence doit rester sur site pour des raisons juridictionnelles, avec le reste dans la région | Le coût suit l'usage, et un endpoint laissé en service se paie même inactif |
| L'organisation veut un seul fournisseur pour la donnée et le ML | Une équipe qui refuse l'enfermement chez un fournisseur → [[ZenML]] ou [[Metaflow]], portables |
| Les compétences AWS existent déjà dans l'équipe | Des analystes métier sans code, à rendre autonomes → [[Dataiku]] ou [[Alteryx]] |

## Mise en œuvre

- Installation — rien à installer : des services activés dans un compte AWS
- Point d'entrée — la console SageMaker Unified Studio, le SDK Python et l'API AWS
- Prérequis — un compte AWS, et une politique d'identités et de réseau tenue ; Outposts pour toute exécution sur site
- Exécution — managé, distribué ; instances d'entraînement et endpoints dimensionnés à la charge
- Coût — à l'usage, à la seconde d'instance ; Outposts se contracte à part, sur engagement

## Écosystème

### Alternatives

- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud. — l'équivalent chez Google, avec l'accès direct aux modèles Gemini.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc. — l'équivalent chez Microsoft, et le seul des trois à tourner sur le matériel du client.
- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — la suite indépendante du cloud, installable sur site.
- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — la couche unique posée par-dessus le cloud plutôt que le natif du fournisseur.
- [[DataRobot]] — Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée. — plus automatisé sur la modélisation, et installable chez le client.

## Ressources

- Documentation — https://docs.aws.amazon.com/sagemaker/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
