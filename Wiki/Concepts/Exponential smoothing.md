---
galaxie: wiki
type: concept
nom: Exponential smoothing
alias: [Lissage exponentiel, ETS, Holt-Winters, SES, Holt, AutoETS]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries]
---

# Exponential smoothing

## Aperçu

- Prévision par **moyenne pondérée** des observations passées, les poids décroissant exponentiellement vers le passé : le récent compte plus que l'ancien.
- Du plus simple (niveau seul) au complet (niveau + tendance + saison), c'est une baseline rapide, robuste et souvent redoutable face à des modèles plus lourds.

## Concepts clés

### SES → Holt → Holt-Winters
- **SES** (simple) : lisse un **niveau** seul (paramètre $\alpha$), pour séries sans tendance ni saison. **Holt** : ajoute une **tendance** ($\beta$). **Holt-Winters** : ajoute la **saisonnalité** ($\gamma$), additive ou multiplicative.

### Cadre ETS (Error, Trend, Seasonal)
- Formulation en **espace d'états** : chaque composante est additive (A), multiplicative (M) ou absente (N). Les combinaisons (≈30 modèles) sont départagées automatiquement par AIC — c'est ce que fait AutoETS.

### Tendance amortie (damped)
- La tendance s'**aplatit** à long horizon au lieu de filer à l'infini. Souvent plus réaliste et plus précise sur horizon long que la tendance linéaire pure.

### Additif vs multiplicatif
- Saison **additive** quand l'amplitude saisonnière est stable ; **multiplicative** quand elle croît avec le niveau (sinon, passer au log puis additif).

## Les maths, simplement

- SES : $\hat{y}_{t+1} = \alpha\, y_t + (1-\alpha)\, \hat{y}_t$, avec $0 < \alpha < 1$. Le lissage est récursif.
- En déroulant la récurrence : $\hat{y}_{t+1} = \sum_{k \ge 0} \alpha (1-\alpha)^k\, y_{t-k}$ — des poids **géométriques** qui décroissent avec l'ancienneté $k$.

## En pratique

- **AutoETS** sélectionne automatiquement la forme (E,T,S) par AIC : laisser faire plutôt que choisir à la main.
- Ne requiert **pas** la [[Stationarity|stationnarité]] (modélise tendance et saison directement), contrairement à [[ARIMA SARIMA|ARIMA]] — atout sur séries à tendance/saison marquées.
- Outils : [[Dev/Services/statsforecast|statsforecast]] (AutoETS rapide à grande échelle), [[Dev/Services/darts|darts]] (modèles ETS sous API unifiée).

## Approches voisines & alternatives

- [[ARIMA SARIMA]] — famille concurrente : ETS par lissage des composantes, ARIMA par autocorrélation. Tout ETS linéaire admet un équivalent ARIMA, mais ETS couvre aussi des cas non linéaires (saison multiplicative).
- [[Stationarity]] — non requise par ETS, ce qui le distingue d'ARIMA.
- [[Forecasting framing]] — cadre l'horizon et l'évaluation ; ETS sert souvent de baseline.

## Pour aller plus loin

- Hyndman, Koehler, Ord, Snyder (2008) — *Forecasting with Exponential Smoothing: The State Space Approach*.
- Hyndman & Athanasopoulos — FPP3, ch. 8 (exponential smoothing).
