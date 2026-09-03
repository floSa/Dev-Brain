---
role: hub
nom: Mathématiques
alias: [maths, mathématiques appliquées]
pitch: Les quatre socles mathématiques sur lesquels le ML repose — algèbre linéaire, optimisation, théorie de l'information, théorie de l'apprentissage.
domaines: [ml-eng, data-sci]
tags: [linear-algebra, optimization, information-theory, learning-theory, linear-programming]
---

# Mathématiques

> Les quatre socles mathématiques sur lesquels le ML repose — algèbre linéaire, optimisation, théorie de l'information, théorie de l'apprentissage.

## Ce qu'il faut comprendre

- Ce domaine est presque entièrement fait de **notions**, et c'est normal : les mathématiques ne s'installent pas. Sa seule brique est un solveur ([[PuLP]]), parce que l'optimisation discrète est la seule des quatre familles qu'on délègue à un logiciel dédié plutôt qu'à la bibliothèque de calcul qui l'emploie. Elle vit donc dans [[Optimisation]], et le domaine n'a plus aucune page à son propre niveau.
- **La dépendance à retenir entre les quatre sous-dossiers**, et c'est le seul plan à mémoriser : l'[[Optimisation]] cherche un minimum, la [[Théorie de l'information]] fournit la fonction à minimiser, l'[[Algèbre linéaire]] fournit la représentation sur laquelle on calcule, la [[Théorie de l'apprentissage]] dit ce que ce minimum vaut hors de l'échantillon.
- **[[Algèbre linéaire]]** — le langage dans lequel les données et les modèles sont écrits : normes, produits, projections, décompositions. Toute réduction de dimension, tout embedding, tout changement de repère est une décomposition.
- **[[Optimisation]]** — comment un modèle apprend, et la recherche opérationnelle avec. Le dossier se coupe en deux : le continu (descente de gradient, convexité, courbure, pas d'apprentissage) qu'on écrit dans le code d'entraînement, et le discret (contraintes, combinatoire, MIP) qu'on modélise et qu'on confie à un solveur.
- **[[Théorie de l'information]]** — comment on mesure l'incertitude et l'écart entre deux distributions. C'est de là que sort la perte de toute classification, et la plupart des critères qui comparent deux lois.
- **[[Théorie de l'apprentissage]]** — pourquoi la généralisation est possible. Ces bornes sont trop lâches pour dimensionner quoi que ce soit en pratique ; leur intérêt est de dire **de quoi** dépend la généralisation.
- **Ce qui n'est PAS ici, et pourquoi** : la **probabilité** est rangée en [[Probabilités]], sous « Statistiques & inférence », parce que ces pages se justifient toutes par l'inférence — les quatre piliers de ce domaine sont ceux ci-dessus, pas la probabilité. Et l'**analyse factorielle** ([[PCA]], [[Analyse factorielle]]) est là-bas aussi : ici on range la décomposition, là-bas la méthode qui l'applique à un tableau de données.

## Choisir

- Comprendre pourquoi un entraînement ne converge pas → [[Optimisation]].
- Un programme linéaire ou en nombres entiers à résoudre en Python → [[PuLP]], qui délègue à CBC, HiGHS, Gurobi ou CPLEX.
- Une optimisation continue, non linéaire, dans du code numérique → [[scipy.stats|SciPy]] et son module `optimize`, pas ce domaine.
- Choisir une perte, comparer deux distributions → [[Théorie de l'information]].
- Résoudre un système, décomposer une matrice, choisir une norme → [[Algèbre linéaire]].
- Savoir ce qu'une erreur d'entraînement garantit — ou pas → [[Théorie de l'apprentissage]].
- Réduire la dimension → [[SVD]] pour la mécanique, [[PCA]] pour la méthode, [[Réduction de dimension]] pour le panorama.
- Les outils qui appliquent tout ça → [[Machine Learning]] et [[Statistiques & inférence]].

<!-- AUTO:START -->
### Sous-domaines
- [[Algèbre linéaire]] · [[Optimisation]] · [[Théorie de l'apprentissage]] · [[Théorie de l'information]]
<!-- AUTO:END -->
