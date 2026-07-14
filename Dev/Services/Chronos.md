---
galaxie: dev
type: service
nom: Chronos
alias: [Chronos-T5, Chronos-Bolt, Chronos-2, chronos-forecasting]
pitch: "Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params)."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/darts|darts]]", "[[Dev/Services/Prophet|Prophet]]"]
remplace_par: []
status: actif
tags: [forecasting, timeseries, foundation-model, transformers, deep-learning]
url_docs: https://github.com/amazon-science/chronos-forecasting
url_repo: https://github.com/amazon-science/chronos-forecasting
---

# Chronos

## Pourquoi

Chronos (Amazon) est un **modèle de fondation pour séries temporelles** : pré-entraîné sur d'immenses corpus de séries hétérogènes, il prévoit une série jamais vue en **zero-shot**, sans entraîner ni régler un modèle par série. La première génération **tokenise** les valeurs — mise à l'échelle puis discrétisation en bins — et entraîne un **seq2seq bâti sur T5**, exactement comme un modèle de langue. *Chronos-Bolt* est une variante plus rapide et plus légère. **Chronos-2** (2025) abandonne la tokenisation discrète pour un **encoder-only multivarié natif** (~120 M params) qui gère par *in-context learning* le forecasting univarié, multivarié et avec covariables. Sortie probabiliste (quantiles) → intervalles de prédiction natifs.

## Quand l'utiliser

- **Baseline immédiate** sans pipeline par série : démarrage à froid (peu d'historique), parc de séries hétérogènes.
- Besoin d'**intervalles probabilistes** sans calibration manuelle.
- Prévision **multivariée / avec covariables** en zero-shot (Chronos-2).
- Prototypage rapide d'une prévision « forte par défaut » avant d'investir dans un modèle dédié.

## Quand NE PAS l'utiliser

- Une seule série longue et stationnaire où un modèle statistique bien réglé suffit pour bien moins cher → [[Dev/Services/statsforecast|statsforecast]], [[ARIMA SARIMA]].
- Beaucoup de séries à prévoir vite sur CPU, sans GPU → [[Dev/Services/statsforecast|statsforecast]].
- Catalogue de réseaux neuronaux à entraîner / fine-tuner soi-même → [[Dev/Services/neuralforecast|neuralforecast]].
- Contraintes fortes de latence / budget GPU, ou domaine très spécifique où un modèle dédié fine-tuné l'emporte.

## Déploiement & coût

- Poids ouverts (Apache-2.0), gratuits, accessibles via [[Dev/Services/HuggingFace|HuggingFace]] ; `pip install chronos-forecasting`. Rien de managé : self-host.
- Inférence sur **GPU conseillée** (modèles 100 M+ params) ; mono-machine. Chronos-Bolt allège pour le CPU / l'edge.
- Intégrable comme modèle dans [[Dev/Services/darts|darts]] et dans AutoGluon-TimeSeries.

## Pièges

- Le pari zero-shot ne **bat pas toujours** un modèle dédié bien réglé : évaluer sur SES données avant d'adopter.
- Risque de **fuite de pré-entraînement** (série de test vue à l'entraînement) qui gonfle les scores de leaderboard — juger en [[Walk-forward CV]].
- Coût d'inférence GPU non négligeable pour de très nombreuses séries.

## Alternatives

- [[Dev/Services/darts|darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Dev/Services/Prophet|Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.

## Liens

- [[Foundation models pour séries temporelles]] — le concept dont Chronos est l'un des modèles phares (tokenisation, panorama, évaluation).
- [[Forecasting framing]] — cadrer le problème (horizon, fuite, covariables) reste indispensable même en zero-shot.
- [[Walk-forward CV]] — l'évaluation honnête sur ses propres données, face au battage des leaderboards.
- Voisins statistiques/neuronaux : [[Dev/Services/statsforecast|statsforecast]], [[Dev/Services/neuralforecast|neuralforecast]].
- Doc / poids : https://github.com/amazon-science/chronos-forecasting
