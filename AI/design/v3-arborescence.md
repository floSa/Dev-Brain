---
galaxie: meta
nom: v3-arborescence
type: design-doc
created: 2026-09-04
modified: 2026-09-05
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
| `Dev/Patterns/Pattern - *.md` | 5 | `role: pattern` — dans « Patterns/ » |
| `Dev/Rules/` | 5 | `role: rule` — dans « Rules/ » |
| `MOC/Categories` + `MOC/Types` | 22 | **absorbés** par les pages hub, par `git mv` |
| `MOC/Themes` | 5 | **déplacés** vers « Métiers/ », `role: hub` |
| `MOC/Concepts` | 10 | **conservés jusqu'au lot 4**, qui les tue domaine par domaine — **6 supprimées au 2026-09-05**, sur mesure R7 ; restent `Deep learning`, `LLM (notions)`, `Machine learning (notions)`, `NLP (notions)` |

**Notions à recatégoriser : 205** — c'est le seul poste de travail non mécanique.
**141 faites au 2026-09-05** : les 37 du domaine pilote « Statistiques & inférence », puis
`math` (26), `data` (13, en deux passages), `signal` (5), `ai` (4) et `llm` (56).
**156 restent** sous `Wiki/Concepts/` — `dl` (52), `ml` (67), `rl` (17), `ts` (13), `nlp` (7).

