---
role: brique
nom: aeon
alias: [aeon-toolkit, aeon toolkit, aeon time series]
pitch: "Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Kats]]", "[[Merlion]]", "[[DeepOD]]"]
complements: []
tags: [timeseries, classification, clustering, forecasting]
url_docs: https://www.aeon-toolkit.org/
url_repo: https://github.com/aeon-toolkit/aeon
---

# aeon

<!-- AUTO:BANDEAU:START -->
> Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque généraliste de *time series machine learning*, publiée dans le JMLR en 2024. Son
README la décrit comme compatible scikit-learn et couvrant classification, régression,
clustering, prévision, détection d'anomalies, distances, segmentation, recherche de
similarité, transformations et benchmarking. Beaucoup d'algorithmes y sont contribués ou
maintenus par les chercheurs qui les ont publiés ; le projet est affilié à NumFOCUS.

La détection d'anomalies n'y est qu'un module parmi dix. Au 1.6.0 (2026-09-18), le dépôt
contient :

- **Séries uniques** (`aeon.anomaly_detection.series`) : `STOMP`, `LeftSTAMPi`, `MERLIN`,
  `MADRID` (distances de sous-séquences), `KMeansAD`, `CBLOF`, `LOF`, `ROCKAD`, `COPOD`,
  `DWT_MLEAD`, `IsolationForest`, `ExtendedIsolationForest`, `OneClassSVM`, `STRAY`. Chaque
  détecteur expose `fit` / `predict` et rend un tableau de la longueur de la série : score
  ou booléen par point.
- `PyODAdapter` : enveloppe n'importe quel modèle [[PyOD]] sur des fenêtres glissantes ou
  disjointes ; plusieurs détecteurs ci-dessus (Isolation Forest par exemple) en sont des
  spécialisations et exigent PyOD.
- **Collections de séries** (`aeon.anomaly_detection.collection`) : `ROCKAD`,
  `ClassificationAdapter`, `OutlierDetectionAdapter`, pour juger des séries entières plutôt
  que des points.

La liste a été lue dans les fichiers du dépôt, pas dans la page de documentation. `MADRID` et
`ExtendedIsolationForest` sont annoncés comme nouveaux dans les notes de la 1.6.0. Aucun
détecteur profond n'y figure : les réseaux d'`aeon` servent la classification, la régression, le
clustering et la prévision.

Le module de segmentation expose `ClaSPSegmenter`, `FLUSSSegmenter`, `BinSegmenter`
(qui importe [[ruptures]]), `GreedyGaussianSegmenter`, `HMMSegmenter`,
`InformationGainSegmenter`, `EAggloSegmenter`, `HidalgoSegmenter` et `RandomSegmenter` :
c'est l'entrée pour les ruptures dans la même API.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une seule bibliothèque pour classer, regrouper, prévoir et détecter sur les mêmes séries, avec l'API `fit` / `predict` de scikit-learn | Le seul besoin est la détection d'anomalies : [[PyOD]] (tabulaire), [[STUMPY]] (discords) ou [[DeepOD]] (profond) sont plus fournis sur ce terrain |
| Distances de sous-séquences (`MERLIN`, `MADRID`, `STOMP`, `LeftSTAMPi`) sans quitter l'écosystème | Détecteurs profonds (autoencodeurs, transformeurs) : aucun dans le module d'anomalies → [[DeepOD]], [[TSB-AD]] |
| Segmenter par `ClaSPSegmenter`, `FLUSSSegmenter` ou `BinSegmenter` et comparer avec la détection de points | Flux en continu avec mise à jour incrémentale : l'API est `fit` / `predict` sur une série donnée → [[River]] |
| Prototyper vite avec un détecteur de [[PyOD]] sur fenêtres glissantes via `PyODAdapter` | Besoin de seuil, d'évaluation par événement ou de VUS-PR : rien de tel dans le module → [[Évaluer une détection d'anomalies]] |
| Code de recherche reproductible : implémentations fidèles aux articles, d'après le README | Python 3.10 ou moins : la 1.6.0 demande `>=3.11,<3.15` ; l'API évolue (composants retirés après dépréciation, par exemple `LearningShapeletClassifier` en 1.6.0) |

## Mise en œuvre

- Installation — `uv add aeon` ; extras `aeon[all_extras]` (PyOD, ruptures, STUMPY, tslearn, tsfresh, statsmodels, torch, TensorFlow selon la plateforme) ou `aeon[dl]` pour l'apprentissage profond
- Point d'entrée — API Python : `from aeon.anomaly_detection.series import PyODAdapter` ou, par exemple, `from aeon.anomaly_detection.series.distance_based import STOMP` ; `fit_predict(X, axis=…)`
- Prérequis — Python 3.11 à 3.14 ; NumPy 2, pandas, scikit-learn, SciPy, Numba ; les détecteurs adossés à PyOD demandent `pyod`, `BinSegmenter` demande `ruptures`
- Exécution — CPU mono-machine, en bibliothèque ; latence de compilation Numba au premier appel
- Coût — gratuit, BSD-3-Clause ; aucune infrastructure

## Écosystème

### Alternatives

- [[Kats]] — Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha.
- [[Merlion]] — Bibliothèque Python de Salesforce « time series intelligence » — prévision, détection d'anomalies et de ruptures sous une interface commune, avec ensembles, post-traitement des scores, AutoML et benchmark — dépôt archivé, plus maintenu depuis la 2.0.4 (juin 2024).
- [[DeepOD]] — Bibliothèque Python de détecteurs d'anomalies profonds, tabulaires et séries temporelles (Deep SVDD, REPEN, RDP, GOAD, USAD, TimesNet, Anomaly Transformer, DCdetector…), sous une API fit / decision_function à la PyOD, avec un banc d'essai de recherche ; PyTorch, dépendances épinglées anciennes et dernière release en 2023.

## Ressources

- Documentation — https://www.aeon-toolkit.org/
- Dépôt — https://github.com/aeon-toolkit/aeon
- Article — Middlehurst, Ismail-Fawaz, Guillaume, Holder, Guijo-Rubio, Bulatova, Tsaprounis, Mentel, Walter, Schäfer, Bagnall, *aeon: a Python Toolkit for Learning from Time Series*, JMLR 25, 2024 : http://jmlr.org/papers/v25/23-1444.html

## Voir aussi

- [[Time series anomaly detection]] — la notion du dossier qu'il outille en partie
- [[Détection d'anomalies]] — le hub du dossier
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des autres détecteurs de séries
- [[Séries temporelles]] — le hub du domaine : prévision, classification et clustering relèvent d'`aeon`
- [[Détection de ruptures]] — la notion que son module de segmentation recouvre
- [[Évaluer une détection d'anomalies]] — comment juger ses scores, que le module ne fournit pas
- [[Jeux de données d'anomalies]] — où trouver des séries étiquetées pour les éprouver
- [[Scikit-Learn]] — l'API dont il reprend les conventions
