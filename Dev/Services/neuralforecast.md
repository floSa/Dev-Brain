---
galaxie: dev
type: service
nom: neuralforecast
alias: [nixtla-neuralforecast]
pitch: "Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/statsforecast|statsforecast]]", "[[Dev/Services/darts|darts]]", "[[Dev/Services/Prophet|Prophet]]"]
remplace_par: []
status: actif
tags: [forecasting, timeseries, deep-learning, gpu]
url_docs: https://nixtlaverse.nixtla.io/neuralforecast/
url_repo: https://github.com/Nixtla/neuralforecast
---

# neuralforecast

## Pourquoi

neuralforecast (Nixtla) fournit des implémentations rapides et homogènes de **30+ architectures neuronales de prévision** — du MLP/RNN aux modèles récents (NBEATS, NHITS, TFT, PatchTST, iTransformer, TimesNet, TimeLLM). Bâtie sur PyTorch (Lightning), elle privilégie l'usabilité : API commune, sélection automatique de modèle (classes `Auto*` via Ray/Optuna), prévision probabiliste, covariables exogènes et statiques.

## Quand l'utiliser

- Tirer le meilleur des **réseaux de neurones** pour la prévision, avec des modèles éprouvés prêts à l'emploi.
- Jeux de **multiples séries** (entraînement global) avec covariables et accès GPU.
- Prévision probabiliste (quantiles, distributions) et décomposition interprétable (tendance/saisonnalité).
- Sélection automatique d'architecture + HPO distribué via Ray.

## Quand NE PAS l'utiliser

- Peu de données ou une seule série courte : un modèle statistique est plus sûr → [[Dev/Services/statsforecast|statsforecast]], [[Dev/Services/Prophet|Prophet]].
- Besoin des modèles classiques et ML sous une même API → [[Dev/Services/darts|darts]].
- Pas de GPU et forte contrainte de temps sur beaucoup de séries → [[Dev/Services/statsforecast|statsforecast]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; `uv add neuralforecast`. Rien à héberger.
- PyTorch → entraînement/inférence GPU mono-machine ; passage à l'échelle surtout sur la **sélection de modèles** (Ray/Optuna), pas de training multi-nœuds natif.
- Partie de l'écosystème Nixtla (interopère avec [[Dev/Services/statsforecast|statsforecast]] et utilsforecast).

## Pièges

- Les réseaux exigent assez d'historique et de séries : sur petits jeux, ils perdent face aux modèles statistiques.
- Réglage de l'horizon (`h`), de la fenêtre d'entrée et des covariables : risque de fuite (`futr_exog` mal cadrées).
- Coût GPU et temps d'entraînement non négligeables face à statsforecast.

## Alternatives

- [[Dev/Services/statsforecast|statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[Dev/Services/darts|darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Dev/Services/Prophet|Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — framework sous-jacent (Lightning) des modèles.
- [[Dev/Services/statsforecast|statsforecast]] — pendant statistique du même écosystème Nixtla.
- Doc : https://nixtlaverse.nixtla.io/neuralforecast/
