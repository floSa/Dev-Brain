---
role: brique
nom: HeidiSQL
alias: [heidisql]
pitch: "Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: open-source
os: "Windows (Linux/macOS via Wine)"
langage: Delphi
alternatives: ["[[DBeaver]]", "[[DataGrip]]", "[[MySQL Workbench]]"]
complements: []
tags: [db-client, relational]
url_docs: https://www.heidisql.com/help.php
url_repo: https://github.com/HeidiSQL/HeidiSQL
---

# HeidiSQL

<!-- AUTO:BANDEAU:START -->
> Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Delphi | open-source | Windows (Linux/macOS via Wine) | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Client SQL léger pour Windows, historiquement orienté MySQL et MariaDB, qui gère aussi
PostgreSQL, SQL Server et SQLite. Démarrage instantané, faible empreinte mémoire, édition des
données en grille, export de structure et de données. Écrit en Delphi, il n'a besoin d'aucune
machine virtuelle : c'est ce qui explique à la fois sa réactivité et son ancrage Windows.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Poste Windows, besoin d'un client réactif et minimaliste | Moins de fonctions visuelles avancées, les diagrammes ER en particulier, qu'un outil plus lourd |
| Travail surtout MySQL/MariaDB, avec un peu de Postgres, SQL Server ou SQLite | |
| Tâches courantes : éditer des données, exporter une base, lancer des requêtes rapides | |

## Mise en œuvre

- Installation — installeur Windows
- Point d'entrée — application de bureau : grille d'édition des données, export de structure et de données
- Prérequis — Windows natif ; Linux et macOS seulement via Wine
- Exécution — sur le poste de travail, aucun service à héberger
- Coût — gratuit, licence GPL

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.

## Ressources

- Documentation — https://www.heidisql.com/help.php

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
