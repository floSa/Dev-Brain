---
title: Backlog d'enrichissement du DevBrain
date: 2026-06-10
author: agent
status: backlog
---

# Backlog d'enrichissement du DevBrain

> Document généré par analyse croisée de deux sources :
> 1. **Tes projets** dans `\\wsl.localhost\ubuntu-24.04\home\florian\mes_projets`
>    (lecture des `pyproject.toml` / `requirements.txt` / READMEs / `documentation/`).
> 2. **L'analyse de la collection existante** du brain (≈190 concepts, 165 services,
>    31 comparatifs) — repérage des trous internes indépendamment des projets.
>
> Colonne **Source** : nom du projet d'où sort le besoin, ou `Analyse` quand c'est
> un trou que j'ai repéré dans la cohérence du brain lui-même.
>
> Rien n'a encore été créé. Ce fichier est une file d'attente, à traiter via la
> skill `enrichir-brain`.

---

## 0. Vue d'ensemble — le décalage central

Le brain est un **curriculum ML/AI/stats quasi-exhaustif et académique**. Mais
ce que tu **construis réellement** mobilise trois familles peu ou pas couvertes :

- **Recherche / planification / théorie des jeux** (MCTS, AlphaZero, CFR) — ta
  galaxie RL est profonde mais s'arrête avant la recherche arborescente, alors
  que ton projet phare (Courtisant) est un AlphaZero.
- **Vision convolutive** (CNN, ResNet, transfer learning) — tu as `Transformer
  architectures`, `Diffusion`, `KAN`… mais **aucune fiche CNN**, alors que 3
  projets font de la vision.
- **Optimisation discrète / combinatoire** (MIP, branch & bound) — toute ton
  optimisation fichée est *continue* (gradient, Newton, convexité).

Et côté **data engineering**, le brain a tous les *outils* (Airflow, Dagster,
Spark, DuckDB…) mais presque aucun *concept* (ELT, idempotence, CDC, contrats
de données). Angle mort pour un profil qui se revendique data engineer.

---

## 1. Concepts à créer

### 1.1 — Révélés par tes projets (rédaction facile, tu l'as déjà codé)

| Nom | Description | Source |
|---|---|---|
| **Monte Carlo Tree Search (MCTS)** | Recherche arborescente par simulation (sélection UCT, expansion, rollout, backup). Le chaînon manquant entre ta galaxie RL et la planification. | Courtisant-Game |
| **AlphaZero / self-play** | Boucle d'auto-apprentissage : réseau policy+value guidant un MCTS, entraîné sur ses propres parties. Relie `Policy gradient`, `Value functions`, MCTS. | Courtisant-Game |
| **CFR (Counterfactual Regret Minimization)** | Minimisation de regret pour jeux à information imparfaite. Référencé par le dossier `cfr/` du projet. | Courtisant-Game |
| **Théorie des jeux (Nash, information imparfaite)** | Équilibres, stratégies mixtes, jeux à somme nulle. Socle de tes deux jeux de cartes. | Courtisant-Game, Urban-Rivals |
| **CNN / réseaux convolutifs** | Convolution, pooling, champ réceptif, hiérarchie de features. Le trou le plus voyant pour un profil vision. | image_detection_pneumonia, classification_bubbles |
| **Architectures CNN (ResNet, MobileNet, EfficientNet)** | Connexions résiduelles, blocs inversés, depthwise-separable. Tu utilises ResNet (Courtisant) et MobileNetV2 (bubbles). | Courtisant-Game, classification_bubbles |
| **Transfer learning & fine-tuning vision** | Backbone préentraîné + tête custom, gel/dégel de couches. `PEFT`/`SFT` ne couvrent que le LLM. | image_detection_pneumonia |
| **Classification audio par spectrogramme** | Pipeline audio → STFT/mel-spectrogramme → CNN. Relie `STFT et spectrogramme`, `librosa`, CNN. | classification_bubbles |
| **GraphRAG / Knowledge Graph pour RAG** | Couplage base vectorielle + graphe pour reconstruire le contexte hiérarchique avant génération. Architecture centrale de tes 2 projets RAG. | rag-ingestion-pipeline, rag-agent-chat |
| **Construction de Knowledge Graph** | Extraction document → entités/relations → graphe (Document>Section>Text>Image). | rag-ingestion-pipeline |
| **Human-in-the-loop (agents)** | L'utilisateur valide/sélectionne les sources avant génération. Pattern d'agent interruptible (LangGraph). | rag-agent-chat |
| **Programmation linéaire en nombres entiers (MIP)** | Formulation objectif/contraintes, relaxation LP, branch & bound, optimum exact garanti. | MKM |
| **Optimisation combinatoire** | Cadre général (sac à dos, affectation, couverture). Famille entièrement absente du brain. | MKM |
| **Fuzzy matching / similarité de chaînes** | Levenshtein, Jaro-Winkler, token-set ratio (RapidFuzz). Récurrent dans tes pipelines de matching. | Musique_Tools, MKM |
| **Web scraping (headless, session auth, anti-bot)** | Playwright vs HTTP, persistance de session, contournement Cloudflare, throttling éthique. | MKM, Legos, Modeles_comparatifs |
| **Systèmes de recommandation** | Filtrage collaboratif, similarité item-item, factorisation matricielle. Musique_Tools fait de la reco d'artistes sans backbone théorique. | Musique_Tools |
| **EDA automatisée / profiling** | Génération de rapports exploratoires (distribution, corrélation, valeurs manquantes) en une commande. | Notebooks_convertion |

