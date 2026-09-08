---
role: brique
nom: pmdarima
alias: [pyramid-arima, auto-arima, pmd]
pitch: "AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[statsforecast]]", "[[darts]]"]
complements: []
tags: [forecasting, timeseries]
url_docs: https://alkaline-ml.com/pmdarima/
url_repo: https://github.com/alkaline-ml/pmdarima
---

# pmdarima

<!-- AUTO:BANDEAU:START -->
> AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2025-11-17 |
<!-- AUTO:BANDEAU:END -->

## Définition

pmdarima (ex-pyramid-arima) porte en Python l'`auto.arima` de R : `auto_arima` choisit les
ordres $(p,d,q)(P,D,Q)$ d'un SARIMA par tests de racine unitaire pour la différenciation, puis
minimisation d'un critère d'information sur un espace restreint par la recherche *stepwise* de
Hyndman-Khandakar. Il enveloppe statsmodels (SARIMAX) derrière une interface familière à
scikit-learn — `fit` / `predict`, pipelines, Box-Cox, termes de Fourier — avec variables
exogènes, diagnostics de résidus et intervalles de prédiction. L'ajustement se fait série par
série, sans vectorisation.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| AutoARIMA sur une série, ou quelques-unes, sans régler les ordres à la main | Un ajustement par série, non vectorisé : la lenteur devient rédhibitoire dès que les séries se multiplient |
| Baseline statistique interprétable, avec diagnostics de résidus et intervalles | `m`, la période saisonnière, est à fournir et conditionne tout : 12 en mensuel annuel, 7 en journalier hebdomadaire |
| Pipelines à la scikit-learn : Box-Cox, termes de Fourier, différenciation | `stepwise=True` par défaut peut manquer l'optimum global ; la recherche exhaustive, elle, coûte cher |
| Rester proche de statsmodels tout en automatisant la boucle Box-Jenkins | Hypothèses ARIMA héritées : modèle linéaire, série à stationnariser au préalable → [[Stationarity]] |
| | Non-linéarités fortes, parc de séries, covariables riches : le terrain des modèles globaux → [[neuralforecast]] |

## Mise en œuvre

- Installation — `uv add pmdarima`
- Point d'entrée — API Python `pmdarima.auto_arima(...)`, et `pmdarima.pipeline.Pipeline` pour enchaîner les transformations
- Prérequis — statsmodels, NumPy et SciPy ; extension Cython compilée, embarquée dans les roues
- Exécution — CPU, mono-machine, une série à la fois
- Coût — gratuit, MIT ; rien à héberger

## Écosystème

### Alternatives

- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.

## Ressources

- Documentation — https://alkaline-ml.com/pmdarima/
- Dépôt — https://github.com/alkaline-ml/pmdarima

## Voir aussi

- [[ARIMA SARIMA]] — la notion : le modèle dont pmdarima automatise la sélection
- [[Forecasting framing]] — cadrer horizon, exogènes et évaluation avant d'ajuster
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
