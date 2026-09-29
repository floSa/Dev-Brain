---
role: notion
nom: Recherche sémantique
alias: [semantic search, recherche par le sens, recherche dense]
categorie: database/recherche
domaines: [data-eng, ai-eng]
tags: [search, semantic-search, embeddings]
---

# Recherche sémantique

## Aperçu

- Retrouver des documents par le **sens** de la requête, non par les mots exacts qu'elle contient. « Voiture rouge » retrouve « automobile écarlate ».
- Elle repose sur des [[embeddings]] : requête et documents sont encodés en vecteurs, et les documents les plus proches sont renvoyés. C'est la moitié dense de la recherche d'information (cf. [[Recherche d'information]]).

## Concepts clés

### Le principe
- Un modèle d'embedding transforme un texte en vecteur dense. La proximité géométrique approxime la proximité de sens.
- On encode le corpus une fois, à l'indexation, et la requête à chaque recherche. Le classement est la distance entre le vecteur de la requête et ceux des documents.

### Ce que l'index change
- La recherche exacte compare à tous les vecteurs ; à l'échelle on utilise une [[Recherche vectorielle approximative]]. L'index inversé ([[Index inversé]]) n'intervient pas dans ce cas : il relie des mots, pas des vecteurs.

### Ce qu'elle rate
- Un identifiant, un code produit, un nom rare, un acronyme : le modèle n'a pas de sens à leur associer, et un mot exact reste plus fiable. C'est la raison d'être de l'hybride ([[Hybrid retrieval]]).
- La qualité dépend du modèle : langue, domaine, longueur des textes. Un modèle généraliste sur un jargon métier peut classer mal.

### Qui la propose
- [[Elasticsearch]] et [[OpenSearch]] (requêtes neuronales), [[Meilisearch]], [[Typesense]] (embeddings générés par le moteur) et [[Apache Solr]] (recherche vectorielle) l'ajoutent à leur index plein texte ; [[txtai]] en fait son cœur.

## Les maths, simplement

- **Similarité cosinus** entre le vecteur requête $q$ et le vecteur document $d$ : $\cos(q,d) = \dfrac{q \cdot d}{\lVert q \rVert \, \lVert d \rVert}$. Elle vaut 1 pour deux vecteurs de même direction, 0 pour deux vecteurs orthogonaux.
- Le classement trie les documents par cosinus décroissant, ou par produit scalaire quand les vecteurs sont normalisés.

## En pratique

- Choisir le modèle d'embedding avant le moteur : c'est lui qui décide de la qualité, et changer de modèle impose de réindexer tout le corpus.
- Évaluer sur ses propres requêtes avec des métriques d'ordre ([[Recherche d'information]]) avant de la préférer au lexical.
- Sur un corpus mêlant textes libres et identifiants, partir de l'hybride plutôt que du dense seul.
- Piège : « sémantique » ne garantit pas la pertinence. Un document proche en sens peut répondre à côté de la question, d'où l'étape de [[Reranking]] après la récupération.

## Approches voisines & alternatives

- [[Recherche d'information]] — la discipline générale, avec ses trois familles.
- [[BM25]] — la recherche lexicale, sa complémentaire.
- [[Hybrid retrieval]] — les deux combinées.
- [[Bases de données vectorielles]] — le stockage dédié aux vecteurs.
- [[RAG]] — l'usage le plus courant aujourd'hui : récupérer du contexte pour un LLM.
- [[sentence-transformers]] — une bibliothèque pour produire ces embeddings.

## Pour aller plus loin

- Reimers et Gurevych (2019) — *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*.
