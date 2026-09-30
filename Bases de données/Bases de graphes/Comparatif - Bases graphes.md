---
role: comparatif
nom: Comparatif - Bases graphes
categorie: database/graphe
tags: [graph-db]
---

# Comparatif - Bases graphes

> On tranche sur : le graphe tient-il sur un nœud, à quel prix d'exploitation, et sous quelle licence.

![[Comparatif - Bases graphes.base]]

## Ce qui départage

- [[Neo4j]] — le plus mûr : Cypher, algorithmes GDS, outillage de viz ; mais Community (GPLv3) est mono-instance et la montée en charge reste verticale ; cluster et sauvegarde en ligne demandent Enterprise.
- [[Nebula Graph]] — distribuée nativement (graphd, storaged, metad, réplication Raft) : trois services à exploiter, le nombre de partitions se fige à la création, et la Community n'a pas reçu de release depuis la 3.8.0 (mai 2024).
- [[Memgraph]] — tout le graphe en mémoire, Cypher et Bolt, flux Kafka ; licence BSL (usage interne seulement) et haute disponibilité automatique réservée à Enterprise.
- [[Apache AGE]] — un graphe dans Postgres, joint au relationnel en SQL ; pas de scale-out propre ni de bibliothèque d'algorithmes.
- [[ArangoDB]] — documents, graphes et recherche dans un moteur, en AQL ; les binaires Community sont plafonnés à 100 Go et réservés à un usage interne.
- [[JanusGraph]] — une couche de graphe sans stockage propre : Gremlin sur Cassandra, ScyllaDB ou HBase, avec un index externe ; la plus extensible, la plus lourde à exploiter, et sans version stable depuis novembre 2024.
- [[Dgraph]] — distribuée et en Apache-2.0 pur, partagée par prédicat, avec GraphQL natif ; reprise par Istari Digital en 2025, sans offre managée ni Cypher.

**Pas de fiche ici**, faute d'être éprouvés pour l'on-prem :

- FalkorDB — fork de RedisGraph (abandonné par Redis, fin de support le 2025-01-31), module Redis en SSPL v1 : une offre en service obligerait à ouvrir le code de l'infrastructure. Projet de 2023, société financée par un seed de 3 M$ ; la v6.0.0 du 2026-09-29 est un moteur entièrement réécrit en Rust, sorti la veille du relevé, et un graphe ne se répartit pas sur plusieurs shards.
- Kùzu — base de graphes embarquée : dépôt archivé par son propriétaire le 2025-10-10, dernière release 0.11.3 ; la société aurait été rachetée par Apple, d'après la presse (heise, 2026-02-16, article non ouvert). Les forks sont jeunes : LadybugDB (actif, équipe non nommée), RyuGraph (sans activité depuis janvier 2026).

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Bases de graphes]] — le hub du dossier.
- [[Bases graphe — modèles et langages de requête]] — la notion : modèles, langages de requête, et quand un graphe bat un relationnel.
