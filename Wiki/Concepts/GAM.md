---
galaxie: wiki
type: concept
nom: GAM
alias: [Modèles additifs généralisés, Generalized Additive Model, Modèle additif généralisé]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regression, linear-model, supervised]
---

# GAM

## Aperçu

- Étend le [[GLM]] en remplaçant chaque effet linéaire par une **fonction lisse** (spline) apprise sur les données.
- Capture des relations **non linéaires** tout en restant additif et interprétable — un effet par variable, lisible.

## Concepts clés

### Du linéaire au lissé
- $g(\mu) = \beta_0 + f_1(x_1) + \dots + f_p(x_p)$ : chaque $f_j$ est une fonction lisse (spline), pas un coefficient unique.

### Splines
- Bases de fonctions (B-splines, splines de lissage, plaques minces). Le modèle apprend la forme de chaque effet.

### Contrôle du lissage
- Un paramètre de pénalité par terme arbitre entre ajustement et régularité (rugosité). Réglé par REML ou GCV.

### Interprétabilité
- On trace chaque $f_j$ : la forme de l'effet partiel de chaque variable se lit directement.

## Les maths, simplement

- $g(\mu) = \beta_0 + \sum_j f_j(x_j)$, chaque $f_j$ développée sur une base de splines.
- Ajustement = vraisemblance pénalisée : $\ell(\beta) - \sum_j \lambda_j \int f_j''(x)^2\,dx$ (pénalise la courbure).
- $\lambda_j \to \infty$ ramène $f_j$ à une droite → le GAM redevient un [[GLM]].

## En pratique

- Idéal quand une relation non linéaire est suspectée mais qu'on veut garder l'interprétabilité (vs boosting/forêts, boîtes noires).
- Surveiller le nombre de degrés de liberté effectifs par terme ; trop de flexibilité → surajustement.
- Interactions : termes tensoriels (`te()`), au-delà des effets purement additifs.
- Outils : `mgcv` (R, la référence), `pyGAM`, `statsmodels` (`gam.GLMGam`). Absent de scikit-learn.

## Approches voisines & alternatives

- [[GLM]] — le cas particulier où chaque effet est linéaire (GAM = GLM + splines).
- [[Régression linéaire]] — le socle, sans lien ni lissage.
- Gradient boosting, forêts aléatoires — non linéaires aussi, mais non additifs et moins interprétables (hors cluster).

## Pour aller plus loin

- Hastie & Tibshirani — *Generalized Additive Models* (1990).
- Simon Wood — *Generalized Additive Models: An Introduction with R* (mgcv).
