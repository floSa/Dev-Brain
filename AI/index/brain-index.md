# Index — DevBrain v2

> Document généré par `AI/scripts/build_index.py`. Ne pas éditer à la main.
> 584 pages actives. Réservoir v1 (0 pages Wiki) : référence, non indexé.

## Dev — briques techniques (galaxie dev)

### service

#### auth
- **PyJWT** — Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.

#### automation/ai-agent
- **gumloop** — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

#### automation/ipaas
- **Zapier** — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.

#### automation/workflow
- **Activepieces** — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- **n8n** — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- **Windmill** — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.

#### compute/distributed
- **CuPy** — NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code.
- **Dask** — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- **Ray** — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).
- **Spark** — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

#### data/format
- **Avro** — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.
- **Parquet** — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.

#### data/lakehouse
- **Apache Iceberg** — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB).

#### data/orchestration
- **Airflow** — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- **Dagster** — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- **Kestra** — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- **Mage** — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- **Prefect** — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- **Temporal** — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

#### data/parsing
- **Docling** — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- **LlamaParse** — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- **Marker** — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- **pdfplumber** — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- **PyMuPDF** — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- **Unstructured** — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.

#### data/scraping
- **cloudscraper** — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- **Crawlee** — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- **curl_cffi** — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- **Firecrawl** — API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.
- **Maxun** — Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.
- **Playwright** — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.
- **Scrapling** — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.
- **Scrapy** — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- **selectolax** — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages.

#### data/streaming
- **Flink** — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch.

#### database/columnar
- **ClickHouse** — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.
- **DuckDB** — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.

#### database/document
- **MongoDB** — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.

#### database/driver
- **ADBC** — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.
- **psycopg2** — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3.

#### database/graph
- **Nebula Graph** — Base de graphes distribuée pour jeux de données massifs.
- **Neo4j** — SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.

#### database/keyvalue
- **Redis** — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.

#### database/relational
- **CockroachDB** — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- **MariaDB** — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- **Microsoft SQL Server** — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.
- **MySQL** — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- **Postgres** — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- **SQLite** — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.

#### database/search
- **Elasticsearch** — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- **Marqo** — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- **txtai** — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- **Vespa** — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.

#### database/timeseries
- **InfluxDB** — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.
- **TimescaleDB** — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

#### database/vector
- **Annoy** — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- **Chroma** — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.
- **Faiss** — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- **hnswlib** — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- **LanceDB** — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- **Milvus** — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- **pgvector** — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- **Pinecone** — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.
- **Qdrant** — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- **ScaNN** — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- **Weaviate** — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.

#### database/wide-column
- **Apache Cassandra** — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

#### devops/ci
- **GitHub Actions** — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.

#### devops/container
- **Docker** — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre.

#### framework/backend
- **FastAPI** — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.
- **Flask** — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.
- **Uvicorn** — Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI.

#### framework/frontend
- **HTMX** — Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd.
- **Jinja2** — Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask.

#### framework/orm
- **Prisma** — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.
- **SQLAlchemy** — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- **SQLModel** — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

#### llm/eval
- **DeepEval** — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- **promptfoo** — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.
- **Ragas** — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- **TruLens** — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

#### llm/finetuning
- **Axolotl** — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- **LLaMA-Factory** — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- **TRL** — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- **Tunix** — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.
- **Unsloth** — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.

#### llm/framework
- **Agno** — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- **AutoGen** — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- **CrewAI** — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- **DB-GPT** — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.
- **Dify** — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.
- **DSPy** — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.
- **fastmcp** — La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma.
- **Flowise** — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.
- **Guidance** — Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing.
- **Haystack** — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- **Instructor** — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- **LangChain** — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- **Langflow** — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- **LangGraph** — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.
- **Letta** — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- **LiteLLM** — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- **LlamaIndex** — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- **OpenAI Agents SDK** — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- **OpenHands** — Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé.
- **OpenRouter** — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.
- **Outlines** — Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas.
- **PydanticAI** — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).
- **RAGatouille** — Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (0.0.9, février 2025).
- **Semantic Kernel** — SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur.
- **smolagents** — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- **Vanna** — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- **WrenAI** — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.

#### llm/framework-module
- **LangChain SQL agent** — Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle.
- **LlamaIndex NLSQLTableQueryEngine** — Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle.

#### llm/local
- **llama.cpp** — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- **LM Studio** — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- **Ollama** — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- **SGLang** — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- **TensorRT-LLM** — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.
- **text-generation-webui** — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- **TGI** — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- **vLLM** — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.

#### llm/observability
- **Helicone** — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.
- **Langfuse** — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- **LangSmith** — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- **Phoenix Arize** — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.

#### ml/eval
- **evaluate** — Bibliothèque HuggingFace de métriques d'évaluation ML prêtes à l'emploi — accuracy, F1, BLEU, ROUGE, exact match… chargées depuis le Hub via une API unique load/compute, comparables d'un projet à l'autre.
- **seqeval** — Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger.

#### ml/feature-store
- **Feast** — Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…).

#### ml/framework
- **Acme** — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- **albumentations** — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- **bm25s** — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.
- **CatBoost** — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- **category_encoders** — Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité.
- **Chronos** — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params).
- **darts** — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- **datasets** — Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub.
- **DeepSpeed** — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.
- **Detectron2** — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.
- **docTR** — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- **Featuretools** — Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables.
- **GLiNER** — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger.
- **Gymnasium** — Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements.
- **hdbscan** — Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster).
- **HuggingFace** — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes.
- **imbalanced-learn** — Rééchantillonnage pour classes déséquilibrées, API compatible scikit-learn — SMOTE et variantes, undersampling, méthodes combinées et ensembles rééquilibrés, dans un Pipeline qui cantonne le resampling au pli d'entraînement.
- **JAX** — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.
- **Keras** — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework.
- **Kornia** — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.
- **librosa** — Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.
- **lifelines** — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.
- **LightGBM** — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- **LIME** — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales.
- **neuralforecast** — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- **NLTK** — Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique.
- **OpenCV** — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning.
- **OpenSpiel** — Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python.
- **PaCMAP** — Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable.
- **pmdarima** — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.
- **Prophet** — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- **pykan** — Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance.
- **PyOD** — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.
- **PyTorch** — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- **PyTorch Geometric** — Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN.
- **PyTorch Lightning** — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.
- **pytorch-crf** — Couche CRF (champ aléatoire conditionnel) pour PyTorch — modélise les dépendances entre labels voisins et décode par Viterbi ; brique de sortie classique d'un tagger d'étiquetage de séquence.
- **rank-bm25** — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.
- **River** — ML en ligne / streaming en Python — apprentissage incrémental échantillon par échantillon (learn_one/predict_one) couvrant classification, régression, clustering, détection d'anomalies et de dérive ; issu de la fusion creme + scikit-multiflow.
- **RLax** — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.
- **Scikit-Learn** — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
- **SDV** — Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL).
- **segment-anything** — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte).
- **sentence-transformers** — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi.
- **sentencepiece** — Tokeniseur sous-mot de Google, indépendant de la langue — BPE et modèle Unigram entraînés directement sur du texte brut (Unicode/octets, sans pré-tokenisation), implémentation C++ et bindings Python.
- **SetFit** — Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM.
- **SHAP** — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- **spaCy** — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.
- **Stable-Baselines3** — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- **statsforecast** — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- **STUMPY** — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.
- **supervision** — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application.
- **TensorFlow** — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.
- **TF-Agents** — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- **timm** — La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision.
- **torchvision** — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- **Ultralytics YOLO** — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0.
- **umap-learn** — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.
- **XGBoost** — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.

