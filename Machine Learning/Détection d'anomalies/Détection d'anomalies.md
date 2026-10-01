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
- **Sur des images de pièces, l'entraînement se fait sur le bon seul.** [[Détection d'anomalies visuelle]] pose le problème (score d'image et carte au pixel, jeux MVTec AD, MVTec AD 2, VisA, Real-IAD) et la saturation de MVTec AD. Trois familles : [[Anomalie visuelle par banque de mémoire]] (SPADE, PaDiM, PatchCore), [[Anomalie visuelle par reconstruction, distillation et flux]] (DRAEM, RD4AD, EfficientAD, Dinomaly, FastFlow…) et [[Anomalie visuelle zero-shot et few-shot]] (WinCLIP, AnomalyCLIP, AnomalyDINO). [[anomalib]] les outille ; [[Comparatif - Détection d'anomalies visuelles]] départage les outils.
- **Sur du tabulaire, trois hypothèses différentes sur le mot « anormal ».** [[Détection d'outliers univariée]] cherche une valeur extrême sur un axe ; [[Détection d'outliers multivariée]] une violation de la structure jointe. Trois détecteurs traduisent trois idées : la densité locale ([[Local Outlier Factor]]), la facilité d'isolement ([[Isolation Forest]]), l'enveloppe apprise du normal ([[One-Class SVM]]). [[PyOD]] les réunit sous une API pour les comparer plutôt que d'en parier un ; [[Comparatif - Détection d'anomalies]] les départage.
- **Sur une série, le contexte compte.** [[Time series anomaly detection]] traite les anomalies contextuelles et collectives ; [[STUMPY]] calcule le matrix profile, donc les motifs et les discords, sans modèle.
- **Un détecteur rend un score, pas une alerte.** [[Score et seuil d'alerte]] décrit le passage à la décision : quantile, valeurs extrêmes, conformal, et l'erreur du taux de base qui fait qu'un faible taux de fausses alertes noie quand même les vraies.
- **L'évaluation est le point où ce domaine se trompe le plus souvent.** [[Évaluer une détection d'anomalies]] : AUROC contre AUPR en classe rare, biais du point-adjust sur les séries, métriques par événement, fuite de labels. Les jeux publics qui servent de terrain d'essai, avec leur licence, sont dans [[Jeux de données d'anomalies]].
- **Quand le modèle est un réseau de neurones**, la question devient celle d'une entrée qu'il n'a jamais vue : [[Détection hors distribution (OOD)]]. La frontière avec [[Data drift]] : l'OOD juge un exemple, la dérive juge une distribution.
- **Ce qui reste hors du dossier, par construction.** Le clustering, les mélanges gaussiens et la réduction de dimension sont du [[Non supervisé]], même s'ils savent signaler du bruit : l'anomalie n'y est qu'un usage possible (règle D-R10). Estimer une durée de vie résiduelle ou décider d'une intervention est de la maintenance prédictive, dont la notion d'entrée est [[Maintenance prédictive et RUL]] (règle D-R11).

## Choisir

- Un point aberrant sur une variable → [[Détection d'outliers univariée]].
- Des images de pièces à contrôler, avec du bon seul → [[Détection d'anomalies visuelle]], puis [[anomalib]] pour comparer les méthodes sur ses images ; [[patchcore-inspection]] comme baseline.
- Des tableaux de variables, aucune étiquette → [[PyOD]] pour comparer, [[Isolation Forest]] comme premier essai ; [[Local Outlier Factor]] si la densité varie d'une zone à l'autre ; [[One-Class SVM]] avec un échantillon vérifié de normal.
- Une série temporelle → [[Time series anomaly detection]], puis [[STUMPY]] pour des anomalies de forme.
- Régler le seuil d'une alerte → [[Score et seuil d'alerte]].
- Mesurer honnêtement un détecteur → [[Évaluer une détection d'anomalies]] avant d'annoncer un chiffre.
- Choisir un jeu de test public, et savoir ce que sa licence permet → [[Jeux de données d'anomalies]].
- Savoir si un modèle de classification doit refuser une entrée → [[Détection hors distribution (OOD)]].

<!-- AUTO:START -->
### Notions
- [[Anomalie visuelle par banque de mémoire]] — domaines : data-sci, ml-eng
- [[Anomalie visuelle par reconstruction, distillation et flux]] — domaines : data-sci, ml-eng
- [[Anomalie visuelle zero-shot et few-shot]] — domaines : data-sci, ml-eng
- [[Détection d'anomalies visuelle]] — domaines : data-sci, ml-eng
- [[Détection d'outliers multivariée]] — domaines : data-sci, ml-eng
- [[Détection d'outliers univariée]] — domaines : data-sci, ml-eng
- [[Détection hors distribution (OOD)]] — domaines : ml-eng, mlops, data-sci
- [[Isolation Forest]] — domaines : data-sci, ml-eng
- [[Local Outlier Factor]] — domaines : data-sci, ml-eng
- [[One-Class SVM]] — domaines : data-sci, ml-eng
- [[Score et seuil d'alerte]] — domaines : data-sci, ml-eng, mlops
- [[Time series anomaly detection]] — domaines : data-sci, mlops
- [[Types d'anomalies et régimes de supervision]] — domaines : data-sci, ml-eng
- [[Évaluer une détection d'anomalies]] — domaines : data-sci, ml-eng

### Briques
- [[anomalib]] — Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0.
- [[AnomalyCLIP]] — Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT.
- [[Dinomaly]] — Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0.
- [[Jeux de données d'anomalies]] — Annuaire commenté de onze jeux de référence pour la détection d'anomalies — images industrielles (MVTec AD, MVTec AD 2, VisA, Real-IAD), séries temporelles (NAB, SMD, SMAP/MSL, SWaT, TSB-AD) et tabulaire (ADBench, ODDS) — avec, pour chacun, la licence des données et ce qu'elle permet en usage commercial. Rien à installer ; plusieurs jeux sont réservés à la recherche.
- [[patchcore-inspection]] — Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023.
- [[PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.
- [[STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.

### Comparatifs
- [[Comparatif - Détection d'anomalies]]
- [[Comparatif - Détection d'anomalies visuelles]]
<!-- AUTO:END -->

## Notes
