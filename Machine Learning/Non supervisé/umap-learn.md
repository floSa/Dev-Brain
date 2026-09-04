---
role: brique
nom: umap-learn
alias: [UMAP, Uniform Manifold Approximation and Projection]
pitch: "Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite."
categorie: ml/non-supervise
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Scikit-Learn]]", "[[PaCMAP]]"]
complements: ["[[hdbscan]]"]
tags: [dimensionality-reduction, manifold, unsupervised]
url_docs: https://umap-learn.readthedocs.io/
url_repo: https://github.com/lmcinnes/umap
---

# umap-learn

<!-- AUTO:BANDEAU:START -->
> Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation de référence d'**UMAP** — *Uniform Manifold Approximation and Projection* —,
réduction de dimension non linéaire fondée sur l'apprentissage de variété. Elle construit un
graphe de voisinage flou en haute dimension, puis l'optimise en basse dimension. Elle préserve
mieux la structure globale que t-SNE et tourne nettement plus vite, cœur Numba et recherche de
voisins par pynndescent à l'appui. Elle sert autant à la visualisation 2-3D qu'au
pré-traitement vers k dimensions, en API scikit-learn (`fit_transform`), avec `transform` sur
données nouvelles et un mode supervisé ou semi-supervisé. Deux réglages commandent tout :
`n_neighbors`, l'équilibre local/global, et `min_dist`, la compacité des amas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualiser en 2-3D des données à haute dimension — embeddings, single-cell, images — en gardant des amas lisibles | Le paquet PyPI s'appelle `umap-learn` mais le module s'importe `umap`, à ne pas confondre avec le paquet `umap`, sans rapport |
| Réduire la dimension avant un clustering, dans le pipeline UMAP → HDBSCAN | Les distances et les tailles d'amas dans la projection ne sont pas quantitativement fiables : ne pas les sur-interpréter |
| Projeter de nouveaux points après apprentissage, via `transform` — ce que t-SNE ne fait pas nativement | Résultat stochastique : fixer `random_state` pour la reproductibilité, au prix du parallélisme |
| Réduction supervisée, guidée par les labels, pour mieux séparer des classes | Réduction linéaire interprétable — axes, variance expliquée → [[PCA]] |

## Mise en œuvre

- Installation — `uv add umap-learn` ; le module s'importe `umap`
- Point d'entrée — l'API scikit-learn : `fit_transform`, puis `transform` sur données nouvelles
- Prérequis — NumPy et scikit-learn ; Numba, dont la compilation JIT rend la première exécution lente
- Exécution — single-node, en mémoire ; rien à héberger
- Coût — BSD-3-Clause, gratuit

## Écosystème

### Alternatives

- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
- [[PaCMAP]] — Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable.

### Compléments

- [[hdbscan]] — Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster). — le clustering en aval du pipeline UMAP → HDBSCAN

## Ressources

- Documentation — https://umap-learn.readthedocs.io/
- Dépôt — https://github.com/lmcinnes/umap

## Voir aussi

- [[Réduction de dimension]] — la notion chapeau ; UMAP est de la famille manifold
- [[t-SNE and UMAP]] — la notion : réduction non linéaire pour la visualisation
- [[Comparatif - Réduction de dimension]] — ce qui départage les méthodes du dossier