#### ml/hyperopt
- **Hyperopt** — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.
- **Optuna** — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- **Ray Tune** — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

#### ml/monitoring
- **Evidently** — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.

#### ml/orchestration
- **Flyte** — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.
- **Metaflow** — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- **ZenML** — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.

#### ml/serving
- **BentoML** — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- **KServe** — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- **NVIDIA Triton** — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- **ONNX Runtime** — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge.
- **Ray Serve** — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.
- **Seldon Core** — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- **TensorFlow Serving** — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- **TensorRT** — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM.
- **TorchServe** — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.

#### ml/tracking
- **Aim** — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- **ClearML** — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- **Comet** — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- **MLflow** — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- **Neptune** — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- **TensorBoard** — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.
- **Weights & Biases** — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.

#### ml/training
- **accelerate** — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.

#### observability/log
- **Loki** — Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana.

#### observability/metric
- **Grafana** — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud.

#### storage
- **AWS S3** — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- **Ceph** — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- **Cloudflare R2** — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.
- **Garage** — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- **MinIO** — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- **SeaweedFS** — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.

#### tooling/data
- **connectorx** — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.
- **Faker** — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- **Mimesis** — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- **Modin** — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- **numpy** — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- **pandas** — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- **Polars** — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- **PyWavelets** — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- **scipy.signal** — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.
- **xarray** — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).

#### tooling/lint
- **Ruff** — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.

#### tooling/migration
- **Alembic** — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.
- **Flyway** — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- **Liquibase** — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.

#### tooling/notebook
- **jupysql** — SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats.
- **jupytext** — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.
- **Marimo** — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.
- **papermill** — Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI.
- **Quarto** — Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia).

#### tooling/optim
- **PuLP** — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).

#### tooling/package
- **dynaconf** — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- **hydra** — Framework de configuration hiérarchique composable (Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- **pip** — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.
- **Pydantic** — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.
- **Pydantic Settings** — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.
- **python-dotenv** — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- **Rich** — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.
- **Typer** — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.
- **uv** — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

#### tooling/stats
- **ArviZ** — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- **CausalImpact** — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.
- **Fanalysis** — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR.
- **pingouin** — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- **Prince** — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
- **PyMC** — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- **scipy.stats** — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- **Stan** — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
- **statsmodels** — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.

#### tooling/test
- **mcpjam** — « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM.
- **pytest** — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.
- **testcontainers** — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.

#### tooling/viz
- **altair** — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.
- **bokeh** — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- **matplotlib** — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.
- **missingno** — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.
- **plotly** — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- **seaborn** — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.
- **sweetviz** — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- **ydata-profiling** — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.

#### ui/data-app
- **Dash** — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- **Shiny for Python** — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- **Streamlit** — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.

#### ui/ml-demo
- **Gradio** — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

### pattern

#### (sans catégorie)
- **Pattern - Moteur de jeu pur + IA séparée** — —
- **Pattern - Pipeline scraping → matching → optimisation** — —
- **Pattern - RAG structuré graphe + human-in-the-loop** — —
- **Pattern - Stack démo ML locale multi-services** — —

### rule

#### (sans catégorie)
- **Rule - Config typée** — —
- **Rule - Packaging démo** — —
- **Rule - Qualité stricte** — —
- **Rule - Structure de projet** — —
- **Rule - Toolchain Python** — —

### rex

#### (sans catégorie)
- **REX - Postgres** — —

### outil

#### tooling/api
- **Bruno** — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.
- **Postman** — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.

#### tooling/code-assistant
- **Aider** — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- **Cline** — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- **Continue** — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- **Graphify** — Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.

#### tooling/db-admin
- **DataGrip** — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- **DBeaver** — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- **HeidiSQL** — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- **MongoDB Compass** — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- **MySQL Workbench** — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- **pgAdmin** — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- **Redis Insight** — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).

#### tooling/design
- **Figma** — Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.
- **Penpot** — Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.

#### tooling/diagram
- **draw.io** — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- **Excalidraw** — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- **FossFLOW** — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.
- **Mermaid** — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.

#### tooling/media
- **Claude Video** — Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.

## Wiki — notions (galaxie wiki)

### concept

#### concept/ai
- **AI security** — domaines : ai-eng · alias : sécurité IA, sécurité LLM, LLM security, AI security, OWASP LLM Top 10, sécurité des apps LLM
- **Guardrails** — domaines : ai-eng · alias : garde-fous, guardrails, garde-fous LLM, garde-fous d'entrée/sortie
- **Jailbreaking and defenses** — domaines : ai-eng · alias : jailbreak, jailbreaking, contournement de l'alignement, jailbreaking and defenses, DAN
- **Prompt injection** — domaines : ai-eng · alias : injection de prompt, prompt injection, indirect prompt injection, injection indirecte, LLM01

#### concept/data
- **Architecture médaillon** — domaines : data-eng · alias : medallion, médaillon, architecture médaillon, bronze silver gold, bronze/silver/gold, multi-hop architecture
- **Bases de données** — domaines : data-eng, data-sci, ai-eng · alias : base de données, bdd, database, sgbd, dbms
- **Bases de données vectorielles** — domaines : data-eng, ai-eng · alias : vector db, vector store, base vectorielle
- **Change Data Capture (CDC)** — domaines : data-eng · alias : CDC, change data capture, capture de changements, log-based replication
- **Contrats de données & qualité** — domaines : data-eng · alias : data contract, contrat de données, data quality, qualité des données, freshness, fraîcheur, validation de données
- **ELT vs ETL & idempotence** — domaines : data-eng · alias : ELT, ETL, idempotence, rejouabilité, backfill, rerun
- **Index ANN — internes** — domaines : data-eng, ai-eng · alias : ANN, index ANN, HNSW, IVF, PQ, product quantization, approximate nearest neighbor, recherche ANN
- **Migrations de schéma** — domaines : data-eng · alias : migration, migrations, schema migration, db migration
- **Notebooks-as-code** — domaines : data-sci, mlops · alias : notebooks as code, jupytext, pairing de notebooks, notebook pairing, notebooks reproductibles, nbstripout
- **ORM** — domaines : data-eng · alias : orm, object-relational mapping, mapping objet-relationnel
- **Partitionnement & layout de données** — domaines : data-eng · alias : partitionnement, partitioning, data layout, layout de données, bucketing, partition pruning, taille de fichiers, small files problem
- **Stream processing** — domaines : data-eng · alias : stream processing, traitement de flux, windowing, fenêtrage, watermarks, exactly-once, event-time
- **Versionnage de données** — domaines : data-eng, mlops · alias : data versioning, versionnage de données, DVC, lakeFS, time travel, data lineage
- **Web scraping** — domaines : data-eng · alias : scraping, web scraping, crawling, extraction de données web, headless browsing

