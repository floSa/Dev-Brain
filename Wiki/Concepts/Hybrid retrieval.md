---
galaxie: wiki
type: concept
nom: Hybrid retrieval
alias: [recherche hybride, hybrid search, retrieval hybride, dense + sparse]
categorie: concept/llm
domaines: [ai-eng]
tags: [retrieval, hybrid-search, semantic-search, search, rag]
---

# Hybrid retrieval

## Aperçu

- Combiner deux récupérations complémentaires : **dense** (similarité d'[[embeddings]], le sens) et **lexicale / sparse** (BM25, les mots exacts).
- Chacune rattrape les angles morts de l'autre ; ensemble elles dominent presque toujours une modalité seule sur un corpus réaliste.

## Concepts clés

### Dense vs lexical
- **Dense** : trouve paraphrases et synonymes, mais peut rater un identifiant, un code, un nom rare.
- **Lexical ([[BM25]])** : excelle sur les correspondances exactes (entités, références, jargon, acronymes), aveugle au synonyme.

### Fusion des résultats
- Deux listes classées à combiner. Deux familles :
  - **Reciprocal Rank Fusion (RRF)** : combine les **rangs**, sans calibrer les scores. Robuste, défaut courant.
  - **Pondération de scores** : normaliser puis $\alpha \cdot \text{dense} + (1-\alpha)\cdot \text{lexical}$ ; demande de calibrer $\alpha$.

### Sparse appris
- Modèles type **SPLADE** : sparse mais appris, à mi-chemin entre BM25 et dense.

## Les maths, simplement

- **BM25**, score d'un document $D$ pour une requête $Q$ : $\sum_{t \in Q} \text{IDF}(t)\cdot \dfrac{f(t,D)\,(k_1+1)}{f(t,D) + k_1\,(1 - b + b\,\frac{|D|}{\text{avgdl}})}$, avec $f(t,D)$ la fréquence du terme, $|D|$ la longueur du document, $\text{avgdl}$ la longueur moyenne, $k_1$ et $b$ des paramètres.
- **RRF** : $\text{RRF}(d) = \sum_i \frac{1}{k + r_i(d)}$ — fusionne les rangs de chaque liste.

## En pratique

- Beaucoup de moteurs le font nativement : [[Dev/Services/Elasticsearch|Elasticsearch]] / OpenSearch (BM25 + kNN), [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Qdrant|Qdrant]] ; côté framework, [[Dev/Services/Haystack|Haystack]] expose des retrievers hybrides.
- Récupérer large en hybride, puis resserrer avec [[Reranking]] : combinaison gagnante.
- Régler la pondération sur **son** corpus ; choisir RRF si l'on ne veut pas calibrer.
- Piège : croire que le dense suffit — sur entités exactes et requêtes courtes, BM25 reste imbattable.

## Approches voisines & alternatives

- [[RAG]] — le retrieval hybride en est un levier de qualité direct.
- [[embeddings]] — la moitié dense de l'équation.
- [[Reranking]] — l'étape d'après, sur le pool fusionné.
- [[Advanced RAG]] — l'hybride y est une brique standard.
- [[Bases de données vectorielles]] — beaucoup intègrent désormais BM25 + ANN dans le même moteur.
- [[Recherche d'information]] — la discipline générale dont l'hybride est une stratégie ; [[TF-IDF]] et [[BM25]] en sont le versant lexical.

## Pour aller plus loin

- Formal et al. (2021) — *SPLADE*.
- Cormack et al. (2009) — *Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods*.
