---
galaxie: dev
type: service
nom: statsforecast
alias: [nixtla-statsforecast]
pitch: "Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray)."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Prophet|Prophet]]", "[[Dev/Services/neuralforecast|neuralforecast]]", "[[Dev/Services/darts|darts]]", "[[Dev/Services/pmdarima|pmdarima]]"]
remplace_par: []
status: actif
tags: [forecasting, timeseries, distributed]
url_docs: https://nixtlaverse.nixtla.io/statsforecast/
url_repo: https://github.com/Nixtla/statsforecast
---

# statsforecast

## Pourquoi

statsforecast (Nixtla) offre les implémentations **les plus rapides** des modèles statistiques de prévision — AutoARIMA, AutoETS, AutoCES, Theta, MSTL — compilées en JIT par **Numba**. Pensée pour ajuster efficacement des **millions de séries**, avec compatibilité native Spark / Dask / Ray, prévision probabiliste (intervalles de confiance) et variables exogènes.

## Quand l'utiliser

- **Beaucoup de séries** à prévoir vite, avec des modèles statistiques solides comme baseline.
- Sélection automatique (AutoARIMA / AutoETS) sans tuning manuel.
- Passage à l'échelle distribué (Spark, Dask, Ray) sans changer d'API.
- Établir une référence forte avant de tenter du neuronal.

## Quand NE PAS l'utiliser

- Modèles neuronaux / dépendances non linéaires complexes → [[Dev/Services/neuralforecast|neuralforecast]], [[Dev/Services/darts|darts]].
- Une seule série saisonnière à expliquer simplement (effets calendaires) → [[Dev/Services/Prophet|Prophet]].
- Ingénierie de features ML poussée et covariables très riches sous une même API → [[Dev/Services/darts|darts]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; `uv add statsforecast`. Rien à héberger.
- Accélération **Numba** (premier appel : compilation ~5 s, puis < 0,2 s). Distribué nativement via Spark / Dask / Ray.
- Écosystème Nixtla (interopère avec [[Dev/Services/neuralforecast|neuralforecast]] et utilsforecast).

## Pièges

- Premier appel lent (compilation Numba) — normal, ne pas le confondre avec une lenteur réelle.
- Format long strict (`unique_id`, `ds`, `y`) et fréquence (`freq`) à respecter scrupuleusement.
- Modèles statistiques : ne capturent pas les relations non linéaires complexes.

## Alternatives

- [[Dev/Services/Prophet|Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- [[Dev/Services/neuralforecast|neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[Dev/Services/darts|darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Dev/Services/pmdarima|pmdarima]] — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.

## Liens

- [[ARIMA SARIMA]] — AutoARIMA est l'un de ses modèles phares.
- [[Exponential smoothing]] — AutoETS implémente le cadre ETS.
- [[Forecasting framing]] — cadrer horizon, covariables et évaluation en amont.
- [[Dev/Services/neuralforecast|neuralforecast]] — pendant neuronal du même écosystème Nixtla.
- Doc : https://nixtlaverse.nixtla.io/statsforecast/
