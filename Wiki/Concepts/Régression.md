---
galaxie: wiki
type: concept
nom: Régression
alias: [Regression, Régression supervisée, Modélisation de cible continue]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regression, supervised]
---

# Régression

## Aperçu

- Branche de l'[[Apprentissage supervisé]] où la cible est **continue** : prédire une quantité (prix, durée, consommation, température) plutôt qu'une étiquette.
- L'écart entre prédiction et réalité a un sens et une unité : se tromper de 2 est deux fois pire que de se tromper de 1. C'est précisément ce qui la distingue de la [[Classification]], où « chat » et « chien » ne se soustraient pas.

## Concepts clés

### Quand régresser plutôt que classer
- La cible est **numérique et ordonnée**, et les écarts sont interprétables. Sinon, [[Classification]].
- Piège fréquent : **binariser une cible continue** (« prix > 100k ? ») par confort. On jette de l'information et on perd en précision. Ne le faire que si la décision métier est réellement binaire.
- Cible de comptage (0, 1, 2, 3…), positive et discrète : ni l'un ni l'autre exactement — passer par un [[GLM]] (Poisson, binomiale négative). Cible = durée avant événement, avec des observations non terminées : [[Analyse de survie]].

### Ce que le modèle estime vraiment
- Par défaut, une régression prédit la **moyenne conditionnelle** $\mathbb{E}[y \mid x]$. C'est un choix, pas une fatalité : la perte utilisée décide de la statistique estimée.
- Perte quadratique → moyenne (sensible aux valeurs extrêmes). Perte absolue → **médiane** (robuste). Perte pinball → un **quantile** donné, base de la régression quantile et des intervalles de prédiction.

### Linéaire ne veut pas dire « droite »
- « Linéaire » qualifie la linéarité en **paramètres**, pas en variables. $y = \beta_0 + \beta_1 x + \beta_2 x^2$ reste un modèle linéaire.
- Étendre sans quitter le cadre : termes polynomiaux, splines ([[GAM]]), fonctions de lien et lois non normales ([[GLM]]).

### Les familles disponibles
- **Linéaires** — [[Régression linéaire]] (baseline, interprétable), pénalisées ([[Régularisation]] : Ridge, Lasso, ElasticNet), généralisées ([[GLM]]), additives ([[GAM]]).
- **À base d'arbres** — [[Arbres de décision]], [[Random Forest]], [[Gradient Boosting (GBDT)]] : non-linéarités et interactions gratuites, mais **prédiction constante par morceaux** — incapables d'extrapoler hors de la plage vue.
- **À distance / noyau** — [[k-NN]], [[SVM]] (SVR).
- **Réseaux de neurones** — [[Perceptron et MLP]], utiles surtout quand les entrées sont non structurées.

### Diagnostiquer, pas seulement scorer
- Un $R^2$ correct peut masquer un modèle faux. Tracer **résidus vs prédictions** : une structure visible (courbure, entonnoir) dit que le modèle rate quelque chose.
- Entonnoir = variance non constante (hétéroscédasticité) → transformer la cible (log) ou changer de loi ([[GLM]]). Courbure = non-linéarité manquante.

## Les maths, simplement

- Moindres carrés — le critère de référence : $\min_\beta \sum_{i=1}^{n} (y_i - x_i^\top \beta)^2$. Solution fermée $\hat{\beta} = (X^\top X)^{-1} X^\top y$, qui se dégrade quand les variables sont corrélées (d'où la [[Régularisation]]).
- Le choix de la perte fixe ce qu'on estime : $\ell_2 = (y - \hat{y})^2$ → moyenne ; $\ell_1 = |y - \hat{y}|$ → médiane ; pinball $\rho_\tau$ → quantile $\tau$.
- $R^2 = 1 - \dfrac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$ — la part de variance expliquée par rapport au modèle « je prédis toujours la moyenne ». Négatif = pire que cette baseline.

## En pratique

- **Baseline** : prédire la moyenne (ou la médiane) de la cible. Puis [[Régression linéaire]]. Le $R^2$ n'a de sens que relativement à cette référence.
- **Choisir la métrique selon le coût de l'erreur** : RMSE punit les grosses erreurs (dérivée de la perte quadratique), MAE les traite toutes pareil, MAPE explose quand la cible approche 0. Voir [[Regression metrics]].
- **Les arbres n'extrapolent pas.** Un [[Gradient Boosting (GBDT)|GBDT]] entraîné sur des surfaces de 20 à 200 m² prédira une constante à 400 m². Sur une tendance qui sort de la plage observée, un modèle linéaire est plus sûr.
- Cible très asymétrique (prix, revenus, durées) : passer en `log(y)` linéarise souvent la relation et stabilise la variance — sans oublier que la moyenne des logs n'est pas le log de la moyenne au moment de repasser en unités.
- Une prédiction ponctuelle sans **incertitude** est peu exploitable : régression quantile, ou intervalles par [[Bootstrap|bootstrap]].
- Si la cible est indexée par le temps, ce n'est plus de la régression i.i.d. : ordre et fuite temporelle changent tout ([[Forecasting framing]], [[Walk-forward CV]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn]] (`LinearRegression`, `Ridge`, `RandomForestRegressor`), [[Dev/Services/statsmodels|statsmodels]] (inférence, tests, diagnostics), [[Dev/Services/XGBoost|XGBoost]] / [[Dev/Services/LightGBM|LightGBM]].

## Approches voisines & alternatives

- [[Classification]] — l'autre branche supervisée : cible catégorielle plutôt que continue.
- [[Apprentissage supervisé]] — le cadre englobant des deux.
- [[Régression linéaire]] — la baseline, et le socle de toute la famille.
- [[Régularisation]] — Ridge / Lasso / ElasticNet : indispensables dès que les variables sont nombreuses ou corrélées.
- [[GLM]] — cibles non gaussiennes (comptages, proportions, durées).
- [[GAM]] — non-linéarités lisses tout en gardant la lecture variable par variable.
- [[Gradient Boosting (GBDT)]] — l'état de l'art sur tabulaire, au prix de l'extrapolation.
- [[Regression metrics]] — RMSE, MAE, MAPE, $R^2$ : laquelle et pourquoi.
- [[Analyse de survie]] — quand la cible est une durée partiellement observée (censure).
- [[Forecasting framing]] — quand la cible est une série temporelle.
- [[Types de données et choix de modèle]] — l'aiguillage amont.

## Pour aller plus loin

- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 3 (Linear Methods for Regression).
- Gelman & Hill — *Data Analysis Using Regression and Multilevel/Hierarchical Models*.
- Documentation scikit-learn — *Linear Models* et *Generalized Linear Models*.
