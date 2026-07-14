---
galaxie: wiki
type: concept
nom: Recherche d'information
alias: [information retrieval, IR, recherche documentaire, retrieval lexical dense hybride]
categorie: concept/nlp
domaines: [ai-eng, data-sci]
tags: [nlp, information-retrieval, retrieval, hybrid-search, ranking, semantic-search]
---

# Recherche d'information

## Aperçu

- Trouver, dans une grande collection, les documents les plus **pertinents** pour une requête, puis les **ordonner**. Discipline antérieure de loin aux LLM, et qui fonde aujourd'hui le retrieval du [[RAG]].
- Trois familles de méthodes — lexicale, dense, hybride — suivies d'une étape de reclassement, le tout jugé par des métriques d'ordre.

## Concepts clés

### Lexicale (sparse)
- Appariement sur les **mots exacts**, pondérés par [[TF-IDF]] puis [[BM25]]. Rapide, interprétable, fort sur entités et jargon ; aveugle aux synonymes.

### Dense (sémantique)
- Encoder requête et documents en [[embeddings]] et chercher les plus proches (cosinus) via un index ANN ([[Bases de données vectorielles]]). Capte le sens, gère paraphrases et synonymes.

### Hybride + RRF
- Combiner les deux listes classées. [[Hybrid retrieval]] détaille : la **Reciprocal Rank Fusion** combine les rangs sans calibrer les scores ; l'alternative est une somme pondérée de scores normalisés.

### Re-ranking
- Deuxième étage : un cross-encoder ([[Reranking]]) reclasse finement le top-k récupéré, troquant du coût contre de la précision sur l'élite des candidats.

### Rappel vs précision
- Premier étage = maximiser le **rappel** (ne rien rater) ; reranking = maximiser la **précision** en tête de liste. Les deux objectifs se partagent le pipeline.

## Les maths, simplement

- **RRF** : $\text{RRF}(d) = \sum_i \dfrac{1}{k + r_i(d)}$, où $r_i(d)$ est le rang de $d$ dans la liste $i$ et $k$ une constante (~60). Fusionne des rangs, pas des scores → robuste à l'hétérogénéité d'échelle.
- Métriques d'ordre : **NDCG**, **MAP**, **MRR** — cf. [[Ranking metrics]].

## En pratique

- Pile typique : moteur lexical ([[Dev/Services/Elasticsearch|Elasticsearch]] / OpenSearch, BM25) + index vectoriel (dense), fusion RRF, puis reranker cross-encoder. Beaucoup de moteurs intègrent désormais les deux.
- Démarrer simple : BM25 seul est un baseline étonnamment fort ; ajouter le dense puis l'hybride si le rappel plafonne.
- En contexte LLM, c'est l'étage `retrieval` du [[RAG]] ; soigner aussi la [[Query transformations|transformation de requête]] en amont.
- Toujours mesurer sur **son** corpus avec des [[Ranking metrics]] — ne pas se fier au ressenti.

## Approches voisines & alternatives

- [[TF-IDF]], [[BM25]] — le versant lexical de la recherche.
- [[embeddings]], [[Bases de données vectorielles]] — le versant dense et son stockage.
- [[Hybrid retrieval]] — la fusion des deux (page sœur côté LLM / RAG).
- [[Late-interaction retrieval]] — la voie multi-vecteur (ColBERT), entre dense mono-vecteur et cross-encoder.
- [[Reranking]] — l'étage de précision sur le pool récupéré.
- [[RAG]] / [[Advanced RAG]] — l'application phare en IA générative.
- [[Ranking metrics]] — l'évaluation d'un ordre de pertinence.
- [[Traitement du langage naturel]] — page chapeau du sous-domaine.

## Pour aller plus loin

- Manning, Raghavan & Schütze — *Introduction to Information Retrieval* (référence libre, Stanford).
- Cormack et al. (2009) — *Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods*.