#### concept/dl
- **Adam optimizer** — domaines : data-sci, ml-eng · alias : Adam, AdamW, adaptive moment estimation, RMSprop, Adagrad, optimiseur adaptatif
- **Apprentissage auto-supervisé en vision** — domaines : data-sci, ml-eng · alias : self-supervised learning, SSL, auto-supervisé, SimCLR, MoCo, BYOL, DINO, MAE, masked autoencoder, apprentissage contrastif
- **Architectures CNN** — domaines : ml-eng · alias : ResNet, MobileNet, EfficientNet, ConvNeXt, backbone vision, CNN architectures
- **Augmentation d'images** — domaines : data-sci, ml-eng · alias : data augmentation, augmentation de données, Mixup, CutMix, RandAugment
- **Classification audio par spectrogramme** — domaines : data-sci, ml-eng · alias : classification audio, audio classification, sound classification, reconnaissance de sons, audio CNN, mel-spectrogramme CNN, acoustic scene classification, SpecAugment
- **Classification d'images** — domaines : data-sci, ml-eng · alias : image classification, classification d'image, top-1, top-5, ImageNet
- **CNN** — domaines : data-sci, ml-eng · alias : convnet, réseau convolutif, convolutional neural network, convolution, pooling, champ réceptif
- **Diffusion models** — domaines : ml-eng, ai-eng · alias : DDPM, denoising diffusion, score-based models, latent diffusion, modèles de diffusion, diffusion
- **Distillation** — domaines : ml-eng, ai-eng · alias : Knowledge distillation, distillation de connaissances, teacher-student, distillation prof-élève, soft labels, dark knowledge
- **Détection d'objets** — domaines : data-sci, ml-eng · alias : object detection, détection d'objet, bounding box, boîtes englobantes, anchors, NMS, YOLO, Faster R-CNN, RetinaNet, DETR
- **Entraînement distribué** — domaines : ml-eng, mlops · alias : Distributed training, DDP, DistributedDataParallel, FSDP, ZeRO, data parallelism, model parallelism, pipeline parallelism, tensor parallelism, sharding, DeepSpeed, parallélisme de données
- **Estimation de pose** — domaines : data-sci, ml-eng · alias : pose estimation, keypoints, points-clés, pose humaine, OpenPose, HRNet, ViTPose, MediaPipe, OKS, PCK, heatmap
- **Flash Attention and efficient attention** — domaines : ml-eng, mlops, ai-eng · alias : Flash Attention, FlashAttention, attention efficace, multi-query attention, MQA, grouped-query attention, GQA, sparse attention, sliding window attention
- **GANs** — domaines : ml-eng, ai-eng · alias : GAN, generative adversarial network, génération adversariale, réseau antagoniste génératif, DCGAN, StyleGAN, WGAN, CycleGAN, pix2pix
- **Gradient checkpointing** — domaines : ml-eng · alias : Gradient checkpointing, activation checkpointing, recomputation, rematerialization, rematérialisation, recalcul d'activations, checkpoint
- **Graph Neural Networks** — domaines : ml-eng, data-sci · alias : GNN, graph neural network, réseaux de neurones sur graphes, GCN, GAT, GraphSAGE, message passing, passage de messages
- **Image generation** — domaines : ml-eng, ai-eng · alias : text-to-image, T2I, génération d'images, Stable Diffusion, DALL-E, Midjourney, FLUX, inpainting
- **Kolmogorov-Arnold Networks** — domaines : ml-eng · alias : KAN, KANs, réseaux de Kolmogorov-Arnold, kolmogorov-arnold network
- **Metric learning & ré-identification** — domaines : data-sci, ml-eng · alias : metric learning, apprentissage de métrique, ré-identification, re-identification, re-id, person re-id, reconnaissance faciale, face recognition, triplet loss, contrastive loss, ArcFace, CosFace, Siamese, CMC, Rank-1
- **Mixed precision** — domaines : ml-eng · alias : Mixed precision, précision mixte, AMP, automatic mixed precision, fp16, bf16, float16, bfloat16, loss scaling, autocast, half precision, demi-précision
- **Mixture of Experts** — domaines : ml-eng, ai-eng · alias : MoE, mélange d'experts, sparse MoE, Switch Transformer, experts conditionnels, top-k routing
- **Modèles de fondation vision** — domaines : ml-eng, ai-eng · alias : foundation models vision, vision foundation models, CLIP, DINOv2, DINOv3, SigLIP, OpenCLIP, modèles de fondation visuels
- **Métriques vision** — domaines : data-sci, ml-eng · alias : métriques de vision, vision metrics, mAP, mean average precision, IoU, intersection over union, Dice, mIoU, AP
- **OCR** — domaines : data-sci, ml-eng · alias : reconnaissance optique de caractères, reconnaissance de texte, text recognition, text detection, scene text, Tesseract, PaddleOCR, EasyOCR, docTR, CRNN, CTC, TrOCR, CER, WER
- **Positional encoding** — domaines : ml-eng, ai-eng · alias : encodage de position, encodage positionnel, RoPE, rotary embeddings, ALiBi, sinusoidal positional encoding
- **Pruning** — domaines : ml-eng, ai-eng · alias : Pruning, élagage, élagage de modèle, sparsity, sparsité, structured pruning, unstructured pruning, élagage structuré, élagage non structuré, magnitude pruning, lottery ticket
- **Quantization** — domaines : ml-eng, ai-eng · alias : Quantification, quantisation, INT8, INT4, FP8, GGUF, GPTQ, AWQ, PTQ, QAT, K-quants
- **Rendu neuronal 3D & estimation de profondeur** — domaines : data-sci, ml-eng · alias : NeRF, neural radiance fields, 3D Gaussian Splatting, 3DGS, gaussian splatting, rendu neuronal, novel view synthesis, estimation de profondeur, depth estimation, MiDaS, DPT, Depth Anything
- **Segment Anything (SAM)** — domaines : ml-eng, ai-eng · alias : SAM, Segment Anything Model, segmentation promptable, promptable segmentation, SAM 2, SAM 3, SA-1B
- **Segmentation** — domaines : data-sci, ml-eng · alias : segmentation d'image, image segmentation, segmentation sémantique, segmentation d'instance, segmentation panoptique, U-Net, Mask R-CNN, DeepLab
- **Self-attention** — domaines : ml-eng, ai-eng · alias : auto-attention, scaled dot-product attention, multi-head attention, MHA, attention QKV, cross-attention
- **Speech models** — domaines : ml-eng, ai-eng · alias : ASR, TTS, speech-to-text, text-to-speech, reconnaissance vocale, synthèse vocale, Whisper, modèles de parole, speech-to-speech
- **State Space Models** — domaines : ml-eng, ai-eng · alias : SSM, modèles à espace d'états, Mamba, S4, S5, selective state space, linear-time sequence model
- **Suivi d'objets** — domaines : data-sci, ml-eng · alias : object tracking, MOT, multi-object tracking, suivi multi-cibles, tracking-by-detection, SORT, DeepSORT, ByteTrack, Kalman, MOTA, IDF1, HOTA
- **Transfer learning vision** — domaines : data-sci, ml-eng · alias : transfer learning, transfert d'apprentissage, fine-tuning vision, feature extraction, backbone gelé
- **Transformer architectures** — domaines : ml-eng, ai-eng · alias : Transformer, transformeur, architecture transformeur, encoder-decoder, decoder-only, encoder-only
- **Video generation** — domaines : ml-eng, ai-eng · alias : text-to-video, T2V, génération de vidéos, Sora, video diffusion, image-to-video
- **Vision Language Models** — domaines : ml-eng, ai-eng · alias : VLM, vision-language models, modèles vision-langage, multimodal LLM, MLLM, image-text
- **Vision par ordinateur** — domaines : data-sci, ml-eng · alias : computer vision, CV, vision
- **Vision Transformers (ViT)** — domaines : ml-eng, ai-eng · alias : ViT, Vision Transformer, vision transformers, DeiT, Swin Transformer, transformeur de vision

