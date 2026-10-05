---
role: comparatif
nom: Comparatif - Solveurs d'optimisation
categorie: math/optimisation
tags: [optimization, linear-programming, combinatorial-optimization]
---

# Comparatif - Solveurs d'optimisation

> On tranche sur : la **couche** — un modeleur qui délègue, un solveur qui résout, une suite qui fait les deux, un solveur taillé pour un seul problème — puis sur la **classe du problème** : linéaire et entier, convexe, non linéaire, contraintes combinatoires, tournées.

![[Comparatif - Solveurs d'optimisation.base]]

## Ce qui départage

Sept membres sur quatre couches : trois **modeleurs** qui délèguent la résolution ([[PuLP]], [[Pyomo]], [[CVXPY]]), un **solveur** ([[HiGHS]]), une **suite** qui fait les deux ([[OR-Tools]]) et deux spécialistes des **tournées** ([[PyVRP]], [[HGS-CVRP]]). Un modèle écrit avec un modeleur se passe à un solveur : le choix se fait donc deux fois, et le tableau mélange les deux.

- [[PuLP]] — un **modeleur**, pas un solveur : variables, objectif et contraintes se déclarent en objets Python proches de la formulation mathématique, PuLP génère un LP/MPS et **délègue** la résolution — CBC livré par défaut, GLPK, HiGHS, SCIP, Gurobi, CPLEX interchangeables sans réécrire le modèle. Trois bornes se lisent dans sa fiche : le périmètre s'arrête au LP/MIP (le non linéaire relève de [[Pyomo]] ou de [[CVXPY]]), CBC décroche des solveurs commerciaux sur les gros MIP — où la cause est presque toujours la **formulation**, un big-M lâche, avant le solveur —, et `value()` renvoie `None` tant que `LpStatus[prob.status]` n'a pas été vérifié.
- [[Pyomo]] — le modeleur le plus **large** : LP, MIP, non linéaire, MINLP, disjonctif, stochastique, dans un modèle qui est un objet Python ; il n'installe aucun solveur, il en faut un à côté, libre ou commercial. À prendre quand le problème sort du linéaire entier ou quand le modèle se génère depuis des données ; sinon [[PuLP]] se lit en moins de lignes.
- [[CVXPY]] — le modeleur du **convexe** : la règle DCP vérifie la convexité à la construction et refuse le reste, puis le problème est traduit pour Clarabel, OSQP ou SCS (livrés) ou pour HiGHS et SCIP. Il rend les multiplicateurs de Lagrange et sait dériver la solution par rapport aux paramètres. Ni séquencement ni intervalles.
- [[HiGHS]] — un **solveur** libre de LP, de QP convexe et de MIP linéaire, MIT, sans dépendance : le solveur par défaut à installer derrière [[PuLP]], [[Pyomo]] ou [[CVXPY]]. Ni non linéaire, ni QP en entiers ; la documentation reconnaît peu de gains de parallélisme au-delà d'un nombre modeste de fils.
- [[OR-Tools]] — une **suite** qui est à la fois modeleur et solveur : CP-SAT pour les contraintes sur entiers (intervalles, `no_overlap`, `cumulative`), Glop et PDLP pour le linéaire, un module de tournées. Tout est entier dans CP-SAT. À prendre pour l'ordonnancement et les plannings de personnel, ou quand le problème est riche en règles ; un LP de grande taille va plus droit chez [[HiGHS]].
- [[PyVRP]] — le **spécialiste des tournées** en Python : capacités, fenêtres de temps, flotte hétérogène, multi-dépôts, collectes-livraisons, recherche locale itérée ; données entières. Une édition Enterprise payante existe à part, pour les pauses réglementaires et l'équité.
- [[HGS-CVRP]] — l'implémentation de **référence** du CVRP canonique par recherche génétique hybride : un exécutable C++, MIT, jusqu'à environ 1 000 clients. Ni fenêtres de temps ni multi-dépôts : au-delà du CVRP simple, [[PyVRP]].

Aucun membre ne résout un problème que son modèle formule mal : sur les MIP, la formulation compte avant le solveur ([[Programmation linéaire en nombres entiers (MIP)]]), et c'est la raison pour laquelle le choix d'un modeleur précède celui d'un solveur.

Absents du comparatif, par choix : **Gurobi**, **CPLEX**, **MOSEK** et **Xpress**, commerciaux ; **Timefold Solver**, dont l'édition Enterprise est propriétaire ; les solveurs libres **CBC**, **GLPK** et **SCIP**, qui n'ont pas de fiche dans le brain.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
