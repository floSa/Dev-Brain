---
galaxie: wiki
type: concept
nom: Forecasting metrics
alias: [Métriques de prévision, MAPE, sMAPE, MASE, WAPE, RMSSE, pinball loss, forecast accuracy]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries, model-evaluation]
---

# Forecasting metrics

## Aperçu

- Mesurent l'écart entre série prévue et série observée. Spécificité temporelle : l'échelle varie d'une série à l'autre, il y a des zéros et l'erreur peut être asymétrique (sur- vs sous-stock).
- Le choix de métrique précède la comparaison des modèles. Une mauvaise métrique (MAPE sur des séries à zéros) classe faux silencieusement.

## Concepts clés

### Erreurs d'échelle : MAE, RMSE
- Dans l'unité de la cible (lisibles), mais **dépendent de l'échelle** : non comparables entre séries de magnitudes différentes. RMSE pénalise davantage les grosses erreurs que MAE. Pendants temporels des [[Regression metrics]].

### Erreurs relatives : MAPE, sMAPE, WAPE
- En pourcentage, donc comparables entre échelles. **MAPE** explose près de zéro et pénalise plus la sur-prévision (asymétrique). **sMAPE** symétrise mais reste instable. **WAPE** (MAD/Mean) pondère par le volume — robuste, courante en supply chain.

### Erreurs scaled : MASE, RMSSE
- Normalisées par l'erreur d'une **baseline naïve** (souvent la *seasonal naive*) calculée sur le train. Sans dimension, comparables entre séries, **définies même avec des zéros**. Métriques officielles des compétitions M4 (MASE) et M5 (RMSSE) ; valeur < 1 = bat la naïve.

### Prévision probabiliste : pinball, coverage
- Évaluer un **intervalle/quantile**, pas un point. La perte **pinball** (quantile loss) note un quantile prédit ; le **coverage** vérifie qu'un intervalle à 90 % contient bien ~90 % des réalisations. CRPS agrège sur tous les quantiles.

### Biais vs dispersion
- ME / MPE mesurent le **biais** (tendance à sur- ou sous-prévoir), à distinguer de la magnitude (MAE/RMSE). Un biais systématique se corrige ; une dispersion élevée non.

## Les maths, simplement

- $\text{MAPE}=\dfrac{100}{n}\sum_t\dfrac{|y_t-\hat y_t|}{|y_t|}$ ; $\text{WAPE}=\dfrac{\sum_t|y_t-\hat y_t|}{\sum_t|y_t|}$.
- $\text{MASE}=\dfrac{\text{MAE}}{\frac{1}{n-m}\sum_{t=m+1}^{n}|y_t-y_{t-m}|}$ : MAE divisée par celle de la *seasonal naive* de période $m$ ($m=1$ si non saisonnier). RMSSE en est la version quadratique.
- Perte pinball au quantile $\tau$ : $L_\tau(y,\hat q)=\max\big(\tau(y-\hat q),\,(\tau-1)(y-\hat q)\big)$ — pénalise asymétriquement selon le quantile visé.

## En pratique

- Multi-séries / portefeuille hétérogène → **MASE ou RMSSE** par défaut (comparables, robustes aux zéros). MAPE/WAPE pour communiquer un % métier, jamais sur des séries à zéros.
- Toute métrique se lit sur un **backtest** à origine glissante ([[Walk-forward CV]]), jamais en in-sample.
- Toujours rapporter face à une **baseline naïve** : une RMSE brute ne dit rien sans point de comparaison.
- Outils : [[Dev/Services/statsforecast|statsforecast — utilsforecast.losses (mase, rmsse, mape…)]], [[Dev/Services/darts|darts.metrics]].

## Approches voisines & alternatives

- [[Regression metrics]] — les métriques de régression (MSE, MAE, R²) dont celles-ci sont la déclinaison temporelle.
- [[Forecasting framing]] — choisit la métrique selon l'usage (échelle, zéros, asymétrie) avant de modéliser.
- [[Walk-forward CV]] — le protocole sur lequel ces métriques sont agrégées.
- [[Intermittent demand]] — le cas où MAPE s'effondre et où MASE/RMSSE s'imposent.
- [[Hierarchical forecasting]] — métriques à évaluer à chaque niveau d'agrégation.

## Pour aller plus loin

- Hyndman & Koehler (2006) — *Another look at measures of forecast accuracy* (introduit le MASE).
- Makridakis et al. — compétitions M4 (2020, MASE) et M5 (2022, RMSSE et pinball pondéré).
