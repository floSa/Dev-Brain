---
role: brique
nom: JanusGraph
alias: [janusgraph, Janus, Janus Graph, TinkerPop JanusGraph]
pitch: "Couche de graphe Java au-dessus de Cassandra, ScyllaDB ou HBase et d'un index Elasticsearch ou Solr (Apache-2.0, Linux Foundation) — Gremlin, milliards de sommets ; trois composants à opérer, et aucune version stable depuis novembre 2024."
categorie: database/graphe
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Nebula Graph]]", "[[Dgraph]]"]
complements: ["[[Apache Cassandra]]", "[[Elasticsearch]]"]
tags: [graph-db, distributed]
url_docs: https://docs.janusgraph.org/
url_repo: https://github.com/JanusGraph/janusgraph
---

# JanusGraph

<!-- AUTO:BANDEAU:START -->
> Couche de graphe Java au-dessus de Cassandra, ScyllaDB ou HBase et d'un index Elasticsearch ou Solr (Apache-2.0, Linux Foundation) — Gremlin, milliards de sommets ; trois composants à opérer, et aucune version stable depuis novembre 2024.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Une **couche de graphe** et non une base complète : JanusGraph range sommets et arêtes dans
un stockage clé-colonne qu'il ne fournit pas (Cassandra, ScyllaDB, HBase, Bigtable,
BerkeleyDB), et délègue la recherche par propriété à un index externe (Elasticsearch, Solr
ou Lucene). Le langage est **Gremlin**, celui d'Apache TinkerPop : un parcours impératif, sans
Cypher natif. Les garanties transactionnelles (ACID ou cohérence à terme) sont celles du
backend choisi ; la cible annoncée est des centaines de milliards d'éléments. Projet de la
Linux Foundation, code en Apache-2.0. Relevé le 2026-09-30 : dernière version stable
**1.1.0** (2024-11-07, TinkerPop 3.7), une 1.2.0 (TinkerPop 3.8, Cassandra 5,
Elasticsearch 9) sans date dans la documentation, environ 5 840 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un graphe de plusieurs milliards d'éléments, avec une équipe qui exploite déjà Cassandra ou HBase et Elasticsearch | Un volume modeste ou une équipe réduite : trois composants à déployer, régler et superviser (le backend, l'index, JanusGraph avec son serveur Gremlin) |
| Gremlin et TinkerPop, pour un code portable entre moteurs qui le parlent | Du Cypher : JanusGraph n'en parle pas nativement |
| Choisir soi-même le compromis du stockage : cohérence, latence, coût, selon le backend | Un support contractuel ou un service managé : aucune offre managée n'a été trouvée |
| Apache-2.0, sans édition payante, sous gouvernance de fondation | Une version stable récente : la 1.1.0 date de novembre 2024, et les commits des dernières semaines viennent presque tous d'une seule personne |
| | Un modèle tabulaire, des transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — JanusGraph avec son serveur Gremlin, plus un backend de stockage et un index externe, tous à déployer ; les versions testées de la 1.1.0 sont Cassandra 3.11 et 4.0, HBase 2.6, ScyllaDB 6.2 et BerkeleyDB JE, sous Java 8 ou 11
- Point d'entrée — Gremlin, depuis la console, le serveur Gremlin ou un pilote TinkerPop
- Prérequis — le choix du backend et de l'index avant la première écriture ; une équipe qui sait les opérer
- Exécution — self-hébergé ; distribué, le scaling étant celui du backend
- Coût — gratuit, Apache-2.0 (la documentation est en CC-BY 4.0) ; le coût réel est l'exploitation des trois composants

## Limites à connaître

- **Activité concentrée.** Dix-sept commits entre le 2026-09-21 et le 2026-09-29, presque tous signés d'une même personne ; le nombre de contributeurs n'a pas pu être lu. Le risque est celui d'un projet tenu par très peu de mains, pas celui d'un projet à l'arrêt.
- **La reprise par un grand éditeur n'est pas établie.** Seul un membre de comité d'IBM, en 2017, est ressorti des recherches ; rien ne confirme un soutien actuel.
- **Adoption déclarée, non datée.** Airbnb, eBay, Red Hat et Target sont cités sur le site du projet, Netflix et Uber sur la page GitHub ; aucune date d'usage n'est donnée.

## Écosystème

### Alternatives

- [[Nebula Graph]] — Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée.
- [[Dgraph]] — Base de graphes distribuée en Go (Apache-2.0) — sharding par prédicat, Raft, DQL et GraphQL natif ; reprise par Istari Digital en 2025, sans offre managée ni Cypher, et à la gouvernance encore fragile.

### Compléments

- [[Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter. — l'un des backends de stockage, celui des déploiements les plus répandus.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — l'un des index externes, pour la recherche par propriété et le full-text.

## Ressources

- Documentation — https://docs.janusgraph.org/
- Dépôt — https://github.com/JanusGraph/janusgraph
- Documentation — les versions et leurs dépendances : https://docs.janusgraph.org/changelog/
- Documentation — Apache TinkerPop et Gremlin : https://tinkerpop.apache.org/

## Voir aussi

- [[Bases de graphes]] — le hub du sous-domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[Bases graphe — modèles et langages de requête]] — la notion : modèles, langages de requête, et quand un graphe bat un relationnel (Gremlin face à Cypher et GQL)
