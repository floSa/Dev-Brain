---
role: comparatif
nom: Comparatif - Forecasting
categorie: ml/series-temporelles
tags: [forecasting, timeseries]
---

# Comparatif - Forecasting

> On tranche sur : entraîner un modèle par série, un modèle global, ou n'en entraîner aucun — puis le nombre de séries à couvrir et le budget de calcul, CPU compilé ou GPU.

![[Comparatif - Forecasting.base]]

## Ce qui départage

- [[statsforecast]] — les mêmes modèles statistiques (AutoARIMA, AutoETS, Theta, MSTL) **compilés par Numba** et distribuables sur Spark/Dask/Ray : c'est le seul qui vise le million de séries. Format long strict (`unique_id`, `ds`, `y`), et un premier appel lent qui est la compilation, pas une lenteur.
- [[pmdarima]] — `auto.arima` de R porté en Python, en **enveloppant statsmodels** : diagnostics de résidus et boucle Box-Jenkins automatisée, sur une interface scikit-learn. Un ajustement **par série, non vectorisé** — d'où statsforecast dès que les séries se multiplient.
- [[Prophet]] — modèle **additif interprétable** : tendance à points de rupture + saisonnalités de Fourier + jours fériés, robuste aux trous et aux aberrations, réglable par un non-spécialiste. Un modèle = **une seule série**, et il est mal adapté à la demande intermittente.
- [[darts]] — une **API unique** `fit`/`predict` de l'ARIMA aux réseaux (N-BEATS, TFT, TiDE), donc le seul lieu où comparer les trois familles sans changer d'interface. Tout transite par l'objet `TimeSeries`, et la distinction `past_covariates` / `future_covariates` est la source d'erreurs.
- [[neuralforecast]] — le **catalogue neuronal** le plus large et le plus récent (NHITS, PatchTST, iTransformer, TimesNet), avec sélection automatique `Auto*` via Ray/Optuna. Exige assez d'historique et assez de séries : sur petits jeux, il perd contre les modèles statistiques.
- [[Chronos]] — **modèle de fondation** : il prévoit une série jamais vue en zero-shot, sans pipeline par série, quantiles compris ; Chronos-2 gère le multivarié et les covariables par *in-context learning*. Le pari ne bat pas toujours un modèle dédié, et les scores de leaderboard sont exposés à la fuite de pré-entraînement.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
