---
galaxie: wiki
type: concept
nom: Matrix products
alias: [produit matriciel, multiplication matricielle, matrix multiplication, produit matrice-vecteur]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra]
---

# Matrix products

## Aperçu

- Le produit matriciel compose des **applications linéaires** : appliquer $A$ puis $B$ revient à appliquer la matrice unique $BA$.
- Brique de calcul de tout le ML : une couche dense, c'est $W x + b$ ; un batch, c'est un produit matrice-matrice. Le coût se concentre ici, d'où les GPU et les BLAS.

## Concepts clés

### Produit scalaire (dot product)
- Entre deux vecteurs : $x^\top y = \sum_i x_i y_i$. Mesure l'alignement (cf. similarité cosinus, base des [[embeddings]]).
- Nul ⇔ vecteurs orthogonaux. C'est la pierre angulaire des [[Projections]] et des [[Vector norms]] ($\|x\|_2^2 = x^\top x$).

### Produit matrice-vecteur
- $A x$ = combinaison linéaire des colonnes de $A$, pondérée par les composantes de $x$. C'est l'image de $x$ par la transformation $A$.
- Lecture duale : chaque composante de $Ax$ est un produit scalaire entre une ligne de $A$ et $x$.

### Produit matrice-matrice
- $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ : ligne $i$ de $A$ contre colonne $j$ de $B$. Compatibilité des dimensions : $(m\times n)(n\times p) = (m\times p)$.
- Interprétation : composition de deux transformations linéaires.

### Propriétés à ne pas confondre
- **Non commutatif** : $AB \neq BA$ en général (l'ordre des transformations compte).
- Associatif et distributif : $A(BC)=(AB)C$, $A(B+C)=AB+AC$. L'ordre de parenthésage change le coût, pas le résultat.
- Transposée : $(AB)^\top = B^\top A^\top$.
- À distinguer du **produit de Hadamard** $A \odot B$ (terme à terme) et du produit de Kronecker, qui ne sont pas des compositions.

## Les maths, simplement

- Forme générale : $C = AB$ avec $C_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}$.
- Géométrie : une matrice carrée déforme l'espace (rotation, mise à l'échelle, cisaillement) ; le déterminant $\det A$ donne le facteur de dilatation des volumes, nul ⇔ matrice singulière.
- Coût naïf : $O(mnp)$, soit $O(n^3)$ pour deux matrices $n\times n$ — d'où l'intérêt des décompositions ([[Matrix decompositions]]) qui évitent de recalculer ces produits.

## En pratique

- Vectoriser : un produit matriciel via BLAS bat toujours une boucle Python explicite. `A @ B`, `numpy.matmul`, `torch.matmul`.
- En deep learning, les produits sont *batchés* (tenseurs 3D+) ; surveiller l'ordre des dimensions et le broadcasting.
- Parenthéser malin : pour $A x$ avec $A = UV$ (rang faible), calculer $U(Vx)$ et non $(UV)x$ économise des ordres de grandeur.
- Outils : [[Dev/Services/numpy|numpy]] (`@`, `numpy.linalg`), [[Dev/Services/PyTorch|torch]] (`torch.matmul`, `einsum`).

## Approches voisines & alternatives

- [[Matrix decompositions]] — factoriser une matrice pour résoudre systèmes et moindres carrés sans inverser.
- [[Vector norms]] — le produit scalaire d'un vecteur avec lui-même donne sa norme.
- [[Projections]] — projeter, c'est un produit par une matrice idempotente $P$.
- [[Eigendecomposition]] — diagonaliser rend le produit trivial dans la bonne base.

## Pour aller plus loin

- Strang — *Introduction to Linear Algebra*, ch. 1-2.
- BLAS / LAPACK : la couche bas niveau derrière `numpy` et `torch`.
- Algorithmes sous-cubiques (Strassen, Coppersmith-Winograd) — théoriques, rarement utilisés en pratique.
