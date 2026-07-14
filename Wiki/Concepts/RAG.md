---
galaxie: wiki
type: concept
nom: RAG
alias: [Retrieval-Augmented Generation, génération augmentée par récupération, retrieval augmented generation]
categorie: concept/llm
domaines: [ai-eng]
tags: [rag, llm, retrieval, embeddings, semantic-search]
---

# RAG

## Aperçu

- Patron qui **ancre** la génération d'un LLM sur des documents **récupérés à la volée** : on cherche les passages pertinents pour la question, on les injecte dans le prompt, le modèle répond à partir d'eux.
- Réduit les hallucinations, ouvre l'accès à des connaissances privées ou récentes, sans réentraîner le modèle.

## Concepts clés

### Les deux temps : indexation puis requête
- **Hors-ligne (indexation)** : découper les documents ([[Chunking strategies]]), les encoder en [[embeddings]], les ranger dans une [[Bases de données vectorielles]].
- **En ligne (requête)** : encoder la question, récupérer le top-k des chunks proches, les concaténer au prompt, générer.

### Le retrieval est le goulot
- Un mauvais retrieval plafonne la qualité finale, peu importe le LLM derrière.
- Récupération dense (similarité d'embeddings), lexicale ([[BM25]]) ou [[Hybrid retrieval|hybride]].

### Génération ancrée
- Le prompt assemble instruction + contexte récupéré + question ; le modèle synthétise le contexte plutôt que sa mémoire paramétrique.
- Bonne pratique : répondre « uniquement à partir du contexte » et signaler explicitement l'absence d'information.

### Naïf vs avancé
- RAG naïf = un seul retrieval, top-k brut. Suffisant pour démarrer.
- Limites (requêtes ambiguës, multi-hop, bruit) → [[Advanced RAG]].

## Les maths, simplement

- Retrieval top-k : garder les $k$ chunks $c$ maximisant la similarité cosinus avec la requête $q$, soit $\operatorname{top\text{-}k}_c \cos(\mathbf{e}_q, \mathbf{e}_c)$ où $\mathbf{e}$ est l'embedding.
- Compromis sur $k$ : trop petit → contexte incomplet (rappel faible) ; trop grand → bruit, dilution et coût en tokens.

## En pratique

- Stack minimal : parseur de documents → [[Chunking strategies|chunking]] → [[embeddings]] → [[Bases de données vectorielles]] → LLM. Monté en quelques lignes avec [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/LangChain|LangChain]] ou [[Dev/Services/Haystack|Haystack]].
- Leviers de qualité, par ordre de rentabilité : qualité du chunking, [[Hybrid retrieval|retrieval hybride]], [[Reranking|reranking]] du top-k, puis prompt.
- Mesurer, pas deviner : faithfulness, context precision/recall (cf. [[RAG eval]]).
- Pièges : chunks trop gros (bruit) ou trop petits (contexte cassé) ; embeddings inadaptés à la langue/domaine ; métadonnées oubliées (pas de filtrage par source/date) ; cas « rien trouvé » non géré.

## Approches voisines & alternatives

- [[Advanced RAG]] — les techniques multi-étapes quand le RAG naïf plafonne.
- [[Chunking strategies]] — comment découper, en amont de tout.
- [[Hybrid retrieval]] — dense + lexical pour ne pas rater les correspondances exactes.
- [[Reranking]] — reclasser le top-k avant la génération.
- [[embeddings]] — la représentation qui rend la recherche sémantique possible.
- [[Bases de données vectorielles]] — la mémoire interrogeable du système.
- [[Context engineering]] — le RAG est un levier d'ingénierie de contexte : il décide quoi injecter dans la fenêtre.
- Frameworks : [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/Haystack|Haystack]], [[Dev/Services/LangChain|LangChain]].
- Alternative au RAG : le [[SFT|fine-tuning]] (apprendre la connaissance dans les poids) — coûteux et statique ; le RAG reste préférable pour des données qui changent.

## Pour aller plus loin

- Lewis et al. (2020) — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (papier fondateur).
- Sujets liés : [[Query transformations]], [[Routing and cascading]], [[RAG eval]], [[GraphRAG]] (retrieval sur graphe de connaissances).
