---
galaxie: wiki
type: concept
nom: Forecasting framing
alias: [Cadrage forecasting, Cadrage d'une prévision, Forecasting problem framing]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries]
---

# Forecasting framing

## Aperçu

- Avant de choisir un modèle, cadrer le problème de prévision : que prédit-on, à quel **horizon**, à quelle **fréquence**, avec quelles données disponibles, et comment on **évalue**.
- Une erreur de cadrage — surtout la fuite d'information du futur — invalide silencieusement n'importe quel modèle, aussi sophistiqué soit-il. Le cadrage prime sur le choix d'algorithme.

## Concepts clés

### Horizon & fréquence
- Combien de pas en avant prédire ($h$) et à quelle résolution (heure, jour, semaine). Prévision à **un pas** vs **multi-pas**. Trois stratégies multi-pas : récursive (réinjecter ses prédictions), directe (un modèle par horizon), multi-sorties (prédire le vecteur d'un coup).

### Local vs global, uni- vs multivarié
- Une série isolée vs un **parc** de séries. Modèle **local** (un modèle par série, ex. un ARIMA chacune) vs **global** (un seul modèle entraîné sur toutes les séries, ex. un réseau de neurones). Le global apprend des régularités partagées et passe mieux à l'échelle.

### Covariables passées vs futures
- Distinction critique pour éviter la fuite : les **covariables passées** ne sont connues que jusqu'à l'instant courant (ex. une mesure capteur), les **covariables futures** sont connues d'avance (calendrier, jours fériés, prix planifié, météo prévue). N'utiliser une variable au temps $t+h$ que si elle sera réellement disponible à la prévision.

### Backtesting à origine glissante
- Évaluer en avançant l'**origine de prévision** dans le temps (fenêtre glissante ou extensible), jamais en entraînant sur des dates postérieures au test. C'est le [[Validation croisée|TimeSeriesSplit]] / walk-forward — le seul protocole honnête en temporel.

### Cible & baseline
- Transformer la cible si utile (log, différenciation, désaisonnalisation) et toujours fixer une **baseline naïve** à battre : la *seasonal naive* (« demain = même jour la semaine dernière ») est souvent étonnamment dure à dépasser.

## Les maths, simplement

- On estime $\hat{y}_{t+h\mid t} = f\big(y_{\le t},\, x\big)$ : la valeur à l'horizon $h$ sachant le passé observé jusqu'à $t$ et des covariables $x$. Le conditionnement « $\mid t$ » dit explicitement quelle information est autorisée.
- Distinguer la **perte d'entraînement** (ex. pinball/quantile pour une prévision probabiliste) de la **métrique d'évaluation** rapportée (MAPE, MASE…). Optimiser l'une ne garantit pas l'autre.

## En pratique

- Piège n°1 : la **fuite temporelle** (entraîner sur le futur, standardiser sur tout l'historique, utiliser une covariable indisponible à la prévision). Tout pré-traitement s'ajuste *dans* la fenêtre d'entraînement.
- Choisir la métrique selon l'usage (échelle, zéros, asymétrie sur/sous-stock) avant de comparer les modèles.
- Outils : [[Dev/Services/darts|darts]] (backtesting et `historical_forecasts` intégrés), [[Dev/Services/statsforecast|statsforecast]] (cross-validation temporelle à grande échelle), [[Dev/Services/Prophet|Prophet]] (baseline interprétable), [[Dev/Services/pmdarima|pmdarima]] (AutoARIMA sur une série, interface scikit-learn). Protocole d'éval : [[Validation croisée]] (TimeSeriesSplit).

## Approches voisines & alternatives

- [[Stationarity]] — propriété à vérifier avant un modèle ARMA ; oriente les transformations de la cible.
- [[Autocorrelation]] — diagnostic de la structure temporelle (mémoire, saisonnalité) en amont du choix de modèle.
- [[ARIMA SARIMA]] / [[Exponential smoothing]] — les familles statistiques classiques, baselines à cadrer correctement avant tout modèle ML/DL.
- [[Validation croisée]] — la CV temporelle (TimeSeriesSplit) matérialise le backtesting à origine glissante.

## Pour aller plus loin

- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice* (FPP3), ch. 5 (the forecaster's toolbox).
- Nixtla — documentation de la cross-validation temporelle (`cross_validation`).
