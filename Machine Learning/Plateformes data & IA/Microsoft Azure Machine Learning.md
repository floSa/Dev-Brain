---
role: brique
nom: Microsoft Azure Machine Learning
alias: [Azure ML, azure-ml, Azure Machine Learning, AzureML]
pitch: "Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc."
categorie: ml/plateforme
famille: saas
domaines: [mlops, ml-eng, data-sci]
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[AWS SageMaker]]", "[[Google Cloud Vertex AI]]", "[[Dataiku]]", "[[Databricks]]", "[[DataRobot]]"]
complements: []
tags: [ml-platform, model-serving, model-registry, ml-pipeline, automl, kubernetes]
url_docs: https://learn.microsoft.com/azure/machine-learning/
url_repo: 
---

# Microsoft Azure Machine Learning

<!-- AUTO:BANDEAU:START -->
> Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

L'écosystème de machine learning d'Azure, organisé autour d'un **espace de travail** qui
rassemble jeux de données, calculs, expériences, registre de modèles et endpoints. Tout s'y
pilote de trois façons interchangeables : l'interface, le SDK Python, ou des fichiers YAML
passés à la ligne de commande — ce dernier point en fait la plus déclarative des trois offres
cloud. Sa singularité opérationnelle est **Azure Arc** : une extension installée sur
n'importe quel cluster Kubernetes conforme, y compris sur le matériel du client, permet d'y
exécuter entraînement et inférence pilotés depuis Azure. Le plan de contrôle, lui, reste dans
Azure, et un abonnement demeure obligatoire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un cluster Kubernetes existe déjà sur site et doit porter le calcul, sans plan de contrôle à opérer | **Le plan de contrôle reste dans Azure** : l'abonnement est obligatoire, et l'isolement complet du site n'est pas atteignable |
| Le client est un compte Microsoft : annuaire, réseau et gouvernance déjà en place | La sortie sortante vers Azure doit être ouverte et tenue, proxy compris, ce qui se négocie avec la sécurité du client |
| L'infrastructure doit se décrire en YAML versionné plutôt qu'en clics | Le besoin est un déploiement entièrement souverain, sans lien avec un fournisseur → [[Dataiku]] ou [[DataRobot]] |
| Le projet est réparti entre le site industriel et le cloud, sur les mêmes définitions | Une équipe qui veut rester portable entre fournisseurs → [[ZenML]] ou [[Metaflow]] |
| L'organisation veut un seul fournisseur pour la donnée et le ML | Des analystes métier sans code, à rendre autonomes → [[Alteryx]] |

## Mise en œuvre

- Installation — un espace de travail créé dans un abonnement Azure ; pour le calcul sur site, l'extension Azure Machine Learning déployée sur un cluster Kubernetes attaché par Azure Arc
- Point d'entrée — le studio web, le SDK Python, ou des définitions YAML passées à la CLI
- Prérequis — un abonnement Azure ; pour le mode Arc, un cluster Kubernetes conforme et une connexion sortante vers Azure, proxy accepté
- Exécution — managé, distribué ; le calcul peut être déporté sur le cluster du client sans changer les définitions
- Coût — à l'usage pour le calcul et les endpoints ; en mode Arc, le matériel est celui du client et seul le plan de contrôle est facturé par Azure

## Écosystème

### Alternatives

- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts. — l'équivalent chez AWS, dont la descente sur site passe par du matériel loué à AWS.
- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud. — l'équivalent chez Google, avec l'accès direct aux modèles Gemini.
- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — la suite indépendante du cloud, dont le plan de contrôle lui-même s'installe sur site.
- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — la couche unique posée par-dessus le cloud, dont Azure propose une édition intégrée.
- [[DataRobot]] — Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée. — même socle Kubernetes, mais installé en entier chez le client.

## Ressources

- Documentation — https://learn.microsoft.com/azure/machine-learning/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
