---
role: comparatif
nom: Comparatif - Détection d'anomalies en séries temporelles
categorie: ml/anomalie
tags: [timeseries, benchmark]
---

# Comparatif - Détection d'anomalies en séries temporelles

> On tranche sur : ce que l'outil rend (un score, des ruptures, un banc d'essai), son état de maintenance, et la dépendance à un service tiers.

![[Comparatif - Détection d'anomalies en séries temporelles.base]]

## Ce qui départage

- [[aeon]] — l'API scikit-learn commune à toute la série temporelle (classification, clustering, prévision, anomalies) ; son module d'anomalies reste modeste, sans réseau profond, avec un adaptateur vers PyOD.
- [[DeepOD]] — les détecteurs profonds (tabulaires et séries) sous une API à la PyOD, plus un banc d'essai de recherche ; dépendances épinglées anciennes et dernière version en 2023 : à essayer dans un environnement isolé.
- [[Orion]] — des pipelines complets (AER, TadGAN, LSTM à seuil dynamique) avec benchmark intégré ; statut officiel pre-alpha, Python limité à moins de 3.12.
- [[Kats]] — détection de ruptures et d'outliers (CUSUM, BOCPD) à côté de la prévision, mais dernière version publiée en 2022 et paquet PyPI épinglé sur des versions anciennes.
- [[Merlion]] — prévision, anomalies et ruptures sous une interface commune avec ensembles et post-traitement des scores ; dépôt archivé, à ne pas choisir pour un projet neuf.
- [[ruptures]] — ne rend ni score ni alerte mais des points de rupture, hors ligne ; l'outil à prendre quand la question est « quand le régime a changé ».
- [[STUMPY]] — les discords du matrix profile : anomalies de forme, sans modèle ni étiquettes ; calcul exact quadratique en longueur, fenêtre à caler sur la période.
- [[time-series-anomaly-detector]] — les algorithmes du service Azure (résidu spectral, détecteur multivarié à attention sur graphe), exécutés en local ; roues publiées pour Linux x86_64 et Windows seulement, plus de commit depuis novembre 2025.
- [[TSB-AD]] — pas un détecteur à déployer mais le banc d'essai qui permet de comparer les autres, avec VUS-PR comme métrique de référence ; à utiliser avant de choisir, pas après.

On tranche d'abord sur la sortie attendue (score, rupture, motif), puis sur l'état de maintenance : Merlion archivé, Kats sans version depuis 2022 : deux pages décrivent des outils à ne pas prendre pour un projet neuf.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Détection d'anomalies]] — le dossier qui range ces briques et les notions qui les expliquent.
- [[Time series anomaly detection]] — la notion qui cadre le sujet.
- [[Comparatif - Détection d'anomalies]] — le comparatif voisin, pour les détecteurs tabulaires.
