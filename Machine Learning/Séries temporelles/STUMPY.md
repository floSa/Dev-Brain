---
role: brique
nom: STUMPY
alias: [stumpy, matrix profile python]
pitch: "Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyOD]]"]
complements: []
tags: [anomaly-detection, timeseries]
url_docs: https://stumpy.readthedocs.io/
url_repo: https://github.com/stumpy-dev/stumpy
---

# STUMPY

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Calcule le *matrix profile* d'une série : pour chaque sous-séquence de longueur `m`, la
distance à sa plus proche voisine ailleurs dans la série. De ce seul objet découlent les
motifs (répétitions), les discords (anomalies de forme), la segmentation de régimes et les
chaînes temporelles. L'implémentation est vectorisée et compilée par Numba, parallèle
multicœur, distribuable sur Dask et portée sur GPU — c'est ce qui la rend utilisable sur de
longues séries. La distance étant z-normalisée, la comparaison porte sur la forme et jamais
sur le niveau. Une autre implémentation Python existe, `matrixprofile`, nettement moins active.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Anomalies de forme (discords) dans une série, sans modèle ni labels | Prévoir des valeurs futures : STUMPY décrit, il ne prédit pas → [[Prophet]] |
| Découverte de motifs récurrents, segmentation de régimes, chaînes temporelles | Simple seuillage univarié sur un flux → [[Détection d'outliers univariée]] |
| Longues séries : `stumped` (Dask) et `gpu_stump` (GPU) tiennent l'échelle | Fenêtre `m` mal calée : trop courte elle capte le bruit, trop longue elle noie l'anomalie — la caler sur la période physique |
| | Coût quadratique en longueur pour le calcul exact : passer à l'approché (`scrump`) ou au distribué |
| | Régions plates (variance proche de zéro) : la z-normalisation y fabrique des artefacts |

## Mise en œuvre

- Installation — `uv add stumpy`
- Point d'entrée — API Python `stumpy.stump(T, m)`, puis `stumped` (Dask) et `gpu_stump` (CUDA)
- Prérequis — Numba ; un cluster Dask ou un GPU seulement pour les très longues séries
- Exécution — CPU multicœur mono-machine par défaut ; latence de compilation JIT au premier appel, négligeable ensuite
- Coût — gratuit, BSD-3-Clause ; aucune infrastructure côté cœur

## Écosystème

### Alternatives

- [[PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.

## Ressources

- Documentation — https://stumpy.readthedocs.io/
- Dépôt — https://github.com/stumpy-dev/stumpy

## Voir aussi

- [[Time series anomaly detection]] — la notion du dossier qu'il outille (discords, motifs)
- [[ARIMA SARIMA]] — un modèle du « normal » dont on peut analyser les résidus
- [[Exponential smoothing]] — l'autre modèle du « normal » disponible dans le dossier
- [[Comparatif - Détection d'anomalies]] — ce qui le départage des détecteurs tabulaires
