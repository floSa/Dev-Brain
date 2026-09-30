---
role: brique
nom: Apache AGE
alias: [AGE, apache age, AGE PostgreSQL, A Graph Extension]
pitch: "Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de plus à opérer, mais pas de bibliothèque d'algorithmes ni de scale-out propre."
categorie: database/graphe
famille: extension
licence_type: open-source
maturite: production
langage: C
alternatives: ["[[Neo4j]]", "[[Memgraph]]"]
complements: ["[[Postgres]]"]
tags: [graph-db, postgres]
url_docs: https://age.apache.org/age-manual/master/index.html
url_repo: https://github.com/apache/age
---

# Apache AGE

<!-- AUTO:BANDEAU:START -->
> Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de plus à opérer, mais pas de bibliothèque d'algorithmes ni de scale-out propre.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension C | open-source | dans le moteur hôte, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Extension de PostgreSQL qui ajoute un **graphe de propriétés** à une base existante. Chaque
label devient une table Postgres, les propriétés vivent dans un type `agtype` proche de
JSONB, et une requête **openCypher** s'écrit *dans* le SQL, par la fonction `cypher()` :
`SELECT * FROM cypher('g', $$ MATCH … $$) AS (n agtype)`. Le résultat se joint donc aux
tables relationnelles, dans la même transaction et la même sauvegarde. Aucun index n'est créé
d'office : des btree sur `id`, `start_id`, `end_id` et un GIN sur `properties` se posent à la
main. Relevé le 2026-09-30 : le site annonce la **1.7.0** pour PostgreSQL 18 et la 1.6.0 pour
les versions 14 à 17 ; une 1.8.0 est en release candidate (2026-09-19, marquée « pending PMC
approval ») ; environ 4 860 étoiles. Projet de premier niveau de l'Apache Software Foundation
depuis juin 2022, après deux ans d'incubation.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Postgres est déjà en place et le besoin de graphe est modeste : un seul moteur, une seule sauvegarde, des transactions communes | Des parcours profonds sont critiques : les notes de la 1.8 corrigent encore des erreurs dans les parcours à longueur variable, à mesurer avant de s'engager |
| Mélanger relationnel, graphe et vecteurs dans une requête, pour un GraphRAG sans second moteur (avec [[pgvector]]) | Des algorithmes de graphe prêts à l'emploi (centralité, communautés) : la documentation lue n'en propose pas, hors le plus court chemin ajouté en 1.8 |
| Une licence Apache-2.0 sans édition payante, portée par une fondation | Un graphe très volumineux : le passage à l'échelle est celui de Postgres (partitionnement, réplicas), sans sharding propre au graphe |
| Azure Database for PostgreSQL, qui propose l'extension | Une montée de version de Postgres sans délai : une branche d'AGE existe par version majeure, et elle sort après celle de Postgres |
| | Un service managé hors Azure : aucun autre n'a été trouvé (une demande chez DigitalOcean est ouverte depuis 2022) |
| | Un simple modèle tabulaire, sans relations profondes → [[Postgres]] seul |

## Mise en œuvre

- Installation — l'extension se compile ou s'installe pour la version majeure de Postgres utilisée, puis se charge (`shared_preload_libraries`) et se crée dans la base
- Point d'entrée — SQL, avec `cypher('nom_du_graphe', $$ … $$)` ; le résultat se déclare en colonnes `agtype`
- Prérequis — les index sur les tables de labels, à créer à la main ; `MATCH (n {k: v})` et `WHERE n.k = v` ne se planifient pas de la même façon
- Exécution — dans le processus Postgres ; le scaling est celui de Postgres
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Couverture d'openCypher et performances de parcours profond : non établies à la source.** Les documents lus ne chiffrent ni l'un ni l'autre ; aucun comparatif indépendant n'a été trouvé. Le point de départ honnête est une mesure sur ses propres données.
- **Parrain historique fragile.** Bitnine, la société d'origine, est devenue SKAI Worldwide (KOSDAQ) et affiche des pertes, d'après des extraits de recherche non recoupés à la source. Les auteurs des commits des trois derniers mois sont variés, ce qui limite le risque.
- **Contradiction de documentation.** Le dépôt annonce PostgreSQL 11 à 18 ; la FAQ du site dit « jusqu'à 16 » et semble périmée.

## Écosystème

### Alternatives

- [[Neo4j]] — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).
- [[Memgraph]] — Base de graphes en mémoire, compatible Cypher et Bolt (C++, BSL 1.1) — temps réel et flux Kafka, mono-nœud ; haute disponibilité automatique, RBAC et SSO réservés à l'édition Enterprise.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — le moteur hôte, sans lequel l'extension n'existe pas.

## Ressources

- Documentation — https://age.apache.org/age-manual/master/index.html
- Dépôt — https://github.com/apache/age
- Documentation — la disponibilité sur Azure : https://learn.microsoft.com/en-us/azure/postgresql/azure-ai/generative-ai-age-overview
- Documentation — les index et les performances : https://learn.microsoft.com/en-us/azure/postgresql/azure-ai/generative-ai-age-performance

## Voir aussi

- [[Bases de graphes]] — le hub du sous-domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[Bases graphe — modèles et langages de requête]] — la notion : modèles, langages de requête, et quand un graphe bat un relationnel (openCypher dans SQL, SQL/PGQ et le retrait de PostgreSQL 19)
- [[pgvector]] — la recherche vectorielle dans la même base, pour coupler graphe et similarité
