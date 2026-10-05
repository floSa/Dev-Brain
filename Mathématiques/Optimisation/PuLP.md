---
role: brique
nom: PuLP
alias: [pulp]
pitch: "Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…)."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Pyomo]]", "[[CVXPY]]", "[[OR-Tools]]"]
complements: ["[[HiGHS]]"]
tags: [optimization, linear-programming, combinatorial-optimization]
url_docs: https://coin-or.github.io/pulp/
url_repo: https://github.com/coin-or/pulp
---

# PuLP

<!-- AUTO:BANDEAU:START -->
> Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

Modeleur Python pour la **programmation linéaire** (LP) et **en nombres entiers** (MIP).
Variables, objectif et contraintes se déclarent comme des objets Python — `LpProblem`,
`LpVariable`, opérateurs `+` et `<=` — puis PuLP génère un fichier LP ou MPS et
**délègue** la résolution à un solveur externe. COIN-OR CBC est livré avec le paquet et
sert par défaut ; GLPK, HiGHS et SCIP côté open source, Gurobi, CPLEX, MOSEK et XPRESS
côté commercial se substituent sans réécrire une ligne du modèle. C'est la conséquence à
retenir : PuLP n'est pas un solveur, c'est la couche qui rend le solveur interchangeable.
Le projet fait partie de COIN-OR, et son API minimale colle à la formulation
mathématique — ce qui en fait le point d'entrée le plus court vers la recherche
opérationnelle en Python.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Modéliser un problème LP ou MIP — allocation de ressources, planification, sac à dos, affectation, tournées — sans coupler le code à un solveur précis | Optimisation non linéaire ou convexe générale, quadratique ou conique : [[Pyomo]] et [[CVXPY]] sont plus expressifs |
| Prototyper une formulation puis changer de solveur, de CBC à Gurobi, sans réécrire le modèle | Modèle industriel très gros où l'on exploite finement l'API native du solveur — callbacks, warm start : API Gurobi ou CPLEX directe, ou [[Pyomo]] |
| Apprendre ou enseigner le MIP : la syntaxe colle à la formulation mathématique | Optimisation continue sans contraintes linéaires : `scipy.optimize` couvre le besoin |
| | Attendre du solveur qu'il rattrape la formulation : CBC est correct mais décroche des solveurs commerciaux sur les gros MIP, et quand le branch & bound traîne la cause est presque toujours un big-M lâche → [[Programmation linéaire en nombres entiers (MIP)]] |

## Mise en œuvre

- Installation — `uv add pulp` ; le binaire CBC est inclus, aucun solveur à installer pour démarrer
- Point d'entrée — import Python : `LpProblem`, `LpVariable`, puis `prob.solve()`. Toujours lire `LpStatus[prob.status]` avant `value()`, qui renvoie `None` tant que le modèle n'est pas résolu ou s'il est infaisable. Garder des noms de variables simples : espaces et caractères spéciaux cassent l'export LP
- Prérequis — Python ; un solveur externe seulement si l'on quitte CBC — GLPK, HiGHS, SCIP, ou une licence commerciale pour Gurobi, CPLEX, MOSEK, XPRESS
- Exécution — dans le process appelant, mono-nœud ; rien à héberger, la résolution tourne en local
- Coût — gratuit, MIT ; les solveurs commerciaux demandent chacun leur propre licence

## Écosystème

### Alternatives

- [[Pyomo]] — Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR. — le modeleur à prendre quand le problème sort du LP et du MIP, ou quand il faut piloter finement le solveur.
- [[CVXPY]] — Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0. — le modeleur pour les problèmes convexes, quadratiques ou coniques, que PuLP ne formule pas.
- [[OR-Tools]] — Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0. — la suite qui porte son propre solveur de contraintes, pour les modèles riches en ordre et en ressources.

### Compléments

- [[HiGHS]] — Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers. — un solveur libre auquel PuLP délègue la résolution, à la place de CBC.

## Ressources

- Documentation — https://coin-or.github.io/pulp/
- Dépôt — https://github.com/coin-or/pulp

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Optimisation combinatoire]] — la notion : la classe de problèmes que le MIP formule
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier, qui réunit PuLP et les autres modeleurs et solveurs libres
- [[Programmation par contraintes]] — la famille voisine quand le modèle n'est pas linéaire ou que les domaines sont finis.
- [[Plannings de personnel (rostering)]] — un cas d'usage de modélisation en MIP.
