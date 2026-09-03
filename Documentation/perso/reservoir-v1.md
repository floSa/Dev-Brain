# Réservoir v1 — backlog de migration vers v2

> Inventaire des 393 pages v1, regroupé par **destination v2** (catégorie / sous-catégorie),
> pour piocher quoi ajouter via le skill `enrichir-brain`.
> **Ne plus lancer `AI/scripts/list_reservoir.py`** (il écraserait ce fichier).

**Légende** : ✅ déjà en v2 · ⬜ à créer · ⚠️ catégorie à créer / à valider (ne pas inventer sans accord).

> ⚠️ **Les coches ✅/⬜ ne se modifient PAS à la main.** Elles sont dérivées de l'index par
> `uv run AI/scripts/sync_reservoir.py` (source de vérité = `brain-index.json`). Le script
> recoche tout et affiche le prochain lot suggéré.

Rappel du rangement **v3** : il n'y a plus ni `Dev/` ni `Wiki/`, et donc plus de dossier à choisir. Une page se range par sa `categorie:`, qui donne son dossier dans l'arbre des 20 domaines (`AI/scripts/arbo.py`) ; ce qu'elle **est** — brique, notion, pattern, règle — est porté par `role:`, pas par son chemin. Les skills perso portent `skill/*`, rattaché à « Outils de développement » (arbitrage du 2026-09-04).

## Boucle de migration (1 conversation = 1 lot)

Plafond **5 pages explicites** par conversation : `enrichir-brain` crée aussi les pages connexes (concept parent, alternatives), donc 5 + X fichiers — on garde la marge pour ne pas embrouiller la conv.

**Prompt-type à coller dans une nouvelle conv Claude Code :**

```
Mode build. Lis Documentation/perso/reservoir-v1.md. Prends AU PLUS 5 pages ⬜ de
la section « <SECTION> », applique le skill enrichir-brain (mode sujet : plan →
mon GO → drainer). Le skill crée aussi les pages connexes nécessaires (donc parfois
plus de 5 fichiers, c'est voulu). À la fin : uv run AI/scripts/sync_reservoir.py
pour recocher le statut, puis commit + push + merge main d'office.
```

Sur les sections marquées ⚠️ (catégorie non tranchée), valider la catégorie avant de créer.

---

# PARTIE A — Services & outils (galaxie `Dev`)

## Bases de données → `database/*`

**Relationnelles** — `database/relational`
- ✅ **Postgres** — relationnel de référence, extensible (JSONB, pgvector).
- ✅ **MariaDB** — fork communautaire de MySQL.
- ✅ **CockroachDB** — relationnel distribué compatible Postgres.


**Document / clé-valeur / wide-column** — `database/document`, `keyvalue`, `wide-column`
- ✅ **MongoDB** — base documents JSON.
- ✅ **Redis** — clé-valeur en mémoire, cache et structures.
- ✅ **Apache Cassandra** — wide-column distribué, écriture massive.

**Graphes** — `database/graph`
- ✅ **Neo4j** — base de graphes de référence (Cypher).
- ✅ **Nebula Graph** — base de graphes distribuée.

**Colonnes / analytique** — `database/columnar`
- ✅ **DuckDB** — OLAP embarqué, le « SQLite analytique ».
- ✅ **ClickHouse** — colonnaire analytique très rapide.

**Séries temporelles** — `database/timeseries`
- ✅ **InfluxDB** — base de séries temporelles native.
- ✅ **TimescaleDB** — extension séries temporelles de Postgres.

**Recherche** — `database/search`
- ✅ **Elasticsearch** — moteur de recherche / indexation texte.


