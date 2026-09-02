---
role: brique
nom: LangChain
alias: [langchain, langchain-ai]
pitch: "Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith."
categorie: llm/socle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LlamaIndex]]", "[[Haystack]]", "[[DSPy]]", "[[Semantic Kernel]]", "[[PydanticAI]]"]
complements: []
tags: [llm, rag, agents, tool-use]
url_docs: https://docs.langchain.com/
url_repo: https://github.com/langchain-ai/langchain
---

# LangChain

## Pourquoi

Framework d'applications LLM le plus adopté (≈140k stars, version 1.x). Son cœur : des **interfaces standardisées** — modèles de chat, embeddings, vector stores, retrievers, outils — derrière lesquelles se branchent des centaines d'**intégrations**, ce qui permet de changer de fournisseur ou de base vectorielle sans réécrire la logique. On compose ces briques en **chaînes** (LCEL, le langage d'expression) et en **agents** (LLM qui choisit des outils en boucle). Écrit en **Python** (un portage JS/TS existe), licence **MIT**. C'est aussi le socle d'un écosystème plus large : [[LangGraph]] pour les agents stateful, LangSmith pour l'observabilité.

## Quand l'utiliser

- Prototyper vite une app LLM en s'appuyant sur le **catalogue d'intégrations** (modèles, vector stores, loaders, outils).
- Construire des **agents** simples à moyens (appel d'outils, RAG conversationnel) sans tout recâbler à la main.
- Rester **agnostique du fournisseur** : abstraire OpenAI/Anthropic/local derrière une interface commune.
- Bénéficier de l'écosystème ([[LangGraph]], LangSmith) pour passer du proto à la prod.

## Quand NE PAS l'utiliser

- Application **centrée données / RAG** où l'indexation et la récupération priment → [[LlamaIndex]].
- Pipelines de production avec **contrôle explicite** du flux (retrieval → routing → generation) → [[Haystack]].
- Besoin d'**optimiser automatiquement** les prompts plutôt que de les écrire à la main → [[DSPy]].
- Agents à **état complexe** (cycles, reprise, human-in-the-loop) : utiliser directement [[LangGraph]], la couche dédiée du même écosystème.

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée dans l'app (`pip`/`uv`), aucune infra propre — l'app scale comme n'importe quel service Python.
- Compléments **managés payants** de l'éditeur (LangChain Inc.) : LangSmith (observabilité/eval) et LangGraph Platform (déploiement d'agents) — optionnels, le framework reste utilisable seul.
- Les coûts réels viennent des **appels aux LLM** sous-jacents, pas du framework.

## Pièges

- **Surface d'API mouvante** : refactorings fréquents entre versions (0.x → 1.x), modules éclatés (`langchain-core`, `langchain-community`, packages d'intégration) — épingler les versions.
- Les **abstractions peuvent masquer** les prompts et appels réels : déboguer un comportement inattendu demande souvent de descendre sous la chaîne (d'où LangSmith).
- Facile de faire « marcher une démo », plus dur de fiabiliser : pour les agents non triviaux, basculer vers [[LangGraph]] plutôt que d'empiler les agents LangChain.

## Alternatives

- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.
- [[Semantic Kernel]] — SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur.
- [[PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).

## Liens

- Concept : [[RAG]] — et ses techniques [[Chunking strategies]], [[Hybrid retrieval]], [[Reranking]], [[Advanced RAG]].
- [[LangGraph]] — couche d'orchestration d'agents stateful du même écosystème, **au-dessus de** LangChain (graphes cycliques, état, reprise).
- Peut router ses appels via [[LiteLLM]] pour abstraire le fournisseur (format OpenAI vers 100+ providers).
- Modèles et embeddings depuis [[HuggingFace]] ; vector stores comme [[Qdrant]] ou [[Chroma]] pour le RAG.
- Module text-to-SQL : [[LangChain SQL agent]] (SQLDatabaseToolkit + agent) — cf. concept [[Text-to-SQL]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.langchain.com/