#### concept/llm
- **Advanced RAG** — domaines : ai-eng · alias : RAG avancé, advanced retrieval-augmented generation, modular RAG
- **Agent evaluation** — domaines : ai-eng · alias : évaluation d'agents, agent evaluation, agent eval
- **Agent memory** — domaines : ai-eng · alias : mémoire d'agent, agent memory, mémoire LLM
- **Agent patterns** — domaines : ai-eng · alias : patrons d'agents, agent design patterns, agentic patterns
- **agent-loops** — domaines : ai-eng · alias : agent loop, boucle d'agent, boucle perception-action, agentic loop
- **Chain-of-Thought** — domaines : ai-eng · alias : CoT, chaîne de pensée, raisonnement pas à pas, self-consistency, zero-shot CoT
- **Chunking strategies** — domaines : ai-eng · alias : chunking, découpage de documents, stratégies de découpage, text splitting
- **Code and math benchmarks** — domaines : ai-eng, ml-eng · alias : benchmarks code, benchmarks maths, HumanEval, MBPP, SWE-bench, GSM8K, MATH, AIME, pass@k, éval par exécution
- **Constrained decoding** — domaines : ai-eng · alias : génération contrainte, décodage contraint, structured generation, grammar-constrained decoding
- **Construction de graphes de connaissances** — domaines : ai-eng · alias : knowledge graph construction, KG construction, extraction d'entités et de relations, knowledge graph building, peuplement de graphe de connaissances
- **Context engineering** — domaines : ai-eng · alias : ingénierie de contexte, gestion du contexte, context window management
- **Decoding strategies** — domaines : ai-eng · alias : stratégies de décodage, décodage, sampling, greedy, top-k, top-p, nucleus sampling, beam search, température
- **GraphRAG** — domaines : ai-eng · alias : graph RAG, knowledge graph RAG, RAG sur graphe, RAG augmenté par graphe de connaissances
- **GRPO** — domaines : ml-eng, ai-eng · alias : Group Relative Policy Optimization, optimisation de politique par groupes, optimisation de politique relative par groupe
- **Human-in-the-loop** — domaines : ai-eng · alias : HITL, human in the loop, supervision humaine, validation humaine, intervention humaine
- **Hybrid retrieval** — domaines : ai-eng · alias : recherche hybride, hybrid search, retrieval hybride, dense + sparse
- **Inference optimization** — domaines : ai-eng, mlops · alias : optimisation de l'inférence, KV-cache, cache KV, continuous batching, batching dynamique, PagedAttention, débit LLM, latence LLM
- **Late-interaction retrieval** — domaines : ai-eng · alias : colbert, colbertv2, late interaction, interaction tardive, recherche multi-vecteur, plaid, maxsim
- **LLM benchmarks** — domaines : ai-eng, ml-eng · alias : bancs d'essai LLM, benchmarks LLM, leaderboard, MMLU, GPQA, BBH, IFEval, MT-Bench, Chatbot Arena, LMArena, HELM
- **LLM caching** — domaines : ai-eng · alias : response caching, cache de réponses LLM, semantic cache, cache sémantique, exact-match cache, GPTCache
- **LLM eval metrics** — domaines : ai-eng · alias : métriques d'évaluation LLM, évaluation LLM, LLM evaluation, exact match, BLEU, ROUGE, BERTScore, pass@k, G-Eval, offline eval
- **LLM observability** — domaines : ai-eng, mlops · alias : observabilité LLM, observabilité des apps LLM, tracing LLM, online eval, monitoring LLM, traces, spans, coûts tokens
- **LLM-as-judge** — domaines : ai-eng · alias : LLM as a judge, LLM juge, LLM évaluateur, G-Eval, pairwise comparison, reference-free evaluation, MT-Bench
- **LoRA et QLoRA** — domaines : ml-eng, ai-eng · alias : LoRA, Low-Rank Adaptation, QLoRA, quantized LoRA, adapters LoRA, low-rank adapters
- **mcp-protocol** — domaines : ai-eng · alias : MCP, Model Context Protocol, protocole MCP
- **Multi-agent systems** — domaines : ai-eng · alias : systèmes multi-agents, multi-agent systems, MAS
- **PEFT** — domaines : ml-eng, ai-eng · alias : parameter-efficient fine-tuning, fine-tuning paramétriquement efficace, adapters
- **Perplexity** — domaines : ai-eng · alias : perplexité, PPL
- **Prompt engineering** — domaines : ai-eng · alias : conception de prompts, prompt design, few-shot prompting, in-context learning
- **prompt-caching** — domaines : ai-eng · alias : prompt caching, cache de préfixes de prompt, prefix caching, cache de prompt, context caching
- **Query transformations** — domaines : ai-eng · alias : query transformation, réécriture de requête, query rewriting, query expansion, query decomposition, multi-query, HyDE, step-back prompting
- **RAG** — domaines : ai-eng · alias : Retrieval-Augmented Generation, génération augmentée par récupération, retrieval augmented generation
- **RAG eval** — domaines : ai-eng · alias : RAG evaluation, évaluation RAG, évaluation des pipelines RAG, faithfulness, groundedness, context precision, context recall, answer relevancy
- **Reasoning models** — domaines : ai-eng · alias : modèles de raisonnement, reasoning model, large reasoning model, LRM, test-time compute, inference-time scaling, long chain-of-thought, thinking models
- **Reliability patterns** — domaines : ai-eng · alias : patrons de fiabilité, reliability patterns, fiabilité des apps LLM
- **Reranking** — domaines : ai-eng · alias : reranking, reclassement, re-ranking, rerank
- **Reward modeling** — domaines : ml-eng, ai-eng · alias : reward model, modèle de récompense, RM, preference model, modèle de préférence, RLAIF
- **RL for LLMs** — domaines : ml-eng, ai-eng · alias : RL for language models, reinforcement learning for LLMs, RL appliqué aux LLM, RL post-training, post-training RL, RLVR
- **RLHF and DPO** — domaines : ml-eng, ai-eng · alias : RLHF, DPO, alignement par préférences, preference tuning, direct preference optimization
- **Routing and cascading** — domaines : ai-eng · alias : routing, query routing, semantic routing, model routing, model cascading, cascade de modèles, routage et cascade
- **Scaling laws** — domaines : ai-eng, ml-eng · alias : lois d'échelle, loi d'échelle, scaling law, Chinchilla, Kaplan, compute-optimal
- **Server-Sent Events & streaming LLM** — domaines : ai-eng · alias : SSE, server-sent events, streaming LLM, streaming de tokens, sse-starlette, text/event-stream, EventSource
- **SFT** — domaines : ml-eng, ai-eng · alias : supervised fine-tuning, fine-tuning supervisé, instruction tuning, instruction fine-tuning
- **Small Language Models** — domaines : ai-eng · alias : SLM, petits modèles de langage, small language model, modèles compacts, edge LLM, on-device LLM
- **Speculative decoding** — domaines : ai-eng · alias : décodage spéculatif, speculative sampling, échantillonnage spéculatif, draft model, modèle brouillon, EAGLE, Medusa
- **Structured outputs** — domaines : ai-eng · alias : sorties structurées, sortie structurée, JSON mode
- **Synthetic data generation** — domaines : ml-eng, ai-eng · alias : synthetic data, génération de données synthétiques, données synthétiques, self-instruct, evol-instruct, distillation de données
- **Text-to-SQL** — domaines : ai-eng · alias : text to sql, nl2sql, natural language to sql, texte vers SQL, requête en langage naturel
- **Tokenization** — domaines : ai-eng · alias : tokenisation, découpage en tokens, BPE, byte-pair encoding, subword tokenization
- **Tool use patterns** — domaines : ai-eng · alias : patrons d'appel d'outils, tool use patterns, function calling patterns
- **tool-use** — domaines : ai-eng · alias : function calling, appel d'outils, tool calling, appel de fonctions

