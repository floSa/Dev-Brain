---
role: hub
nom: Mathématiques
alias: [maths, mathématiques appliquées]
pitch: Les quatre socles mathématiques sur lesquels le ML repose — algèbre linéaire, optimisation, théorie de l'information, théorie de l'apprentissage.
domaines: [ml-eng, data-sci]
tags: [linear-algebra, optimization, information-theory, linear-programming]
---

# Mathématiques

> Les quatre socles mathématiques sur lesquels le ML repose — algèbre linéaire, optimisation, théorie de l'information, théorie de l'apprentissage.

## Ce qu'il faut comprendre

- Ce domaine est presque entièrement fait de **notions**, et c'est normal : les mathématiques ne s'installent pas. Sa seule brique est un solveur ([[PuLP]]), parce que l'optimisation discrète est la seule des quatre familles qu'on délègue à un logiciel dédié plutôt qu'à la bibliothèque de calcul qui l'emploie.
- **Algèbre linéaire** — le langage dans lequel les données et les modèles sont écrits. [[Vector norms]] et [[Matrix products]] pour la mécanique de base ; [[Matrix decompositions]], [[SVD]], [[Eigendecomposition]] et [[Projections]] pour ce qui la rend utile : toute réduction de dimension, tout embedding, tout changement de repère est une décomposition.
- **Optimisation** — comment un modèle apprend. [[Gradient descent]] est le mécanisme ; [[Convexity]] dit quand il garantit quelque chose, et le [[Loss landscape and saddle points|paysage de perte]] dit pourquoi il n'en garantit rien en profond. [[Newton & quasi-Newton]] exploite la courbure quand on peut se le payer, [[Learning rate schedules]] est le réglage qui décide le plus souvent du résultat. La branche discrète est à part : [[Optimisation sous contrainte]], [[Optimisation combinatoire]], [[Programmation linéaire en nombres entiers (MIP)]] — c'est là que [[PuLP]] intervient.
- **Théorie de l'information** — comment on mesure l'incertitude et l'écart entre deux distributions. [[Shannon entropy]] est l'unité de compte ; [[Cross-entropy]] est la fonction de perte de toute classification ; [[KL divergence]], [[Jensen-Shannon divergence]], [[Mutual information]] mesurent des écarts et des dépendances. [[Optimal transport]] et [[Wasserstein distance]] répondent au cas que la KL traite mal : deux distributions à supports disjoints.
- **Théorie de l'apprentissage** — pourquoi la généralisation est possible. [[PAC learning]], [[VC dimension]], [[Rademacher complexity]] et [[Generalization bounds]] bornent l'écart entre erreur d'entraînement et erreur réelle ; [[No Free Lunch theorem]] rappelle qu'aucun algorithme ne domine partout. Ces bornes sont trop lâches pour dimensionner quoi que ce soit en pratique — leur intérêt est de dire **de quoi** dépend la généralisation.
- La dépendance à retenir entre les quatre : l'optimisation cherche un minimum, la théorie de l'information fournit la fonction à minimiser, l'algèbre linéaire fournit la représentation sur laquelle on calcule, la théorie de l'apprentissage dit ce que ce minimum vaut hors de l'échantillon.

## Choisir

- Un programme linéaire ou en nombres entiers à résoudre en Python → [[PuLP]], qui délègue à CBC, HiGHS, Gurobi ou CPLEX.
- Une optimisation continue, non linéaire, dans du code numérique → [[scipy.stats|SciPy]] et son module `optimize`, pas ce domaine.
- Comprendre pourquoi un entraînement ne converge pas → [[Gradient descent]], [[Learning rate schedules]], [[Loss landscape and saddle points]].
- Comparer deux distributions → [[KL divergence]] si les supports se recouvrent, [[Wasserstein distance]] sinon.
- Réduire la dimension → [[SVD]] pour la mécanique, [[PCA]] pour la méthode, [[Réduction de dimension]] pour le panorama.
- Les outils qui appliquent tout ça → [[Machine Learning]] et [[Statistiques & inférence]].

<!-- AUTO:START -->
### Briques
- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).

### Comparatifs
- [[Comparatif - Solveurs d'optimisation]]
<!-- AUTO:END -->
