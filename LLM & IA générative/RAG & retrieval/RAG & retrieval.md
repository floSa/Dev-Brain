---
role: hub
nom: RAG & retrieval
alias: [retrieval augmented generation, récupération augmentée]
pitch: Ancrer une réponse sur des documents récupérés à la volée — et rattraper le retrieval quand la version naïve plafonne.
domaines: [ai-eng, data-eng]
tags: [rag, retrieval, chunking, reranking, semantic-search, knowledge-graph]
---

# RAG & retrieval

> Ancrer une réponse sur des documents récupérés à la volée — et rattraper le retrieval quand la version naïve plafonne.

## Ce qu'il faut comprendre

- **Le RAG est un problème de recherche avant d'être un problème de LLM.** Son plafond de qualité est celui du retrieval : un modèle plus gros ne répare pas un passage qu'on ne lui a pas donné. [[RAG]] pose le patron ; [[Advanced RAG]] est le catalogue de ce qu'on lui ajoute quand le top-k brut ne suffit plus.
- Le pipeline a **trois étages, et chacun a ses pages**. Avant le retrieval, on travaille la requête ([[Query transformations]]) et on décide où l'envoyer ([[Routing and cascading]], dans [[Passerelles]]). Pendant, on combine dense et lexical ([[Hybrid retrieval]]) ou on garde une interaction token-à-token ([[Late-interaction retrieval]]). Après, on reclasse ([[Reranking]]). C'est l'ordre de l'exécution, et c'est l'ordre dans lequel on débogue.
- **La décision la plus rentable est prise avant toute recherche** : [[Chunking strategies]] fixe l'unité qu'on indexe. Un chunk mal taillé casse le contexte ou noie le signal, et aucun étage aval ne le rattrape.
- Quand la réponse exige de **relier des faits épars**, l'index plat ne suffit plus : [[GraphRAG]] interroge un graphe d'entités, que [[Construction de graphes de connaissances]] fabrique en amont. La qualité du graphe plafonne celle de tout ce qui l'interroge — même rapport qu'entre le chunking et le retrieval vectoriel.
- **Deux natures de briques cohabitent.** [[LlamaIndex]] et [[Haystack]] sont des frameworks de pipeline complets ; [[RAGatouille]] n'apporte qu'un étage — ColBERT, la late interaction — à insérer dans un pipeline existant. Le moteur de stockage, lui, n'est pas ici : il est dans [[Vectoriel]] et [[Recherche]].
- Le pipeline **se mesure étage par étage** ou pas du tout : une bonne réponse sur un mauvais contexte est un coup de chance. Cf. [[RAG eval]] et [[RAG benchmarks]], dans [[Évaluation]].

## Choisir

- Partir d'un pipeline complet, orienté indexation de documents → [[LlamaIndex]].
- Un pipeline explicite, composant par composant, plutôt qu'une abstraction → [[Haystack]].
- Ajouter du ColBERT à un pipeline qui existe déjà → [[RAGatouille]].
- Les réponses sont plausibles mais fausses sur les termes rares → [[Hybrid retrieval]].
- Le bon passage est récupéré mais mal classé → [[Reranking]].
- Les questions sont mal posées, ambiguës ou conversationnelles → [[Query transformations]].
- La question demande de croiser plusieurs documents → [[GraphRAG]].
- Rien ne marche et on n'a pas encore regardé le découpage → [[Chunking strategies]], d'abord.
- Stocker et interroger les vecteurs → [[Vectoriel]] ; un moteur qui indexe aussi du texte → [[Recherche]].

<!-- AUTO:START -->
### Notions
- [[Advanced RAG]] — domaines : ai-eng
- [[Chunking strategies]] — domaines : ai-eng
- [[Construction de graphes de connaissances]] — domaines : ai-eng
- [[GraphRAG]] — domaines : ai-eng
- [[Hybrid retrieval]] — domaines : ai-eng
- [[Late-interaction retrieval]] — domaines : ai-eng
- [[Query transformations]] — domaines : ai-eng
- [[RAG]] — domaines : ai-eng
- [[Reranking]] — domaines : ai-eng

### Briques
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[RAGatouille]] — Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025).
<!-- AUTO:END -->
