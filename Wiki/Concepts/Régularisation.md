---
galaxie: wiki
type: concept
nom: Régularisation
alias: [Ridge, Lasso, ElasticNet, Pénalisation L1/L2, Regularization]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regularization, linear-model, supervised]
---

# Régularisation

## Aperçu

- Ajoute une **pénalité** sur la taille des coefficients d'un modèle linéaire pour combattre le surapprentissage et la colinéarité.
- Lasso (L1) annule des coefficients → **sélection de variables** ; Ridge (L2) les rétrécit ; ElasticNet combine les deux.

## Concepts clés

### Ridge (L2)
- Pénalise $\sum_j \beta_j^2$. Rétrécit les coefficients vers $0$ sans les annuler. Stabilise sous colinéarité.

### Lasso (L1)
- Pénalise $\sum_j |\beta_j|$. Met des coefficients exactement à $0$ → modèle parcimonieux, sélection automatique.

### ElasticNet
- Mélange L1 + L2. Garde la sélection du Lasso tout en gérant mieux les groupes de variables corrélées (où le Lasso en choisit une au hasard).

### Compromis biais-variance
- La pénalité ajoute du biais pour réduire la variance → meilleure généralisation (cf. [[Compromis biais-variance]]). Force réglée par $\lambda$ ([[Validation croisée]]).

## Les maths, simplement

- Ridge : $\min_\beta \lVert y - X\beta\rVert^2 + \lambda \lVert\beta\rVert_2^2$.
- Lasso : $\min_\beta \lVert y - X\beta\rVert^2 + \lambda \lVert\beta\rVert_1$.
- ElasticNet : pénalité $\lambda\,\big(\alpha\lVert\beta\rVert_1 + (1-\alpha)\lVert\beta\rVert_2^2\big)$.
- Lecture bayésienne : Ridge = a priori gaussien, Lasso = a priori de Laplace sur les $\beta$ → l'estimateur est un [[Estimation MAP|MAP]].

## En pratique

- **Standardiser** les variables d'abord : la pénalité dépend de l'échelle.
- Régler $\lambda$ par validation croisée (`RidgeCV`, `LassoCV`).
- Lasso instable si variables très corrélées → préférer ElasticNet.
- S'applique aussi à la [[Régression logistique]] et aux [[GLM]] (déviance pénalisée).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.linear_model.Ridge / Lasso / ElasticNet]].

## Approches voisines & alternatives

- [[Régression linéaire]] — le modèle de base que la pénalité contraint.
- [[SVM]] — le terme $\lVert w \rVert^2$ de sa marge **est** une pénalité L2 ; son `C` est l'inverse de $\lambda$.
- [[Perceptron et MLP]] — même pénalité L2 (`alpha`), complétée par dropout et early stopping.
- [[Régression logistique]] — même pénalité, cible catégorielle.
- [[GLM]] — la régularisation s'étend aux GLM (déviance + L1/L2).
- [[Estimation MAP]] — la lecture bayésienne des pénalités.
- [[Gradient descent]] — l'objectif pénalisé (perte + L1/L2) se minimise par descente de (sous-)gradient.
- [[Optimisation sous contrainte]] — une pénalité L1/L2 est la forme lagrangienne d'une contrainte sur la norme des coefficients ($\lVert\beta\rVert \le t$).
- [[Compromis biais-variance]] — la pénalité échange du biais contre moins de variance ; la régularisation en est le levier direct.
- [[Sélection de variables]] — le Lasso L1 est une sélection intégrée (*embedded*).
- AIC/BIC, réduction de dimension ([[PCA]]) — autres parades à la sur-dimension.

## Pour aller plus loin

- Hoerl & Kennard (1970, Ridge) ; Tibshirani (1996, Lasso) ; Zou & Hastie (2005, ElasticNet).
- ESL ch. 3.4.
