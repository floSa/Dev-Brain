---
role: brique
nom: Kats
alias: [facebookresearch/Kats, Kats Meta, kit to analyze time series]
pitch: "Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[ruptures]]", "[[aeon]]", "[[Merlion]]"]
complements: []
tags: [timeseries, forecasting, change-point, multivariate]
url_docs: https://facebookresearch.github.io/Kats/
url_repo: https://github.com/facebookresearch/Kats
---

# Kats

<!-- AUTO:BANDEAU:START -->
> Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Kats (« kit to analyze time series ») est publié par l'équipe Infrastructure Data Science de
Facebook, devenue Meta. Il vise un guichet unique pour la série temporelle : statistiques
descriptives, **détection** (points de rupture, régressions, anomalies), **prévision**,
extraction de features et plongements, analyse multivariée. Côté détection, le dépôt
contient notamment CUSUM, BOCPD (rupture bayésienne en ligne), un détecteur de statistiques
robustes, un détecteur d'outliers, un détecteur de signification statistique, un détecteur
fondé sur Prophet et un détecteur multivarié. Tout passe par un objet `TimeSeriesData`.
Le dépôt n'est pas archivé et reçoit des commits (le plus récent date du 2026-10-01), mais ce
sont pour l'essentiel des synchronisations de maintenance venues du dépôt interne de Meta
(annotations de types, tests instables, montée de version de Python). Les **releases**, elles,
s'arrêtent à la 0.2.0, publiée le 2022-03-15.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Détection de **ruptures et de régressions** sur des métriques (CUSUM, BOCPD), avec prévision et features dans la même API | Le paquet PyPI 0.2.0 épingle des versions anciennes (NumPy <1.22, pandas ≤1.3.5, statsmodels 0.12.2, `fbprophet` 0.7.1, `pystan` 2.19) : il ne s'installe pas dans un environnement récent sans effort |
| Un détecteur à base de Prophet ou de statistiques robustes suffit, sur des séries de métriques de service | Aucune release depuis 2022 et classifier PyPI « Alpha » : pas de promesse de stabilité de l'API |
| Lire ou réutiliser le code de détecteurs de ruptures bien documentés (CUSUM, BOCPD) | Détection de ruptures seule, sur signal échantillonné → [[ruptures]], bibliothèque dédiée à cette seule tâche |
| | Anomalies de séries profondes ou multivariées, avec benchmark → [[DeepOD]], [[Orion]] ou [[TSB-AD]] |
| | Un projet qui doit rester maintenable plusieurs années : le statut réel est celui d'un dépôt de recherche appliquée, pas d'un produit |

## Mise en œuvre

- Installation — `uv add kats` ; version minimale avec `MINIMAL_KATS=1` (omet les dépendances de test et désactive des fonctions). Prévoir un environnement dédié, ou une installation depuis le dépôt
- Point d'entrée — API Python : `TimeSeriesData`, puis un détecteur (`CUSUMDetector`, `BOCPDetector`, `RobustStatDetector`, `OutlierDetector`…) ou un modèle de prévision
- Prérequis — Python 3.8, 3.9 ou 3.12 déclarés par `setup.py` ; pile scientifique aux versions épinglées
- Exécution — mono-machine, CPU
- Coût — gratuit, MIT ; aucune infrastructure côté cœur

## Écosystème

### Alternatives

- [[ruptures]] — Bibliothèque Python de détection de ruptures hors ligne — segmente un signal en régimes avec des algorithmes de recherche (PELT, Binseg, BottomUp, Window, Dynp, KernelCPD) combinables à des fonctions de coût (L2, RBF, normale, rang…) ; elle rend des points de changement, pas des scores d'anomalie.
- [[aeon]] — Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.
- [[Merlion]] — Bibliothèque Python de Salesforce « time series intelligence » — prévision, détection d'anomalies et de ruptures sous une interface commune, avec ensembles, post-traitement des scores, AutoML et benchmark — dépôt archivé, plus maintenu depuis la 2.0.4 (juin 2024).

## Ressources

- Documentation — https://facebookresearch.github.io/Kats/
- Dépôt — https://github.com/facebookresearch/Kats
- Dépôt — paquet PyPI : https://pypi.org/project/kats/
- Article — Billet de présentation (Facebook Engineering, 2021) : https://engineering.fb.com/2021/06/21/open-source/kats/

## Voir aussi

- [[Détection de ruptures]] — la notion de ses détecteurs CUSUM et BOCPD
- [[Time series anomaly detection]] — la notion du dossier : anomalies ponctuelles, contextuelles, collectives
- [[Détection d'anomalies en ligne]] — l'usage en flux de BOCPD
- [[Prophet]] — le modèle de prévision que son détecteur Prophet réutilise
- [[Séries temporelles]] — le hub des modèles de prévision, côté prévision de Kats
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des autres bibliothèques
- [[Évaluer une détection d'anomalies]] — comment juger ses détections
