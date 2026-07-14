---
galaxie: wiki
type: concept
nom: Convexity
alias: [Convexité, Convex optimization, Optimisation convexe, fonction convexe, ensemble convexe]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, convexity]
---

# Convexity

## Aperçu

- La convexité est la propriété qui rend une optimisation **facile** : tout minimum local est le minimum global, et une méthode de descente y converge sans se faire piéger.
- Savoir si une perte est convexe détermine la confiance qu'on peut avoir dans un solveur : OLS, Ridge/Lasso, régression logistique, SVM sont convexes ; un réseau de neurones ne l'est pas (cf. [[Loss landscape and saddle points]]).

## Concepts clés

### Ensemble convexe
- Un ensemble $C$ est convexe si le segment entre deux points de $C$ reste dans $C$ : $\forall x,y\in C,\ \lambda\in[0,1],\ \lambda x+(1-\lambda)y\in C$.

### Fonction convexe
- $f$ est convexe si son graphe est sous la corde : $f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y)$.
- **1er ordre** : $f(y)\ge f(x)+\nabla f(x)^\top (y-x)$ — la tangente est sous la courbe.
- **2nd ordre** : la hessienne $\nabla^2 f \succeq 0$ (semi-définie positive) partout. Ses valeurs propres sont $\ge 0$ (cf. [[Eigendecomposition]]).

### Convexité stricte et forte
- **Stricte** : inégalité stricte → minimum unique.
- **Forte** ($\mu$-convexe) : $\nabla^2 f \succeq \mu I$, $\mu>0$. Garantit une vitesse de convergence **linéaire** des méthodes de descente.

## Les maths, simplement

- Pourquoi « local = global » : sur une fonction convexe, $\nabla f(x^\star)=0$ suffit à certifier l'optimum — pas de vallée parasite.
- **Conditionnement** : pour une fonction $\mu$-fortement convexe et $L$-lisse, le ratio $\kappa = L/\mu$ pilote la vitesse de la [[Gradient descent]] — $\kappa$ grand = surface étirée, convergence lente.
- Une somme de fonctions convexes est convexe : perte convexe + pénalité convexe ($\lVert\beta\rVert_1$, $\lVert\beta\rVert_2^2$) reste convexe → la [[Régularisation]] ne casse pas la convexité.

## En pratique

- **Convexes** (solveur fiable, optimum garanti) : moindres carrés ([[Régression linéaire]]), log-vraisemblance logistique ([[Régression logistique]]), SVM (hinge), Ridge/Lasso.
- **Non convexes** : réseaux de neurones, factorisation matricielle, k-means → pas de garantie globale, le point d'arrivée dépend de l'initialisation.
- Reformuler un problème en programme convexe (LP/QP/SOCP) quand c'est possible : outils `cvxpy`, `scipy.optimize`.

## Approches voisines & alternatives

- [[Gradient descent]] — converge vers l'optimum global dès que la fonction est convexe ; sa vitesse dépend du conditionnement.
- [[Newton & quasi-Newton]] — convergence quadratique sur les fonctions convexes lisses.
- [[Loss landscape and saddle points]] — ce qui arrive quand la convexité est perdue (cas des réseaux profonds).
- [[Régularisation]] — les pénalités L1/L2 sont convexes ; elles préservent un problème convexe.
- [[Régression logistique]] — la log-vraisemblance est convexe, d'où un optimum unique.
- [[Optimisation sous contrainte]] — sous convexité, les conditions KKT certifient l'optimum global et la dualité forte tient.
- [[Programmation linéaire en nombres entiers (MIP)]] — le LP est convexe ; c'est l'intégralité qui brise la convexité et rend le MIP difficile.

## Pour aller plus loin

- Boyd & Vandenberghe — *Convex Optimization* (référence, PDF libre).
- Distinguer convexité (garantie) et lissité (différentiabilité) : le Lasso est convexe mais non lisse → sous-gradient.
