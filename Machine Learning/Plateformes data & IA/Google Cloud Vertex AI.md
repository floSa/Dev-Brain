---
role: brique
nom: Google Cloud Vertex AI
alias: [Vertex AI, vertex-ai, Vertex, Gemini Enterprise Agent Platform]
pitch: "Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud."
categorie: ml/plateforme
famille: saas
domaines: [mlops, ml-eng, ai-eng]
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[AWS SageMaker]]", "[[Microsoft Azure Machine Learning]]", "[[Dataiku]]", "[[Databricks]]", "[[DataRobot]]"]
complements: []
tags: [ml-platform, model-serving, model-registry, ml-pipeline, automl, llm]
url_docs: https://cloud.google.com/vertex-ai/docs
url_repo: 
---

# Google Cloud Vertex AI

<!-- AUTO:BANDEAU:START -->
> Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

L'écosystème de machine learning de Google Cloud, réuni sous une console unique :
entraînement managé, réglage, registre de modèles, pipelines, endpoints d'inférence, et
modélisation automatique pour les cas courants. Sa singularité tient à l'accès direct aux
modèles de fondation maison — la famille **Gemini** — servis par la même plateforme que les
modèles entraînés par le client, ce qui en fait autant une porte d'entrée vers l'IA générative
qu'un outil de ML classique. Le produit est en cours de **rebaptême en Gemini Enterprise
Agent Platform**, annoncé à Google Cloud Next '26, la feuille de route passant par cette
nouvelle marque. Sur site, seule une **partie** descend : un jeu restreint d'API pré-entraînées
sur l'appliance air-gapped de Google Distributed Cloud.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le client est déjà sur Google Cloud, avec BigQuery comme centre de gravité de la donnée | **Un compte Google Cloud est obligatoire** ; l'appliance air-gapped ne porte qu'un sous-ensemble d'API pré-entraînées, pas la plateforme |
| Le projet mêle ML classique et modèles de fondation, servis au même endroit | Le produit **change de nom et de contour** : la marque Vertex AI cède la place à Gemini Enterprise Agent Platform, ce qui rend la documentation mouvante |
| L'accès aux modèles Gemini sous contrat d'entreprise est un critère | Le besoin est un déploiement complet et souverain sur du matériel qu'on possède → [[Dataiku]] ou [[DataRobot]] |
| Il faut de l'entraînement distribué et des accélérateurs à la demande | L'organisation est multi-cloud et veut le rester → [[ZenML]], ou [[Databricks]] qui tourne sur les trois |
| L'organisation veut un seul fournisseur pour la donnée et le ML | Des analystes métier sans code, à rendre autonomes → [[Alteryx]] |

## Mise en œuvre

- Installation — rien à installer : des services activés dans un projet Google Cloud
- Point d'entrée — la console Vertex AI, le SDK Python et l'API
- Prérequis — un projet Google Cloud, ses identités et ses quotas ; une appliance Google Distributed Cloud pour le cas air-gapped
- Exécution — managé, distribué ; l'appliance air-gapped est bornée par son matériel, un seul accélérateur par appareil
- Coût — à l'usage : calcul d'entraînement, endpoints servis, et facturation au token pour les modèles de fondation

## Écosystème

### Alternatives

- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts. — l'équivalent chez AWS, avec une descente sur site plus complète.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc. — l'équivalent chez Microsoft, et le seul des trois à tourner sur le matériel du client.
- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — la suite indépendante du cloud, installable sur site.
- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — la couche unique posée par-dessus le cloud, portable entre les trois.
- [[DataRobot]] — Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée. — plus automatisé sur la modélisation, et installable chez le client.

## Ressources

- Documentation — https://cloud.google.com/vertex-ai/docs

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
