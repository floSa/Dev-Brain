---
role: brique
nom: Dgraph
alias: [dgraph, Dgraph Labs, DQL, dgraph-io]
pitch: "Base de graphes distribuée en Go (Apache-2.0) — sharding par prédicat, Raft, DQL et GraphQL natif ; reprise par Istari Digital en 2025, sans offre managée ni Cypher, et à la gouvernance encore fragile."
categorie: database/graphe
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Nebula Graph]]", "[[ArangoDB]]", "[[JanusGraph]]"]
complements: []
tags: [graph-db, distributed]
url_docs: https://docs.dgraph.io/
url_repo: https://github.com/dgraph-io/dgraph
---

# Dgraph

<!-- AUTO:BANDEAU:START -->
> Base de graphes distribuée en Go (Apache-2.0) — sharding par prédicat, Raft, DQL et GraphQL natif ; reprise par Istari Digital en 2025, sans offre managée ni Cypher, et à la gouvernance encore fragile.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes **distribuée nativement**, écrite en Go, stockée sur Badger. Un cluster
compte deux rôles : *Zero* (métadonnées, coordination, rééquilibrage) et *Alpha* (les
données). Le partage se fait **par prédicat** — chaque type de relation est un « tablet »
affecté à un groupe — et non par nœud ; chaque groupe est un groupe Raft, et les requêtes qui
traversent deux groupes sont des jointures distribuées. Deux interfaces : **DQL**, le langage
propre, et une API **GraphQL** générée depuis un schéma ; des index vectoriels (HNSW) existent
depuis la v24. Relevé le 2026-09-30 : **v25.4.1** (2026-08-24), environ 21 800 étoiles,
Apache-2.0, dernier commit le 2026-09-29. Dgraph Labs est passée sous Hypermode (2023), qui a
revendu le projet à Istari Digital en octobre 2025.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un graphe distribué en Apache-2.0 pur : depuis la v25.0.0, l'ancienne licence Enterprise est retirée, et ACL, sauvegarde et chiffrement sont dans le cœur | Un service managé : Istari ne prévoit pas d'hébergement, et aucun fournisseur n'a été trouvé |
| Une API GraphQL servie directement par la base, ou DQL pour des parcours et des index | Du Cypher ou du Gremlin : aucun n'est disponible ; Istari annonce que le langage reste à décider, et que GraphQL devient un effort communautaire |
| Un sharding par relation, adapté à des schémas où chaque prédicat a sa propre charge | Un environnement Windows ou macOS : seuls Linux amd64 et arm64 sont pris en charge |
| Un projet actif en code : release de la v25.4.1 le 2026-08-24 et commits jusqu'au 2026-09-29 | Un éditeur qui engage un support : le projet dépend d'une petite équipe, et sa société a changé de main deux fois |
| | Une exposition non protégée du port d'administration de Zero : avant la v25.4.0, ses points d'entrée HTTP n'avaient aucune authentification |

## Mise en œuvre

- Installation — cluster self-host (Zero et Alpha), sous Linux ; images Docker publiées (environ 24 millions de tirages)
- Point d'entrée — DQL ou GraphQL
- Prérequis — le réseau du port 6080 de Zero fermé ou protégé, surtout en dessous de la v25.4.0 ; Linux en amd64 ou arm64
- Exécution — self-hébergé ; distribué, avec transactions ACID distribuées
- Coût — gratuit, Apache-2.0 ; le coût réel est l'exploitation du cluster

## Limites à connaître

- **Gouvernance en transition.** Dgraph Labs, Hypermode puis Istari Digital : le forum est passé aux discussions GitHub le 2025-12-09, la feuille de route 2026 (sécurité, échelle, distribution) est déclarée, et l'équipe active compte environ six auteurs. Le dépôt n'est ni archivé ni en pause, mais le risque de pérennité est moyen.
- **Licence contradictoire dans la documentation.** Les notes de la v25.0.0 annoncent le retrait de la licence Enterprise ; une page de la documentation dit encore que ces fonctions sont sous la « Dgraph Community License ». Cette page semble datée de la v24, sans preuve directe.
- **Usage réel non recoupé.** Le chiffre des tirages Docker est le seul indicateur d'adoption relevé.

## Écosystème

### Alternatives

- [[Nebula Graph]] — Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée.
- [[ArangoDB]] — Base multi-modèle (documents, graphes, clé-valeur, recherche) interrogée en AQL (C++, BSL 1.1) — cluster complet, mais binaires Community limités à un usage interne sous 100 Go de données, licence commerciale au-delà.
- [[JanusGraph]] — Couche de graphe Java au-dessus de Cassandra, ScyllaDB ou HBase et d'un index Elasticsearch ou Solr (Apache-2.0, Linux Foundation) — Gremlin, milliards de sommets ; trois composants à opérer, et aucune version stable depuis novembre 2024.

## Ressources

- Documentation — https://docs.dgraph.io/
- Dépôt — https://github.com/dgraph-io/dgraph
- Documentation — l'architecture : https://docs.dgraph.io/installation/dgraph-architecture
- Article — l'arrivée d'Istari : https://discuss.dgraph.io/t/dgraph-welcome-to-istari/20021

## Voir aussi

- [[Bases de graphes]] — le hub du sous-domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[Bases graphe — modèles et langages de requête]] — la notion : modèles, langages de requête, et quand un graphe bat un relationnel (DQL, le sharding par prédicat et les jointures distribuées)