#### concept/math
- **Convexity** — domaines : data-sci, ml-eng · alias : Convexité, Convex optimization, Optimisation convexe, fonction convexe, ensemble convexe
- **Cross-entropy** — domaines : data-sci, ml-eng, ai-eng · alias : Entropie croisée, cross entropy, log-loss, log loss, perte d'entropie croisée, negative log-likelihood, NLL
- **Eigendecomposition** — domaines : data-sci, ml-eng · alias : décomposition spectrale, diagonalisation, valeurs propres, vecteurs propres, eigenvalue decomposition, EVD
- **Generalization bounds** — domaines : data-sci, ml-eng · alias : Bornes de généralisation, borne de généralisation, generalization bound, erreur de généralisation, generalization gap
- **Gradient descent** — domaines : data-sci, ml-eng · alias : Descente de gradient, GD, SGD, Stochastic gradient descent, Descente de gradient stochastique, Mini-batch
- **Jensen-Shannon divergence** — domaines : data-sci, ml-eng · alias : Divergence de Jensen-Shannon, Jensen-Shannon, JSD, JS divergence, divergence JS
- **KL divergence** — domaines : data-sci, ml-eng · alias : Divergence de Kullback-Leibler, Kullback-Leibler, KL, relative entropy, entropie relative, divergence KL
- **Learning rate schedules** — domaines : ml-eng, ai-eng · alias : Learning rate schedules, Planification du taux d'apprentissage, LR schedule, Warmup, Cosine decay, Cyclical learning rate
- **Loss landscape and saddle points** — domaines : ml-eng, ai-eng · alias : Loss landscape, Paysage de perte, Saddle points, Points-selles, Surface de perte, Sharp minima
- **Matrix decompositions** — domaines : data-sci, ml-eng · alias : factorisation matricielle, décompositions matricielles, matrix factorization
- **Matrix products** — domaines : data-sci, ml-eng · alias : produit matriciel, multiplication matricielle, matrix multiplication, produit matrice-vecteur
- **Mutual information** — domaines : data-sci, ml-eng · alias : Information mutuelle, MI, mutual info, information mutuelle ponctuelle, PMI
- **Newton & quasi-Newton** — domaines : data-sci, ml-eng · alias : Newton, Méthode de Newton, Newton-Raphson, quasi-Newton, BFGS, L-BFGS, IRLS
- **No Free Lunch theorem** — domaines : data-sci, ml-eng · alias : Théorème No Free Lunch, No Free Lunch, NFL, pas de repas gratuit, théorème du pas de modèle universel
- **Optimal transport** — domaines : data-sci, ml-eng · alias : Transport optimal, OT, Plan de transport, Monge-Kantorovich, Sinkhorn, Earth mover's distance problem
- **Optimisation combinatoire** — domaines : data-sci, ml-eng · alias : Combinatorial optimization, Sac à dos, Knapsack, Problème d'affectation, Assignment problem, Set cover, Couverture d'ensemble, Voyageur de commerce, TSP
- **Optimisation sous contrainte** — domaines : data-sci, ml-eng · alias : Constrained optimization, Lagrangien, Multiplicateurs de Lagrange, Lagrange multipliers, KKT, Karush-Kuhn-Tucker, Conditions KKT, Dualité lagrangienne
- **PAC learning** — domaines : data-sci, ml-eng · alias : Apprentissage PAC, Probably Approximately Correct, PAC, PAC learnability, apprenabilité PAC
- **Programmation linéaire en nombres entiers (MIP)** — domaines : data-sci, ml-eng · alias : MIP, MILP, Mixed-Integer Programming, ILP, Integer programming, Programmation linéaire, LP, Linear programming, Branch and bound, Relaxation LP
- **Projections** — domaines : data-sci, ml-eng · alias : projection orthogonale, projecteur, projection
- **Rademacher complexity** — domaines : data-sci, ml-eng · alias : Complexité de Rademacher, Rademacher, complexité de Rademacher empirique, Rademacher averages
- **Shannon entropy** — domaines : data-sci, ml-eng · alias : Entropie de Shannon, entropie, information entropy, entropy, entropie de l'information
- **SVD** — domaines : data-sci, ml-eng · alias : décomposition en valeurs singulières, singular value decomposition, valeurs singulières
- **VC dimension** — domaines : data-sci, ml-eng · alias : Dimension VC, Vapnik-Chervonenkis dimension, dimension de Vapnik-Chervonenkis, VC dim, shattering
- **Vector norms** — domaines : data-sci, ml-eng · alias : normes vectorielles, normes, Lp norms, norme Lp
- **Wasserstein distance** — domaines : data-sci, ml-eng · alias : Distance de Wasserstein, Wasserstein, earth mover's distance, EMD, distance du transport optimal

