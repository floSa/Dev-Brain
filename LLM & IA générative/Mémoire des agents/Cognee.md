---
role: brique
nom: Cognee
alias: [cognee, topoteretes]
pitch: "Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta."
categorie: llm/memoire
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Mem0]]", "[[Graphiti]]", "[[Letta]]", "[[OpenViking]]"]
complements: ["[[Neo4j]]", "[[pgvector]]", "[[LanceDB]]", "[[Ollama]]", "[[Docling]]", "[[LangGraph]]"]
tags: [agent-memory, knowledge-graph, rag, agents, local-llm]
url_docs: https://docs.cognee.ai/
url_repo: https://github.com/topoteretes/cognee
---

# Cognee

<!-- AUTO:BANDEAU:START -->
> Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de **mémoire et de connaissance** pour agents. Depuis la v1.0, l'interface tient en
quatre verbes — `remember`, `recall`, `improve`, `forget` — qui regroupent les anciennes
`add`, `cognify`, `memify` et `search`, toujours supportées. `cognify` enchaîne huit étapes
et construit un **graphe** par extraction LLM, ou par GLiNER en local sans LLM, plus des
résumés, de la provenance et une détection de contradictions, ces deux dernières en option.
`recall` propose de nombreux modes (complétion hybride par défaut, par graphe, par
passages, temporelle, Cypher en opt-in…). Le code est sous **Apache-2.0** ; la société
éditrice, Topoteretes, vend en plus Cognee Cloud, une offre Enterprise en BYOC et un
**adaptateur Postgres de production sous licence commerciale**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| La mémoire de l'agent et la **connaissance documentaire** (PDF, fichiers, conversations) doivent vivre dans un seul moteur | Seuls des faits de conversation par utilisateur sont à retenir : plus simple avec [[Mem0]] |
| Plusieurs utilisateurs ou clients : `ENABLE_BACKEND_ACCESS_CONTROL` est actif par défaut, avec authentification, tenants, rôles et permissions read, write, delete, share **par jeu de données** | Un graphe de **production** est requis : Kuzu, le défaut, est jugé « non recommandé en production » par la doc (un seul écrivain, une seule machine, ni réplication ni bascule) ; Neo4j Enterprise ou Aura est recommandé en multi-utilisateur |
| Une pile entièrement locale et **sans clé** est visée : sans clé API, la configuration bascule sur GLiNER et FastEmbed ; Ollama, LM Studio, llama.cpp et un point d'accès vLLM sont documentés | Les modèles locaux sont petits : la doc classe `mistral`, `phi3` et `qwen2.5` sous 14 B comme problématiques pour l'extraction de graphe |
| L'ingestion de documents doit passer par un parseur choisi : [[Docling]] est documenté comme loader (extra `cognee[docling]`) | La **dimension temporelle** est le cœur du besoin → [[Graphiti]] |

## Mise en œuvre

- Installation — `pip install cognee` (extras par backend, dont `docling`) ; constat du 2026-10-01 : v1.6.2 du 2026-09-29 (PyPI), environ 31,3 k étoiles, Python 3.10 à 3.14, classifieur PyPI « 4 - Beta », environ une version par semaine
- Point d'entrée — `remember` / `recall` / `improve` / `forget` en Python ; API REST FastAPI (port 8000, Docker, Compose, Helm documentés) ; serveur MCP en mode autonome ou partagé, un jeton par utilisateur
- Prérequis — trois stockages : relationnel (SQLite par défaut, Postgres, Turso), vecteur (LanceDB par défaut, PGVector, Chroma, Neptune Analytics) et graphe (Kuzu par défaut, Neo4j, Neptune). Qdrant, FalkorDB, Memgraph et Redis sont des adaptateurs communautaires. Une isolation par jeu de données exige un *handler* par backend (Kuzu, LanceDB, PGVector, FalkorDB, Neo4j, Qdrant ; pas Neptune). Le README de Graphiti déclare par ailleurs que l'amont de Kuzu n'est plus maintenu
- Exécution — bibliothèque embarquée, ou serveur ; hors défaut, les bases sont à héberger. `llama.cpp` en processus sérialise les appels, et Ollama exige un `num_ctx` suffisant (sinon erreurs HTTP 500). Télémétrie active par défaut : `TELEMETRY_DISABLED=true` ; pour un serveur, la doc recommande aussi `ACCEPT_LOCAL_FILE_PATH=False` et `ALLOW_CYPHER_QUERY=False`
- Coût — gratuit sous Apache-2.0 : usage chez un client, embarquement et service hébergé permis, sans copyleft, marque exclue. Réserves : l'adaptateur Postgres de production est un produit à licence ; la page tarifs réserve à l'offre Enterprise la mémoire bi-temporelle et la provenance, que la documentation décrit pourtant pour l'open source — écart non tranché, à vérifier avant de s'y engager. **CVE-2026-31231** (exécution de code à distance par le point d'accès des notebooks, sévérité critique 9.8) : versions 0.3.0 à 1.1.3, corrigée en **1.2.0**

## Écosystème

### Alternatives

- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[Graphiti]] — Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.
- [[Letta]] — Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

### Compléments

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.

## Ressources

- Documentation — https://docs.cognee.ai/
- Documentation — bases de graphes supportées : https://docs.cognee.ai/setup-configuration/graph-stores.md
- Documentation — modèles locaux avec Ollama : https://docs.cognee.ai/guides/local-ollama.md
- Article — avis de sécurité GHSA-8pr4-p4c8-8gr9 : https://github.com/topoteretes/cognee/security/advisories/GHSA-8pr4-p4c8-8gr9
- Dépôt — https://github.com/topoteretes/cognee

## Voir aussi

- [[Agent memory]] — la notion ; Cognee mêle mémoire d'agent et graphe de connaissances documentaire
- [[Comparatif - Mémoire pour agents]] — le départage des outils de mémoire du dossier
- [[Mémoire des agents]] — le hub du dossier
- [[Construction de graphes de connaissances]] — la notion de la construction de graphe, que `cognify` automatise
