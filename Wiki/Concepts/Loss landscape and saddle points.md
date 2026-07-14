---
galaxie: wiki
type: concept
nom: Loss landscape and saddle points
alias: [Loss landscape, Paysage de perte, Saddle points, Points-selles, Surface de perte, Sharp minima]
categorie: concept/math
domaines: [ml-eng, ai-eng]
tags: [optimization, loss-landscape]
---

# Loss landscape and saddle points

## Aperçu

- Le « paysage de perte » est la surface $L(\theta)$ qu'une optimisation parcourt. Sa géométrie explique pourquoi l'entraînement est facile ou difficile.
- En grande dimension non convexe (réseaux profonds), l'obstacle n'est presque jamais le minimum local : ce sont les **points-selles** et les zones plates/étirées qui ralentissent la [[Gradient descent]].

## Concepts clés

### Points critiques
- Là où $\nabla L=0$. Leur nature se lit dans les valeurs propres de la hessienne (cf. [[Eigendecomposition]]) :
  - toutes $>0$ → **minimum** ; toutes $<0$ → maximum ; **signes mixtes → point-selle**.

### La malédiction de la dimension
- En dimension $d$, un point critique a d'autant plus de chances d'être un point-selle (au moins une direction descendante) que $d$ est grand. Les vrais minima locaux médiocres sont rares.

### Conditionnement, plateaux, ravins
- $\kappa = \lambda_{\max}/\lambda_{\min}$ de la hessienne mesure l'étirement : grand $\kappa$ = vallée étroite où la descente zigzague (cf. [[Convexity]]).
- **Plateaux** (gradient quasi nul) et **ravins** ralentissent fortement.

### Minima nets vs plats
- Les minima **plats** généralisent souvent mieux que les minima **nets** ; la taille de batch et le pas influencent vers lesquels on converge.

## Les maths, simplement

- Près d'un point critique, $L(\theta+\Delta)\approx L+\tfrac12\Delta^\top H\Delta$ : le signe des valeurs propres de $H$ décide tout.
- Fuir un point-selle demande de l'énergie : le **bruit** du SGD et le **momentum** poussent hors de la direction plate où le gradient s'annule.
- [[Newton & quasi-Newton|Newton]] se méfie ici : avec $H$ indéfinie, il peut converger *vers* le point-selle au lieu de le fuir.

## En pratique

- SGD (bruit) + momentum pour s'échapper des selles ; warmup et planification du pas pour traverser les zones mal conditionnées (cf. [[Learning rate schedules]]).
- La taille de batch agit sur la netteté du minimum atteint → sur la généralisation ([[Compromis biais-variance]]).
- Visualisation : coupes 2D filtrées des poids (Li et al.) pour « voir » plateaux et bassins.

## Approches voisines & alternatives

- [[Convexity]] — le cas idéal sans point-selle ni minimum parasite.
- [[Gradient descent]] — l'algorithme qui parcourt ce paysage.
- [[Newton & quasi-Newton]] — exploite la courbure, mais piégé par les selles.
- [[Learning rate schedules]] — règle le pas pour franchir plateaux et ravins.
- [[Eigendecomposition]] — le spectre de la hessienne classe les points critiques.

## Pour aller plus loin

- Dauphin et al. (2014) — les points-selles, et non les minima locaux, dominent en grande dimension.
- Li et al. (2018) — *Visualizing the Loss Landscape of Neural Nets*.
