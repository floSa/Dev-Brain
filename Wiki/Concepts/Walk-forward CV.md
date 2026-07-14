---
galaxie: wiki
type: concept
nom: Walk-forward CV
alias: [Validation glissante, Backtesting, Rolling origin, Expanding window, Time series cross-validation, cutoff, cutoffs]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [timeseries, model-evaluation, resampling]
---

# Walk-forward CV

## Aperçu

- Protocole d'évaluation temporel : avancer l'**origine de prévision** dans le temps et toujours tester sur du futur. Le seul honnête en séries temporelles, où l'ordre interdit d'entraîner sur des dates postérieures au test.
- Matérialise le **backtesting** : on rejoue, à plusieurs origines, l'enchaînement « entraîner → prévoir → mesurer », puis on moyenne.

## Concepts clés

### Origine glissante vs extensible
- **Expanding** : la fenêtre d'entraînement grandit à chaque origine (tout le passé). **Rolling** : fenêtre de taille fixe qui glisse (oublie le passé lointain) — utile en présence de dérive.

### Backtesting / historical forecasts
- Répéter prévision + évaluation à des origines successives $t_1<t_2<\dots$ et agréger les [[Forecasting metrics]]. Donne une estimation stable, par opposition à un unique découpage train/test.

### Gap / purge / embargo
- Insérer un **trou** entre fin du train et début du test pour neutraliser la fuite quand des features à long lag (ou des fenêtres glissantes) chevauchent la frontière. Purge/embargo = la version stricte (López de Prado).

### Multi-horizon
- Évaluer à chaque horizon $h$ et agréger par horizon : la précision se dégrade en général quand $h$ croît, ce qui se voit mal sur une métrique globale.

### vs K-Fold
- Un K-Fold aléatoire entraînerait sur le futur pour prédire le passé → **fuite temporelle**. C'est exactement le `TimeSeriesSplit` de la [[Validation croisée]].

## Les maths, simplement

- Pour des origines $t_1,\dots,t_n$ : $\widehat{\text{err}}=\dfrac{1}{n}\sum_{i=1}^{n} L\big(y_{t_i+1:t_i+h},\ \hat y_{t_i+1:t_i+h\mid t_i}\big)$ — chaque terme n'utilise que l'information jusqu'à $t_i$.
- L'écart-type des erreurs sur les origines renseigne sur la **stabilité** dans le temps (régimes, ruptures), pas seulement sur le niveau moyen d'erreur.

## En pratique

- **Coûteux** : un réentraînement par origine. Compromis fréquent → réentraîner moins souvent qu'on ne prédit (refit périodique, prédiction à chaque pas).
- Fixer le **gap = horizon** quand les features chevauchent la frontière train/test, sinon fuite.
- Outils : [[Dev/Services/statsforecast|statsforecast — cross_validation]], [[Dev/Services/darts|darts — historical_forecasts / backtest]], [[Dev/Services/Scikit-Learn|sklearn — TimeSeriesSplit]].

## Approches voisines & alternatives

- [[Validation croisée]] — la CV générale dont ceci est la déclinaison temporelle (TimeSeriesSplit en détail).
- [[Forecasting framing]] — où le backtesting à origine glissante est posé comme protocole d'évaluation.
- [[Forecasting metrics]] — ce que l'on agrège sur les origines.
- [[Data leakage]] — la fuite temporelle que ce protocole prévient.

## Pour aller plus loin

- Hyndman & Athanasopoulos — FPP3, ch. 5.10 (time series cross-validation / evaluation on a rolling origin).
- Nixtla — documentation `cross_validation` (backtesting à grande échelle).
- López de Prado — *Advances in Financial Machine Learning* (purged & embargoed CV).
