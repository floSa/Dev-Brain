---
role: brique
nom: LlamaIndex
alias: [llamaindex, llama-index, llama_index, run-llama, GPT Index]
pitch: "Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LangChain]]", "[[Haystack]]", "[[DSPy]]"]
complements: []
tags: [llm, rag, embeddings, agents]
url_docs: https://developers.llamaindex.ai/python/framework/
url_repo: https://github.com/run-llama/llama_index
---

# LlamaIndex

<!-- AUTO:BANDEAU:START -->
> Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework **orienté données** pour connecter un LLM à des sources privées. Là où d'autres
partent de l'orchestration générale, LlamaIndex (ex-*GPT Index*) part du **pipeline de
connaissance** : charger des documents — LlamaHub en offre des centaines de connecteurs —,
les découper, les **indexer** (index vectoriel, par mots-clés, arbre, graphe de connaissances),
puis les **récupérer** et les passer au LLM via des moteurs de requête et de chat. C'est la
voie la plus directe vers un RAG sur ses propres données, et l'offre s'est étendue aux agents
sous forme de workflows événementiels. Le packaging est modulaire : `llama-index-core` d'un
côté, les intégrations de l'autre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Construire un RAG sur une base documentaire — ingestion, indexation, requête — avec un minimum de plomberie | Les réglages par défaut (taille de chunk, top-k) conditionnent fortement la qualité : à mesurer, jamais à subir |
| Exploiter des structures d'index variées — vectoriel, résumé, graphe de connaissances — selon la forme des données | API en évolution rapide, éclatée en sous-packages d'intégration : épingler les versions |
| Brancher beaucoup de sources hétérogènes via les connecteurs LlamaHub | Le graphe de connaissances et les index avancés sont séduisants mais coûteux en tokens et en latence — ne pas les prendre par défaut |
| Ajouter des agents et des workflows par-dessus une couche retrieval déjà en place | |

## Mise en œuvre

- Installation — `uv add llama-index-core`, plus les paquets d'intégration voulus
- Point d'entrée — chargement par connecteur LlamaHub, découpage, indexation, puis moteurs de requête et de chat
- Prérequis — un vector store pour l'index ([[Qdrant]], [[Chroma]], [[Weaviate]], [[pgvector]]) ; du parsing en amont si les documents ne sont pas déjà du texte ([[Docling]], [[Unstructured]], [[LlamaParse]])
- Exécution — bibliothèque importée dans l'app, aucune infra dédiée
- Coût — gratuit sous MIT ; LlamaCloud (parsing et index hébergés) est une offre payante distincte du framework ; le coût réel est dominé par les appels LLM et l'embedding des documents, à l'indexation comme à la requête

## Écosystème

### Alternatives

- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.

## Ressources

- Documentation — https://developers.llamaindex.ai/python/framework/
- Dépôt — https://github.com/run-llama/llama_index

## Voir aussi

- [[RAG]] — la notion du dossier
- [[Chunking strategies]] · [[Hybrid retrieval]] · [[Reranking]] · [[Advanced RAG]] — les techniques du pipeline
- [[LlamaIndex NLSQLTableQueryEngine]] — son module text-to-SQL, cf. [[Text-to-SQL]]
- [[LiteLLM]] — pour router ses appels de modèle ; [[HuggingFace]] pour les modèles
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks du domaine
