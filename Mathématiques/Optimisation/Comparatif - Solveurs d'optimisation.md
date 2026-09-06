---
role: comparatif
nom: Comparatif - Solveurs d'optimisation
categorie: math/optimisation
tags: [optimization, linear-programming, combinatorial-optimization]
---

# Comparatif - Solveurs d'optimisation

> On tranche sur : la classe du problème — linéaire et entier, ou non linéaire — et sur le couplage au solveur, qu'on veut délégué ou piloté finement.

![[Comparatif - Solveurs d'optimisation.base]]

## Ce qui départage

- [[PuLP]] — un **modeleur**, pas un solveur : variables, objectif et contraintes se déclarent en objets Python proches de la formulation mathématique, PuLP génère un LP/MPS et **délègue** la résolution — CBC livré par défaut, GLPK, HiGHS, SCIP, Gurobi, CPLEX interchangeables sans réécrire le modèle. Trois bornes se lisent dans sa fiche : le périmètre s'arrête au LP/MIP (le non linéaire relève de Pyomo ou CVXPY), CBC décroche des solveurs commerciaux sur les gros MIP — où la cause est presque toujours la **formulation**, un big-M lâche, avant le solveur —, et `value()` renvoie `None` tant que `LpStatus[prob.status]` n'a pas été vérifié.

## Ce comparatif ne compare rien, et ce n'est pas la conversion qui le règle

**Un seul membre.** La page est écrite au même gabarit que les 46 autres, et elle porte
comme elles un `role:`, une couleur et des liens sortants — mais une puce unique n'est pas
une comparaison, et il faut le dire ici plutôt que le laisser deviner.

Le défaut n'est pas dans la vue : son filtre est juste, `categorie == "math/optimisation"`
sélectionne exactement ce que le vault contient. **Le défaut est que le vault n'a pas les
autres solveurs.** La fiche [[PuLP]] en nomme onze en clair, aucun n'ayant de page :

- modeleurs concurrents — **Pyomo**, **CVXPY**, `scipy.optimize` ;
- solveurs open source pilotés par PuLP — **CBC**, **GLPK**, **HiGHS**, **SCIP** ;
- solveurs commerciaux — **Gurobi**, **CPLEX**, **MOSEK**, **XPRESS**.

`R8b` continue d'être émis après la conversion, et c'est le comportement voulu : la règle
compte les membres du `.base`, que la page n'a pas modifié. L'avertissement reste donc
visible tant que le trou n'est pas comblé. Il est ouvert au backlog
(`AI/backlog-enrichissement-brain.md`, section « Solveurs d'optimisation »).

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
