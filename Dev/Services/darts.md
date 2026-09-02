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

## Pourquoi

darts (Unit8) unifie la prévision de séries temporelles derrière une **API unique fit/predict à la scikit-learn** : des modèles classiques (ARIMA, ETS, Theta, Prophet, TBATS) aux modèles ML (wrappers scikit-learn, LightGBM, XGBoost, CatBoost) jusqu'aux réseaux de neurones (N-BEATS, N-HiTS, TFT, TiDE, TSMixer) via PyTorch Lightning. Objet `TimeSeries` central, support uni/multivarié, covariables passées et futures, backtesting, ensembles, prévision probabiliste et détection d'anomalies dans une seule bibliothèque.

## Quand l'utiliser

- **Comparer rapidement** plusieurs familles de modèles (statistiques / ML / DL) avec la même interface.
- Pipelines de prévision complets : covariables, backtesting, prévision probabiliste, réconciliation hiérarchique.
- Détection d'anomalies sur séries (wrap de modèles de prévision ou de PyOD).
- Entraînement GPU/TPU de modèles neuronaux sans écrire la boucle PyTorch.

## Quand NE PAS l'utiliser

- Prévision de très nombreuses séries en un temps minimal → [[statsforecast]].
- Catalogue de réseaux neuronaux le plus large et le plus récent → [[neuralforecast]].
- Une seule série saisonnière simple à prévoir vite, interprétable → [[Prophet]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; `uv add darts` (variantes `u8darts` pour installer sans les dépendances lourdes). Rien à héberger.
- Pur Python ; modèles DL sur PyTorch Lightning → entraînement GPU/TPU mono-machine. Pas de training distribué multi-nœuds natif.

## Pièges

- Tout passe par l'objet `TimeSeries` : anticiper la conversion depuis pandas/polars (fréquence régulière, valeurs manquantes).
- Modèles globaux (ML, DL) entraînés sur plusieurs séries : bien distinguer `past_covariates` et `future_covariates`, source d'erreurs.
- Dépendances lourdes (PyTorch) : utiliser la variante allégée si seuls les modèles classiques servent.

## Alternatives

- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[pmdarima]] — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.
- [[Chronos]] — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params). Approche voisine (zero-shot deep learning) plutôt que concurrent direct ; darts peut l'intégrer comme modèle.

## Liens

- [[Forecasting framing]] — son backtesting intégré matérialise le cadrage (horizon, covariables, origine glissante).
- [[PyTorch]] — backend (Lightning) des modèles neuronaux de darts.
- Intègre comme modèles [[LightGBM]], [[XGBoost]], [[CatBoost]] et [[Prophet]].
- Doc : https://unit8co.github.io/darts/
