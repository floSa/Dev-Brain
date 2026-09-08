---
role: brique
nom: statsforecast
alias: [nixtla-statsforecast]
pitch: "Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray)."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Prophet]]", "[[neuralforecast]]", "[[darts]]", "[[pmdarima]]"]
complements: []
tags: [forecasting, timeseries, distributed]
url_docs: https://nixtlaverse.nixtla.io/statsforecast/
url_repo: https://github.com/Nixtla/statsforecast
---

# statsforecast

<!-- AUTO:BANDEAU:START -->
> Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-16 |
<!-- AUTO:BANDEAU:END -->

## Définition

statsforecast (Nixtla) donne les implémentations les plus rapides des modèles statistiques de
prévision — AutoARIMA, AutoETS, AutoCES, Theta, MSTL — compilées en JIT par Numba. L'entrée est
un tableau au format long strict (`unique_id`, `ds`, `y`) et la même API se distribue
nativement sur Spark, Dask et Ray : c'est ce qui lui permet de viser le million de séries.
Prévision probabiliste par intervalles et variables exogènes comprises. Le premier appel
paraît lent : c'est la compilation, pas le modèle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Beaucoup de séries à prévoir vite, avec des modèles statistiques solides comme référence | Format long strict (`unique_id`, `ds`, `y`) et `freq` à respecter scrupuleusement |
| Sélection automatique (AutoARIMA, AutoETS) sans réglage manuel | Modèles statistiques : ils ne captent pas les dépendances non linéaires complexes |
| Passage à l'échelle distribué (Spark, Dask, Ray) sans changer d'API | Premier appel lent, le temps de la compilation Numba — à ne pas confondre avec une lenteur réelle |
| Établir une référence forte avant de tenter du neuronal | Ingénierie de variables poussée et covariables très riches : ce n'est pas son terrain |

## Mise en œuvre

- Installation — `uv add statsforecast`
- Point d'entrée — API Python `StatsForecast(models=[...], freq=...)`, puis `forecast` / `cross_validation` sur un DataFrame long
- Prérequis — Numba ; un cluster Spark, Dask ou Ray seulement pour le distribué
- Exécution — CPU multicœur mono-machine, ou distribué sur Spark, Dask et Ray sans changer d'API
- Coût — gratuit, Apache-2.0 ; rien à héberger

## Écosystème

### Alternatives

- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- [[neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[pmdarima]] — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.

## Ressources

- Documentation — https://nixtlaverse.nixtla.io/statsforecast/
- Dépôt — https://github.com/Nixtla/statsforecast

## Voir aussi

- [[ARIMA SARIMA]] — la notion derrière AutoARIMA, son modèle phare
- [[Exponential smoothing]] — le cadre ETS qu'implémente AutoETS
- [[Forecasting framing]] — cadrer horizon, covariables et évaluation en amont
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
