---
role: brique
nom: Azure AI Anomaly Detector
alias: [Azure Anomaly Detector, Anomaly Detector Azure, Azure Cognitive Services Anomaly Detector, AI Services Anomaly Detector]
pitch: "Service managé Microsoft de détection d'anomalies sur séries temporelles, par API REST univariée (flux, lot, ruptures) et multivariée (réseau à attention sur graphe) — retiré le 1er octobre 2026 ; page conservée pour savoir quoi faire d'un projet qui en dépend."
categorie: ml/anomalie
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: deprecated
langage: 
alternatives: ["[[time-series-anomaly-detector]]"]
complements: []
tags: [timeseries, multivariate, change-point, streaming]
url_docs: https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview
url_repo: 
---

# Azure AI Anomaly Detector

<!-- AUTO:BANDEAU:START -->
> Service managé Microsoft de détection d'anomalies sur séries temporelles, par API REST univariée (flux, lot, ruptures) et multivariée (réseau à attention sur graphe) — retiré le 1er octobre 2026 ; page conservée pour savoir quoi faire d'un projet qui en dépend.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Service d'Azure AI services, exposé en API REST et en SDK, qui détectait des anomalies dans
des séries temporelles sans exiger de connaissance en machine learning. Deux volets. Le
volet **univarié** : détection en flux (le dernier point est-il anormal ?), détection en lot
sur une série entière, détection de points de rupture de tendance ; le modèle était choisi
automatiquement selon la forme des données (algorithme SR-CNN, KDD 2019). Le volet
**multivarié** : un modèle entraîné sur les données du client, fondé sur un réseau à attention
sur graphe, qui tient compte des corrélations entre plusieurs signaux (jusqu'à 300 d'après la
documentation), avec la maintenance prédictive et l'AIOps comme cas d'usage cités.
**Retrait le 2026-10-01** : depuis le 2023-09-20 plus aucune nouvelle ressource ne pouvait
être créée, et le service est retiré à la date annoncée par Microsoft. Cette page existe pour
un seul cas : un projet, un notebook ou un pipeline tiers qui appelle encore ce service et
doit être migré.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lire du code existant qui l'appelle, pour savoir quoi remplacer (granularité, période, valeurs attendues et marges) | **Retiré le 2026-10-01** : aucun nouveau projet ne doit en dépendre |
| Retrouver le vocabulaire de l'API pour migrer vers un équivalent local | Microsoft recommande [[time-series-anomaly-detector]] — les mêmes algorithmes, en bibliothèque Python — ou Microsoft Fabric (Real-Time Intelligence, en préversion), qui l'intègre |
| | Détection d'anomalies **univariée** sur des tables Kusto → fonctions intégrées d'Azure Data Explorer (`series_decompose_anomalies`) ; Microsoft reconnaît qu'elles ne couvrent pas le multivarié |
| | Plusieurs candidats à comparer, avec benchmark → [[Orion]], [[DeepOD]] ou [[TSB-AD]] ; détection de ruptures seule → [[ruptures]] |
| | Détection sur site, sans compte cloud (cas on-prem) : le service ne s'y prêtait pas, il fallait un compte Azure |
| | Un pipeline [[Orion]] nommé `azure` appelle ce service par clé et point d'accès : il ne peut plus fonctionner après le retrait |

## Mise en œuvre

- Installation — rien à installer ; il n'est plus possible de créer la ressource Azure
- Point d'entrée — API REST et SDK clients (univarié : flux, lot, ruptures ; multivarié : entraînement puis inférence)
- Prérequis — une ressource Azure existante avant le 2023-09-20 ; plus utilisable après le 2026-10-01
- Exécution — managé, hébergé par Microsoft ; aucune exécution locale
- Coût — sans objet après le retrait ; tarif historique non relevé

## Écosystème

### Alternatives

- [[time-series-anomaly-detector]] — Bibliothèque Python open source de Microsoft, issue des algorithmes du service Azure AI Anomaly Detector — détecteurs univariés (résidu spectral, ESD, z-score) et détecteur multivarié à attention sur graphe, exécutés en local ; la voie de sortie que Microsoft recommande après le retrait du service.

## Ressources

- Documentation — Documentation et avis de retrait : https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview
- Documentation — Guide Fabric (Real-Time Intelligence, préversion) : https://learn.microsoft.com/en-us/fabric/real-time-intelligence/anomaly-detection
- Article — Fil de questions-réponses Microsoft sur le retrait et les alternatives : https://learn.microsoft.com/en-us/answers/questions/1434709/azure-anomaly-detection-is-being-retired-what-are
- Papier — SR-CNN, « Time-Series Anomaly Detection Service at Microsoft » (Ren et al., KDD 2019) : https://arxiv.org/abs/1906.03821
- Papier — Réseau à attention sur graphe multivarié (Zhao et al., ICDM 2020) : https://arxiv.org/abs/2009.02040

## Voir aussi

- [[Time series anomaly detection]] — la notion du dossier : univarié, multivarié, flux et lot
- [[Anomalies multivariées par apprentissage profond]] — la famille de son volet multivarié
- [[Détection d'anomalies en ligne]] — son mode « flux », point par point
- [[Maintenance prédictive et RUL]] — l'usage cité par Microsoft pour le multivarié
- [[Comparatif - Détection d'anomalies en séries temporelles]] — vers quoi migrer
