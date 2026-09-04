---
role: brique
nom: neuralforecast
alias: [nixtla-neuralforecast]
pitch: "Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[statsforecast]]", "[[darts]]", "[[Prophet]]"]
complements: []
tags: [forecasting, timeseries, deep-learning, gpu]
url_docs: https://nixtlaverse.nixtla.io/neuralforecast/
url_repo: https://github.com/Nixtla/neuralforecast
---

# neuralforecast

<!-- AUTO:BANDEAU:START -->
> Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

neuralforecast (Nixtla) rassemble sous une API commune une trentaine d'architectures
neuronales de prévision, du MLP et du RNN aux modèles les plus récents — NBEATS, NHITS, TFT,
PatchTST, iTransformer, TimesNet, TimeLLM. Bâtie sur PyTorch Lightning, elle vise l'usage
plutôt que la recherche : classes `Auto*` qui règlent les hyperparamètres via Ray ou Optuna,
prévision probabiliste par quantiles ou distributions, covariables exogènes et statiques. Le
modèle est global — il s'entraîne sur l'ensemble des séries à la fois, ce qui suppose d'en
avoir assez, et assez d'historique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tirer le meilleur des réseaux sur un parc de séries, avec des architectures éprouvées prêtes à l'emploi | Peu de données, ou une seule série courte : le modèle global n'a pas de quoi apprendre et perd contre les modèles statistiques |
| Entraînement global multi-séries, avec covariables, sur GPU | Pas de GPU et beaucoup de séries à traiter vite : le temps d'entraînement devient l'obstacle |
| Prévision probabiliste (quantiles, distributions) et décomposition interprétable | Horizon `h`, fenêtre d'entrée et `futr_exog` mal cadrés : c'est par là que le futur fuit |
| Sélection automatique d'architecture et recherche d'hyperparamètres distribuée via Ray | Pas d'entraînement multi-nœuds natif : seule la sélection de modèles se distribue |

## Mise en œuvre

- Installation — `uv add neuralforecast`
- Point d'entrée — API Python `NeuralForecast(models=[...], freq=...)`, puis `fit` / `predict` sur un DataFrame long
- Prérequis — PyTorch ; un GPU en pratique ; Ray ou Optuna pour les classes `Auto*`
- Exécution — GPU mono-machine pour l'entraînement ; seule la sélection de modèles se distribue (Ray)
- Coût — gratuit, Apache-2.0 ; rien à héberger, le coût réel est celui du GPU

## Écosystème

### Alternatives

- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.

## Ressources

- Documentation — https://nixtlaverse.nixtla.io/neuralforecast/
- Dépôt — https://github.com/Nixtla/neuralforecast

## Voir aussi

- [[Forecasting framing]] — la notion à poser en amont : horizon, covariables, évaluation
- [[PyTorch]] — le framework (Lightning) sous ses modèles
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