#### concept/ml
- **AdaBoost** — domaines : data-sci, ml-eng · alias : Adaptive Boosting, Boosting adaptatif, AdaBoostClassifier, SAMME
- **Analyse discriminante** — domaines : data-sci, ml-eng · alias : LDA, QDA, Linear Discriminant Analysis, Quadratic Discriminant Analysis, Analyse discriminante linéaire, Analyse factorielle discriminante, AFD, LinearDiscriminantAnalysis
- **Apprentissage non supervisé** — domaines : data-sci · alias : Unsupervised learning, Apprentissage non supervise, Méthodes non supervisées
- **Apprentissage supervisé** — domaines : data-sci, ml-eng · alias : Supervised learning, Apprentissage supervise, Modélisation supervisée
- **Arbres de décision** — domaines : data-sci, ml-eng · alias : Decision tree, Arbre de décision, CART
- **Bagging** — domaines : data-sci, ml-eng · alias : Bootstrap aggregating, Ensachage
- **Boosting** — domaines : data-sci, ml-eng · alias : Boostage
- **Calibration** — domaines : data-sci, ml-eng · alias : Calibration des probabilités, fiabilité, diagramme de fiabilité, reliability diagram, Platt scaling, régression isotonique, temperature scaling, ECE, Expected Calibration Error
- **Classification** — domaines : data-sci, ml-eng · alias : Classification supervisée, Classifieur, Classifier, Classement
- **Classification hiérarchique (CAH)** — domaines : data-sci · alias : CAH, Classification ascendante hiérarchique, Hierarchical clustering, HAC, Agglomerative clustering, Dendrogramme
- **Classification metrics** — domaines : data-sci, ml-eng · alias : Métriques de classification, exactitude, accuracy, précision, rappel, F1, F1-score, log-loss, matrice de confusion, sensibilité, spécificité, MCC, Brier
- **Clustering** — domaines : data-sci · alias : Partitionnement, Partitionnement non supervisé, Cluster analysis, Analyse de clusters, Regroupement
- **Clustering evaluation** — domaines : data-sci · alias : Évaluation du clustering, évaluation de clustering, silhouette, indice de silhouette, ARI, Adjusted Rand Index, NMI, AMI, Davies-Bouldin, Calinski-Harabasz, DBCV
- **Compromis biais-variance** — domaines : data-sci, ml-eng · alias : Bias-variance tradeoff, Biais-variance, Sous-apprentissage, Surapprentissage, Underfitting, Overfitting
- **Data drift** — domaines : mlops, data-sci · alias : dérive de données, distribution shift, drift, dérive de distribution
- **Data leakage** — domaines : data-sci, ml-eng · alias : fuite de données, fuite d'information, target leakage
- **DBSCAN** — domaines : data-sci · alias : Density-Based Spatial Clustering, Density-Based Spatial Clustering of Applications with Noise
- **Déploiement de modèles** — domaines : mlops · alias : model deployment, déploiement de modèle, canary, blue-green, shadow deployment, progressive delivery, déploiement progressif, rollout
- **Détection d'outliers multivariée** — domaines : data-sci, ml-eng · alias : outliers multivarié, LOF, Isolation Forest, Elliptic Envelope, ECOD, COPOD, Mahalanobis
- **Détection d'outliers univariée** — domaines : data-sci, ml-eng · alias : outliers univarié, Z-score, IQR, MAD, règle de Tukey, modified Z-score
- **EDA automatisée & profiling** — domaines : data-sci, data-eng · alias : EDA, analyse exploratoire, exploratory data analysis, data profiling, profiling de données
- **embeddings** — domaines : data-sci, ai-eng · alias : représentations vectorielles, plongements, embedding, vector embeddings
- **Encodage des variables catégorielles** — domaines : data-sci · alias : Encodage catégoriel, Categorical encoding, One-Hot encoding, Target encoding, Weight of Evidence, WoE
- **Ensembling** — domaines : data-sci, ml-eng · alias : méthodes d'ensemble, ensemble learning, ensemble de modèles, agrégation de modèles
- **Explicabilité des modèles** — domaines : data-sci, ml-eng · alias : explicabilité, interprétabilité, explainability, interpretability, feature importance, SHAP, LIME, permutation importance
- **Extra Trees** — domaines : data-sci, ml-eng · alias : ExtraTrees, Extremely Randomized Trees, Arbres extrêmement aléatoires, ExtraTreesClassifier, Extra-Trees
- **Feature store — concept** — domaines : mlops, data-eng · alias : feature store, magasin de features, online store, offline store, point-in-time correctness, train/serve skew
- **GAM** — domaines : data-sci, ml-eng · alias : Modèles additifs généralisés, Generalized Additive Model, Modèle additif généralisé
- **Gaussian Mixture Models (GMM)** — domaines : data-sci · alias : GMM, Mélange de gaussiennes, Modèle de mélange gaussien, Mixture models, Mélanges gaussiens
- **Gaussian Process** — domaines : data-sci, ml-eng · alias : GP, Processus gaussien, Régression par processus gaussien, GaussianProcessRegressor, Krigeage, Kriging
- **GLM** — domaines : data-sci, ml-eng · alias : Modèles linéaires généralisés, Generalized Linear Model, Modèle linéaire généralisé
- **Gradient Boosting (GBDT)** — domaines : data-sci, ml-eng · alias : GBDT, Gradient boosting, Gradient boosted trees, Boosting de gradient, GBM
- **HDBSCAN** — domaines : data-sci · alias : Hierarchical DBSCAN, Hierarchical Density-Based Spatial Clustering
- **Imbalanced classification** — domaines : data-sci, ml-eng · alias : classes déséquilibrées, déséquilibre de classes, class imbalance
- **Imputation des valeurs manquantes** — domaines : data-sci · alias : Imputation, Missing value imputation, Gestion des valeurs manquantes, MICE, KNN imputer
- **Ingénierie des caractéristiques** — domaines : data-sci, ml-eng · alias : Feature engineering, Ingénierie des variables, Feature preprocessing
- **Isolation Forest** — domaines : data-sci, ml-eng · alias : iForest, Forêt d'isolement, IsolationForest
- **K-Means** — domaines : data-sci · alias : K-means, kmeans, K-moyennes, Lloyd, k-means++
- **k-médoïds (PAM)** — domaines : data-sci · alias : k-medoids, PAM, Partitioning Around Medoids, k-médoïdes, CLARA
- **k-NN** — domaines : data-sci, ml-eng · alias : KNN, k plus proches voisins, k-Nearest Neighbors, Plus proches voisins, KNeighborsClassifier, Apprentissage paresseux, Lazy learning
- **Local Outlier Factor** — domaines : data-sci, ml-eng · alias : LOF, Facteur d'aberration locale, LocalOutlierFactor, Densité locale
- **Mise à l'échelle** — domaines : data-sci · alias : Normalisation, Standardisation, Feature scaling, Scaling, StandardScaler, MinMaxScaler, RobustScaler
- **Model registry & versioning** — domaines : mlops · alias : model registry, registre de modèles, model versioning, versioning de modèles, lignage de modèle, model lineage, champion-challenger
- **Monitoring de modèle en production** — domaines : mlops · alias : model monitoring, monitoring ML, surveillance de modèle, observabilité ML, ML monitoring
- **Mécanismes de données manquantes** — domaines : data-sci · alias : MCAR, MAR, MNAR, missingness, mécanisme du manque, données manquantes, missing data mechanism, Rubin
- **Naive Bayes** — domaines : data-sci, ml-eng · alias : Bayésien naïf, Classifieur bayésien naïf, GaussianNB, MultinomialNB, BernoulliNB, ComplementNB
- **One-Class SVM** — domaines : data-sci, ml-eng · alias : OCSVM, SVM à une classe, OneClassSVM, SGDOneClassSVM, Novelty detection
- **Optimisation d'hyperparamètres** — domaines : data-sci, ml-eng · alias : Hyperparameter tuning, GridSearch, RandomSearch, Optimisation bayésienne, HPO, Réglage des hyperparamètres
- **Perceptron et MLP** — domaines : data-sci, ml-eng · alias : Perceptron, MLP, Multi-Layer Perceptron, Perceptron multicouche, Réseau de neurones, Feedforward network, MLPClassifier
- **Random Forest** — domaines : data-sci, ml-eng · alias : RF, Forêts aléatoires, Random forests, Forêt aléatoire
- **Ranking metrics** — domaines : data-sci, ml-eng · alias : Métriques de ranking, métriques d'ordonnancement, NDCG, DCG, MAP, MRR, Precision@k, Recall@k, Hit Rate, learning-to-rank, métriques de recherche d'information
- **Regression metrics** — domaines : data-sci, ml-eng · alias : Métriques de régression, MSE, RMSE, MAE, R2, R², R² ajusté, coefficient de détermination, erreur quadratique moyenne, Huber, régression quantile
- **ROC-AUC / courbe PR** — domaines : data-sci, ml-eng · alias : ROC, AUC, courbe ROC, courbe PR, precision-recall, AUC-ROC, AUC-PR, ROC-AUC
- **Régression** — domaines : data-sci, ml-eng · alias : Regression, Régression supervisée, Modélisation de cible continue
- **Régression et classification multi-sorties** — domaines : data-sci · alias : multi-output, multioutput, multi-sorties, multi-target, multi-label, MultiOutputRegressor, MultiOutputClassifier, RegressorChain, ClassifierChain
- **Régression linéaire** — domaines : data-sci, ml-eng · alias : Linear regression, OLS, Moindres carrés ordinaires
- **Régression logistique** — domaines : data-sci, ml-eng · alias : Logistic regression, Régression logit
- **Régression quantile** — domaines : data-sci, ml-eng · alias : Quantile regression, QuantileRegressor, Perte pinball, Pinball loss, Régression médiane, Intervalles de prédiction
- **Régularisation** — domaines : data-sci, ml-eng · alias : Ridge, Lasso, ElasticNet, Pénalisation L1/L2, Regularization
- **SVM** — domaines : data-sci, ml-eng · alias : Support Vector Machine, Machine à vecteurs de support, Séparateur à vaste marge, SVC, SVR, Astuce du noyau, Kernel trick
- **Systèmes de recommandation** — domaines : data-sci, ml-eng · alias : recommender systems, recsys, filtrage collaboratif, collaborative filtering, factorisation matricielle, matrix factorization, two-tower
- **Sélection de variables** — domaines : data-sci, ml-eng · alias : Feature selection, Sélection de caractéristiques, Sélection d'attributs, RFE, SelectKBest
- **t-SNE and UMAP** — domaines : data-sci · alias : t-SNE, UMAP, visualisation haute dimension
- **Types de données et choix de modèle** — domaines : data-sci, ml-eng · alias : Choix de modèle, Model selection, Quel modèle choisir, Aiguillage modèle, Cheat sheet modèles, Types de variables
- **Validation croisée** — domaines : data-sci, ml-eng · alias : Cross-validation, K-Fold, Validation croisée stratifiée, TimeSeriesSplit, CV

