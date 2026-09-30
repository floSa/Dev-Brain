---
role: brique
nom: Merlion
alias: [salesforce-merlion, salesforce/Merlion, Merlion Salesforce]
pitch: "Bibliothèque Python de Salesforce « time series intelligence » — prévision, détection d'anomalies et de ruptures sous une interface commune, avec ensembles, post-traitement des scores, AutoML et benchmark — dépôt archivé, plus maintenu depuis la 2.0.4 (juin 2024)."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: deprecated
langage: Python
alternatives: ["[[aeon]]", "[[Kats]]"]
complements: []
tags: [timeseries, forecasting, benchmark, change-point, thresholding]
url_docs: https://opensource.salesforce.com/Merlion/index.html
url_repo: https://github.com/salesforce/Merlion
---

# Merlion

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de Salesforce « time series intelligence » — prévision, détection d'anomalies et de ruptures sous une interface commune, avec ensembles, post-traitement des scores, AutoML et benchmark — dépôt archivé, plus maintenu depuis la 2.0.4 (juin 2024).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Merlion est une bibliothèque Python de Salesforce couvrant la prévision, la détection
d'anomalies et la détection de ruptures, univariées et multivariées, derrière une interface
unique. Elle fournit des modèles statistiques, des ensembles d'arbres et des modèles
profonds, des `DefaultDetector` et `DefaultForecaster` comme point de départ, de l'AutoML
pour le réglage, des **règles de post-traitement** qui rendent les scores d'anomalie plus
lisibles et réduisent les fausses alertes, des **ensembles** de modèles, un chargeur de
jeux de données de benchmark (`ts_datasets`), des pipelines d'évaluation qui simulent
le réentraînement en production, un tableau de bord et un backend distribué PySpark.
**Le dépôt est archivé** : le fichier `CONTRIBUTING-ARCHIVED.md` (« no longer actively
maintained », aucune contribution acceptée) a été ajouté le 2026-03-11, dernier commit du
dépôt. La dernière version publiée sur PyPI est la 2.0.4 du 2024-06-20 (la dernière release
GitHub étiquetée est la 2.0.2, du 2023-02-15).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lire une référence de conception : post-traitement des scores d'anomalie, ensembles, évaluation par rejeu en production | **Archivée, aucune correction à attendre** : tout nouveau projet part sur une bibliothèque maintenue |
| Un projet existant en dépend déjà et tourne : l'épingler à la 2.0.4 le temps de migrer | Compatibilité avec les versions récentes de Python, NumPy et pandas non garantie : le paquet borne NumPy <2.0 |
| Retrouver l'architecture et les résultats du rapport technique (arXiv 2109.09265) | Prévision de séries → [[darts]] |
| | Détecteurs d'anomalies sur série, sur un cadre maintenu → [[Kats]], [[aeon]], [[DeepOD]] ou [[PyOD]] |
| | Benchmark sérieux d'algorithmes d'anomalies → [[TSB-AD]] |
| | Détection de ruptures seule → [[ruptures]] |
| | Certains détecteurs exigent un JDK (Java 11) installé : dépendance d'exécution à prévoir |

## Mise en œuvre

- Installation — `uv add salesforce-merlion` (extras `dashboard`, `spark`, `deep-learning` ou `all`) ; épingler `==2.0.4`
- Point d'entrée — API Python : `DefaultDetector` / `DefaultForecaster`, `model.train` puis `get_anomaly_label` ; tableau de bord par `python -m merlion.dashboard`
- Prérequis — Python ≥3.7 déclaré par le paquet ; OpenMP pour LightGBM ; JDK 11 pour certains détecteurs d'anomalies ; chargeurs de jeux `ts_datasets` à installer depuis le dépôt en mode éditable
- Exécution — mono-machine par défaut ; backend PySpark optionnel
- Coût — gratuit, BSD-3-Clause ; aucune infrastructure côté cœur

## Écosystème

### Alternatives

- [[aeon]] — Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.
- [[Kats]] — Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha.

## Ressources

- Documentation — https://opensource.salesforce.com/Merlion/index.html
- Dépôt — archivé : https://github.com/salesforce/Merlion
- Dépôt — paquet PyPI : https://pypi.org/project/salesforce-merlion/
- Papier — Rapport technique (Bhatnagar et al., 2021) : https://arxiv.org/abs/2109.09265

## Voir aussi

- [[Time series anomaly detection]] — la notion du dossier qu'il outille
- [[Score et seuil d'alerte]] — le post-traitement des scores, point fort de Merlion
- [[Détection de ruptures]] — sa détection de points de changement
- [[Séries temporelles]] — le hub des modèles de prévision, l'autre moitié de Merlion
- [[Comparatif - Détection d'anomalies en séries temporelles]] — où il se place, et vers quoi aller
- [[Évaluer une détection d'anomalies]] — ses métriques de détection et de délai
- [[Jeux de données d'anomalies]] — NAB et les autres jeux livrés par `ts_datasets`
