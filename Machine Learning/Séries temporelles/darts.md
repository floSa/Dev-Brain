---
role: brique
nom: darts
alias: [u8darts, unit8-darts]
pitch: "Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Prophet]]", "[[statsforecast]]", "[[neuralforecast]]", "[[pmdarima]]", "[[Chronos]]"]
complements: []
tags: [forecasting, timeseries, deep-learning]
url_docs: https://unit8co.github.io/darts/
url_repo: https://github.com/unit8co/darts
---

# darts

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

darts (Unit8) met une API unique `fit` / `predict`, à la scikit-learn, devant trois familles de
modèles : les classiques (ARIMA, ETS, Theta, TBATS, Prophet), les modèles ML enveloppés
(scikit-learn, LightGBM, XGBoost, CatBoost) et les réseaux (N-BEATS, N-HiTS, TFT, TiDE,
TSMixer) sur PyTorch Lightning. C'est donc le seul endroit du dossier où comparer les trois
familles sans changer d'interface. Tout transite par un objet `TimeSeries` — fréquence
régulière, trous explicites — et s'y ajoutent backtesting, ensembles, prévision probabiliste,
réconciliation hiérarchique et détection d'anomalies.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer plusieurs familles de modèles (statistiques, ML, DL) sous la même interface | Tout passe par l'objet `TimeSeries` : la conversion depuis pandas ou polars (fréquence régulière, valeurs manquantes) est un préalable à anticiper |
| Pipeline complet : covariables, backtesting, prévision probabiliste, réconciliation hiérarchique | Modèles globaux entraînés sur plusieurs séries : confondre `past_covariates` et `future_covariates` est l'erreur classique, et elle fait fuiter le futur |
| Détection d'anomalies sur série, en enveloppant un modèle de prévision ou PyOD | Dépendances lourdes (PyTorch) : préférer la variante `u8darts` si seuls les modèles classiques servent |
| Entraîner un réseau sur GPU sans écrire la boucle PyTorch | Pas d'entraînement distribué multi-nœuds natif : l'échelle s'arrête à la machine |

## Mise en œuvre

- Installation — `uv add darts`, ou `u8darts` pour la variante sans les dépendances lourdes
- Point d'entrée — API Python : un objet `TimeSeries`, puis `model.fit(...)` / `model.predict(...)`, et `historical_forecasts` pour le backtesting
- Prérequis — PyTorch Lightning pour les modèles neuronaux seulement ; les modèles classiques s'en passent
- Exécution — CPU mono-machine ; GPU ou TPU pour les modèles neuronaux, sans multi-nœuds
- Coût — gratuit, Apache-2.0 ; rien à héberger

## Écosystème

### Alternatives

- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[pmdarima]] — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.
- [[Chronos]] — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params). Approche voisine, que darts peut d'ailleurs intégrer comme modèle.

## Ressources

- Documentation — https://unit8co.github.io/darts/
- Dépôt — https://github.com/unit8co/darts

## Voir aussi

- [[Forecasting framing]] — la notion que son backtesting matérialise : horizon, covariables, origine glissante
- [[PyTorch]] — le backend (Lightning) de ses modèles neuronaux
- [[LightGBM]] · [[XGBoost]] · [[CatBoost]] — les gradient boostings qu'il enveloppe comme modèles de prévision
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
