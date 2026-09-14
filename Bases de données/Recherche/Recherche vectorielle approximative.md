---
role: notion
nom: Recherche vectorielle approximative
alias: [approximate kNN, kNN approximatif, recherche kNN approximative, recherche des plus proches voisins approximative]
categorie: database/recherche
domaines: [data-eng, ai-eng]
tags: [search, ann, semantic-search]
---

# Recherche vectorielle approximative

## Aperçu

- Retrouver, dans un moteur de recherche, les $k$ documents dont le vecteur est le plus proche de celui de la requête, en échangeant un peu de **rappel** contre beaucoup de **vitesse**.
- Angle de cette page : ce que le moteur en fait. Les internes des index (HNSW, IVF, PQ) sont dans [[Index ANN — internes]] et ne sont pas repris ici.

## Concepts clés

### Exact ou approximatif
- L'exact (force brute) compare la requête à tous les vecteurs : rappel parfait, coût proportionnel au corpus. Il convient aux petits jeux ou aux sous-ensembles déjà filtrés.
- L'approximatif restreint la recherche à des candidats probables. La documentation d'[[Elasticsearch]] le recommande pour la plupart des charges de production, où la latence et l'échelle comptent plus qu'un rappel parfait.

### Les deux paramètres de la requête
- `k` : le nombre de voisins à renvoyer. `num_candidates` : la taille du pool exploré avant le classement final, dans [[Elasticsearch]]. Plus le pool est large, meilleur est le rappel, plus la latence monte.
- Ils jouent le rôle de l'`ef` d'un HNSW pur : le compromis rappel contre latence se règle à la requête, cf. [[hnswlib]].

### L'index dans le moteur
- [[Lucene]] porte un index HNSW natif, avec `maxConn` (16 par défaut) et `beamWidth` (100 par défaut) à la construction ; [[Typesense]] embarque un HNSW réglable par `M` et `ef_construction`.
- [[OpenSearch]] expose des requêtes k-NN et neuronales ; [[Apache Solr]] et [[Meilisearch]] proposent aussi la recherche vectorielle.

### Filtrer en même temps
- Une requête réelle combine souvent la proximité et un filtre (client, date, type). Le filtre exclut des documents de la liste renvoyée ; l'enchaînement pré-filtre / post-filtre, et son effet sur le rappel, est décrit dans [[Bases de données vectorielles]].

### D'où viennent les vecteurs
- Le vecteur de la requête sort du même modèle d'[[embeddings]] que ceux des documents. Certains moteurs le génèrent eux-mêmes à partir du texte de la requête, d'autres reçoivent le vecteur déjà calculé.

## Les maths, simplement

- **Rappel\@k** = (nombre de vrais $k$ plus proches retrouvés) / $k$. C'est ce qu'on sacrifie pour la vitesse, et ce qu'il faut mesurer sur ses propres requêtes.
- La proximité se mesure par cosinus, produit scalaire ou distance $L^2$ ; le choix est lié au modèle d'embedding et souvent figé à la création de l'index.

## En pratique

- Mesurer le rappel sur un jeu de requêtes réel avant de figer `num_candidates` ou `ef` : trop bas, il chute sans erreur.
- Pour un petit corpus ou un sous-ensemble filtré, le kNN exact suffit et évite d'avoir à régler un index.
- Piège : l'ANN ne remplace pas la recherche par mot. Sur un identifiant, un code ou un nom rare, le lexical reste supérieur ; d'où [[Hybrid retrieval]].
- Un moteur de recherche qui porte un index vectoriel évite un second système, mais un moteur dont l'unique index est vectoriel reste plus spécialisé : cf. [[Comparatif - Bases vectorielles]].

## Approches voisines & alternatives

- [[Index ANN — internes]] — comment fonctionnent HNSW, IVF et PQ.
- [[Bases de données vectorielles]] — le concept englobant, côté stockage.
- [[Recherche sémantique]] — l'usage qui motive cette recherche.
- [[Index inversé]] — l'autre structure, lexicale, du même moteur.
- [[Hybrid retrieval]] — la combinaison avec BM25.
- [[k-NN]] — le même principe, côté apprentissage automatique.

## Pour aller plus loin

- Malkov et Yashunin (2016) — *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs*.
- [[Comparatif - Bases vectorielles]] — les moteurs dont l'index est vectoriel.
