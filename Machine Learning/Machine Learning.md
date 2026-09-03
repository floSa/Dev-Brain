---
role: hub
nom: Machine Learning
alias: [ML, apprentissage automatique]
pitch: Apprendre une fonction à partir de données — la cadrer, l'entraîner, mesurer ce qu'elle vaut, puis la tenir en production.
domaines: [data-sci, ml-eng, mlops]
tags: [supervised, unsupervised, model-evaluation, feature-engineering, hyperparameter-tuning, ml-pipeline, model-monitoring, explainability, ensemble, clustering]
---

# Machine Learning

> Apprendre une fonction à partir de données — la cadrer, l'entraîner, mesurer ce qu'elle vaut, puis la tenir en production.

## Ce qu'il faut comprendre

- **Les sous-dossiers ne découpent pas le sujet, ils rangent des pages** — et le critère est la `categorie:` de la page, pas la matière dont elle traite. Les noms se recouvrent donc en langue courante : un modèle de vision *est* un modèle profond, une bibliothèque de séries temporelles *fait* de la régression. Ce que chaque dossier est réellement : [[Socle]] ce qui **ne suppose rien de la donnée** — cadrer le problème, puis la boîte classique qui le résout ; [[Apprentissage profond]] le **réseau lui-même** — architecture, optimisation, échelle, compression, et les socles qui l'exécutent — pas tout ce qui est profond ; [[Vision]] ce qu'on **fait d'une image**, tâches et bibliothèques ; [[NLP]] celles dont l'entrée est du **texte** hors génération — un LLM n'est pas ici, il est dans [[LLM & IA générative]] ; [[Séries temporelles]] celles dont l'entrée est **indexée par le temps** ; [[Apprentissage par renforcement]] ce qui apprend **par interaction** plutôt que sur un jeu figé ; [[Tabulaire]] ce qui travaille des **colonnes** ; [[Serving]] ce qui **expose** un modèle déjà entraîné ; [[Suivi d'expériences]] ce qui **enregistre** les entraînements ; [[Interprétabilité]] ce qui **explique** une prédiction ; [[Évaluation de modèles]] ce qui **mesure** ce qu'elle vaut ; [[Non supervisé]] ce qui cherche une structure **sans cible**. Ce qui reste au niveau du domaine est ce qui **traverse** les autres : l'orchestration, l'optimisation d'hyperparamètres, le monitoring, le feature store, les embeddings, le hub de modèles.
- **Trois régimes d'apprentissage**, et le premier tri se fait là. [[Apprentissage supervisé]] dispose d'une cible annotée et se juge sur une erreur mesurable ; [[Apprentissage non supervisé]] n'en a pas et se juge sur une structure qu'il faut interpréter, donc bien plus difficilement ; [[Reinforcement learning]] n'a ni cible ni jeu figé, seulement un signal de récompense obtenu en agissant. Passer du premier au deuxième change la nature de la preuve, pas seulement l'algorithme.
- **Le premier choix n'est pas l'algorithme, c'est le cadrage.** [[Types de données et choix de modèle]] pose la question dans le bon ordre — quelle est la variable cible, à quelle granularité, avec quelles données disponibles *au moment de la prédiction*. [[Classification]], [[Régression]], [[Régression et classification multi-sorties]] et [[Systèmes de recommandation]] ne sont pas des familles d'algorithmes mais des formes de problème, et un cadrage faux ne se rattrape par aucun modèle.
- **Sur données tabulaires, le gradient boosting reste l'état de l'art** — c'est le fait le plus utile du domaine, et il tient depuis dix ans. [[Arbres de décision]] en est la brique élémentaire ; [[Bagging]] et [[Random Forest]] réduisent la variance en moyennant, [[Extra Trees]] pousse la randomisation plus loin ; [[Boosting]], [[AdaBoost]] et [[Gradient Boosting (GBDT)]] réduisent le biais en corrigeant séquentiellement. [[Ensembling]] est la généralisation des deux. Le deep learning ne les bat pas sur ce terrain, il coûte simplement plus cher.
- **Les modèles simples ne sont pas des modèles pauvres** : ils sont interprétables, calibrés et rapides à réentraîner. [[Régression linéaire]] et [[Régression logistique]] restent la référence de comparaison obligatoire ; [[GLM]] les étend aux lois non gaussiennes, [[GAM]] à la non-linéarité lisible, [[Régression quantile]] à la prédiction d'un intervalle plutôt que d'une moyenne. [[Régularisation]] est ce qui les rend utilisables en grande dimension. [[Naive Bayes]], [[k-NN]], [[Analyse discriminante]], [[SVM]], [[Gaussian Process]] et [[Perceptron et MLP]] complètent la boîte classique.
- **La mesure décide de tout, et c'est là que la plupart des projets échouent.** [[Compromis biais-variance]] explique pourquoi une erreur d'entraînement basse ne prouve rien ; [[Validation croisée]] est le protocole qui donne un chiffre honnête, [[Data leakage]] la façon la plus courante de le rendre faux sans s'en apercevoir. Choisir la métrique est un acte métier : [[Classification metrics]], [[Regression metrics]], [[Ranking metrics]], [[ROC-AUC & courbe PR]]. Deux pièges méritent leur propre page — [[Calibration]], parce qu'un score n'est pas une probabilité tant qu'on ne l'a pas vérifié, et [[Imbalanced classification]], où l'exactitude est trompeuse par construction.
- **La préparation des données pèse plus lourd que le choix du modèle.** [[EDA automatisée & profiling]] pour la première passe — elle est rangée dans [[Data & pipelines]] avec son outillage, parce qu'elle décrit un jeu de données et non un modèle —, puis [[Ingénierie des caractéristiques]], [[Encodage des variables catégorielles]], [[Mise à l'échelle]], [[Sélection de variables]]. Les valeurs manquantes se traitent en deux temps : comprendre d'abord les [[Mécanismes de données manquantes]] — pourquoi elles manquent conditionne ce qu'on a le droit d'en faire — puis [[Imputation des valeurs manquantes]].
- **Sans cible, la validation n'existe plus** : c'est ce qui rend le non-supervisé exigeant. [[Clustering]] pose le cadre, [[K-Means]] et [[k-médoïds (PAM)]] partitionnent, [[DBSCAN]] et [[Clustering hiérarchique par densité]] trouvent des formes quelconques et laissent du bruit dehors, [[Classification hiérarchique (CAH)]] produit un arbre plutôt qu'une partition, [[Gaussian Mixture Models (GMM)]] une affectation probabiliste. [[Clustering evaluation]] est la page à lire avant d'annoncer un résultat.
- **Réduire la dimension sert à deux choses opposées** — visualiser, ou compresser avant un modèle — et les outils ne sont pas interchangeables. [[t-SNE and UMAP]] préservent le voisinage local et servent à voir, pas à alimenter un classifieur ; [[ICA]] sépare des sources, [[NMF]] impose la positivité et donne des parties additives. Les [[embeddings]] sont la version apprise du même problème.
- **La détection d'anomalies est un problème de définition avant d'être un problème d'algorithme.** [[Détection d'outliers univariée]] et [[Détection d'outliers multivariée]] ne visent pas la même chose ; [[Isolation Forest]], [[Local Outlier Factor]] et [[One-Class SVM]] traduisent trois hypothèses différentes sur ce qu'« anormal » veut dire.
- **Un modèle en production est un système, pas un fichier.** [[Déploiement de modèles]] et [[Model registry & versioning]] posent la traçabilité, [[Monitoring de modèle en production]] et [[Data drift]] la surveillance — un modèle ne tombe pas en panne, il se dégrade en silence. [[Feature store — concept]] règle le décalage entre les features d'entraînement et celles servies à l'inférence. [[Explicabilité des modèles]] est ce qu'on doit au métier, [[Optimisation d'hyperparamètres]] ce qu'on doit au modèle.