**Vectorielles** — `database/vector`
- ✅ **pgvector** — extension vectorielle de Postgres.
- ✅ **Qdrant** — base vectorielle open-source (Rust).
- ✅ **Weaviate** — base vectorielle avec schéma et modules.
- ✅ **Milvus** — base vectorielle distribuée à grande échelle.
- ✅ **Pinecone** — base vectorielle managée serverless.
- ✅ **Chroma** — base vectorielle légère orientée prototypage RAG.
- ✅ **Faiss** — bibliothèque ANN Meta (index en mémoire). ⚠️ lib, pas un serveur.
- ✅ **Annoy** — index ANN sur disque (Spotify). ⚠️ lib.
- ✅ **hnswlib** — implémentation HNSW C++/Python. ⚠️ lib.
- ✅ **ScaNN** — ANN Google optimisé. ⚠️ lib.

## Orchestration & ingénierie de données → `data/*`

**Orchestrateurs** — `data/orchestration`
- ✅ **Airflow** — ordonnanceur de DAGs, standard historique.
- ✅ **Dagster** — orchestrateur orienté assets data.
- ✅ **Prefect** — orchestrateur Python moderne.
- ✅ **Mage** — orchestrateur ELT low-code.
- ✅ **Kestra** — orchestrateur déclaratif YAML.
- ✅ **Temporal** — moteur de workflows durables.


**Streaming / lakehouse / formats** — `data/streaming`, `lakehouse`, `format`
- ✅ **Flink** — traitement de flux temps réel.
- ✅ **Apache Iceberg** — format de table lakehouse transactionnel.
- ✅ **Parquet** — format colonnaire sur disque.
- ✅ **Avro** — format ligne avec schéma (sérialisation).

**Parsing de documents** — `data/parsing`
- ✅ **Unstructured** — extraction de contenu multi-format.
- ✅ **Docling** — parsing de documents structurés (IBM).
- ✅ **LlamaParse** — parsing documents orienté LLM/RAG.
- ✅ **Marker** — conversion PDF → Markdown.
- ✅ **PyMuPDF** — extraction texte/images PDF rapide.
- ✅ **pdfplumber** — extraction tableaux et texte PDF.

## Machine Learning & MLOps → `ml/*`, `compute/*`

**Frameworks de modélisation** — `ml/framework`
- ✅ **Scikit-Learn** — ML classique de référence.
- ✅ **XGBoost** — gradient boosting optimisé.
- ✅ **LightGBM** — boosting rapide gros volumes.
- ✅ **CatBoost** — boosting natif catégoriel.
- ✅ **Featuretools** — feature engineering automatisée.
- ✅ **category_encoders** — encodages catégoriels avancés.
- ✅ **PyTorch** — deep learning, recherche et prod.
- ✅ **TensorFlow** — deep learning Google.
- ✅ **JAX** — calcul différentiable haute perf.
- ✅ **HuggingFace** — hub modèles + librairies transformers.
- ✅ **darts** — forecasting unifié (statistique + ML). ⚠️ forecasting.
- ✅ **neuralforecast** — forecasting par réseaux de neurones.
- ✅ **statsforecast** — forecasting statistique rapide.
- ✅ **Prophet** — forecasting additif grand public (Meta).
- ✅ **lifelines** — analyse de survie. ⚠️ ou `tooling/stats`.
- ✅ **hdbscan** — implémentation HDBSCAN. ⚠️ lib du concept HDBSCAN.
- ✅ **umap-learn** — réduction de dimension UMAP. ⚠️ lib.

**Suivi d'expériences** — `ml/tracking`
- ✅ **MLflow** — tracking + registry de modèles.
- ✅ **Weights & Biases** — tracking et visualisation d'expériences.
- ✅ **Neptune** — tracking d'expériences ML.
- ✅ **Comet** — tracking et monitoring ML.
- ✅ **ClearML** — tracking + orchestration.
- ✅ **Aim** — tracking open-source léger.

**Optimisation d'hyperparamètres** — `ml/hyperopt`
- ✅ **Optuna** — optimisation bayésienne + pruning.
- ✅ **Hyperopt** — optimisation TPE historique.
- ✅ **Ray Tune** — HPO distribué (écosystème Ray).

