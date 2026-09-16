---
role: brique
nom: Memgraph
alias: [memgraph, Memgraph DB, memgraph community]
pitch: "Base de graphes en mémoire, compatible Cypher et Bolt (C++, BSL 1.1) — temps réel et flux Kafka, mono-nœud ; haute disponibilité automatique, RBAC et SSO réservés à l'édition Enterprise."
categorie: database/graphe
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Neo4j]]", "[[Apache AGE]]"]
complements: []
tags: [graph-db, in-memory]
url_docs: https://memgraph.com/docs
url_repo: https://github.com/memgraph/memgraph
---

# Memgraph

<!-- AUTO:BANDEAU:START -->
> Base de graphes en mémoire, compatible Cypher et Bolt (C++, BSL 1.1) — temps réel et flux Kafka, mono-nœud ; haute disponibilité automatique, RBAC et SSO réservés à l'édition Enterprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | source-available | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes de propriétés **en mémoire**, écrite en C++, qui parle Cypher par le
protocole Bolt : les pilotes et les outils de [[Neo4j]] s'y branchent. Tout le graphe vit en
RAM (un nœud pèse environ 204 octets, une arête 154, selon la documentation) ; la durabilité
vient de snapshots et d'un journal WAL, avec des transactions ACID en isolation par snapshot.
Un mode « sur disque » (RocksDB) existe mais reste expérimental, sans réplication ni haute
disponibilité. Autour du moteur : des modules de requête (Python, C/C++, Rust), la
bibliothèque d'algorithmes **MAGE** (plus de 40), des index vectoriels et des flux Kafka,
Pulsar et Redpanda. Relevé le 2026-09-30 : **v3.13.1** (2026-09-14), environ 4 590 étoiles,
une vingtaine de releases en douze mois.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un graphe qui tient dans la RAM d'un serveur, avec une latence basse et des écritures fréquentes : fraude, recommandation en temps réel | Livrer, embarquer ou revendre Memgraph à des tiers, ou l'offrir en service : la BSL 1.1 l'interdit, une licence commerciale est à négocier |
| Cypher et Bolt, pour réutiliser des pilotes et des requêtes écrits pour Neo4j | Une haute disponibilité avec bascule automatique, du RBAC, du SSO, de l'audit ou du multi-tenant sans payer : tout cela est Enterprise, tarifé à la mémoire licenciée |
| Des données qui arrivent en flux (Kafka, Pulsar, Redpanda) et des algorithmes MAGE lancés sur le graphe vivant | Un graphe plus gros que la RAM d'un nœud : pas de sharding, et le mode sur disque est expérimental |
| Un index vectoriel dans la même base, pour du GraphRAG | Une compatibilité Cypher totale : les expressions de label négatives, plusieurs fonctions et la syntaxe des plus courts chemins (`*BFS`) diffèrent de Neo4j |
| Un usage interne en production : la BSL l'autorise | Un modèle tabulaire, des transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — self-host (éditions Community et Enterprise), ou managé sur Memgraph Cloud (AWS, de 1 à 32 Go de RAM)
- Point d'entrée — Cypher sur Bolt, depuis Memgraph Lab ou un pilote
- Prérequis — une RAM dimensionnée sur le graphe entier, index compris ; la licence BSL lue avant tout déploiement chez un client
- Exécution — self-hébergé ou managé ; mono-nœud, avec réplication main/replicas manuelle et bascule manuelle en Community
- Coût — Community gratuite sous BSL 1.1 (conversion vers Apache-2.0 à la date de changement du fichier de licence) ; Enterprise sous licence Memgraph, tarifée selon la mémoire licenciée, prix non publié

## Limites à connaître

- **Licence à lire en entier, pas à survoler.** La BSL 1.1 autorise la production pour un usage interne ; elle interdit de distribuer ou d'embarquer, d'offrir Memgraph en DBaaS et de bâtir un produit concurrent. Le fichier lu nomme « Community Edition version 2.0 » comme œuvre sous licence et écrit la date de conversion « 2030-14-09 » (jour avant mois) : à faire confirmer par l'éditeur avant de s'y fier.
- **MAGE a changé de dépôt.** Le dépôt `memgraph/mage` (Apache-2.0) est archivé depuis le 2026-01-22, fusionné dans le dépôt principal ; la licence des algorithmes depuis la fusion n'a pas été confirmée.
- **Adoption déclarée par l'éditeur.** NASA, Capitec (3,5 millions de cas par jour), Cedars-Sinai et d'autres sont cités sur son site ; aucun de ces usages n'a été recoupé.

## Écosystème

### Alternatives

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).
- [[Apache AGE]] — Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de plus à opérer, mais pas de bibliothèque d'algorithmes ni de scale-out propre.

## Ressources

- Documentation — https://memgraph.com/docs
- Dépôt — https://github.com/memgraph/memgraph
- Documentation — les différences de Cypher avec Neo4j : https://memgraph.com/docs/querying/differences-in-cypher-implementations
- Documentation — les licences : https://github.com/memgraph/memgraph/tree/master/licenses

## Voir aussi

- [[Bases de graphes]] — le hub du sous-domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
