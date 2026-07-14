---
galaxie: wiki
type: concept
nom: Optimisation sous contrainte
alias: [Constrained optimization, Lagrangien, Multiplicateurs de Lagrange, Lagrange multipliers, KKT, Karush-Kuhn-Tucker, Conditions KKT, Dualité lagrangienne]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, constrained-optimization, convexity]
---

# Optimisation sous contrainte

## Aperçu

- Minimiser une fonction sous des **contraintes d'égalité et d'inégalité** : la solution n'est plus là où le gradient s'annule, mais là où il s'équilibre avec les contraintes actives.
- Le **Lagrangien** transforme un problème contraint en un problème sans contrainte ; les conditions **KKT** en donnent l'optimalité.

## Concepts clés

### Multiplicateurs de Lagrange (égalités)
- Pour $\min f(x)$ s.c. $g(x)=0$ : à l'optimum, $\nabla f = \lambda \nabla g$ — les gradients sont colinéaires. Le scalaire $\lambda$ est le **multiplicateur**.
- Lagrangien : $\mathcal{L}(x,\lambda) = f(x) + \lambda\, g(x)$ ; annuler $\nabla \mathcal{L}$ redonne la condition.

### Conditions KKT (inégalités)
- Pour des contraintes $h_i(x) \le 0$ : à l'optimum, (1) stationnarité $\nabla f + \sum_i \mu_i \nabla h_i = 0$, (2) admissibilité, (3) $\mu_i \ge 0$, (4) **complémentarité** $\mu_i h_i = 0$ (une contrainte inactive a un multiplicateur nul).
- Sous [[Convexity|convexité]] et qualification des contraintes, KKT est **nécessaire et suffisant** → certificat d'optimalité.

### Dualité
- Le **problème dual** $\max_{\mu \ge 0} \min_x \mathcal{L}$ fournit une borne inférieure (dualité faible) ; elle égale le primal sous convexité (dualité forte). Le multiplicateur = **prix marginal** (shadow price) de la contrainte.

## Les maths, simplement

- Interprétation : $\lambda$ et $\mu$ mesurent la **sensibilité** de l'optimum à un relâchement de la contrainte — de combien gagne-t-on en desserrant le second membre d'une unité.
- Lien direct avec la [[Régularisation]] : une pénalité $\lambda \lVert\beta\rVert$ est la forme lagrangienne d'une contrainte $\lVert\beta\rVert \le t$ — Ridge et Lasso *sont* de l'optimisation sous contrainte.

## En pratique

- SVM, Ridge/Lasso, maximum d'entropie : tous se posent et se résolvent via Lagrangien / KKT.
- Méthodes : pénalités, lagrangien augmenté, points intérieurs (barrières), gradient projeté.
- Outils : `scipy.optimize.minimize` (contraintes `eq` / `ineq`), `cvxpy` (programmes convexes contraints).

## Approches voisines & alternatives

- [[Convexity]] — sous convexité, KKT certifie l'optimum global et la dualité forte tient.
- [[Régularisation]] — la pénalité L1/L2 est la forme lagrangienne d'une contrainte sur la norme des coefficients.
- [[Gradient descent]] — version contrainte : gradient projeté, méthodes de pénalité.
- [[Programmation linéaire en nombres entiers (MIP)|Programmation linéaire]] — la dualité LP est le cas linéaire de la dualité lagrangienne ; le MIP en est l'analogue à variables discrètes.

## Pour aller plus loin

- Boyd & Vandenberghe — *Convex Optimization*, ch. 5 (dualité ; PDF libre).
- Nocedal & Wright — *Numerical Optimization* (méthodes contraintes).
