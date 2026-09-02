---
galaxie: meta
nom: v3-arborescence
type: design-doc
created: 2026-09-04
modified: 2026-09-04
status: en-construction
tags: [meta, design, v3, migration]
---

# DevBrain v3 — Inventaire et arborescence cible

> Document de travail. Il porte **l'arbre sur papier** et se complète au fil de la migration.
> Généré depuis le vault réel, puis annoté à la main. Les cases se cochent lot par lot.

## Comment lire ce document

- Un dossier par **domaine**, nommé avec le libellé français.
- Un sous-dossier quand un sous-domaine atteint **5 pages** — sinon les pages restent
  au niveau du domaine. Règle mécanique, aucun arbitrage.
- Chaque dossier porte une page à son nom, `role: hub`, qui sert d'aiguillage.
- `[b]` brique · `[n]` notion · `[c]` comparatif.
- **À arbitrer** liste les notions dont le sous-domaine reste à dériver page par page.

## Inventaire

| Objet | Nombre | Devient |
|---|---|---|
| `Dev/Services/` + `Dev/Outils/` | 336 | `role: brique` |
| `Wiki/Concepts/` | 299 | `role: notion` |
| `Dev/Patterns/*.base` | 47 | `role: comparatif` (page `.md` + vue embarquée) |
| `Dev/Patterns/Pattern - *.md` | 5 | `role: pattern` |
| `Dev/Rules/` | 5 | `role: rule` |
| `MOC/` | 39 | **supprimé** — absorbé par les pages hub |

**Notions à recatégoriser : 205** — c'est le seul poste de travail non mécanique.

> **État au 2026-09-04.** Lot 3 : **15 domaines sur 20** migrés — le pilote
> « Bases de données » puis les 14 plus petits, soit 121 pages et 19 comparatifs
> descendus dans l'arbre. 524 pages restent sous `Dev/` et `Wiki/`, réparties sur les
> 5 domaines les plus gros : Machine Learning, LLM & IA générative, Data & pipelines,
> Statistiques & inférence, Mathématiques. Ce sont eux qui portent les 205 notions à
> recatégoriser au lot 4.
>
> Le vault porte 668 pages actives et **23 hubs** (15 de domaine, 8 de sous-domaine).
> `MOC/Categories/` ne garde que 5 pages : les 14 autres ont été déplacées par `git mv`
> vers le hub de leur dossier — une MOC de domaine ne disparaît pas, elle *devient* le
> hub (cf. remontée 6 de `lot-3-arborescence.md`). Seule
> `MOC/Categories/Bases de données.md` a réellement disparu, dans la fusion de l'étape 4
> avec la notion chapeau homonyme.
>
> Deux mouvements hors inventaire : `Wiki/Concepts/HDBSCAN.md` est renommée
> `Clustering hiérarchique par densité` (collision de casse avec
> `Dev/Services/hdbscan.md`, impossible sur un système de fichiers Windows), et
> `Wiki/Outils/Obsidian.md` (`skill/knowledge`, aucun domaine dans ce document) rejoint
> « Outils de développement/ » par arbitrage de floSa. `Wiki/Outils/` est vide.
> Plus un seul wikilink qualifié dans le vault.

## Arbre cible

```
SecondBrain/
├── Machine Learning/   (241 pages)
│   ├── Apprentissage profond/   (60)
│   ├── Apprentissage par renforcement/   (23)
│   ├── Séries temporelles/   (20)
│   ├── NLP/   (13)
│   ├── Serving/   (9)
│   ├── Vision/   (9)
│   ├── Suivi d'expériences/   (7)
│   ├── Interprétabilité/   (7)
│   ├── Tabulaire/   (6)
│   └── (20 pages au niveau du domaine)
├── LLM & IA générative/   (131 pages)
│   ├── Agents de code/   (13)
│   ├── Runtimes/   (9)
│   ├── Agents/   (9)
│   ├── Fine-tuning/   (5)
│   ├── Text-to-SQL/   (5)
│   ├── Assistants/   (5)
│   └── (28 pages au niveau du domaine)
├── Bases de données/   (47 pages)
│   ├── Vectoriel/   (11)
│   ├── Administration/   (7)
│   ├── Recherche/   (6)
│   ├── Relationnel/   (6)
│   └── (17 pages au niveau du domaine)
├── Statistiques & inférence/   (47 pages — 10 au lot 3, les 37 notions au lot 4)
│   └── (10 pages au niveau du domaine)
├── Data & pipelines/   (46 pages)
│   ├── Scraping/   (10)
│   ├── Parsing/   (9)
│   ├── Orchestration/   (6)
│   ├── DataFrames/   (5)
│   ├── Visualisation/   (5)
│   └── (11 pages au niveau du domaine)
├── Mathématiques/   (27 pages)
│   └── (1 pages au niveau du domaine)
├── Outils de développement/   (19 pages)
│   ├── Notebooks/   (5)
│   └── (14 pages au niveau du domaine)
├── Signal & audio/   (8 pages — APRÈS lot 4 ; 3 pages et aucun sous-dossier au lot 3,
│   │                    les 5 notions portant encore `concept/signal`)
│   ├── Traitement/   (7)
│   └── (1 pages au niveau du domaine)
├── Design & diagrammes/   (7 pages)
│   ├── Diagrammes/   (5)
│   └── (2 pages au niveau du domaine)
├── Calcul distribué/   (7 pages)
│   └── (7 pages au niveau du domaine)
├── Web & API/   (6 pages)
│   └── (6 pages au niveau du domaine)
├── Stockage/   (6 pages — plafond du seuil, cf. remontée 8)
│   └── (6 pages au niveau du domaine)
├── Automatisation no-code/   (5 pages — plafond du seuil, cf. remontée 8)
│   └── (5 pages au niveau du domaine)
├── Médias/   (4 pages)
│   └── (4 pages au niveau du domaine)
├── Interfaces & apps data/   (4 pages)
│   └── (4 pages au niveau du domaine)
├── Sécurité/   (3 pages)
│   └── (3 pages au niveau du domaine)
├── Observabilité/   (3 pages)
│   └── (3 pages au niveau du domaine)
├── Réseau/   (2 pages)
│   └── (2 pages au niveau du domaine)
├── Documents/   (2 pages)
│   └── (2 pages au niveau du domaine)
├── DevOps/   (2 pages)
│   └── (2 pages au niveau du domaine)
```

