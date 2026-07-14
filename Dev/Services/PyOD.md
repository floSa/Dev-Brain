---
galaxie: dev
type: service
nom: PyOD
alias: [Python Outlier Detection, pyod]
pitch: "Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/STUMPY|STUMPY]]"]
remplace_par: []
status: actif
tags: [anomaly-detection, unsupervised]
url_docs: https://pyod.readthedocs.io/
url_repo: https://github.com/yzhao062/pyod
---

# PyOD

## Pourquoi

Bibliothèque de référence (depuis 2017) pour la **détection d'outliers** sur données multivariées. Rassemble **50+ détecteurs** — classiques (LOF, Isolation Forest, KNN, OCSVM, [[Détection d'outliers multivariée|ECOD/COPOD]]) et profonds (autoencodeurs, DeepSVDD) — sous une **API scikit-learn** homogène (`fit`, `decision_scores_`, `predict`). Son intérêt central : **benchmarker** plusieurs méthodes sur le même jeu avec un seul code, plutôt que de miser sur un seul détecteur.

## Quand l'utiliser

- [[Détection d'outliers multivariée]] sur tabulaire : comparer rapidement LOF, IsolationForest, ECOD, COPOD…
- Besoin de détecteurs **sans paramètre** robustes (ECOD, COPOD) comme baseline solide.
- Pipeline reproductible avec API scikit-learn (`Pipeline`, `contamination`, scores continus).

## Quand NE PAS l'utiliser

- Seuils **univariés** simples (Z-score, IQR, MAD) → `numpy`/`scipy.stats` suffisent, cf. [[Détection d'outliers univariée]].
- Anomalies de **forme dans une série temporelle** → [[Dev/Services/STUMPY|STUMPY]] (matrix profile).
- Un seul détecteur natif (IsolationForest, LOF) en one-shot → [[Dev/Services/Scikit-Learn|scikit-learn]] suffit, sans dépendance supplémentaire.

## Déploiement & coût

- Bibliothèque open-source (**BSD-2-Clause**), gratuite ; `uv add pyod`.
- **Single-node, en mémoire**, API scikit-learn ; les détecteurs profonds (v2) nécessitent **PyTorch** et bénéficient d'un GPU.
- Aucune infra ; cœur classique en NumPy/SciPy, CPU.

## Pièges

- **Contamination** : paramètre clé qui fixe le seuil binaire ; mal réglé, il fausse `labels_`. Préférer raisonner sur `decision_scores_`.
- Tous les détecteurs ne **passent pas à l'échelle** de la même façon (LOF/KNN coûteux en grande dimension/volume).
- Modèles profonds = **hyperparamètres et GPU** ; pas un gain automatique sur les classiques.
- **Standardiser** les features avant les méthodes à distance/densité.

## Alternatives

Pas de substitut unifié équivalent dans le brain. À la marge : [[Dev/Services/Scikit-Learn|scikit-learn]] pour un détecteur natif isolé, et [[Dev/Services/STUMPY|STUMPY]] pour le cas séries temporelles.

- [[Dev/Services/STUMPY|STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

## Liens

- [[Détection d'outliers multivariée]] — le cadre qu'il outille (LOF, IForest, ECOD, COPOD).
- [[Détection d'outliers univariée]] — pour les cas mono-variable, plus légers.
- [[Dev/Services/STUMPY|STUMPY]] — l'équivalent côté séries temporelles.
- [[Dev/Patterns/Comparatif - Détection d'anomalies|Comparatif — Détection d'anomalies]]
- Doc : https://pyod.readthedocs.io/
