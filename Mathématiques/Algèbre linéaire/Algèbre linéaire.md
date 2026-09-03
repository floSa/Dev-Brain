---
role: hub
nom: Algèbre linéaire
alias: [linear algebra, calcul matriciel, décompositions matricielles]
pitch: Le langage dans lequel les données et les modèles sont écrits — normes, produits, projections, et les décompositions qui rendent tout le reste calculable.
domaines: [data-sci, ml-eng]
tags: [linear-algebra, matrix-decomposition, eigenvalue, vector-norm, projection]
---

# Algèbre linéaire

> Le langage dans lequel les données et les modèles sont écrits — normes, produits, projections, et les décompositions qui rendent tout le reste calculable.

## Ce qu'il faut comprendre

- **Ce dossier porte des objets et leurs propriétés, pas des méthodes.** [[SVD]] est la factorisation $A = U\Sigma V^\top$ ; [[PCA]] est la méthode d'analyse de données qui l'emploie, et elle vit dans [[Analyse factorielle]]. La frontière est celle-là et elle est nette : on range ici ce qui est vrai de toute matrice, là-bas ce qu'on en fait sur un tableau de données.
- **Deux pages disent ce qui coûte cher, et le reste en découle.** [[Matrix products]] est le seul endroit où le calcul se concentre — une couche dense est $Wx + b$, un batch est un produit matrice-matrice, et c'est pour ce produit-là qu'existent les GPU et les BLAS. [[Vector norms]] décide de tout ce qui se mesure : la perte (L2 = MSE), la régularisation (L1 = Lasso), les distances, le clipping de gradient. Changer de norme change le modèle, pas seulement l'échelle.
- **La règle de calcul à retenir : ne jamais inverser une matrice.** [[Matrix decompositions]] explique pourquoi — décomposer en facteurs structurés (triangulaires, orthogonaux, diagonaux) puis résoudre par substitution est à la fois plus rapide et numériquement plus sûr que former $A^{-1}$.
- **Les deux décompositions ne se recouvrent pas.** [[Eigendecomposition]] cherche les directions qu'une matrice **carrée** étire sans tourner ($Av = \lambda v$) ; [[SVD]] existe pour **toute** matrice, même rectangulaire, et c'est la plus stable — d'où son rôle de socle commun à la compression, au pseudo-inverse et à la recommandation.
- **[[Projections]] est le pont vers la réduction de dimension.** Projeter, c'est remplacer un vecteur par le point le plus proche d'un sous-espace : les moindres carrés, la PCA et toute [[Réduction de dimension|réduction de dimension]] sont ce même geste, à la base près.

## Choisir

- Comprendre ce que coûte un modèle en calcul → [[Matrix products]].
- Choisir une perte, une régularisation ou une distance → [[Vector norms]].
- Résoudre un système ou des moindres carrés sans exploser numériquement → [[Matrix decompositions]].
- Une matrice carrée, une dynamique, une puissance de matrice → [[Eigendecomposition]].
- Une matrice rectangulaire, une compression, un pseudo-inverse → [[SVD]].
- Approximer un vecteur dans un espace plus petit → [[Projections]].
- Appliquer tout ça à un tableau de données pour en interpréter les axes → [[Analyse factorielle]], pas ce dossier.
- Le calculer en Python → [[numpy]], au dossier [[DataFrames]].

<!-- AUTO:START -->
### Notions
- [[Eigendecomposition]] — domaines : data-sci, ml-eng
- [[Matrix decompositions]] — domaines : data-sci, ml-eng
- [[Matrix products]] — domaines : data-sci, ml-eng
- [[Projections]] — domaines : data-sci, ml-eng
- [[SVD]] — domaines : data-sci, ml-eng
- [[Vector norms]] — domaines : data-sci, ml-eng
<!-- AUTO:END -->
