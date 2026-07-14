---
galaxie: dev
type: service
nom: Nebula Graph
alias: [nebula, nebula graph, nebulagraph]
pitch: "Base de graphes distribuée pour jeux de données massifs."
categorie: database/graph
licence_type: open-source
hosted: both
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/Neo4j|Neo4j]]"]
remplace_par: []
status: actif
tags: [graph-db, distributed]
url_docs: https://docs.nebula-graph.io/
url_repo: https://github.com/vesoft-inc/nebula
---

# Nebula Graph

## Pourquoi

Base de graphes **distribuée nativement**, conçue pour les graphes qui ne tiennent pas sur une seule machine (centaines de milliards de nœuds et d'arêtes). L'architecture sépare trois rôles — *graphd* (calcul des requêtes), *storaged* (stockage partitionné) et *metad* (métadonnées) — chacun scalant indépendamment par ajout de nœuds. Le stockage est partitionné (sharding) et répliqué via Raft pour la cohérence. Le langage **nGQL** est proche de Cypher et le moteur supporte aussi openCypher. Le compromis assumé : la distribution massive au prix d'une exploitation plus lourde qu'un moteur mono-instance.

## Quand l'utiliser

- Très grands graphes dépassant la capacité d'un nœud unique, avec scale-out horizontal attendu.
- Forte volumétrie d'écriture concurrente sur le graphe (ingestion continue de relations).
- Besoin de haute disponibilité et de réplication multi-nœuds intégrées (Raft).
- Charges de parcours sur graphes massifs : recommandation à grande échelle, antifraude, knowledge graph d'entreprise.

## Quand NE PAS l'utiliser

- Graphe tenant sur un nœud, écosystème et maturité d'outillage prioritaires → [[Dev/Services/Neo4j|Neo4j]].
- Données peu connectées, modèle tabulaire et transactions classiques → [[Dev/Services/Postgres|Postgres]].
- Petit projet ou prototype : la complexité opérationnelle du cluster ne se justifie pas → [[Dev/Services/Neo4j|Neo4j]].

## Déploiement & coût

- Self-host (cluster multi-nœuds des trois services) ou managé via **Nebula Graph Cloud**.
- Scaling horizontal par ajout de nœuds storaged/graphd ; partitions et réplicas Raft réglables.
- Licence **Apache 2.0**, gratuit et OSI ; le coût réel est l'exploitation du cluster distribué.

## Pièges

- Trois services distincts à déployer et superviser : la barrière d'entrée opérationnelle dépasse celle d'un moteur mono-instance.
- Dimensionner le nombre de partitions dès la création : il ne se modifie pas à chaud sans réingestion.
- Écosystème et outillage plus jeunes que Neo4j (pilotes, viz, algorithmes prêts à l'emploi).
- nGQL ressemble à Cypher mais n'est pas identique : portage non automatique.

## Alternatives

- [[Dev/Services/Neo4j|Neo4j]] — SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases graphes]] — comparatif des moteurs de graphe
- [[Wiki/Concepts/Graph Neural Networks|Graph Neural Networks]] — ML sur graphes, branché sur les données stockées ici
- Doc : https://docs.nebula-graph.io/