### 1.2 — Trous internes du brain (mon analyse, indépendamment des projets)

| Nom | Description | Source |
|---|---|---|
| **Inférence causale (tronc)** | DAG causal, confounding, backdoor criterion, propensity score. Tu as les feuilles (`Diff-in-Diff`, `CUPED`, `A-B testing`, service `CausalImpact`) mais pas le tronc. | Analyse |
| **Analyse de survie** | Kaplan-Meier, hazard, modèle de Cox, censure. Le service `lifelines` est fiché sans aucun concept derrière. | Analyse |
| **Graph Neural Networks (GNN)** | Message passing, GCN/GAT/GraphSAGE. Bases graphes fichées (Neo4j, Nebula), aucun concept GNN. | Analyse |
| **ELT vs ETL & idempotence** | Pattern de chargement, rejouabilité, gestion des reruns. Aucun concept DE malgré 6+ orchestrateurs fichés. | Analyse |
| **Contrats de données & qualité** | Schémas attendus, validation, tests de fraîcheur/volumétrie (Great Expectations / Pandera). | Analyse |
| **Change Data Capture (CDC)** | Capture incrémentale des changements de base, log-based vs query-based. | Analyse |
| **Architecture médaillon (bronze/silver/gold)** | Organisation en couches d'un lakehouse. Iceberg/Parquet fichés sans le pattern. | Analyse |
| **Partitionnement & layout de données** | Partitions, bucketing, fichiers de taille optimale, pruning. | Analyse |
| **Stream processing (windowing, exactly-once)** | Fenêtres temporelles, watermarks, sémantiques de livraison. Service Flink fiché sans concept. | Analyse |
| **Index ANN — internes (HNSW, IVF, PQ)** | Comment marchent réellement les index que tu utilises (Faiss, hnswlib, ScaNN). | Analyse |
| **Déploiement de modèles (canary, shadow, blue-green)** | Stratégies de rollout ML. Tu as `Data drift` et `Reliability patterns`, pas le déploiement. | Analyse |
| **Model registry & versioning** | Versionnage de modèles, stages, lignage. MLflow fiché côté outil seulement. | Analyse |
| **Feature store (concept)** | Online/offline store, point-in-time correctness. Service `Feast` fiché sans concept. | Analyse |
| **Versionnage de données (DVC, lakeFS)** | Versionner les datasets comme du code. | Analyse |
| **Optimisation sous contrainte (Lagrangien, KKT)** | Le pont entre ton optimisation continue fichée et la programmation linéaire. | Analyse |
| **Optimal transport** | Plan de transport, distance de Wasserstein comme problème d'optimisation. `Wasserstein distance` fiché côté divergences seulement. | Analyse |
| **Server-Sent Events / streaming LLM** | Streaming token-par-token côté serveur (sse-starlette). Récurrent dans tes apps LLM. | rag-agent-chat / Analyse |
| **Notebooks-as-code (jupytext, pairing .py/.md)** | Versionner des notebooks proprement, diff lisible. Cœur du projet de refonte de tes notebooks. | Notebooks_convertion |

