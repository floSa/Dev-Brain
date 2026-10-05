---
role: brique
nom: CVXPY
alias: [cvxpy, CVX Python, disciplined convex programming Python]
pitch: "Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PuLP]]", "[[Pyomo]]", "[[OR-Tools]]"]
complements: ["[[HiGHS]]"]
tags: [optimization, convexity, constrained-optimization, linear-programming]
url_docs: https://www.cvxpy.org/
url_repo: https://github.com/cvxpy/cvxpy
---

# CVXPY

<!-- AUTO:BANDEAU:START -->
> Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Langage de modélisation **embarqué dans Python** pour les problèmes d'optimisation **convexes**. On écrit
variables, objectif et contraintes presque comme sur le papier (`cp.Minimize(cp.sum_squares(A @ x - b))`,
`x >= 0`), sans passer par la forme standard qu'exigent les solveurs. CVXPY applique les règles de la
**programmation convexe disciplinée** (DCP) : chaque expression a une courbure connue, la règle de
composition dit si le problème est convexe, et il est refusé sinon (`DCPError`, constaté en maximisant
une norme). Il le réécrit alors dans la forme qu'attend le solveur choisi et renvoie la valeur, les
variables, et les **multiplicateurs de Lagrange** de chaque contrainte (`dual_value`).

Les solveurs libres **Clarabel, OSQP et SCS** sont livrés ; beaucoup d'autres s'installent à part, dont
HiGHS, SCIP, GLPK, CBC et des solveurs commerciaux. La table de la documentation dit, solveur par solveur,
quelles classes il traite : LP, QP, cône du second ordre, semi-défini, exponentiel, MIP. Par défaut CVXPY
appelle le solveur le plus spécialisé : OSQP pour un QP, Clarabel pour un SOCP. Les **variables entières**
sont acceptées avec un solveur qui sait le faire, ce qui donne des LP en nombres entiers ([[HiGHS]]). Des
extensions complètent le cadre : programmation géométrique disciplinée, quasi-convexe disciplinée, problèmes
paramétrés (DPP) et dérivables par rapport à leurs paramètres. Une section DNLP de la documentation traite
le non linéaire lisse, en passant `nlp=True` à `solve` ; elle n'a pas été éprouvée ici.

Relevé le 2026-10-05 : **v1.9.3** du 2026-09-19 (PyPI, Python 3.11 et plus ; version testée localement avec
HiGHS), dépôt actif (push du 2026-10-04), Apache-2.0 lue dans `LICENSE`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le problème est convexe — moindres carrés sous bornes, régression régularisée, portefeuille, contrôle optimal, ajustement sous contraintes | Un problème non convexe ou combinatoire riche en règles : [[OR-Tools]] pour les contraintes, [[Pyomo]] pour le non linéaire général |
| Vérifier la convexité à la construction plutôt que de la découvrir à la résolution : la règle DCP la contrôle | Un LP ou un MIP purement linéaire, posé tel quel : [[PuLP]] est plus court, sans règle de courbure à respecter |
| Les gradients de la solution par rapport aux paramètres comptent (couches différentiables) | Une expression mathématiquement convexe mais écrite hors des règles : CVXPY la rejette et il faut la reformuler |
| Changer de solveur selon la classe du problème sans réécrire le modèle | Un grand MIP : les solveurs commerciaux (Gurobi, CPLEX, MOSEK) restent la référence, et la formulation compte plus que le solveur |

## Mise en œuvre

- Installation — `uv add cvxpy` ; `uv add highspy` ajoute HiGHS pour le linéaire et l'entier
- Point d'entrée — `import cvxpy as cp`, `x = cp.Variable(n)`, `prob = cp.Problem(cp.Minimize(...), [contraintes])`, `prob.solve()` puis `x.value` ; `prob.solve(solver=cp.HIGHS)` impose le solveur, `verbose=True` affiche sa sortie
- Prérequis — Python 3.11 minimum pour la version relevée ; un problème convexe respectant les règles DCP
- Exécution — dans le process appelant ; l'option `solver_path` essaie plusieurs solveurs dans l'ordre
- Coût — gratuit, Apache-2.0 ; certains solveurs optionnels (Gurobi, MOSEK, CPLEX) demandent une licence

## Limites à connaître

- **Une limite de forme, pas de performance.** Un problème convexe écrit hors des règles DCP est refusé ; la documentation donne les atomes autorisés et leur courbure.
- **Le choix du solveur dépend de la classe.** Un solveur qui ne sait pas traiter le problème fait lever une exception ; la table de la documentation dit lesquels acceptent les entiers (par exemple HiGHS : LP, QP et MIP linéaire seulement).
- **Pas de combinatoire riche.** Les entiers sont permis, mais pas les contraintes de séquencement ou d'intervalle : ce n'est pas un solveur de contraintes.

## Écosystème

### Alternatives

- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…). — le modeleur pour un modèle purement linéaire ou entier, sans règle de courbure.
- [[Pyomo]] — Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR. — le modeleur plus large, qui accepte le non convexe et le non linéaire sans vérifier la convexité.
- [[OR-Tools]] — Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0. — le choix quand le problème est combinatoire et non convexe.

### Compléments

- [[HiGHS]] — Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers. — un solveur libre pour les LP, les QP et les MILP que CVXPY lui confie.

## Ressources

- Documentation — https://www.cvxpy.org/
- Dépôt — https://github.com/cvxpy/cvxpy
- Solveurs — https://www.cvxpy.org/tutorial/solvers/index.html

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Convexity]] — la notion : pourquoi un minimum local d'un problème convexe est global
- [[Optimisation sous contrainte]] — la notion : Lagrangien, dualité, KKT, ce que `dual_value` renvoie
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
