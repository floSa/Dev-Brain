---
role: comparatif
nom: Comparatif - Détection d'anomalies
categorie: ml/non-supervise
tags: [anomaly-detection, unsupervised]
---

# Comparatif - Détection d'anomalies

> On tranche sur : la nature de l'anomalie — un point aberrant dans un tableau, ou une forme inattendue dans une série.

![[Comparatif - Détection d'anomalies.base]]

## Ce qui départage

- [[PyOD]] — 50+ détecteurs multivariés sous une seule API scikit-learn : son intérêt n'est pas un algorithme mais la **comparaison** de plusieurs sur le même jeu, dont ECOD et COPOD qui n'ont aucun paramètre. Le seuil binaire vient de `contamination`, qui fausse `labels_` s'il est mal posé — raisonner sur `decision_scores_`.
- [[STUMPY]] — le matrix profile : les **discords**, c'est-à-dire les anomalies de **forme** dans une série, sans modèle ni labels. Tout se joue sur la fenêtre `m`, à caler sur la période physique, et la z-normalisation fabrique des artefacts sur les régions plates.