---

## 2. Services à ficher

Outils **réellement importés** dans tes projets mais absents de `Dev/Services/`.

### 2.1 — Scraping & parsing

| Nom | Description | Source |
|---|---|---|
| **Playwright** | Automatisation de navigateur headless, session authentifiée persistée (`storage_state`). | MKM, Modeles_comparatifs |
| **selectolax** | Parsing HTML ~10× plus rapide que BeautifulSoup (utilisé sur des pages MKM de 10-20 Mo). | MKM |
| **cloudscraper** | Contournement des challenges Cloudflare pour scraping HTTP. | Legos |
| **curl_cffi** | Client HTTP imitant l'empreinte TLS d'un navigateur (anti-bot). | Legos |

### 2.2 — Optimisation & CLI

| Nom | Description | Source |
|---|---|---|
| **PuLP** | Modélisation de programmes linéaires/MIP en Python, solveur CBC embarqué. | MKM |
| **typer** | Construction de CLI typées à partir d'annotations de fonctions. | MKM |
| **rich** | Rendu terminal (tables, logs, progress) ; sous-jacent à beaucoup de tes CLI. | MKM, Notebooks_convertion |

### 2.3 — Web / UI

| Nom | Description | Source |
|---|---|---|
| **SQLModel** | ORM combinant Pydantic + SQLAlchemy. Tu n'as que SQLAlchemy et Prisma fichés. | Urban-Rivals |
| **HTMX** | Interactivité serveur sans JS lourd (hypermedia). | Urban-Rivals |
| **Jinja2** | Templating HTML côté serveur (FastAPI, prompts). | Urban-Rivals, rag-agent-chat |
| **torchvision** | Modèles vision préentraînés + transforms. Utilisé pour tout ton transfer learning. | image_detection_pneumonia, classification_bubbles |

### 2.4 — Bases vectorielles & data

| Nom | Description | Source |
|---|---|---|
| **LanceDB** | Base vectorielle embarquée orientée colonnes (format Lance). Manque à ta collection vectorielle. | Notebooks_convertion |
| **connectorx** | Chargement ultra-rapide DB → DataFrame (Arrow). | Notebooks_convertion |
| **ADBC (Arrow Database Connectivity)** | Drivers de bases natifs Arrow, alternative à ODBC/DBAPI. | Notebooks_convertion |
| **jupysql** | SQL dans Jupyter (magic `%sql`), multi-backend. | Notebooks_convertion |
| **xarray** | Tableaux N-dimensionnels labellisés (idéal séries temporelles multi-axes / NetCDF). | Notebooks_convertion |

### 2.5 — EDA, NLP & ML

| Nom | Description | Source |
|---|---|---|
| **ydata-profiling** | Rapport EDA automatique exhaustif (ex pandas-profiling). | Notebooks_convertion |
| **sweetviz** | Rapport EDA visuel, comparaison train/test. | Notebooks_convertion |
| **missingno** | Visualisation des patterns de valeurs manquantes. Relie `Mécanismes de données manquantes`. | Notebooks_convertion |
| **NLTK** | Boîte à outils NLP classique (tokenisation, stemming, corpora). Tu n'as que spaCy/GLiNER. | Notebooks_convertion |
| **bm25s** | Implémentation BM25 rapide (alternative à rank-bm25). | Notebooks_convertion |
| **seqeval** | Métriques d'évaluation pour l'étiquetage de séquences (NER). Relie `NER et étiquetage de séquence`. | Notebooks_convertion |
| **PaCMAP** | Réduction de dimension préservant structure locale+globale (alternative à UMAP/t-SNE). | Notebooks_convertion |
| **pykan** | Implémentation des Kolmogorov-Arnold Networks. Le concept `KAN` existe sans service. | Notebooks_convertion |

### 2.6 — Écosystème HuggingFace & tooling

