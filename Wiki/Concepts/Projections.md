---
galaxie: wiki
type: concept
nom: Projections
alias: [projection orthogonale, projecteur, projection]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra, projection]
---

# Projections

## Aperçu

- Projeter un vecteur $b$ sur un sous-espace, c'est trouver le point de ce sous-espace **le plus proche** de $b$ (au sens de la distance L2).
- Idée centrale derrière les moindres carrés, la [[PCA]] et la [[Réduction de dimension]] : remplacer un vecteur par sa meilleure approximation dans un espace plus petit.

## Concepts clés

### Projection sur une droite
- Sur la direction $a$ : $p = \dfrac{a^\top b}{a^\top a}\, a$. Le résidu $b - p$ est orthogonal à $a$ — c'est ce qui rend $p$ optimal.

### Matrice de projection
- Sur le sous-espace engendré par les colonnes de $A$ : $P = A(A^\top A)^{-1}A^\top$, et $p = Pb$.
- **Idempotente** : $P^2 = P$ (projeter deux fois ne change rien) et symétrique ($P^\top = P$) pour une projection orthogonale.

### Moindres carrés = projection
- $\min_x \|Ax - b\|_2$ revient à projeter $b$ sur l'espace des colonnes de $A$ ; la solution vérifie les équations normales $A^\top A\,x = A^\top b$.
- Numériquement, on ne forme pas $A^\top A$ (conditionnement) : on passe par la décomposition [[Matrix decompositions|QR]] ou la [[SVD]].

### Orthogonalité et bases
- Avec une base **orthonormée** $\{q_i\}$, la projection se réduit à une somme de produits scalaires : $p = \sum_i (q_i^\top b)\, q_i$ — plus d'inverse à calculer.
- Gram-Schmidt construit une telle base ; c'est ce que fournit la factorisation QR.

## Les maths, simplement

- Projecteur orthogonal : $P = A(A^\top A)^{-1}A^\top$, avec $P^2=P=P^\top$.
- Décomposition : tout $b$ s'écrit $b = Pb + (I-P)b$, partie dans le sous-espace + partie orthogonale (le résidu). $(I-P)$ projette sur le complément orthogonal.
- Lien PCA : projeter les données sur les premiers axes principaux (vecteurs propres de la covariance) minimise l'erreur de reconstruction — c'est la même optimalité que la troncature [[SVD]].

## En pratique

- Régression linéaire = projection des $y$ sur l'espace des features ; les valeurs ajustées $\hat{y} = Hy$ utilisent la *hat matrix* $H = P$ (cf. [[Régression linéaire]]).
- Pour projeter de façon stable, utiliser une base orthonormée (QR) plutôt que $(A^\top A)^{-1}$.
- Réduire la dimension = projeter sur un sous-espace bien choisi (axes principaux).
- Outils : `numpy.linalg.lstsq` (moindres carrés sans inverser), `numpy.linalg.qr`, [[Dev/Services/numpy|numpy]].

## Approches voisines & alternatives

- [[Vector norms]] — la projection minimise la distance L2 au sous-espace.
- [[Matrix products]] — un projecteur est une matrice idempotente appliquée par produit.
- [[SVD]] — fournit des bases orthonormées et la projection de rang faible optimale.
- [[Matrix decompositions]] — QR donne la base orthonormée qui rend la projection immédiate.

## Pour aller plus loin

- Strang — *Introduction to Linear Algebra*, ch. 4 (projections et moindres carrés).
- Théorème de projection dans les espaces de Hilbert : la même idée en dimension infinie.
