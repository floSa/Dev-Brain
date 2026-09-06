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
- **Retours d'expérience** — le pilier REX séparé est supprimé (audit axe 6, option B, le 2026-09-02) : les retours vont dans la section `## Pièges` de la fiche Service. Beaucoup de tes galères (Playwright/session, WSL2+GPU+Docker, NebulaGraph) n'y sont toujours pas capitalisées.

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
> **TRAITÉ le 2026-07-29** via `enrichir-brain` — grappe élargie à la demande de
> l'utilisateur (MCP, quantization, Mamba-3, DSpark, MLA, MTP, AttnRes).

Concepts candidats (`Wiki/Concepts/`), du plus structurant au plus pointu :

| Nom | Description | Statut |
|---|---|---|
| **Attention linéaire** | Attention sans softmax = mémoire associative de taille fixe (Θ(1) calcul/mémoire vs Θ(n)). Cadre unificateur attention ↔ Mamba. Le « paradoxe de Mamba » : efficient mais faible en rappel (MMLU). | ✅ créé |
| **Architectures hybrides LLM** | Mixer N couches d'attention linéaire pour 1 couche d'attention globale (ratio 3:1-4:1) : le rappel n'est porté que par quelques têtes. Ex. Qwen 3.5, Kimi Linear. | ✅ créé |
| **µP (Maximal Update Parametrization)** | LR ∝ 1/largeur + init ∝ 1/√fan_in → dynamiques d'entraînement identiques à toute échelle, transfert des hyperparamètres petit→grand. | ✅ créé (`Maximal Update Parametrization`) |
| **Mixture of Experts (MoE)** | Découpler paramètres totaux (performance, lois d'échelle) et actifs (coût d'inférence) par sparsité. Ex. DeepSeek V3 671B/37B, Kimi K2 1000B/32B. | ✅ la fiche existait — mise à jour 2026 (ratio de sparsité, fine-grained + shared, effet straggler) |
| **Calculs adaptatifs (early exit, looped transformers)** | Quantité de calcul variable selon la difficulté de l'entrée : Mixture of Depths, HRM/TRM (modèle petit bouclé — biais inductif de raisonnement algorithmique), architectures sans tokenisation (H-Net), RL/effort. | ✅ créé |
| **Attention différentielle** | Deux cartes softmax soustraites (λ) pour annuler le « bruit d'attention » corrélé. | ✅ section de `Flash Attention and efficient attention` — chiffres corrigés depuis le papier ICLR 2025 : rappel **85 % vs 55 %**, pas 99,6 % |
| **Gating & règle delta (gestion de mémoire récurrente)** | Les deux mécanismes qui ont fait évoluer Mamba : décroissance exponentielle des associations passées + remplacement chirurgical (DeltaNet → GDN → KDA). | ✅ section de `Attention linéaire` |

Ajouts hors liste initiale, nécessaires à la cohérence de la grappe :

| Nom | Pourquoi | Statut |
|---|---|---|
| **Multi-head Latent Attention** | Trou visible : la fiche Flash Attention couvrait MQA/GQA mais pas MLA, brique DeepSeek et couche globale des hybrides. | ✅ créé |
| **Multi-Token Prediction** | Sans elle, DSpark n'a pas de baseline (MTP-1) et le lien entraînement ↔ décodage spéculatif manque. | ✅ créé |
| **Attention Residuals** | Seule vraie création de la liste demandée par l'utilisateur (Kimi, arXiv 2603.15031). | ✅ créé |
| `mcp-protocol` | La fiche citait la spec 2025-11-25 : périmée par la révision 2026-07-28 (stateless, MRTR, extensions, autorisation durcie). | ✅ mise à jour |
| `Quantization` | Manquaient les formats microscaling natifs (NVFP4/MXFP4) et la bascule du 4 bits vers l'entraînement. | ✅ mise à jour |
| `State Space Models` | S'arrêtait à Mamba-1. | ✅ mise à jour (state space duality + Mamba-3 ICLR 2026) |
| `Speculative decoding` | Manquait DSpark (arXiv 2607.05147) et le lien MTP. | ✅ mise à jour |
| `agent-loops` | Fiche déjà solide ; complétée sur le budget de contexte et les trois échecs types. | ✅ mise à jour |

