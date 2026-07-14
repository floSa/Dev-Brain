---
galaxie: wiki
type: concept
nom: CA
alias: [AFC, Analyse des correspondances, Analyse factorielle des correspondances, Correspondence Analysis]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis]
---

# CA

## Aperçu

- Analyse factorielle d'une **table de contingence** : visualise les associations entre les modalités de deux variables qualitatives.
- Transpose l'idée de la [[PCA]] à des profils de fréquences, avec la distance du khi-deux.

## Concepts clés

### Profils lignes et colonnes
- Chaque ligne / colonne est ramenée à un profil (fréquences conditionnelles).
- CA projette simultanément profils-lignes et profils-colonnes dans un même plan.

### Distance du khi-deux
- La distance entre deux profils est pondérée par l'inverse de la fréquence marginale → une modalité rare n'est pas négligeable.
- Inertie totale = statistique du khi-deux / effectif total ($\Phi^2$).

### Biplot et proximités
- Deux modalités de variables différentes proches = associées (sur-représentation).
- La proximité ligne–colonne se lit via la relation barycentrique, pas comme une distance directe brute.

## Les maths, simplement

- Table de fréquences $P = N / n$, marges $r$ (lignes), $c$ (colonnes).
- Résidus standardisés $S = D_r^{-1/2}(P - r c^\top) D_c^{-1/2}$, avec $D_r, D_c$ diagonales des marges.
- SVD de $S$ → axes factoriels. Inertie totale $= \sum_j \lambda_j = \Phi^2 = \chi^2 / n$.

## En pratique

- Entrée = table de contingence (croisement de deux variables qualitatives), pas les données brutes.
- À relier au [[Test du khi-deux]] : CA décompose le khi-deux en axes interprétables.
- Modalités très rares → inertie instable ; les regrouper si besoin.
- Outils : `prince.CA`, `FactoMineR::CA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille.
- [[PCA]] — même esprit, mais pour des quantitatives.
- [[MCA]] — la généralisation à plus de deux variables qualitatives.
- [[Test du khi-deux]] — CA en est la lecture géométrique.

## Pour aller plus loin

- Benzécri (analyse des correspondances) ; Greenacre — *Correspondence Analysis in Practice*.
