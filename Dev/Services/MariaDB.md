---
galaxie: dev
type: service
nom: MariaDB
alias: [mariadb]
pitch: "Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle."
categorie: database/relational
licence_type: open-source
hosted: both
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[Dev/Services/MySQL|MySQL]]", "[[Dev/Services/Postgres|Postgres]]", "[[Dev/Services/SQLite|SQLite]]", "[[Dev/Services/CockroachDB|CockroachDB]]", "[[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]]"]
remplace_par: []
status: actif
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

- Compatibilité stricte avec les dernières fonctions MySQL d'Oracle → [[Dev/Services/MySQL|MySQL]].
- Types riches et extensions avancées → [[Dev/Services/Postgres|Postgres]].
- Scale horizontal distribué multi-région natif → [[Dev/Services/CockroachDB|CockroachDB]].

## Déploiement & coût

- Self-host (Docker, paquet) ou managé (SkySQL, Azure Database for MariaDB, déclinaisons cloud).
- Scaling vertical + réplicas ; clustering synchrone via Galera.
- Gratuit (GPL) ; offres entreprise/support via MariaDB plc.

## Pièges

- Divergence croissante avec MySQL : compatibilité forte mais plus totale (fonctions, JSON, réplication).
- Choisir le bon moteur de stockage selon l'usage (InnoDB transactionnel vs Aria vs ColumnStore).
- Vérifier la parité de version quand un outil cible une version MySQL précise.
- Retours d'expérience détaillés : `Dev/REX/REX - MariaDB.md`.

## Alternatives

- [[Dev/Services/MySQL|MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Dev/Services/Postgres|Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/CockroachDB|CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- `Dev/REX/REX - MariaDB.md` — retours d'expérience
- Doc : https://mariadb.com/kb/en/documentation/