Corrigés au passage : 7 renvois « (à créer) » pointant vers des fiches désormais
existantes (`Quantization`, `Distillation`, `Speculative decoding`,
`Reasoning models`, `GRPO`, `RL for LLMs`, `Reward modeling`).

### Reste à trancher sur cette grappe

- **Fiche service `Dev/Services/DeepSpec`** (`categorie: ml/optimization`, MIT) — DSpark est
  documenté côté concept, mais le codebase déployable n'a pas sa fiche Dev. Non fait.
- **Renommage des 5 fiches en kebab-case** (`mcp-protocol`, `agent-loops`, `tool-use`,
  `prompt-caching`, `embeddings`) vers la casse du reste du vault. Non fait — demande une
  reprise des wikilinks entrants.

---

## Solveurs d'optimisation — le seul comparatif à un membre du vault

> Ouvert le **2026-09-06**, à la conversion du lot 5. Source : `Analyse` — trou
> repéré dans la cohérence du brain lui-même, pas dans un projet.

`Comparatif - Solveurs d'optimisation` a **un seul membre**, [[PuLP]], et
`check_brain` le signale depuis longtemps (`[WARN] R8b — 1 membre(s) (< 2) —
comparatif sans comparaison`). La conversion en page ne règle rien et **ne rend
pas l'avertissement silencieux** : R8b compte les membres du `.base`, que la page
n'a pas touché. C'est le bon comportement — l'avertissement décrit un fait vrai,
et le fait n'est pas dans la vue, il est dans le vault.

**Le défaut est que le brain n'a pas les autres solveurs.** La fiche `PuLP` en
nomme onze en clair, et aucun n'a de page. Tous relèveraient de
`categorie: math/optimisation` (dossier « Mathématiques/Optimisation/ »),
`famille: paquet` pour les modeleurs Python, `famille: application` ou
`specification` pour les solveurs livrés en binaire.

| Nom | Ce que c'est | Ce que sa fiche apporterait au comparatif |
|---|---|---|
| **Pyomo** | Modeleur Python généraliste (LP, MIP, NLP, MINLP), Sandia/COIN-OR | Le concurrent direct de PuLP, et le seul à couvrir le **non linéaire** — la borne que la fiche PuLP nomme sans avoir la page en face |
| **CVXPY** | Modeleur d'optimisation **convexe** disciplinée (DCP), Stanford | L'autre moitié du non linéaire : quadratique, conique, et la vérification de convexité par construction |
| **`scipy.optimize`** | Optimisation continue de SciPy — `minimize`, `linprog`, moindres carrés | Le point d'entrée sans contraintes linéaires, déjà installé partout, cité par PuLP comme repli |
| **CBC** | Solveur MIP COIN-OR, livré avec PuLP | Le défaut de PuLP : sa performance est ce qui décide de changer de solveur |
| **HiGHS** | Solveur LP/MIP open source moderne, MIT | Le remplaçant crédible de CBC côté OSS — c'est aussi le solveur par défaut de `scipy.linprog` |
| **GLPK** | Solveur LP/MIP GNU, GPL | L'historique ; sa licence GPL est un critère de départage |
| **SCIP** | Solveur MIP/MINLP académique (ZIB), Apache-2.0 depuis la v9 | Le plus rapide des non commerciaux sur MIP, et le seul OSS à faire du MINLP |
| **Gurobi** | Solveur commercial, licence par cœur | La référence de performance, et le nom qui rend l'arbitrage coût/temps réel |
| **CPLEX** | Solveur commercial IBM | Le second du duopole commercial |
| **MOSEK** | Solveur commercial conique/SDP | Le seul à couvrir la programmation semi-définie |
| **XPRESS** | Solveur commercial FICO | Complète la liste des cibles pilotables par PuLP |

Priorité suggérée, par ce qui débloque le plus vite le comparatif : **Pyomo**,
**CVXPY**, **HiGHS** — trois pages suffiraient à faire de cette vue une
comparaison réelle et à éteindre `R8b`. Le reste peut rester des mentions.

