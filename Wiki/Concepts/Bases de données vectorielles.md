---
galaxie: wiki
type: concept
nom: Bases de données vectorielles
alias: [vector db, vector store, base vectorielle]
categorie: concept/data
domaines: [data-eng, ai-eng]
tags: [vector-db, embeddings, semantic-search, rag]
---

# Bases de données vectorielles

## Aperçu

- Stocke des **embeddings** (vecteurs de flottants) et retrouve les plus proches d'un vecteur requête.
- Sert de mémoire à la recherche sémantique et au RAG : « trouve ce dont le *sens* ressemble à la question », pas « ce dont les mots correspondent ».
- Brique centrale des apps LLM ; côté Dev, plusieurs moteurs l'implémentent (cf. *Approches voisines*).

## Concepts clés

### Embedding
- Vecteur dense (typiquement 384 à 1536 dimensions) produit par un modèle.
- Encode le sens : la proximité géométrique approxime la proximité de sens.
- Détail : voir [[embeddings]].

### Recherche ANN (Approximate Nearest Neighbor)
- Le k-plus-proches-voisins exact coûte O(n) par requête — trop lent à grande échelle.
- Les index ANN (HNSW, IVF, PQ) échangent un peu de rappel contre beaucoup de vitesse.
- HNSW = graphe navigable hiérarchique, défaut courant ; IVF = partitionnement, plus rapide à construire sur gros volumes.
- Détail des familles et de leurs réglages : voir [[Index ANN — internes]].

### Métrique de distance
- Cosinus, produit scalaire, ou L2 (euclidienne).
- Liée au modèle d'embedding ; souvent figée à la création de l'index.

### Filtrage par métadonnées
- Restreindre la recherche par attributs (client, date, type) en plus de la similarité.
- Pre-filter (exact, peut être lent) vs post-filter (rapide, peut perdre du rappel).

### Recherche hybride
- Combine dense (sémantique) et lexical (BM25).
- Rattrape les correspondances exactes — codes, noms propres, références — que le sémantique seul rate.

## Les maths, simplement

- Similarité cosinus : $\cos(\theta) = \dfrac{\mathbf{a}\cdot\mathbf{b}}{\lVert\mathbf{a}\rVert \, \lVert\mathbf{b}\rVert}$ — vaut 1 si même direction (même sens), 0 si orthogonaux.
- Distance euclidienne : $\lVert \mathbf{a}-\mathbf{b}\rVert_2 = \sqrt{\sum_i (a_i - b_i)^2}$ — plus elle est petite, plus c'est proche.
- Sur des vecteurs normalisés ($\lVert\mathbf{a}\rVert = 1$), cosinus et produit scalaire coïncident → beaucoup de moteurs normalisent en amont. Fondations : *Vector norms* (réservoir v1).
- $k$ = nombre de voisins retournés. **Rappel** = fraction des vrais $k$ plus proches effectivement trouvés par l'index approché.

## En pratique

- Pipeline RAG : découper (chunking) → encoder → indexer → requêter top-$k$ → fournir au LLM.
- Index par défaut : HNSW (bon compromis rappel/latence) ; IVF si très gros volume.
- Pièges fréquents : métrique incohérente avec le modèle ; dimensions qui font exploser la RAM ; filtrage mal placé qui ruine le rappel ; oubli de la mise à jour / suppression des vecteurs.
- Pas toujours nécessaire : pour quelques milliers de vecteurs, un index [[Dev/Services/Faiss|Faiss]] en mémoire (ou du NumPy) suffit ; pour un besoin purement lexical, un moteur full-text suffit.

## Approches voisines & alternatives

- Serveurs (persistance, filtrage, API, scaling) : [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/pgvector|pgvector]], [[Dev/Services/Milvus|Milvus]], [[Dev/Services/Pinecone|Pinecone]].
- Bibliothèques ANN embarquées (index in-process, sans serveur) : [[Dev/Services/Faiss|Faiss]], [[Dev/Services/hnswlib|hnswlib]], [[Dev/Services/Annoy|Annoy]], [[Dev/Services/ScaNN|ScaNN]] ; bases légères embarquées (entre les deux) : [[Dev/Services/Chroma|Chroma]], [[Dev/Services/LanceDB|LanceDB]] (multimodale, format colonnaire Lance).
- Moteurs recherche+vectoriel (full-text + ANN dans un même moteur) : [[Dev/Services/Vespa|Vespa]], [[Dev/Services/Elasticsearch|Elasticsearch]], [[Dev/Services/txtai|txtai]], [[Dev/Services/Marqo|Marqo]] — cf. [[Recherche d'information]].
- [[Index ANN — internes]] — comment ces index fonctionnent (HNSW, IVF, PQ) et se règlent.
- [[embeddings]] — ce que ces bases stockent et recherchent.
- Vector norms — la base mathématique des distances employées ici (réservoir v1).
- Recherche lexicale (BM25, full-text) — complément en mode hybride, pas substitut.

## Pour aller plus loin

- Sujets liés à (re)créer en v2 (réservoir v1) : Advanced RAG, Chunking strategies, Decoding strategies.
- Comparatif des moteurs : [[Comparatif - Bases vectorielles]] (vue Dev).
