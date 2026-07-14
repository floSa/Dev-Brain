---
galaxie: wiki
type: concept
nom: Autocorrelation
alias: [Autocorrélation, ACF, PACF, Fonction d'autocorrélation, Corrélogramme]
categorie: concept/ts
domaines: [data-sci]
tags: [timeseries, stochastic-process]
---

# Autocorrelation

## Aperçu

- Corrélation d'une série avec une version d'elle-même **décalée** de $k$ pas. Mesure la mémoire et la dépendance temporelle d'une série.
- C'est l'outil de diagnostic central des séries : il révèle saisonnalité, persistance, non-stationnarité, et guide le choix des ordres d'un modèle ARMA.

## Concepts clés

### ACF — fonction d'autocorrélation
- $\rho(k)$ = corrélation entre $y_t$ et $y_{t-k}$, tracée par le **corrélogramme**. Une décroissance lente trahit une tendance ou une racine unitaire (cf. [[Stationarity]]).

### PACF — autocorrélation partielle
- Corrélation entre $y_t$ et $y_{t-k}$ **après avoir retiré** l'effet des décalages intermédiaires $1, \dots, k-1$. Distingue la dépendance directe de la dépendance transitive.

### Lecture pour identifier ARMA
- **AR($p$)** : la PACF coupe net après le rang $p$, l'ACF décroît progressivement. **MA($q$)** : l'ACF coupe net après $q$, la PACF décroît. C'est le cœur de la méthode Box-Jenkins.

### Saisonnalité & bruit blanc
- Des pics aux multiples de la période (lag 12 pour du mensuel annuel) signalent une saison. Un **bruit blanc** a une ACF nulle partout — l'objectif visé pour les **résidus** d'un bon modèle, vérifié par le test de **Ljung-Box**.

## Les maths, simplement

- $\rho(k) = \dfrac{\gamma(k)}{\gamma(0)} = \dfrac{\mathrm{Cov}(y_t,\, y_{t-k})}{\mathrm{Var}(y_t)}$, valeur dans $[-1, 1]$, avec $\rho(0) = 1$.
- Bandes de significativité approximatives $\pm \dfrac{1{,}96}{\sqrt{n}}$ : au-delà, l'autocorrélation est jugée non nulle (sous hypothèse de bruit blanc).

## En pratique

- ACF/PACF restent le diagnostic visuel de référence pour proposer $(p, q)$ avant ajustement, puis Ljung-Box sur les résidus pour confirmer qu'il ne reste plus de structure exploitable.
- Une autocorrélation forte des résidus = modèle sous-spécifié ; une ACF qui ne décroît pas = différencier d'abord.
- Outils : `statsmodels` (`plot_acf`, `plot_pacf`, `acorr_ljungbox`) ; [[Dev/Services/statsforecast|statsforecast]] et [[Dev/Services/darts|darts]] s'appuient dessus en interne pour AutoARIMA.

## Approches voisines & alternatives

- [[Stationarity]] — l'ACF diagnostique la non-stationnarité (décroissance lente, racine unitaire).
- [[ARIMA SARIMA]] — ACF et PACF identifient directement les ordres $p$ (AR) et $q$ (MA).
- [[Forecasting framing]] — l'analyse d'autocorrélation fait partie de l'exploration en amont du choix de modèle.

## Pour aller plus loin

- Box & Jenkins — *Time Series Analysis: Forecasting and Control* (identification par ACF/PACF).
- Hyndman & Athanasopoulos — FPP3, §2.8–2.9 (autocorrelation, white noise).
