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

## Pourquoi

Fork de MySQL créé par ses auteurs d'origine après le rachat par Oracle, avec une **gouvernance communautaire** (MariaDB Foundation) et une licence 100 % open-source (GPL). Largement compatible avec MySQL (protocole, dialecte) tout en ajoutant ses propres moteurs (Aria, ColumnStore) et fonctionnalités. Souvent un remplacement transparent de MySQL.

## Quand l'utiliser

- Besoin MySQL avec garantie open-source et indépendance vis-à-vis d'Oracle.
- Migration depuis MySQL en conservant les outils et le dialecte familiers.
- Fonctions propres utiles : moteur colonne (ColumnStore), clustering Galera.
- Distributions Linux où MariaDB est devenu le paquet `mysql` par défaut.

## Quand NE PAS l'utiliser

- Compatibilité stricte avec les dernières fonctions MySQL d'Oracle → [[MySQL]].
- Types riches et extensions avancées → [[Postgres]].
- Scale horizontal distribué multi-région natif → [[CockroachDB]].

## Déploiement & coût

- Self-host (Docker, paquet) ou managé (SkySQL, Azure Database for MariaDB, déclinaisons cloud).
- Scaling vertical + réplicas ; clustering synchrone via Galera.
- Gratuit (GPL) ; offres entreprise/support via MariaDB plc.

## Pièges

- Divergence croissante avec MySQL : compatibilité forte mais plus totale (fonctions, JSON, réplication).
- Choisir le bon moteur de stockage selon l'usage (InnoDB transactionnel vs Aria vs ColumnStore).
- Vérifier la parité de version quand un outil cible une version MySQL précise.

## Alternatives

- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- Doc : https://mariadb.com/kb/en/documentation/
