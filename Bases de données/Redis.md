---
role: brique
nom: Redis
alias: [redis]
pitch: "Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub."
categorie: database/cle-valeur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[MongoDB]]", "[[Apache Cassandra]]"]
complements: ["[[Redis Insight]]"]
tags: [nosql, key-value, in-memory]
url_docs: https://redis.io/docs/
url_repo: https://github.com/redis/redis
---

# Redis

<!-- AUTO:BANDEAU:START -->
> Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Store **clé-valeur en mémoire** : les données vivent en RAM, d'où des latences
sub-milliseconde. Au-delà du simple cache, Redis expose des **structures riches** — listes,
sets, hash, sorted sets, streams, HyperLogLog — qui en font un couteau suisse : cache
applicatif, sessions, compteurs, files d'attente, classements, pub/sub et broker de messages.
Le chemin de commande est **mono-thread**, donc déterministe et sans contention de verrou. La
persistance est optionnelle : snapshots RDB ou journal AOF.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cache devant une base plus lente, pour réduire charge et latence de lecture | Tout tient en RAM : dépasser `maxmemory` déclenche l'éviction, ou l'OOM |
| Sessions, rate-limiting, compteurs, verrous distribués | Persistance non garantie par défaut : selon la configuration, un crash perd les écritures récentes |
| File de jobs ou broker léger (listes, streams) et pub/sub temps réel | Mono-thread : une commande coûteuse — `KEYS *`, un gros `SORT` — bloque tout le serveur |
| Classements et fenêtres temporelles via les sorted sets | Redis Cluster impose ses contraintes : slots, et opérations multi-clés limitées au même slot |

## Mise en œuvre

- Installation — self-host par paquet ou Docker, ou managé (Redis Cloud, AWS ElastiCache et MemoryDB, Azure Cache)
- Point d'entrée — le protocole Redis, depuis un client ou un pilote
- Prérequis — de la RAM dimensionnée sur le jeu de données, et une `maxmemory-policy` choisie
- Exécution — self-hébergé ou managé ; mono-nœud par défaut, réplicas pour la disponibilité, Redis Cluster pour le sharding horizontal
- Coût — gratuit ; licence BSD à l'origine, passée SSPL/RSALv2 en 2024 — ce qui a déclenché le fork Valkey — puis revenue open-source sous AGPLv3 avec Redis 8, en mai 2025

## Écosystème

### Alternatives

- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

### Compléments

- [[Redis Insight]] — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search). — le client officiel pour explorer les clés et profiler l'instance.

## Ressources

- Documentation — https://redis.io/docs/
- Dépôt — https://github.com/redis/redis

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases NoSQL]] — ce qui départage les moteurs du dossier
