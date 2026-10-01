---
role: brique
nom: Mem0
alias: [mem0, mem0ai]
pitch: "Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée."
categorie: llm/memoire
famille: paquet
licence_type: open-core
maturite: production
langage: Python
alternatives: ["[[Letta]]", "[[Graphiti]]", "[[Cognee]]", "[[OpenViking]]"]
complements: ["[[Qdrant]]", "[[pgvector]]", "[[Ollama]]", "[[LangGraph]]", "[[CrewAI]]"]
tags: [agent-memory, agents, retrieval, local-llm]
url_docs: https://docs.mem0.ai/
url_repo: https://github.com/mem0ai/mem0
---

# Mem0

<!-- AUTO:BANDEAU:START -->
> Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-core | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche de **mémoire pour agents** qui se branche sur une application existante : à chaque
`add`, un appel LLM extrait les faits à retenir (préférences, décisions, contexte), qui sont
stockés dans un vector store et rattachés à un `user_id`, un `agent_id` ou un `run_id`. Un
`search` les retrouve en combinant trois signaux — sémantique, BM25 et entités. Depuis le
nouvel algorithme de la v3, l'extraction est un seul appel, **en ajout seulement** : plus de
logique UPDATE ou DELETE à la volée. Le dépôt est sous **Apache-2.0**, mais l'édition open
source n'est pas la plateforme : la **mémoire graphe** a été **retirée de l'open source**, et
webhooks, export, opérations par lots, catégories personnalisées et oubli progressif ne
sont documentés que côté Mem0 Platform : une partie des fonctions se trouve dans l'offre hébergée, pas dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un assistant ou un agent de support doit retenir les préférences et faits **d'un utilisateur** d'une session à l'autre, avec quelques lignes (`add`, `search`) | Les faits **changent dans le temps** et il faut les interroger à une date donnée : la mémoire graphe n'existe plus en open source → [[Graphiti]] |
| Le choix du stockage compte : Qdrant par défaut, pgvector, Milvus, Weaviate, Chroma, FAISS, Redis, OpenSearch… sont documentés | L'agent doit **éditer lui-même** sa mémoire dans sa boucle, hiérarchie comprise → [[Letta]] |
| Un LLM et un embedder locaux sont requis : Ollama, LM Studio, vLLM et Hugging Face / FastEmbed sont documentés | Le **serveur MCP officiel** est nécessaire : il est hébergé par Mem0 et exige une clé de la plateforme — inutilisable sans cloud |
| Plusieurs agents partagent la mémoire derrière une API : le serveur `server/` fournit REST, tableau de bord, clés par utilisateur | Corpus de **documents** à indexer et interroger plutôt que des faits de conversation → [[Cognee]] ou un pipeline RAG |
| | Aucun envoi vers un tiers n'est toléré : la télémétrie est **active par défaut** (PostHog) |

## Mise en œuvre

- Installation — `pip install mem0ai` (extras `[nlp]` et modèle spaCy pour la recherche par entités) ; constat du 2026-10-01 : v2.2.1 du 2026-09-25 (PyPI), SDK TypeScript 3.3.1, 66,4 k étoiles, plusieurs versions par semaine (2.1.0 le 18/09, 2.2.0 le 23/09)
- Point d'entrée — `Memory.from_config(...)` avec `add`, `search`, `get_all`, `update`, `delete`, `history` ; depuis la v3, les identifiants d'entité passent dans `filters={...}`, sinon `ValueError`. Alternative : le serveur autonome `server/` (FastAPI sur le port 8888, tableau de bord Next.js, Postgres avec pgvector, Docker Compose, authentification activée par défaut)
- Prérequis — un LLM et un embedder : le défaut documenté est OpenAI, à remplacer pour rester on-prem, en alignant `embedding_dims` sur le store ; un vector store (Qdrant local par défaut). La doc ne mesure pas la qualité d'extraction avec de petits modèles locaux ; le serveur MCP officiel est hébergé, pas local
- Exécution — en bibliothèque (rien à héberger) ou en serveur Docker ; historique en SQLite (`~/.mem0/history.db`) ; mise à l'échelle, haute disponibilité, TLS, sauvegardes et cloisonnement par client sont à la charge de l'opérateur, sans SLA ; `MEM0_TELEMETRY=False` pour couper la télémétrie, et filtrer la sortie réseau
- Coût — gratuit sous Apache-2.0 : usage chez un client, embarquement et service hébergé permis, sous réserve de conserver l'avis de licence ; la marque et les conditions de la plateforme ne sont pas couvertes. Le coût réel est celui des appels LLM d'extraction, à chaque `add`. Les scores LoCoMo et LongMemEval du README sont annoncés par l'éditeur, non repris ici

## Écosystème

### Alternatives

- [[Letta]] — Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte.
- [[Graphiti]] — Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

### Compléments

- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.

## Ressources

- Documentation — https://docs.mem0.ai/
- Documentation — édition open source contre plateforme : https://docs.mem0.ai/platform/platform-vs-oss
- Documentation — migration v2 vers v3, graphe retiré et filtres obligatoires : https://docs.mem0.ai/migration/oss-v2-to-v3
- Dépôt — https://github.com/mem0ai/mem0

## Voir aussi

- [[Agent memory]] — la notion dont il est une implémentation par faits extraits
- [[Comparatif - Mémoire pour agents]] — le départage des outils de mémoire du dossier
- [[Mémoire des agents]] — le hub du dossier