## Détail par domaine

### Machine Learning  ·  241 pages

- [ ] hub écrit · [ ] sous-dossiers créés · [ ] notions recatégorisées · [ ] fiches au nouveau gabarit

**Apprentissage profond/** — `ml/apprentissage-profond` — 60 pages

- `[n]` Adam optimizer
- `[n]` Apprentissage auto-supervisé en vision
- `[n]` Architectures CNN
- `[n]` Architectures hybrides LLM
- `[n]` Attention Residuals
- `[n]` Attention linéaire
- `[n]` Attribution par gradient
- `[n]` Augmentation d'images
- `[n]` Autoencodeurs
- `[n]` CNN
- `[n]` Calculs adaptatifs
- `[n]` Classification audio par spectrogramme
- `[n]` Classification d'images
- `[b]` DeepSpeed — paquet, Python
- `[n]` Diffusion models
- `[n]` Distillation
- `[n]` Détection d'objets
- `[n]` Entraînement distribué
- `[n]` Estimation de pose
- `[n]` Flash Attention and efficient attention
- `[n]` GANs
- `[n]` Gradient checkpointing
- `[n]` Graph Neural Networks
- `[n]` Image generation
- `[n]` Interprétabilité mécaniste
- `[b]` JAX — paquet, Python
- `[b]` Keras — paquet, Python
- `[n]` Kolmogorov-Arnold Networks
- `[n]` Maximal Update Parametrization
- `[n]` Metric learning & ré-identification
- `[n]` Mixed precision
- `[n]` Mixture of Experts
- `[n]` Modèles de fondation vision
- `[n]` Multi-head Latent Attention
- `[n]` Métriques vision
- `[n]` OCR
- `[n]` Positional encoding
- `[n]` Probing
- `[n]` Pruning
- `[b]` PyTorch — paquet, C++/Python
- `[b]` PyTorch Lightning — paquet, Python
- `[n]` Quantization
- `[n]` Rendu neuronal 3D & estimation de profondeur
- `[n]` Segment Anything (SAM)
- `[n]` Segmentation
- `[n]` Self-attention
- `[n]` Sparse autoencoders
- `[n]` Speech models
- `[n]` State Space Models
- `[n]` Suivi d'objets
- `[n]` Superposition
- `[b]` TensorFlow — paquet, C++/Python
- `[n]` Transfer learning vision
- `[n]` Transformer architectures
- `[n]` Video generation
- `[n]` Vision Language Models
- `[n]` Vision Transformers (ViT)
- `[n]` Vision par ordinateur
- `[b]` accelerate — paquet, Python
- `[b]` pykan — paquet, Python

**Apprentissage par renforcement/** — `ml/rl` — 23 pages

- `[b]` Acme — paquet, Python
- `[n]` Actor-Critic methods
- `[n]` AlphaZero and self-play
- `[n]` Bellman equations
- `[n]` Counterfactual Regret Minimization
- `[n]` Exploration vs exploitation
- `[b]` Gymnasium — paquet, Python
- `[n]` Imitation learning
- `[n]` Markov Decision Process
- `[n]` Model-based RL
- `[n]` Monte Carlo Tree Search
- `[n]` Offline RL
- `[b]` OpenSpiel — paquet, Python
- `[n]` PPO
- `[n]` Policy gradient
- `[n]` Q-learning and DQN
- `[b]` RLax — paquet, Python
- `[n]` Reinforcement learning
- `[n]` Reward shaping and hacking
- `[b]` Stable-Baselines3 — paquet, Python
- `[b]` TF-Agents — paquet, Python
- `[n]` Théorie des jeux
- `[n]` Value functions

**Séries temporelles/** — `ml/series-temporelles` — 20 pages

- `[n]` ARIMA SARIMA
- `[n]` Autocorrelation
- `[b]` Chronos — modele, Python
- `[n]` Exponential smoothing
- `[n]` Forecasting framing
- `[n]` Forecasting metrics
- `[n]` Foundation models pour séries temporelles
- `[n]` Hierarchical forecasting
- `[n]` Intermittent demand
- `[n]` Maintenance prédictive et RUL
- `[b]` Prophet — paquet, Python/R
- `[b]` STUMPY — paquet, Python
- `[n]` Stationarity
- `[n]` Time series anomaly detection
- `[n]` Time series feature engineering
- `[n]` Walk-forward CV
- `[b]` darts — paquet, Python
- `[b]` neuralforecast — paquet, Python
- `[b]` pmdarima — paquet, Python
- `[b]` statsforecast — paquet, Python

**NLP/** — `ml/nlp` — 13 pages

- `[n]` BM25
- `[n]` Classification de texte
- `[n]` Fuzzy matching & similarité de chaînes
- `[b]` GLiNER — modele, Python
- `[n]` NER et étiquetage de séquence
- `[b]` NLTK — paquet, Python
- `[n]` Recherche d'information
- `[b]` SetFit — paquet, Python
- `[n]` TF-IDF
- `[n]` Traitement du langage naturel
- `[b]` pytorch-crf — paquet, Python
- `[b]` sentencepiece — paquet, C++/Python
- `[b]` spaCy — paquet, Python

**Serving/** — `ml/serving` — 9 pages

- `[b]` BentoML — plateforme, Python
- `[b]` KServe — plateforme, Go
- `[b]` NVIDIA Triton — plateforme, C++
- `[b]` ONNX Runtime — paquet, C++
- `[b]` Ray Serve — plateforme, Python
- `[b]` Seldon Core — plateforme, Go
- `[b]` TensorFlow Serving — plateforme, C++
- `[b]` TensorRT — paquet, C++
- `[b]` TorchServe — plateforme, Java/Python

**Vision/** — `ml/vision` — 9 pages

- `[b]` Detectron2 — paquet, Python/C++
- `[b]` Kornia — paquet, Python
- `[b]` OpenCV — paquet, C++
- `[b]` Ultralytics YOLO — modele, Python
- `[b]` albumentations — paquet, Python
- `[b]` segment-anything — modele, Python
- `[b]` supervision — paquet, Python
- `[b]` timm — paquet, Python
- `[b]` torchvision — paquet, Python/C++

**Suivi d'expériences/** — `ml/tracking` — 7 pages

- `[b]` Aim — plateforme, Python
- `[b]` ClearML — plateforme, Python
- `[b]` Comet — plateforme, Python
- `[b]` MLflow — plateforme, Python
- `[b]` Neptune — plateforme, Python
- `[b]` TensorBoard — application, Python
- `[b]` Weights & Biases — plateforme, Python

**Interprétabilité/** — `ml/interpretabilite` — 7 pages

- `[b]` Captum — paquet, Python
- `[b]` LIME — paquet, Python
- `[b]` SAELens — paquet, Python
- `[b]` SHAP — paquet, Python
- `[b]` TransformerLens — paquet, Python
- `[b]` interpreto — paquet, Python
- `[b]` nnsight — paquet, Python

**Tabulaire/** — `ml/tabulaire` — 6 pages

- `[b]` CatBoost — paquet, C++
- `[b]` Featuretools — paquet, Python
- `[b]` LightGBM — paquet, C++
- `[b]` XGBoost — paquet, C++
- `[b]` category_encoders — paquet, Python
- `[b]` imbalanced-learn — paquet, Python

**Au niveau du domaine** — 20 pages

- `[b]` Evidently — paquet, Python
- `[b]` Feast — plateforme, Python
- `[b]` Flyte — plateforme, Go
- `[b]` HuggingFace — saas, Python
- `[b]` Hyperopt — paquet, Python
- `[b]` Metaflow — plateforme, Python
- `[b]` Optuna — paquet, Python
- `[b]` PaCMAP — paquet, Python
- `[b]` PyOD — paquet, Python
- `[b]` PyTorch Geometric — paquet, Python
- `[b]` Ray Tune — paquet, Python
- `[b]` River — paquet, Python
- `[b]` Scikit-Learn — paquet, Python
- `[b]` ZenML — plateforme, Python
- `[b]` datasets — paquet, Python
- `[b]` evaluate — paquet, Python
- `[b]` hdbscan — paquet, Python
- `[b]` sentence-transformers — paquet, Python
- `[b]` seqeval — paquet, Python
- `[b]` umap-learn — paquet, Python

**Comparatifs** — 6

- `[c]` Comparatif - Explicabilité — filtre `ml/interpretabilite`
- `[c]` Comparatif - Optimisation d'hyperparamètres — filtre `ml/hyperopt`
- `[c]` Comparatif - Orchestrateurs ML — filtre `ml/orchestration`
- `[c]` Comparatif - Reinforcement learning — filtre `ml/rl`
- `[c]` Comparatif - Serving de modèles — filtre `ml/serving`
- `[c]` Comparatif - Suivi d'expériences ML — filtre `ml/tracking`

**À arbitrer — 67 notions sans sous-domaine**

- [ ] `[n]` AdaBoost
- [ ] `[n]` Analyse discriminante
- [ ] `[n]` Apprentissage non supervisé
- [ ] `[n]` Apprentissage supervisé
- [ ] `[n]` Arbres de décision
- [ ] `[n]` Bagging
- [ ] `[n]` Boosting
- [ ] `[n]` Calibration
- [ ] `[n]` Classification
- [ ] `[n]` Classification hiérarchique (CAH)
- [ ] `[n]` Classification metrics
- [ ] `[n]` Clustering
- [ ] `[n]` Clustering evaluation
- [ ] `[n]` Compromis biais-variance
- [ ] `[n]` DBSCAN
- [ ] `[n]` Data drift
- [ ] `[n]` Data leakage
- [ ] `[n]` Déploiement de modèles
- [ ] `[n]` Détection d'outliers multivariée
- [ ] `[n]` Détection d'outliers univariée
- [ ] `[n]` EDA automatisée & profiling
- [ ] `[n]` Encodage des variables catégorielles
- [ ] `[n]` Ensembling
- [ ] `[n]` Explicabilité des modèles
- [ ] `[n]` Extra Trees
- [ ] `[n]` Feature store — concept
- [ ] `[n]` GAM
- [ ] `[n]` GLM
- [ ] `[n]` Gaussian Mixture Models (GMM)
- [ ] `[n]` Gaussian Process
- [ ] `[n]` Gradient Boosting (GBDT)
- [ ] `[n]` HDBSCAN
- [ ] `[n]` ICA
- [ ] `[n]` Imbalanced classification
- [ ] `[n]` Imputation des valeurs manquantes
- [ ] `[n]` Ingénierie des caractéristiques
- [ ] `[n]` Isolation Forest
- [ ] `[n]` K-Means
- [ ] `[n]` Local Outlier Factor
- [ ] `[n]` Mise à l'échelle
- [ ] `[n]` Model registry & versioning
- [ ] `[n]` Monitoring de modèle en production
- [ ] `[n]` Mécanismes de données manquantes
- [ ] `[n]` NMF
- [ ] `[n]` Naive Bayes
- [ ] `[n]` One-Class SVM
- [ ] `[n]` Optimisation d'hyperparamètres
- [ ] `[n]` Perceptron et MLP
- [ ] `[n]` ROC-AUC & courbe PR
- [ ] `[n]` Random Forest
- [ ] `[n]` Ranking metrics
- [ ] `[n]` Regression metrics
- [ ] `[n]` Régression
- [ ] `[n]` Régression et classification multi-sorties
- [ ] `[n]` Régression linéaire
- [ ] `[n]` Régression logistique
- [ ] `[n]` Régression quantile
- [ ] `[n]` Régularisation
- [ ] `[n]` SVM
- [ ] `[n]` Systèmes de recommandation
- [ ] `[n]` Sélection de variables
- [ ] `[n]` Types de données et choix de modèle
- [ ] `[n]` Validation croisée
- [ ] `[n]` embeddings
- [ ] `[n]` k-NN
- [ ] `[n]` k-médoïds (PAM)
- [ ] `[n]` t-SNE and UMAP

### LLM & IA générative  ·  131 pages

- [ ] hub écrit · [ ] sous-dossiers créés · [ ] notions recatégorisées · [ ] fiches au nouveau gabarit

**Agents de code/** — `llm/agent-de-code` — 13 pages

- `[b]` Aider — cli, Python
- `[b]` BMAD — extension, JavaScript
- `[b]` Cline — extension, TypeScript
- `[b]` Continue — extension, TypeScript, Kotlin
- `[b]` Graphify — cli, Python
- `[b]` Maka — application, TypeScript
- `[b]` Spec Kit — extension, Python
- `[b]` ai-memory — plateforme, Rust
- `[b]` freebuff — cli, TypeScript
- `[b]` i-have-adhd — extension, Markdown
- `[b]` pi — cli, TypeScript
- `[b]` swarm-forge — cli, Clojure
- `[b]` t3code — application, TypeScript

**Runtimes/** — `llm/runtime` — 9 pages

- `[b]` LM Studio — application
- `[b]` Ollama — plateforme, Go
- `[b]` SGLang — plateforme, Python
- `[b]` TGI — plateforme, Rust/Python
- `[b]` TensorRT-LLM — paquet, C++/Python
- `[b]` llama.cpp — plateforme, C/C++
- `[b]` needle — modele, Python
- `[b]` text-generation-webui — application, Python
- `[b]` vLLM — plateforme, Python

**Agents/** — `llm/agents` — 9 pages

- `[b]` Agno — paquet, Python
- `[b]` AutoGen — paquet, "Python, .NET"
- `[b]` CrewAI — paquet, Python
- `[b]` LangGraph — paquet, Python
- `[b]` OpenAI Agents SDK — paquet, "Python, TypeScript"
- `[b]` PraisonAI — paquet, "Python, JavaScript"
- `[b]` PydanticAI — paquet, Python
- `[b]` Semantic Kernel — paquet, "C#, Python, Java"
- `[b]` smolagents — paquet, Python

**Fine-tuning/** — `llm/finetuning` — 5 pages

- `[b]` Axolotl — cli, Python
- `[b]` LLaMA-Factory — cli, Python
- `[b]` TRL — paquet, Python
- `[b]` Tunix — paquet, Python
- `[b]` Unsloth — paquet, Python

**Text-to-SQL/** — `llm/text-to-sql` — 5 pages

- `[b]` DB-GPT — plateforme, Python
- `[b]` LangChain SQL agent — paquet, Python
- `[b]` LlamaIndex NLSQLTableQueryEngine — paquet, Python
- `[b]` Vanna — paquet, Python
- `[b]` WrenAI — plateforme, Python, Rust

**Assistants/** — `llm/assistant` — 5 pages

- `[b]` Hermes Agent — plateforme, "Python, TypeScript"
- `[b]` LM Studio Bionic — application
- `[b]` OpenClaw — plateforme, "TypeScript, Swift"
- `[b]` OpenHands — plateforme, "Python, TypeScript"
- `[b]` OpenMAIC — application, TypeScript

**Au niveau du domaine** — 28 pages

- `[b]` DSPy — paquet, Python
- `[b]` DeepEval — paquet, Python
- `[b]` Dify — plateforme, Python
- `[b]` Flowise — plateforme, TypeScript
- `[b]` Guidance — paquet, Python
- `[b]` Haystack — paquet, Python
- `[b]` Headroom — paquet, "Python, TypeScript, Rust"
- `[b]` Helicone — plateforme, TypeScript
- `[b]` Instructor — paquet, Python
- `[b]` LangChain — paquet, Python
- `[b]` LangSmith — plateforme
- `[b]` Langflow — plateforme, Python
- `[b]` Langfuse — plateforme, TypeScript
- `[b]` Letta — plateforme, Python
- `[b]` LiteLLM — plateforme, Python
- `[b]` LlamaIndex — paquet, Python
- `[b]` OmniRoute — plateforme, TypeScript
- `[b]` OpenRouter — saas
- `[b]` OpenViking — plateforme, Python
- `[b]` Outlines — paquet, Python
- `[b]` Phoenix Arize — plateforme, Python
- `[b]` RAGatouille — paquet, Python
- `[b]` Ragas — paquet, Python
- `[b]` TruLens — paquet, Python
- `[b]` fastmcp — paquet, Python
- `[b]` llmfit — cli, Rust
- `[b]` mcpjam — application, TypeScript
- `[b]` promptfoo — cli, TypeScript

**Comparatifs** — 7

- `[c]` Comparatif - Assistants de code IA — filtre `llm/agent-de-code`
- `[c]` Comparatif - Exécution & serving LLM — filtre `llm/runtime`
- `[c]` Comparatif - Fine-tuning LLM — filtre `llm/finetuning`
- `[c]` Comparatif - Frameworks LLM — filtre `llm/agents, llm/rag, llm/socle, llm/sortie-structuree`
- `[c]` Comparatif - Frameworks text-to-SQL — filtre `llm/text-to-sql`
- `[c]` Comparatif - Observabilité LLM — filtre `llm/observabilite`
- `[c]` Comparatif - Évaluation LLM — filtre `llm/eval`

**À arbitrer — 57 notions sans sous-domaine**

- [ ] `[n]` Advanced RAG
- [ ] `[n]` Agent evaluation
- [ ] `[n]` Agent memory
- [ ] `[n]` Agent patterns
- [ ] `[n]` Agent skills
- [ ] `[n]` Chain-of-Thought
- [ ] `[n]` Chunking strategies
- [ ] `[n]` Code and math benchmarks
- [ ] `[n]` Constrained decoding
- [ ] `[n]` Construction de graphes de connaissances
- [ ] `[n]` Context engineering
- [ ] `[n]` Decoding strategies
- [ ] `[n]` GRPO
- [ ] `[n]` GraphRAG
- [ ] `[n]` Harnais d'agent
- [ ] `[n]` Human-in-the-loop
- [ ] `[n]` Hybrid retrieval
- [ ] `[n]` Inference optimization
- [ ] `[n]` LLM benchmarks
- [ ] `[n]` LLM caching
- [ ] `[n]` LLM eval metrics
- [ ] `[n]` LLM observability
- [ ] `[n]` LLM-as-judge
- [ ] `[n]` Late-interaction retrieval
- [ ] `[n]` LoRA et QLoRA
- [ ] `[n]` Multi-Token Prediction
- [ ] `[n]` Multi-agent systems
- [ ] `[n]` PEFT
- [ ] `[n]` Perplexity
- [ ] `[n]` Prompt engineering
- [ ] `[n]` Query transformations
- [ ] `[n]` RAG
- [ ] `[n]` RAG benchmarks
- [ ] `[n]` RAG eval
- [ ] `[n]` RL for LLMs
- [ ] `[n]` RLHF and DPO
- [ ] `[n]` Reasoning models
- [ ] `[n]` Reliability patterns
- [ ] `[n]` Reranking
- [ ] `[n]` Reward modeling
- [ ] `[n]` Routing and cascading
- [ ] `[n]` SFT
- [ ] `[n]` Sandboxing de code généré
- [ ] `[n]` Scaling laws
- [ ] `[n]` Server-Sent Events & streaming LLM
- [ ] `[n]` Small Language Models
- [ ] `[n]` Speculative decoding
- [ ] `[n]` Structured outputs
- [ ] `[n]` Synthetic data generation
- [ ] `[n]` Text-to-SQL
- [ ] `[n]` Tokenization
- [ ] `[n]` Tool use patterns
- [ ] `[n]` a2a-protocol
- [ ] `[n]` agent-loops
- [ ] `[n]` mcp-protocol
- [ ] `[n]` prompt-caching
- [ ] `[n]` tool-use

### Bases de données  ·  47 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — les 4 sous-hubs sont écrits ; le hub de domaine porte le corps de la
  notion fusionnée, à passer au gabarit §9 au lot 6
- [x] sous-dossiers créés — `Vectoriel/` (11), `Administration/` (7), `Recherche/` (6),
  `Relationnel/` (6) ; 17 pages au niveau du domaine, plus les 10 comparatifs
- [ ] notions recatégorisées — lot 4 ; l'arbre ne porte que des briques aujourd'hui
- [ ] fiches au nouveau gabarit — lot 6

**Vectoriel/** — `database/vecteur` — 11 pages

- `[b]` Annoy — paquet, C++
- `[b]` Chroma — paquet, Rust
- `[b]` Faiss — paquet, C++
- `[b]` LanceDB — paquet, Rust
- `[b]` Milvus — plateforme, Go
- `[b]` Pinecone — saas, Rust
- `[b]` Qdrant — plateforme, Rust
- `[b]` ScaNN — paquet, C++
- `[b]` Weaviate — plateforme, Go
- `[b]` hnswlib — paquet, C++
- `[b]` pgvector — extension, C

**Administration/** — `database/admin` — 7 pages

- `[b]` DBeaver — application, Java
- `[b]` DataGrip — application, Java/Kotlin
- `[b]` HeidiSQL — application, Delphi
- `[b]` MongoDB Compass — application, TypeScript/Electron
- `[b]` MySQL Workbench — application, C++
- `[b]` Redis Insight — application, TypeScript/Electron
- `[b]` pgAdmin — application, Python

**Recherche/** — `database/recherche` — 6 pages

- `[b]` Elasticsearch — plateforme, Java
- `[b]` Marqo — plateforme, Python/Java
- `[b]` Vespa — plateforme, Java/C++
- `[b]` bm25s — paquet, Python
- `[b]` rank-bm25 — paquet, Python
- `[b]` txtai — paquet, Python

**Relationnel/** — `database/relationnel` — 6 pages

- `[b]` CockroachDB — plateforme, Go
- `[b]` MariaDB — plateforme, C/C++
- `[b]` Microsoft SQL Server — plateforme, C++
- `[b]` MySQL — plateforme, C/C++
- `[b]` Postgres — plateforme, C
- `[b]` SQLite — paquet, C

**Au niveau du domaine** — 17 pages

- `[b]` ADBC — specification, C / Go / Java
- `[b]` Alembic — paquet, Python
- `[b]` Apache Cassandra — plateforme, Java
- `[b]` ClickHouse — plateforme, C++
- `[b]` DuckDB — paquet, C++
- `[b]` Flyway — cli, Java
- `[b]` InfluxDB — plateforme, Rust
- `[b]` Liquibase — cli, Java
- `[b]` MongoDB — plateforme, C++
- `[b]` Nebula Graph — plateforme, C++
- `[b]` Neo4j — plateforme, Java
- `[b]` Prisma — paquet, TypeScript
- `[b]` Redis — plateforme, C
- `[b]` SQLAlchemy — paquet, Python
- `[b]` SQLModel — paquet, Python
- `[b]` TimescaleDB — extension, C
- `[b]` psycopg2 — paquet, C/Python

**Comparatifs** — 10

- `[c]` Comparatif - Bases colonnes — filtre `database/analytique`
- `[c]` Comparatif - Bases graphes — filtre `database/graphe`
- `[c]` Comparatif - Bases NoSQL — filtre `database/cle-valeur, database/document`
- `[c]` Comparatif - Bases relationnelles — filtre `database/relationnel`
- `[c]` Comparatif - Bases temporelles — filtre `database/series-temporelles`
- `[c]` Comparatif - Bases vectorielles — filtre `database/vecteur`
- `[c]` Comparatif - Clients de bases de données — filtre `database/admin`
- `[c]` Comparatif - Migrations de schéma — filtre `database/migration`
- `[c]` Comparatif - Moteurs de recherche — filtre `database/recherche`
- `[c]` Comparatif - ORM — filtre `database/orm`

### Statistiques & inférence  ·  47 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/` par `git mv`, corps réécrit
  au gabarit §9
- [x] sous-dossiers créés — **aucun**. Les 4 sous-domaines `stats/*` plafonnent à 4 pages
  (`stats/inference`), sous le seuil de 5 : les 10 briques restent au niveau du domaine
- [ ] notions recatégorisées — **lot 4** : les 37 notions ci-dessous portent `concept/stats`
  et sont encore sous `Wiki/Concepts/`. Le hub les cite en clair dans son corps
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 10 pages

- `[b]` ArviZ — paquet, Python
- `[b]` CausalImpact — paquet, Python
- `[b]` Fanalysis — paquet, Python
- `[b]` Prince — paquet, Python
- `[b]` PyMC — paquet, Python
- `[b]` Stan — paquet, C++ / Python
- `[b]` lifelines — paquet, Python
- `[b]` pingouin — paquet, Python
- `[b]` scipy.stats — paquet, Python
- `[b]` statsmodels — paquet, Python

**Comparatifs** — 1

- `[c]` Comparatif - Outils stats — filtre `stats/`

**À arbitrer — 37 notions sans sous-domaine**

- [ ] `[n]` A priori conjugués
- [ ] `[n]` A-B testing
- [ ] `[n]` Analyse de puissance
- [ ] `[n]` Analyse de survie
- [ ] `[n]` Bootstrap
- [ ] `[n]` CA
- [ ] `[n]` CUPED
- [ ] `[n]` Chaînes de Markov
- [ ] `[n]` Correction des tests multiples
- [ ] `[n]` Diff-in-Diff
- [ ] `[n]` Estimation MAP
- [ ] `[n]` FAMD
- [ ] `[n]` GPA
- [ ] `[n]` HCPC
- [ ] `[n]` Inférence bayésienne
- [ ] `[n]` Inférence causale
- [ ] `[n]` Intervalles de confiance
- [ ] `[n]` Inégalités de concentration
- [ ] `[n]` Loi des grands nombres
- [ ] `[n]` MANOVA et tests multivariés
- [ ] `[n]` MCA
- [ ] `[n]` MCMC
- [ ] `[n]` MFA
- [ ] `[n]` Manifold learning
- [ ] `[n]` Maximum de vraisemblance
- [ ] `[n]` Mouvement brownien
- [ ] `[n]` Multi-armed bandits
- [ ] `[n]` PCA
- [ ] `[n]` PGA
- [ ] `[n]` Processus de Poisson
- [ ] `[n]` Réduction de dimension
- [ ] `[n]` Sequential testing
- [ ] `[n]` Test du khi-deux
- [ ] `[n]` Test t et ANOVA
- [ ] `[n]` Tests d'hypothèse
- [ ] `[n]` Tests non paramétriques
- [ ] `[n]` Théorème central limite

### Data & pipelines  ·  46 pages

- [ ] hub écrit · [ ] sous-dossiers créés · [ ] notions recatégorisées · [ ] fiches au nouveau gabarit

**Scraping/** — `data/scraping` — 10 pages

- `[b]` Crawlee — paquet, TypeScript
- `[b]` Firecrawl — plateforme, TypeScript
- `[b]` Maxun — application, TypeScript
- `[b]` Playwright — paquet, Python
- `[b]` Scrapling — paquet, Python
- `[b]` Scrapy — paquet, Python
- `[b]` cloudscraper — paquet, Python
- `[b]` curl_cffi — paquet, Python
- `[b]` minim — paquet, Python
- `[b]` selectolax — paquet, Python

**Parsing/** — `data/parsing` — 9 pages

- `[b]` Docling — paquet, Python
- `[b]` LlamaParse — saas, Python
- `[b]` Marker — paquet, Python
- `[b]` OpenDataLoader PDF — paquet, Java
- `[b]` PyMuPDF — paquet, C / Python
- `[b]` Unstructured — paquet, Python
- `[b]` docTR — paquet, Python
- `[b]` pdf-inspector — paquet, Rust
- `[b]` pdfplumber — paquet, Python

**Orchestration/** — `data/orchestration` — 6 pages

- `[b]` Airflow — plateforme, Python
- `[b]` Dagster — plateforme, Python
- `[b]` Kestra — plateforme, Java
- `[b]` Mage — plateforme, Python
- `[b]` Prefect — plateforme, Python
- `[b]` Temporal — plateforme, Go

**DataFrames/** — `data/tableau` — 5 pages

- `[b]` Modin — paquet, Python
- `[b]` Polars — paquet, Rust
- `[b]` numpy — paquet, C / Python
- `[b]` pandas — paquet, Python / Cython
- `[b]` xarray — paquet, Python

**Visualisation/** — `data/viz` — 5 pages

- `[b]` altair — paquet, Python
- `[b]` bokeh — paquet, Python / TypeScript
- `[b]` matplotlib — paquet, Python / C++
- `[b]` plotly — paquet, Python / JavaScript
- `[b]` seaborn — paquet, Python

**Au niveau du domaine** — 11 pages

- `[b]` Apache Iceberg — specification, Java
- `[b]` Avro — specification, Java
- `[b]` Faker — paquet, Python
- `[b]` Flink — plateforme, Java
- `[b]` Mimesis — paquet, Python
- `[b]` Parquet — specification, Java
- `[b]` SDV — paquet, Python
- `[b]` connectorx — paquet, Rust
- `[b]` missingno — paquet, Python
- `[b]` sweetviz — paquet, Python
- `[b]` ydata-profiling — paquet, Python

**Comparatifs** — 6

- `[c]` Comparatif - Manipulation de données — filtre `data/tableau`
- `[c]` Comparatif - Orchestrateurs data — filtre `data/orchestration`
- `[c]` Comparatif - Outils EDA - profiling — filtre `data/eda`
- `[c]` Comparatif - Parsing de documents — filtre `data/parsing`
- `[c]` Comparatif - Scraping — filtre `data/scraping`
- `[c]` Comparatif - Visualisation — filtre `data/viz`

### Mathématiques  ·  27 pages

- [ ] hub écrit · [ ] sous-dossiers créés · [ ] notions recatégorisées · [ ] fiches au nouveau gabarit

**Au niveau du domaine** — 1 pages

- `[b]` PuLP — paquet, Python

**Comparatifs** — 1

- `[c]` Comparatif - Solveurs d'optimisation — filtre `math/optimisation`

**À arbitrer — 26 notions sans sous-domaine**

- [ ] `[n]` Convexity
- [ ] `[n]` Cross-entropy
- [ ] `[n]` Eigendecomposition
- [ ] `[n]` Generalization bounds
- [ ] `[n]` Gradient descent
- [ ] `[n]` Jensen-Shannon divergence
- [ ] `[n]` KL divergence
- [ ] `[n]` Learning rate schedules
- [ ] `[n]` Loss landscape and saddle points
- [ ] `[n]` Matrix decompositions
- [ ] `[n]` Matrix products
- [ ] `[n]` Mutual information
- [ ] `[n]` Newton & quasi-Newton
- [ ] `[n]` No Free Lunch theorem
- [ ] `[n]` Optimal transport
- [ ] `[n]` Optimisation combinatoire
- [ ] `[n]` Optimisation sous contrainte
- [ ] `[n]` PAC learning
- [ ] `[n]` Programmation linéaire en nombres entiers (MIP)
- [ ] `[n]` Projections
- [ ] `[n]` Rademacher complexity
- [ ] `[n]` SVD
- [ ] `[n]` Shannon entropy
- [ ] `[n]` VC dimension
- [ ] `[n]` Vector norms
- [ ] `[n]` Wasserstein distance

### Outils de développement  ·  19 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine (issu de `MOC/Categories/`) et sous-hub `Notebooks`
- [x] sous-dossiers créés — `Notebooks/` (5) ; 15 pages au niveau du domaine, plus 3
  comparatifs (`Clients d'API`, `Gestionnaires de paquets Python`, `Frameworks CLI`)
- [x] **20 pages, pas 19** — `Wiki/Outils/Obsidian.md` (`skill/knowledge`) est rattachée
  ici par arbitrage de floSa ; ce tableau ne la comptait pas
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Notebooks/** — `devtools/notebook` — 5 pages

- `[b]` Marimo — application, Python
- `[b]` Quarto — cli, TypeScript
- `[b]` jupysql — extension, Python
- `[b]` jupytext — paquet, Python
- `[b]` papermill — paquet, Python

**Au niveau du domaine** — 14 pages

- `[b]` Bruno — application, JavaScript (Electron)
- `[b]` Postman — saas, JavaScript (Electron)
- `[b]` Pydantic — paquet, Python / Rust
- `[b]` Pydantic Settings — paquet, Python
- `[b]` Rich — paquet, Python
- `[b]` Ruff — cli, Rust
- `[b]` Typer — paquet, Python
- `[b]` dynaconf — paquet, Python
- `[b]` hydra — paquet, Python
- `[b]` pip — cli, Python
- `[b]` pytest — paquet, Python
- `[b]` python-dotenv — paquet, Python
- `[b]` testcontainers — paquet, Python
- `[b]` uv — cli, Rust

**Comparatifs** — 2

- `[c]` Comparatif - Clients d'API — filtre `devtools/client-api`
- `[c]` Comparatif - Gestionnaires de paquets Python — filtre `devtools/paquet`

### Signal & audio  ·  8 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — **aucun** : seules 3 pages sont descendues, pas 8. Les 5
  notions listées ci-dessous portent `concept/signal` et non `signal/traitement` ; leur
  recatégorisation est le lot 4, et le seuil de 5 n'est donc pas atteint par les 2 briques
  `signal/traitement` restantes. Le sous-dossier `Traitement/` décrit l'état visé APRÈS
  le lot 4 — même écart que `Bases de données vectorielles`
- [x] comparatif rattaché — `Comparatif - Traitement du signal`, dont le filtre de chemin
  cassait au déplacement (cf. remontée 7 du lot 3)
- [ ] notions recatégorisées — lot 4, les 5 notions de ce tableau
- [ ] fiches au nouveau gabarit — lot 6

**Traitement/** — `signal/traitement` — 7 pages

- `[n]` Filtrage numérique
- `[n]` Ondelettes
- `[b]` PyWavelets — paquet, C / Cython / Python
- `[n]` STFT et spectrogramme
- `[n]` Traitement du signal
- `[n]` Transformée de Fourier
- `[b]` scipy.signal — paquet, C / Fortran / Python

**Au niveau du domaine** — 1 pages

- `[b]` librosa — paquet, Python

### Design & diagrammes  ·  7 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine (issu de `MOC/Categories/`) et sous-hub `Diagrammes`
- [x] sous-dossiers créés — `Diagrammes/` (5 + 1 comparatif) ; 2 pages et 1 comparatif au
  niveau du domaine
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Diagrammes/** — `design/diagramme` — 5 pages

- `[b]` Archify — extension, JavaScript
- `[b]` Excalidraw — application, TypeScript
- `[b]` FossFLOW — application, TypeScript
- `[b]` Mermaid — extension, JavaScript
- `[b]` draw.io — application, JavaScript

**Au niveau du domaine** — 2 pages

- `[b]` Figma — saas
- `[b]` Penpot — application, Clojure, JavaScript

**Comparatifs** — 2

- `[c]` Comparatif - Design & prototypage — filtre `design/ui`
- `[c]` Comparatif - Diagrammes — filtre `design/diagramme`

### Calcul distribué  ·  7 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun, aucun sous-domaine n'atteint 5 pages
  (`compute/a-la-demande` 3, `compute/distribue` 3, `compute/gpu` 1)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 7 pages

- `[b]` CuPy — paquet, Python / C++ / CUDA
- `[b]` Dask — paquet, Python
- `[b]` Daytona — saas, "TypeScript, Go"
- `[b]` E2B — plateforme, "TypeScript, Python, Go"
- `[b]` Modal — saas, "Python, JavaScript, Go"
- `[b]` Ray — paquet, Python / C++
- `[b]` Spark — plateforme, Scala / JVM

**Comparatifs** — 1

- `[c]` Comparatif - Calcul distribué — filtre `compute/distribue, compute/gpu`

### Web & API  ·  6 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`web/backend` 3, `web/frontend` 2, `web/api` 1)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 6 pages

- `[b]` FastAPI — paquet, Python
- `[b]` Flask — paquet, Python
- `[b]` HTMX — paquet, JavaScript
- `[b]` Jinja2 — paquet, Python
- `[b]` Uvicorn — cli, Python
- `[b]` public-apis — annuaire

### Stockage  ·  6 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine unique, issu de `MOC/Categories/` puis fusionné avec
  le sous-hub `Stockage objet` (voir ci-dessous)
- [x] sous-dossiers créés — **aucun**. `Stockage objet/` avait été créé le 2026-09-04
  (6 pages sur 6), puis **défait le même jour** par le plafond du seuil : un
  sous-domaine qui ne laisse aucune page au niveau du domaine ne se promeut pas.
  Cf. remontée 8 du lot 3
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — `storage/objet` — 6 pages

- `[b]` AWS S3 — saas
- `[b]` Ceph — plateforme, C++
- `[b]` Cloudflare R2 — saas
- `[b]` Garage — plateforme, Rust
- `[b]` MinIO — plateforme, Go
- `[b]` SeaweedFS — plateforme, Go

### Automatisation no-code  ·  5 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine unique, issu de `MOC/Categories/` puis fusionné avec
  le sous-hub `No-code` (voir ci-dessous)
- [x] sous-dossiers créés — **aucun**. `No-code/` avait été créé le 2026-09-04
  (5 pages sur 5, plus le comparatif), puis **défait le même jour** par le plafond du
  seuil ; cf. remontée 8 du lot 3
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — `automation/no-code` — 5 pages

- `[b]` Activepieces — plateforme, TypeScript
- `[b]` Windmill — plateforme, Rust
- `[b]` Zapier — saas
- `[b]` gumloop — saas
- `[b]` n8n — plateforme, TypeScript

**Comparatifs** — 1

- `[c]` Comparatif - Automatisation no-code — filtre `automation/no-code`

### Médias  ·  4 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`media/ingestion` 2, `media/video` 2)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 4 pages

- `[b]` Claude Video — extension, Python
- `[b]` OpenCut — application, TypeScript, Rust
- `[b]` SmartTube — application, Java
- `[b]` Superwhisper — application

### Interfaces & apps data  ·  4 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun : `ui/data-app` a 4 pages, une sous le seuil
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 4 pages

- `[b]` Dash — paquet, Python
- `[b]` Gradio — paquet, Python
- `[b]` Shiny for Python — paquet, Python
- `[b]` Streamlit — paquet, Python

**Comparatifs** — 1

- `[c]` Comparatif - Apps data & démos ML — filtre `ui/data-app`

### Sécurité  ·  3 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`security/recon` 2, `security/auth` 1)
- [ ] notions recatégorisées — lot 4 : les 4 notions de sécurité des LLM (Prompt
  injection, Jailbreaking and defenses, Guardrails, AI security) portent `concept/ai` et
  sont dans la liste « Hors arbre » ; le hub le dit explicitement
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 3 pages

- `[b]` PyJWT — paquet, Python
- `[b]` Web-Check — application, TypeScript
- `[b]` osint4all — annuaire

### Observabilité  ·  3 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun : `observability/supervision` a 3 pages
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 3 pages

- `[b]` Beszel — plateforme, Go
- `[b]` Grafana — application, Go
- `[b]` Loki — plateforme, Go

### Réseau  ·  2 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`network/analyse` 1, `network/transfert` 1)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 2 pages

- `[b]` Sniffnet — application, Rust
- `[b]` croc — cli, Go

### Documents  ·  2 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`docs/capture` 1, `docs/pdf` 1)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 2 pages

- `[b]` Page to Markdown — extension
- `[b]` Stirling PDF — plateforme, Java

### DevOps  ·  2 pages  ·  **migré le 2026-09-04**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/`
- [x] sous-dossiers créés — aucun (`devops/ci` 1, `devops/conteneur` 1)
- [ ] notions recatégorisées — sans objet, le domaine ne porte aucune notion
- [ ] fiches au nouveau gabarit — lot 6

**Au niveau du domaine** — 2 pages

- `[b]` Docker — plateforme, Go
- `[b]` GitHub Actions — saas

## Hors arbre — à arbitrer un par un

18 notions dont le domaine lui-même reste à déterminer.

- [ ] `[n]` AI security — actuellement `concept/ai`
- [ ] `[n]` Architecture médaillon — actuellement `concept/data`
- [x] `[n]` Bases de données — **résolue** : fusionnée dans le hub
  `Bases de données/Bases de données.md` (`role: hub`) au lot 3, avec
  `MOC/Categories/Bases de données.md`. Ne relève plus du lot 4.
- [ ] `[n]` Bases de données vectorielles — actuellement `concept/data`
- [ ] `[n]` Change Data Capture (CDC) — actuellement `concept/data`
- [ ] `[n]` Contrats de données & qualité — actuellement `concept/data`
- [ ] `[n]` ELT vs ETL & idempotence — actuellement `concept/data`
- [ ] `[n]` Guardrails — actuellement `concept/ai`
- [ ] `[n]` Index ANN — internes — actuellement `concept/data`
- [ ] `[n]` Jailbreaking and defenses — actuellement `concept/ai`
- [ ] `[n]` Migrations de schéma — actuellement `concept/data`
- [ ] `[n]` Notebooks-as-code — actuellement `concept/data`
- [ ] `[n]` ORM — actuellement `concept/data`
- [ ] `[n]` Partitionnement & layout de données — actuellement `concept/data`
- [ ] `[n]` Prompt injection — actuellement `concept/ai`
- [ ] `[n]` Stream processing — actuellement `concept/data`
- [ ] `[n]` Versionnage de données — actuellement `concept/data`
- [ ] `[n]` Web scraping — actuellement `concept/data`

9 comparatifs ne filtrent pas sur `categorie` — domaine à poser à la main.

Ce n'est pas une attente neutre : ces 9 croisent un chemin `Dev/Services/` avec un tag ou
une liste de noms, donc **leur vue se vide en silence** dès que leurs membres descendent
dans l'arbre. Le script de migration ne les voit pas. Cf. remontée 7 de
`lot-3-arborescence.md`.

- [x] `[c]` Comparatif - Frameworks CLI — **rangé** dans « Outils de développement/ » ;
      `file.hasTag("cli")` remplacé par `categorie == "devtools/cli"` (2 membres)
- [x] `[c]` Comparatif - Traitement du signal — **rangé** dans « Signal & audio/ » ;
      clause de chemin remplacée par `role == "brique"` (3 membres)
- [~] `[c]` Comparatif - Frontends web légers — **réparé** (`role == "brique"`, 5 membres)
      mais NON rangé : il enjambe « Web & API » et « Interfaces & apps data »
- [ ] `[c]` Comparatif - Boosting — membres dans « Machine Learning », non migré
- [ ] `[c]` Comparatif - Détection & segmentation — idem
- [ ] `[c]` Comparatif - Détection d'anomalies — idem
- [ ] `[c]` Comparatif - Forecasting — idem
- [ ] `[c]` Comparatif - NLP — idem
- [ ] `[c]` Comparatif - Réduction de dimension — idem

