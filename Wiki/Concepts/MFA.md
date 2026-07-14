---
galaxie: wiki
type: concept
nom: MFA
alias: [AFM, Analyse factorielle multiple, Multiple Factor Analysis]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis]
---

# MFA

## Aperçu

- Analyse factorielle de variables **structurées en groupes** (blocs), chaque groupe pouvant être quantitatif ou qualitatif.
- Équilibre les groupes pour qu'aucun ne pèse davantage du seul fait de sa taille.

## Concepts clés

### Pondération par groupe
- Chaque groupe subit d'abord son analyse séparée ([[PCA]] si quanti, [[MCA]] si quali).
- On divise chaque groupe par sa première valeur propre $\lambda_1$ → tous les groupes partagent la même inertie maximale de 1.

### Analyse globale
- PCA pondérée sur l'ensemble des groupes ainsi normalisés.
- Outils dédiés : coefficient RV entre groupes, configurations partielles (où chaque groupe place un même individu), graphe des groupes.

## Les maths, simplement

- $G$ groupes, tableau $X_g$ par groupe. Poids du groupe $g$ : $1/\lambda_1^{(g)}$ (première valeur propre de son analyse séparée).
- Analyse globale = PCA sur la concaténation $[\,X_1/\sqrt{\lambda_1^{(1)}}, \dots, X_G/\sqrt{\lambda_1^{(G)}}\,]$.
- Coefficient RV $\in [0,1]$ : proximité de structure entre deux groupes.

## En pratique

- Cas type : mêmes individus décrits par plusieurs blocs (capteurs, dates, thèmes d'enquête, panels sensoriels).
- Un seul groupe → revient à PCA / MCA / FAMD selon le type.
- Cousins : STATIS, AFM hiérarchique ; superposition de configurations → [[GPA]].
- Outils : `prince.MFA`, `FactoMineR::MFA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille.
- [[PCA]] — l'analyse globale de MFA en est une version pondérée.
- [[FAMD]] — cas mixte sans structure de groupes.
- [[GPA]] — autre façon de confronter plusieurs configurations.
- [[HCPC]] — clustering sur les composantes de la MFA.

## Pour aller plus loin

- Escofier & Pagès (1994), *Multiple factor analysis (AFMULT package)*.
