---
role: pattern
contexte: Détecter des anomalies sur un procédé ou une machine en faisant passer les mesures par un premier étage de règles et de cartes de contrôle, explicable et peu coûteux, avant de confier à un modèle appris ce que ce premier étage ne voit pas.
services_cles: [PyOD, STUMPY, River, ruptures, aeon]
projets_appliques: []
tags: [pattern, anomaly-detection, statistical-process-control, thresholding, predictive-maintenance]
---

# Pattern — Détection d'anomalies en deux étages

## Contexte

Un capteur ou un procédé produit un flux, et l'envie est de poser tout de suite un modèle appris. Deux choses jouent contre : un modèle appris s'explique mal à l'opérateur qui reçoit l'alerte, et il apprend aussi les capteurs gelés, les valeurs hors plage et les arrêts de machine si personne ne les écarte.

Le montage sépare le travail en deux étages :

```
mesures → étage 1 : règles et SPC → (valide, décidé) → étage 2 : modèle appris → alerte
```

- **Étage 1** : bornes physiques, état de la machine, cartes de contrôle. Déterministe, relisible, sans entraînement.
- **Étage 2** : un score appris, sur ce que l'étage 1 laisse passer et qu'il ne sait pas décrire (motifs, interactions entre capteurs).

À appliquer sur tout flux de maintenance ou de procédé, avant d'avoir la preuve qu'un modèle appris apporte quelque chose. Le cadre : [[Contrôle statistique de procédé (SPC)]], [[Score et seuil d'alerte]] et [[Types d'anomalies et régimes de supervision]].

## Stack

| Étage | Outil | Rôle |
|---|---|---|
| 1 | règles écrites à la main | bornes de plausibilité, capteur gelé, état marche/arrêt, hors plage |
| 1 | cartes de contrôle (Shewhart, EWMA, CUSUM, I-MR) | écart d'un procédé à son régime stable ; limites et règles dans [[Contrôle statistique de procédé (SPC)]] |
| 1 | [[ruptures]] | repérer un changement de régime avant de poser les limites ([[Détection de ruptures]]) |
| 2 | [[PyOD]] | détecteurs tabulaires sur des vecteurs de caractéristiques ([[Isolation Forest]], [[Local Outlier Factor]]) |
| 2 | [[STUMPY]] | anomalies de forme par profil matriciel |
| 2 | [[River]] | détection en flux, mémoire bornée ([[Détection d'anomalies en ligne]]) |
| 2 | [[aeon]] | détecteurs de séries temporelles sous une interface commune |
| 2 | réseaux profonds | seulement si le plancher échoue : [[Anomalies multivariées par apprentissage profond]] |

Les deux comparatifs utiles : [[Comparatif - Détection d'anomalies]] (tabulaire) et [[Comparatif - Détection d'anomalies en séries temporelles]].

## Décisions clés

### 1. L'étage 1 écarte avant de détecter

- Une valeur hors plage physique, un capteur qui répète la même mesure, un arrêt de machine : ce ne sont pas des anomalies à scorer, ce sont des données invalides ou un autre régime. Les envoyer à l'étage 2 le contamine ([[Rule - Entraîner sur du normal vérifié]]).
- Conditionner par régime : un démarrage n'est pas un régime stable. Une anomalie contextuelle est un choix de modélisation, pas une donnée ([[Types d'anomalies et régimes de supervision]]).

### 2. Choisir la carte selon le décalage visé

- Grands sauts : Shewhart. Petites dérives de moyenne : CUSUM ou EWMA. Changement de variance : une carte de dispersion.
- **Un capteur rapide n'est pas indépendant** : les cartes supposent des observations indépendantes, et l'autocorrélation multiplie les fausses alertes (la fiche mesure un facteur 4 à φ = 0,3 pour I-MR). Tracer les **résidus** d'un modèle de prévision, ou vérifier l'autocorrélation d'abord.
- Chiffrer le budget d'alertes avant de poser les limites : $\mathrm{ARL}_0$ visé × période d'échantillonnage = temps moyen entre fausses alertes.

