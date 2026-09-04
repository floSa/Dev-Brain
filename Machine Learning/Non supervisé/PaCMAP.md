---
role: brique
nom: PaCMAP
alias: [pacmap, Pairwise Controlled Manifold Approximation]
pitch: "Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable."
categorie: ml/non-supervise
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[umap-learn]]"]
complements: []
tags: [dimensionality-reduction, manifold, unsupervised]
url_docs: https://github.com/YingfanWang/PaCMAP
url_repo: https://github.com/YingfanWang/PaCMAP
---

# PaCMAP

<!-- AUTO:BANDEAU:START -->
> Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Méthode de réduction de dimension non linéaire — *Pairwise Controlled Manifold
Approximation* — conçue pour préserver **à la fois** la structure locale **et** la structure
globale, là où t-SNE et UMAP privilégient le voisinage local. Son ressort tient à trois
familles de paires — voisins, **mid-near**, lointaines — dont les poids évoluent au fil de
l'optimisation : la forme d'ensemble se capte d'abord, le local s'affine ensuite. Le résultat
est plus robuste au choix des hyperparamètres et plus fidèle à la topologie globale. C'est le
membre le plus récent de la famille manifold, après t-SNE, LargeVis et UMAP.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualiser en 2-3D en gardant une structure globale crédible : les positions relatives des amas, pas seulement les grappes locales | Comme pour tout manifold, les distances et les tailles d'amas dans la projection ne sont pas quantitativement fiables : ne pas les sur-interpréter |
| Données à haute dimension où la disposition d'ensemble compte : embeddings, single-cell, trajectoires | Résultat stochastique : fixer la graine, sans quoi deux exécutions ne donnent pas la même figure |
| Cas où t-SNE ou UMAP donnent des amas trop éclatés, ou trop sensibles aux réglages | Très haute dimension : standardiser et pré-réduire par [[PCA]] avant, sinon la projection se dégrade |
| Projeter de nouveaux points après apprentissage, via `transform` | |

## Mise en œuvre

- Installation — `uv add pacmap`, ou conda-forge
- Point d'entrée — une API proche de scikit-learn : `fit_transform`, puis `transform` sur données nouvelles
- Prérequis — NumPy ; recherche de voisins par Annoy, optimisation accélérée par Numba
- Exécution — single-node, en mémoire ; rien à héberger
- Coût — Apache-2.0, gratuit

## Écosystème

### Alternatives

- [[umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.

## Ressources

- Documentation — https://github.com/YingfanWang/PaCMAP

## Voir aussi

- [[Réduction de dimension]] — la notion chapeau ; PaCMAP est de la famille manifold
- [[t-SNE and UMAP]] — la branche non linéaire pour la visualisation
- [[Comparatif - Réduction de dimension]] — ce qui départage les méthodes du dossier
