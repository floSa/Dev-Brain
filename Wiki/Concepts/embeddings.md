---
galaxie: wiki
type: concept
nom: embeddings
alias: [représentations vectorielles, plongements, embedding, vector embeddings]
categorie: concept/ml
domaines: [data-sci, ai-eng]
tags: [embeddings, semantic-search, representation-learning]
---

# embeddings

## Aperçu

- Représentation d'un objet — mot, phrase, image, utilisateur, nœud de graphe — par un **vecteur dense** de réels, appris pour que la **géométrie reflète le sens** : proches dans l'espace = similaires.
- Transforme des données non structurées en entrées numériques exploitables par recherche, clustering, classification, recommandation.

## Concepts clés

### Dense vs sparse
- One-hot / sac-de-mots ([[TF-IDF]]) : vecteurs creux, immenses, sans notion de proximité (« chat » et « félin » orthogonaux).
- Embedding : quelques centaines de dimensions, denses, où la proximité géométrique a un sens.

### Apprises, pas calculées
- Produites par un modèle entraîné sur une tâche : word2vec / GloVe (mots), *sentence-transformers* (phrases), [[Modèles de fondation vision|CLIP]] (images), node2vec (graphes).
- L'espace capte des régularités : `roi − homme + femme ≈ reine`.

### Similarité
- Mesurée par **cosinus** (direction) ou produit scalaire ; sur vecteurs normalisés, les deux coïncident. Voir [[Bases de données vectorielles]].

### Usages
- Recherche sémantique et RAG, déduplication, recommandation, [[Clustering]], classification par transfert, visualisation ([[t-SNE and UMAP]]).

## Les maths, simplement

- Plongement : fonction apprise $f : \mathcal{X} \to \mathbb{R}^d$, avec $d$ de l'ordre de 100 à 4000.
- Similarité cosinus : $\cos(\theta) = \dfrac{\mathbf{a}\cdot\mathbf{b}}{\lVert\mathbf{a}\rVert\,\lVert\mathbf{b}\rVert} \in [-1, 1]$.
- Apprentissage contrastif : rapprocher les paires positives, éloigner les négatives (perte type InfoNCE).

## En pratique

- Choisir le modèle selon le domaine et la langue ; normaliser les vecteurs si l'on travaille au cosinus.
- Stocker et chercher à l'échelle → [[Bases de données vectorielles]] (index ANN).
- Inspecter la structure → [[t-SNE and UMAP]] (sans sur-interpréter les distances).
- Pièges : mélanger des embeddings de modèles différents (espaces incompatibles) ; oublier la normalisation ; dimensions trop grandes (RAM, malédiction de la dimension → [[Réduction de dimension]]).

## Approches voisines & alternatives

- [[Bases de données vectorielles]] — stockage et recherche ANN des embeddings (la mémoire du RAG).
- [[t-SNE and UMAP]] — projeter des embeddings en 2-3D pour les inspecter.
- [[Réduction de dimension]] — compresser ou débruiter un espace d'embeddings.
- [[Clustering]] — regrouper des objets via leurs embeddings.
- [[Metric learning & ré-identification]] — comment entraîner ces espaces (triplet, ArcFace) pour la similarité et la ré-identification.
- [[Modèles de fondation vision]] — CLIP produit des embeddings **image-texte alignés** dans un espace commun (recherche multimodale, zero-shot).
- [[TF-IDF]] — la représentation sparse / lexicale, alternative historique aux embeddings denses.

## Pour aller plus loin

- Mikolov et al. (2013) — *word2vec*.
- Reimers & Gurevych (2019) — *Sentence-BERT*.
- Sujets liés à (re)créer en v2 (réservoir v1) : Tokenization, RAG, Chunking strategies.
