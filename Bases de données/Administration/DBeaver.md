---
role: brique
nom: DBeaver
alias: [dbeaver]
pitch: "Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: open-core
os: "Windows, macOS, Linux"
langage: Java
alternatives: ["[[DataGrip]]", "[[HeidiSQL]]", "[[pgAdmin]]", "[[MySQL Workbench]]", "[[MongoDB Compass]]", "[[Redis Insight]]"]
complements: []
tags: [db-client, relational, nosql]
url_docs: https://dbeaver.com/docs/dbeaver/
url_repo: https://github.com/dbeaver/dbeaver
---

# DBeaver

<!-- AUTO:BANDEAU:START -->
> Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Java | open-core | Windows, macOS, Linux | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Client de base de données universel : un même outil parle à la majorité des SGBD —
Postgres, MySQL et MariaDB, Oracle, SQL Server, SQLite — et, dans les éditions payantes, aux
bases NoSQL comme Mongo, Cassandra ou Redis. Il apporte un éditeur SQL à complétion, un
navigateur de schéma, un éditeur de données en grille et des diagrammes ER. C'est une
application de bureau bâtie sur Eclipse RCP, pas un service : elle s'installe sur le poste,
et le seul état qu'elle garde est celui de ses connexions.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Travailler sur plusieurs SGBD différents sans changer d'outil | L'application Java devient gourmande en mémoire sur de gros jeux de résultats |
| Besoin d'un client gratuit et multiplateforme, riche en fonctions (export/import, diagrammes ER, génération de DDL) | |
| Exploration ad hoc et requêtage SQL au quotidien | |

## Mise en œuvre

- Installation — installeur ou archive pour Windows, macOS et Linux
- Point d'entrée — application de bureau : éditeur SQL, navigateur de schéma, grille de données, diagrammes ER
- Prérequis — Windows, macOS ou Linux ; c'est une application Java bâtie sur Eclipse RCP
- Exécution — sur le poste de travail, aucun service à héberger
- Coût — Community gratuite sous Apache 2.0 ; Enterprise et Ultimate sont commerciales, et seules elles ouvrent le NoSQL et les bases cloud — c'est le modèle open-core

## Écosystème

### Alternatives

- [[DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- [[pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- [[MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- [[MongoDB Compass]] — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- [[Redis Insight]] — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).

## Ressources

- Documentation — https://dbeaver.com/docs/dbeaver/
- Dépôt — https://github.com/dbeaver/dbeaver

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
