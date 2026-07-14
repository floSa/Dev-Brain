---
galaxie: wiki
type: concept
nom: Matrix decompositions
alias: [factorisation matricielle, décompositions matricielles, matrix factorization]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra, matrix-decomposition]
---

# Matrix decompositions

## Aperçu

- Factoriser une matrice $A$ en produit de facteurs structurés (triangulaires, orthogonaux, diagonaux) pour résoudre vite et de façon stable systèmes, moindres carrés et inversions.
- Principe directeur : **ne jamais inverser une matrice** ; décomposer puis résoudre par substitution est plus rapide et numériquement plus sûr.

## Concepts clés

### LU — résolution de systèmes
- $A = LU$ ($L$ triangulaire inférieure, $U$ supérieure), avec pivotage $PA = LU$ pour la stabilité.
- Sert à résoudre $Ax = b$ et à calculer $\det A$. C'est l'élimination de Gauss, mémorisée une fois pour plusieurs seconds membres.

### QR — moindres carrés et bases orthonormées
- $A = QR$ ($Q$ à colonnes orthonormées, $R$ triangulaire supérieure).
- Résout les moindres carrés $\min \|Ax-b\|$ sans former $A^\top A$ (qui dégrade le conditionnement). Issu de Gram-Schmidt ou des réflexions de Householder. Lien direct avec les [[Projections]].

### Cholesky — matrices symétriques définies positives
- $A = L L^\top$, deux fois plus rapide que LU, réservé aux matrices SPD (matrices de covariance, systèmes normaux).
- Échoue si la matrice n'est pas définie positive — utile aussi comme test de positivité.

### Les deux décompositions spectrales
- [[Eigendecomposition]] — $A = Q\Lambda Q^{-1}$, pour les matrices carrées (analyse de transformations, PCA via la covariance).
- [[SVD]] — $A = U\Sigma V^\top$, pour **toute** matrice (rectangulaire incluse) : la décomposition la plus générale et la plus stable.

## Les maths, simplement

- Idée commune : remplacer $A$ par des facteurs où résoudre est immédiat (triangulaire → substitution ; orthogonal → transposée = inverse ; diagonal → division terme à terme).
- Choisir selon la structure : carrée quelconque → LU ; rectangulaire / moindres carrés → QR ; SPD → Cholesky ; analyse spectrale → eigendecomposition ; cas général / robustesse → SVD.
- Le **conditionnement** $\kappa(A)$ gouverne la propagation d'erreur ; les méthodes orthogonales (QR, SVD) le préservent, les méthodes via $A^\top A$ le carrent.

## En pratique

- Résoudre $Ax=b$ plusieurs fois avec le même $A$ : factoriser une fois (`scipy.linalg.lu_factor`), réutiliser.
- SPD connue (covariance) → Cholesky ; jamais `inv(A)` puis produit.
- Outils : `numpy.linalg` (`solve`, `qr`, `cholesky`, `eig`, `svd`), `scipy.linalg` (versions LAPACK plus complètes), [[Dev/Services/numpy|numpy]].

## Approches voisines & alternatives

- [[Eigendecomposition]] — la factorisation spectrale des matrices carrées.
- [[SVD]] — la généralisation à toute matrice, socle de la réduction de dimension.
- [[Matrix products]] — l'opération que ces factorisations cherchent à éviter de répéter.
- [[Projections]] — QR fournit la base orthonormée qui rend la projection triviale.

## Pour aller plus loin

- Golub & Van Loan — *Matrix Computations* (la référence).
- Trefethen & Bau — *Numerical Linear Algebra*.
- Factorisations non négatives (NMF) et creuses : variantes orientées interprétabilité / scalabilité.