## Choisir

- Cadrer le problème avant de choisir un modèle, puis un premier modèle quelle que soit la famille → [[Socle]] et [[Scikit-Learn]] ; il reste la référence à battre avant d'ouvrir autre chose.
- Des colonnes et une cible → [[Tabulaire]] : [[XGBoost]], [[LightGBM]] ou [[CatBoost]] selon les variables catégorielles et le volume.
- Entraîner un réseau de neurones → [[Apprentissage profond]].
- Des images en entrée → [[Vision]] ; du texte à classer, extraire ou rechercher sans génération → [[NLP]] ; une série indexée par le temps → [[Séries temporelles]].
- Un agent qui apprend en agissant → [[Apprentissage par renforcement]].
- Aucune cible : regrouper, projeter, détecter l'anormal → [[Non supervisé]].
- Exposer un modèle entraîné derrière une API → [[Serving]].
- Savoir quel entraînement a produit quel modèle → [[Suivi d'expériences]].
- Expliquer une prédiction au métier ou au régulateur → [[Interprétabilité]].
- Savoir si un score de validation est honnête, et choisir la bonne métrique → [[Évaluation de modèles]].
- Chercher des hyperparamètres → [[Optuna]] par défaut, [[Ray Tune]] si la recherche doit être distribuée, [[Hyperopt]] pour un existant à maintenir. Cf. [[Comparatif - Optimisation d'hyperparamètres]].
- Orchestrer un pipeline d'entraînement reproductible → [[ZenML]] pour rester agnostique de l'infra, [[Metaflow]] pour un chemin balisé du notebook à la production, [[Flyte]] si Kubernetes est déjà le socle. Cf. [[Comparatif - Orchestrateurs ML]].
- Surveiller un modèle en production → [[Evidently]] ; servir les mêmes features à l'entraînement et à l'inférence → [[Feast]].
- Apprendre en flux, sur une donnée qui n'entre pas en mémoire → [[River]].
- Visualiser un nuage en deux dimensions → [[umap-learn]] ou [[PaCMAP]], dans [[Non supervisé]] ; regrouper sans fixer le nombre de groupes → [[hdbscan]]. Cf. [[Comparatif - Réduction de dimension]], qui reste ici parce que ses membres enjambent trois dossiers.
- Détecter des anomalies sur du tabulaire → [[PyOD]], dans [[Non supervisé]] ; sur une série temporelle → [[STUMPY]]. Cf. [[Comparatif - Détection d'anomalies]].
- Un graphe en entrée → [[PyTorch Geometric]].
- Représenter des phrases par des vecteurs → [[sentence-transformers]] ; charger un jeu de données public → [[datasets]] ; calculer une métrique standard → [[evaluate]], ou [[seqeval]] pour l'étiquetage de séquence.
- Récupérer un modèle ou un jeu de données déjà publié → [[HuggingFace]].
- Faire générer du texte, du code ou une image par un modèle de fondation → [[LLM & IA générative]], pas ce domaine.

<!-- AUTO:START -->
### Sous-domaines
- [[Apprentissage par renforcement]] · [[Apprentissage profond]] · [[Interprétabilité]] · [[NLP]] · [[Non supervisé]] · [[Serving]] · [[Socle]] · [[Suivi d'expériences]] · [[Séries temporelles]] · [[Tabulaire]] · [[Vision]] · [[Évaluation de modèles]]

### Notions
- [[Data drift]] — domaines : mlops, data-sci
- [[embeddings]] — domaines : data-sci, ai-eng
- [[Feature store — concept]] — domaines : mlops, data-eng
- [[Monitoring de modèle en production]] — domaines : mlops
- [[Optimisation d'hyperparamètres]] — domaines : data-sci, ml-eng

### Briques
- [[datasets]] — Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub.
- [[Evidently]] — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.
- [[Feast]] — Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…).
- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.
- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes.
- [[Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.
- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- [[Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[PyTorch Geometric]] — Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN.
- [[Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.
- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi.
- [[ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.

### Comparatifs
- [[Comparatif - Détection d'anomalies]]
- [[Comparatif - Optimisation d'hyperparamètres]]
- [[Comparatif - Orchestrateurs ML]]
- [[Comparatif - Réduction de dimension]]
<!-- AUTO:END -->

## Notes
