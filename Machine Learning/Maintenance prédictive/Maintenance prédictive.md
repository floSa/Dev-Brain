---
role: hub
nom: Maintenance prédictive
pitch: Estimer l'état de santé d'une machine et décider quand intervenir — surveillance, indicateurs, diagnostic de défauts, durée de vie résiduelle, coût.
domaines: [data-sci, ml-eng, mlops]
tags: [predictive-maintenance]
---

# Maintenance prédictive

> Estimer l'état de santé d'une machine et décider quand intervenir — surveillance, indicateurs, diagnostic de défauts, durée de vie résiduelle, coût.

## Ce qu'il faut comprendre

- **Le dossier a pour sujet une panne et une décision, pas une série temporelle.** La notion d'entrée est [[Maintenance prédictive et RUL]] : les stratégies (correctif, préventif, prédictif), la différence entre diagnostic et pronostic, la durée de vie résiduelle (RUL) et son score asymétrique. Les autres pages la prolongent sans la répéter.
- **Avant le modèle, le cadre industriel.** [[Surveillance conditionnelle et modes de défaillance]] pose la maintenance conditionnelle (CBM), la courbe P-F et l'AMDEC : ce qu'on surveille, et pourquoi la détection arrive avant la panne d'un intervalle qui borne tout le reste.
- **Du signal à l'indicateur.** [[Analyse vibratoire]] (rangée avec le signal, puisqu'elle traite un signal et non une panne) donne les descripteurs d'une machine tournante ; [[Diagnostic de défauts de roulements]] en fait un diagnostic, avec ses fréquences caractéristiques et le biais connu du jeu CWRU ; [[Indicateurs de santé]] résume plusieurs capteurs en une grandeur dont on juge la monotonie et la tendance.
- **Deux façons de prédire la durée de vie.** [[RUL par apprentissage profond]] régresse une durée à partir de fenêtres de capteurs ; [[RUL par analyse de survie]] modélise un temps jusqu'à la panne avec censure, et s'appuie sur [[lifelines]] et [[Analyse de survie]].
- **Le problème industriel réel : presque pas de pannes.** [[Maintenance prédictive avec peu de pannes]] part de là : anomalie non supervisée, transfert entre machines, simulation. La détection de l'anormal elle-même reste dans [[Détection d'anomalies]] (règle D-R11) : la maintenance l'emploie, elle ne la contient pas.
- **Un score n'est pas une décision.** [[Politique de maintenance et coût]] traduit un RUL ou un score en intervention, au coût moyen le plus bas ; [[Jumeau numérique et modèles hybrides]] traite le cas où un modèle physique complète les données.
- **Construire ou acheter.** Les offres d'éditeur du marché sont propriétaires ou payantes : le brain n'en tient aucune fiche (voir « Hors périmètre du brain » plus bas). Les bibliothèques libres du sujet sont [[scikit-survival]] (survie, GPL-3.0), [[tsfresh]] (table de features) et [[sktime]] (interface unifiée), rangées dans leurs propres dossiers.
- **Un cas à part : la batterie.** [[Santé de batterie (SOH et RUL)]] décline l'état de santé et la fin de vie d'une cellule en trois familles (modèle physique, circuit équivalent, apprentissage) ; [[PyBaMM]] est la brique libre du modèle physique, pour un jumeau recalé sur les mesures.
- **Mesurer avant de modéliser.** Les indicateurs d'exploitation qui servent de référence à tout modèle, MTBF, MTTR, disponibilité et OEE, sont dans [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] et [[OEE et rendement global]] (dossier « Données industrielles »).
- **Les jeux de test publics, et ce qu'ils permettent**, sont dans [[Jeux de données PHM]] : plusieurs sont simulés ou à défauts artificiels, et aucun ne remplace des pannes réelles.

## Choisir

