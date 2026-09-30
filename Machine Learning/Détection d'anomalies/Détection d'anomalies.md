---
role: hub
nom: Détection d'anomalies
pitch: Repérer ce qui s'écarte du normal — points, motifs, images — et décider à partir de quel écart on alerte.
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection]
---

# Détection d'anomalies

> Repérer ce qui s'écarte du normal — points, motifs, images — et décider à partir de quel écart on alerte.

## Ce qu'il faut comprendre

- **Le dossier a pour sujet l'écart au normal, pas une technique.** [[Types d'anomalies et régimes de supervision]] pose le cadre : trois types d'écart (ponctuel, contextuel, collectif), trois régimes selon les étiquettes disponibles, et un vocabulaire — outlier, novelty, hors distribution — sur lequel les sources ne s'accordent pas. Ce qui décide de la méthode est ce qu'on sait du « normal », et si ce normal est propre.
- **Sur du tabulaire, trois hypothèses différentes sur le mot « anormal ».** [[Détection d'outliers univariée]] cherche une valeur extrême sur un axe ; [[Détection d'outliers multivariée]] une violation de la structure jointe. Trois détecteurs traduisent trois idées : la densité locale ([[Local Outlier Factor]]), la facilité d'isolement ([[Isolation Forest]]), l'enveloppe apprise du normal ([[One-Class SVM]]). [[PyOD]] les réunit sous une API pour les comparer plutôt que d'en parier un ; [[Comparatif - Détection d'anomalies]] les départage.
- **Sur une série, le contexte compte.** [[Time series anomaly detection]] traite les anomalies contextuelles et collectives ; [[STUMPY]] calcule le matrix profile, donc les motifs et les discords, sans modèle.
- **Un détecteur rend un score, pas une alerte.** [[Score et seuil d'alerte]] décrit le passage à la décision : quantile, valeurs extrêmes, conformal, et l'erreur du taux de base qui fait qu'un faible taux de fausses alertes noie quand même les vraies.
- **L'évaluation est le point où ce domaine se trompe le plus souvent.** [[Évaluer une détection d'anomalies]] : AUROC contre AUPR en classe rare, biais du point-adjust sur les séries, métriques par événement, fuite de labels. Les jeux publics qui servent de terrain d'essai, avec leur licence, sont dans [[Jeux de données d'anomalies]].
- **Quand le modèle est un réseau de neurones**, la question devient celle d'une entrée qu'il n'a jamais vue : [[Détection hors distribution (OOD)]]. La frontière avec [[Data drift]] : l'OOD juge un exemple, la dérive juge une distribution.
- **Ce qui reste hors du dossier, par construction.** Le clustering, les mélanges gaussiens et la réduction de dimension sont du [[Non supervisé]], même s'ils savent signaler du bruit : l'anomalie n'y est qu'un usage possible (règle D-R10). Estimer une durée de vie résiduelle ou décider d'une intervention est de la maintenance prédictive, dont la notion d'entrée est [[Maintenance prédictive et RUL]] (règle D-R11).

## Choisir

- Un point aberrant sur une variable → [[Détection d'outliers univariée]].
- Des tableaux de variables, aucune étiquette → [[PyOD]] pour comparer, [[Isolation Forest]] comme premier essai ; [[Local Outlier Factor]] si la densité varie d'une zone à l'autre ; [[One-Class SVM]] avec un échantillon vérifié de normal.
- Une série temporelle → [[Time series anomaly detection]], puis [[STUMPY]] pour des anomalies de forme.
- Régler le seuil d'une alerte → [[Score et seuil d'alerte]].
- Mesurer honnêtement un détecteur → [[Évaluer une détection d'anomalies]] avant d'annoncer un chiffre.
- Choisir un jeu de test public, et savoir ce que sa licence permet → [[Jeux de données d'anomalies]].
- Savoir si un modèle de classification doit refuser une entrée → [[Détection hors distribution (OOD)]].

<!-- AUTO:START -->
### Notions
- [[Détection d'outliers multivariée]] — domaines : data-sci, ml-eng
- [[Détection d'outliers univariée]] — domaines : data-sci, ml-eng
- [[Isolation Forest]] — domaines : data-sci, ml-eng
- [[Local Outlier Factor]] — domaines : data-sci, ml-eng
- [[One-Class SVM]] — domaines : data-sci, ml-eng
- [[Time series anomaly detection]] — domaines : data-sci, mlops

### Briques
- [[PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.
- [[STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

### Comparatifs
- [[Comparatif - Détection d'anomalies]]
<!-- AUTO:END -->

## Notes
