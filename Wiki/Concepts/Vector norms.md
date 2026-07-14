---
galaxie: wiki
type: concept
nom: Vector norms
alias: [normes vectorielles, normes, Lp norms, norme Lp]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra, vector-norm, regularization]
---

# Vector norms

## Aperçu

- Une norme $\|x\|$ mesure la « taille » d'un vecteur ; sa version sur une différence $\|x-y\|$ donne une **distance**.
- Le choix de la norme façonne tout en ML : la perte (MSE = L2), la régularisation (Lasso = L1), les distances (k-NN), le clipping de gradient.

## Concepts clés

### Les normes usuelles
- **L2 (euclidienne)** : $\|x\|_2 = \sqrt{\sum_i x_i^2}$. La longueur géométrique ; lisse, différentiable, dérive du produit scalaire $\|x\|_2^2 = x^\top x$.
- **L1 (Manhattan)** : $\|x\|_1 = \sum_i |x_i|$. Favorise la **parcimonie** (beaucoup de zéros) → sélection de variables.
- **L∞ (max)** : $\|x\|_\infty = \max_i |x_i|$. La plus grande composante.
- Généralisation $L_p$ : $\|x\|_p = \left(\sum_i |x_i|^p\right)^{1/p}$.

### Ce qui fait une norme
- Positivité ($\|x\|\geq 0$, nul ⇔ $x=0$), homogénéité ($\|\alpha x\| = |\alpha|\,\|x\|$), inégalité triangulaire ($\|x+y\|\leq\|x\|+\|y\|$).
- La « norme » L0 (nombre de coefficients non nuls) n'en est pas une (pas homogène) mais sert à parler de parcimonie.

### Normes matricielles
- **Frobenius** : $\|A\|_F = \sqrt{\sum_{ij} A_{ij}^2}$, la L2 vue sur les entrées.
- **Spectrale** : $\|A\|_2 = \sigma_{\max}$, la plus grande valeur singulière (cf. [[SVD]]) — gain maximal de la transformation.

## Les maths, simplement

- L1 vs L2 en régularisation : la boule L1 a des coins sur les axes → la solution contrainte y tombe → coefficients exactement nuls (Lasso) ; la boule L2 est ronde → coefficients petits mais non nuls (Ridge). Cf. [[Régularisation]].
- Distance dérivée : $d(x,y) = \|x-y\|$. La similarité cosinus n'est pas une norme mais s'appuie sur la L2 ($\cos\theta = \frac{x^\top y}{\|x\|_2\|y\|_2}$).
- Normaliser un vecteur : $\hat{x} = x/\|x\|_2$ le ramène sur la sphère unité (utile pour comparer des [[embeddings]]).

## En pratique

- Standardiser les variables avant toute méthode à base de distance (k-NN, k-means) : sinon une variable à grande échelle domine la norme.
- Régularisation : L2 par défaut (lisse, stable) ; L1 quand on veut un modèle parcimonieux / sélectionner.
- **Gradient clipping** par la norme L2 pour stabiliser l'entraînement de réseaux profonds.
- Outils : `numpy.linalg.norm` (paramètre `ord`), `torch.linalg.norm`, [[Dev/Services/numpy|numpy]], [[Dev/Services/PyTorch|torch]].

## Approches voisines & alternatives

- [[Régularisation]] — L1/L2 sur les coefficients sont des contraintes de norme.
- [[Projections]] — projeter, c'est trouver le point d'un sous-espace minimisant la distance L2.
- [[Matrix products]] — la norme L2 au carré est le produit scalaire d'un vecteur avec lui-même.
- [[SVD]] — la norme spectrale d'une matrice est sa plus grande valeur singulière.

## Pour aller plus loin

- Boyd & Vandenberghe — *Convex Optimization*, annexe A (normes et boules unité).
- Distances de Minkowski, Mahalanobis : généralisations utiles en clustering et détection d'anomalies.
