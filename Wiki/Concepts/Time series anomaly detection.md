---
galaxie: wiki
type: concept
nom: Time series anomaly detection
alias: [Détection d'anomalies temporelles, Outliers temporels, Time series anomaly, anomaly detection, matrix profile, discord]
categorie: concept/ts
domaines: [data-sci, mlops]
tags: [timeseries, anomaly-detection]
---

# Time series anomaly detection

## Aperçu

- Repérer les points ou segments d'une série qui s'écartent du comportement normal : pannes de capteurs, fraudes, incidents, ruptures.
- Spécificité temporelle : la dépendance, la saisonnalité et la dérive font que « anormal » est **contextuel** — une valeur banale en été peut être aberrante en hiver.

## Concepts clés

### Types d'anomalies
- **Ponctuelle** (un pic isolé), **contextuelle** (normale dans l'absolu mais pas à ce moment), **collective** (une sous-séquence entière anormale alors que chaque point pris seul semble ordinaire).

### Approche par résidus
- Modéliser le « normal » par une prévision ([[ARIMA SARIMA]], [[Exponential smoothing]], décomposition STL) puis signaler les **résidus extrêmes** (z-score, IQR). L'anomalie est ce que le modèle n'explique pas.

### Décomposition & seuils saisonniers
- STL sépare tendance / saison / résidu ; le test ESD sur le résidu (S-H-ESD, Twitter) gère la saisonnalité et évite de confondre un pic saisonnier normal avec une anomalie.

### Méthodes distance / ML
- **Isolation forest** sur features temporelles (cf. [[Time series feature engineering]]), détecteurs multivariés sur fenêtres ([[Détection d'outliers multivariée]]) ; [[Autoencodeurs|autoencodeurs]] / LSTM jugés sur l'erreur de reconstruction.

### Matrix profile
- Pour chaque sous-séquence de longueur $m$, distance euclidienne **z-normalisée** à sa plus proche voisine ailleurs dans la série. Une sous-séquence sans voisine proche est un **discord** = anomalie de **forme** ; la plus répétée est un **motif**.
- **Sans hypothèse de modèle, quasi sans paramètre** (sauf $m$) ; le même calcul livre motifs, discords, segmentation et chaînes. Implémenté à l'échelle par [[Dev/Services/STUMPY|STUMPY]] (Numba/Dask/GPU).

### Évaluation & seuils
- Anomalies = **classe rare** : précision/rappel sur événements (souvent *range-based*), mêmes pièges que la [[Imbalanced classification]]. Labels rares ou absents → seuils calibrés sur un historique « propre ».

## Les maths, simplement

- Score par résidu standardisé : $s_t=\dfrac{|y_t-\hat y_t|}{\hat\sigma}$ ; alerte si $s_t>\kappa$ (typiquement $\kappa=3$).
- Matrix profile : $P_i=\min_{j\,:\,|i-j|\geq m} d\big(T_{i,m},T_{j,m}\big)$, $d$ = distance euclidienne **z-normalisée** (on compare des **formes**, pas des niveaux). **Discord** $=\arg\max_i P_i$ (anomalie), **motif** $=\arg\min_i P_i$ (répétition).

## En pratique

- Distinguer détection **en ligne** (streaming, contrainte de latence, pas de futur) et **batch** (rétrospective, tout l'historique disponible).
- Retirer saisonnalité et dérive avant de juger l'écart, sinon avalanche de faux positifs ([[Stationarity]], [[Autocorrelation]]).
- Cousin du monitoring de production : la dérive de distribution (*data drift*) d'un modèle se surveille avec les mêmes outils.
- Outils : isolation forest via [[Dev/Services/Scikit-Learn|sklearn.ensemble.IsolationForest]] ; [[Dev/Services/STUMPY|STUMPY]] pour le matrix profile (discords, motifs). Détecteurs multivariés génériques → [[Détection d'outliers multivariée]].
- Fenêtre $m$ du matrix profile **déterminante** : trop courte → bruit, trop longue → anomalie noyée ; la caler sur la période physique du phénomène.
- Cas **statique** (point aberrant relativement à une distribution, pas à une dynamique) → [[Détection d'outliers univariée]] sur les résidus, [[Détection d'outliers multivariée]] en tabulaire.

## Approches voisines & alternatives

- [[Détection d'outliers univariée]] — seuillage statistique (Z-score/IQR/MAD), souvent appliqué aux résidus du modèle.
- [[Détection d'outliers multivariée]] — variante **statique** (LOF, Isolation Forest, ECOD/COPOD), sans dimension temporelle.
- [[Forecasting framing]] — le « normal » se modélise comme une prévision ; l'anomalie est le résidu.
- [[Maintenance prédictive et RUL]] — la détection de l'amorce de défaut déclenche le pronostic (RUL) en maintenance prédictive.
- [[Time series feature engineering]] — les features sur lesquelles tournent isolation forest et compagnie.
- [[Stationarity]] / [[Autocorrelation]] — saisonnalité et dérive à retirer avant de juger l'écart.
- [[Imbalanced classification]] — anomalies = classe rare, mêmes pièges d'évaluation.
- [[DBSCAN]] — détection d'outliers par densité, transposable aux sous-séquences.

## Pour aller plus loin

- Hochenbaum, Vallis & Kejariwal — Twitter AnomalyDetection (S-H-ESD).
- Yeh et al. (2016) — *Matrix Profile I* ; implémentation [[Dev/Services/STUMPY|STUMPY]].
- Blázquez-García et al. (2021) — *A Review on Outlier/Anomaly Detection in Time Series Data*.
- Numenta Anomaly Benchmark (NAB) — protocole d'évaluation en streaming.
