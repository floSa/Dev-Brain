---
galaxie: wiki
type: concept
nom: Advanced RAG
alias: [RAG avancé, advanced retrieval-augmented generation, modular RAG]
categorie: concept/llm
domaines: [ai-eng]
tags: [rag, llm, retrieval]
---

# Advanced RAG

## Aperçu

- Ensemble de techniques qui dépassent le [[RAG]] naïf (un seul retrieval, top-k brut) en agissant **avant, pendant et après** la récupération.
- But : meilleur rappel et meilleure précision du contexte — donc réponses plus fidèles — sur les requêtes ambiguës, multi-hop ou bruitées.

## Concepts clés

### Pré-retrieval (côté requête)
- **[[Query transformations]]** : réécriture, expansion, décomposition en sous-questions ; HyDE (générer une réponse hypothétique puis chercher avec son embedding).
- **[[Routing and cascading|Routing]]** : diriger la requête vers le bon index / la bonne source.

### Retrieval
- [[Hybrid retrieval]] (dense + BM25), multi-index, recherche filtrée par métadonnées.
- Découpage malin en amont : [[Chunking strategies]] (parent-child, fenêtre glissante).

### Post-retrieval
- [[Reranking]] du top-k par un cross-encoder.
- **Compression / filtrage** du contexte : ne garder que les phrases utiles (moins de bruit, moins de tokens).

### Patterns établis
- **Self-RAG / corrective RAG** : le modèle juge la pertinence du contexte récupéré et relance si besoin.
- **[[GraphRAG]]** : retrieval sur un graphe de connaissances pour les questions globales / multi-hop.
- **Agentic RAG** : un agent décide quand et quoi récupérer, en boucle.

## Les maths, simplement

- Fusion de classements par **Reciprocal Rank Fusion** : $\text{RRF}(d) = \sum_i \dfrac{1}{k + r_i(d)}$, où $r_i(d)$ est le rang de $d$ dans la liste $i$ et $k$ une constante (souvent 60).
- Intuition : combine plusieurs classements sans avoir à calibrer leurs scores bruts les uns par rapport aux autres.

## En pratique

- Adopter par étapes, en mesurant à chaque ajout : hybride → reranking → query transform. Inutile d'empiler si le RAG naïf suffit.
- Chaque étage coûte en **latence et tokens** : arbitrer gain de qualité contre budget.
- Outillage : [[Dev/Services/LlamaIndex|LlamaIndex]] et [[Dev/Services/Haystack|Haystack]] exposent ces briques (rerankers, routers, query engines) ; [[Dev/Services/LangChain|LangChain]] aussi.
- Piège : complexifier avant d'avoir une mesure ; un pipeline avancé mal évalué masque ses propres régressions.

## Approches voisines & alternatives

- [[RAG]] — le socle dont ceci est l'extension.
- [[GraphRAG]] — le patron qui remplace l'index de chunks plats par un graphe de connaissances (questions multi-hop / globales).
- [[Hybrid retrieval]], [[Reranking]], [[Chunking strategies]] — les briques mobilisées ici.
- [[embeddings]] — toujours la représentation de base.
- Frameworks : [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/Haystack|Haystack]], [[Dev/Services/LangChain|LangChain]].

## Pour aller plus loin

- Gao et al. (2023) — *Retrieval-Augmented Generation for Large Language Models: A Survey* (taxonomie naive / advanced / modular RAG).
- Asai et al. (2023) — *Self-RAG*.
- Sujets liés : [[Query transformations]], [[Routing and cascading]], [[RAG eval]].
