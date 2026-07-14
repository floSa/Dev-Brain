---
galaxie: dev
type: outil
nom: MySQL Workbench
alias: [mysql workbench, workbench]
pitch: "Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: C++
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]", "[[Dev/Outils/HeidiSQL|HeidiSQL]]"]
tags: [db-client, relational]
url_docs: https://dev.mysql.com/doc/workbench/en/
url_repo: https://github.com/mysql/mysql-workbench
---

# MySQL Workbench

## Pourquoi

L'outil graphique **officiel** de MySQL, édité par Oracle, sous GPLv2. Trois piliers : **conception** (modélisation visuelle de schéma et reverse engineering en diagrammes ER), **développement** (éditeur SQL) et **administration** (configuration du serveur, utilisateurs, sauvegarde, suivi des performances). La référence quand le projet est centré MySQL.

## Quand l'utiliser

- Projet MySQL : profiter d'un outil aligné sur le serveur et ses fonctions d'admin.
- Modéliser un schéma visuellement (diagrammes ER) puis générer le DDL.
- Reverse engineering d'une base existante en diagramme.

## Quand NE PAS l'utiliser

- Travailler sur plusieurs SGBD → [[Dev/Outils/DBeaver|DBeaver]].
- Client Windows ultra-léger pour des tâches rapides → [[Dev/Outils/HeidiSQL|HeidiSQL]].

## Bases & plateformes

- MySQL (et MariaDB dans une certaine mesure).
- Windows, macOS, Linux (application C++ native).

## Pièges

- Centré MySQL : peu pertinent pour d'autres moteurs.
- Application parfois réputée lourde ou instable sur certaines plateformes selon les versions.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[Dev/Outils/HeidiSQL|HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Dev/Services/MySQL|MySQL]] — le moteur administré
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://dev.mysql.com/doc/workbench/en/
