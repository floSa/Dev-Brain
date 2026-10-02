---
role: brique
nom: time-series-anomaly-detector
alias: [microsoft/anomaly-detector, anomaly_detector, Microsoft Anomaly Detector open source, MVAD UVAD]
pitch: "Bibliothèque Python open source de Microsoft, issue des algorithmes du service Azure AI Anomaly Detector — détecteurs univariés (résidu spectral, ESD, z-score) et détecteur multivarié à attention sur graphe, exécutés en local ; la voie de sortie que Microsoft recommande après le retrait du service."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Azure AI Anomaly Detector]]"]
complements: []
tags: [timeseries, multivariate, deep-learning, thresholding]
url_docs: 
url_repo: https://github.com/microsoft/anomaly-detector
---

# time-series-anomaly-detector

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python open source de Microsoft, issue des algorithmes du service Azure AI Anomaly Detector — détecteurs univariés (résidu spectral, ESD, z-score) et détecteur multivarié à attention sur graphe, exécutés en local ; la voie de sortie que Microsoft recommande après le retrait du service.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Paquet PyPI `time-series-anomaly-detector` (dépôt `microsoft/anomaly-detector`, module
Python `anomaly_detector`). Microsoft y a publié les algorithmes qui servaient le service
managé [[Azure AI Anomaly Detector]]. Deux familles : un détecteur **univarié**
(`UnivariateAnomalyDetector`, avec des variantes sur série entière ou sur dernier point, un
modèle à résidu spectral, un filtre ESD, un z-score, une détection de période) et un
détecteur **multivarié** (`MultivariateAnomalyDetector`, réseau à attention sur graphe
entraîné sous PyTorch, selon l'arXiv 2009.02040). Tout s'exécute en local : le code ne
contient aucun appel au service Azure, et le dépôt ne mentionne Azure que dans son fichier
`SECURITY.md`. L'interface reprend celle de l'API REST (granularité, période, codes
d'erreur, bornes de longueur de série). À ne pas confondre avec `microsoft/anomalydetector`,
dépôt distinct et plus ancien, qui ne porte que le code SR-CNN (dernier push en 2022).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un projet dépend du service Azure retiré et cherche la voie que Microsoft indique : mêmes algorithmes, en local | Aucune documentation hors README : l'usage se lit dans le code et dans `anomaly-detector-sample-code.ipynb` |
| Détection multivariée sur des signaux de machine (jusqu'à 300 signaux dans le service, d'après sa documentation ; limite de la bibliothèque non vérifiée) avec un modèle à attention sur graphe | Pas un remplacement terme à terme : l'hébergement, la mise à l'échelle et l'authentification de l'API disparaissent, il faut les rebâtir |
| Séries de métriques avec saisonnalité : détection de période, bornes attendues, marges | Dépendances serrées : NumPy <2, pandas ≤2.2.3, SciPy <1.13, Python 3.10 à 3.12 ; PyTorch et MLflow sont tirés d'office |
| Licence MIT, éditeur identifiable, versions récentes (0.4.0 du 2025-11-19) | Dépôt créé en décembre 2023, 34 étoiles, aucun commit depuis 2025-11-19 : l'audience et la cadence de maintenance restent à confirmer avant de s'y engager |
| | Tester plusieurs détecteurs sur des séries labellisées → [[Orion]], [[DeepOD]] ou [[TSB-AD]] |
| | Une solution managée sans code reste voulue : l'offre de Microsoft est désormais dans Fabric (Real-Time Intelligence, en préversion), qui suppose une capacité Fabric |

## Mise en œuvre

- Installation — `uv add time-series-anomaly-detector` (extension Cython compilée ; roues publiées pour Python 3.10 à 3.12, Linux x86_64 et Windows seulement — ailleurs, compilation depuis les sources)
- Point d'entrée — API Python `anomaly_detector.UnivariateAnomalyDetector`, `EntireAnomalyDetector`, `LatestAnomalyDetector`, `MultivariateAnomalyDetector` ; le multivarié s'entraîne par `fit` puis s'interroge par `predict`
- Prérequis — Python ≥3.10 ; PyTorch et MLflow pour le multivarié ; aucun compte ni clé Azure
- Exécution — local, CPU ou GPU selon PyTorch ; le détecteur univarié valide 12 à 8 640 points par appel
- Coût — gratuit, MIT ; aucune infrastructure côté cœur

## Écosystème

### Alternatives

- [[Azure AI Anomaly Detector]] — Service managé Microsoft de détection d'anomalies sur séries temporelles, par API REST univariée (flux, lot, ruptures) et multivariée (réseau à attention sur graphe) — retiré le 1er octobre 2026 ; page conservée pour savoir quoi faire d'un projet qui en dépend.

## Ressources

- Dépôt — README, exemple, tests : https://github.com/microsoft/anomaly-detector
- Dépôt — paquet PyPI : https://pypi.org/project/time-series-anomaly-detector/
- Papier — Réseau à attention sur graphe (Zhao et al., ICDM 2020) : https://arxiv.org/abs/2009.02040
- Papier — SR-CNN, « Time-Series Anomaly Detection Service at Microsoft » (Ren et al., KDD 2019) : https://arxiv.org/abs/1906.03821
- Article — Annonce du retrait du service : https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview

## Voir aussi

- [[Anomalies multivariées par apprentissage profond]] — la notion de son détecteur à attention sur graphe
- [[Time series anomaly detection]] — la notion du dossier qu'il outille
- [[Score et seuil d'alerte]] — comment passer d'un score à une alerte (sévérité, seuil dynamique)
- [[Maintenance prédictive et RUL]] — l'usage cité par Microsoft pour le détecteur multivarié
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des autres bibliothèques
- [[Évaluer une détection d'anomalies]] — les métriques pour juger ses détections