- Comprendre le vocabulaire et le cadre → [[Maintenance prédictive et RUL]], puis [[Surveillance conditionnelle et modes de défaillance]].
- Une machine tournante équipée d'accéléromètres → [[Analyse vibratoire]], puis [[Diagnostic de défauts de roulements]].
- Plusieurs capteurs à résumer en un état → [[Indicateurs de santé]].
- Prédire une durée de vie → [[RUL par apprentissage profond]] avec beaucoup de trajectoires complètes ; [[RUL par analyse de survie]] quand la plupart des unités sont encore en service (censure).
- Quasi aucune panne enregistrée → [[Maintenance prédictive avec peu de pannes]], puis [[Détection d'anomalies]].
- Décider quand intervenir → [[Politique de maintenance et coût]].
- Survie avec un modèle d'ensemble ou une évaluation sous censure → [[scikit-survival]] ; avec des tests et des rapports de risque → [[lifelines]].
- Transformer des fenêtres de capteurs en table pour un classifieur ou une régression → [[tsfresh]], ou [[sktime]] pour une interface commune.
- Un service ou une plateforme du marché, ou un historien déjà en place → hors périmètre du brain, voir « Hors périmètre du brain » plus bas.
- Une cellule lithium-ion à suivre ou à simuler → [[Santé de batterie (SOH et RUL)]], puis [[PyBaMM]] pour le modèle physique.
- Chiffrer la fiabilité et le rendement d'un parc d'équipements → [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] et [[OEE et rendement global]].
- Mesurer sur un terrain public → [[Jeux de données PHM]].
- Monter la chaîne sur site, de l'automate à l'alerte → [[Pattern - Pipeline de maintenance prédictive on-prem]], avec [[Pattern - Détection d'anomalies en deux étages]] pour le modèle.

## Hors périmètre du brain (propriétaires ou payants)

Le brain ne tient pas de fiche pour ces offres, citées ici pour mémoire : Seeq, Siemens Insights Hub, AVEVA PI System, Cognite Data Fusion.

**GMAO libres, mais open-core** (vérifié le 2026-10-04) : Atlas CMMS est sous AGPL-3.0 avec une licence commerciale en double et des fonctions « Enterprise » débloquées par une clé ; openMAINT a un cœur sous AGPL, mais son application mobile et son portail libre-service sont propriétaires. Le brain n'en tient pas de fiche (règle « libre seulement »), la GMAO restant la source des ordres de travail et des dates de panne dont se nourrissent les [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]].

**Services fermés** : Amazon Lookout for Equipment (arrêt le 2026-10-07), Amazon Monitron (fermé aux nouveaux clients), Azure AI Anomaly Detector (retiré le 2026-10-01).

<!-- AUTO:START -->
### Notions
- [[Diagnostic de défauts de roulements]] — domaines : data-sci, mlops
- [[Indicateurs de santé]] — domaines : data-sci, mlops
- [[Jumeau numérique et modèles hybrides]] — domaines : data-sci, ml-eng
- [[Maintenance prédictive avec peu de pannes]] — domaines : data-sci, ml-eng, mlops
- [[Maintenance prédictive et RUL]] — domaines : data-sci, mlops
- [[Politique de maintenance et coût]] — domaines : data-sci, mlops
- [[RUL par analyse de survie]] — domaines : data-sci, mlops
- [[RUL par apprentissage profond]] — domaines : data-sci, ml-eng
- [[Santé de batterie (SOH et RUL)]] — domaines : data-sci, ml-eng, mlops
- [[Surveillance conditionnelle et modes de défaillance]] — domaines : data-sci, infra-ops

### Briques
- [[Jeux de données PHM]] — Annuaire commenté de huit jeux de référence pour la maintenance prédictive — turboréacteurs simulés (C-MAPSS), roulements (CWRU, PRONOSTIA/FEMTO, IMS, XJTU-SY, Paderborn), batteries (NASA PCoE) et sons de machines (MIMII) — avec, pour chacun, la licence des données, le mode d'accès et ce qu'elle permet en usage commercial. Rien à installer ; un seul jeu interdit l'usage commercial par une licence écrite, mais la plupart n'en portent aucune.
- [[PyBaMM]] — Bibliothèque Python de simulation de batteries par modèles physiques (SPM, SPMe, DFN, MPM, MSMR…) : un cadre pour écrire et résoudre des équations différentielles, une bibliothèque de modèles et de jeux de paramètres, des outils d'expériences de cyclage ; les modèles de vieillissement (SEI, dépôt de lithium, perte de matière active) y sont des options, pas de l'apprentissage.
<!-- AUTO:END -->

## Notes
