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

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
