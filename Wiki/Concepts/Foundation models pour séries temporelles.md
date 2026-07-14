---
galaxie: wiki
type: concept
nom: Foundation models pour séries temporelles
alias: [Time series foundation models, TSFM, Modèles de fondation séries temporelles, Foundation models time series, Zero-shot forecasting]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [timeseries, forecasting, transformers, deep-learning]
---

# Foundation models pour séries temporelles

## Aperçu

- Grands modèles **pré-entraînés sur d'immenses corpus de séries hétérogènes**, utilisables en **zero-shot** (ou few-shot) sur une série jamais vue, sans entraîner un modèle par série. C'est la transposition du paradigme « modèle de fondation » des LLM au forecasting.
- Promesse : une **baseline forte prête à l'emploi**, surtout en *cold-start* (peu d'historique) ou sur un parc hétérogène. Contrepartie : coût d'inférence (modèles 100 M+ paramètres, GPU) et gains qui ne battent pas toujours un modèle dédié bien réglé.

## Concepts clés

### Le pari du zero-shot
- Le pré-entraînement massif sur des millions de séries fait émerger une capacité de généralisation : prévoir une série inédite **sans fit**. Le few-shot consiste à fine-tuner légèrement le modèle sur le domaine cible.

### Représentation de la série en entrée
- **Patching** : découper la série en *patches* contigus, chacun traité comme un token (façon ViT) — réduit la longueur de séquence (TimesFM, PatchTST).
- **Tokenisation par quantification** : mettre à l'échelle puis discrétiser les valeurs en un « vocabulaire » de bins, et entraîner comme un modèle de langue (Chronos). Parallèle direct avec la [[Tokenization]] en NLP.
- **Any-variate** : aplatir un nombre variable de variables/covariables dans une même séquence (Moirai).

### Architectures
- **Encoder-only** (Moirai 1.0, MOMENT), **decoder-only autorégressif** (TimesFM, Lag-Llama, Moirai 2.0), **tokenisation + seq2seq** (Chronos, bâti sur T5). La plupart reposent sur les [[Transformer architectures]] et la [[Self-attention]] ; quelques modèles légers s'en écartent (TTM = MLP-Mixer).

### Panorama des modèles
- **TimeGPT** (Nixtla, 2023) — premier modèle de fondation commercial, accès par API.
- **Lag-Llama** (2024) — decoder-only open, prévision probabiliste.
- [[Dev/Services/Chronos|Chronos]] (Amazon) — tokenisation de valeurs sur T5 ; *Chronos-Bolt* plus rapide ; **Chronos-2** (2025) abandonne la tokenisation discrète pour un encoder-only à *group attention*, multivarié natif (~120 M params).
- **Moirai** (Salesforce) — any-variate ; **Moirai 2.0** (août 2025) passe en decoder-only, ~30× moins de paramètres pour de meilleurs scores.
- **TimesFM** (Google) — decoder-only *patched* ; **TimesFM 2.5** (sept. 2025) reprend la tête de GIFT-Eval avec ~200 M params.
- **MOMENT** (CMU), **Tiny Time Mixers / TTM** (IBM, minuscules pour l'edge).

### Sortie probabiliste
- La plupart produisent des **quantiles** ou une distribution → intervalles de prédiction natifs, pas seulement une trajectoire moyenne.

### Évaluation
- **GIFT-Eval** (Salesforce) : ~23 jeux de données, ~144 000 séries, 7 domaines, 10 fréquences, avec leaderboard et corpus de pré-entraînement *non-leaking*. Le risque cardinal : la **fuite** (séries de test présentes dans le pré-entraînement) qui gonfle artificiellement les scores.

## Les maths, simplement

- Zero-shot : prédire $\hat y_{t+1:t+h} = f_\theta(y_{1:t})$ avec $\theta$ **figé**, appris une fois pour toutes sur un corpus $\mathcal{D}$ de millions de séries — aucun ajustement sur la série cible.
- Tokenisation (Chronos) : mise à l'échelle $\tilde y = y/\text{scale}$ puis quantification en un des $B$ bins → un « mot ». Entraînement par entropie croisée, exactement comme un modèle de langue.
- Patching : la série de longueur $L$ est découpée en patches de taille $p$, ramenant la séquence à $L/p$ tokens — d'où un coût d'attention divisé par $p^2$.

## En pratique

- **Quand** : baseline immédiate sans pipeline par série, démarrage à froid, parc de séries hétérogènes, besoin d'intervalles probabilistes sans calibration manuelle.
- **Quand éviter** : une seule série longue et stationnaire où [[ARIMA SARIMA]] / [[Exponential smoothing]] suffisent à moindre coût ; contraintes fortes de latence / budget GPU ; domaine très spécifique où un modèle dédié fine-tuné l'emporte.
- **Évaluer sur SES données** en [[Walk-forward CV]] avec les bonnes [[Forecasting metrics]] — ne pas se fier au seul leaderboard (risque de fuite de pré-entraînement).
- **Accès** : poids ouverts de Chronos, Moirai, TimesFM, MOMENT via [[Dev/Services/HuggingFace|HuggingFace]] ; architectures récentes voisines (NHITS, PatchTST, TFT) dans [[Dev/Services/neuralforecast|neuralforecast]] ; backtesting et intégration via [[Dev/Services/darts|darts]] ; TimeGPT par l'API Nixtla. Distillation / quantization pour alléger l'inférence.

## Approches voisines & alternatives

- [[Forecasting framing]] — cadrer le problème (horizon, fuite, covariables) reste indispensable, même en zero-shot.
- [[ARIMA SARIMA]] / [[Exponential smoothing]] — baselines statistiques souvent encore compétitives pour bien moins cher.
- [[Time series feature engineering]] — l'approche ML/global que les modèles de fondation cherchent à court-circuiter.
- [[Transformer architectures]] / [[Self-attention]] — le socle technique de la plupart de ces modèles.
- [[Scaling laws]] — le pari d'échelle hérité des LLM, transposé au temporel.
- [[Forecasting metrics]] / [[Walk-forward CV]] — l'évaluation honnête, indispensable face au battage des leaderboards.

## Pour aller plus loin

- Garza, Mergenthaler-Canseco et al. (2023) — *TimeGPT-1* (Nixtla).
- Ansari et al. (2024) — *Chronos: Learning the Language of Time Series* (Amazon).
- Das, Kumar, Sen et al. (2024) — *A decoder-only foundation model for time-series forecasting* (TimesFM, Google).
- Woo et al. (2024) — *Unified Training of Universal Time Series Forecasting Transformers* (Moirai, Salesforce).
- Aksu et al. (2024) — *GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation* (arXiv 2410.10393) + leaderboard.
