---
role: hub
nom: Bases de graphes
alias: [bases graphes, graph databases, bdd graphe, bases de données graphe]
pitch: Stocker des entités et leurs relations, et interroger des chemins de profondeur variable — les moteurs de graphe, leurs langages et ce que leur licence permet.
domaines: [data-eng, ai-eng, data-sci]
tags: [graph-db]
---

# Bases de graphes

> Stocker des entités et leurs relations, et interroger des chemins de profondeur variable — les moteurs de graphe, leurs langages et ce que leur licence permet.

## Ce qu'il faut comprendre

- **Un moteur de graphe ne se distingue pas d'un relationnel par le stockage, mais par la requête.** Un chemin de longueur inconnue — « les contacts de mes contacts, jusqu'à ce que… » — s'écrit en une ligne et se parcourt sans jointure répétée. Quand les relations sont peu profondes, un relationnel bien indexé rivalise, et [[Postgres]] reste le défaut.
- **Trois natures de briques cohabitent ici.** Un moteur **natif** ([[Neo4j]], [[Memgraph]], [[Nebula Graph]]) ; une **extension** d'une base existante ([[Apache AGE]], dans Postgres) ; un moteur **multi-modèle** dont le graphe est l'un des modèles ([[ArangoDB]]).
- **La licence est le premier critère qui départage, avant les performances.** Neo4j Community est libre (GPLv3) mais mono-instance, et Enterprise est commercial ; Memgraph et ArangoDB sont en BSL 1.1, avec un usage interne permis et un plafond de 100 Go sur les binaires d'ArangoDB ; Apache AGE et Nebula Graph sont en Apache-2.0, et la Community de Nebula n'a plus de release depuis mai 2024.
- **Le langage n'est pas le même d'un moteur à l'autre.** Cypher (Neo4j, Memgraph, Apache AGE), nGQL (Nebula Graph), AQL (ArangoDB) : changer de moteur veut dire réécrire les requêtes, même entre deux dialectes voisins.

## Choisir

- Un Postgres déjà en place et un graphe modeste → [[Apache AGE]] : une extension, pas une base de plus.
- Le moteur de référence et l'écosystème le plus riche, sur un nœud → [[Neo4j]] Community ; une haute disponibilité impose l'édition Enterprise, payante.
- Un graphe qui tient en RAM, du temps réel, Cypher et Bolt, en usage interne → [[Memgraph]].
- Des documents, des graphes et de la recherche dans un seul moteur → [[ArangoDB]], licence lue en entier.
- Un graphe qui dépasse un nœud, sans licence restrictive → [[Nebula Graph]], en surveillant sa maintenance. Cf. [[Comparatif - Bases graphes]].

<!-- AUTO:START -->
### Briques
- [[Apache AGE]] — Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de plus à opérer, mais pas de bibliothèque d'algorithmes ni de scale-out propre.
- [[ArangoDB]] — Base multi-modèle (documents, graphes, clé-valeur, recherche) interrogée en AQL (C++, BSL 1.1) — cluster complet, mais binaires Community limités à un usage interne sous 100 Go de données, licence commerciale au-delà.
- [[Memgraph]] — Base de graphes en mémoire, compatible Cypher et Bolt (C++, BSL 1.1) — temps réel et flux Kafka, mono-nœud ; haute disponibilité automatique, RBAC et SSO réservés à l'édition Enterprise.
- [[Nebula Graph]] — Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée.
- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).

### Comparatifs
- [[Comparatif - Bases graphes]]
<!-- AUTO:END -->