> **État au 2026-09-05 — le lot 3 est CLOS.** Les 20 domaines ont été migrés le
> 2026-09-04 (le pilote « Bases de données », les 14 plus petits, les trois moyens,
> « LLM & IA générative », puis « Machine Learning »), et la clôture du 2026-09-05 a
> rangé ce qu'aucun domaine n'accueillait, par quatre arbitrages de floSa :
>
> - les 5 `MOC/Themes/` **descendent à la racine dans « Métiers/ »**, `role: hub`, corps
>   au gabarit §9 — gardées parce que `domaines:` est le seul axe transverse à un arbre
>   rangé par domaine technique. Pas « Domaines/ » : le mot est déjà pris par l'arbre
>   (remontée 21) ;
> - les 2 `MOC/Types/` deviennent les hubs de **« Patterns/ »** et **« Rules/ »**, que
>   les 5 patterns et les 5 règles rejoignent — c'est `role:` qui les groupe ;
> - `Comparatif - Frontends web légers.base` va dans **« Interfaces & apps data/ »** ;
> - **`MOC/Concepts/` ne bouge pas et n'est pas supprimée** : 30 des 297 notions ne sont
>   atteignables (R7) que par elle. Elle meurt au lot 4, avec `Wiki/Concepts/`.
>
> `Dev/` n'existe plus. Le vault porte **697 pages actives** et **53 hubs** (20 de
> domaine, 26 de sous-domaine, 5 de métier, 2 de rôle) ; 818 fichiers `.md`/`.base`
> avant comme après la clôture. Les 47 comparatifs sont dans le dossier de leurs membres,
> et le relevé de leurs membres avant / après ne montre aucun écart.
>
> **Ce qui reste sous `Wiki/`** ne relève pas du lot 3 : les 297 notions `concept/*`,
> que le lot 4 recatégorisera et descendra.
>
> `MOC/Categories/` est vide : ses 20 pages ont été déplacées par `git mv` vers le hub
> de leur dossier — une MOC de domaine ne disparaît pas, elle *devient* le hub (cf.
> remontée 6 de `lot-3-arborescence.md`). Seule `MOC/Categories/Bases de données.md` a
> réellement disparu, dans la fusion de l'étape 4 avec la notion chapeau homonyme ;
> `Wiki/Concepts/Text-to-SQL.md` est le second cas de notion chapeau, au niveau d'un
> sous-domaine cette fois, et elle *devient* le sous-hub (cf. remontée 15). Deux MOC
> de `MOC/Concepts/` — « Apprentissage par renforcement » et « Séries temporelles » —
> deviennent de la même façon les sous-hubs homonymes de « Machine Learning »
> (cf. remontée 18).
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
├── LLM & IA générative/   (129 pages — 74 au lot 3, 55 notions au lot 4)
│   ├── Agents/   (18)
│   ├── Runtimes/   (14)
│   ├── Agents de code/   (13)
│   ├── Fine-tuning/   (13)
│   ├── RAG & retrieval/   (12)
│   ├── Évaluation/   (11)
│   ├── Modèles de langage/   (6)
│   ├── Assistants/   (5)
│   ├── Observabilité des LLM/   (5)
│   ├── Passerelles/   (5)
│   ├── Sortie typée/   (5)
│   ├── Text-to-SQL/   (5)
│   └── (17 pages au niveau du domaine)
├── Bases de données/   (51 pages — 47 au lot 3, 4 notions au lot 4)
│   ├── Vectoriel/   (13)
│   ├── Administration/   (7)
│   ├── Recherche/   (6)
│   ├── Relationnel/   (6)
│   └── (19 pages au niveau du domaine)
├── Statistiques & inférence/   (47 pages — **lot 4 fait le 2026-09-05**)
│   ├── Tests & estimation/   (15)
│   ├── Analyse factorielle/   (12)
│   ├── Bayésien/   (7)
│   ├── Probabilités/   (6)
│   └── (7 pages au niveau du domaine)
├── Data & pipelines/   (46 pages)
│   ├── Scraping/   (10)
│   ├── Parsing/   (9)
│   ├── Orchestration/   (6)
│   ├── DataFrames/   (5)
│   ├── Visualisation/   (5)
│   └── (11 pages au niveau du domaine)
├── Mathématiques/   (27 pages — 1 au lot 3, les 26 notions au lot 4)
│   └── (1 pages au niveau du domaine)
├── Outils de développement/   (21 pages — 20 au lot 3, 1 notion au lot 4)
│   ├── Notebooks/   (6)
│   └── (15 pages au niveau du domaine)
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
├── Sécurité/   (8 pages — 3 au lot 3, 4 notions puis 1 au lot 4)
│   ├── Systèmes IA/   (5)
│   └── (3 pages au niveau du domaine)
├── Observabilité/   (3 pages)
│   └── (3 pages au niveau du domaine)
├── Réseau/   (2 pages)
│   └── (2 pages au niveau du domaine)
├── Documents/   (2 pages)
│   └── (2 pages au niveau du domaine)
├── DevOps/   (2 pages)
│   └── (2 pages au niveau du domaine)
│
├── Métiers/   (5 hubs transverses, générés depuis `domaines:`)
│   └── Data Science · Data Engineering · MLOps · ML Engineering · AI Engineering
├── Patterns/   (1 hub + 5 pages `role: pattern`)
└── Rules/      (1 hub + 5 pages `role: rule`)
```

Les trois derniers ne sont pas des domaines et ne se dérivent d'aucune `categorie:` :
« Métiers/ » est indexé par le champ `domaines:`, « Patterns/ » et « Rules/ » par
`role:`. `check_arbo.py` les compte à part (`arbo.ROLES_SANS_CATEGORIE`).

## Détail par domaine

### Machine Learning  ·  241 pages  ·  **migré le 2026-09-04**

- [x] hub écrit · [x] sous-dossiers créés · [ ] notions recatégorisées · [ ] fiches au nouveau gabarit

> 85 briques et 12 comparatifs descendus, 9 sous-dossiers promus, 10 hubs écrits.
> Les 156 notions listées ci-dessous portent encore `concept/ml`, `concept/dl`,
> `concept/rl`, `concept/ts` ou `concept/nlp` : elles restent sous `Wiki/Concepts/`
> jusqu'au lot 4, et les hubs les citent toutes en clair en attendant.

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

### LLM & IA générative  ·  129 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05**

- [x] hub écrit — hub de domaine issu de `MOC/Categories/`, corps réécrit au gabarit §9
  au lot 3, puis **réécrit au lot 4** : sa première puce annonçait « six sous-dossiers »
  et énumérait au niveau du domaine le RAG, l'éval, l'observabilité, la sortie structurée
  et la passerelle, qui ont désormais le leur. Les 6 sous-hubs neufs sont écrits ; celui
  de `Text-to-SQL/` porte toujours le corps de la notion chapeau absorbée (à passer au
  §9 au lot 6, comme celui de « Bases de données »)
- [x] sous-dossiers créés — 6 au lot 3 (`Agents de code/`, `Runtimes/`, `Agents/`,
  `Fine-tuning/`, `Text-to-SQL/`, `Assistants/`), **6 de plus au lot 4** :
  `RAG & retrieval/` (12), `Évaluation/` (11), `Modèles de langage/` (6),
  `Observabilité des LLM/` (5), `Passerelles/` (5), `Sortie typée/` (5). 17 pages au
  niveau du domaine, plus 1 des 7 comparatifs
- [x] notions recatégorisées — **lot 4, 2026-09-05** : 55 des 56 notions `concept/llm`
  descendent ici, la 56e (`Sandboxing de code généré`) va dans « Sécurité/ ».
  **Trois valeurs ouvertes** — `llm/modele`, `llm/prompt`, `llm/protocole` — et **une
  retirée**, `llm/mcp`, que `llm/protocole` remplace. `concept/llm` sort du vocabulaire
  et `MOC/Concepts/LLM (notions)` est supprimée sur mesure R7
- [ ] fiches au nouveau gabarit — lot 6

**Agents/** — `llm/agents` — 18 pages

- `[n]` Agent patterns · `[n]` Agent skills · `[n]` agent-loops · `[n]` Harnais d'agent ·
  `[n]` Human-in-the-loop · `[n]` Multi-agent systems · `[n]` Reliability patterns ·
  `[n]` Tool use patterns · `[n]` tool-use
- `[b]` Agno — paquet, Python
- `[b]` AutoGen — paquet, "Python, .NET"
- `[b]` CrewAI — paquet, Python
- `[b]` LangGraph — paquet, Python
- `[b]` OpenAI Agents SDK — paquet, "Python, TypeScript"
- `[b]` PraisonAI — paquet, "Python, JavaScript"
- `[b]` PydanticAI — paquet, Python
- `[b]` Semantic Kernel — paquet, "C#, Python, Java"
- `[b]` smolagents — paquet, Python

**Runtimes/** — `llm/runtime` — 14 pages

- `[n]` Inference optimization · `[n]` Multi-Token Prediction · `[n]` prompt-caching ·
  `[n]` Server-Sent Events & streaming LLM · `[n]` Speculative decoding
- `[b]` LM Studio — application
- `[b]` Ollama — plateforme, Go
- `[b]` SGLang — plateforme, Python
- `[b]` TGI — plateforme, Rust/Python
- `[b]` TensorRT-LLM — paquet, C++/Python
- `[b]` llama.cpp — plateforme, C/C++
- `[b]` needle — modele, Python
- `[b]` text-generation-webui — application, Python
- `[b]` vLLM — plateforme, Python

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

**Fine-tuning/** — `llm/finetuning` — 13 pages

- `[n]` GRPO · `[n]` LoRA et QLoRA · `[n]` PEFT · `[n]` RL for LLMs ·
  `[n]` RLHF and DPO · `[n]` Reward modeling · `[n]` SFT ·
  `[n]` Synthetic data generation
- `[b]` Axolotl — cli, Python
- `[b]` LLaMA-Factory — cli, Python
- `[b]` TRL — paquet, Python
- `[b]` Tunix — paquet, Python
- `[b]` Unsloth — paquet, Python

**RAG & retrieval/** — `llm/rag` — 12 pages — **dossier neuf au lot 4**

> Le libellé n'est pas « RAG » : c'est le nom de fichier d'une **notion qui vit dans le
> dossier**, exactement le cas de `signal/traitement` (remontée 17). Un lien nu ne
> résoudrait plus de façon déterministe.

- `[n]` Advanced RAG · `[n]` Chunking strategies ·
  `[n]` Construction de graphes de connaissances · `[n]` GraphRAG ·
  `[n]` Hybrid retrieval · `[n]` Late-interaction retrieval ·
  `[n]` Query transformations · `[n]` RAG · `[n]` Reranking
- `[b]` Haystack — paquet, Python
- `[b]` LlamaIndex — paquet, Python
- `[b]` RAGatouille — paquet, Python

**Évaluation/** — `llm/eval` — 11 pages — **dossier neuf au lot 4**

- `[n]` Agent evaluation · `[n]` Code and math benchmarks · `[n]` LLM benchmarks ·
  `[n]` LLM eval metrics · `[n]` LLM-as-judge · `[n]` RAG benchmarks · `[n]` RAG eval
- `[b]` DeepEval — paquet, Python
- `[b]` Ragas — paquet, Python
- `[b]` TruLens — paquet, Python
- `[b]` promptfoo — cli, TypeScript
- `[c]` Comparatif - Évaluation LLM — descendu avec ses 4 membres

**Modèles de langage/** — `llm/modele` — 6 pages — **valeur et dossier neufs au lot 4**

> Le seul sous-dossier du domaine qui ne porte **aucune brique** : il décrit l'objet, pas
> ce qu'on en fait. La valeur a été ouverte parce que le vocabulaire `llm/*` était
> entièrement applicatif — c'est la situation de la remontée 1, rejouée.

- `[n]` Decoding strategies · `[n]` Perplexity · `[n]` Reasoning models ·
  `[n]` Scaling laws · `[n]` Small Language Models · `[n]` Tokenization

**Assistants/** — `llm/assistant` — 5 pages

- `[b]` Hermes Agent — plateforme, "Python, TypeScript"
- `[b]` LM Studio Bionic — application
- `[b]` OpenClaw — plateforme, "TypeScript, Swift"
- `[b]` OpenHands — plateforme, "Python, TypeScript"
- `[b]` OpenMAIC — application, TypeScript

**Observabilité des LLM/** — `llm/observabilite` — 5 pages — **dossier neuf au lot 4**

> Le libellé n'est ni « Observabilité » (le hub du **domaine** homonyme) ni
> « Observabilité LLM » (un `alias:` de la notion qui vit dans le dossier). Les deux
> ensembles de la remontée 8 mordaient en même temps.

- `[n]` LLM observability
- `[b]` Helicone — plateforme, TypeScript
- `[b]` LangSmith — plateforme
- `[b]` Langfuse — plateforme, TypeScript
- `[b]` Phoenix Arize — plateforme, Python
- `[c]` Comparatif - Observabilité LLM — descendu avec ses 4 membres

**Passerelles/** — `llm/passerelle` — 5 pages — **dossier neuf au lot 4**

- `[n]` LLM caching · `[n]` Routing and cascading
- `[b]` LiteLLM — plateforme, Python
- `[b]` OmniRoute — plateforme, TypeScript
- `[b]` OpenRouter — saas

**Sortie typée/** — `llm/sortie-structuree` — 5 pages — **dossier neuf au lot 4**

> Ni « Sortie structurée », ni « Sorties structurées », ni « Génération contrainte », ni
> « Décodage contraint » : les quatre sont des `alias:` de `Structured outputs` ou de
> `Constrained decoding`, qui vivent dans le dossier.

- `[n]` Constrained decoding · `[n]` Structured outputs
- `[b]` Guidance — paquet, Python
- `[b]` Instructor — paquet, Python
- `[b]` Outlines — paquet, Python

**Text-to-SQL/** — `llm/text-to-sql` — 5 pages

- `[b]` DB-GPT — plateforme, Python
- `[b]` LangChain SQL agent — paquet, Python
- `[b]` LlamaIndex NLSQLTableQueryEngine — paquet, Python
- `[b]` Vanna — paquet, Python
- `[b]` WrenAI — plateforme, Python, Rust

**Au niveau du domaine** — 17 pages

- `llm/prompt` — **valeur neuve**, 3 pages, sous le seuil :
  `[n]` Chain-of-Thought · `[n]` Context engineering · `[n]` Prompt engineering
- `llm/protocole` — **valeur neuve**, remplace `llm/mcp`, 4 pages, sous le seuil :
  `[n]` a2a-protocol · `[n]` mcp-protocol · `[b]` fastmcp — paquet, Python ·
  `[b]` mcpjam — application, TypeScript
- `llm/memoire` — 4 : `[n]` Agent memory · `[b]` Headroom — paquet ·
  `[b]` Letta — plateforme, Python · `[b]` OpenViking — plateforme, Python
- `llm/low-code` — 3 : `[b]` Dify · `[b]` Flowise · `[b]` Langflow
- `llm/socle` — 2 : `[b]` DSPy — paquet, Python · `[b]` LangChain — paquet, Python
- `llm/outillage` — 1 : `[b]` llmfit — cli, Rust

**Comparatifs** — 7, dont **1 seul reste au niveau du domaine**

- `[c]` Comparatif - Frameworks LLM — filtre `llm/agents, llm/rag, llm/socle,
  llm/sortie-structuree` : ses membres enjambent quatre sous-domaines dont un non promu,
  il **reste** au niveau du domaine (remontée 16 — la règle porte sur les membres)
- `[c]` Comparatif - Assistants de code IA — dans `Agents de code/`
- `[c]` Comparatif - Exécution & serving LLM — dans `Runtimes/`
- `[c]` Comparatif - Fine-tuning LLM — dans `Fine-tuning/`
- `[c]` Comparatif - Frameworks text-to-SQL — dans `Text-to-SQL/`
- `[c]` Comparatif - Observabilité LLM — **descendu au lot 4** dans `Observabilité des LLM/`
- `[c]` Comparatif - Évaluation LLM — **descendu au lot 4** dans `Évaluation/`

**Les 56 notions `concept/llm`, et où elles sont allées**

Le corps du hub en citait **35 sur 56** nommément, et ses paragraphes sont des familles :
c'est lui qui a rangé la majorité (étape 0, remontées 1 et 12). Les 21 autres sont
dérivées page par page, principalement sur leur section `## Approches voisines`.

- [x] `[n]` Advanced RAG → `llm/rag`
- [x] `[n]` Agent evaluation → `llm/eval`
- [x] `[n]` Agent memory → `llm/memoire`
- [x] `[n]` Agent patterns → `llm/agents`
- [x] `[n]` Agent skills → `llm/agents`
- [x] `[n]` Chain-of-Thought → `llm/prompt`
- [x] `[n]` Chunking strategies → `llm/rag`
- [x] `[n]` Code and math benchmarks → `llm/eval`
- [x] `[n]` Constrained decoding → `llm/sortie-structuree`
- [x] `[n]` Construction de graphes de connaissances → `llm/rag`
- [x] `[n]` Context engineering → `llm/prompt`
- [x] `[n]` Decoding strategies → `llm/modele`
- [x] `[n]` GRPO → `llm/finetuning`
- [x] `[n]` GraphRAG → `llm/rag`
- [x] `[n]` Harnais d'agent → `llm/agents`
- [x] `[n]` Human-in-the-loop → `llm/agents`
- [x] `[n]` Hybrid retrieval → `llm/rag`
- [x] `[n]` Inference optimization → `llm/runtime`
- [x] `[n]` LLM benchmarks → `llm/eval`
- [x] `[n]` LLM caching → `llm/passerelle`
- [x] `[n]` LLM eval metrics → `llm/eval`
- [x] `[n]` LLM observability → `llm/observabilite`
- [x] `[n]` LLM-as-judge → `llm/eval`
- [x] `[n]` Late-interaction retrieval → `llm/rag`
- [x] `[n]` LoRA et QLoRA → `llm/finetuning`
- [x] `[n]` Multi-Token Prediction → `llm/runtime`
- [x] `[n]` Multi-agent systems → `llm/agents`
- [x] `[n]` PEFT → `llm/finetuning`
- [x] `[n]` Perplexity → `llm/modele` — et **non** `llm/eval` : la page se dit
      INTRINSÈQUE et range l'éval applicative parmi ses « alternatives »
- [x] `[n]` Prompt engineering → `llm/prompt`
- [x] `[n]` Query transformations → `llm/rag`
- [x] `[n]` RAG → `llm/rag`
- [x] `[n]` RAG benchmarks → `llm/eval`
- [x] `[n]` RAG eval → `llm/eval`
- [x] `[n]` RL for LLMs → `llm/finetuning`
- [x] `[n]` RLHF and DPO → `llm/finetuning`
- [x] `[n]` Reasoning models → `llm/modele`
- [x] `[n]` Reliability patterns → `llm/agents`
- [x] `[n]` Reranking → `llm/rag`
- [x] `[n]` Reward modeling → `llm/finetuning`
- [x] `[n]` Routing and cascading → `llm/passerelle` — et **non** `llm/rag`, où le hub
      la citait : la page nomme les trois briques du sous-domaine et écrit
      « passerelles qui l'implémentent »
- [x] `[n]` SFT → `llm/finetuning`
- [x] `[n]` Sandboxing de code généré → **`security/ia`**, hors du domaine
- [x] `[n]` Scaling laws → `llm/modele`
- [x] `[n]` Server-Sent Events & streaming LLM → `llm/runtime` — et **non** `web/api` :
      ses voisines sont Decoding strategies, Tokenization et Inference optimization
- [x] `[n]` Small Language Models → `llm/modele`
- [x] `[n]` Speculative decoding → `llm/runtime`
- [x] `[n]` Structured outputs → `llm/sortie-structuree`
- [x] `[n]` Synthetic data generation → `llm/finetuning`
- [x] `[n]` Tokenization → `llm/modele`
- [x] `[n]` Tool use patterns → `llm/agents`
- [x] `[n]` a2a-protocol → `llm/protocole`
- [x] `[n]` agent-loops → `llm/agents`
- [x] `[n]` mcp-protocol → `llm/protocole`
- [x] `[n]` prompt-caching → `llm/runtime`
- [x] `[n]` tool-use → `llm/agents`

### Bases de données  ·  51 pages  ·  **migré le 2026-09-04, 4 notions rangées le 2026-09-05**

- [x] hub écrit — les 4 sous-hubs sont écrits ; le hub de domaine porte le corps de la
  notion fusionnée, à passer au gabarit §9 au lot 6
- [x] sous-dossiers créés — `Vectoriel/` (13), `Administration/` (7), `Recherche/` (6),
  `Relationnel/` (6) ; 19 pages au niveau du domaine, plus les 10 comparatifs
- [x] notions recatégorisées — lot 4, 2026-09-05 : les **4 notions remontées** par la
  conversation `concept/data` sont descendues ici, aucune valeur ouverte, aucun
  sous-dossier promu ni défait (`orm` 3→4 et `migration` 3→4 restent sous le seuil,
  `vecteur` 11→13 avait déjà son dossier). Le domaine n'avait porté que des briques
  jusque-là. Le corps du sous-hub `Vectoriel` a été complété : il n'énumérait que des
  briques, il nomme désormais les deux notions et dit à quel étage chacune se lit
- [ ] fiches au nouveau gabarit — lot 6

**Vectoriel/** — `database/vecteur` — 13 pages

- `[n]` Bases de données vectorielles — notion chapeau des moteurs du dossier
- `[n]` Index ANN — internes — HNSW, IVF, PQ : ce qui tourne sous les moteurs
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

**Au niveau du domaine** — 19 pages

- `[n]` Migrations de schéma — `database/migration`, 4 pages, sous le seuil
- `[n]` ORM — `database/orm`, 4 pages, sous le seuil
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

### Statistiques & inférence  ·  47 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/` par `git mv`, corps réécrit
  au gabarit §9, puis complété au lot 4 : il dit désormais ce que chacun des quatre
  sous-dossiers range, et ce qui reste au niveau du domaine
- [x] sous-dossiers créés — **quatre, au lot 4**. Au lot 3 il n'y en avait aucun : les
  4 sous-domaines `stats/*` plafonnaient à 4 pages, sous le seuil. Les 37 notions les
  ont fait franchir le seuil, et 9 des 10 briques ont suivi la promotion de leur
  sous-domaine — c'est la conséquence normale de la règle 2, pas un effet de bord
- [x] notions recatégorisées — **lot 4, 2026-09-05** : les 37 sont dans l'arbre, plus
  aucune ne porte `concept/stats`, et la valeur est retirée du vocabulaire
- [ ] fiches au nouveau gabarit — lot 6

**Tests & estimation/** — `stats/inference` — 15 pages

- `[n]` Analyse de puissance · `[n]` Analyse de survie · `[n]` Bootstrap
- `[n]` Correction des tests multiples · `[n]` Intervalles de confiance
- `[n]` MANOVA et tests multivariés · `[n]` Maximum de vraisemblance
- `[n]` Test du khi-deux · `[n]` Test t et ANOVA · `[n]` Tests d'hypothèse
- `[n]` Tests non paramétriques
- `[b]` lifelines · `[b]` pingouin · `[b]` scipy.stats · `[b]` statsmodels

**Analyse factorielle/** — `stats/exploratoire` — 12 pages

- `[n]` CA · `[n]` FAMD · `[n]` GPA · `[n]` HCPC · `[n]` MCA · `[n]` MFA
- `[n]` Manifold learning · `[n]` PCA · `[n]` PGA · `[n]` Réduction de dimension
- `[b]` Fanalysis · `[b]` Prince

**Bayésien/** — `stats/bayesien` — 7 pages

- `[n]` A priori conjugués · `[n]` Estimation MAP · `[n]` Inférence bayésienne · `[n]` MCMC
- `[b]` ArviZ · `[b]` PyMC · `[b]` Stan

**Probabilités/** — `stats/probabilite` — 6 pages — **valeur nouvelle**

- `[n]` Chaînes de Markov · `[n]` Inégalités de concentration
- `[n]` Loi des grands nombres · `[n]` Mouvement brownien
- `[n]` Processus de Poisson · `[n]` Théorème central limite

**Au niveau du domaine** — 7 pages

- `stats/experimentation` — **valeur nouvelle**, 4 pages, sous le seuil :
  `[n]` A-B testing · `[n]` CUPED · `[n]` Multi-armed bandits · `[n]` Sequential testing
- `stats/causal` — 3 pages, sous le seuil :
  `[n]` Diff-in-Diff · `[n]` Inférence causale · `[b]` CausalImpact

**Comparatifs** — 1

- `[c]` Comparatif - Outils stats — filtre `stats/`, donc le domaine entier : il reste au
  niveau du domaine et sa vue est inchangée par la promotion des quatre sous-dossiers

### Data & pipelines  ·  54 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05**

- [x] hub écrit — hub de domaine (issu de `MOC/Categories/` par `git mv`, corps réécrit
  au gabarit §9) et les 5 sous-hubs `Scraping`, `Parsing`, `Orchestration`, `DataFrames`,
  `Visualisation`
- [x] sous-dossiers créés — les 5 ci-dessus, **inchangés au lot 4** : `Scraping/` gagne
  une page et reste le seul touché. `data/eda` (3), `data/format` (4),
  `data/synthetique` (3), `data/streaming` (2), `data/ingestion` (2) et la nouvelle
  `data/fiabilite` (4) restent sous le seuil
- [~] notions recatégorisées — **lot 4, 2026-09-05 : 8 sur 13.** Le constat du lot 3
  (« aucune n'est propre à ce domaine ») s'est vérifié : **5 appellent un autre
  domaine** et n'ont PAS été déplacées, par consigne de floSa — une notion qui appelle
  un sous-domaine hors du périmètre du lot se remonte, elle ne se déplace pas. Elles
  restent sous `Wiki/Concepts/`, et `concept/data` reste donc dans le vocabulaire de
  `taxonomie.md`, seule valeur `concept/*` survivante d'un domaine traité
- [ ] fiches au nouveau gabarit — lot 6

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

**Scraping/** gagne `[n]` Web scraping — 11 pages

**Au niveau du domaine** — 18 pages

- `data/fiabilite` — **valeur nouvelle**, 4 pages, sous le seuil. Ce qu'un pipeline doit
  garantir quel que soit l'outil qui l'exécute, là où `data/orchestration` porte l'outil
  qui l'exécute : `[n]` Architecture médaillon · `[n]` Contrats de données & qualité ·
  `[n]` ELT vs ETL & idempotence · `[n]` Versionnage de données
- `data/format` — 4 pages : `[b]` Apache Iceberg · `[b]` Avro · `[b]` Parquet ·
  `[n]` Partitionnement & layout de données
- `data/synthetique` — 3 : `[b]` Faker · `[b]` Mimesis · `[b]` SDV
- `data/eda` — 3 : `[b]` missingno · `[b]` sweetviz · `[b]` ydata-profiling
- `data/streaming` — 2 : `[b]` Flink · `[n]` Stream processing
- `data/ingestion` — 2 : `[b]` connectorx · `[n]` Change Data Capture (CDC)

**Remontées — 5 notions `concept/data` NON déplacées**

Effet de seuil mesuré pour chacune **avant** de décider (remontée 3 du pilote) : il est
nul, aucune ne forcerait de restructuration. Ce n'est donc pas le seuil qui les retient,
c'est la frontière de domaine.

- `[n]` ORM → `database/orm` (3 → 4, sous le seuil)
- `[n]` Migrations de schéma → `database/migration` (3 → 4, sous le seuil)
- `[n]` Bases de données vectorielles → `database/vecteur` (12 → 13, `Vectoriel/` existe)
- `[n]` Index ANN — internes → `database/vecteur` (→ 14, `Vectoriel/` existe)
- `[n]` Notebooks-as-code → `devtools/notebook` (5 → 6, `Notebooks/` existe)

**Comparatifs** — 6

- `[c]` Comparatif - Manipulation de données — filtre `data/tableau`
- `[c]` Comparatif - Orchestrateurs data — filtre `data/orchestration`
- `[c]` Comparatif - Outils EDA - profiling — filtre `data/eda`
- `[c]` Comparatif - Parsing de documents — filtre `data/parsing`
- `[c]` Comparatif - Scraping — filtre `data/scraping`
- `[c]` Comparatif - Visualisation — filtre `data/viz`

### Mathématiques  ·  27 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/` par `git mv`, corps réécrit
  au gabarit §9 au lot 3, puis **réduit au lot 4** : il n'énumère plus les 26 notions,
  il aiguille vers les quatre sous-hubs qui les portent, et il dit ce qui n'est PAS ici
  (la probabilité, l'analyse factorielle) et pourquoi
- [x] sous-dossiers créés — **quatre, au lot 4**, et le domaine n'a plus AUCUNE page à
  son niveau. C'est permis : le plafond du seuil ne bloque que le sous-domaine qui
  égale le total de son domaine (`arbo.py`), et aucun des quatre n'y arrive. Trois
  valeurs ont dû être ouvertes ; `math/optimisation` existait et a été **élargie** —
  elle ne portait que la recherche opérationnelle tant qu'elle n'avait qu'une brique
- [x] notions recatégorisées — **lot 4, 2026-09-05** : les 26 sont dans l'arbre, plus
  aucune ne porte `concept/math`, et la valeur est retirée du vocabulaire
- [x] **le corps du hub a rangé les 26 à lui seul.** Ses quatre puces, écrites au lot 3,
  citent chaque notion nommément et une seule fois : c'est une partition exacte, et
  l'étape 0 de la procédure du lot n'a eu qu'à la suivre. Un seul écart tag / hub —
  `Optimal transport` porte le tag `optimization` et va en `math/information`, avec
  `Wasserstein distance` dont il est la valeur optimale
- [ ] fiches au nouveau gabarit — lot 6

**Optimisation/** — `math/optimisation` — 10 pages — **valeur élargie**

- `[n]` Convexity · `[n]` Gradient descent · `[n]` Learning rate schedules
- `[n]` Loss landscape and saddle points · `[n]` Newton & quasi-Newton
- `[n]` Optimisation combinatoire · `[n]` Optimisation sous contrainte
- `[n]` Programmation linéaire en nombres entiers (MIP)
- `[b]` PuLP — paquet, Python
- `[c]` Comparatif - Solveurs d'optimisation — **descendu ici avec ses membres** : son
  filtre est `categorie == "math/optimisation"` exactement, donc tous ses membres sont
  dans ce dossier. Celui de « Statistiques & inférence » filtre le préfixe entier et
  enjambe les quatre sous-dossiers : il est resté au niveau du domaine. La règle porte
  sur les **membres**, pas sur le nom du fichier

**Théorie de l'information/** — `math/information` — 7 pages — **valeur nouvelle**

- `[n]` Cross-entropy · `[n]` Jensen-Shannon divergence · `[n]` KL divergence
- `[n]` Mutual information · `[n]` Optimal transport · `[n]` Shannon entropy
- `[n]` Wasserstein distance

**Algèbre linéaire/** — `math/algebre-lineaire` — 6 pages — **valeur nouvelle**

- `[n]` Eigendecomposition · `[n]` Matrix decompositions · `[n]` Matrix products
- `[n]` Projections · `[n]` SVD · `[n]` Vector norms

**Théorie de l'apprentissage/** — `math/theorie-apprentissage` — 5 pages — **valeur nouvelle**

- `[n]` Generalization bounds · `[n]` No Free Lunch theorem · `[n]` PAC learning
- `[n]` Rademacher complexity · `[n]` VC dimension

> Exactement 5, donc exactement au seuil : relu deux fois comme la remontée 4 du pilote
> l'exige. Ce sont les **5 seules pages du vault** taguées `learning-theory`, et aucune
> des trois autres familles ne peut y verser — le compte est un fait mesuré, pas un
> arbitrage qui viserait le seuil. La valeur nomme la **théorie** et non
> « apprentissage » seul, qui à côté de `ml/*` se lirait comme apprentissage automatique.

**Au niveau du domaine** — 0 page

### Outils de développement  ·  21 pages  ·  **migré le 2026-09-04, 1 notion rangée le 2026-09-05**

- [x] hub écrit — hub de domaine (issu de `MOC/Categories/`) et sous-hub `Notebooks`
- [x] sous-dossiers créés — `Notebooks/` (6) ; 15 pages au niveau du domaine, plus 3
  comparatifs (`Clients d'API`, `Gestionnaires de paquets Python`, `Frameworks CLI`)
- [x] **20 pages, pas 19** — `Wiki/Outils/Obsidian.md` (`skill/knowledge`) est rattachée
  ici par arbitrage de floSa ; ce tableau ne la comptait pas
- [x] notions recatégorisées — lot 4, 2026-09-05 : « sans objet » était faux. Une notion
  remontée par la conversation `concept/data`, `Notebooks-as-code`, est descendue dans
  `Notebooks/` (5→6, le dossier existait déjà). Le corps du sous-hub la nomme désormais :
  il décrivait sa matière — pairing, sorties hors du dépôt — sans jamais la citer
- [ ] fiches au nouveau gabarit — lot 6

**Notebooks/** — `devtools/notebook` — 6 pages

- `[n]` Notebooks-as-code — la discipline dont les 5 briques sont l'outillage
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

### Signal & audio  ·  8 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/` ; corps complété au lot 4 :
  il aiguille vers le sous-hub et dit pourquoi `signal/audio` n'a pas de dossier
- [x] sous-dossiers créés — **`Traitement/` au lot 4**. C'est le seul domaine du lot dont
  l'arbre d'arrivée était **déjà écrit ici** depuis le lot 3, avec ses 7 pages : les 2
  briques `signal/traitement` étaient sous le seuil tant que les 5 notions portaient
  `concept/signal`. Rien n'a été arbitré, le seuil a fait le travail
- [x] notions recatégorisées — **lot 4, 2026-09-05** : les 5 sont dans l'arbre, plus
  aucune ne porte `concept/signal`, et la valeur est retirée du vocabulaire. Aucune des
  5 ne parle d'audio : elles vont toutes en `signal/traitement`
- [x] comparatif rattaché — `Comparatif - Traitement du signal`, dont le filtre de chemin
  cassait au déplacement (cf. remontée 7 du lot 3). Il **reste au niveau du domaine** :
  ses 3 membres enjambent les deux sous-domaines, `scipy.signal` et `PyWavelets` en
  `signal/traitement`, `librosa` en `signal/audio`
- [ ] fiches au nouveau gabarit — lot 6

**Traitement/** — `signal/traitement` — 7 pages

- `[n]` Filtrage numérique · `[n]` Ondelettes · `[n]` STFT et spectrogramme
- `[n]` Traitement du signal · `[n]` Transformée de Fourier
- `[b]` PyWavelets — paquet, C / Cython / Python
- `[b]` scipy.signal — paquet, C / Fortran / Python

> Le libellé du dossier est « **Traitement** » et non « Traitement du signal », qui est
> le `nom:` d'une notion **vivant dans ce dossier** — deux fichiers du même nom, et un
> lien nu ne résout plus de façon déterministe. Même raison qu'au pilote pour
> « Tests & estimation » et « Analyse factorielle » (remontée 8).

**Au niveau du domaine** — 1 page

- `[b]` librosa — paquet, Python (`signal/audio`, seul de son sous-domaine)

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

### Sécurité  ·  8 pages  ·  **migré le 2026-09-04, notions rangées le 2026-09-05 (deux fois)**

- [x] hub écrit — hub de domaine, issu de `MOC/Categories/` ; corps **réécrit au lot 4** :
  le domaine porte désormais trois activités et non deux, et la phrase qui annonçait que
  les notions de sécurité IA « ne sont pas descendues ici » est remplacée
- [x] sous-dossiers créés — `Systèmes IA/` (5), au **second** passage du 2026-09-05 :
  la 5e page de `security/ia` arrive du domaine « LLM & IA générative » et fait franchir
  le seuil. Le libellé n'est pas « Sécurité des systèmes IA », qui redoublerait le nom du
  domaine parent — même défaut qu'« Inférence » sous « Statistiques & inférence »
  (remontée 8). Restent au niveau du domaine `security/recon` (2) et `security/auth` (1)
- [x] notions recatégorisées — **lot 4, en deux temps.** 2026-09-05, valeur nouvelle
  `security/ia` : les 4 notions `concept/ai` descendent, `concept/ai` est retirée du
  vocabulaire. Puis, dans le lot `concept/llm`, `Sandboxing de code généré` les rejoint —
  ses voisines déclarées sont [[Prompt injection]], [[AI security]], [[Guardrails]] et
  [[Human-in-the-loop]], soit quatre des cinq déjà tranchées
- [ ] fiches au nouveau gabarit — lot 6

**Systèmes IA/** — `security/ia` — 5 pages

- `[n]` AI security — la page chapeau
- `[n]` Guardrails
- `[n]` Jailbreaking and defenses
- `[n]` Prompt injection
- `[n]` Sandboxing de code généré — arrivée du lot `concept/llm`, c'est elle qui promeut

**Au niveau du domaine** — 3 pages

- `security/recon` — 2 : `[b]` Web-Check — application, TypeScript · `[b]` osint4all — annuaire
- `security/auth` — 1 : `[b]` PyJWT — paquet, Python

> **La décision que le lot 4 devait trancher, et elle va contre l'arbre.** L'arbre de
> décision du domaine met D1 (« a besoin d'un LLM ») avant D9 (« porte sur la sécurité »),
> et les quatre pages ne parlent que d'applications LLM : elles auraient dû aller en
> `llm/*`. Les deux hubs concernés se répondaient d'ailleurs dans ce sens — celui de
> « LLM & IA générative » les revendiquait nommément, celui de « Sécurité » écrivait
> qu'elles n'étaient pas descendues là. Arbitrage de floSa : elles portent `concept/ai` et
> non `concept/llm` — la famille large était déjà un choix — et **la sécurité est une
> pratique qui traverse les modèles**, pas un sous-sujet de l'IA générative. Ce n'est pas
> un effet de seuil : 3 → 7 pages ne promeut aucun sous-dossier. Les deux phrases de hub
> sont réécrites dans le même commit.
>
> **Le lot `concept/llm` a rejoué le cas, et la réponse a été la même.**
> `Sandboxing de code généré` porte `concept/llm` et non `concept/ai`, donc l'argument de
> la famille large ne s'appliquait pas ; c'est le contenu qui a tranché — la page ouvre
> sur « le code généré est non fiable par construction… parce que son entrée peut l'être
> ([[Prompt injection]]) », et ses voisines déclarées sont quatre des cinq pages du
> dossier. Cette fois **il y a un effet de seuil** : 4 → 5, donc `Systèmes IA/` naît.
> Arbitrage explicite de floSa : ce n'est pas un argument. « Le seuil ne se négocie jamais
> page par page, ni pour l'atteindre ni pour l'éviter ; la catégorie se décide sur le
> contenu, le dossier suit tout seul. »

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

18 notions dont le domaine lui-même reste à déterminer. **Les 18 sont traitées au lot 4**,
en deux passages. Le premier, par famille d'origine, en a rangé 12 — les 8 de `concept/data`
propres à « Data & pipelines », et les 4 de sécurité IA que floSa a tranchées en
`security/ia` (motif dans la section « Sécurité ») — et en a **remonté 5**, dont le domaine
d'accueil était hors de son périmètre. Le second, le 2026-09-05, a pris ces 5 **par domaine
d'accueil** comme la remontée 15 le suggérait : « Bases de données » pour quatre d'entre
elles, « Outils de développement » pour la cinquième. La dix-huitième était déjà résolue au
lot 3. `concept/data` est sorti du vocabulaire dans le même commit.

- [x] `[n]` AI security — **rangée** `security/ia`, lot 4
- [x] `[n]` Architecture médaillon — **rangée** `data/fiabilite`, lot 4
- [x] `[n]` Bases de données — **résolue** : fusionnée dans le hub
  `Bases de données/Bases de données.md` (`role: hub`) au lot 3, avec
  `MOC/Categories/Bases de données.md`. Ne relève plus du lot 4.
- [x] `[n]` Bases de données vectorielles — **rangée** `database/vecteur`, lot 4, second passage (11 → 13 avec `Index ANN`, `Vectoriel/` existait)
- [x] `[n]` Change Data Capture (CDC) — **rangée** `data/ingestion`, lot 4
- [x] `[n]` Contrats de données & qualité — **rangée** `data/fiabilite`, lot 4
- [x] `[n]` ELT vs ETL & idempotence — **rangée** `data/fiabilite`, lot 4
- [x] `[n]` Guardrails — **rangée** `security/ia`, lot 4
- [x] `[n]` Index ANN — internes — **rangée** `database/vecteur`, lot 4, second passage
- [x] `[n]` Jailbreaking and defenses — **rangée** `security/ia`, lot 4
- [x] `[n]` Migrations de schéma — **rangée** `database/migration`, lot 4, second passage (3 → 4, sous le seuil, pas de dossier)
- [x] `[n]` Notebooks-as-code — **rangée** `devtools/notebook`, lot 4, second passage (5 → 6, `Notebooks/` existait)
- [x] `[n]` ORM — **rangée** `database/orm`, lot 4, second passage (3 → 4, sous le seuil, pas de dossier)
- [x] `[n]` Partitionnement & layout de données — **rangée** `data/format`, lot 4
- [x] `[n]` Prompt injection — **rangée** `security/ia`, lot 4
- [x] `[n]` Stream processing — **rangée** `data/streaming`, lot 4
- [x] `[n]` Versionnage de données — **rangée** `data/fiabilite`, lot 4
- [x] `[n]` Web scraping — **rangée** `data/scraping`, lot 4

9 comparatifs ne filtrent pas sur `categorie` — domaine à poser à la main. **Les 9 sont
traités** depuis la clôture du 2026-09-05.

Ce n'était pas une attente neutre : ces 9 croisaient un chemin `Dev/Services/` avec un tag
ou une liste de noms, donc **leur vue se vidait en silence** dès que leurs membres
descendaient dans l'arbre, sans que le script de migration les voie. La substitution est
la même partout — `role == "brique"`, qui dit ce que le chemin disait et ne bouge plus
avec l'arbre. Cf. remontées 7, 14 et 16 de `lot-3-arborescence.md`.

- [x] `[c]` Comparatif - Frameworks CLI — **rangé** dans « Outils de développement/ » ;
      `file.hasTag("cli")` remplacé par `categorie == "devtools/cli"` (2 membres)
- [x] `[c]` Comparatif - Traitement du signal — **rangé** dans « Signal & audio/ » ;
      clause de chemin remplacée par `role == "brique"` (3 membres)
- [x] `[c]` Comparatif - Frontends web légers — **réparé** (`role == "brique"`, 5 membres)
      puis **rangé** dans « Interfaces & apps data/ » le 2026-09-05, par arbitrage de
      floSa : trois de ses cinq membres y vivent (Streamlit, Gradio, Dash), FastAPI et
      HTMX n'y figurent que comme l'option à la main. C'est un comparatif d'interfaces
      pour applications data, pas un comparatif de web
- [x] `[c]` Comparatif - Boosting — **rangé** dans « Machine Learning/Tabulaire/ » (3 membres) ;
      clause de chemin remplacée par `role == "brique"`
- [x] `[c]` Comparatif - Détection & segmentation — **rangé** dans « Machine Learning/Vision/ » (6 membres) ;
      clause de chemin remplacée par `role == "brique"`
- [x] `[c]` Comparatif - Détection d'anomalies — **rangé** dans « Machine Learning/ » — ses 2 membres enjambent deux sous-domaines ;
      clause de chemin remplacée par `role == "brique"`
- [x] `[c]` Comparatif - Forecasting — **rangé** dans « Machine Learning/Séries temporelles/ » (6 membres) ;
      clause de chemin remplacée par `role == "brique"`
- [x] `[c]` Comparatif - NLP — traduit plus tôt (`role == "brique"`, 16 membres),
      **rangé** dans « Machine Learning/NLP/ »
- [x] `[c]` Comparatif - Réduction de dimension — traduit plus tôt
      (`role == "brique"`, 5 membres), **rangé** dans « Machine Learning/ » : ses
      membres se partagent `ml/non-supervise`, `ml/socle` et `stats/exploratoire`

