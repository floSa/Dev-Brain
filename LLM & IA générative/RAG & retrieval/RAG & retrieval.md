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
- **Trois questions se posent avant tout moteur.** Faut-il récupérer du tout, ou coller un petit corpus stable dans le prompt avec un cache ? ([[Coller le corpus ou récupérer]]). Qui a le droit de lire quoi, car le filtre se pose avant le prompt et aucun montage ne corrige un sur-partage à la source ? ([[Droits d'accès dans un RAG]]). Le corpus a-t-il une structure à exploiter, sections, table des matières, résumés par niveau ? ([[RAG hiérarchique]]).
- **Deux natures de briques cohabitent.** [[LlamaIndex]] et [[Haystack]] sont des frameworks de pipeline complets ; [[RAGatouille]] n'apporte qu'un étage — ColBERT, la late interaction — à insérer dans un pipeline existant. Les rerankers ([[bge-reranker]], [[FlashRank]], [[Cohere Rerank]], [[Jina Reranker]]) sont de cette seconde nature : un étage de plus, jamais un pipeline. Le moteur de stockage, lui, n'est pas ici : il est dans [[Vectoriel]] et [[Recherche]].
- Le pipeline **se mesure étage par étage** ou pas du tout : une bonne réponse sur un mauvais contexte est un coup de chance. Cf. [[RAG eval]] et [[RAG benchmarks]], dans [[Évaluation]].

## Choisir

- Un moteur RAG livré avec parsing par mise en page, index, chat et droits, plutôt qu'un assemblage → [[RAGFlow]] ; le choix entre clé en main et assemblé est dans [[RAG documentaire on-prem - clé en main ou assemblé]].
- Partir d'un pipeline complet, orienté indexation de documents → [[LlamaIndex]].
- Un pipeline explicite, composant par composant, plutôt qu'une abstraction → [[Haystack]].
- Ajouter du ColBERT à un pipeline qui existe déjà → [[RAGatouille]].
- Des schémas, tableaux ou plans que l'OCR défigure, et un GPU pour indexer → [[RAG visuel - retrouver des documents sans OCR]] ; la brique est [[ColPali]], dont la bibliothèque n'est plus recommandée (préférer [[sentence-transformers]]) et dont la licence des poids se lit modèle par modèle.
- Les réponses sont plausibles mais fausses sur les termes rares → [[Hybrid retrieval]].
- Le bon passage est récupéré mais mal classé → [[Reranking]], puis un reranker : [[bge-reranker]] en local et ouvert, [[FlashRank]] sans GPU, [[Cohere Rerank]] en API, [[Jina Reranker]] pour le contexte long (poids non commerciaux) — départagés dans [[Comparatif - Rerankers]].
- Les questions sont mal posées, ambiguës ou conversationnelles → [[Query transformations]].
- La question demande de croiser plusieurs documents → [[GraphRAG]]. Deux frameworks de graphe, **sans classement** faute de mesure indépendante : [[Microsoft GraphRAG]] (communautés et rapports de communauté, donc une recherche globale sur tout le corpus ; indexation plus lourde ; dépôt en mode maintenance, corrections de bogues et de dépendances seulement) ou [[LightRAG]] (pas de communautés, ajout et suppression incrémentaux de documents, serveur avec interface web ; stockages par défaut hors production, à protéger avant toute exposition). Corpus stable et questions de synthèse : le premier ; corpus qui change : le second ; dans les deux cas, mesurer d'abord un RAG vectoriel sur ses questions.
- Un petit corpus stable, à droits uniques, interrogé souvent → le coller dans le prompt avec un cache plutôt que d'indexer ; sinon récupérer : [[Coller le corpus ou récupérer]].
- Des documents longs et structurés (manuels, normes, contrats) → un découpage parent-enfant d'abord, un arbre de résumés ou la table des matières ensuite : [[RAG hiérarchique]].
- Des utilisateurs qui n'ont pas les mêmes droits sur les documents → filtrer avant le prompt, à chaque appel : [[Droits d'accès dans un RAG]].
- Des graphiques, des photos ou des enregistrements à retrouver par une question en texte → [[Embedding multimodal et modality gap]], dans [[Embeddings & encodeurs]] (modèles : [[EmbeddingGemma 2]], [[Qwen3-VL-Embedding]], [[SigLIP 2]]).
- Les faits sont déjà dans un graphe RDF à schéma écrit et la question demande une liste exacte → interroger plutôt que résumer : [[Interroger un graphe en langage naturel]] ; le sujet commence à [[Graphe de connaissances]], dans le dossier [[Ontologies et RDF]] ; pour l'usine, [[Pattern - Graphe de connaissances industriel sur site]].
- Rien ne marche et on n'a pas encore regardé le découpage → [[Chunking strategies]], d'abord.
- Stocker et interroger les vecteurs → [[Vectoriel]] ; un moteur qui indexe aussi du texte → [[Recherche]].
- Le modèle doit décider quand chercher, relancer ou vérifier, sur des questions à plusieurs sauts → [[RAG agentique]].

<!-- AUTO:START -->
### Notions
- [[Advanced RAG]] — domaines : ai-eng
- [[Chunking strategies]] — domaines : ai-eng
- [[Coller le corpus ou récupérer]] — domaines : ai-eng
- [[Construction de graphes de connaissances]] — domaines : ai-eng
- [[Droits d'accès dans un RAG]] — domaines : ai-eng, data-eng
- [[GraphRAG]] — domaines : ai-eng
- [[Hybrid retrieval]] — domaines : ai-eng
- [[Late-interaction retrieval]] — domaines : ai-eng
- [[Query transformations]] — domaines : ai-eng
- [[RAG]] — domaines : ai-eng
- [[RAG agentique]] — domaines : ai-eng
- [[RAG documentaire on-prem - clé en main ou assemblé]] — domaines : ai-eng
- [[RAG hiérarchique]] — domaines : ai-eng
- [[RAG visuel - retrouver des documents sans OCR]] — domaines : ai-eng, data-eng
- [[Reranking]] — domaines : ai-eng

### Briques
- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local.
- [[Cohere Rerank]] — API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis.
- [[ColPali]] — Recherche de pages de documents par leur image (ILLUIN, code MIT) — un modèle vision-langage encode chaque page en environ 1 030 vecteurs comparés à la requête par MaxSim, sans OCR ; colpali-engine est déprécié au profit de Sentence Transformers v6, et la licence des poids varie selon le modèle de base.
- [[FlashRank]] — Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[Jina Reranker]] — Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem.
- [[LightRAG]] — Framework RAG sur graphe (HKUDS, MIT) — extraction d'entités et de relations par LLM, récupération à deux niveaux (détails et concepts) sur graphe et vecteurs, ajout et suppression incrémentaux de documents ; serveur avec interface web et API, v1.5.7 en septembre 2026.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Microsoft GraphRAG]] — Bibliothèque Python de recherche (Microsoft, MIT) qui extrait un graphe d'un corpus par LLM, le découpe en communautés avec un rapport par communauté, puis répond en recherche locale, globale ou DRIFT ; projet en mode maintenance (corrections et mises à jour de dépendances seulement), v3.3.0 en octobre 2026.
- [[RAGatouille]] — Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025).
- [[RAGFlow]] — Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.

### Comparatifs
- [[Comparatif - Rerankers]]
<!-- AUTO:END -->
