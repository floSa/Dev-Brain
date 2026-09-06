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
alternatives: []
complements: []
tags: [optimization, linear-programming, combinatorial-optimization]
url_docs: https://coin-or.github.io/pulp/
url_repo: https://github.com/coin-or/pulp
---

# PuLP

<!-- AUTO:BANDEAU:START -->
> Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
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
| Modéliser un problème LP ou MIP — allocation de ressources, planification, sac à dos, affectation, tournées — sans coupler le code à un solveur précis | Optimisation non linéaire ou convexe générale, quadratique ou conique : Pyomo et CVXPY sont plus expressifs (aucun des deux n'est fiché au brain) |
| Prototyper une formulation puis changer de solveur, de CBC à Gurobi, sans réécrire le modèle | Modèle industriel très gros où l'on exploite finement l'API native du solveur — callbacks, warm start : API Gurobi ou CPLEX directe, ou Pyomo |
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

- *Aucune alternative déclarée : les candidats naturels — Pyomo (LP, MIP, NLP, MINLP, proche d'un langage algébrique), CVXPY (optimisation convexe en formulation DCP), Google OR-Tools (MIP, CP-SAT, routing) — n'ont pas de page au brain. Le manque est ouvert au backlog d'enrichissement, section « Solveurs d'optimisation ».*

## Ressources

- Documentation — https://coin-or.github.io/pulp/
- Dépôt — https://github.com/coin-or/pulp

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Optimisation combinatoire]] — la notion : la classe de problèmes que le MIP formule
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier, qui ne compte qu'un membre faute des autres solveurs au brain
