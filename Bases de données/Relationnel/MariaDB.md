---
role: brique
nom: MariaDB
alias: [mariadb]
pitch: "Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle."
categorie: database/relationnel
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[MySQL]]", "[[Postgres]]", "[[SQLite]]", "[[CockroachDB]]", "[[Microsoft SQL Server]]"]
complements: []
tags: [relational]
url_docs: https://mariadb.com/kb/en/documentation/
url_repo: https://github.com/MariaDB/server
---

# MariaDB

<!-- AUTO:BANDEAU:START -->
> Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C/C++ | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Fork de MySQL créé par ses auteurs d'origine après le rachat par Oracle, piloté depuis par la
MariaDB Foundation. Il reste largement compatible — même protocole filaire, même dialecte, mêmes
clients — et ajoute ses propres moteurs de stockage (Aria, le moteur colonne ColumnStore) ainsi
que le clustering synchrone Galera. Dans la plupart des cas, il remplace MySQL sans que
l'application s'en aperçoive ; c'est d'ailleurs le paquet `mysql` par défaut de plusieurs
distributions Linux.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Besoin MySQL avec une gouvernance indépendante d'Oracle | Divergence croissante avec MySQL : compatibilité forte, mais plus totale (fonctions, JSON, réplication) |
| Migration depuis MySQL en conservant outils et dialecte familiers | Un outil qui cible une version MySQL précise oblige à vérifier la parité de version |
| Fonctions propres utiles : moteur colonne ColumnStore, clustering synchrone Galera | Le moteur de stockage est un choix structurant (InnoDB transactionnel, Aria, ColumnStore) — le défaut ne convient pas partout |
| Distributions Linux où MariaDB est devenu le paquet `mysql` par défaut | |

## Mise en œuvre

- Installation — paquet système ou image Docker ; managé (SkySQL, déclinaisons cloud)
- Point d'entrée — serveur SQL sur le port 3306, protocole et dialecte MySQL ; les clients et pilotes MySQL fonctionnent tels quels
- Prérequis — un serveur à administrer ; le moteur de stockage se choisit à la création du schéma
- Exécution — un primaire plus des réplicas ; clustering synchrone multi-maître via Galera
- Coût — gratuit sous GPL ; offres de support entreprise via MariaDB plc

## Écosystème

### Alternatives

- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Ressources

- Documentation — https://mariadb.com/kb/en/documentation/
- Dépôt — https://github.com/MariaDB/server

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
