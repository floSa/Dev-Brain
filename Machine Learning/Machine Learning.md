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

- **Les sous-dossiers ne découpent pas le sujet, ils rangent des pages** — et le critère est la `categorie:` de la page, pas la matière dont elle traite. Les noms se recouvrent donc en langue courante : un modèle de vision *est* un modèle profond, une bibliothèque de séries temporelles *fait* de la régression. Ce que chaque dossier est réellement : [[Socle]] ce qui **ne suppose rien de la donnée** — cadrer le problème, puis la boîte classique qui le résout ; [[Apprentissage profond]] le **réseau lui-même** — architecture, optimisation, échelle, compression, et les socles qui l'exécutent — pas tout ce qui est profond ; [[Vision]] ce qu'on **fait d'une image**, tâches et bibliothèques ; [[NLP]] celles dont l'entrée est du **texte** hors génération — un LLM n'est pas ici, il est dans [[LLM & IA générative]] ; [[Séries temporelles]] celles dont l'entrée est **indexée par le temps** ; [[Apprentissage par renforcement]] ce qui apprend **par interaction** plutôt que sur un jeu figé ; [[Tabulaire]] ce qui travaille des **colonnes** ; [[Serving]] ce qui **expose** un modèle déjà entraîné ; [[Suivi d'expériences]] ce qui **enregistre** les entraînements ; [[Interprétabilité]] ce qui **explique** une prédiction ; [[Monitoring de modèles]] ce qui **surveille** un modèle déployé — dérive, performance sans étiquettes, tests avant mise en production ; [[Évaluation de modèles]] ce qui **mesure** ce qu'elle vaut ; [[Non supervisé]] ce qui cherche une structure **sans cible** ; [[Embeddings & encodeurs]] ce qui **produit des vecteurs** — bibliothèques, serveurs et modèles d'embedding, sans les stocker ; [[Recherche d'hyperparamètres]] ce qui **règle** un modèle en connaissant le coût d'un essai — optimisation bayésienne, arrêt précoce, et les bibliothèques qui les exécutent ; [[Plateformes data & IA]] les **suites commerciales** qui prétendent couvrir tout le cycle à elles seules — préparation, entraînement, déploiement, gouvernance — et qui se choisissent d'abord sur le lieu où tournent les données. Ce qui reste au niveau du domaine est ce qui **traverse** les autres : l'orchestration, le feature store, le hub de modèles.
- **Trois régimes d'apprentissage**, et le premier tri se fait là. [[Apprentissage supervisé]] dispose d'une cible annotée et se juge sur une erreur mesurable ; [[Apprentissage non supervisé]] n'en a pas et se juge sur une structure qu'il faut interpréter, donc bien plus difficilement ; [[Reinforcement learning]] n'a ni cible ni jeu figé, seulement un signal de récompense obtenu en agissant. Passer du premier au deuxième change la nature de la preuve, pas seulement l'algorithme.
- **Le premier choix n'est pas l'algorithme, c'est le cadrage.** [[Types de données et choix de modèle]] pose la question dans le bon ordre — quelle est la variable cible, à quelle granularité, avec quelles données disponibles *au moment de la prédiction*. [[Classification]], [[Régression]], [[Régression et classification multi-sorties]] et [[Systèmes de recommandation]] ne sont pas des familles d'algorithmes mais des formes de problème, et un cadrage faux ne se rattrape par aucun modèle.
- **Sur données tabulaires, le gradient boosting reste l'état de l'art** — c'est le fait le plus utile du domaine, et il tient depuis dix ans. [[Arbres de décision]] en est la brique élémentaire ; [[Bagging]] et [[Random Forest]] réduisent la variance en moyennant, [[Extra Trees]] pousse la randomisation plus loin ; [[Boosting]], [[AdaBoost]] et [[Gradient Boosting (GBDT)]] réduisent le biais en corrigeant séquentiellement. [[Ensembling]] est la généralisation des deux. Le deep learning ne les bat pas sur ce terrain, il coûte simplement plus cher.
- **Les modèles simples ne sont pas des modèles pauvres** : ils sont interprétables, calibrés et rapides à réentraîner. [[Régression linéaire]] et [[Régression logistique]] restent la référence de comparaison obligatoire ; [[GLM]] les étend aux lois non gaussiennes, [[GAM]] à la non-linéarité lisible, [[Régression quantile]] à la prédiction d'un intervalle plutôt que d'une moyenne. [[Régularisation]] est ce qui les rend utilisables en grande dimension. [[Naive Bayes]], [[k-NN]], [[Analyse discriminante]], [[SVM]], [[Gaussian Process]] et [[Perceptron et MLP]] complètent la boîte classique.
- **La mesure décide de tout, et c'est là que la plupart des projets échouent.** [[Compromis biais-variance]] explique pourquoi une erreur d'entraînement basse ne prouve rien ; [[Validation croisée]] est le protocole qui donne un chiffre honnête, [[Data leakage]] la façon la plus courante de le rendre faux sans s'en apercevoir. Choisir la métrique est un acte métier : [[Classification metrics]], [[Regression metrics]], [[Ranking metrics]], [[ROC-AUC & courbe PR]]. Deux pièges méritent leur propre page — [[Calibration]], parce qu'un score n'est pas une probabilité tant qu'on ne l'a pas vérifié, et [[Imbalanced classification]], où l'exactitude est trompeuse par construction.
- **La préparation des données pèse plus lourd que le choix du modèle.** [[EDA automatisée & profiling]] pour la première passe — elle est rangée dans [[Data & pipelines]] avec son outillage, parce qu'elle décrit un jeu de données et non un modèle —, puis [[Ingénierie des caractéristiques]], [[Encodage des variables catégorielles]], [[Mise à l'échelle]], [[Sélection de variables]]. Les valeurs manquantes se traitent en deux temps : comprendre d'abord les [[Mécanismes de données manquantes]] — pourquoi elles manquent conditionne ce qu'on a le droit d'en faire — puis [[Imputation des valeurs manquantes]].
- **Sans cible, la validation n'existe plus** : c'est ce qui rend le non-supervisé exigeant. [[Clustering]] pose le cadre, [[K-Means]] et [[k-médoïds (PAM)]] partitionnent, [[DBSCAN]] et [[Clustering hiérarchique par densité]] trouvent des formes quelconques et laissent du bruit dehors, [[Classification hiérarchique (CAH)]] produit un arbre plutôt qu'une partition, [[Gaussian Mixture Models (GMM)]] une affectation probabiliste. [[Clustering evaluation]] est la page à lire avant d'annoncer un résultat.
- **Réduire la dimension sert à deux choses opposées** — visualiser, ou compresser avant un modèle — et les outils ne sont pas interchangeables. [[t-SNE and UMAP]] préservent le voisinage local et servent à voir, pas à alimenter un classifieur ; [[ICA]] sépare des sources, [[NMF]] impose la positivité et donne des parties additives. Les [[embeddings]] sont la version apprise du même problème.
- **La détection d'anomalies est un problème de définition avant d'être un problème d'algorithme.** [[Détection d'outliers univariée]] et [[Détection d'outliers multivariée]] ne visent pas la même chose ; [[Isolation Forest]], [[Local Outlier Factor]] et [[One-Class SVM]] traduisent trois hypothèses différentes sur ce qu'« anormal » veut dire.
- **Un modèle en production est un système, pas un fichier.** [[Déploiement de modèles]] et [[Model registry & versioning]] posent la traçabilité, [[CI-CD pour le ML]] ce qui change dans le pipeline qui les enchaîne, [[Monitoring de modèle en production]] et [[Data drift]] la surveillance, outillée dans [[Monitoring de modèles]] — un modèle ne tombe pas en panne, il se dégrade en silence. [[Feature store — concept]] règle le décalage entre les features d'entraînement et celles servies à l'inférence. [[Explicabilité des modèles]] est ce qu'on doit au métier, [[Optimisation d'hyperparamètres]] ce qu'on doit au modèle.

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
- Chercher des hyperparamètres → [[Optuna]] par défaut, [[Ray Tune]] si la recherche doit être distribuée, [[Hyperopt]] pour un existant à maintenir. Cf. [[Comparatif - Optimisation d'hyperparamètres]] ; comprendre quand un substitut bayésien vaut mieux que le hasard → [[Optimisation bayésienne]].
- Orchestrer un pipeline d'entraînement reproductible → [[ZenML]] pour rester agnostique de l'infra, [[Metaflow]] pour un chemin balisé du notebook à la production, [[Flyte]] si Kubernetes est déjà le socle. Cf. [[Comparatif - Orchestrateurs ML]].
- Acheter une suite entière plutôt que d'assembler ces briques — parce qu'il faut une console, un catalogue et des droits communs, et personne pour tenir une plateforme → [[Plateformes data & IA]]. Le tri s'y fait d'abord sur l'hébergement : [[Dataiku]], [[DataRobot]] et [[Alteryx]] s'installent sur site, les cinq autres non. Cf. [[Comparatif - Plateformes data & IA]].
- Surveiller un modèle en production → [[Evidently]], le seul des trois outils fichés encore maintenu ; estimer la performance sans étiquettes → [[NannyML]] ; valider avant déploiement → [[Deepchecks]]. Cf. [[Comparatif - Monitoring de modèles]]. Servir les mêmes features à l'entraînement et à l'inférence → [[Feast]].
- Apprendre en flux, sur une donnée qui n'entre pas en mémoire → [[River]].
- Visualiser un nuage en deux dimensions → [[umap-learn]] ou [[PaCMAP]], dans [[Non supervisé]] ; regrouper sans fixer le nombre de groupes → [[hdbscan]]. Cf. [[Comparatif - Réduction de dimension]], descendu dans [[Non supervisé]] au lot 5 : ses membres enjambent trois dossiers, et c'est la `categorie:` de sa page qui décide désormais du sien.
- Détecter des anomalies sur du tabulaire → [[PyOD]], dans [[Non supervisé]] ; sur une série temporelle → [[STUMPY]]. Cf. [[Comparatif - Détection d'anomalies]].
- Un graphe en entrée → [[PyTorch Geometric]].
- Représenter des phrases par des vecteurs → [[sentence-transformers]], et [[Embeddings & encodeurs]] pour choisir le modèle et l'outil qui le sert (cf. [[Comparatif - Embeddings]]) ; charger un jeu de données public → [[datasets]] ; calculer une métrique standard → [[evaluate]], ou [[seqeval]] pour l'étiquetage de séquence.
- Récupérer un modèle ou un jeu de données déjà publié → [[HuggingFace]].
- Étiqueter soi-même des données pour l'apprentissage supervisé, sur des machines sans cloud → [[Annotation de données]] : [[CVAT]] pour les images, la vidéo et le 3D, [[Label Studio]] pour le texte, l'audio, les séries et les images ; rôles, SSO et contrôle qualité automatique sont payants dans les deux.
- Faire générer du texte, du code ou une image par un modèle de fondation → [[LLM & IA générative]], pas ce domaine.
- Peu d'étiquettes et beaucoup de données brutes → [[Apprentissage semi-supervisé]] ; choisir quoi étiqueter → [[Active learning]] ; des données qui ne peuvent pas quitter leur propriétaire → [[Apprentissage fédéré]] ; une garantie formelle de confidentialité → [[Confidentialité différentielle]] (les trois autres sont rangés dans [[Socle]]).
- Un écart de décisions ou d'erreurs entre groupes de personnes → [[Équité et biais algorithmique]], dans [[Évaluation de modèles]].

<!-- AUTO:START -->
### Sous-domaines
- [[Apprentissage par renforcement]] · [[Apprentissage profond]] · [[Embeddings & encodeurs]] · [[Interprétabilité]] · [[Monitoring de modèles]] · [[NLP]] · [[Non supervisé]] · [[Plateformes data & IA]] · [[Recherche d'hyperparamètres]] · [[Serving]] · [[Socle]] · [[Suivi d'expériences]] · [[Séries temporelles]] · [[Tabulaire]] · [[Vision]] · [[Évaluation de modèles]]

### Notions
- [[Active learning]] — domaines : data-sci, ml-eng
- [[Annotation de données]] — domaines : data-sci, ml-eng
- [[CI-CD pour le ML]] — domaines : mlops
- [[Feature store — concept]] — domaines : mlops, data-eng

### Briques
- [[CVAT]] — Outil d'annotation pour la vision — images, vidéo, nuages de points 3D — avec boîtes, polygones, masques, squelettes, cuboïdes et suivi d'objets par interpolation, 27 formats d'export et pré-annotation par fonctions serverless (SAM, YOLOv7, Detectron2) ; MIT, mais SSO, contrôle qualité automatique, analytics et agents sont réservés à l'édition Enterprise.
- [[datasets]] — Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub.
- [[Feast]] — Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…).
- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.
- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes.
- [[Label Studio]] — Plateforme d'annotation web multimodale — images, texte, audio, vidéo, séries temporelles — configurée par un gabarit XML, avec pré-annotation par un backend ML ; l'édition Community est sous Apache-2.0, rôles, SSO SAML, métriques d'accord et boucle d'active learning automatique sont réservés aux éditions payantes.
- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- [[PyTorch Geometric]] — Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN.
- [[ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.

### Comparatifs
- [[Comparatif - Orchestrateurs ML]]
<!-- AUTO:END -->

## Notes