#### concept/nlp
- **BM25** — domaines : ai-eng, data-sci · alias : Okapi BM25, best matching 25, bm25
- **Classification de texte** — domaines : data-sci, ml-eng · alias : text classification, classification de documents, catégorisation de texte, analyse de sentiment
- **Fuzzy matching & similarité de chaînes** — domaines : data-eng, data-sci · alias : fuzzy matching, similarité de chaînes, string matching, approximate string matching, distance d'édition, Levenshtein, Jaro-Winkler, record linkage, déduplication
- **NER et étiquetage de séquence** — domaines : data-sci, ml-eng · alias : NER, named entity recognition, reconnaissance d'entités nommées, étiquetage de séquence, sequence labeling, token classification, BiLSTM-CRF
- **Recherche d'information** — domaines : ai-eng, data-sci · alias : information retrieval, IR, recherche documentaire, retrieval lexical dense hybride
- **TF-IDF** — domaines : data-sci, ai-eng · alias : tf-idf, term frequency-inverse document frequency, pondération tf-idf
- **Traitement du langage naturel** — domaines : data-sci, ml-eng, ai-eng · alias : NLP, natural language processing, TALN, TAL, traitement automatique du langage

#### concept/rl
- **Actor-Critic methods** — domaines : ml-eng · alias : actor-critic, acteur-critique, méthodes acteur-critique, A2C, A3C, advantage actor-critic
- **AlphaZero and self-play** — domaines : ml-eng, ai-eng · alias : AlphaZero, self-play, jeu contre soi-même, AlphaGo Zero, MuZero, apprentissage par self-play
- **Bellman equations** — domaines : ml-eng · alias : équations de Bellman, équation de Bellman, Bellman equation, Bellman optimality, optimalité de Bellman, Bellman backup
- **Counterfactual Regret Minimization** — domaines : ml-eng, ai-eng · alias : CFR, counterfactual regret minimization, minimisation du regret contrefactuel, CFR+, regret matching, Deep CFR, MCCFR
- **Exploration vs exploitation** — domaines : ml-eng, ai-eng · alias : exploration vs exploitation, exploration-exploitation, dilemme exploration-exploitation, exploration/exploitation, explore-exploit
- **Imitation learning** — domaines : ml-eng, ai-eng · alias : imitation learning, apprentissage par imitation, behavioral cloning, BC, learning from demonstration, inverse RL, IRL, GAIL
- **Markov Decision Process** — domaines : ml-eng · alias : MDP, processus de décision markovien, processus décisionnel de Markov, Markov decision process
- **Model-based RL** — domaines : ml-eng · alias : model-based RL, RL basé modèle, model-based reinforcement learning, RL avec modèle, world models, planification
- **Monte Carlo Tree Search** — domaines : ml-eng, ai-eng · alias : MCTS, Monte Carlo Tree Search, recherche arborescente Monte-Carlo, UCT, UCB applied to trees
- **Offline RL** — domaines : ml-eng · alias : offline RL, RL hors ligne, batch RL, offline reinforcement learning, RL hors interaction, batch reinforcement learning
- **Policy gradient** — domaines : ml-eng, ai-eng · alias : policy gradient, gradient de politique, méthodes basées politique, policy-based methods, REINFORCE, policy optimization
- **PPO** — domaines : ml-eng, ai-eng · alias : PPO, Proximal Policy Optimization, optimisation proximale de politique, clipped surrogate
- **Q-learning and DQN** — domaines : ml-eng · alias : Q-learning, DQN, Deep Q-Network, deep Q-learning, Q-apprentissage, apprentissage par Q
- **Reinforcement learning** — domaines : ml-eng, ai-eng · alias : RL, apprentissage par renforcement, reinforcement learning, agent-environnement
- **Reward shaping and hacking** — domaines : ml-eng, ai-eng · alias : reward shaping, reward hacking, façonnage de récompense, détournement de récompense, specification gaming, reward design, potential-based shaping
- **Théorie des jeux** — domaines : ml-eng, ai-eng · alias : game theory, théorie des jeux, équilibre de Nash, Nash equilibrium, jeu à somme nulle, zero-sum, information imparfaite, minimax
- **Value functions** — domaines : ml-eng · alias : fonctions de valeur, fonction de valeur, value function, V-function, Q-function, fonction Q, fonction de valeur d'état-action

#### concept/signal
- **Filtrage numérique** — domaines : data-sci, ml-eng · alias : filtre numérique, Butterworth, fenêtrage, apodisation, FIR, IIR, transformée de Hilbert, digital filter
- **Ondelettes** — domaines : data-sci, ml-eng · alias : wavelets, DWT, CWT, transformée en ondelettes, multirésolution, scalogramme
- **STFT et spectrogramme** — domaines : data-sci, ml-eng · alias : STFT, spectrogramme, short-time Fourier transform, mel-spectrogramme, MFCC, mel spectrogram
- **Traitement du signal** — domaines : data-sci, ml-eng · alias : TdS, signal processing, DSP, traitement numérique du signal
- **Transformée de Fourier** — domaines : data-sci, ml-eng · alias : FFT, DFT, transformée de Fourier discrète, transformée de Fourier rapide, analyse spectrale, domaine fréquentiel

