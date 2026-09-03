---
role: comparatif
nom: Comparatif - Bases graphes
categorie: database/graphe
tags: [graph-db]
---

# Comparatif - Bases graphes

> On tranche sur : le graphe tient-il sur un nœud, et à quel prix d'exploitation.

![[Comparatif - Bases graphes.base]]

## Ce qui départage

- [[Neo4j]] — le plus mûr : Cypher, algorithmes GDS, outillage de viz ; mais Community est mono-instance et la montée en charge reste verticale.
- [[Nebula Graph]] — distribuée nativement (graphd, storaged, metad, réplication Raft) : trois services à exploiter, et le nombre de partitions se fige à la création.
