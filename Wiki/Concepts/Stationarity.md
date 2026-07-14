---
galaxie: wiki
type: concept
nom: Stationarity
alias: [Stationnarité, Série stationnaire, Stationnaire, Racine unitaire]
categorie: concept/ts
domaines: [data-sci]
tags: [timeseries, stochastic-process]
---

# Stationarity

## Aperçu

- Une série est **stationnaire** quand ses propriétés statistiques (moyenne, variance, structure d'autocovariance) ne changent pas dans le temps.
- C'est l'hypothèse de base de nombreux modèles (ARMA) : on ne peut extrapoler que ce qui est stable. La plupart des séries réelles ne le sont pas — il faut les y ramener.

## Concepts clés

### Forte vs faible (au second ordre)
- Stationnarité **forte** : toute la loi jointe est invariante par translation temporelle (exigeante, rarement testée). Stationnarité **faible** : seuls moyenne, variance et autocovariance le sont — suffisant pour la modélisation linéaire.

### Sources de non-stationnarité
- **Tendance** (moyenne qui dérive), **saisonnalité** (motif périodique), **variance changeante** (hétéroscédasticité), et la **racine unitaire** (marche aléatoire : le choc d'aujourd'hui persiste indéfiniment).

### Rendre stationnaire
- **Différenciation** d'ordre $d$ ($y_t - y_{t-1}$) contre la tendance — c'est le « I » de [[ARIMA SARIMA]]. **Différenciation saisonnière** d'ordre $D$ au pas $m$ contre la saison. **Log / Box-Cox** pour stabiliser une variance croissante. Désaisonnalisation explicite.

### Tests
- **ADF** (Augmented Dickey-Fuller) : $H_0$ = présence d'une racine unitaire (non stationnaire). **KPSS** : $H_0$ = stationnaire — complémentaire, à lire avec l'ADF. Phillips-Perron en variante robuste.

## Les maths, simplement

- Stationnarité faible : $E[y_t] = \mu$ et $\mathrm{Var}(y_t) = \sigma^2$ constants, et $\mathrm{Cov}(y_t, y_{t+k}) = \gamma(k)$ ne dépend que du décalage $k$, pas de $t$.
- Marche aléatoire $y_t = y_{t-1} + \varepsilon_t$ : $\mathrm{Var}(y_t) = t\,\sigma^2$ croît avec le temps → non stationnaire. Une seule différence $\Delta y_t = \varepsilon_t$ la rend stationnaire (bruit blanc).

## En pratique

- Croiser **ADF + KPSS** : un seul test induit en erreur (un ADF non significatif ne prouve pas la stationnarité). Les deux d'accord → conclusion solide.
- Ne pas **sur-différencier** : différencier au-delà du nécessaire injecte de l'autocorrélation négative artificielle et gonfle la variance.
- Outils : [[Dev/Services/statsforecast|statsforecast]] et [[Dev/Services/darts|darts]] choisissent $d$/$D$ automatiquement via AutoARIMA ; `statsmodels` fournit `adfuller` et `kpss`.

## Approches voisines & alternatives

- [[Autocorrelation]] — l'ACF qui décroît très lentement signale une non-stationnarité (racine unitaire).
- [[ARIMA SARIMA]] — le « I » est exactement la différenciation qui stationnarise.
- [[Exponential smoothing]] — ne requiert **pas** la stationnarité (modélise tendance et saison directement), contrairement à ARIMA : un point de choix entre les deux.
- [[Forecasting framing]] — la stationnarité oriente les transformations de la cible au cadrage.

## Pour aller plus loin

- Dickey & Fuller (1979) — test de racine unitaire.
- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice* (FPP3), §9.1 (stationarity and differencing).
