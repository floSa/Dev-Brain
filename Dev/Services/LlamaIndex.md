---
galaxie: dev
type: service
nom: LlamaIndex
alias: [llamaindex, llama-index, llama_index, run-llama, GPT Index]
pitch: "Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LangChain|LangChain]]", "[[Dev/Services/Haystack|Haystack]]", "[[Dev/Services/DSPy|DSPy]]"]
remplace_par: []
status: actif
tags: [llm, rag, embeddings, agents]
url_docs: https://developers.llamaindex.ai/python/framework/
url_repo: https://github.com/run-llama/llama_index
---

# LlamaIndex

## Pourquoi

Framework **orienté données** pour connecter des LLM à des sources privées. Là où d'autres partent de l'orchestration générale, LlamaIndex (ex-*GPT Index*) part du **pipeline de connaissance** : charger des documents (LlamaHub : centaines de connecteurs), les découper et les **indexer** (index vectoriel, par mots-clés, arbre, graphe de connaissances), puis les **récupérer** et les passer au LLM via des moteurs de requête et de chat. La voie la plus directe pour un **RAG** sur ses propres données ; l'offre s'est étendue aux **agents** (workflows événementiels). Écrit en **Python**, licence **MIT**, packaging modulaire (`llama-index-core` + intégrations).

## Quand l'utiliser

- Construire un **RAG** sur une base documentaire : ingestion → indexation → requête, avec un minimum de plomberie.
- Exploiter des **structures d'index variées** (vectoriel, résumé, graphe de connaissances) selon la forme des données.
- Brancher beaucoup de **sources hétérogènes** via les connecteurs LlamaHub.
- Ajouter des **agents/workflows** par-dessus la couche retrieval déjà en place.

## Quand NE PAS l'utiliser

- App généraliste où l'orchestration d'**agents et d'outils** prime sur la donnée → [[Dev/Services/LangChain|LangChain]].
- Pipelines de production à **flux explicite et composable** (entreprise) → [[Dev/Services/Haystack|Haystack]].
- Recherche d'une **optimisation automatique** des prompts/modules → [[Dev/Services/DSPy|DSPy]].

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée dans l'app, pas d'infra dédiée.
- Offre **managée payante** de l'éditeur : **LlamaCloud** (parsing via [[Dev/Services/LlamaParse|LlamaParse]], index hébergés) — optionnelle, distincte du framework OSS.
- Coût dominé par les appels LLM et l'**embedding** des documents (indexation initiale + requêtes).

## Pièges

- Beaucoup d'**abstractions d'index/retriever** : les réglages par défaut (taille de chunk, top-k) conditionnent fortement la qualité — à mesurer, pas à subir.
- API en **évolution rapide** et éclatée en sous-packages d'intégration ; épingler les versions.
- Le **graphe de connaissances** et les index avancés sont séduisants mais coûteux en tokens/latence : ne pas les choisir par défaut.

## Alternatives

- [[Dev/Services/LangChain|LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Dev/Services/Haystack|Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[Dev/Services/DSPy|DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.

## Liens

- Concept : [[RAG]] — et ses techniques [[Chunking strategies]], [[Hybrid retrieval]], [[Reranking]], [[Advanced RAG]].
- Vector stores pour l'index : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Chroma|Chroma]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/pgvector|pgvector]].
- Parsing de documents en amont : [[Dev/Services/LlamaParse|LlamaParse]], [[Dev/Services/Docling|Docling]], [[Dev/Services/Unstructured|Unstructured]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs) ; modèles depuis [[Dev/Services/HuggingFace|HuggingFace]].
- Module text-to-SQL : [[Dev/Services/LlamaIndex NLSQLTableQueryEngine|LlamaIndex NLSQLTableQueryEngine]] — cf. concept [[Text-to-SQL]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://developers.llamaindex.ai/python/framework/
