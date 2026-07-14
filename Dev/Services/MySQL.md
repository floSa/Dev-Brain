---
galaxie: dev
type: service
nom: MySQL
alias: [mysql]
pitch: "SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web."
categorie: database/relational
licence_type: open-source
hosted: both
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[Dev/Services/Postgres|Postgres]]", "[[Dev/Services/MariaDB|MariaDB]]", "[[Dev/Services/SQLite|SQLite]]", "[[Dev/Services/CockroachDB|CockroachDB]]", "[[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]]"]
remplace_par: []
status: actif
tags: [relational]
url_docs: https://dev.mysql.com/doc/
url_repo: https://github.com/mysql/mysql-server
---

# MySQL

## Pourquoi

SGBD relationnel le plus déployé du web, pilier historique de la stack LAMP. Simple à prendre en main, écosystème et hébergement managé omniprésents, moteur InnoDB transactionnel (ACID) éprouvé. Détenu par Oracle, avec une édition Community open-source (GPL) et une édition Enterprise commerciale.

## Quand l'utiliser

- Application web classique, CMS (WordPress…), besoin relationnel standard.
- Recherche du plus large écosystème d'hébergement et de tutoriels.
- Charge lecture intensive avec réplicas ; schéma relationnel simple et stable.
- Compatibilité avec un existant ou un hébergeur qui impose MySQL.

## Quand NE PAS l'utiliser

- Types riches, extensions, requêtes avancées → [[Dev/Services/Postgres|Postgres]].
- Volonté d'un fork 100 % open-source, sans Oracle → [[Dev/Services/MariaDB|MariaDB]].
- Scale horizontal des écritures multi-région → [[Dev/Services/CockroachDB|CockroachDB]].

## Déploiement & coût

- Self-host (Docker, paquet) ou managé partout (RDS, Cloud SQL, Aurora MySQL…).
- Scaling vertical + réplicas lecture ; sharding applicatif ou via Vitess pour l'échelle.
- Édition Community gratuite (GPL) ; Enterprise payante (support, outillage).

## Pièges

- Défauts historiques laxistes (modes SQL, encodage) : forcer `utf8mb4` et un `sql_mode` strict.
- Divergences fonctionnelles avec [[Dev/Services/MariaDB|MariaDB]] : compatibilité non garantie à 100 %.
- Gouvernance Oracle : certaines fonctionnalités réservées à l'édition Enterprise.
- Retours d'expérience détaillés : `Dev/REX/REX - MySQL.md`.

## Alternatives

- [[Dev/Services/Postgres|Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[Dev/Services/MariaDB|MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/CockroachDB|CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- `Dev/REX/REX - MySQL.md` — retours d'expérience
- Doc : https://dev.mysql.com/doc/
