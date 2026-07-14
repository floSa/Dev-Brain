---
galaxie: wiki
type: concept
nom: Programmation linéaire en nombres entiers (MIP)
alias: [MIP, MILP, Mixed-Integer Programming, ILP, Integer programming, Programmation linéaire, LP, Linear programming, Branch and bound, Relaxation LP]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, linear-programming, combinatorial-optimization]
---

# Programmation linéaire en nombres entiers (MIP)

## Aperçu

- Optimise un objectif **linéaire** sous des contraintes **linéaires**, tout ou partie des variables étant contraintes à être **entières**. Cadre de référence pour les décisions discrètes (oui/non, combien d'unités) en recherche opérationnelle.
- Un programme linéaire (LP) pur se résout en temps polynomial ; l'intégralité le rend **NP-difficile** — d'où la relaxation LP et le branch & bound.

## Concepts clés

### Programme linéaire (LP) et relaxation
- LP : $\min c^\top x$ s.c. $Ax \le b,\ x \ge 0$. Résolu par le **simplexe** (parcours des sommets) ou les **méthodes de point intérieur**.
- **Relaxation LP** : on retire la contrainte d'intégralité. Son optimum est une **borne** (inférieure en minimisation) sur l'optimum entier, et le point de départ de la recherche.

### Branch & bound
- Si la relaxation donne une variable fractionnaire $x_j = 2{,}4$, on **branche** en deux sous-problèmes : $x_j \le 2$ et $x_j \ge 3$.
- Chaque nœud est borné par sa relaxation LP ; un nœud dont la borne est pire que la meilleure solution entière connue (l'**incumbent**) est **élagué**. L'arbre n'explore qu'une fraction de l'espace.

### Coupes et branch & cut
- **Plans coupants** (Gomory, coupes de couverture) : inégalités valides qui retranchent des solutions fractionnaires sans éliminer d'entier admissible → resserrent la relaxation. Couplés au branch & bound = **branch & cut**, cœur des solveurs modernes.

## Les maths, simplement

- MIP : $\min c^\top x$ s.c. $Ax \le b$, $x \ge 0$, $x_j \in \mathbb{Z}$ pour $j \in I$.
- La qualité d'une formulation se lit au **gap d'intégralité** : écart entre l'optimum entier et celui de sa relaxation LP. Plus la relaxation est serrée (proche de l'enveloppe convexe des points entiers), plus le branch & bound converge vite.
- Modélisation : les choix logiques s'encodent en binaires $x \in \{0,1\}$ et contraintes « big-M ».

## En pratique

- Sert à modéliser tournées de véhicules, planification, allocation de ressources, sac à dos, affectation — voir [[Optimisation combinatoire]].
- Solveurs : Gurobi, CPLEX (commerciaux, très rapides), HiGHS, CBC, SCIP (open source). Modélisation Python : [[Dev/Services/PuLP|PuLP]] (CBC par défaut), `Pyomo`, `OR-Tools`, `cvxpy`.
- Piège : une formulation « big-M » mal calibrée donne une relaxation lâche → arbre qui explose. Soigner la formulation prime sur le choix du solveur.

## Approches voisines & alternatives

- [[Optimisation combinatoire]] — la classe de problèmes discrets que le MIP résout en pratique.
- [[Convexity]] — le LP est convexe (donc facile) ; c'est l'intégralité, non convexe, qui rend le MIP dur.
- [[Optimisation sous contrainte]] — cadre continu (Lagrangien, KKT) ; le MIP en est la version à variables discrètes.
- [[Optimal transport]] — le problème de transport discret est un cas particulier de programmation linéaire.
- Programmation dynamique — alternative exacte pour les problèmes à sous-structure optimale (sac à dos, plus court chemin).

## Pour aller plus loin

- Wolsey — *Integer Programming*.
- Documentation Gurobi / Google OR-Tools (modélisation MIP, exemples).
