---
role: brique
nom: MySQL Workbench
alias: [mysql workbench, workbench]
pitch: "Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: C++
alternatives: ["[[DBeaver]]", "[[HeidiSQL]]"]
complements: ["[[MySQL]]"]
tags: [db-client, relational]
url_docs: https://dev.mysql.com/doc/workbench/en/
url_repo: https://github.com/mysql/mysql-workbench
---

# MySQL Workbench

<!-- AUTO:BANDEAU:START -->
> Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application C++ | open-source | Windows, macOS, Linux | — |
<!-- AUTO:BANDEAU:END -->

## Définition

L'outil graphique officiel de MySQL, édité par Oracle. Il tient sur trois piliers : la
**conception** — modélisation visuelle du schéma et reverse engineering en diagrammes ER —,
le **développement** avec son éditeur SQL, et l'**administration** du serveur : configuration,
utilisateurs, sauvegarde, suivi des performances. C'est une application native en C++, alignée
sur les versions du serveur qu'elle accompagne.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Projet MySQL : un outil aligné sur le serveur et ses fonctions d'administration | Centré MySQL : peu pertinent dès qu'un autre moteur entre en jeu |
| Modéliser un schéma visuellement en diagrammes ER, puis générer le DDL | Réputée lourde, voire instable, sur certaines plateformes selon les versions |
| Reverse engineering d'une base existante vers un diagramme | |

## Mise en œuvre

- Installation — installeur Windows, macOS ou Linux
- Point d'entrée — application de bureau : diagrammes ER, éditeur SQL, console d'administration
- Prérequis — un serveur MySQL — MariaDB dans une certaine mesure ; application C++ native
- Exécution — sur le poste de travail, aucun service à héberger
- Coût — gratuit, licence GPLv2

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.

### Compléments

- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — le moteur que l'outil administre et modélise

## Ressources

- Documentation — https://dev.mysql.com/doc/workbench/en/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
