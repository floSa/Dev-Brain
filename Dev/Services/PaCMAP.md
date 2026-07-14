---
galaxie: dev
type: service
nom: PaCMAP
alias: [pacmap, Pairwise Controlled Manifold Approximation]
pitch: "Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/umap-learn|umap-learn]]"]
remplace_par: []
status: actif
tags: [dimensionality-reduction, manifold, unsupervised]
url_docs: https://github.com/YingfanWang/PaCMAP
url_repo: https://github.com/YingfanWang/PaCMAP
---

# PaCMAP

## Pourquoi

Méthode de [[Réduction de dimension]] **non linéaire** (PaCMAP — *Pairwise Controlled Manifold Approximation*) conçue pour préserver **à la fois** la structure locale **et** la structure globale, là où [[t-SNE and UMAP|t-SNE et UMAP]] privilégient le voisinage local. Son ressort : trois familles de paires (voisins, **mid-near**, lointaines) dont les poids évoluent au fil de l'optimisation — on capte d'abord la forme d'ensemble, puis on affine le local. Résultat plus robuste au choix d'hyperparamètres et fidèle à la topologie globale (membre récent de la famille manifold, après t-SNE, LargeVis et UMAP).

## Quand l'utiliser

- Visualiser en 2-3D en gardant une **structure globale** crédible (positions relatives des amas, pas seulement des grappes locales).
- Données à haute dimension où la disposition d'ensemble compte (embeddings, single-cell, trajectoires).
- Alternative quand t-SNE/UMAP donnent des amas trop éclatés ou trop sensibles aux réglages.
- Projeter de nouveaux points (`transform`) après apprentissage, comme UMAP.

## Quand NE PAS l'utiliser

- Choix par défaut éprouvé, gros écosystème et nombreuses intégrations → [[Dev/Services/umap-learn|umap-learn]].
- Réduction **linéaire** interprétable (axes, variance expliquée) → [[PCA]] via [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- Référence visuelle purement locale bien documentée → t-SNE (`sklearn.manifold`).

## Déploiement & coût

- Bibliothèque Python (`uv add pacmap`, ou conda-forge). Rien à héberger.
- Single-node, en mémoire ; recherche de voisins via Annoy, optimisation accélérée par Numba.
- Apache-2.0, gratuit. API proche de scikit-learn (`fit_transform`).

## Pièges

- Moins mature et moins répandu qu'UMAP : écosystème et intégrations plus restreints, API encore < 1.0.
- Comme tout manifold : **distances et tailles d'amas** dans la projection ne sont pas quantitativement fiables.
- Stochastique : fixer la graine pour la reproductibilité ; standardiser et, sur très haute dimension, pré-réduire par [[PCA]].

## Alternatives

- [[Dev/Services/umap-learn|umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.

## Liens

- [[Dev/Patterns/Comparatif - Réduction de dimension]] — PCA / t-SNE / UMAP / PaCMAP.
- Concept : [[t-SNE and UMAP]] — la branche non linéaire pour la viz ; page chapeau [[Réduction de dimension]] (famille manifold).
- [[Dev/Services/umap-learn|umap-learn]] — la référence dont PaCMAP est l'alternative orientée structure globale.
- Doc : https://github.com/YingfanWang/PaCMAP
