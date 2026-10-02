---
role: rule
domaine: evaluation
applicable: anomaly-detection
strictness: must
tags: [rule, anomaly-detection, model-evaluation, thresholding]
---

# Rule — Évaluer une anomalie par événement, pas par point

## Principe

Une anomalie de série est un segment, et l'exploitation traite des événements : compter par point favorise les longs segments et flatte des métriques que le hasard suffit à faire monter. On rapporte ce que l'équipe de maintenance vit : événements trouvés, délai, fausses alertes par jour.

## MUST

- Rapporter au moins : le nombre d'événements détectés sur le nombre d'événements réels, le **délai de détection**, et le nombre de **fausses alertes par jour** (ou par semaine).
- Regrouper les alertes consécutives en un événement avant de compter ou d'envoyer : une anomalie qui dure cinq minutes n'est pas trois cents alertes ([[Score et seuil d'alerte]]).
- **Ne jamais rapporter le point-adjust seul.** Il compte comme détecté tout le segment dès qu'un point franchit le seuil, et un score aléatoire suffit presque à le satisfaire. Si un article reproduit l'emploie, recalculer sans l'ajustement et comparer à un score aléatoire et à un score trivial (la valeur brute, sa différence) ([[Évaluer une détection d'anomalies]]).
- Calculer la **référence aléatoire** de chaque métrique sur son propre jeu : un AUPR de 0,3 est excellent pour 1 % d'anomalies, médiocre pour 20 %.

## SHOULD

- Rapporter une métrique indépendante du seuil (AUPR, ou VUS-PR sur des séries) **et** une métrique à seuil fixé, avec le seuil choisi sur du normal vérifié ([[Rule - Entraîner sur du normal vérifié]]).
- Donner un intervalle d'incertitude (bootstrap) : peu d'événements de test donnent des valeurs instables.
- Mettre le résultat en coût dès que $c_p$ et $c_f$ sont connus : [[Politique de maintenance et coût]].
- En vision, lire l'AU-PRO avec l'AUROC image : une carte pixel est dominée par les grandes régions ([[Détection d'anomalies visuelle]]).
- Comparer à l'étage de règles seul, pas à rien ([[Pattern - Détection d'anomalies en deux étages]]).

## NICE-TO-HAVE

- Ajouter une métrique par événement paramétrée par la tolérance de l'exploitation (l'affiliation, par exemple), en gardant à l'esprit que sur les scénarios synthétiques de TSB-AD elle distingue mal les cas entre eux : ne pas l'employer comme seule métrique.
- Publier avec le résultat le calendrier des événements manqués : ce sont eux que l'équipe voudra relire.

## Exemples

### Bon

```text
événements réels      : 12      détectés : 9      manqués : 3
délai de détection    : médiane 14 min, pire cas 2 h 10
fausses alertes       : 0,4 par jour (budget de l'équipe : 1 par jour)
score aléatoire, même jeu : 2 événements détectés, 3,1 fausses alertes par jour
```

### Mauvais

```text
F1 = 0,96   (point-adjust, seuil réglé sur le jeu de test, aucune référence)
```

## Exceptions

- Le point est l'unité de décision (une mesure isolée à rejeter, un capteur qui décroche à l'échantillon) : la métrique par point est alors la bonne, et se rapporte avec sa référence aléatoire.
- Aucun événement étiqueté (non supervisé pur) : ne pas rapporter de métrique ; décrire les alertes relues par un opérateur, et le dire.
- Image par image : la décision se prend à l'image ; rapporter une métrique image **et** une métrique pixel, sans les confondre.

## Voir aussi

- [[Évaluer une détection d'anomalies]] — point-adjust et son biais, métriques par événement, VUS-PR, AU-PRO
- [[Score et seuil d'alerte]] — budget d'alertes, fatigue d'alerte
- [[Politique de maintenance et coût]] — traduire un résultat en coût
- [[Pattern - Pipeline de maintenance prédictive on-prem]] — où l'évaluation par événement se branche
- [[Rule - Entraîner sur du normal vérifié]]
