---
galaxie: dev
type: service
nom: PuLP
alias: [pulp]
pitch: "Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…)."
categorie: tooling/optim
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [optimization, linear-programming, combinatorial-optimization]
url_docs: https://coin-or.github.io/pulp/
url_repo: https://github.com/coin-or/pulp
---

# PuLP

## Pourquoi

Modeleur Python pour la **programmation linéaire (LP)** et **en nombres entiers (MIP)**. On déclare variables, objectif et contraintes comme des objets Python (`LpProblem`, `LpVariable`, opérateurs `+`/`<=`), PuLP génère un fichier LP/MPS et délègue la résolution à un **solveur** externe. Le solveur par défaut est **COIN-OR CBC**, livré avec le paquet ; PuLP pilote aussi GLPK, HiGHS, SCIP (open source) et Gurobi, CPLEX, MOSEK, XPRESS (commerciaux). Fait partie du projet COIN-OR. API minimale : c'est le point d'entrée le plus simple à la recherche opérationnelle en Python.

## Quand l'utiliser

- Modéliser un problème LP/MIP (allocation de ressources, planification, sac à dos, affectation, tournées) sans coupler le code à un solveur précis.
- Prototyper une formulation puis changer de solveur (CBC → Gurobi) sans réécrire le modèle.
- Apprendre / enseigner le MIP : la syntaxe colle à la formulation mathématique.

## Quand NE PAS l'utiliser

- Optimisation **non linéaire** ou convexe générale (quadratique, conique) → Pyomo ou CVXPY, plus expressifs.
- Modèles industriels très gros où l'on exploite finement l'API native du solveur (callbacks, warm start) → API Gurobi/CPLEX directe, ou Pyomo.
- Optimisation continue sans contraintes linéaires → `scipy.optimize`.

## Déploiement & coût

- Bibliothèque Python (`uv add pulp`) ; le binaire CBC est inclus. MIT, gratuit. Les solveurs commerciaux demandent une licence séparée.
- Single-node ; rien à héberger, la résolution tourne en local dans le process.

## Pièges

- CBC est correct mais loin des solveurs commerciaux sur les gros MIP : si le branch & bound traîne, c'est presque toujours la **formulation** (big-M lâche) avant le choix du solveur — voir [[Wiki/Concepts/Programmation linéaire en nombres entiers (MIP)|MIP]].
- `value()` renvoie `None` tant que le modèle n'a pas été résolu ou s'il est infaisable : toujours vérifier `LpStatus[prob.status]`.
- Les noms de variables avec espaces ou caractères spéciaux cassent l'export LP : garder des noms simples.

## Alternatives

- Pyomo — modélisation d'optimisation plus générale (LP, MIP, NLP, MINLP), proche d'un langage algébrique. *(Page dédiée non créée.)*
- CVXPY — optimisation **convexe** en formulation déclarative (DCP). *(Page dédiée non créée.)*
- Google OR-Tools — boîte à outils RO (MIP, CP-SAT, routing) avec solveurs maison. *(Page dédiée non créée.)*

## Liens

- [[Dev/Patterns/Comparatif - Solveurs d'optimisation]] — modeleurs & solveurs LP/MIP/non linéaire.
- Concept sous-jacent : [[Wiki/Concepts/Programmation linéaire en nombres entiers (MIP)|programmation linéaire en nombres entiers (MIP)]].
- Doc : https://coin-or.github.io/pulp/
