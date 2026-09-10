---
role: hub
nom: Plateformes data & IA
alias: [plateformes ML, plateformes de données et d'IA, suites data science]
pitch: "Les suites qui couvrent tout le cycle sous une console unique — et la question qu'elles posent toutes : sur quel matériel, et à quel prix de sortie."
domaines: [data-sci, data-eng, mlops, ml-eng]
tags: [ml-platform, automl, data-governance, low-code, lakehouse]
---

# Plateformes data & IA

> Les suites qui couvrent tout le cycle sous une console unique — et la question qu'elles posent toutes : sur quel matériel, et à quel prix de sortie.

## Ce qu'il faut comprendre

- **Ce dossier ne range pas des outils, il range des socles.** Une brique d'ailleurs dans l'arbre résout une étape : [[Optuna]] cherche des hyperparamètres, [[MLflow]] enregistre des entraînements, [[KServe]] expose un modèle. Une page d'ici prétend faire les quatre étapes — préparation des données, entraînement, déploiement, gouvernance — et les vendre ensemble. C'est cette prétention, et non la technologie, qui définit la valeur `ml/plateforme` (règle D-R9 de la taxonomie).
- **La confusion voisine est avec [[Machine Learning]] au niveau du domaine**, où vivent [[ZenML]], [[Metaflow]] et [[Flyte]]. Ceux-là décrivent un **pipeline** et laissent dehors l'infrastructure, le catalogue et les droits — ZenML l'écrit lui-même, « il n'exécute rien lui-même ». Une plateforme, au contraire, apporte le calcul avec elle. Le choix entre les deux familles n'est pas technique : c'est le choix entre assembler et acheter.
- **Le premier tri est le matériel, et c'est le seul qui ne se rattrape pas.** Trois de ces huit s'installent sur des serveurs qu'on possède : [[Dataiku]], [[DataRobot]] et [[Alteryx]]. Les cinq autres exigent un compte chez un fournisseur, et le code comme les données vivent alors chez lui. Pour un industriel dont les données ne sortent pas du site, la liste tombe à trois avant même qu'on parle de fonctionnalités.
- **« Sur site » ne veut pas dire la même chose chez les trois clouds**, et la nuance décide de projets entiers. [[Microsoft Azure Machine Learning]] fait tourner entraînement et inférence sur un **Kubernetes déjà en place**, par Azure Arc — le matériel est celui du client. [[AWS SageMaker]] descend sur site avec **Outposts**, c'est-à-dire des baies AWS louées et posées dans la salle machine. [[Google Cloud Vertex AI]] n'en descend qu'une **partie**, sur l'appliance air-gapped de Google Distributed Cloud. Dans les trois cas le plan de contrôle reste chez le fournisseur.
- **L'enfermement se mesure à la sortie, pas à l'entrée.** Ce qui coûte cher à quitter n'est jamais l'interface : ce sont les formats propriétaires, les fonctions SQL maison, les recettes visuelles qui n'existent que là, et le catalogue de droits qu'il faudra rebâtir. Une plateforme qui exécute du Python standard et écrit dans un format ouvert se quitte ; une qui ne s'exprime qu'en flux visuels ne se quitte pas sans tout réécrire.
- **[[Snowflake]] est ici et non dans [[Bases de données]]**, alors que c'est un entrepôt. Le motif est écrit dans la taxonomie (règle D-R8) : son concurrent réel en clientèle est [[Databricks]], pas un autre moteur, et Snowpark, Cortex et Snowflake ML exécutent désormais code et modèles dans le moteur. Le rangement dit où l'on cherche une page ; les liens disent à quoi elle ressemble, et Snowflake reste câblé à [[ClickHouse]] et [[DuckDB]].
- **La couche sans code n'est pas un gadget, c'est le modèle économique.** [[Alteryx]] et [[Dataiku]] la mettent au premier plan parce que leurs acheteurs sont des analystes métier, pas des développeurs. Elle achète l'autonomie de gens qui n'écriront jamais de Python, et elle coûte la revue de code : un flux visuel se relit mal, se teste mal et se versionne mal.
- **Aucune de ces huit n'a de dépôt public**, et c'est pourquoi la colonne *Fraîcheur* de leur bandeau reste muette : la sonde d'amont n'a rien à interroger. L'absence d'amont est ici une propriété du produit, pas un défaut de la fiche.

## Choisir

- Les données ne sortent pas du site, et l'équipe mêle profils techniques et métier → [[Dataiku]].
- Les données ne sortent pas du site, et le besoin est de produire vite beaucoup de modèles supervisés → [[DataRobot]].
- Des analystes métier, des flux de préparation à reprendre, pas de Python dans l'équipe → [[Alteryx]].
- Gros volumes, data engineering en code, architecture lakehouse assumée → [[Databricks]].
- L'entrepôt SQL est déjà le centre de gravité, et l'IA doit venir à lui → [[Snowflake]].
- Le client est déjà sur un cloud et n'en sortira pas → l'écosystème natif : [[AWS SageMaker]], [[Google Cloud Vertex AI]] ou [[Microsoft Azure Machine Learning]].
- Un cluster Kubernetes existe sur site et doit porter le calcul, sans que le plan de contrôle soit à opérer → [[Microsoft Azure Machine Learning]] par Azure Arc, seul des trois à le faire.
- Comparer les huit sur le seul critère qui tranche vraiment → [[Comparatif - Plateformes data & IA]].
- Comprendre ce qu'une plateforme intègre avant d'en choisir une → [[Plateforme data & IA — concept]].
- Assembler plutôt qu'acheter, en gardant la main sur chaque brique → [[ZenML]], [[Metaflow]] ou [[Flyte]], au niveau du domaine, et [[Comparatif - Orchestrateurs ML]].

<!-- AUTO:START -->
### Notions
- [[Plateforme data & IA — concept]] — domaines : data-sci, data-eng, mlops, ml-eng

### Briques
- [[Alteryx]] — Préparation, enrichissement et analyse de données en flux visuels sans code, pour analystes métier : Designer sur poste Windows, Server pour publier et planifier, Analytics Cloud pour la version managée.
- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts.
- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement.
- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits.
- [[DataRobot]] — Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée.
- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc.
- [[Snowflake]] — Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement.

### Comparatifs
- [[Comparatif - Plateformes data & IA]]
<!-- AUTO:END -->

## Notes