**Serving / inférence** — `ml/serving`
- ✅ **BentoML** — packaging et service de modèles.
- ✅ **NVIDIA Triton** — serveur d'inférence multi-framework.
- ✅ **KServe** — serving sur Kubernetes.
- ✅ **Seldon Core** — serving + explicabilité sur K8s.
- ✅ **TorchServe** — serving PyTorch.
- ✅ **TensorFlow Serving** — serving TensorFlow.
- ✅ **Ray Serve** — serving scalable (écosystème Ray).

**Orchestration ML / feature store** — `ml/orchestration`, `ml/feature-store`
- ✅ **ZenML** — pipelines MLOps portables.
- ✅ **Metaflow** — pipelines ML (Netflix).
- ✅ **Flyte** — pipelines ML/data sur K8s.
- ✅ **Feast** — feature store open-source.

**Calcul distribué** — `compute/distributed`
- ✅ **Ray** — calcul distribué Python générique.
- ✅ **Dask** — parallélisme Python (pandas/numpy à l'échelle).
- ✅ **Spark** — moteur big data distribué.
- ✅ **CuPy** — numpy sur GPU. ⚠️ ou `tooling/data`.


**Exécution locale / serving** — `llm/local`
- ✅ **Ollama** — exécution locale de LLM simplifiée.
- ✅ **llama.cpp** — inférence LLM CPU/GPU en C++.
- ✅ **vLLM** — serving LLM haut débit (PagedAttention).
- ✅ **TGI** — Text Generation Inference (HuggingFace).
- ✅ **SGLang** — runtime de serving LLM rapide.
- ✅ **TensorRT-LLM** — inférence LLM optimisée NVIDIA.
- ✅ **LM Studio** — interface bureau pour LLM locaux.
- ✅ **text-generation-webui** — UI web pour LLM locaux.

**Frameworks d'applications LLM** — `llm/framework`
- ✅ **LangChain** — framework d'apps LLM (chaînes, outils).
- ✅ **LlamaIndex** — framework RAG / indexation.
- ✅ **LangGraph** — graphes d'agents stateful.
- ✅ **Haystack** — framework RAG/recherche (deepset).
- ✅ **DSPy** — programmation et optimisation de prompts.
- ✅ **Semantic Kernel** — orchestration LLM (Microsoft).
- ✅ **PydanticAI** — agents typés (Pydantic).
- ✅ **Instructor** — sorties structurées validées.
- ✅ **LiteLLM** — passerelle unifiée multi-fournisseurs.
- ✅ **AutoGen** — framework multi-agents (Microsoft).
- ✅ **CrewAI** — orchestration d'agents en rôles.

**Évaluation LLM** — `llm/eval`
- ✅ **Ragas** — évaluation de pipelines RAG.
- ✅ **DeepEval** — tests unitaires pour LLM.
- ✅ **TruLens** — évaluation et traçage d'apps LLM.

**Observabilité LLM** — `llm/observability`
- ✅ **Langfuse** — traçage et analytics LLM open-source.
- ✅ **LangSmith** — observabilité (écosystème LangChain).
- ✅ **Phoenix Arize** — observabilité et eval LLM/ML.
- ✅ **Helicone** — proxy d'observabilité LLM.

## Backend, UI, DevOps, stockage, observabilité

**Frameworks backend** — `framework/backend`
- ✅ **FastAPI** — framework API Python async.
- ✅ **Uvicorn** — serveur ASGI (sert FastAPI).

**ORM** — `framework/orm`
- ✅ **Prisma** — ORM TypeScript typé.
- ✅ **SQLAlchemy** — ORM/toolkit SQL Python de référence.
- ✅ **psycopg2** — ORM/toolkit SQL Python Postgres

**Applications data / démos** — `ui/data-app`, `ui/ml-demo`
- ✅ **Streamlit** — apps data en Python pur.
- ✅ **Dash** — apps analytiques (Plotly).
- ✅ **Shiny for Python** — apps réactives (Posit).
- ✅ **Gradio** — démos de modèles ML en quelques lignes.

**DevOps** — `devops/container`, `devops/ci`
- ✅ **Docker** — conteneurisation, packaging reproductible.
- ✅ **GitHub Actions** — CI/CD intégrée à GitHub.

**Stockage objet** — `storage`
- ✅ **MinIO** — stockage objet S3-compatible auto-hébergé.
- ✅ **AWS S3** — stockage objet de référence.
- ✅ **Cloudflare R2** — stockage objet sans frais de sortie.
- ✅ **Ceph** — stockage objet S3-compatible auto-hébergé.
- ✅ **Garage** — stockage objet S3-compatible auto-hébergé.
- ✅ **SeaweedFS** — stockage objet S3-compatible auto-hébergé.

**Observabilité** — `observability/metric`, `observability/log`
- ✅ **Grafana** — dashboards de métriques.
- ✅ **Loki** — agrégation de logs (Grafana).

## Outillage Python → `tooling/*`

**Migrations** — `tooling/migration`
- ✅ **Flyway** — migrations SQL versionnées (JVM).
- ✅ **Liquibase** — migrations multi-format.
- ✅ **Alembic** — migrations de schéma (SQLAlchemy).

**Manipulation de données** — `tooling/data`
- ✅ **pandas** — dataframes Python de référence.
- ✅ **Polars** — dataframes rapides (Rust, lazy).
- ✅ **numpy** — calcul tableau N-dimensionnel.
- ✅ **Modin** — pandas parallélisé.

**Visualisation** — `tooling/viz`
- ✅ **matplotlib** — base de la viz Python.
- ✅ **seaborn** — viz statistique sur matplotlib.
- ✅ **plotly** — viz interactive.
- ✅ **altair** — viz déclarative (Vega-Lite).
- ✅ **bokeh** — viz interactive web.

**Statistiques** — `tooling/stats`
- ✅ **scipy.stats** — lois et tests statistiques.
- ✅ **statsmodels** — modélisation statistique (R-like).
- ✅ **pingouin** — tests statistiques simples et lisibles.
- ✅ **Prince** — analyse factorielle (ACP, ACM, AFC…).
- ✅ **Fanalysis** — analyse factorielle (tradition française).
- ✅ **PyMC** — programmation probabiliste bayésienne.
- ✅ **Stan** — inférence bayésienne (langage dédié).
- ✅ **ArviZ** — diagnostic et viz de modèles bayésiens.
- ✅ **CausalImpact** — impact causal par séries temporelles.

**Config / packaging / tests** — `tooling/package`, `tooling/test`, `tooling/lint`
- ✅ **uv** — gestionnaire de paquets/venv Python ultra-rapide.
- ✅ **pip** — installeur de paquets historique.
- ✅ **Pydantic** — validation de données typée.
- ✅ **Pydantic Settings** — config typée par env.
- ✅ **dynaconf** — gestion de config multi-environnement.
- ✅ **hydra** — config hiérarchique (expériences ML).
- ✅ **python-dotenv** — chargement de `.env`.
- ✅ **Ruff** — linter + formateur Python rapide.
- ✅ **pytest** — framework de tests Python.
- ✅ **testcontainers** — dépendances jetables en conteneur pour les tests.


---

# PARTIE B — Notions (`role: notion`)

> Re-découpés par thème pour sortir du fourre-tout. Le **domaine d'accueil** est indiqué en
> tête de chaque bloc : c'est le dossier de l'arbre où la page se rangera, et sa `categorie:`
> se dérive du vocabulaire de `Documentation/general/taxonomie.md` comme pour une brique.
> Les sous-domaines de galaxie `concept/*` qui figuraient ici sont sortis du vocabulaire
> le 2026-09-05, avec la clôture du lot 4.

## Statistiques → « Statistiques & inférence »

**Inférence & tests**
- ✅ **Tests d'hypothèse** — cadre H0/H1, décision et significativité.
- ✅ **Intervalles de confiance** — estimation d'un paramètre par fourchette.
- ✅ **Test t et ANOVA** — comparaison de moyennes.
- ✅ **Test du khi-deux** — indépendance / ajustement.
- ✅ **Tests non paramétriques** — sans hypothèse de distribution (Wilcoxon…).
- ✅ **Correction des tests multiples** — Bonferroni, FDR.
- ✅ **Analyse de puissance** — taille d'échantillon, puissance.
- ✅ **Bootstrap** — rééchantillonnage pour estimer l'incertitude.

**Expérimentation & causalité**
- ✅ **A/B testing** — comparaison contrôlée de deux variantes.
- ✅ **CUPED** — réduction de variance par données pré-expérience.
- ✅ **Sequential testing** — décision en continu, peeking maîtrisé.
- ✅ **Multi-armed bandits** — allocation adaptative exploration/exploitation.
- ✅ **Diff-in-Diff** — effet causal par doubles différences.

**Bayésien & estimation**
- ✅ **Inférence bayésienne** — a priori × vraisemblance → a posteriori.
- ✅ **Maximum de vraisemblance** — estimation MLE.
- ✅ **Estimation MAP** — maximum a posteriori.
- ✅ **A priori conjugués** — a priori qui simplifient le calcul.

**Probabilités & processus**
- ✅ **Théorème central limite** — convergence vers la loi normale.
- ✅ **Loi des grands nombres** — moyenne empirique → espérance.
- ✅ **Inégalités de concentration** — bornes non asymptotiques.
- ✅ **Chaînes de Markov** — le futur ne dépend que du présent.
- ✅ **MCMC** — échantillonnage par chaînes de Markov.
- ✅ **Processus de Poisson** — événements rares dans le temps.
- ✅ **Mouvement brownien** — processus continu aléatoire.
- ✅ **Autocorrelation** — corrélation d'une série avec elle-même décalée. ⚠️ ou séries temporelles.
- ✅ **Stationarity** — propriétés invariantes dans le temps. ⚠️ ou séries temporelles.

**Analyse factorielle & réduction de dimension**
- ✅ **PCA** — analyse en composantes principales.
- ✅ **CA** — analyse des correspondances.
- ✅ **MCA** — correspondances multiples.
- ✅ **FAMD** — données mixtes (quanti + quali).
- ✅ **MFA** — analyse factorielle multiple (groupes).
- ✅ **GPA** — Procruste généralisée.
- ✅ **PGA** — analyse géodésique principale.
- ✅ **HCPC** — classification sur composantes principales.
- ✅ **Réduction de dimension** — page chapeau.

## Machine learning classique → « Machine Learning »

**Modèles linéaires & régression**
- ✅ **Régression linéaire** — relation linéaire cible continue.
- ✅ **Régression logistique** — classification probabiliste.
- ✅ **Régularisation** — Ridge / Lasso / ElasticNet.
- ✅ **GLM** — modèles linéaires généralisés.
- ✅ **GAM** — modèles additifs généralisés.

**Arbres & ensembles**
- ✅ **Arbres de décision** — segmentation par règles.
- ✅ **Random Forest** — bagging d'arbres décorrélés.
- ✅ **Gradient Boosting (GBDT)** — boosting séquentiel.
- ✅ **Bagging** — ensemble parallèle, réduit la variance.
- ✅ **Boosting** — ensemble séquentiel, réduit le biais.

**Clustering & non supervisé**
- ✅ **Clustering** — page chapeau.
- ✅ **K-Means** — partition par centroïdes.
- ✅ **Classification hiérarchique (CAH)** — dendrogramme.
- ✅ **DBSCAN** — clustering par densité.
- ✅ **HDBSCAN** — DBSCAN hiérarchique.
- ✅ **Gaussian Mixture Models (GMM)** — mélange de gaussiennes.
- ✅ **Clustering evaluation** — silhouette, ARI, indices de qualité.
- ✅ **t-SNE and UMAP** — réduction de dimension non linéaire pour viz.

**Feature engineering**
- ✅ **Ingénierie des caractéristiques** — page chapeau.
- ✅ **Imputation des valeurs manquantes** — médiane, KNN, MICE.
- ✅ **Encodage des variables catégorielles** — One-Hot, Target, WoE.
- ✅ **Mise à l'échelle** — normalisation / standardisation.
- ✅ **Sélection de variables** — filtrage, wrapper, intégré.

**Évaluation & validation**
- ✅ **Validation croisée** — K-Fold, stratifiée, TimeSeries.
- ✅ **ROC-AUC / courbe PR** — sensibilité/spécificité, précision-rappel.
- ✅ **Compromis biais-variance** — sous- vs surapprentissage.
- ✅ **Optimisation d'hyperparamètres** — GridSearch, bayésien.
- ✅ **Classification metrics** — précision, rappel, F1, log-loss.
- ✅ **Regression metrics** — MSE, MAE, R².
- ✅ **Ranking metrics** — NDCG, MAP, MRR.
- ✅ **Calibration** — fiabilité des probabilités prédites.
- ✅ **Imbalanced classification** — gestion des classes déséquilibrées.
- ✅ **Data leakage** — fuite d'information de la cible.
- ✅ **Ensembling** — combiner des modèles (chapeau, au-delà de bagging/boosting).

**Embeddings & dim. reduction**
- ✅ **embeddings** — représentations vectorielles denses.

## MLOps & monitoring → « Machine Learning » (`ml/monitoring`) ou « DevOps »
- ✅ **Data drift** — dérive de distribution en production. ⚠️ sous-domaine MLOps à valider.

## Mathématiques pour le ML → « Mathématiques »

**Algèbre linéaire**
- ✅ **Matrix products** — produits matriciels, sens géométrique.
- ✅ **Matrix decompositions** — LU, QR, Cholesky.
- ✅ **Eigendecomposition** — valeurs/vecteurs propres.
- ✅ **SVD** — décomposition en valeurs singulières.
- ✅ **Vector norms** — normes L1/L2/L∞.
- ✅ **Projections** — projection orthogonale.

**Optimisation**
- ✅ **Convexity** — convexité et garanties d'optimisation.
- ✅ **Gradient descent** — descente de gradient.
- ✅ **Newton & quasi-Newton** — méthodes du second ordre.
- ✅ **Loss landscape and saddle points** — géométrie de la perte.
- ✅ **Learning rate schedules** — planification du pas. ⚠️ ou apprentissage profond.

**Théorie de l'information**
- ✅ **Shannon entropy** — entropie, mesure d'incertitude.
- ✅ **Cross-entropy** — entropie croisée (perte de classification).
- ✅ **KL divergence** — divergence de Kullback-Leibler.
- ✅ **Jensen-Shannon divergence** — divergence symétrisée.
- ✅ **Mutual information** — information mutuelle.
- ✅ **Wasserstein distance** — distance de transport optimal.

**Théorie de l'apprentissage**
- ✅ **PAC learning** — apprentissage PAC.
- ✅ **VC dimension** — capacité d'une classe d'hypothèses.
- ✅ **Rademacher complexity** — complexité de Rademacher.
- ✅ **Generalization bounds** — bornes de généralisation.
- ✅ **No Free Lunch theorem** — pas de modèle universel.

## Deep learning → « Machine Learning » (`ml/apprentissage-profond`)
- ✅ **Transformer architectures** — architecture transformeur.
- ✅ **Self-attention** — mécanisme d'attention.
- ✅ **Positional encoding** — encodage de position.
- ✅ **Flash Attention and efficient attention** — attention optimisée mémoire.
- ✅ **Mixture of Experts** — experts conditionnels (MoE).
- ✅ **State Space Models** — modèles à espace d'états (Mamba).
- ✅ **Adam optimizer** — optimiseur adaptatif.
- ✅ **Distillation** — compression prof → élève.
- ✅ **Quantization** — réduction de précision.
- ✅ **Diffusion models** — modèles génératifs par diffusion.
- ✅ **Image generation** — génération d'images.
- ✅ **Video generation** — génération de vidéos.
- ✅ **Speech models** — modèles de parole (ASR/TTS).
- ✅ **Vision Language Models** — modèles vision-langage.

## LLM & IA générative → « LLM & IA générative »

**Fonctionnement & inférence**
- ✅ **Tokenization** — découpage en tokens.
- ✅ **embeddings** — (cf. ML) représentations denses, base du RAG.
- ✅ **Decoding strategies** — greedy, top-k, top-p, beam.
- ✅ **Perplexity** — mesure de qualité d'un modèle de langue.
- ✅ **Inference optimization** — KV-cache, batching.
- ✅ **Speculative decoding** — décodage spéculatif.
- ✅ **Scaling laws** — lois d'échelle.
- ✅ **Small Language Models** — petits modèles efficaces.
- ✅ **Reasoning models** — modèles de raisonnement.
- ✅ **prompt-caching** — cache de préfixes de prompt.
- ✅ **LLM caching** — mise en cache des réponses.

**RAG & retrieval**
- ✅ **RAG** — génération augmentée par récupération.
- ✅ **Advanced RAG** — RAG avancé (multi-étapes).
- ✅ **Chunking strategies** — découpage des documents.
- ✅ **Hybrid retrieval** — dense + lexical (BM25).
- ✅ **Reranking** — reclassement des passages.
- ✅ **Query transformations** — réécriture de requêtes.
- ✅ **Routing and cascading** — routage et cascade de modèles.
- ✅ **RAG eval** — évaluation des pipelines RAG.

**Agents**
- ✅ **Agent patterns** — patrons d'agents.
- ✅ **agent-loops** — boucle perception-action.
- ✅ **Agent memory** — mémoire d'agent.
- ✅ **Agent evaluation** — évaluation d'agents.
- ✅ **Multi-agent systems** — systèmes multi-agents.
- ✅ **Tool use patterns** — patrons d'appel d'outils.
- ✅ **tool-use** — appel d'outils par LLM.
- ✅ **mcp-protocol** — Model Context Protocol.
- ✅ **Context engineering** — ingénierie de contexte.
- ✅ **Structured outputs** — sorties structurées (JSON).
- ✅ **Reliability patterns** — fiabilité des apps LLM.

**Prompting & alignement**
- ✅ **Prompt engineering** — conception de prompts.
- ✅ **Chain-of-Thought** — raisonnement pas à pas.
- ✅ **RLHF and DPO** — alignement par préférences.
- ✅ **SFT** — fine-tuning supervisé.
- ✅ **PEFT** — fine-tuning paramétriquement efficace (LoRA).
- ✅ **Reward modeling** — modèle de récompense.
- ✅ **RL for LLMs** — RL appliqué aux LLM.
- ✅ **GRPO** — optimisation de politique par groupes.
- ✅ **Synthetic data generation** — génération de données synthétiques.

**Évaluation LLM**
- ✅ **LLM eval metrics** — métriques d'évaluation LLM.
- ✅ **LLM-as-judge** — LLM évaluateur.
- ✅ **LLM benchmarks** — bancs d'essai LLM.
- ✅ **Code and math benchmarks** — benchmarks code/maths.
- ✅ **LLM observability** — observabilité en production.

## Sécurité IA → « Sécurité » (`security/ia`)
- ✅ **AI security** — panorama des risques IA.
- ✅ **Prompt injection** — injection de prompt.
- ✅ **Jailbreaking and defenses** — contournements et défenses.
- ✅ **Guardrails** — garde-fous d'entrée/sortie.

## Reinforcement learning → « Machine Learning » (`ml/rl`)
- ✅ **Reinforcement learning** — cadre général.
- ✅ **Markov Decision Process** — MDP.
- ✅ **Bellman equations** — équations de Bellman.
- ✅ **Value functions** — fonctions de valeur.
- ✅ **Q-learning and DQN** — apprentissage par valeurs.
- ✅ **Policy gradient** — gradient de politique.
- ✅ **PPO** — Proximal Policy Optimization.
- ✅ **Actor-Critic methods** — acteur-critique.
- ✅ **Exploration vs exploitation** — dilemme exploration/exploitation.
- ✅ **Model-based RL** — RL basé modèle.
- ✅ **Offline RL** — RL hors ligne.
- ✅ **Imitation learning** — apprentissage par imitation.
- ✅ **Reward shaping and hacking** — façonnage et détournement de récompense.

## Séries temporelles & forecasting → « Machine Learning » (`ml/series-temporelles`)
- ✅ **ARIMA SARIMA** — modèles autorégressifs.
- ✅ **Exponential smoothing** — lissage exponentiel.
- ✅ **Forecasting framing** — cadrage d'un problème de prévision.
- ✅ **Forecasting metrics** — métriques de prévision (MAPE…).
- ✅ **Hierarchical forecasting** — prévision hiérarchique.
- ✅ **Intermittent demand** — demande intermittente.
- ✅ **Time series feature engineering** — features temporelles.
- ✅ **Time series anomaly detection** — détection d'anomalies.
- ✅ **Walk-forward CV** — validation glissante temporelle.

---

# PARTIE C — Skills perso & workflows

## Outils en ligne de commande → « Outils de développement » (`devtools/*`)
- ✅ **uv** — gestionnaire de paquets/venv Python. C'est une **brique**, pas un skill perso.

## Skills Claude Code → « Outils de développement » (`skill/*`)
- ⬜ anthropic-{consolidate-memory, docx, pdf, pptx, setup-cowork, skill-creator, xlsx}
- ⬜ claude-{api, fewer-permission-prompts, init, keybindings-help, loop, review, schedule, security-review, simplify, update-config}

## Serveurs MCP → « Outils de développement » (`skill/knowledge` ou à valider)
- ⬜ mcp-{filesystem, github, obsidian, postgres}
- ⬜ mcp-obsidian — reference outils

## Extensions Obsidian → « Outils de développement » (`skill/knowledge`)
- ⬜ kepano-defuddle — extraction d'article propre.
- ⬜ kepano-obsidian-skills — skills Obsidian officiels.

## Workflows → domaine à dériver de leur sujet (le dossier `Wiki/Workflows/` n'existe plus)
- ⬜ Bootstrap projet AI eng
- ⬜ Debug pipeline data
- ⬜ Evaluer un modele forecast
- ⬜ Evaluer un systeme LLM

## Index & guides v1 (référence, non migrables tels quels)
- _guide, _installer-un-skill, Roadmap, Roadmap-AI — repensés en v2 puis en v3 (les hubs de l'arbre, `Documentation/`). Le dossier `Wiki/Roadmaps/` n'existe plus.

---

# PARTIE D — Patterns & Rules v1 (référence)

## Patterns → « Patterns/ » (`role: pattern`)
- ⬜ Pattern - Agent ReAct · Pattern - API REST FastAPI minimale · Pattern - CLI Python distribuable · Pattern - Forecasting production · Pattern - LLM Eval setup · Pattern - Pipeline ELT moderne · Pattern - RAG basique · Pattern - SaaS multi-tenant
- ⬜ Comparatif - Bases vectorielles *(refait en `.base` v2)* · Comparatif - LLM eval et observability · Comparatif - ML orchestration · Comparatif - Orchestrateurs data

## Rules → « Rules/ » (`role: rule`)
- **Global** : ⬜ Code-style · Documentation · Git · README · Security · Tests
- **Types** : ⬜ CLI · Data-pipeline · Library · ML-pipeline · Web-app
- **Documentation** : ⬜ Config-Env · Database-{Graph,Relational,Vector} · Document-Processing · LLM-Orchestration · Orchestration-Data · Storage-Object · Project-README · README - Service · Tests · Index

## REX (v1) → section `## Pièges` de la brique concernée
- ⬜ **REX - Postgres** — *(le REX v1 existe dans le réservoir ; le pilier REX est supprimé depuis le 2026-09-02 — audit axe 6, option B. À reporter, si utile, dans la section `## Pièges` de `Bases de données/Relationnel/Postgres.md`).*
