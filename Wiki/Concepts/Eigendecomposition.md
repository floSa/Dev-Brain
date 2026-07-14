---
galaxie: wiki
type: concept
nom: Eigendecomposition
alias: [décomposition spectrale, diagonalisation, valeurs propres, vecteurs propres, eigenvalue decomposition, EVD]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra, matrix-decomposition, eigenvalue]
---

# Eigendecomposition

## Aperçu

- Trouver les directions $v$ qu'une matrice carrée $A$ se contente d'étirer sans tourner : $Av = \lambda v$. $v$ est un **vecteur propre**, $\lambda$ une **valeur propre**.
- Dans la base de ces directions, la transformation devient une simple mise à l'échelle (matrice diagonale) — d'où « diagonaliser ».

## Concepts clés

### Valeurs et vecteurs propres
- $Av = \lambda v$ : $A$ agit comme une dilatation de facteur $\lambda$ le long de $v$.
- Les $\lambda$ sont les racines du polynôme caractéristique $\det(A - \lambda I) = 0$. Leur somme = trace, leur produit = déterminant.

### Diagonalisation
- $A = Q \Lambda Q^{-1}$ : colonnes de $Q$ = vecteurs propres, $\Lambda$ diagonale des valeurs propres.
- Rend les puissances triviales : $A^k = Q \Lambda^k Q^{-1}$ (utile pour les [[Chaînes de Markov]], PageRank, systèmes dynamiques).

### Cas symétrique — le théorème spectral
- Si $A$ est symétrique (réelle), ses vecteurs propres sont **orthogonaux** et $A = Q\Lambda Q^\top$ avec $Q$ orthogonale. Valeurs propres toutes réelles.
- C'est exactement le cas des matrices de covariance → fondement algébrique de la [[PCA]].

### Quand ça n'existe pas
- Une matrice non symétrique peut être non diagonalisable (valeurs propres répétées sans assez de vecteurs propres). La [[SVD]] n'a jamais ce défaut → on lui préfère souvent la SVD.

## Les maths, simplement

- Équation centrale : $A v = \lambda v$, soit $(A - \lambda I)v = 0$ avec $v \neq 0$, ce qui impose $\det(A-\lambda I)=0$.
- Forme factorisée : $A = Q \Lambda Q^{-1}$ (et $Q^{-1}=Q^\top$ si $A$ symétrique).
- Signe des $\lambda$ : tous $> 0$ ⇔ matrice définie positive ; informe sur la courbure (cf. points-selles en optimisation, matrice hessienne).

## En pratique

- Réservé aux matrices **carrées** ; pour le reste ou pour la robustesse numérique, passer par la [[SVD]].
- Sur une covariance symétrique, `numpy.linalg.eigh` (variante symétrique) est plus rapide et stable que `eig`.
- Trier les $\lambda$ par ordre décroissant pour lire l'importance des axes (PCA, spectral clustering).
- Outils : `numpy.linalg.eig` / `eigh`, `scipy.linalg.eig`, [[Dev/Services/numpy|numpy]], [[Dev/Services/Scikit-Learn|sklearn]] (PCA, SpectralClustering).

## Approches voisines & alternatives

- [[SVD]] — la généralisation à toute matrice ; pour une matrice symétrique SPD, SVD et eigendecomposition coïncident.
- [[PCA]] — application directe : diagonaliser la matrice de covariance des données.
- [[Matrix decompositions]] — la famille des factorisations dont c'est la version spectrale.
- [[Matrix products]] — diagonaliser, c'est trouver la base où le produit devient une mise à l'échelle.

## Pour aller plus loin

- Strang — *Introduction to Linear Algebra*, ch. 6.
- Spectral clustering, PageRank, analyse de stabilité — applications classiques du spectre.
- Méthode de la puissance itérée : calcul de la plus grande valeur propre sans décomposer.
