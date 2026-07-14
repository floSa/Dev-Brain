---
galaxie: meta
nom: tags
type: gouvernance
created: 2026-06-04
modified: 2026-06-11
tags: [meta, gouvernance, vocabulaire]
---

# Tags — vocabulaire contrôlé

Liste fermée des tags autorisés dans le champ `tags:` du frontmatter (pages Dev et Wiki).

## Règle

- Le skill enrichir-brain **pioche** ses tags ici. Il n'en **invente jamais**.
- Besoin d'un tag absent → le **proposer** à l'utilisateur, l'ajouter ici d'abord, puis l'utiliser.
- Un tag = un concept transverse réutilisable (sujet, technique). Pas une catégorie : la catégorie vit dans le champ `categorie:` (cf. [[taxonomie]]).
- Format : kebab-case, anglais court, au singulier.

## Vocabulaire

| Tag | Sens |
|-----|------|
| `vector-db` | Base de données vectorielle (stockage + recherche ANN) |
| `rag` | Retrieval-Augmented Generation |
| `embeddings` | Représentations vectorielles denses |
| `semantic-search` | Recherche par similarité de sens |
| `hybrid-search` | Combinaison recherche dense + lexicale (BM25) |
| `ann` | Approximate Nearest Neighbor (HNSW, IVF…) |
| `postgres` | Écosystème PostgreSQL |
| `relational` | Base relationnelle (SQL, ACID) |
| `nosql` | Base non-relationnelle |
| `document-db` | Stockage orienté documents (JSON) |
| `key-value` | Stockage clé-valeur |
| `wide-column` | Stockage en colonnes larges (type Cassandra) |
| `columnar` | Stockage orienté colonnes (analytique) |
| `olap` | Analytique / agrégations (par opposition à OLTP) |
| `timeseries` | Séries temporelles / métriques |
| `graph-db` | Base de graphes (données connectées) |
| `search` | Moteur de recherche / indexation textuelle |
| `distributed` | Architecture distribuée multi-nœuds |
| `in-memory` | Données en mémoire (cache, faible latence) |
| `embedded` | Moteur embarqué / sans serveur |
| `db-client` | Client GUI d'accès / administration de bases de données |
| `api-client` | Client d'API : composer, envoyer et tester des requêtes HTTP/REST/GraphQL/gRPC (collections, environnements, scripts) |
| `code-assistant` | Assistant IA de codage intégré (éditeur ou terminal) : complétion, chat, édition multi-fichiers, mode agent |
| `diagram` | Création de diagrammes et schémas techniques (flowcharts, UML, réseau, isométrique, whiteboard) |
| `diagram-as-code` | Diagramme généré à partir de texte/code versionnable (par opposition à l'édition GUI) |
| `whiteboard` | Tableau blanc / canvas infini de croquis, souvent collaboratif |
| `isometric` | Diagramme isométrique 3D (infrastructure, systèmes) |
| `design-tool` | Outil de design d'interface et de prototypage UI/UX (maquettes, composants, prototypes) |
| `note-taking` | Prise de notes et base de connaissances personnelle (markdown local, liens bidirectionnels, graphe) |
| `migration` | Migration de schéma versionnée (DDL sous contrôle de version) |
| `orm` | Mapping objet-relationnel (couche d'accès aux données typée) |
| `db-driver` | Pilote / adaptateur bas niveau d'accès à une base (DB-API, wrapper libpq) |
| `statistical-inference` | Généraliser d'un échantillon à une population |
| `hypothesis-testing` | Test d'hypothèse (H0/H1, décision) |
| `p-value` | p-value et seuil de significativité |
| `confidence-interval` | Estimation d'un paramètre par intervalle |
| `parametric-test` | Test supposant une forme de distribution (normalité…) |
| `non-parametric` | Méthode sans hypothèse de distribution |
| `resampling` | Rééchantillonnage (bootstrap, permutation) |
| `multiple-testing` | Correction de la multiplicité des tests |
| `statistical-power` | Puissance et dimensionnement d'échantillon |
| `effect-size` | Taille d'effet (ampleur, au-delà de la significativité) |
| `experimentation` | Expérimentation en ligne / test contrôlé (A/B, bandits) |
| `ab-testing` | Test A/B — comparaison contrôlée de deux variantes |
| `causal-inference` | Inférence causale — estimer l'effet d'un traitement |
| `variance-reduction` | Réduction de variance d'un estimateur (CUPED, stratification) |
| `multi-armed-bandit` | Allocation adaptative exploration/exploitation |
| `sequential-analysis` | Analyse séquentielle — décision en continu |
| `bayesian` | Approche bayésienne (a priori × vraisemblance → a posteriori) |
| `prior` | Distribution a priori (information avant les données) |
| `probabilistic-programming` | Programmation probabiliste (spécifier un modèle génératif, inférer l'a posteriori) |
| `maximum-likelihood` | Estimation par maximum de vraisemblance |
| `point-estimation` | Estimation ponctuelle d'un paramètre (vs intervalle / distribution) |
| `probability` | Théorie des probabilités (lois, variables aléatoires, convergence) |
| `stochastic-process` | Processus stochastique (évolution aléatoire indexée par le temps) |
| `markov` | Propriété de Markov (le futur ne dépend que du présent) |
| `monte-carlo` | Méthodes de Monte-Carlo (estimation par simulation aléatoire) |
| `convergence` | Convergence asymptotique d'estimateurs / de lois (LGN, TCL) |
| `concentration` | Inégalités de concentration (bornes de probabilité non asymptotiques) |
| `dimensionality-reduction` | Réduction de dimension (projeter dans un espace de plus faible dimension) |
| `factor-analysis` | Méthodes factorielles / analyse de données (axes latents, tradition Benzécri) |
| `clustering` | Partitionnement non supervisé en groupes |
| `unsupervised` | Apprentissage non supervisé (pas de variable cible) |
| `manifold` | Variété / géométrie non euclidienne (manifold learning, riemannien) |
| `multivariate` | Méthode/test portant simultanément sur plusieurs variables réponses (MANOVA, Hotelling T²) |
| `supervised` | Apprentissage supervisé (variable cible) |
| `model-evaluation` | Métriques et validation de modèles |
| `explainability` | Explicabilité / interprétabilité des modèles — attribuer et comprendre les prédictions (Shapley/SHAP, surrogate local/LIME, permutation importance, MDI) |
| `regression` | Modélisation supervisée d'une cible continue |
| `classification` | Prédiction supervisée d'une cible catégorielle |
| `multi-output` | Prédiction simultanée de plusieurs cibles (multi-target regression, multi-label / multi-output classification) |
| `survival-analysis` | Analyse de survie (modélisation du temps jusqu'à un événement, avec censure) |
| `regularization` | Pénalisation des coefficients (L1/L2) contre le surapprentissage |
| `linear-model` | Prédicteur (généralisé / additif) fonction des variables explicatives |
| `tree-based` | Méthode à base d'arbres de décision (arbre seul ou ensemble) |
| `ensemble` | Méthode d'ensemble — agrégation de plusieurs modèles en un prédicteur |
| `bagging` | Bootstrap aggregating — modèles parallèles sur rééchantillons, réduit la variance |
| `boosting` | Ensemble séquentiel — chaque modèle corrige les erreurs résiduelles du précédent |
| `feature-engineering` | Construction et transformation des variables d'entrée d'un modèle (imputation, encodage, mise à l'échelle, sélection) |
| `missing-data` | Données manquantes : mécanismes (MCAR/MAR/MNAR) et stratégies de gestion |
| `eda` | Analyse exploratoire / profiling automatisé d'un jeu de données (types, distributions, valeurs manquantes, corrélations, cardinalités) |
| `hyperparameter-tuning` | Réglage des hyperparamètres d'un modèle (grid search, random search, optimisation bayésienne) |
| `dataframe` | Manipulation de données tabulaires en table (DataFrame : colonnes typées, group-by, jointures) |
| `array` | Calcul sur tableaux N-dimensionnels (ndarray) et opérations vectorisées |
| `lazy-evaluation` | Évaluation différée : construire un plan/graphe de calcul et l'optimiser avant exécution |
| `out-of-core` | Traitement de données plus grandes que la RAM (par morceaux / streaming) |
| `parallel` | Parallélisme multi-cœurs sur une seule machine (par opposition à `distributed`, multi-nœuds) |
| `package-manager` | Gestionnaire de paquets / environnements Python (résolution, installation, lockfile) |
| `linter` | Analyse statique du code (erreurs, style, bonnes pratiques) |
| `formatter` | Formatage automatique du code (style cohérent, sans débat) |
| `testing` | Tests automatisés (unitaires, fonctionnels, fixtures) |
| `data-validation` | Validation de données à l'exécution selon un schéma typé |
| `type-hints` | Annotations de type Python (`typing`) exploitées par l'outil |
| `config` | Gestion de configuration applicative (variables d'environnement, fichiers, secrets) |
| `cli` | Construction d'applications en ligne de commande (parsing d'arguments, commandes et sous-commandes, complétion shell) |
| `terminal-ui` | Rendu et formatage riche dans le terminal (couleurs, styles, tables, barres de progression) et interfaces texte plein écran (TUI) |
| `dataviz` | Visualisation de données (production de graphiques) |
| `static-viz` | Graphiques statiques (rendu image : PNG/SVG/PDF) |
| `interactive-viz` | Graphiques interactifs (zoom, survol, sortie web/JS) |
| `declarative-viz` | Spécification déclarative (grammaire des graphiques, Vega-Lite) |
| `statistical-viz` | Visualisation statistique prête à l'emploi (distributions, relations) |
| `web-framework` | Couche web Python — framework d'API ou serveur HTTP/ASGI |
| `data-app` | Application de données interactive bâtie en Python pur (script → web app, sans front dédié) |
| `dashboard` | Tableau de bord analytique interactif (plusieurs vues / filtres liés) |
| `ml-demo` | Interface de démonstration interactive d'un modèle ML (entrée → sortie) |
| `container` | Conteneurisation / images OCI (packaging d'applications isolées et portables) |
| `ci-cd` | Intégration et déploiement continus (pipelines automatisés déclenchés sur événements) |
| `object-storage` | Stockage objet (buckets, accès par clé, API type S3) |
| `s3-compatible` | Implémente l'API Amazon S3 (interopérable avec l'écosystème et les outils S3) |
| `observability` | Observabilité d'infrastructure / d'applications (métriques, logs, traces) |
| `metrics` | Métriques de supervision / monitoring (séries temporelles d'exploitation) |
| `logging` | Agrégation et requêtage de logs (collecte, indexation, exploration) |
| `orchestration` | Orchestration de workflows / tâches (planification, dépendances, exécution de DAG) |
| `data-pipeline` | Pipeline de données (ELT/ETL : ingestion → transformation → chargement) |
| `scheduler` | Planification temporelle de tâches (déclenchement cron / par intervalle) |
| `low-code` | Construction visuelle / par blocs, à faible quantité de code |
| `declarative-config` | Workflow défini de façon déclarative (YAML / config) plutôt qu'en code impératif |
| `streaming` | Traitement de flux de données en continu (temps réel, par événements) |
| `lakehouse` | Format de table transactionnel sur stockage objet (couche table : ACID, time travel, schema evolution) |
| `file-format` | Format de fichier de données sur disque (encodage, compression, schéma) |
| `serialization` | Sérialisation de données structurées (encodage binaire compact pour échange / stockage) |
| `schema-evolution` | Évolution de schéma compatible (ajout / retrait de champs sans casser lecteurs et écrivains) |
| `durable-execution` | Exécution durable de workflows (état persisté, reprise après panne, exécutions longues) |
| `idempotence` | Idempotence / rejouabilité d'un traitement : un rerun ou un backfill produit le même état final (sans doublon ni dérive) |
| `data-contract` | Contrat de données — interface versionnée producteur↔consommateur (schéma, sémantique, garanties / SLA) |
| `data-quality` | Qualité des données — validation, fraîcheur, complétude, volumétrie, cohérence (tests de données) |
| `cdc` | Change Data Capture — capture incrémentale des changements d'une base source (log-based / query-based) |
| `data-versioning` | Versionnage de données — états immuables et adressables d'un jeu / dépôt de données (snapshots, commits, time travel) pour la reproductibilité |
| `partitioning` | Partitionnement & layout physique des données — clé de partition (répertoires/fichiers), bucketing, partition pruning, taille de fichiers / small files problem (distinct de `pruning`, l'élagage de modèle) |
| `data-modeling` | Modélisation / organisation logique des données en couches ou schémas (architecture médaillon bronze/silver/gold, schéma en étoile, normalisation) |
| `document-parsing` | Extraction de contenu structuré depuis des documents (PDF, Office, HTML, images) |
| `pdf` | Traitement de fichiers PDF |
| `ocr` | Reconnaissance optique de caractères (texte dans images / scans) |
| `table-extraction` | Extraction de tableaux depuis des documents |
| `markdown-conversion` | Conversion de documents en Markdown (pour LLM / RAG) |
| `layout-analysis` | Analyse de la mise en page d'un document (blocs, colonnes, ordre de lecture) |
| `web-scraping` | Extraction de données depuis des pages web (navigation headless, authentification de session, contournement d'anti-bot, throttling) |
| `deep-learning` | Réseaux de neurones profonds (entraînement par rétropropagation) |
| `gpu` | Calcul accéléré sur GPU / TPU (par opposition au CPU seul) |
| `autograd` | Différentiation automatique (gradients calculés par le moteur, pas à la main) |
| `transformers` | Modèles à base de transformeurs (mécanisme d'attention) |
| `model-hub` | Hub de modèles pré-entraînés (téléchargement, partage, versionnage) |
| `fine-tuning` | Ajustement d'un modèle pré-entraîné sur une tâche / un domaine |
| `nlp` | Traitement automatique du langage naturel |
| `forecasting` | Prévision de valeurs futures d'une série temporelle |
| `experiment-tracking` | Suivi d'expériences ML (journalisation des paramètres, métriques, artefacts ; comparaison de runs) |
| `model-registry` | Registre de modèles versionnés (stades, promotion, lineage) |
| `model-serving` | Déploiement d'un modèle entraîné comme service d'inférence (API REST/gRPC) |
| `deployment-strategy` | Stratégie de mise en production d'un modèle / service — rollout progressif et bascule réversible (canary, blue-green, shadow/mirroring, rollback) ; distinct de `model-serving` (exposer en API) |
| `inference` | Inférence / prédiction en production (par opposition à l'entraînement) |
| `kubernetes` | Brique native Kubernetes (opérateurs, CRD, déploiement cloud-native) |
| `ml-pipeline` | Pipeline ML orchestré (étapes d'entraînement / validation / déploiement versionnées et reproductibles) |
| `feature-store` | Magasin de features ML (stockage offline + online, cohérence entraînement/inférence, serving faible latence) |
| `llm` | Grand modèle de langage (LLM) — génération de texte par transformeur autorégressif |
| `local-llm` | Exécution locale de LLM (sur poste / serveur perso, hors API cloud) |
| `quantization` | Réduction de la précision des poids pour alléger mémoire et calcul (GGUF, GPTQ, AWQ, FP8) |
| `agents` | Agent LLM — système qui planifie et appelle des outils en boucle pour accomplir une tâche |
| `tool-use` | Appel d'outils / de fonctions par le LLM (function calling) |
| `prompt-optimization` | Optimisation automatique de prompts — programmation déclarative de LLM compilée vers des prompts (ou un fine-tune) |
| `llm-gateway` | Passerelle / proxy unifié vers plusieurs fournisseurs de LLM (format unique, routage, suivi des coûts) |
| `multi-agent` | Système multi-agents — plusieurs agents LLM qui collaborent / se coordonnent pour accomplir une tâche |
| `structured-output` | Sortie structurée — contraindre un LLM à produire un objet conforme à un schéma typé (JSON / Pydantic) |
| `llm-eval` | Évaluation de systèmes LLM (qualité des réponses, RAG, agents) — métriques et jeux de tests |
| `llm-observability` | Observabilité d'applications LLM en production (traces, métriques, coûts, débogage) |
| `tracing` | Traçage d'exécution : spans imbriqués des appels LLM et outils (qui appelle quoi, latence, coût) |
| `rag-eval` | Évaluation spécifique des pipelines RAG (faithfulness, context precision/recall, answer relevancy) |
| `llm-as-judge` | LLM utilisé comme évaluateur d'une sortie (scoring automatique d'une réponse selon des critères) |
| `ranking` | Qualité d'un ordre prédit / ordonnancement (learning-to-rank, recherche d'information : NDCG, MAP, MRR) |
| `recommender-systems` | Systèmes de recommandation — prédire l'affinité utilisateur↔item (filtrage collaboratif, factorisation matricielle, modèles two-tower) |
| `calibration` | Fiabilité des probabilités prédites (une probabilité de 0,8 se réalise ~80 % du temps) |
| `class-imbalance` | Classification à classes déséquilibrées (distribution très inégale, événements rares) |
| `data-leakage` | Fuite d'information (de la cible ou du futur) du train vers l'évaluation |
| `representation-learning` | Apprentissage de représentations vectorielles denses (embeddings) |
| `retrieval` | Récupération de passages pertinents pour un LLM (dense, lexical, hybride) |
| `chunking` | Découpage de documents en fragments indexables (pour le RAG) |
| `reranking` | Reclassement fin des candidats récupérés (cross-encoder, fusion de scores) |
| `tokenization` | Découpage du texte en tokens / sous-mots (BPE, WordPiece, vocabulaire) |
| `decoding` | Stratégie de génération token par token (greedy, top-k, top-p, beam, température) |
| `context-engineering` | Composition et gestion du contexte fourni au LLM (assemblage, budget de tokens, fenêtre) |
| `perplexity` | Perplexité — qualité intrinsèque d'un modèle de langue (exponentielle de l'entropie croisée) |
| `prompting` | Conception de prompts — formuler instructions, exemples et format pour guider le LLM (artisanat manuel, par opposition à `prompt-optimization` automatique) |
| `reasoning` | Raisonnement multi-étapes du LLM (chaîne de pensée, self-consistency, modèles de raisonnement) |
| `alignment` | Alignement d'un LLM sur les préférences et intentions humaines (RLHF, DPO, modèle de récompense) |
| `inference-optimization` | Accélération de l'inférence LLM (KV-cache, continuous batching, paged attention, décodage spéculatif) |
| `scaling-laws` | Lois d'échelle — relation compute / données / paramètres ↔ perte (Kaplan, Chinchilla, compute-optimal) |
| `small-language-model` | Petit modèle de langage (SLM) efficace — exécution edge / on-device, distillation, quantization |
| `query-transformation` | Transformation de requête en amont du retrieval (réécriture, expansion, décomposition multi-hop, HyDE, step-back) |
| `routing` | Routage d'une requête vers le bon index / modèle, et cascade de modèles (escalade du moins cher au plus cher) |
| `caching` | Mise en cache pour LLM : préfixes de prompt (côté serveur / API) ou réponses (exactes / sémantiques) |
| `benchmark` | Banc d'essai standardisé (jeu de tâches + métrique agrégée) pour comparer des modèles ; classements / leaderboards |
| `code-generation` | Génération de code par LLM (complétion, synthèse de programmes, agents de code) |
| `text-to-sql` | Génération de requêtes SQL à partir de langage naturel (NL2SQL) — traduire une question en SQL exécutable sur une base |
| `mcp` | Model Context Protocol — exposition standardisée d'outils, ressources et prompts à un LLM via une architecture client-serveur (JSON-RPC) |
| `reliability` | Fiabilité d'applications LLM en production (retries, backoff, fallback, timeouts, validation, dégradation gracieuse) |
| `reinforcement-learning` | Apprentissage par renforcement — politique optimisant une récompense par essais (cadre MDP ; PPO, GRPO, RL appliqué aux LLM) |
| `synthetic-data` | Données synthétiques générées par modèle pour l'entraînement / l'évaluation (self-instruct, distillation, paires de préférences) |
| `ai-security` | Sécurité des systèmes LLM/IA — surface d'attaque, panorama des risques (OWASP LLM Top 10), menaces et contre-mesures |
| `prompt-injection` | Injection de prompt — détournement des instructions du système via des entrées non fiables (directe, indirecte, exfiltration) |
| `jailbreak` | Contournement de l'alignement de sécurité d'un LLM pour lui faire produire un contenu interdit |
| `guardrails` | Garde-fous d'entrée/sortie autour des appels LLM (validation de schéma, filtrage, modération, détection d'injection) |
| `safety` | Sûreté et alignement comportemental d'un modèle (refus, contenu nuisible, usage abusif) |
| `linear-algebra` | Algèbre linéaire — vecteurs, matrices, espaces vectoriels et applications linéaires |
| `matrix-decomposition` | Factorisation d'une matrice en facteurs structurés (LU, QR, Cholesky, eigen, SVD) |
| `eigenvalue` | Valeurs et vecteurs propres — spectre d'une matrice (diagonalisation, décomposition spectrale) |
| `vector-norm` | Norme d'un vecteur / d'une matrice (L1, L2, L∞, Frobenius) — mesure de taille et de distance |
| `projection` | Projection orthogonale d'un vecteur sur un sous-espace (projecteur, moindres carrés) |
| `optimization` | Optimisation numérique — minimisation d'une fonction objectif (méthodes du premier / second ordre, convexité) |
| `gradient-descent` | Descente de gradient — minimisation itérative par pas dans la direction de plus forte pente (batch, stochastique, mini-batch) |
| `convexity` | Convexité — un minimum local est global ; garanties d'optimisation pour fonctions et ensembles convexes |
| `second-order` | Méthodes du second ordre — exploitation de la courbure (hessienne) pour l'optimisation (Newton, quasi-Newton) |
| `learning-rate` | Taux d'apprentissage — réglage et planification du pas de descente (warmup, decay, cosine, cyclique) |
| `loss-landscape` | Paysage de perte — géométrie de la surface objectif (minima, points-selles, conditionnement, netteté) |
| `linear-programming` | Programmation linéaire — objectif et contraintes linéaires (simplexe, point intérieur) et son extension en nombres entiers (MIP, branch & bound, relaxation LP) |
| `combinatorial-optimization` | Optimisation combinatoire — meilleure configuration dans un ensemble discret (sac à dos, affectation, couverture ; NP-difficulté, heuristiques) |
| `constrained-optimization` | Optimisation sous contrainte — minimisation sous égalités/inégalités (multiplicateurs de Lagrange, conditions KKT, dualité) |
| `information-theory` | Théorie de l'information — quantifier incertitude, information et écart entre distributions |
| `entropy` | Entropie — mesure d'incertitude d'une distribution (Shannon) |
| `cross-entropy` | Entropie croisée — coût d'encoder une loi avec une autre (perte de classification, log-loss) |
| `kl-divergence` | Divergence de Kullback-Leibler — écart dirigé entre deux distributions (et ses dérivés : Jensen-Shannon) |
| `mutual-information` | Information mutuelle — quantité d'information partagée entre deux variables aléatoires |
| `optimal-transport` | Transport optimal — distance entre distributions par coût de déplacement (Wasserstein, earth mover's) |
| `learning-theory` | Théorie de l'apprentissage statistique — apprenabilité et garanties de généralisation |
| `pac-learning` | Apprentissage PAC (Probably Approximately Correct) — apprenabilité et complexité d'échantillon |
| `vc-dimension` | Dimension de Vapnik-Chervonenkis — capacité d'une classe d'hypothèses (cardinal de shattering) |
| `rademacher-complexity` | Complexité de Rademacher — capacité mesurée par la corrélation au bruit aléatoire (data-dependent) |
| `generalization-bound` | Borne de généralisation — écart garanti entre risque empirique et risque réel |
| `no-free-lunch` | Théorème No Free Lunch — aucun apprenant universellement supérieur sans a priori |
| `attention` | Mécanisme d'attention — pondération apprise des éléments d'une séquence (self / cross, scaled dot-product, multi-head) |
| `positional-encoding` | Encodage de la position dans une séquence pour un modèle permutation-invariant (sinusoïdal, appris, RoPE, ALiBi) |
| `mixture-of-experts` | Mélange d'experts (MoE) — couches d'experts à activation conditionnelle (routing top-k, sparsité, capacité découplée du calcul) |
| `state-space-model` | Modèle à espace d'états (SSM) — séquence à temps linéaire, état latent récurrent (S4, Mamba, RWKV), alternative à l'attention |
| `generative-model` | Modèle génératif — apprend à échantillonner la distribution des données (diffusion, GAN, VAE, autorégressif) |
| `diffusion` | Modèle de diffusion — génération par débruitage itératif d'un bruit gaussien (DDPM, score-based, latent diffusion) |
| `multimodal` | Multimodal — traite ou relie plusieurs modalités (texte, image, audio, vidéo) |
| `image-generation` | Génération d'images — synthèse d'images, surtout à partir de texte (text-to-image) |
| `video-generation` | Génération de vidéos — synthèse de séquences vidéo (text-to-video, image-to-video) |
| `speech` | Traitement de la parole — reconnaissance (ASR) et synthèse (TTS) vocales |
| `vision-language` | Modèles vision-langage — entrée image + texte, raisonnement multimodal (VLM) |
| `computer-vision` | Vision par ordinateur — perception et compréhension d'images/vidéos (classification, détection, segmentation) |
| `cnn` | Réseau de neurones convolutif — convolution, pooling, champ réceptif ; ossature historique de la vision |
| `transfer-learning` | Transfert d'apprentissage — réutiliser un modèle pré-entraîné (ses features) sur une nouvelle tâche / un nouveau domaine |
| `data-augmentation` | Augmentation de données — transformations synthétiques des entrées pour régulariser l'entraînement (Mixup, CutMix, RandAugment) |
| `image-classification` | Classification d'images — attribuer une étiquette globale à une image entière (pendant vision de `text-classification`) |
| `object-detection` | Détection d'objets — localiser et classer des instances par boîtes englobantes (anchors, NMS, mAP) |
| `segmentation` | Segmentation d'image — étiquetage au niveau du pixel (sémantique, instance, panoptique ; U-Net, Mask R-CNN, SAM) |
| `pose-estimation` | Estimation de pose — localisation de points-clés / articulations (keypoints) dans une image ou une vidéo |
| `object-tracking` | Suivi d'objets — association temporelle d'identités à travers les frames d'une vidéo (multi-object tracking) |
| `metric-learning` | Apprentissage de métrique — apprendre un espace d'embeddings où la distance reflète la similarité (contrastive, triplet, ArcFace) |
| `re-identification` | Ré-identification — retrouver la même instance / identité à travers le temps et les caméras (person re-id, reconnaissance faciale) |
| `vit` | Vision Transformer — ossature à base d'[[Self-attention\|attention]] sur des patchs d'image (parallèle au `cnn`) |
| `self-supervised` | Apprentissage auto-supervisé — pré-entraînement sur tâche prétexte sans étiquettes (contrastif, masquage, self-distillation) ; distinct de `unsupervised` |
| `foundation-model` | Modèle de fondation — gros modèle pré-entraîné généraliste, réutilisable par transfert / zero-shot (CLIP, DINOv2) |
| `gan` | Réseau antagoniste génératif (GAN) — générateur vs discriminateur entraînés en jeu adversarial |
| `neural-rendering` | Rendu neuronal — représentation 3D apprise d'une scène et synthèse de nouvelles vues (NeRF, 3D Gaussian Splatting) |
| `depth-estimation` | Estimation de profondeur — prédiction de la distance par pixel (monoculaire, stéréo, MVS) |
| `markov-decision-process` | Processus de décision markovien (MDP) — cadre formel états / actions / transitions / récompenses du RL |
| `dynamic-programming` | Programmation dynamique — résolution récursive par sous-problèmes (équations de Bellman, value/policy iteration) |
| `value-function` | Fonction de valeur — récompense cumulée espérée d'un état (V) ou d'une paire état-action (Q) |
| `exploration-exploitation` | Dilemme exploration/exploitation — arbitrer entre tester l'inconnu et exploiter le meilleur connu |
| `temporal-difference` | Apprentissage par différence temporelle — bootstrap sur l'estimation courante (TD, Q-learning, SARSA) |
| `policy-gradient` | Méthodes de gradient de politique — optimisent π directement (REINFORCE, actor-critic, PPO, GRPO) |
| `model-based-rl` | RL basé modèle — apprend la dynamique et planifie (Dyna, MCTS, world models) |
| `offline-rl` | RL hors ligne — apprend une politique depuis un dataset fixe de transitions, sans interaction (batch RL ; distribution shift, pessimisme : BCQ, CQL, IQL) |
| `imitation-learning` | Apprentissage par imitation — apprend une politique à partir de démonstrations d'expert (behavioral cloning, DAgger, inverse RL, GAIL) |
| `reward-shaping` | Conception du signal de récompense — façonnage (potential-based shaping) et détournement (reward hacking, loi de Goodhart, specification gaming) |
| `game-theory` | Théorie des jeux — décisions stratégiques multi-agents : équilibre de Nash, jeux à somme nulle, information imparfaite, minimax |
| `self-play` | Apprentissage par self-play — l'agent progresse en jouant contre lui-même ou ses versions passées (AlphaZero, curriculum auto-généré) |
| `planning` | Planification par recherche avant (lookahead) dans un modèle/simulateur connu — recherche arborescente (MCTS, minimax) |
| `regret-minimization` | Minimisation du regret — apprentissage en ligne convergeant vers l'équilibre via le regret cumulé (CFR, regret matching) |
| `anomaly-detection` | Détection d'anomalies — repérer les points / segments qui s'écartent du comportement normal (outliers, nouveautés, ruptures) |
| `data-drift` | Dérive de données — la distribution des entrées en production s'écarte de l'entraînement (covariate shift, `P(X)` change) |
| `concept-drift` | Dérive de concept — la relation entrée→cible se déforme dans le temps (`P(y\|X)` change) |
| `model-monitoring` | Surveillance d'un modèle ML en production (dérive, performance, qualité des données ; distinct de l'`observability` d'infra) |
| `signal-processing` | Traitement du signal — analyse et transformation de signaux échantillonnés (temps ↔ fréquence) |
| `fourier` | Analyse de Fourier — décomposition d'un signal en fréquences (DFT/FFT, domaine spectral) |
| `wavelet` | Ondelettes — analyse temps-échelle multirésolution (DWT/CWT) |
| `spectrogram` | Représentation temps-fréquence (STFT, mel-spectrogramme, MFCC) |
| `digital-filter` | Filtrage numérique (FIR/IIR, Butterworth, fenêtrage) |
| `information-retrieval` | Recherche d'information — indexer et classer des documents par pertinence pour une requête (TF-IDF, BM25, métriques NDCG/MAP/MRR) ; discipline classique, plus large que le `retrieval` RAG-centré |
| `string-matching` | Similarité et appariement approximatif de chaînes (distance d'édition / Levenshtein, Jaro-Winkler, token-set) — fuzzy matching, déduplication, record linkage |
| `ner` | Reconnaissance d'entités nommées — repérer et typer les mentions (personnes, lieux, dates, montants) dans un texte |
| `sequence-labeling` | Étiquetage de séquence — attribuer un label à chaque token (schémas IOB/BILOU, CRF, décodage de Viterbi) |
| `text-classification` | Classification de texte — assigner une ou plusieurs catégories à un document (baseline TF-IDF → embeddings → LLM) |
| `knowledge-graph` | Graphe de connaissances — entités typées reliées par des relations sémantiques, comme représentation interrogeable des connaissances (distinct du moteur de stockage `graph-db`) |
| `relation-extraction` | Extraction de relations entre entités à partir de texte (triplets sujet–relation–objet) — brique de construction d'un graphe de connaissances |
| `human-in-the-loop` | Intervention humaine dans une boucle automatisée / agent — validation, approbation ou correction d'une action à fort enjeu (HITL) |
| `gnn` | Graph Neural Network — réseau de neurones sur graphes par passage de messages (agrégation du voisinage) : GCN, GAT, GraphSAGE |
| `distributed-training` | Entraînement distribué d'un modèle sur plusieurs GPU / nœuds — parallélisme de données/modèle/pipeline/tenseur et sharding des états (DDP, FSDP, ZeRO) |
| `mixed-precision` | Entraînement en précision mixte (fp16/bf16 avec maître fp32 et loss scaling) — moins de mémoire, plus de débit GPU |
| `memory-optimization` | Réduction de l'empreinte mémoire à l'entraînement (recomputation d'activations, offloading, sharding d'états) |
| `pruning` | Élagage de modèle — suppression de poids (non structuré) ou de structures (structuré) pour réduire taille et calcul |
| `model-compression` | Compression de modèle pour réduire taille, mémoire et calcul (pruning, quantization, distillation) ; distinct de l'accélération algorithmique `inference-optimization` |
| `notebook` | Notebook computationnel — cellules code + sortie + narration (.ipynb, noyau Jupyter) |
| `reproducibility` | Reproductibilité — relancer un traitement et retrouver le même résultat (environnement épinglé, seeds, versionnage code/données) |
| `version-control` | Gestion de version de code source (git : diff, revue, branches, historique) ; distinct de `data-versioning` (états d'un jeu de données) |
| `audio-classification` | Classification audio — étiqueter un son global : genre musical, scène acoustique, événement sonore ; distinct de `speech` (ASR/TTS) |
| `hypermedia` | Approche hypermedia — HTML comme moteur d'état applicatif (HATEOAS) : interactivité par attributs sur le HTML existant, fragments échangés côté serveur, sans SPA |
| `templating` | Moteur de templates — génération de texte/HTML à partir de gabarits et de données (rendu côté serveur, héritage de templates, échappement automatique) |
| `authentication` | Authentification — vérification d'identité et gestion des accès (tokens, sessions, JWT, OAuth/OIDC) |
| `cryptography` | Primitives cryptographiques — signature et vérification, HMAC, chiffrement à clé symétrique / asymétrique (RSA, ECDSA, EdDSA) |
| `rex` | Marqueur de type — page de retour d'expérience (`Dev/REX/`). Imposé par le gabarit REX |
| `bugs` | Marqueur de type — REX centré sur des bugs / incidents rencontrés. Imposé par le gabarit REX |
| `pattern` | Marqueur de type — page de pattern / décision d'architecture (`Dev/Patterns/`). Imposé par le gabarit Pattern |
| `rule` | Marqueur de type — page de règle transverse (`Dev/Rules/`). Imposé par le gabarit Rule |

> Démarrage : tags du premier cluster (bases vectorielles), étendu aux bases de données puis aux statistiques (inférence, expérimentation & inférence causale, estimation & approche bayésienne, probabilités & processus stochastiques, puis réduction de dimension & analyse factorielle), puis au ML généraliste (apprentissage supervisé, évaluation de modèles, puis modèles linéaires & régression : régression, classification, régularisation, modèles linéaires ; puis arbres & ensembles : arbres de décision, ensemble, bagging, boosting ; puis ingénierie des caractéristiques : feature-engineering ; puis évaluation & sélection de modèles : hyperparameter-tuning), puis à l'outillage Python (gestion de paquets, lint/format, tests, validation & configuration), puis à la visualisation (dataviz, statique, interactif, déclaratif, statistique), puis à l'orchestration de données (orchestration, pipelines ELT, planification, low-code, déclaratif), puis à l'ingénierie de données avancée (streaming, lakehouse & formats de fichiers : file-format, serialization, schema-evolution ; exécution durable de workflows : durable-execution), puis aux frameworks de deep learning (deep-learning, gpu, autograd, transformers, model-hub, fine-tuning, nlp), puis à la prévision de séries temporelles (forecasting, réutilise timeseries), puis au suivi d'expériences ML (experiment-tracking, model-registry), puis à l'exécution & au serving de LLM (llm, local-llm, quantization ; réutilise model-serving, inference, gpu), puis aux frameworks d'applications LLM (agents, tool-use, prompt-optimization ; passerelle multi-fournisseurs : llm-gateway ; puis aux frameworks d'agents et de sorties structurées : multi-agent, structured-output), puis à l'évaluation et l'observabilité des LLM (évaluation : llm-eval, rag-eval, llm-as-judge ; observabilité de production : llm-observability, tracing), puis aux métriques d'évaluation ML (qualité d'un ordonnancement : ranking ; fiabilité des probabilités prédites : calibration), puis aux concepts ML transverses (classes déséquilibrées : class-imbalance ; fuite de données : data-leakage ; apprentissage de représentations : representation-learning), puis au prompting & à l'alignement des LLM (conception de prompts : prompting ; raisonnement multi-étapes : reasoning ; alignement par préférences : alignment ; réutilise fine-tuning), puis à l'observabilité d'infrastructure (observability, metrics, logging ; réutilise tracing) et aux pilotes de bases de données (db-driver), puis à l'inférence & l'échelle des LLM (accélération de l'inférence : inference-optimization ; lois d'échelle : scaling-laws ; petits modèles : small-language-model ; réutilise reasoning, alignment), puis aux techniques RAG avancées et au caching LLM (transformation de requête : query-transformation ; routage et cascade : routing ; mise en cache : caching ; réutilise rag-eval, retrieval, inference-optimization), puis à l'évaluation par bancs d'essai (banc d'essai standardisé : benchmark ; génération de code par LLM : code-generation), puis au cluster agents (évaluation d'agents, exposition standardisée d'outils par le Model Context Protocol, fiabilité des apps LLM : mcp, reliability ; réutilise agents, tool-use, structured-output, llm-eval), puis au post-training par RL des LLM (apprentissage par renforcement appliqué aux LLM, modèle de récompense, GRPO : reinforcement-learning ; génération de données synthétiques pour l'entraînement : synthetic-data ; réutilise alignment, fine-tuning, reasoning), puis aux mathématiques pour le ML (algèbre linéaire : linear-algebra, matrix-decomposition, eigenvalue, vector-norm, projection ; réutilise regularization et dimensionality-reduction), puis à l'optimisation pour le ML (optimisation numérique, descente de gradient, convexité, méthodes du second ordre, planification du taux d'apprentissage, paysage de perte : optimization, gradient-descent, convexity, second-order, learning-rate, loss-landscape), puis à la théorie de l'information pour le ML (entropie, entropie croisée, divergences entre distributions et transport optimal : information-theory, entropy, cross-entropy, kl-divergence, mutual-information, optimal-transport), puis aux architectures de deep learning (transformeurs et attention : attention, positional-encoding, mixture-of-experts ; réutilise transformers, deep-learning, inference-optimization, scaling-laws), puis aux modèles à espace d'états et à la compression / l'optimisation des modèles (state-space-model ; réutilise optimization, gradient-descent, learning-rate, quantization, small-language-model, synthetic-data, fine-tuning, inference-optimization pour Adam, Distillation et Quantization), puis aux fondations du reinforcement learning (cadre MDP, équations de Bellman, fonctions de valeur, dilemme exploration/exploitation : markov-decision-process, dynamic-programming, value-function, exploration-exploitation ; réutilise reinforcement-learning, markov, multi-armed-bandit), puis aux algorithmes du reinforcement learning (apprentissage par différence temporelle, gradient de politique, RL basé modèle : temporal-difference, policy-gradient, model-based-rl ; réutilise reinforcement-learning, value-function, dynamic-programming, deep-learning pour Q-learning/DQN, Policy gradient, PPO, Actor-Critic, Model-based RL), puis au RL avancé (RL hors ligne, apprentissage par imitation, conception et détournement de récompense : offline-rl, imitation-learning, reward-shaping ; réutilise reinforcement-learning, value-function, supervised, alignment pour Offline RL, Imitation learning, Reward shaping and hacking), puis au traitement du signal (analyse et transformation de signaux échantillonnés, analyse de Fourier, ondelettes, représentations temps-fréquence, filtrage numérique : signal-processing, fourier, wavelet, spectrogram, digital-filter), puis au traitement du langage naturel (recherche d'information lexicale/dense/hybride, reconnaissance d'entités et étiquetage de séquence, classification de texte : information-retrieval, ner, sequence-labeling, text-classification ; réutilise nlp, retrieval, ranking, reranking, hybrid-search, semantic-search, search, classification, supervised, class-imbalance, feature-engineering, embeddings), puis à la détection d'anomalies & d'outliers (réutilise anomaly-detection, unsupervised, timeseries), puis à l'explicabilité des modèles (attribution et interprétation des prédictions : explainability ; réutilise supervised), puis aux compléments de sous-domaines existants (prédiction simultanée de plusieurs cibles : multi-output ; mécanismes de données manquantes : missing-data ; tests/analyses multivariés : multivariate), puis à la vision par ordinateur (perception d'images, réseaux convolutifs, transfert d'apprentissage et augmentation de données : computer-vision, cnn, transfer-learning, data-augmentation ; réutilise deep-learning, fine-tuning, regularization, transformers pour CNN, architectures CNN, transfer learning vision et augmentation d'images), puis aux tâches de vision (classification d'images, détection d'objets, segmentation sémantique/instance/panoptique, segmentation promptable SAM, métriques de vision : image-classification, object-detection, segmentation ; réutilise computer-vision, cnn, deep-learning, model-evaluation, transformers), puis aux tâches de vision avancées (estimation de pose et points-clés, suivi d'objets multi-cibles, reconnaissance de texte dans l'image, apprentissage de métrique et ré-identification : pose-estimation, object-tracking, metric-learning, re-identification ; réutilise ocr, computer-vision, object-detection, deep-learning, embeddings, representation-learning, transformers), puis à la frontière de la vision (Vision Transformer et son ossature, modèles de fondation vision, apprentissage auto-supervisé, génération adversariale, rendu neuronal 3D et estimation de profondeur : vit, self-supervised, foundation-model, gan, neural-rendering, depth-estimation ; réutilise transformers, attention, computer-vision, representation-learning, embeddings, vision-language, transfer-learning, generative-model, image-generation, diffusion, deep-learning), puis au cluster RL & jeux (théorie des jeux et algorithmes de planification / self-play / minimisation du regret : game-theory, self-play, planning, regret-minimization ; réutilise monte-carlo, model-based-rl, deep-learning, reinforcement-learning, optimization pour MCTS, AlphaZero, CFR, Théorie des jeux), puis au cluster GraphRAG & graphes de connaissances (graphe de connaissances pour le RAG, extraction d'entités/relations, intervention humaine dans la boucle agent : knowledge-graph, relation-extraction, human-in-the-loop ; réutilise rag, retrieval, graph-db, ner, agents, reliability), puis aux réseaux de neurones sur graphes (Graph Neural Networks par passage de messages : gnn ; réutilise deep-learning, representation-learning, graph-db, knowledge-graph), puis à l'optimisation discrète & avancée (programmation linéaire en nombres entiers, optimisation combinatoire, optimisation sous contrainte : linear-programming, combinatorial-optimization, constrained-optimization ; réutilise optimization, convexity, dynamic-programming, optimal-transport pour MIP, Optimisation combinatoire, Optimisation sous contrainte et Optimal transport), puis à l'efficacité d'entraînement & à la compression de modèles (entraînement distribué multi-GPU/nœuds, précision mixte, recomputation d'activations à l'entraînement, élagage et compression de modèle : distributed-training, mixed-precision, memory-optimization, pruning, model-compression ; réutilise deep-learning, gpu, inference-optimization, quantization, small-language-model pour Entraînement distribué, Mixed precision, Gradient checkpointing, Pruning — et rétrofit model-compression sur Quantization et Distillation), puis à un cluster transverse data-sci / data-eng (systèmes de recommandation, similarité de chaînes / fuzzy matching, web scraping, EDA automatisée & profiling : recommender-systems, string-matching, web-scraping, eda ; réutilise ranking, embeddings, retrieval, information-retrieval, nlp, feature-engineering, missing-data, anomaly-detection), puis à l'ingénierie de données — pipelines & qualité (ELT/ETL & idempotence, contrats & qualité de données, Change Data Capture, versionnage de données : idempotence, data-contract, data-quality, cdc, data-versioning ; réutilise data-pipeline, data-validation, schema-evolution, streaming), puis à l'architecture & au layout de données (couches médaillon bronze/silver/gold, partitionnement & layout physique, stream processing, internes des index ANN : data-modeling, partitioning ; réutilise lakehouse, data-pipeline, data-quality, file-format, olap, streaming, idempotence, ann, vector-db, embeddings), puis au cluster MLOps — cycle de vie du modèle en production (stratégie de déploiement progressif : deployment-strategy ; réutilise model-serving, inference, model-registry, experiment-tracking, feature-store, model-monitoring, data-drift, concept-drift), puis à un cluster Wiki transverse (streaming d'inférence LLM côté serveur, notebooks-as-code, classification audio par spectrogramme : notebook, reproducibility, version-control, audio-classification ; réutilise streaming, llm, web-framework, spectrogram, cnn), puis à l'outillage CLI & terminal (construction d'applications en ligne de commande, rendu riche en terminal : cli, terminal-ui), puis aux frameworks frontend hypermedia & templating (approche hypermedia côté HTML, moteur de templates côté serveur : hypermedia, templating ; réutilise web-framework, type-hints, data-validation), puis aux outils Dev d'usage quotidien (clients d'API et assistants IA de codage : api-client, code-assistant ; réutilise code-generation, agents, llm, version-control, mcp), puis aux frameworks text-to-SQL (génération de requêtes SQL depuis le langage naturel : text-to-sql ; réutilise llm, rag, agents, multi-agent, local-llm, fine-tuning), puis aux outils de diagramme, de design et de connaissance (schémas techniques, diagram-as-code, whiteboard, isométrique, design d'interface, prise de notes : diagram, diagram-as-code, whiteboard, isometric, design-tool, note-taking). À étendre au fil des ajouts via enrichir-brain.