#### concept/stats
- **A priori conjugués** — domaines : data-sci · alias : conjugate priors, conjugate prior, lois a priori conjuguées, prior conjugué, conjugaison
- **A/B testing** — domaines : data-sci · alias : AB testing, test A/B, split testing, online controlled experiment, OCE, randomized experiment
- **Analyse de puissance** — domaines : data-sci · alias : power analysis, statistical power, taille d'échantillon
- **Analyse de survie** — domaines : data-sci · alias : survival analysis, time-to-event, analyse de survie, Kaplan-Meier, Cox, risques proportionnels, hazard, censure
- **Bootstrap** — domaines : data-sci · alias : resampling, rééchantillonnage
- **CA** — domaines : data-sci · alias : AFC, Analyse des correspondances, Analyse factorielle des correspondances, Correspondence Analysis
- **Chaînes de Markov** — domaines : data-sci · alias : Markov chains, propriété de Markov, Markov property
- **Correction des tests multiples** — domaines : data-sci · alias : multiple testing, multiple comparisons, Bonferroni, FDR
- **CUPED** — domaines : data-sci · alias : Controlled-experiment Using Pre-Experiment Data, variance reduction, regression adjustment
- **Diff-in-Diff** — domaines : data-sci · alias : DiD, difference-in-differences, différence des différences, doubles différences
- **Estimation MAP** — domaines : data-sci · alias : MAP, maximum a posteriori, maximum a posteriori estimation, estimation maximum a posteriori
- **FAMD** — domaines : data-sci · alias : AFDM, Analyse factorielle de données mixtes, Factor Analysis of Mixed Data
- **GPA** — domaines : data-sci · alias : Generalized Procrustes Analysis, Analyse procustéenne généralisée, Procruste généralisé
- **HCPC** — domaines : data-sci · alias : Classification hiérarchique sur composantes principales, Hierarchical Clustering on Principal Components
- **Inférence bayésienne** — domaines : data-sci · alias : Bayesian inference, inference bayesienne, Bayes, statistique bayésienne
- **Inférence causale** — domaines : data-sci · alias : causal inference, inférence causale, causalité, DAG, confounding, confondeur, backdoor, propensity score, score de propension
- **Intervalles de confiance** — domaines : data-sci · alias : confidence interval, confidence intervals, IC
- **Inégalités de concentration** — domaines : data-sci · alias : Concentration inequalities, Hoeffding, Chebyshev, inégalité de Markov
- **Loi des grands nombres** — domaines : data-sci · alias : Law of large numbers, LGN, LLN
- **Manifold learning** — domaines : data-sci · alias : manifold learning, apprentissage de variété, Isomap, LLE, Locally Linear Embedding, Kernel PCA, Laplacian Eigenmaps, spectral embedding
- **MANOVA et tests multivariés** — domaines : data-sci · alias : MANOVA, tests multivariés, multivariate analysis of variance, Hotelling, Hotelling T2, Wilks lambda, trace de Pillai
- **Maximum de vraisemblance** — domaines : data-sci · alias : MLE, maximum likelihood estimation, maximum likelihood, vraisemblance maximale
- **MCA** — domaines : data-sci · alias : ACM, Analyse des correspondances multiples, Multiple Correspondence Analysis
- **MCMC** — domaines : data-sci · alias : Markov chain Monte Carlo, Monte-Carlo par chaînes de Markov, Metropolis-Hastings, NUTS, Gibbs
- **MFA** — domaines : data-sci · alias : AFM, Analyse factorielle multiple, Multiple Factor Analysis
- **Mouvement brownien** — domaines : data-sci · alias : Brownian motion, processus de Wiener, Wiener process
- **Multi-armed bandits** — domaines : data-sci · alias : MAB, bandit manchot, bandits, Epsilon-Greedy, Thompson Sampling, exploration-exploitation
- **PCA** — domaines : data-sci · alias : ACP, Analyse en composantes principales, Principal Component Analysis
- **PGA** — domaines : data-sci · alias : Principal Geodesic Analysis, Analyse géodésique principale
- **Processus de Poisson** — domaines : data-sci · alias : Poisson process, processus ponctuel de Poisson
- **Réduction de dimension** — domaines : data-sci · alias : dimensionality reduction, réduction de dimensionnalité
- **Sequential testing** — domaines : data-sci · alias : test séquentiel, analyse séquentielle, peeking, always-valid inference, SPRT, alpha spending
- **Test du khi-deux** — domaines : data-sci · alias : chi-squared, chi-square, khi2, test d'indépendance
- **Test t et ANOVA** — domaines : data-sci · alias : t-test, ANOVA, test de Student, comparaison de moyennes
- **Tests d'hypothèse** — domaines : data-sci · alias : hypothesis testing, test statistique, H0, significativité
- **Tests non paramétriques** — domaines : data-sci · alias : non-parametric, non-parametric tests, Wilcoxon, Mann-Whitney, Kruskal-Wallis
- **Théorème central limite** — domaines : data-sci · alias : Central limit theorem, CLT, TCL

#### concept/ts
- **ARIMA SARIMA** — domaines : data-sci, ml-eng · alias : ARIMA, SARIMA, ARMA, Box-Jenkins, AutoARIMA
- **Autocorrelation** — domaines : data-sci · alias : Autocorrélation, ACF, PACF, Fonction d'autocorrélation, Corrélogramme
- **Exponential smoothing** — domaines : data-sci, ml-eng · alias : Lissage exponentiel, ETS, Holt-Winters, SES, Holt, AutoETS
- **Forecasting framing** — domaines : data-sci, ml-eng · alias : Cadrage forecasting, Cadrage d'une prévision, Forecasting problem framing
- **Forecasting metrics** — domaines : data-sci, ml-eng · alias : Métriques de prévision, MAPE, sMAPE, MASE, WAPE, RMSSE, pinball loss, forecast accuracy
- **Foundation models pour séries temporelles** — domaines : data-sci, ml-eng · alias : Time series foundation models, TSFM, Modèles de fondation séries temporelles, Foundation models time series, Zero-shot forecasting
- **Hierarchical forecasting** — domaines : data-sci, ml-eng · alias : Prévision hiérarchique, Réconciliation, Hierarchical reconciliation, MinT, bottom-up, top-down
- **Intermittent demand** — domaines : data-sci, ml-eng · alias : Demande intermittente, Croston, SBA, TSB, demande sporadique, slow movers
- **Maintenance prédictive et RUL** — domaines : data-sci, mlops · alias : Maintenance prédictive / RUL, Maintenance prédictive, RUL, Remaining useful life, Durée de vie résiduelle, Pronostic, Predictive maintenance, PdM
- **Stationarity** — domaines : data-sci · alias : Stationnarité, Série stationnaire, Stationnaire, Racine unitaire
- **Time series anomaly detection** — domaines : data-sci, mlops · alias : Détection d'anomalies temporelles, Outliers temporels, Time series anomaly, anomaly detection, matrix profile, discord
- **Time series feature engineering** — domaines : data-sci, ml-eng · alias : Features temporelles, Lag features, Rolling features, Fourier terms, Time series features
- **Walk-forward CV** — domaines : data-sci, ml-eng · alias : Validation glissante, Backtesting, Rolling origin, Expanding window, Time series cross-validation, cutoff, cutoffs

### outil

#### skill/knowledge
- **Obsidian** — Base de connaissances personnelle (propriétaire, gratuit en usage perso) : notes markdown locales, liens bidirectionnels et vue en graphe, extensible par plugins ; le socle de ce DevBrain.
