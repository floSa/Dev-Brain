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
- **Sur une série, quatre questions distinctes.** Un point ou un motif hors norme : [[Time series anomaly detection]], et pour plusieurs capteurs à la fois [[Anomalies multivariées par apprentissage profond]] — où les méthodes simples battent souvent les réseaux sur TSB-AD ([[TSB-AD]]). Un changement durable de régime : [[Détection de ruptures]] ([[ruptures]]). Un procédé suivi contre ses limites : [[Contrôle statistique de procédé (SPC)]]. Un flux qui n'attend pas : [[Détection d'anomalies en ligne]]. Un modèle de fondation de prévision réemployé comme détecteur : [[Foundation models et anomalies de séries]]. Les outils sont réunis dans [[Comparatif - Détection d'anomalies en séries temporelles]] : [[aeon]], [[DeepOD]], [[Orion]], [[Kats]], [[time-series-anomaly-detector]], et deux pages de mémoire — [[Merlion]] (archivé) et [[Azure AI Anomaly Detector]] (retiré le 2026-10-01).
- **Un détecteur rend un score, pas une alerte.** [[Score et seuil d'alerte]] décrit le passage à la décision : quantile, valeurs extrêmes, conformal, et l'erreur du taux de base qui fait qu'un faible taux de fausses alertes noie quand même les vraies.
- **L'évaluation est le point où ce domaine se trompe le plus souvent.** [[Évaluer une détection d'anomalies]] : AUROC contre AUPR en classe rare, biais du point-adjust sur les séries, métriques par événement, fuite de labels. Les jeux publics qui servent de terrain d'essai, avec leur licence, sont dans [[Jeux de données d'anomalies]].
- **Quand le modèle est un réseau de neurones**, la question devient celle d'une entrée qu'il n'a jamais vue : [[Détection hors distribution (OOD)]]. La frontière avec [[Data drift]] : l'OOD juge un exemple, la dérive juge une distribution.
- **Ce qui reste hors du dossier, par construction.** Le clustering, les mélanges gaussiens et la réduction de dimension sont du [[Non supervisé]], même s'ils savent signaler du bruit : l'anomalie n'y est qu'un usage possible (règle D-R10). Estimer une durée de vie résiduelle ou décider d'une intervention est de la maintenance prédictive, dont la notion d'entrée est [[Maintenance prédictive et RUL]] (règle D-R11).

## Choisir

