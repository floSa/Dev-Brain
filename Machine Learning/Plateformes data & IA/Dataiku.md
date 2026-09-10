---
role: brique
nom: Dataiku
alias: [dataiku, DSS, Dataiku DSS]
pitch: "Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits."
categorie: ml/plateforme
famille: plateforme
domaines: [data-sci, data-eng, mlops]
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Databricks]]", "[[DataRobot]]", "[[Alteryx]]", "[[AWS SageMaker]]", "[[Google Cloud Vertex AI]]", "[[Microsoft Azure Machine Learning]]"]
complements: []
tags: [ml-platform, low-code, data-governance, automl, ml-pipeline, self-hosted]
url_docs: https://doc.dataiku.com/dss/latest/
url_repo: 
---

# Dataiku

<!-- AUTO:BANDEAU:START -->
> Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme | propriétaire | self-hébergé ou managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme collaborative qui réunit sur un même projet la préparation des données, la
modélisation, le déploiement et la gouvernance. Sa particularité est de servir **deux publics
sur les mêmes objets** : un analyste enchaîne des recettes visuelles, un data scientist ouvre
un notebook Python, R ou SQL au milieu du même flux, et les deux voient le même graphe de
dépendances. Le serveur s'installe sur des machines qu'on possède — c'est l'installation
historique, sur Linux — et délègue les calculs lourds à un Kubernetes ou à un moteur SQL
externe. Une édition managée, Dataiku Cloud, existe à côté. La licence se compte par
utilisateur et par nœud, ce qui fait croître la facture avec la taille de l'équipe.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les données ne doivent pas quitter le site, et il faut malgré tout une plateforme complète | Le produit est **propriétaire et facturé par utilisateur** : le coût croît avec l'équipe, pas avec l'usage |
| Une équipe mixte — analystes métier et profils Python — doit travailler sur les mêmes projets | Les recettes visuelles sont un **format maison** : ce qui est construit en clic ne se rejoue pas hors de la plateforme |
| Il faut une traçabilité de bout en bout : lignage, droits par rôle, journal des déploiements | Une équipe entièrement Python qui veut garder la main sur chaque brique → [[ZenML]] ou [[Metaflow]] |
| L'organisation veut industrialiser sans monter une équipe plateforme | Le besoin est le traitement de très gros volumes en code, pas la collaboration → [[Databricks]] |
| Le calcul doit être délégué à un Kubernetes ou à un entrepôt déjà en place | Le besoin se réduit à produire beaucoup de modèles supervisés vite → [[DataRobot]] |

## Mise en œuvre

- Installation — paquet sur un serveur Linux, ou déploiement Kubernetes ; édition managée Dataiku Cloud
- Point d'entrée — l'interface web du projet : recettes visuelles, notebooks et code sur le même flux
- Prérequis — un serveur dédié dimensionné pour le service, et un moteur de calcul externe (Kubernetes, Spark ou base SQL) dès que les volumes dépassent le nœud
- Exécution — self-hébergé ou managé ; les traitements sont poussés vers le moteur choisi
- Coût — licence commerciale, tarification par utilisateur et par nœud ; une édition gratuite limitée existe pour découvrir

## Écosystème

### Alternatives

- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — l'autre grande suite, mais en code et sans installation sur site.
- [[DataRobot]] — Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée. — même liberté d'hébergement, périmètre plus étroit et plus automatisé.
- [[Alteryx]] — Préparation, enrichissement et analyse de données en flux visuels sans code, pour analystes métier : Designer sur poste Windows, Server pour publier et planifier, Analytics Cloud pour la version managée. — le concurrent sur le terrain visuel, sans la moitié data science.
- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts. — l'option native si le client est déjà chez AWS.
- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud. — idem chez Google.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc. — idem chez Microsoft, avec une vraie option sur site.

## Ressources

- Documentation — https://doc.dataiku.com/dss/latest/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
