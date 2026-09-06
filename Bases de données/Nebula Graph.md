---
role: brique
nom: Nebula Graph
alias: [nebula, nebula graph, nebulagraph]
pitch: "Base de graphes distribuée pour jeux de données massifs."
categorie: database/graphe
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Neo4j]]"]
complements: []
tags: [graph-db, distributed]
url_docs: https://docs.nebula-graph.io/
url_repo: https://github.com/vesoft-inc/nebula
---

# Nebula Graph

<!-- AUTO:BANDEAU:START -->
> Base de graphes distribuée pour jeux de données massifs.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes **distribuée nativement**, conçue pour les graphes qui ne tiennent pas sur
une seule machine — centaines de milliards de nœuds et d'arêtes. L'architecture sépare trois
rôles : *graphd* pour le calcul des requêtes, *storaged* pour le stockage partitionné,
*metad* pour les métadonnées, chacun montant en charge indépendamment par ajout de nœuds. Le
stockage est shardé et répliqué par Raft. Le langage **nGQL** est proche de Cypher, que le
moteur accepte aussi via openCypher.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Très grands graphes dépassant la capacité d'un nœud unique, avec scale-out horizontal attendu | Trois services distincts à déployer et superviser : la barrière opérationnelle dépasse celle d'un moteur mono-instance |
| Forte volumétrie d'écriture concurrente : ingestion continue de relations | Le nombre de partitions se fige à la création : le modifier à chaud impose une réingestion |
| Haute disponibilité et réplication multi-nœuds intégrées, par Raft | Écosystème et outillage plus jeunes : pilotes, visualisation, algorithmes prêts à l'emploi |
| Parcours sur graphes massifs : recommandation à grande échelle, antifraude, knowledge graph d'entreprise | nGQL ressemble à Cypher sans lui être identique : un portage n'est pas automatique |
| | Petit projet ou prototype : la complexité opérationnelle du cluster ne se rembourse pas |
| | Données peu connectées, modèle tabulaire et transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — cluster self-host des trois services (graphd, storaged, metad), ou managé sur Nebula Graph Cloud
- Point d'entrée — nGQL, proche de Cypher ; openCypher également accepté
- Prérequis — le nombre de partitions décidé avant la première ingestion
- Exécution — self-hébergé ou managé ; distribué, scaling par ajout de nœuds graphd et storaged, réplicas Raft réglables
- Coût — gratuit, licence Apache 2.0 ; le coût réel est l'exploitation du cluster distribué

## Écosystème

### Alternatives

- [[Neo4j]] — SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.

## Ressources

- Documentation — https://docs.nebula-graph.io/
- Dépôt — https://github.com/vesoft-inc/nebula

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[Graph Neural Networks]] — le ML sur graphes, branché sur les données stockées ici
