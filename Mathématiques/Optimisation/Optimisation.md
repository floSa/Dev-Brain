---
role: hub
nom: Optimisation
alias: [optimization, minimisation, recherche opérationnelle, programmation mathématique]
pitch: Minimiser une fonction — le mécanisme qui fait apprendre un modèle, les garanties qu'on a ou non, et la branche discrète qu'on délègue à un solveur.
domaines: [data-sci, ml-eng, ai-eng]
tags: [optimization, gradient-descent, convexity, second-order, learning-rate, linear-programming, combinatorial-optimization]
---

# Optimisation

> Minimiser une fonction — le mécanisme qui fait apprendre un modèle, les garanties qu'on a ou non, et la branche discrète qu'on délègue à un solveur.

## Ce qu'il faut comprendre

- **Le dossier se coupe en deux, et la ligne de coupe est le type de variable.** Le **continu** — [[Gradient descent]], [[Convexity]], [[Loss landscape and saddle points]], [[Newton & quasi-Newton]], [[Learning rate schedules]] — est ce qui fait apprendre un modèle ; on l'écrit dans le code d'entraînement. Le **discret** — [[Optimisation sous contrainte]], [[Optimisation combinatoire]], [[Programmation linéaire en nombres entiers (MIP)]] — est de la recherche opérationnelle ; on le modélise et on le confie à un solveur, et c'est là que [[PuLP]] intervient. Les deux moitiés partagent le mot « optimiser » et presque rien d'autre.
- **[[Convexity]] est la question à poser en premier**, parce qu'elle décide de la confiance à accorder au résultat : en convexe, tout minimum local est global et une descente converge sans se faire piéger. OLS, Ridge, Lasso, régression logistique et SVM sont convexes ; un réseau de neurones ne l'est pas.
- **En non convexe, l'obstacle n'est presque jamais le minimum local.** [[Loss landscape and saddle points]] le dit : en grande dimension ce sont les **points-selles** et les zones plates qui ralentissent, pas des cuvettes parasites. C'est ce qui explique pourquoi l'entraînement profond marche malgré l'absence de garantie.
- **Le premier ordre gagne par le coût, pas par la qualité.** [[Newton & quasi-Newton]] converge en beaucoup moins d'itérations en exploitant la courbure, mais chaque itération paie la hessienne — inabordable au-delà de quelques milliers de paramètres. [[Gradient descent]] ne demande que le gradient, que la différentiation automatique fournit gratuitement : c'est pour ça qu'il est partout.
- **Le réglage qui décide le plus souvent du résultat n'est pas l'algorithme, c'est le pas.** [[Learning rate schedules]] est l'hyperparamètre le plus déterminant de l'entraînement, avant l'architecture et avant l'optimiseur.
- **`math/optimisation` n'est pas `ml/hyperopt`.** Ici on minimise une fonction **connue**, dont on a le gradient ou la structure. Chercher des hyperparamètres, c'est optimiser une fonction qu'on ne peut qu'évaluer, une fois par entraînement — un autre problème, un autre outillage.

## Choisir

- Comprendre pourquoi un entraînement ne converge pas → [[Gradient descent]], puis [[Learning rate schedules]], puis [[Loss landscape and saddle points]].
- Savoir si le résultat d'un solveur est *le* minimum ou *un* minimum → [[Convexity]].
- Peu de paramètres, un optimum précis exigé → [[Newton & quasi-Newton]].
- Des contraintes d'égalité ou d'inégalité à respecter → [[Optimisation sous contrainte]] (Lagrangien, KKT).
- Des décisions discrètes — affecter, planifier, découper → [[Optimisation combinatoire]], puis [[Programmation linéaire en nombres entiers (MIP)]] pour la formulation.
- Résoudre un LP ou un MIP en Python → [[PuLP]], qui délègue à CBC, HiGHS, Gurobi ou CPLEX.
- Une optimisation continue non linéaire dans du code numérique → le module `optimize` de SciPy, pas ce dossier.
- Chercher des hyperparamètres → [[Optimisation d'hyperparamètres]], au domaine [[Machine Learning]].

<!-- AUTO:START -->
### Notions
- [[Convexity]] — domaines : data-sci, ml-eng
- [[Gradient descent]] — domaines : data-sci, ml-eng
- [[Learning rate schedules]] — domaines : ml-eng, ai-eng
- [[Loss landscape and saddle points]] — domaines : ml-eng, ai-eng
- [[Newton & quasi-Newton]] — domaines : data-sci, ml-eng
- [[Optimisation combinatoire]] — domaines : data-sci, ml-eng
- [[Optimisation sous contrainte]] — domaines : data-sci, ml-eng
- [[Programmation linéaire en nombres entiers (MIP)]] — domaines : data-sci, ml-eng

### Briques
- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).

### Comparatifs
- [[Comparatif - Solveurs d'optimisation]]
<!-- AUTO:END -->
