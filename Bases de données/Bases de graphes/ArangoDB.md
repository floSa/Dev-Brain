---
role: brique
nom: ArangoDB
alias: [arangodb, Arango, AQL]
pitch: "Base multi-modèle (documents, graphes, clé-valeur, recherche) interrogée en AQL (C++, BSL 1.1) — cluster complet, mais binaires Community limités à un usage interne sous 100 Go de données, licence commerciale au-delà."
categorie: database/graphe
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Neo4j]]"]
complements: []
tags: [graph-db, document-db, distributed]
url_docs: https://docs.arango.ai/arangodb/3.12/
url_repo: https://github.com/arangodb/arangodb
---

# ArangoDB

<!-- AUTO:BANDEAU:START -->
> Base multi-modèle (documents, graphes, clé-valeur, recherche) interrogée en AQL (C++, BSL 1.1) — cluster complet, mais binaires Community limités à un usage interne sous 100 Go de données, licence commerciale au-delà.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | source-available | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base **multi-modèle** : des documents JSON, des graphes, du clé-valeur et de la recherche
plein texte (ArangoSearch) dans un seul moteur, interrogés par un seul langage, **AQL**, sur
un stockage RocksDB. En cluster, trois rôles : des *Agents* qui portent la configuration par
Raft, des *Coordinateurs* sans état qui reçoivent les requêtes, des *DB-Servers* qui stockent
les shards avec réplication synchrone ; les graphes se partitionnent par SmartGraphs et
satellites. Depuis la 3.12.5, la Community contient toutes les fonctions autrefois
réservées à Enterprise (SmartGraphs, satellites, sauvegarde à chaud, chiffrement). Relevé le
2026-09-30 : **3.12.12.1** (tag du 2026-09-29), environ 14 280 étoiles, une dizaine de tags
en douze mois. La documentation ne mentionne ni Cypher, ni Gremlin.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des documents, des graphes et de la recherche dans un seul moteur et un seul langage, plutôt que trois bases | Un jeu de données de 100 Go ou plus en Community, un usage non interne, une redistribution ou un embarquement : la licence des binaires les interdit, une licence commerciale est requise |
| Un jeu de données sous 100 Go agrégés sur le cluster, ou une licence Enterprise achetée | Une offre qui donne à des tiers l'accès à des bases ArangoDB (DBaaS) : interdite par la BSL 1.1 |
| Un cluster à réplication synchrone, avec SmartGraphs et sauvegarde à chaud sans licence de fonctions en plus | Cypher, Gremlin ou GraphQL exigés : AQL est le seul langage documenté |
| GraphRAG et vecteurs par l'Arango Contextual Data Platform (4.0 en disponibilité générale en avril 2026) | Un environnement sans accès réseau : les clés Enterprise sont de courte durée, avec activation en ligne |
| | Un graphe pur et petit, sans document à côté : ce moteur en fait plus que nécessaire |

## Mise en œuvre

- Installation — cluster self-host (Agents, Coordinateurs, DB-Servers) ou instance unique ; ou managé sur Arango Managed Platform (AWS, GCP)
- Point d'entrée — AQL, depuis l'interface web ou un pilote
- Prérequis — la licence des binaires lue avant tout déploiement : le seuil de 100 Go se mesure sur l'ensemble du cluster
- Exécution — self-hébergé ou managé ; distribué, modèle CP, réplication synchrone leader/followers
- Coût — code en BSL 1.1 (conversion vers Apache-2.0 au quatrième anniversaire de la date de sortie, donc en 2028) ; binaires Community gratuits sous une licence d'usage interne ; Enterprise commerciale

## Limites à connaître

- **Trois textes, pas un.** Le code source est en BSL 1.1 (usage interne en production autorisé, DBaaS interdit, aucune limite de taille). Les **binaires** officiels suivent l'ArangoDB Community License : usage interne, moins de 100 Go agrégés, ni redistribution ni embarquement, audit possible, résiliation possible par l'éditeur. Compiler soi-même le code BSL lève-t-il le plafond ? Aucune source lue ne le dit.
- **Dates de release approximatives.** La page GitHub Releases est vide ; les dates de version relevées sont celles des commits de tag, pas celles de publication.
- **La plateforme GenAI est un autre produit.** Elle exige Enterprise 3.12.9 au moins et certaines de ses fonctions demandent une licence.

## Écosystème

### Alternatives

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).

## Ressources

- Documentation — https://docs.arango.ai/arangodb/3.12/
- Dépôt — https://github.com/arangodb/arangodb
- Documentation — les incompatibilités et le texte de licence de la 3.12 : https://docs.arango.ai/arangodb/3.12/release-notes/version-3.12/incompatible-changes-in-3-12/
- Documentation — le fichier LICENSE du dépôt : https://github.com/arangodb/arangodb/blob/devel/LICENSE

## Voir aussi

- [[Bases de graphes]] — le hub du sous-domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[MongoDB]] — le document pur, sans graphe
