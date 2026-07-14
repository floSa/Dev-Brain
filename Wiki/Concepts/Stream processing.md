---
galaxie: wiki
type: concept
nom: Stream processing
alias: [stream processing, traitement de flux, windowing, fenêtrage, watermarks, exactly-once, event-time]
categorie: concept/data
domaines: [data-eng]
tags: [streaming, data-pipeline, idempotence]
---

# Stream processing

## Aperçu

- Traiter des événements **en continu**, au fil de l'eau, plutôt que par lots planifiés : agrégations, jointures, détection de motifs sur un flux sans fin.
- Difficulté centrale : un flux est **non borné** et **désordonné**. Tout le sujet est de produire des résultats corrects malgré des événements tardifs, et de garantir qu'on ne perd ni ne double rien.

## Concepts clés

### Event-time vs processing-time
- **Event-time** : l'instant où l'événement s'est produit (estampillé à la source).
- **Processing-time** : l'instant où le moteur le traite.
- Les deux divergent (latence réseau, rejeu, panne). Compter « par heure » n'a de sens qu'en **event-time** ; sinon un retard décale silencieusement les agrégats dans la mauvaise fenêtre.

### Windowing (fenêtrage)
- Découper un flux infini en **fenêtres** finies pour pouvoir agréger.
- **Tumbling** : fenêtres fixes contiguës (toutes les 5 min, sans recouvrement).
- **Sliding** : fenêtres de taille fixe qui se chevauchent (5 min, glissant toutes les 1 min).
- **Session** : fenêtres délimitées par des trous d'inactivité (regroupe l'activité d'un utilisateur).

### Watermarks
- Estimation du moteur : « j'ai probablement vu tous les événements jusqu'à l'instant *t* ».
- Le watermark **autorise la fermeture** d'une fenêtre event-time : il arbitre entre attendre les retardataires (latence) et émettre le résultat (fraîcheur).
- Un événement arrivé **après** le watermark est *late* : à laisser tomber, ou à router vers un traitement de correction. Réglage subtil — trop serré perd des données, trop lâche ajoute de la latence.

### État & jointures
- Le traitement est **stateful** : fenêtres, compteurs, jointures de flux maintiennent un état entre événements.
- Cet état doit survivre aux pannes → il est **snapshotté** périodiquement (checkpointing). C'est le vrai coût opérationnel du streaming.

### Garanties de livraison
- **At-most-once** : on peut perdre des événements (rapide, fragile).
- **At-least-once** : aucun perdu, mais doublons possibles au rejeu.
- **Exactly-once** : effet observé une seule fois, malgré rejeux et pannes — obtenu par checkpointing de l'état + sinks transactionnels ou **idempotents**. En pratique « effectively-once » = at-least-once + écriture idempotente. Cf. [[ELT vs ETL & idempotence]].

## En pratique

- Moteur de référence en brain : [[Dev/Services/Flink|Flink]] — vrai streaming stateful, event-time/watermarks natifs, exactly-once par checkpointing. Alternatives hors brain : Spark Structured Streaming (micro-batch), Kafka Streams (bibliothèque couplée à Kafka).
- Raisonner d'abord en **event-time** et fixer la politique de watermark / late data **avant** de coder les fenêtres : c'est là que se logent les bugs silencieux.
- Rendre les sinks **idempotents** (upsert par clé) : c'est ce qui transforme un at-least-once robuste en résultat exactly-once observable, sans dépendre d'un commit transactionnel parfait.
- Côté stockage aval : un sink streaming produit beaucoup de petits fichiers → prévoir la compaction. Cf. [[Partitionnement & layout de données]].
- Ne pas dégainer le streaming par défaut : un batch incrémental toutes les X minutes ([[ELT vs ETL & idempotence|ELT]] orchestré) couvre une grande part des besoins « temps réel » pour une fraction du coût d'exploitation.
- Pièges : confondre event-time et processing-time, watermark mal calibré, état qui gonfle sans borne (TTL manquant), exactly-once supposé mais sink non idempotent.

## Approches voisines & alternatives

- [[Dev/Services/Flink|Flink]] — le moteur de flux stateful (event-time, watermarks, exactly-once).
- [[Change Data Capture (CDC)]] — produit un flux de changements, consommateur typique d'un moteur de streaming.
- [[ELT vs ETL & idempotence]] — l'alternative micro-batch, et la clé de l'exactly-once (idempotence du sink).
- [[Partitionnement & layout de données]] — gérer les petits fichiers générés en sortie de flux.
- Alternative : batch incrémental planifié — plus simple à opérer quand la latence de quelques minutes est tolérable.

## Pour aller plus loin

- Le « Dataflow model » (Google) — cadre de référence event-time / windowing / watermarks / triggers.
- Bus de messages amont : Apache Kafka (source/sink de flux le plus courant) — candidat service Dev.
