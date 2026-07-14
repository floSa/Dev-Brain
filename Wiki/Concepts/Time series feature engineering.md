---
galaxie: wiki
type: concept
nom: Time series feature engineering
alias: [Features temporelles, Lag features, Rolling features, Fourier terms, Time series features]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries, feature-engineering]
---

# Time series feature engineering

## Aperçu

- Transformer une série (ou un parc de séries) en **table de features** exploitable par un modèle ML/global : gradient boosting, réseaux. C'est le principal levier de précision d'un forecasting ML.
- Le danger central est la **fuite temporelle** : toute feature doit n'utiliser que le passé disponible à l'instant de prévision.

## Concepts clés

### Lags
- Valeurs décalées $y_{t-k}$. Le choix des décalages est guidé par l'[[Autocorrelation|ACF/PACF]] et la saisonnalité (lag 7 pour du quotidien hebdomadaire, lag 12 pour du mensuel annuel).

### Fenêtres glissantes
- Statistiques (moyenne, écart-type, min/max, médiane) sur une fenêtre **fermée au passé** (jusqu'à $t-1$). Captent niveau et volatilité locaux. Une fenêtre incluant $t$ fuite la cible.

### Calendrier & Fourier
- Heure, jour de semaine, mois, jours fériés, indicateurs d'événements. Pour des saisonnalités multiples ou longues, des **termes de Fourier** $\sin/\cos$ encodent la périodicité avec peu de paramètres.

### Covariables passées vs futures
- Distinction critique (cf. [[Forecasting framing]]) : n'utiliser au temps $t+h$ qu'une variable **réellement connue d'avance** (calendrier, prix planifié) — jamais une mesure qui ne sera disponible qu'après.

### Transformations de cible
- Log / Box-Cox (stabiliser la variance), différenciation (retirer tendance), désaisonnalisation. À **réajuster dans chaque fenêtre d'entraînement**, pas sur tout l'historique.

## Les maths, simplement

- Moyenne glissante de fenêtre $w$ : $\bar y_t^{(w)}=\frac{1}{w}\sum_{i=1}^{w} y_{t-i}$ (somme close à $t-1$).
- Terme de Fourier d'ordre $k$ pour une saison $m$ : $\sin\!\big(\tfrac{2\pi k t}{m}\big),\ \cos\!\big(\tfrac{2\pi k t}{m}\big)$ — quelques harmoniques suffisent à approcher une saisonnalité lisse.

## En pratique

- Pièges de fuite : fenêtres fermées au passé, scaler/encodage **ajustés sur le train seulement**, pas de feature au temps $t+h$ indisponible à la prévision.
- Modèle **global** (un seul modèle sur toutes les séries via ces features) pour passer à l'échelle — [[Dev/Services/neuralforecast|neuralforecast]] côté réseaux. `tsfresh` extrait des centaines de features automatiquement (à filtrer).
- Valider en [[Walk-forward CV]] : une feature qui « améliore » en in-sample peut fuiter.

## Approches voisines & alternatives

- [[Ingénierie des caractéristiques]] — le cadre général dont ceci est la déclinaison temporelle.
- [[Forecasting framing]] — covariables passées vs futures, et la fuite temporelle.
- [[Walk-forward CV]] — le protocole qui valide ces features sans fuite.
- [[Autocorrelation]] — ACF/PACF orientent le choix des lags.

## Pour aller plus loin

- Christ et al. — `tsfresh` (extraction et sélection automatiques de features de séries).
- Solutions M5 sur Kaggle — l'art des lags et fenêtres glissantes pour le boosting.
- Hyndman & Athanasopoulos — FPP3, ch. 7 (time series regression, Fourier terms).