### 3. Mesurer ce que l'étage 1 manque avant de monter à l'étage 2

- Rejouer l'étage 1 sur l'historique avec les défauts connus : quels défauts passent, avec quel délai ? Ce relevé justifie l'étage 2, ou le rend inutile.
- Un plancher simple fait souvent aussi bien : sur le banc TSB-AD, des méthodes statistiques et des réseaux simples égalent ou battent des architectures complexes (CNN et LSTM à égalité avec l'ACP à deux décimales ; les transformeurs derrière). Les sources divergent sur la portée de ce constat : lire [[Anomalies multivariées par apprentissage profond]] avant d'en tirer une règle.
- Monter par paliers : détecteur tabulaire sur caractéristiques, puis modèle de séries, puis réseau profond. Ne pas garder un modèle qu'un plus simple égale.

### 4. L'étage 2 s'entraîne sur ce que l'étage 1 a validé

- Données d'entraînement : uniquement des fenêtres déclarées normales par l'étage 1 **et** vérifiées par quelqu'un qui connaît la machine ([[Rule - Entraîner sur du normal vérifié]]).
- Les deux étages ne partagent pas leurs seuils : le seuil de l'étage 2 se règle sur du normal qui n'a pas servi à l'entraîner ni à l'évaluation ([[Score et seuil d'alerte]]).

### 5. Deux niveaux de décision, deux niveaux de gravité

- Étage 1 déclenché : alerte explicite et immédiate (« valeur hors plage », « carte hors contrôle »). L'opérateur sait quoi regarder.
- Étage 2 seul : alerte de second rang, avec le score et la fenêtre en cause. Regrouper les alertes consécutives en un événement.
- Journaliser les deux scores, pas seulement la décision : on peut alors retoucher les seuils sans rejouer la machine ([[Détection d'anomalies en ligne]]).

### 6. Évaluer par événement

- Compter des événements détectés, un délai de détection et des fausses alertes par jour, pas des points ([[Rule - Évaluer une anomalie par événement, pas par point]], [[Évaluer une détection d'anomalies]]).
- Comparer l'étage 2 **à l'étage 1 seul**, pas à rien : sinon le gain mesuré est celui des règles.

## Pièges

- **Cumuler les règles de séquence par réflexe** : chaque règle ajoutée abaisse l'ARL sous contrôle ; mesurer le taux d'alerte sur une période propre.
- **Poser des limites de Shewhart sur un signal autocorrélé** sans le dire : fausses alertes en rafale, puis réglage « à la louche » qui masque les vrais défauts.
- **Étage 2 entraîné sur l'historique brut** : arrêts, pannes et capteurs défectueux deviennent du normal.
- **Étage 1 jamais relu** : un changement de procédé ou de capteur décale les limites ; les revoir à intervalle fixé ([[Data drift]]).
- **Modèle qui s'adapte trop vite** : il absorbe la dérive qu'on veut voir. Un modèle figé accumule des fausses alertes au changement de régime.
- **Confondre stable et conforme** : une carte de contrôle dit qu'un procédé est stable, un indice de capabilité qu'il respecte la tolérance ; le second n'a de sens que sous le premier.
- **Deux étages pour paraître sérieux** : si l'étage 1 attrape tous les défauts connus, l'étage 2 n'ajoute que de la maintenance de modèle.

## Voir aussi

- [[Contrôle statistique de procédé (SPC)]] — l'étage 1, avec ses limites sous autocorrélation
- [[Détection d'anomalies en ligne]] — l'étage 2 quand le flux ne se stocke pas
- [[Time series anomaly detection]] — la notion d'ensemble sur les séries
- [[Pattern - Pipeline de maintenance prédictive on-prem]] — où ce montage se place dans la chaîne
- [[Rule - Entraîner sur du normal vérifié]], [[Rule - Évaluer une anomalie par événement, pas par point]]