| Nom | Description | Source |
|---|---|---|
| **datasets** (HF) | Chargement/streaming de datasets, mapping efficace. | Notebooks_convertion |
| **accelerate** | Abstraction multi-GPU/mixed-precision pour l'entraînement PyTorch. | Notebooks_convertion |
| **evaluate** (HF) | Hub de métriques standardisées. | Notebooks_convertion |
| **sentencepiece** | Tokenisation subword (BPE/unigram) pour modèles de langue. Relie `Tokenization`. | Notebooks_convertion |
| **jupytext** | Pairing notebook ↔ script `.py`/`.md` pour un versionnage propre. | Notebooks_convertion |
| **TensorBoard** | Visualisation d'entraînement (scalaires, histogrammes, embeddings). Manque à ta galaxie suivi d'expériences. | Notebooks_convertion |
| **PyJWT** | Génération/validation de JWT. Catégorie `Auth` quasi vide. | Notebooks_convertion |

---

## 3. Comparatifs `.base` à créer

| Nom | Description | Source |
|---|---|---|
| **Comparatif - Scraping** | Playwright vs Selenium vs requests vs cloudscraper vs curl_cffi (JS, anti-bot, vitesse). | MKM, Legos |
| **Comparatif - Solveurs d'optimisation** | PuLP vs OR-Tools vs scipy.optimize vs cvxpy (LP, MIP, non-linéaire). | MKM |
| **Comparatif - Frameworks CLI** | typer vs click vs argparse vs fire. | MKM |
| **Comparatif - Outils EDA / profiling** | ydata-profiling vs sweetviz vs missingno vs D-Tale. | Notebooks_convertion |
| **Comparatif - Frontends web légers** | FastAPI+HTMX vs Streamlit vs Gradio vs Dash (le `.base` Apps data ne couvre pas le couple serveur+hypermedia). | Urban-Rivals, classification_bubbles |
| **Comparatif - Réduction de dimension** | PCA vs t-SNE vs UMAP vs PaCMAP (les concepts existent, pas le comparatif outillé). | Notebooks_convertion / Analyse |

---

## 4. Patterns à créer

| Nom | Description | Source |
|---|---|---|
| **Pattern - Stack démo ML locale multi-services** | Ta signature architecturale : DB (séries-temp/relationnelle) + MongoDB + MinIO + FastAPI + Streamlit, en docker-compose, `.env.example` + Makefile. Vue dans 3 projets. | classification_bubbles, rag-ingestion-pipeline, RAG_Ollama_Streamlit |
| **Pattern - RAG structuré graphe + human-in-the-loop** | Vectoriel pour le rappel, graphe pour le contexte hiérarchique, validation utilisateur avant génération, LLM local cité. | rag-agent-chat |
| **Pattern - Moteur de jeu pur + IA séparée** | Séparation stricte règles (`jeu.py`, aucune IA) / IA (`mcts_network.py`) / UI. Bonne discipline réutilisable. | Courtisant-Game |
| **Pattern - Pipeline scraping → matching → optimisation** | Récupération HTML → parsing → matching flou → solveur. Squelette commun MKM / Musique_Tools. | MKM, Musique_Tools |

---

## 5. Rules à capturer (`Dev/Rules/` est vide)

Conventions **ultra-stables** observées dans tous tes projets récents — méritent
d'être figées en règles transverses :

| Nom | Description | Source |
|---|---|---|
| **Rule - Toolchain Python** | `uv` (venv + lock) + `ruff` (lint/format) systématiques ; jamais pip+venv ni flake8/black séparés. | tous projets |
| **Rule - Structure de projet** | `src/` + `tests/` + `documentation/` + `pyproject.toml`, packaging hatchling/setuptools. | Urban-Rivals, MKM, rag-agent-chat |
| **Rule - Config typée** | `pydantic-settings` + `.env` gitignored + `.env.example` versionné ; jamais de secret en dur. | rag-agent-chat, MKM |
| **Rule - Qualité stricte** | ruff lint sélectif (E,F,W,I,B,UP,SIM,N,ANN) + `mypy --strict` + pre-commit + pytest-cov. | rag-agent-chat, rag-ingestion-pipeline |
| **Rule - Packaging démo** | docker-compose multi-services + Makefile (`make train`, `make up`) + `demo.gif` dans le README. | classification_bubbles, RAG_Ollama_Streamlit |

---

## 6. Zones structurellement vides du vault

Constat brut, à toi de décider si tu veux les amorcer :

