---
galaxie: dev
type: service
nom: STUMPY
alias: [stumpy, matrix profile python]
pitch: "Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/PyOD|PyOD]]"]
remplace_par: []
status: actif
tags: [anomaly-detection, timeseries]
url_docs: https://stumpy.readthedocs.io/
url_repo: https://github.com/stumpy-dev/stumpy
---

# STUMPY

## Pourquoi

Calcule efficacement le **matrix profile** d'une série temporelle : pour chaque sous-séquence, la distance à sa plus proche voisine. De ce seul objet découlent **motifs** (répétitions), **discords** (anomalies de forme), segmentation et chaînes temporelles. Implémentation **vectorisée et compilée** (Numba JIT), **parallèle** multicœur, **distribuée** (Dask) et **GPU** (CUDA) — d'où son passage à l'échelle. C'est l'outil de référence pour la [[Time series anomaly detection|détection d'anomalies temporelles]] par matrix profile.

## Quand l'utiliser

- Détecter des **anomalies de forme** (discords) dans une série, sans modèle ni labels.
- **Découverte de motifs** récurrents, segmentation de régimes, time series chains.
- Volumes importants : `stumped` (Dask) et `gpu_stump` (GPU) pour les longues séries.

## Quand NE PAS l'utiliser

- Outliers **tabulaires multivariés** (pas de structure de forme) → [[Dev/Services/PyOD|PyOD]].
- Simple seuillage **univarié** sur un flux → [[Détection d'outliers univariée]] (`numpy`/`scipy`).
- **Prévision** de valeurs futures → [[Dev/Services/Prophet|Prophet]], [[ARIMA SARIMA]] ; STUMPY décrit, ne prédit pas.

## Déploiement & coût

- Bibliothèque open-source (**BSD-3-Clause**), gratuite ; `uv add stumpy`.
- **Single-node par défaut**, mais conçue pour l'échelle : Numba (parallèle), **Dask** (distribué, `stumped`), **GPU** (`gpu_stump`).
- Aucune infra côté cœur ; un cluster Dask ou un GPU seulement pour les très longues séries.

## Pièges

- **Fenêtre $m$** : hyperparamètre déterminant ; trop courte = bruit, trop longue = anomalie noyée. La caler sur la période physique.
- **Latence de compilation Numba** au premier appel (JIT) ; négligeable ensuite.
- **Mémoire / coût** quadratique en longueur pour le calcul exact ; passer à l'approché (`scrump`) ou au distribué sur très longues séries.
- La distance étant **z-normalisée**, les régions **plates** (variance ~0) produisent des artefacts.

## Alternatives

- [[Dev/Services/PyOD|PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.

Côté matrix profile spécifiquement, `matrixprofile` (matrix-profile-foundation) est l'autre implémentation Python, moins active.

## Liens

- [[Time series anomaly detection|Détection d'anomalies temporelles]] — le cadre qu'il outille (discords, motifs).
- [[Dev/Services/PyOD|PyOD]] — l'équivalent côté outliers tabulaires multivariés.
- [[ARIMA SARIMA]] · [[Exponential smoothing]] — modèles du « normal » dont on peut analyser les résidus.
- [[Dev/Patterns/Comparatif - Détection d'anomalies|Comparatif — Détection d'anomalies]]
- Doc : https://stumpy.readthedocs.io/