Voisinage à câbler à la création (règle de propagation, `brain-v3.md` §10) : le
dossier « Mathématiques/Optimisation/ » porte déjà les notions
`Optimisation sous contrainte`, `Optimisation combinatoire` et
`Programmation linéaire en nombres entiers (MIP)`, plus le hub `Optimisation` —
ce sont elles qu'il faudra relier, et la page
`Comparatif - Solveurs d'optimisation` dont la section « Ce comparatif ne compare
rien » sera alors à retirer.

---

## Ce que le lot 8 verse ici — arrêté le 2026-09-06

> Ouvert le **2026-09-06**, à la clôture du lot 8 et de la migration v3. Source :
> `Analyse` — le lot 8 est un lot de RÈGLES, et tout ce qui suit est du **contenu**.
> C'est la frontière que `lot-8-durcissement.md` pose lui-même : « ne pas durcir une
> règle avec des violations résiduelles », mais pas davantage créer des pages pour
> faire taire un avertissement. Un avertissement se traite comme un sujet.

### 1. Les cinq comparatifs manquants, avec leur axe de départage déjà écrit

Signalés par la conversion du lot 6, qui a lu les 337 fiches à la file. Chacun est
bon marché à ouvrir parce que **ce qui départage est déjà rédigé dans les fiches** —
il reste à l'extraire, pas à le trouver. `check_brain` les signale sous `R8a`.

| Catégorie | Briques | Ce qui départage, déjà écrit | Signalé par |
|---|---|---|---|
| `ml/apprentissage-profond` | **8** | quatre paragraphes « Nuance : … » font mot pour mot le travail d'une section « Ce qui départage » : bas niveau contre structure imposée, moteur d'optimisation contre surcouche, `Fabric` comme pendant d'`accelerate` | lot 6 / 4 |
| `llm/assistant` | 5 | et `Comparatif - Frameworks LLM` les **exclut explicitement** par un commentaire de son propre filtre | lot 6 / 8 |
| `data/format` | 3 | Parquet contre Avro, colonnaire contre ligne ; Iceberg au-dessus des deux, qui n'est pas un format mais une sémantique de table | lot 6 / 13 |
| `data/synthetique` | 3 | Faker contre Mimesis, écosystème contre vitesse ; SDV ailleurs, il apprend une distribution | lot 6 / 13 |
| `compute/a-la-demande` | 3 | Daytona, E2B, Modal partagent un dossier avec quatre moteurs sans partager leur vue | lot 6 / 15 |

**À ouvrir en premier : `ml/apprentissage-profond`.** C'est le plus coûteux des cinq
et pour une raison qui empire avec le temps : faute de comparatif d'accueil, les
quatre « Nuance » ont dû être **repliées en cellules `Écarter si`**. L'information
est conservée, mais éclatée en quatre morceaux qui devront rester d'accord entre eux
— et rien ne le vérifie.

Un sixième trou, d'une autre nature : `Comparatif - Gestionnaires de paquets Python`
ne dit rien de la **vitesse**, alors que `pip → uv` sur la vitesse était la
redirection la plus nette de la fiche `pip`. L'intégration a retenu la borne sur la
fiche ; ajouter la colonne au comparatif reste à faire.

### 2. Les onze filtres de vue trop étroits — `R8e`

`R8e`, née au lot 8, signale **11 briques** qu'une vue a laissées dehors alors
qu'elle retient leurs pairs de la même `categorie:`. Ce n'est pas un manque de
comparatif : le comparatif existe, et son filtre est trop étroit. Le correctif est
d'**élargir le filtre du `.base`**, pas d'écrire une page — donc c'est un travail
d'une ligne par vue, et il est ici parce qu'il touche du contenu de vue.

| Vue | Ce que son filtre rate | Pourquoi |
|---|---|---|
| `ml/tabulaire` | Featuretools, category_encoders, imbalanced-learn | filtre `file.hasTag("boosting")` — les trois ne font pas de boosting |
| `ml/vision` | Kornia, timm, torchvision | filtre `object-detection or segmentation` — les trois sont des socles, pas des tâches |
| `web/backend` | Flask, Uvicorn | |
| `web/frontend` | Jinja2 | |
| `ml/non-supervise` | hdbscan | |
| `ml/socle` | River | |

