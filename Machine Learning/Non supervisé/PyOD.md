---
role: brique
nom: PyOD
alias: [Python Outlier Detection, pyod]
pitch: "Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une."
categorie: ml/non-supervise
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[STUMPY]]"]
complements: []
tags: [anomaly-detection, unsupervised]
url_docs: https://pyod.readthedocs.io/
url_repo: https://github.com/yzhao062/pyod
---

# PyOD

<!-- AUTO:BANDEAU:START -->
> Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de référence, depuis 2017, pour la détection d'outliers sur données
**multivariées**. Elle rassemble plus de cinquante détecteurs — classiques (LOF, Isolation
Forest, KNN, OCSVM, ECOD, COPOD) et profonds (autoencodeurs, DeepSVDD) — sous une API
scikit-learn homogène : `fit`, `decision_scores_`, `predict`. Son intérêt central n'est pas un
algorithme mais la **comparaison** : benchmarker plusieurs méthodes sur le même jeu avec un
seul code, plutôt que de miser sur un seul détecteur. Le seuil binaire vient du paramètre
`contamination` ; c'est sur `decision_scores_`, continus, qu'il vaut mieux raisonner.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer rapidement LOF, IsolationForest, ECOD et COPOD sur le même jeu tabulaire | Tous les détecteurs ne passent pas à l'échelle de la même façon : LOF et KNN deviennent coûteux en grande dimension ou en volume |
| Une baseline solide sans paramètre à régler : ECOD et COPOD | Les détecteurs profonds ajoutent hyperparamètres et GPU, sans gain automatique sur les classiques |
| Pipeline reproductible en API scikit-learn : `Pipeline`, `contamination`, scores continus | Un seul détecteur natif — IsolationForest, LOF — en one-shot → [[Scikit-Learn]] suffit, sans dépendance supplémentaire |
| | Seuils univariés simples (Z-score, IQR, MAD) : `numpy` et `scipy.stats` suffisent, cf. [[Détection d'outliers univariée]] |

## Mise en œuvre

- Installation — `uv add pyod`
- Point d'entrée — l'API scikit-learn : `fit`, puis `decision_scores_` et `predict`
- Prérequis — NumPy et SciPy ; features standardisées avant toute méthode à distance ou à densité ; PyTorch pour les détecteurs profonds
- Exécution — single-node, en mémoire, CPU ; le GPU ne sert qu'aux détecteurs profonds
- Coût — BSD-2-Clause, gratuit ; rien à héberger

## Écosystème

### Alternatives

- [[STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

## Ressources

- Documentation — https://pyod.readthedocs.io/
- Dépôt — https://github.com/yzhao062/pyod

## Voir aussi

- [[Détection d'outliers multivariée]] — la notion qu'il outille : LOF, IForest, ECOD, COPOD
- [[Comparatif - Détection d'anomalies]] — ce qui départage les briques du dossier
- [[Apprentissage non supervisé]] — le cadre