- `Wiki/Outils/` — **vide**. Le catalogue de skills/outils (le pilier « utiliser ») n'existe pas encore.
- `Wiki/Roadmaps/` — **vide**.
- `Wiki/Workflows/` — **vide**. Aucune procédure capturée alors que tu en répètes (scraping→matching→optim, ingestion RAG, entraînement self-play).
- `Dev/Rules/` — **vide** (cf. §5).
- `Dev/REX/` — un seul fichier (`REX - Postgres`). Beaucoup de tes galères (Playwright/session, WSL2+GPU+Docker, NebulaGraph) ne sont pas capitalisées.

---

## 7. Ordre de traitement suggéré

1. **Grappe « projet phare »** : MCTS → AlphaZero → CFR → Théorie des jeux. Tu l'as codé, la rédaction est ancrée.
2. **Grappe vision** : CNN → architectures CNN → transfer learning → classification audio.
3. **Tronc causal + analyse de survie** : débloque une grappe entière déjà à moitié présente.
4. **Concepts data engineering** : comble l'angle mort le plus large pour ton positionnement.
5. **Services** (§2) : rapides, mécaniques, à faire en lot via `enrichir-brain`.
6. **Patterns + Rules** : capitalise ta signature architecturale.

---

## 8. Grappe « architectures LLM 2026 » (ajout 2026-07-09)

> Source : vidéo *« Le Transformer en passe d'être dépassé ? »* (Alexandre TL, 56 min,
> YouTube `SqyHPlEM40Q`), analysée en détail dans un watch-report local
> (`video-le-transformer-en-passe-detre-depasse.md` = toutes les slides + narration ;
> chaque candidat ci-dessous pointe vers un timestamp précis de la vidéo).
> Non traité — en attente de validation avant création via `enrichir-brain`.

Concepts candidats (`Wiki/Concepts/`), du plus structurant au plus pointu :

| Nom | Description | Lien avec l'existant |
|---|---|---|
| **Attention linéaire** | Attention sans softmax = mémoire associative de taille fixe (Θ(1) calcul/mémoire vs Θ(n)). Cadre unificateur attention ↔ Mamba. Le « paradoxe de Mamba » : efficient mais faible en rappel (MMLU). | complète `Transformer architectures`, `Tokenization` |
| **Architectures hybrides LLM** | Mixer N couches d'attention linéaire pour 1 couche d'attention globale (ratio 3:1-4:1) : le rappel n'est porté que par quelques têtes. Ex. Qwen 3.5, Kimi Linear. | dépend d'Attention linéaire |
| **µP (Maximal Update Parametrization)** | LR ∝ 1/largeur + init ∝ 1/√fan_in → dynamiques d'entraînement identiques à toute échelle, transfert des hyperparamètres petit→grand. | proche de tes fiches optimisation/entraînement |
| **Mixture of Experts (MoE)** | Découpler paramètres totaux (performance, lois d'échelle) et actifs (coût d'inférence) par sparsité. Ex. DeepSeek V3 671B/37B, Kimi K2 1000B/32B. | trou visible : tous les modèles ouverts récents sont MoE |
| **Calculs adaptatifs (early exit, looped transformers)** | Quantité de calcul variable selon la difficulté de l'entrée : Mixture of Depths, HRM/TRM (modèle petit bouclé — biais inductif de raisonnement algorithmique), architectures sans tokenisation (H-Net), RL/effort. | relie `Reasoning`, lois d'échelle |
| **Attention différentielle** | Deux cartes softmax soustraites (λ) pour annuler le « bruit d'attention » corrélé — gains massifs sur needle-in-a-haystack (99.6 % vs 55 % à 4k). | pointu ; optionnel |
| **Gating & règle delta (gestion de mémoire récurrente)** | Les deux mécanismes qui ont fait évoluer Mamba : décroissance exponentielle des associations passées + remplacement chirurgical (DeltaNet → GDN → KDA). | sous-fiche possible d'Attention linéaire |

Suggestion de traitement : les 5 premiers forment une grappe cohérente
(« pourquoi les LLM 2026 ne sont plus des Transformers vanilla ») ; les 2 derniers
peuvent vivre comme sections des fiches parentes plutôt que fiches autonomes.
