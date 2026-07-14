---
galaxie: wiki
type: concept
nom: ARIMA SARIMA
alias: [ARIMA, SARIMA, ARMA, Box-Jenkins, AutoARIMA]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries]
---

# ARIMA SARIMA

## Aperçu

- Famille de modèles linéaires combinant **autorégression** (AR), **différenciation** (I) et **moyenne mobile** (MA). SARIMA ajoute une composante saisonnière.
- Référence historique de la prévision statistique : interprétable, bien outillé, et une baseline solide via la sélection automatique AutoARIMA.

## Concepts clés

### AR, I, MA
- **AR($p$)** : $y_t$ régressé sur ses $p$ valeurs passées. **MA($q$)** : $y_t$ fonction des $q$ erreurs passées. **I($d$)** : différenciation $d$ fois pour atteindre la [[Stationarity|stationnarité]] avant d'ajuster l'ARMA.

### SARIMA
- Notation $(p,d,q)(P,D,Q)_m$ : mêmes composantes répétées au pas saisonnier $m$ (12 pour du mensuel annuel). Capture une saisonnalité régulière par différenciation et termes saisonniers.

### Identification Box-Jenkins
- Stationnariser → lire l'[[Autocorrelation|ACF/PACF]] pour proposer $p$ et $q$ → ajuster → **diagnostiquer les résidus** (doivent être un bruit blanc, test de Ljung-Box) → départager par AIC/BIC. **AutoARIMA** automatise toute cette boucle.

### Exogènes (ARIMAX)
- Ajout de régresseurs externes (jours fériés, prix) : la composante linéaire accueille des covariables, à condition qu'elles soient disponibles à l'horizon de prévision (cf. [[Forecasting framing]]).

## Les maths, simplement

- Avec l'opérateur retard $B$ ($B y_t = y_{t-1}$) : $\;\phi(B)\,(1-B)^d\, y_t = \theta(B)\,\varepsilon_t$, où $\phi$ est le polynôme AR, $\theta$ le polynôme MA, $(1-B)^d$ la différenciation, et $\varepsilon_t$ un bruit blanc.
- Exemple ARIMA(1,1,0) : $(1-\phi_1 B)(1-B) y_t = \varepsilon_t$ — un AR(1) sur la série différenciée une fois.

## En pratique

- Préférer **AutoARIMA** au réglage manuel : il explore $(p,d,q)(P,D,Q)$ par critère d'information et tests de racine unitaire.
- Modèle **linéaire** : il ne capte pas les non-linéarités ; [[Exponential smoothing|ETS]] le concurrence souvent à armes égales sur séries simples.
- Outils : [[Dev/Services/pmdarima|pmdarima]] (AutoARIMA pur Python, wrap statsmodels), [[Dev/Services/statsforecast|statsforecast]] (AutoARIMA compilé Numba, à grande échelle), [[Dev/Services/darts|darts]] (mêmes modèles sous une API unifiée).

## Approches voisines & alternatives

- [[Exponential smoothing]] — l'autre famille classique : ETS modélise tendance/saison par lissage, ARIMA par autocorrélation. Comparées systématiquement ; tout ETS linéaire a un équivalent ARIMA, l'inverse est faux.
- [[Stationarity]] — prérequis : le « I » différencie jusqu'à stationnarité.
- [[Autocorrelation]] — ACF/PACF déterminent les ordres $p$ et $q$.
- [[Forecasting framing]] — cadre l'horizon, les exogènes et l'évaluation.

## Pour aller plus loin

- Box & Jenkins (1970) — *Time Series Analysis: Forecasting and Control*.
- Hyndman & Athanasopoulos — FPP3, ch. 9 (ARIMA models).
