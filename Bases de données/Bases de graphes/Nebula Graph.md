---
role: brique
nom: Nebula Graph
alias: [nebula, nebula graph, nebulagraph]
pitch: "Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée."
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
> Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes **distribuée nativement**, conçue pour les graphes qui ne tiennent pas sur
une seule machine — centaines de milliards de nœuds et d'arêtes. L'architecture sépare trois
rôles : *graphd* pour le calcul des requêtes, *storaged* pour le stockage partitionné,
*metad* pour les métadonnées, chacun montant en charge indépendamment par ajout de nœuds. Le
stockage est shardé et répliqué par Raft. Le langage **nGQL** est proche de Cypher sans lui être identique : la
documentation parle de compatibilité partielle avec openCypher 9, et aucun support de GQL n'a été trouvé. Relevé le
2026-09-30 : la dernière version stable est la **3.8.0** (2024-05-17), environ 12 400 étoiles, Apache-2.0.
Le dépôt reçoit peu de code (deux commits fonctionnels en douze mois) ; les algorithmes de graphe et la recherche
vectorielle sont annoncés dans l'édition Enterprise 5.x, dont le code n'est pas public.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Très grands graphes dépassant la capacité d'un nœud unique, avec scale-out horizontal attendu | Trois services distincts à déployer et superviser : la barrière opérationnelle dépasse celle d'un moteur mono-instance |
| Forte volumétrie d'écriture concurrente : ingestion continue de relations | Le nombre de partitions se fige à la création : le modifier à chaud impose une réingestion |
| Haute disponibilité et réplication multi-nœuds intégrées, par Raft | Écosystème et outillage plus jeunes : pilotes, visualisation, algorithmes prêts à l'emploi |
| Parcours sur graphes massifs : recommandation à grande échelle, antifraude, knowledge graph d'entreprise | nGQL ressemble à Cypher sans lui être identique (`==` au lieu de `=`, schéma fort, rang d'arête) : un portage n'est pas automatique |
| | Maintenance : aucune release depuis la 3.8.0 (mai 2024), et le développement des fonctions nouvelles passe par l'édition Enterprise, propriétaire — à peser pour un projet sur plusieurs années |
| | Petit projet ou prototype : la complexité opérationnelle du cluster ne se rembourse pas |
| | Données peu connectées, modèle tabulaire et transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — cluster self-host des trois services (graphd, storaged, metad), ou managé sur Nebula Graph Cloud
- Point d'entrée — nGQL, proche de Cypher ; compatibilité partielle avec openCypher 9
- Prérequis — le nombre de partitions décidé avant la première ingestion
- Exécution — self-hébergé ou managé ; distribué, scaling par ajout de nœuds graphd et storaged, réplicas Raft réglables
- Coût — gratuit, Apache 2.0 pour le cœur, Studio et Dashboard (Algorithm ne déclare pas de licence) ; l'édition Enterprise est propriétaire ; le coût réel est l'exploitation du cluster distribué

## Écosystème

### Alternatives

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).

## Ressources

- Documentation — https://docs.nebula-graph.io/
- Dépôt — https://github.com/vesoft-inc/nebula
- Documentation — compatibilité de nGQL avec openCypher : https://docs.nebula-graph.io/3.8.0/3.ngql-guide/1.nGQL-overview/1.overview/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[Graph Neural Networks]] — le ML sur graphes, branché sur les données stockées ici
