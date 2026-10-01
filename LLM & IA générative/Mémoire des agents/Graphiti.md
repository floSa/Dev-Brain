---
role: brique
nom: Graphiti
alias: [graphiti, graphiti-core, zep graphiti]
pitch: "Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud."
categorie: llm/memoire
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Mem0]]", "[[Cognee]]", "[[Letta]]"]
complements: ["[[Neo4j]]", "[[Ollama]]", "[[vLLM]]"]
tags: [agent-memory, knowledge-graph, agents, retrieval, local-llm]
url_docs: https://help.getzep.com/graphiti/getting-started/overview
url_repo: https://github.com/getzep/graphiti
---

# Graphiti

<!-- AUTO:BANDEAU:START -->
> Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de **graphe de connaissances temporel** pour la mémoire d'agents, publié par Zep. Les
données entrent par **épisodes** (message, texte, JSON) ; un LLM en tire des entités et des
**faits** (arêtes) dont chacun porte une fenêtre de validité, `valid_at` et `invalid_at`. Un
fait contredit par un épisode ultérieur est **invalidé**, pas supprimé : le graphe sait ce
qui était vrai à telle date et d'où vient chaque fait. La recherche combine vecteur, BM25 et
parcours de graphe. L'architecture est décrite dans Rasmussen et al., *Zep: A Temporal
Knowledge Graph Architecture for Agent Memory* (arXiv 2501.13956, 2025) ; les scores de ce
papier sont annoncés par l'éditeur, datent de janvier 2025 et ne sont pas repris ici.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les faits **évoluent** — statut d'un équipement, titulaire d'un rôle, version d'un contrat — et la question porte sur « à telle date » ou sur « ce qui a changé » | Il s'agit de retenir des préférences d'utilisateur, sans relations ni historique → [[Mem0]], plus léger |
| La **provenance** compte : chaque fait renvoie à l'épisode qui l'a produit | Aucun LLM capable de **sortie structurée** n'est disponible : la doc déconseille les petits modèles, qui produisent un JSON incorrect |
| Un graphe Neo4j existe déjà, ou une base de graphes est acceptable à l'exploitation | Le coût d'ingestion est une contrainte : chaque épisode déclenche **plusieurs appels LLM** (extraction, dédoublonnage, arêtes, résumés), dont le nombre n'est pas documenté |
| Le besoin est un moteur à intégrer, pas une plateforme | Une **plateforme clé en main** on-prem est attendue : API multi-utilisateur, authentification, administration — la Community Edition de Zep est arrêtée (annonce du 2025-04-02) et Zep Cloud n'est pas auto-hébergeable |

## Mise en œuvre

- Installation — `pip install graphiti-core` (extras `falkordb`, `falkordblite`, `neptune`, `kuzu`, `sentence-transformers`) ; constat du 2026-10-01 : v0.30.2 du 2026-09-08 (PyPI), environ 31,3 k étoiles, Python 3.10 ou plus ; serveur MCP versionné à part (mcp-v1.1.0)
- Point d'entrée — classe `Graphiti` avec `add_episode` et `search` ; serveur MCP (`mcp_server/`, transport stdio ou HTTP, FalkorDB par défaut, aucune authentification documentée) et dossier `server/` pour une API REST FastAPI
- Prérequis — une base de graphes : Neo4j 5.26 ou plus (défaut), FalkorDB 1.1.2 ou plus, FalkorDBLite (embarqué, Python 3.12 ou plus), Amazon Neptune avec OpenSearch ; Kuzu est **déprécié** (amont non maintenu, retrait annoncé). LLM, embedder et reranker valent OpenAI par défaut : pour sortir du cloud, `OpenAIGenericClient` vise tout point d'accès compatible (Ollama, vLLM, llama.cpp, LM Studio), avec repli de `json_schema` vers `json_object` sans garantie, et quatre tentatives en cas de JSON invalide
- Exécution — bibliothèque, plus une base de graphes à héberger et à sauvegarder ; MCP et REST à protéger par l'opérateur. Télémétrie PostHog active par défaut : `GRAPHITI_TELEMETRY_ENABLED=false`, et filtrer la sortie réseau
- Coût — gratuit sous Apache-2.0 : usage chez un client, embarquement et service hébergé permis, avec conservation des mentions. **Les licences des backends sont à lire à part** : FalkorDB est sous SSPLv1, Neo4j Community sous GPLv3 (cf. [[Neo4j]]). Épingler la version **0.28.2 ou plus** : CVE-2026-32247 (injection Cypher par `SearchFilters.node_labels`, sévérité haute 8.1)

## Écosystème

### Alternatives

- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.
- [[Letta]] — Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte.

### Compléments

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.

## Ressources

- Documentation — https://help.getzep.com/graphiti/getting-started/overview
- Papier — https://arxiv.org/abs/2501.13956
- Article — annonce de la fin de la Community Edition de Zep : https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/
- Article — avis de sécurité GHSA-gg5m-55jj-8m5g : https://github.com/getzep/graphiti/security/advisories/GHSA-gg5m-55jj-8m5g
- Dépôt — https://github.com/getzep/graphiti

## Voir aussi

- [[Agent memory]] — la notion ; Graphiti en est la variante à **graphe temporel**, que la notion ne décrit pas encore
- [[Comparatif - Mémoire pour agents]] — le départage des outils de mémoire du dossier
- [[Mémoire des agents]] — le hub du dossier
- [[Memgraph]] et [[Apache AGE]] — autres bases de graphes du brain ; ni l'une ni l'autre n'est documentée par Graphiti
