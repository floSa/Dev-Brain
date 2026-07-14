---
galaxie: dev
type: service
nom: umap-learn
alias: [UMAP, Uniform Manifold Approximation and Projection]
pitch: "Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Scikit-Learn|Scikit-Learn]]", "[[Dev/Services/PaCMAP|PaCMAP]]"]
remplace_par: []
status: actif
tags: [dimensionality-reduction, manifold, unsupervised]
url_docs: https://umap-learn.readthedocs.io/
url_repo: https://github.com/lmcinnes/umap
---

# umap-learn

## Pourquoi

Implémentation de référence d'**UMAP** (Uniform Manifold Approximation and Projection), réduction de dimension **non linéaire** fondée sur l'apprentissage de variété (famille manifold de la [[Réduction de dimension]]). Construit un graphe de voisinage flou en haute dimension, puis l'optimise en basse dimension. Préserve mieux la **structure globale** que t-SNE et tourne nettement plus vite (cœur Numba, recherche de voisins via pynndescent). Sert aussi bien à la visualisation 2-3D qu'au pré-traitement vers k dimensions. API scikit-learn (`fit_transform`), avec `transform` sur données nouvelles et un mode supervisé / semi-supervisé.

## Quand l'utiliser

- Visualiser en 2-3D des données à haute dimension (embeddings, single-cell, images) en gardant des amas lisibles.
- Réduire la dimension **avant un clustering** (pipeline [[Dev/Services/hdbscan|UMAP → HDBSCAN]]).
- Projeter de nouveaux points après apprentissage (`transform`) — ce que t-SNE ne fait pas nativement.
- Réduction **supervisée** (UMAP guidé par les labels) pour mieux séparer des classes.

## Quand NE PAS l'utiliser

- Réduction **linéaire** interprétable (axes = combinaisons de variables, variance expliquée) → [[Wiki/Concepts/PCA|PCA]] via [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- t-SNE ou autres manifolds suffisent sans nouvelle dépendance → `sklearn.manifold` de [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- Conserver des distances exactes ou une inertie chiffrée → méthodes factorielles ([[Réduction de dimension]]).

## Déploiement & coût

- Bibliothèque Python (`uv add umap-learn`), accélérée par Numba. Rien à héberger.
- Single-node, en mémoire ; première exécution lente (compilation Numba JIT), puis rapide.
- BSD-3-Clause, gratuit.

## Pièges

- Le paquet PyPI s'appelle `umap-learn` mais le module s'importe `import umap` — à ne pas confondre avec le paquet `umap` (sans rapport).
- Les distances et les **tailles d'amas** dans la projection ne sont pas quantitativement fiables : ne pas les sur-interpréter.
- Très sensible à `n_neighbors` (équilibre local/global) et `min_dist` (compacité) : tester plusieurs réglages.
- Stochastique : fixer `random_state` pour la reproductibilité (au prix du parallélisme).

## Alternatives

- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
- [[Dev/Services/PaCMAP|PaCMAP]] — Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable.

## Liens

- [[Dev/Patterns/Comparatif - Réduction de dimension]] — PCA / t-SNE / UMAP / PaCMAP.
- Concept : [[t-SNE and UMAP]] — la notion (réduction non linéaire pour la viz) ; page chapeau [[Réduction de dimension]] (famille manifold).
- Pipeline fréquent : umap-learn (réduction) → [[Dev/Services/hdbscan|hdbscan]] (clustering).
- Doc : https://umap-learn.readthedocs.io/
