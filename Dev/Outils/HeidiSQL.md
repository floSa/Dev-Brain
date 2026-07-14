---
galaxie: dev
type: outil
nom: HeidiSQL
alias: [heidisql]
pitch: "Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: open-source
os: "Windows (Linux/macOS via Wine)"
langage: Delphi
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]", "[[Dev/Outils/DataGrip|DataGrip]]", "[[Dev/Outils/MySQL Workbench|MySQL Workbench]]"]
tags: [db-client, relational]
url_docs: https://www.heidisql.com/help.php
url_repo: https://github.com/HeidiSQL/HeidiSQL
---

# HeidiSQL

## Pourquoi

Client SQL **léger et rapide** pour Windows, gratuit sous GPL. Historiquement orienté MySQL/MariaDB, il gère aussi PostgreSQL, SQL Server et SQLite. Démarrage instantané, faible empreinte mémoire, édition de données en grille, export de structure et de données — l'outil de prédilection pour un usage Windows sans installer une machine Java.

## Quand l'utiliser

- Poste Windows, besoin d'un client réactif et minimaliste.
- Travail surtout MySQL/MariaDB, avec un peu de Postgres / SQL Server / SQLite.
- Tâches courantes : éditer des données, exporter une base, lancer des requêtes rapides.

## Quand NE PAS l'utiliser

- Couverture de moteurs très large (Oracle, NoSQL…) → [[Dev/Outils/DBeaver|DBeaver]].
- Complétion et refactoring SQL de niveau IDE → [[Dev/Outils/DataGrip|DataGrip]].
- Modélisation et administration MySQL avancées → [[Dev/Outils/MySQL Workbench|MySQL Workbench]].

## Bases & plateformes

- MySQL/MariaDB, PostgreSQL, SQL Server, SQLite.
- Windows natif (Delphi) ; fonctionne sous Linux/macOS via Wine.

## Pièges

- Pas d'application native macOS/Linux (Wine seulement).
- Moins de fonctions visuelles avancées (diagrammes ER) qu'un outil plus lourd.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[Dev/Outils/DataGrip|DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[Dev/Outils/MySQL Workbench|MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://www.heidisql.com/help.php
