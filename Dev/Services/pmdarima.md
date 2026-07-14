---
galaxie: dev
type: service
nom: pmdarima
alias: [pyramid-arima, auto-arima, pmd]
pitch: "AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/statsforecast|statsforecast]]", "[[Dev/Services/darts|darts]]"]
remplace_par: []
status: actif
tags: [forecasting, timeseries]
url_docs: https://alkaline-ml.com/pmdarima/
url_repo: https://github.com/alkaline-ml/pmdarima
---

# pmdarima

## Pourquoi

pmdarima (ex-pyramid-arima) apporte à Python l'équivalent de la fonction **auto.arima de R** : `auto_arima` choisit automatiquement les ordres $(p,d,q)(P,D,Q)$ d'un (S)ARIMA par tests de racine unitaire (différenciation) et minimisation d'un critère d'information. Il **enveloppe statsmodels** (SARIMAX) derrière une interface familière à scikit-learn (`fit` / `predict`, pipelines, transformations), avec variables exogènes et intervalles de prédiction.

## Quand l'utiliser

- Obtenir un **AutoARIMA** sur **une** série (ou quelques-unes) sans régler les ordres à la main.
- Baseline statistique interprétable, avec diagnostics de résidus et intervalles de confiance.
- Pipelines `pmdarima` (Box-Cox, termes de Fourier pour la saisonnalité, différenciation) à la scikit-learn.
- Rester proche de statsmodels tout en automatisant la boucle Box-Jenkins (cf. [[ARIMA SARIMA]]).

## Quand NE PAS l'utiliser

- **Beaucoup** de séries à ajuster vite → [[Dev/Services/statsforecast|statsforecast]] (AutoARIMA compilé Numba, des ordres de grandeur plus rapide).
- Comparer plusieurs familles (stats / ML / DL) sous une API unique → [[Dev/Services/darts|darts]].
- Non-linéarités fortes, parc de séries, covariables riches → modèles globaux ML/DL ([[Dev/Services/neuralforecast|neuralforecast]]).

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add pmdarima`. Rien à héberger.
- Cython + statsmodels / NumPy / SciPy ; **single-node** (CPU). La recherche `stepwise` (Hyndman-Khandakar) restreint l'espace exploré pour rester rapide sur une série.

## Pièges

- **Lenteur** dès que les séries se multiplient : un ajustement par série, non vectorisé — d'où statsforecast à l'échelle.
- `m` (période saisonnière) est **à fournir** et conditionne tout : `m=12` mensuel annuel, `m=7` journalier hebdomadaire…
- `stepwise=True` par défaut : plus rapide mais peut manquer l'optimum global (la recherche exhaustive, elle, est coûteuse).
- Hérite des hypothèses ARIMA : modèle **linéaire**, série à stationnariser (cf. [[Stationarity]]).

## Alternatives

- [[Dev/Services/statsforecast|statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[Dev/Services/darts|darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.

## Liens

- [[ARIMA SARIMA]] — le modèle sous-jacent ; pmdarima en automatise la sélection (AutoARIMA).
- [[Forecasting framing]] — cadrer horizon, exogènes et évaluation avant d'ajuster.
- [[Dev/Services/statsforecast|statsforecast]] — l'AutoARIMA moderne à grande échelle (même rôle, bien plus rapide).
- [[Dev/Services/darts|darts]] — API unifiée qui propose aussi AutoARIMA.
- Doc : https://alkaline-ml.com/pmdarima/
