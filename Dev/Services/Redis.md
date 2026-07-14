---
galaxie: dev
type: service
nom: Redis
alias: [redis]
pitch: "Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub."
categorie: database/keyvalue
licence_type: open-source
hosted: both
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Dev/Services/MongoDB|MongoDB]]", "[[Dev/Services/Apache Cassandra|Apache Cassandra]]"]
remplace_par: []
status: actif
tags: [nosql, key-value, in-memory]
url_docs: https://redis.io/docs/
url_repo: https://github.com/redis/redis
---

# Redis

## Pourquoi

Store **clé-valeur en mémoire** : les données vivent en RAM, d'où des latences sub-milliseconde. Au-delà du simple cache, Redis expose des **structures riches** (listes, sets, hash, sorted sets, streams, HyperLogLog) qui en font un couteau suisse : cache applicatif, sessions, compteurs, files d'attente, classements, pub/sub et broker de messages. Le chemin de commande est mono-thread, donc déterministe et sans contention de verrou.

## Quand l'utiliser

- Cache devant une base plus lente, pour réduire charge et latence de lecture.
- Sessions, rate-limiting, compteurs, verrous distribués.
- File de jobs ou broker léger (listes, streams) et pub/sub temps réel.
- Classements et fenêtres temporelles via sorted sets.

## Quand NE PAS l'utiliser

- Source de vérité durable au-delà de ce qui tient en RAM → base sur disque ([[Dev/Services/Postgres|Postgres]], [[Dev/Services/MongoDB|MongoDB]]).
- Requêtes ad hoc riches sur les données → [[Dev/Services/MongoDB|MongoDB]].
- Très gros volumes répartis sur de nombreux nœuds en écriture → [[Dev/Services/Apache Cassandra|Apache Cassandra]].

## Déploiement & coût

- Self-host (Docker, paquet) ou managé (Redis Cloud, AWS ElastiCache/MemoryDB, Azure Cache).
- Persistance optionnelle (snapshots RDB, journal AOF) ; réplicas pour la HA ; **Redis Cluster** pour le sharding horizontal.
- Licence : BSD à l'origine, passée **SSPL/RSALv2** en 2024 (déclencheur du fork **Valkey**), **revenue open-source sous AGPLv3** avec Redis 8 (mai 2025).

## Pièges

- Tout en RAM : dépasser la mémoire déclenche l'éviction (`maxmemory-policy`) ou l'OOM.
- Persistance non garantie par défaut : un crash peut perdre les écritures récentes selon la config.
- Mono-thread : une commande coûteuse (`KEYS *`, gros `SORT`) bloque tout le serveur.
- Redis Cluster impose des contraintes (slots, opérations multi-clés limitées au même slot).

## Alternatives

- [[Dev/Services/MongoDB|MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Dev/Services/Apache Cassandra|Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases NoSQL]] — comparatif des moteurs NoSQL
- Doc : https://redis.io/docs/
