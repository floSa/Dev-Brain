---
galaxie: dev
type: service
nom: Prophet
alias: [fbprophet, fb-prophet]
pitch: "Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python/R
scaling: single-node
alternatives: ["[[Dev/Services/statsforecast|statsforecast]]", "[[Dev/Services/neuralforecast|neuralforecast]]", "[[Dev/Services/darts|darts]]", "[[Dev/Services/Chronos|Chronos]]"]
remplace_par: []
status: actif
tags: [forecasting, timeseries]
url_docs: https://facebook.github.io/prophet/
url_repo: https://github.com/facebook/prophet
---

# Prophet

## Pourquoi

Prophet décompose une série temporelle en un **modèle additif** : tendance (linéaire ou logistique avec points de rupture) + saisonnalités multiples (annuelle, hebdomadaire, quotidienne, par séries de Fourier) + effets de jours fériés et d'événements. L'ajustement, porté par Stan, est robuste aux données manquantes, aux valeurs aberrantes et aux changements de tendance. Conçu pour qu'un analyste obtienne une prévision raisonnable en réglant des paramètres **interprétables**, sans expertise en séries temporelles.

## Quand l'utiliser

- Séries métier à **forte saisonnalité** avec plusieurs années d'historique (trafic, ventes, demande).
- Besoin d'une prévision **rapide et interprétable**, avec intervalles d'incertitude, par un non-spécialiste.
- Intégration d'effets calendaires connus (jours fériés, promotions, événements).
- Prototypage : une baseline solide en quelques lignes, en Python comme en R.

## Quand NE PAS l'utiliser

- Beaucoup de séries (milliers, millions) à prévoir vite → [[Dev/Services/statsforecast|statsforecast]].
- Modèles neuronaux récents ou covariables riches → [[Dev/Services/neuralforecast|neuralforecast]], [[Dev/Services/darts|darts]].
- Séries sans saisonnalité marquée ou très courtes : un modèle plus simple (ETS, ARIMA) suffit souvent.
- Demande **intermittente** (beaucoup de zéros) : Prophet est mal adapté.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add prophet`. Rien à héberger.
- Cœur d'inférence en **Stan** (C++) sous API Python et R. Mono-machine ; passage à l'échelle en parallélisant série par série (un modèle par série).
- Développée par l'équipe Core Data Science de Meta ; rythme de développement ralenti depuis ~2023 (mode maintenance), mais toujours utilisée et maintenue.

## Pièges

- Un modèle Prophet = **une seule série** : pour un parc de séries, boucler/paralléliser soi-même (coûteux à grande échelle).
- L'installation traîne le backend Stan (compilation) — privilégier les roues précompilées.
- Tendance logistique : nécessite de fixer `cap`/`floor` explicitement, oubli fréquent.
- Peut sur-réagir aux changements de tendance ; ajuster `changepoint_prior_scale`.

## Alternatives

- [[Dev/Services/statsforecast|statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[Dev/Services/neuralforecast|neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[Dev/Services/darts|darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Dev/Services/Chronos|Chronos]] — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params). Approche voisine zero-shot, pas un concurrent direct du modèle additif.

## Liens

- [[Forecasting framing]] — cadrer un problème de prévision (horizon, covariables, backtesting) avant de choisir Prophet.
- [[Dev/Services/darts|darts]] — intègre Prophet comme l'un de ses modèles classiques.
- Doc : https://facebook.github.io/prophet/
