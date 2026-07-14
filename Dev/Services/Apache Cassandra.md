---
galaxie: dev
type: service
nom: Apache Cassandra
alias: [cassandra, apache cassandra]
pitch: "Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter."
categorie: database/wide-column
licence_type: open-source
hosted: both
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Dev/Services/MongoDB|MongoDB]]", "[[Dev/Services/Redis|Redis]]"]
remplace_par: []
status: actif
tags: [nosql, wide-column, distributed]
url_docs: https://cassandra.apache.org/doc/
url_repo: https://github.com/apache/cassandra
---

# Apache Cassandra

## Pourquoi

Base NoSQL **wide-column** distribuée, conçue pour le volume et la disponibilité. Architecture **sans maître** (peer-to-peer) : tous les nœuds sont égaux, pas de point unique de défaillance, et ajouter des nœuds augmente la capacité de façon quasi linéaire. Réplication multi-datacenter native et cohérence **réglable par requête** (de `ONE` à `QUORUM`/`ALL`). Le modèle se pense autour des requêtes : on dénormalise et on modélise par pattern d'accès, pas par entité.

## Quand l'utiliser

- Écritures massives et continues (télémétrie, logs, IoT, séries d'événements).
- Haute disponibilité « always-on » et déploiement multi-région / multi-datacenter.
- Volumes dépassant un seul nœud, avec scale-out linéaire attendu.
- Charge dont les patterns de lecture sont connus d'avance et stables.

## Quand NE PAS l'utiliser

- Requêtes ad hoc, jointures, agrégations imprévues → [[Dev/Services/Postgres|Postgres]] ou [[Dev/Services/MongoDB|MongoDB]].
- Petit volume mono-nœud : la complexité opérationnelle ne se justifie pas → [[Dev/Services/Postgres|Postgres]].
- Cache ou structures en mémoire → [[Dev/Services/Redis|Redis]].

## Déploiement & coût

- Self-host (cluster de nœuds, JVM à tuner) ou managé (DataStax Astra, Amazon Keyspaces).
- Scaling horizontal par ajout de nœuds ; réplication réglable par datacenter.
- Licence **Apache 2.0**, gratuit et OSI ; le coût réel est l'exploitation du cluster (JVM, compaction, réparations).

## Pièges

- Modéliser par entité plutôt que par requête mène à des partitions inexploitables.
- Pas de jointures ni d'agrégations libres ; `ALLOW FILTERING` est un piège à scans.
- Partitions trop larges ou « hot partitions » dégradent tout le cluster.
- Exploitation JVM exigeante : compaction, repair et tombstones à surveiller.

## Alternatives

- [[Dev/Services/MongoDB|MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Dev/Services/Redis|Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases NoSQL]] — comparatif des moteurs NoSQL
- Doc : https://cassandra.apache.org/doc/