- Un point aberrant sur une variable → [[Détection d'outliers univariée]].
- Des tableaux de variables, aucune étiquette → [[PyOD]] pour comparer, [[Isolation Forest]] comme premier essai ; [[Local Outlier Factor]] si la densité varie d'une zone à l'autre ; [[One-Class SVM]] avec un échantillon vérifié de normal.
- Une série temporelle → [[Time series anomaly detection]], puis [[STUMPY]] pour des anomalies de forme.
- Plusieurs capteurs, des étiquettes rares → [[Anomalies multivariées par apprentissage profond]], après avoir essayé les méthodes statistiques ; une comparaison honnête passe par [[TSB-AD]].
- Dater un changement de régime → [[Détection de ruptures]] avec [[ruptures]].
- Surveiller un procédé contre ses limites naturelles → [[Contrôle statistique de procédé (SPC)]], avant tout apprentissage.
- Un flux continu, des décisions à la volée → [[Détection d'anomalies en ligne]].
- Un modèle de prévision déjà en place → [[Foundation models et anomalies de séries]].
- Régler le seuil d'une alerte → [[Score et seuil d'alerte]].
- Mesurer honnêtement un détecteur → [[Évaluer une détection d'anomalies]] avant d'annoncer un chiffre.
- Choisir un jeu de test public, et savoir ce que sa licence permet → [[Jeux de données d'anomalies]].
- Savoir si un modèle de classification doit refuser une entrée → [[Détection hors distribution (OOD)]].

<!-- AUTO:START -->
### Notions
- [[Anomalies multivariées par apprentissage profond]] — domaines : data-sci, ml-eng
- [[Contrôle statistique de procédé (SPC)]] — domaines : data-sci, ml-eng
- [[Détection d'anomalies en ligne]] — domaines : data-sci, ml-eng, mlops
- [[Détection d'outliers multivariée]] — domaines : data-sci, ml-eng
- [[Détection d'outliers univariée]] — domaines : data-sci, ml-eng
- [[Détection de ruptures]] — domaines : data-sci, ml-eng
- [[Détection hors distribution (OOD)]] — domaines : ml-eng, mlops, data-sci
- [[Foundation models et anomalies de séries]] — domaines : data-sci, ml-eng
- [[Isolation Forest]] — domaines : data-sci, ml-eng
- [[Local Outlier Factor]] — domaines : data-sci, ml-eng
- [[One-Class SVM]] — domaines : data-sci, ml-eng
- [[Score et seuil d'alerte]] — domaines : data-sci, ml-eng, mlops
- [[Time series anomaly detection]] — domaines : data-sci, mlops
- [[Types d'anomalies et régimes de supervision]] — domaines : data-sci, ml-eng
- [[Évaluer une détection d'anomalies]] — domaines : data-sci, ml-eng

### Briques
- [[aeon]] — Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.
- [[Azure AI Anomaly Detector]] — Service managé Microsoft de détection d'anomalies sur séries temporelles, par API REST univariée (flux, lot, ruptures) et multivariée (réseau à attention sur graphe) — retiré le 1er octobre 2026 ; page conservée pour savoir quoi faire d'un projet qui en dépend.
- [[DeepOD]] — Bibliothèque Python de détecteurs d'anomalies profonds, tabulaires et séries temporelles (Deep SVDD, REPEN, RDP, GOAD, USAD, TimesNet, Anomaly Transformer, DCdetector…), sous une API fit / decision_function à la PyOD, avec un banc d'essai de recherche ; PyTorch, dépendances épinglées anciennes et dernière release en 2023.
- [[Jeux de données d'anomalies]] — Annuaire commenté de onze jeux de référence pour la détection d'anomalies — images industrielles (MVTec AD, MVTec AD 2, VisA, Real-IAD), séries temporelles (NAB, SMD, SMAP/MSL, SWaT, TSB-AD) et tabulaire (ADBench, ODDS) — avec, pour chacun, la licence des données et ce qu'elle permet en usage commercial. Rien à installer ; plusieurs jeux sont réservés à la recherche.
- [[Kats]] — Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha.
- [[Merlion]] — Bibliothèque Python de Salesforce « time series intelligence » — prévision, détection d'anomalies et de ruptures sous une interface commune, avec ensembles, post-traitement des scores, AutoML et benchmark — dépôt archivé, plus maintenu depuis la 2.0.4 (juin 2024).
- [[Orion]] — Bibliothèque Python du Data to AI Lab (MIT) de détection d'anomalies non supervisée sur séries temporelles — pipelines « vérifiés » prêts à l'emploi (AER, TadGAN, LSTM à seuil dynamique, autoencodeurs, matrix profile…), benchmark intégré, statut officiel pre-alpha.
- [[PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.
- [[ruptures]] — Bibliothèque Python de détection de ruptures hors ligne — segmente un signal en régimes avec des algorithmes de recherche (PELT, Binseg, BottomUp, Window, Dynp, KernelCPD) combinables à des fonctions de coût (L2, RBF, normale, rang…) ; elle rend des points de changement, pas des scores d'anomalie.
- [[STUMPY]] — Bibliothèque Python de matrix profile pour l'analyse de séries temporelles — calcul efficace (Numba, parallèle, Dask, GPU) des motifs et des discords (anomalies de forme), de la segmentation et des chaînes temporelles.
- [[time-series-anomaly-detector]] — Bibliothèque Python open source de Microsoft, issue des algorithmes du service Azure AI Anomaly Detector — détecteurs univariés (résidu spectral, ESD, z-score) et détecteur multivarié à attention sur graphe, exécutés en local ; la voie de sortie que Microsoft recommande après le retrait du service.
- [[TSB-AD]] — Banc d'essai et bibliothèque Python de détection d'anomalies en séries temporelles (NeurIPS 2024) — 1 070 séries univariées et multivariées tirées de 40 jeux, une quarantaine d'algorithmes statistiques, neuronaux et modèles de fondation sous une même fonction, et VUS-PR comme métrique de référence ; sert à comparer et à évaluer, pas à déployer.

### Comparatifs
- [[Comparatif - Détection d'anomalies]]
- [[Comparatif - Détection d'anomalies en séries temporelles]]
<!-- AUTO:END -->

## Notes
