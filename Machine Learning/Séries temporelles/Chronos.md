---
role: brique
nom: Chronos
alias: [Chronos-T5, Chronos-Bolt, Chronos-2, chronos-forecasting]
pitch: "Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params)."
categorie: ml/series-temporelles
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[darts]]", "[[Prophet]]"]
complements: []
tags: [forecasting, timeseries, foundation-model, transformers, deep-learning]
url_docs: https://github.com/amazon-science/chronos-forecasting
url_repo: https://github.com/amazon-science/chronos-forecasting
---

# Chronos

<!-- AUTO:BANDEAU:START -->
> Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | à jour · 2026-07-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Pré-entraîné par Amazon sur d'immenses corpus de séries hétérogènes, il prévoit une série
jamais vue en zero-shot, sans pipeline ni réglage par série. La première génération tokenise
les valeurs — mise à l'échelle, puis discrétisation en bins — et entraîne un seq2seq bâti sur
T5, exactement comme un modèle de langue ; Chronos-Bolt en est la variante allégée. Chronos-2
(2025) abandonne la tokenisation discrète pour un encoder-only multivarié natif (~120 M
params) qui absorbe covariables et séries liées par *in-context learning*. La sortie est
probabiliste : les quantiles donnent les intervalles sans calibration.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Baseline immédiate sans pipeline par série : démarrage à froid, parc de séries hétérogènes | Le pari zero-shot ne bat pas toujours un modèle dédié bien réglé : évaluer sur ses propres données avant d'adopter → [[Walk-forward CV]] |
| Intervalles probabilistes attendus sans calibration manuelle | Les scores de leaderboard sont exposés à la fuite de pré-entraînement : la série de test a pu être vue à l'entraînement |
| Prévision multivariée ou avec covariables, en zero-shot (Chronos-2) | Beaucoup de séries à prévoir vite sans GPU : le coût d'inférence devient l'obstacle → [[statsforecast]] |
| Prototypage : une prévision forte par défaut avant d'investir dans un modèle dédié | Catalogue de réseaux à entraîner ou fine-tuner soi-même → [[neuralforecast]] |
| | Une seule série longue et stationnaire : un modèle statistique bien réglé suffit pour bien moins cher → [[ARIMA SARIMA]] |

## Mise en œuvre

- Installation — `uv add chronos-forecasting` ; poids ouverts, distribués via [[HuggingFace]]
- Point d'entrée — API Python `BaseChronosPipeline.from_pretrained(...)`, puis `predict_quantiles` ; intégrable comme modèle dans darts et AutoGluon-TimeSeries
- Prérequis — GPU conseillé au-delà de 100 M de paramètres ; Chronos-Bolt allège pour le CPU et l'edge
- Exécution — inférence mono-machine, rien de managé ; le modèle se charge dans un runtime local
- Coût — gratuit, poids sous Apache-2.0 ; le coût réel est celui du GPU d'inférence

## Écosystème

### Alternatives

- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.

## Ressources

- Documentation — https://github.com/amazon-science/chronos-forecasting

## Voir aussi

- [[Foundation models pour séries temporelles]] — la notion dont Chronos est l'un des modèles phares
- [[Forecasting framing]] — cadrer horizon, fuite et covariables reste nécessaire, même en zero-shot
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
