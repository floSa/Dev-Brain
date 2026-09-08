---
role: brique
nom: Prophet
alias: [fbprophet, fb-prophet]
pitch: "Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python/R
alternatives: ["[[statsforecast]]", "[[neuralforecast]]", "[[darts]]", "[[Chronos]]"]
complements: []
tags: [forecasting, timeseries]
url_docs: https://facebook.github.io/prophet/
url_repo: https://github.com/facebook/prophet
---

# Prophet

<!-- AUTO:BANDEAU:START -->
> Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python/R | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-15 |
<!-- AUTO:BANDEAU:END -->

## Définition

Décompose une série en un modèle additif : une tendance, linéaire ou logistique, à points de
rupture ; des saisonnalités multiples exprimées en séries de Fourier ; des effets de jours
fériés et d'événements. L'ajustement, porté par Stan, encaisse les trous, les valeurs
aberrantes et les changements de régime. Le parti pris est l'interprétabilité : chaque
composante se lit et se règle séparément, ce qu'un analyste peut faire sans expertise en
séries temporelles. La contrepartie est structurelle — un modèle vaut pour une seule série.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Série métier à forte saisonnalité, plusieurs années d'historique (trafic, ventes, demande) | Un modèle = une seule série : un parc impose de boucler et de paralléliser soi-même, ce qui coûte cher à grande échelle |
| Prévision rapide et interprétable, intervalles compris, par un non-spécialiste | Demande intermittente, beaucoup de zéros : le modèle additif y est mal adapté → [[Intermittent demand]] |
| Effets calendaires connus à injecter : jours fériés, promotions, événements | Série courte ou sans saisonnalité marquée : un ETS ou un ARIMA suffit → [[Exponential smoothing]] |
| Baseline en quelques lignes, en Python comme en R | Tendance logistique : `cap` et `floor` sont à fixer explicitement, oubli fréquent |
| | Sur-réaction aux ruptures de tendance, à borner par `changepoint_prior_scale` |

## Mise en œuvre

- Installation — `uv add prophet` ; privilégier les roues précompilées, sinon l'installation traîne la compilation Stan
- Point d'entrée — API Python et R : `Prophet().fit(df)` sur un DataFrame à colonnes `ds` et `y`
- Prérequis — le backend Stan (C++), embarqué dans les roues ; aucune infrastructure
- Exécution — CPU, mono-machine ; le passage à l'échelle se fait série par série, en parallélisant
- Coût — gratuit, MIT ; développement en mode maintenance chez Meta depuis 2023 environ

## Écosystème

### Alternatives

- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[Chronos]] — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params). Approche voisine zero-shot, pas un concurrent direct du modèle additif.

## Ressources

- Documentation — https://facebook.github.io/prophet/
- Dépôt — https://github.com/facebook/prophet

## Voir aussi

- [[Forecasting framing]] — cadrer horizon, covariables et évaluation avant de choisir un modèle
- [[Comparatif - Forecasting]] — ce qui départage les briques du dossier
