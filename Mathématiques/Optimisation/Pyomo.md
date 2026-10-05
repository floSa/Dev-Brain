---
role: brique
nom: Pyomo
alias: [pyomo, Python Optimization Modeling Objects, Coopr]
pitch: "Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PuLP]]", "[[CVXPY]]", "[[OR-Tools]]"]
complements: ["[[HiGHS]]"]
tags: [optimization, linear-programming, combinatorial-optimization, constrained-optimization]
url_docs: https://pyomo.readthedocs.io/
url_repo: https://github.com/Pyomo/pyomo
---

# Pyomo

<!-- AUTO:BANDEAU:START -->
> Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Langage de modélisation **algébrique** embarqué dans Python. Un modèle se construit comme un objet
(`ConcreteModel`, variables `Var`, contraintes `Constraint`, objectif `Objective`) dans un programme
Python complet : boucles, fonctions et données pandas servent à le générer. Pyomo écrit ensuite le
problème et le passe à un **solveur externe**, qu'il n'installe pas : ni solveur livré, ni dépendance
stricte à un solveur, pour éviter les conflits de versions.

Le README liste ses classes de problèmes : programmation linéaire, quadratique, non linéaire, MIP, MIQP,
**MINLP**, programmation stochastique en nombres entiers, programmation disjonctive généralisée,
équations différentielles algébriques, programmation avec contraintes d'équilibre et programmation par
contraintes. Le paquet complémentaire `mpi-sppy` parallélise les sous-problèmes stochastiques. C'est
l'étendue qui le sépare de [[PuLP]], limité au LP et au MIP.

Relevé le 2026-10-05 : **6.10.1** du 2026-06-04 (PyPI, *Production/Stable*, Python 3.10 et plus ; le projet
teste CPython 3.10 à 3.14 et PyPy 3.11), dépôt actif (push du 2026-09-30). Le fichier `LICENSE.md` est une
licence **BSD à trois clauses** (copyright Sandia) ; GitHub l'affiche sans identifiant SPDX.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un modèle non linéaire, MINLP, disjonctif ou stochastique, que [[PuLP]] ne couvre pas | Un LP ou un MIP simple à poser vite : [[PuLP]] se lit en moins de lignes |
| Un modèle généré par du code à partir de données (indices, ensembles, paramètres) et conservé dans un dépôt | Un problème de contraintes riche en ordre et en ressources : [[OR-Tools]] (CP-SAT) l'exprime plus directement |
| Garder le choix du solveur et en changer sans réécrire le modèle | Un problème strictement convexe qu'on veut voir **vérifié** convexe avant résolution : [[CVXPY]] et sa règle DCP |
| Un outil de recherche ou d'enseignement où le modèle est lui-même un objet à manipuler | Mesurer la vitesse de construction du modèle sur de très gros problèmes : le README renvoie à des courbes de performance, aucun chiffre n'a été relevé ici |

## Mise en œuvre

- Installation — `uv add pyomo` ; le solveur s'installe à part, par exemple `uv add highspy` pour [[HiGHS]] (testé ici : `SolverFactory('highs')` le trouve), ou `conda install -c conda-forge ipopt glpk`
- Point d'entrée — `import pyomo.environ as pyo`, `m = pyo.ConcreteModel()`, `m.x = pyo.Var(bounds=(0, 4))`, `m.c = pyo.Constraint(expr=...)`, `m.o = pyo.Objective(expr=..., sense=pyo.maximize)`, puis `pyo.SolverFactory("highs").solve(m)`
- Prérequis — Python 3.10 minimum ; un solveur, libre (HiGHS, GLPK, SCIP, Ipopt) ou commercial (Gurobi, CPLEX) ; la documentation précise que chacun est responsable de la licence de son solveur
- Exécution — dans le process appelant ; le solveur peut être un exécutable ou une bibliothèque Python
- Coût — gratuit, BSD-3-Clause ; les solveurs commerciaux demandent chacun leur licence

## Limites à connaître

- **Aucun solveur n'est fourni.** Sans solveur installé, `SolverFactory("glpk")` ou `("cbc")` répond « non disponible » (constaté sur une installation neuve) ; la table de la documentation indique la commande `pip` ou `conda` de chaque solveur.
- **Lire la condition de terminaison avant la valeur.** `results.solver.termination_condition` dit si le solveur a trouvé l'optimum, une borne ou rien.
- **Sans convexité, rien ne garantit l'optimum global.** Le choix d'un solveur non linéaire ne change pas la nature du problème : la question se pose d'abord par [[Convexity]].

## Écosystème

### Alternatives

- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…). — le modeleur plus court, limité au LP et au MIP, à préférer quand rien de non linéaire n'est en jeu.
- [[CVXPY]] — Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0. — le modeleur convexe : la structure du problème est vérifiée à la construction, au prix de ne pas accepter ce qui n'est pas convexe.
- [[OR-Tools]] — Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0. — la suite qui apporte son propre solveur de contraintes, là où Pyomo délègue tout.

### Compléments

- [[HiGHS]] — Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers. — un solveur libre pour les modèles linéaires et entiers, qui s'installe par `pip`.

## Ressources

- Documentation — https://pyomo.readthedocs.io/
- Dépôt — https://github.com/Pyomo/pyomo
- Documentation — https://www.pyomo.org/documentation/

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Optimisation sous contrainte]] — la notion : contraintes, Lagrangien, KKT
- [[Programmation linéaire en nombres entiers (MIP)]] — la notion voisine, pour le cas entier linéaire
- [[Optimisation combinatoire]] — la classe de problèmes que le MIP formule
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
