---
galaxie: dev
type: outil
nom: DBeaver
alias: [dbeaver]
pitch: "Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: open-core
os: "Windows, macOS, Linux"
langage: Java
status: actif
alternatives: ["[[Dev/Outils/DataGrip|DataGrip]]", "[[Dev/Outils/HeidiSQL|HeidiSQL]]", "[[Dev/Outils/pgAdmin|pgAdmin]]", "[[Dev/Outils/MySQL Workbench|MySQL Workbench]]", "[[Dev/Outils/MongoDB Compass|MongoDB Compass]]", "[[Dev/Outils/Redis Insight|Redis Insight]]"]
tags: [db-client, relational, nosql]
url_docs: https://dbeaver.com/docs/dbeaver/
url_repo: https://github.com/dbeaver/dbeaver
---

# DBeaver

## Pourquoi

Client de base de données **universel** : un même outil pour la majorité des SGBD (Postgres, MySQL/MariaDB, Oracle, SQL Server, SQLite) et, en édition payante, les bases NoSQL (Mongo, Cassandra, Redis). Éditeur SQL avec complétion, navigateur de schéma, éditeur de données en grille, diagrammes ER. L'Edition Community est gratuite sous Apache 2.0.

## Quand l'utiliser

- Travailler sur plusieurs SGBD différents sans changer d'outil.
- Besoin d'un client gratuit, multiplateforme, riche (export/import, diagrammes ER, génération de DDL).
- Exploration ad hoc et requêtage SQL au quotidien.

## Quand NE PAS l'utiliser

- Complétion SQL et refactoring de niveau IDE → [[Dev/Outils/DataGrip|DataGrip]].
- Un seul moteur, console officielle pleinement intégrée → [[Dev/Outils/pgAdmin|pgAdmin]] (Postgres), [[Dev/Outils/MySQL Workbench|MySQL Workbench]] (MySQL).
- Très léger et rapide sous Windows uniquement → [[Dev/Outils/HeidiSQL|HeidiSQL]].

## Bases & plateformes

- Community (Apache 2.0) : bases relationnelles. Enterprise/Ultimate (commercial) : NoSQL, BDD cloud — modèle **open-core**.
- Windows, macOS, Linux (application Java/Eclipse RCP).

## Pièges

- L'application Java peut être gourmande en mémoire sur de gros jeux de résultats.
- Le support NoSQL (Mongo, Redis…) est réservé aux éditions payantes.

## Alternatives

- [[Dev/Outils/DataGrip|DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[Dev/Outils/HeidiSQL|HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- [[Dev/Outils/pgAdmin|pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- [[Dev/Outils/MySQL Workbench|MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- [[Dev/Outils/MongoDB Compass|MongoDB Compass]] — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- [[Dev/Outils/Redis Insight|Redis Insight]] — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://dbeaver.com/docs/dbeaver/
