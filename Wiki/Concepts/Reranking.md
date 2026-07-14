---
galaxie: wiki
type: concept
nom: Reranking
alias: [reranking, reclassement, re-ranking, rerank]
categorie: concept/llm
domaines: [ai-eng]
tags: [retrieval, reranking, ranking, rag]
---

# Reranking

## Aperçu

- Deuxième étage du retrieval : reprendre le top-k récupéré (rapide mais grossier) et le **reclasser finement** avant de le passer au LLM.
- Gain de précision parmi les meilleurs candidats, là où le premier étage ne visait que le rappel.

## Concepts clés

### Bi-encoder vs cross-encoder
- **Bi-encoder** (1er étage) : encode requête et document **séparément**, compare des vecteurs. Rapide, pré-calculable, mais grossier.
- **Cross-encoder** (reranker) : encode la paire **(requête, document) ensemble** et juge la pertinence directement. Beaucoup plus précis, beaucoup plus coûteux → réservé au top-k.

### Le pipeline en deux temps
- Récupérer large (top-50/100) au 1er étage, reclasser puis garder le top-3/5 au reranker. Le LLM ne voit que l'élite.

### Variantes
- **Cross-encoders ouverts** : BGE-reranker, mxbai-rerank (via [[Dev/Services/HuggingFace|HuggingFace]]).
- **API managées** : Cohere Rerank, Jina Reranker.
- **LLM-as-reranker** : demander au LLM de scorer / ordonner les passages (souple, cher).

## Les maths, simplement

- Cross-encoder : score de pertinence $s = g(\text{requête}, \text{document}) \in \mathbb{R}$ calculé sur la paire concaténée ; on trie le top-k par $s$ décroissant.
- Différence clé avec le bi-encoder $\cos(\mathbf{e}_q, \mathbf{e}_d)$ : pas d'embeddings indépendants, donc pas de pré-calcul possible — d'où le coût à la requête.

## En pratique

- Souvent le **meilleur rapport gain/effort** après le retrieval hybride : un reranker sur un top-k correct relève nettement la précision finale.
- Choisir la profondeur : reranker trop de candidats = latence ; trop peu = on perd le bénéfice du large rappel amont.
- Intégré nativement dans [[Dev/Services/Haystack|Haystack]], [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/LangChain|LangChain]] (rankers, node postprocessors, compressors).
- Piège : reranker un top-k déjà mauvais ne crée pas l'information manquante — soigner d'abord [[Hybrid retrieval]] et [[Chunking strategies]].

## Approches voisines & alternatives

- [[RAG]] / [[Advanced RAG]] — le reranking en est le post-retrieval canonique.
- [[Hybrid retrieval]] — fournit le pool large que le reranker affine.
- [[embeddings]] — base du 1er étage bi-encoder que le cross-encoder vient corriger.
- [[Ranking metrics]] — NDCG, MAP, MRR pour évaluer la qualité d'un reclassement.
- [[Late-interaction retrieval]] — alternative multi-vecteur (ColBERT, MaxSim) au cross-encoder pour l'étage de précision.
- [[Recherche d'information]] — le cadre général (lexical / dense / hybride) dont le reranking est l'étage final.

## Pour aller plus loin

- Nogueira & Cho (2019) — *Passage Re-ranking with BERT*.
- Reimers & Gurevych (2019) — *Sentence-BERT* (bi- vs cross-encoder).