Les deux premiers groupes ont été trouvés **à la main**, par deux lots différents,
chacun croyant à un cas isolé. C'est ce qui a motivé `R8e`.

### 3. Les 89 briques hors de toute vue — dont 27 sans recours

Décompte du 2026-09-06, sur les 47 vues : **89 briques sur 337 (26 %)** ne sont
membres d'aucune. Elles se décomposent en trois populations, et seule la troisième
n'a pas d'issue :

- **51** relèvent des 13 catégories que `R8a` signale déjà — leur issue est un
  comparatif à créer (§1 ci-dessus en couvre 5) ;
- **11** sont le cas `R8e` — leur issue est un filtre à élargir (§2) ;
- **27** vivent dans une catégorie de **1 ou 2 briques**, où aucun comparatif n'a de
  sens : les seuils sont à 3 briques et 2 membres, et à raison. Leur seule issue est
  de **ficher des voisins** — c'est-à-dire d'enrichir le brain, ce qui est
  exactement le propos de ce fichier. Aucune règle ne les signale, et c'est
  volontaire : 27 avertissements irréparables auraient rendu `R8a` illisible.

Conséquence à ne pas perdre de vue : une brique hors de toute vue garde **toutes**
ses redirections en cellules `Écarter si`, faute de comparatif d'accueil. Ces 89
briques sont donc aussi celles qui pèsent le plus dans le taux de 26 % de cellules
liées qui a rendu la règle 5 du §10 inatteignable dans sa forme d'origine.

### 4. Les 39 champs de frontmatter vides

`build_bandeau.py` les nomme à chaque passage, et depuis le lot 8 il tourne à chaque
clôture — le compte est donc sous les yeux à chaque fois. **34 sont un `maturite:`
seul**, et six lots ont mesuré que le trou suit les **dossiers** saisis sans ce champ,
pas la famille de la brique : c'est un artefact de saisie par lots, pas une
information manquante par nature. Chaque champ vide coûte une colonne de bandeau.

### 5. Les six déclarations d'`alternatives:` que la fiche elle-même démentit

Réciproques et donc valides pour `check_brain` (R12 passe), mais fausses au sens :

- `t3code`, `Spec Kit` et `BMAD` se placent **au-dessus** de ce qu'elles déclarent
  concurrent ;
- `PyTorch Lightning` et `accelerate` déclarent `DeepSpeed` en alternative, alors que
  les trois fiches disent que c'est un **backend** — donc un `complements:`.

Aucune règle ne peut trancher cela : la réciprocité est vérifiable, la justesse d'une
relation ne l'est pas. C'est une relecture.

### 6. Les briques nommées mais non fichées

Relevées par les lots de conversion, qui les citent en clair faute de page à lier.
C'est aussi ce qui interdit d'exiger un wikilink sur toute redirection (règle 5 du
§10) : les rendre obligatoires à ficher serait une décision de contenu déguisée en
décision de format.

- outillage Python : `Click`, `argparse`, `Fire`, `mypy`, `unittest`, `conda`,
  `MkDocs`, `attrs`, `Flake8`, `Black`, `isort`, `pylint`, `Textual`, `colorama`,
  `prompt_toolkit`, `marshmallow`, `cattrs` ;
- réseau et sécurité : `Wireshark`, `rsync`, `Qualys SSL Labs`, `Podman`,
  `Kubernetes` ;
- data et ML : `psycopg 3`, `asyncpg`, `scikit-survival`, `Pyomo`, `verl`,
  `OpenRLHF`, `tiktoken`, `Vowpal Wabbit`, `LightEval` ;
- les onze solveurs de `PuLP` — ils ont leur propre section ci-dessus.

### 7. Deux notions qui citent une catégorie disparue

`Contrats de données & qualité` (cite `data/quality`) et `Versionnage de données`
(cite `data/versioning`) nomment en prose des catégories que la taxonomie ne porte
plus. **Elles n'ont pas été corrigées, et ne doivent pas l'être ici** : ce sont des
pages `role: notion`, la mémoire perso de floSa, et on ne les réécrit pas sans qu'il
l'ait demandé. À lui proposer, pas à faire.
