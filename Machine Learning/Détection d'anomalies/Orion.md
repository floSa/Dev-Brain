---
role: brique
nom: Orion
alias: [orion-ml, sintel-dev/Orion, Orion DAI-Lab, Sintel Orion]
pitch: "Bibliothèque Python du Data to AI Lab (MIT) de détection d'anomalies non supervisée sur séries temporelles — pipelines « vérifiés » prêts à l'emploi (AER, TadGAN, LSTM à seuil dynamique, autoencodeurs, matrix profile…), benchmark intégré, statut officiel pre-alpha."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[DeepOD]]"]
complements: []
tags: [timeseries, unsupervised, deep-learning, gan, benchmark]
url_docs: https://sintel.dev/Orion/
url_repo: https://github.com/sintel-dev/Orion
---

# Orion

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python du Data to AI Lab (MIT) de détection d'anomalies non supervisée sur séries temporelles — pipelines « vérifiés » prêts à l'emploi (AER, TadGAN, LSTM à seuil dynamique, autoencodeurs, matrix profile…), benchmark intégré, statut officiel pre-alpha.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Orion est la bibliothèque de détection d'anomalies du projet Sintel, développé au Data to AI
Lab du MIT (paquet PyPI `orion-ml`, dépôt `sintel-dev/Orion`). Elle ne propose pas un
algorithme mais un catalogue de **pipelines** : chacun enchaîne prétraitement, modèle,
calcul de l'erreur puis recherche des intervalles anormaux, et se lance par un nom
(`Orion(pipeline='aer')`, `fit`, `detect`). La sortie est un tableau d'intervalles
`start`, `end`, `severity`. Le dossier `verified` regroupe AER, ARIMA, TadGAN, LSTM à
seuillage dynamique, autoencodeurs (dense, LSTM, VAE), matrix profile ; `sandbox` en garde
d'autres (Anomaly Transformer, LNN) ; `pretrained` appelle des modèles de fondation
(Chronos 2, TimesFM). Le nom prête à confusion : d'autres projets s'appellent Orion, et
seul `orion-ml` est celui-ci.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Détection **non supervisée** sur des signaux de télémétrie (type NASA SMAP/MSL), sans labels d'entraînement | Un seul modèle simple suffit : un détecteur statistique ou [[STUMPY]] s'installent sans pile deep learning |
| Comparer plusieurs pipelines sur ses propres signaux : le module de benchmark et le classement (victoires contre ARIMA, sur 12 jeux) sont fournis | Le statut officiel est **pre-alpha** (badge du README, classifier PyPI) : l'API et les pipelines peuvent bouger |
| Reproduire des méthodes publiées (TadGAN, AER) avec leur code d'origine | Dernière version publiée : 0.7.1 (2025-03-17) ; Python <3.12 exigé par le paquet — vérifier avant de l'inscrire dans une image récente |
| Sortie en intervalles avec sévérité, directement exploitable par une revue d'expert | Dépendances lourdes et épinglées (TensorFlow <2.15, PyTorch <2.6, NumPy <2) : à isoler dans son propre environnement |
| | Un pipeline `azure` existe mais appelle le service Azure AI Anomaly Detector, retiré le 2026-10-01 → [[Azure AI Anomaly Detector]] |
| | Des séries multivariées de grande taille ou un besoin de suite de référence → [[TSB-AD]] ou [[DeepOD]] |

## Mise en œuvre

- Installation — `uv add orion-ml` (extra `pretrained` pour les pipelines à modèle de fondation)
- Point d'entrée — API Python `Orion(pipeline=…)` avec `fit` puis `detect` ; module `orion.benchmark` pour comparer des pipelines
- Prérequis — Python 3.8 à 3.11 ; TensorFlow et PyTorch tirés comme dépendances
- Exécution — mono-machine ; entraînement par signal, durée dépendant du pipeline
- Coût — gratuit, MIT ; aucune infrastructure côté cœur

## Écosystème

### Alternatives

- [[DeepOD]] — Bibliothèque Python de détecteurs d'anomalies profonds, tabulaires et séries temporelles (Deep SVDD, REPEN, RDP, GOAD, USAD, TimesNet, Anomaly Transformer, DCdetector…), sous une API fit / decision_function à la PyOD, avec un banc d'essai de recherche ; PyTorch, dépendances épinglées anciennes et dernière release en 2023.

## Ressources

- Documentation — https://sintel.dev/Orion/
- Dépôt — https://github.com/sintel-dev/Orion
- Dépôt — paquet PyPI : https://pypi.org/project/orion-ml/
- Papier — TadGAN (Geiger et al., IEEE BigData 2020) : https://arxiv.org/abs/2009.07769
- Papier — AER (Wong et al., IEEE BigData 2022) : https://arxiv.org/abs/2212.13558
- Papier — Sintel (Alnegheimish et al., SIGMOD 2022) : https://dl.acm.org/doi/10.1145/3514221.3517910

## Voir aussi

- [[Time series anomaly detection]] — la notion du dossier qu'il outille
- [[Anomalies multivariées par apprentissage profond]] — la famille de modèles de ses pipelines profonds
- [[Autoencodeurs]] — le principe de reconstruction derrière AER, TadGAN et les autoencodeurs
- [[Score et seuil d'alerte]] — du score d'erreur à l'intervalle signalé
- [[Foundation models et anomalies de séries]] — ses pipelines `pretrained`
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des autres bibliothèques de séries
- [[Évaluer une détection d'anomalies]] — métriques par intervalle pour juger ses sorties
- [[Jeux de données d'anomalies]] — les jeux (SMAP/MSL, NAB, Yahoo) de son benchmark et leurs défauts connus
