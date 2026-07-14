---
galaxie: wiki
type: concept
nom: GPA
alias: [Generalized Procrustes Analysis, Analyse procustéenne généralisée, Procruste généralisé]
categorie: concept/stats
domaines: [data-sci]
tags: [factor-analysis, dimensionality-reduction]
---

# GPA

## Aperçu

- Generalized Procrustes Analysis : superpose plusieurs **configurations** de points décrivant les mêmes individus, pour en extraire une configuration consensus.
- Élimine les différences d'origine, d'orientation et d'échelle qui ne portent pas d'information.

## Concepts clés

### Les transformations autorisées
- Translation, rotation, réflexion, mise à l'échelle (homothétie) — pas de déformation.
- Chaque configuration est ajustée pour coller au mieux aux autres.

### Consensus
- La configuration consensus est obtenue itérativement : ajuster chaque configuration sur le consensus courant, recalculer le consensus, répéter.
- Le résidu mesure le désaccord entre configurations.

### Origine : le profil libre
- Conçu pour l'analyse sensorielle (free-choice profiling) : plusieurs juges notent des produits avec leurs propres descripteurs.

## Les maths, simplement

- $m$ configurations $X_1,\dots,X_m$ (mêmes lignes). On minimise $\sum_{k} \lVert T_k(X_k) - \bar{X} \rVert^2$.
- $T_k$ = translation + transformation orthogonale (rotation / réflexion) + facteur d'échelle ; $\bar{X}$ = consensus (moyenne des configurations ajustées).
- Résolu par alternance (ajustement procustéen puis recalcul du consensus), souvent suivi d'une [[PCA]] du consensus pour le visualiser.

## En pratique

- Entrée = plusieurs tableaux décrivant les mêmes individus dans des espaces comparables.
- Proche de la logique [[MFA]] (confronter des groupes), mais centré sur la géométrie plutôt que la pondération.
- À ne pas confondre avec l'analyse procustéenne des formes (morphométrie) : même algèbre, autre usage.
- Outils : `prince.GPA`, `FactoMineR::GPA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille.
- [[PCA]] — appliquée au consensus pour le représenter.
- [[MFA]] — autre approche de plusieurs groupes / configurations (pondération plutôt que superposition).

## Pour aller plus loin

- Gower (1975), *Generalized Procrustes Analysis*, Psychometrika 40(1).
