---
role: hub
nom: Séries temporelles
alias: [forecasting, prévision]
pitch: Les bibliothèques dont l'entrée est indexée par le temps — prévoir, détecter une rupture, et valider sans tricher avec le futur.
domaines: [data-sci, ml-eng]
tags: [timeseries, forecasting, anomaly-detection, foundation-model]
---

# Séries temporelles

> Les bibliothèques dont l'entrée est indexée par le temps — prévoir, détecter une rupture, et valider sans tricher avec le futur.

## Ce qu'il faut comprendre

- **Ce dossier ne se distingue pas par ses algorithmes mais par une contrainte : l'ordre.** Un modèle de prévision fait de la régression, et rien n'interdit d'y mettre du gradient boosting ([[Tabulaire]]) ou un réseau profond ([[Apprentissage profond]]). Ce qui change est qu'on ne peut ni mélanger les lignes, ni utiliser une information postérieure à l'instant prédit. Toute la difficulté est là, et c'est aussi d'ici que vient la forme la plus commune de [[Data leakage]].
- **Le cadrage précède le modèle, et il est plus décisif que lui.** [[Forecasting framing]] : quel horizon, quelle fréquence, une prévision par point ou par intervalle, combien de séries, quelles covariables connues à l'avance. Un cadrage flou produit un score flatteur et une mise en production décevante.
- **La validation ne peut pas être une validation croisée ordinaire** : [[Walk-forward CV]] est le seul protocole honnête, parce qu'il n'entraîne jamais sur des données postérieures à ce qu'il prédit. Les métriques ont leurs pièges propres — échelle, zéros, saisonnalité — cf. [[Forecasting metrics]].
- **Les modèles statistiques classiques restent des références difficiles à battre**, surtout sur peu d'historique : [[ARIMA SARIMA]] et [[Exponential smoothing]]. Ils supposent des propriétés à vérifier d'abord — [[Stationarity]] et [[Autocorrelation]] sont les deux diagnostics à poser avant tout ajustement.
- **Le deep learning gagne quand il y a beaucoup de séries, pas beaucoup d'historique** : un réseau apprend des motifs partagés entre milliers de séries là où un modèle par série n'a rien à généraliser. Les [[Foundation models pour séries temporelles]] poussent l'idée jusqu'au zero-shot — plus aucun entraînement par série.
- **Trois situations métier cassent les modèles génériques** et méritent d'être reconnues avant de choisir : [[Hierarchical forecasting]], quand les prévisions doivent se sommer d'un niveau à l'autre ; [[Intermittent demand]], quand la série est majoritairement à zéro et qu'une erreur quadratique n'a plus de sens ; [[Maintenance prédictive et RUL]], où la cible est une durée de vie restante et non une valeur future.
- **La détection d'anomalies temporelle n'est pas la détection d'outliers** : ce qui est anormal est une *forme* dans le temps, pas une valeur extrême. [[Time series anomaly detection]] ; l'outillage tabulaire est au niveau du domaine, cf. [[Comparatif - Détection d'anomalies]].
- Enfin, la voie souvent la plus rentable : transformer le problème en tabulaire par [[Time series feature engineering]] — retards, fenêtres glissantes, calendrier — puis appliquer un modèle de [[Tabulaire]].

## Choisir

- Beaucoup de séries, du statistique, et de la vitesse → [[statsforecast]] : AutoARIMA et AutoETS compilés, jusqu'à des millions de séries.
- Un AutoARIMA façon R sur quelques séries → [[pmdarima]].
- Une prévision correcte sans expertise séries temporelles, avec saisonnalités et jours fériés → [[Prophet]].
- Des réseaux de neurones de prévision, récents et prêts à l'emploi → [[neuralforecast]].
- Une API unique pour comparer statistique et neuronal sur le même jeu → [[darts]].
- Prévoir sans entraîner de modèle par série → [[Chronos]]. Cf. [[Comparatif - Forecasting]].
- Chercher des motifs répétés ou des ruptures de forme → [[STUMPY]], par matrix profile.
- Transformer la série en colonnes puis modéliser → [[Tabulaire]] ; industrialiser le réentraînement → [[Suivi d'expériences]] et [[Serving]].

<!-- AUTO:START -->
### Notions
- [[ARIMA SARIMA]] — domaines : data-sci, ml-eng
- [[Autocorrelation]] — domaines : data-sci
- [[Exponential smoothing]] — domaines : data-sci, ml-eng
- [[Forecasting framing]] — domaines : data-sci, ml-eng
- [[Forecasting metrics]] — domaines : data-sci, ml-eng
- [[Foundation models pour séries temporelles]] — domaines : data-sci, ml-eng
- [[Hierarchical forecasting]] — domaines : data-sci, ml-eng
- [[Intermittent demand]] — domaines : data-sci, ml-eng
- [[Maintenance prédictive et RUL]] — domaines : data-sci, mlops
- [[Stationarity]] — domaines : data-sci
- [[Time series anomaly detection]] — domaines : data-sci, mlops
- [[Time series feature engineering]] — domaines : data-sci, ml-eng
- [[Walk-forward CV]] — domaines : data-sci, ml-eng

### Briques
- [[Chronos]] — Modèle de fondation pour séries temporelles (Amazon) — prévision zero-shot sans entraîner un modèle par série : Chronos tokenise les valeurs sur T5, Chronos-2 (2025) passe à un encoder-only multivarié natif (~120 M params).
- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[neuralforecast]] — Prévision par réseaux de neurones (Nixtla) — 30+ architectures récentes (NHITS, NBEATS, TFT, PatchTST) sur PyTorch, GPU, prévision probabiliste et covariables.
- [[pmdarima]] — AutoARIMA pur Python façon auto.arima de R — sélection automatique des ordres (p,d,q)(P,D,Q) par tests de racine unitaire et critère d'information, sur une interface scikit-learn ; wrap de statsmodels.
- [[Prophet]] — Modèle de prévision additif (tendance + saisonnalités + effets calendaires) de Meta — robuste aux données manquantes et aux ruptures de tendance, exploitable sans expertise séries temporelles.
- [[statsforecast]] — Prévision statistique ultra-rapide (Nixtla) — AutoARIMA / AutoETS / Theta compilés par Numba, jusqu'à des millions de séries (Spark, Dask, Ray).
- [[STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

### Comparatifs
- [[Comparatif - Forecasting]]
<!-- AUTO:END -->

## Notes
