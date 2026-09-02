---
role: hub
nom: Administration
pitch: Clients graphiques pour explorer, requêter et administrer un serveur de base de données.
domaines: [data-eng]
---

# Administration

> Clients graphiques pour explorer, requêter et administrer un serveur de base de données.

## Ce qu'il faut comprendre

- Ce sont des **applications de poste**, pas des briques à déployer : elles n'entrent pas dans une architecture, elles s'installent sur la machine de qui exploite la base.
- Le partage se fait sur une seule question : **un outil universel ou l'outil officiel du moteur ?** L'universel évite d'apprendre sept interfaces ; l'officiel expose les fonctions propres au moteur que l'universel ne montre pas.
- Aucun de ces clients ne remplace les migrations de schéma versionnées ([[Alembic]], [[Flyway]], [[Liquibase]], au niveau du domaine) : cliquer une modification de schéma ne la rejoue pas en production.

## Choisir

- Plusieurs moteurs à couvrir avec un seul outil, gratuitement → [[DBeaver]].
- Complétion SQL et refactoring de niveau IDE, licence JetBrains acceptée → [[DataGrip]].
- Windows, léger et rapide, MySQL/MariaDB en tête → [[HeidiSQL]].
- L'outil officiel du moteur : [[pgAdmin]] (Postgres), [[MySQL Workbench]] (MySQL), [[MongoDB Compass]] (Mongo), [[Redis Insight]] (Redis).

<!-- AUTO:START -->
### Briques
- [[DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- [[MongoDB Compass]] — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- [[MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- [[pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- [[Redis Insight]] — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).

### Comparatifs
- [[Comparatif - Clients de bases de données]]
<!-- AUTO:END -->
