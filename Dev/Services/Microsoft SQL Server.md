---
galaxie: dev
type: service
nom: Microsoft SQL Server
alias: [sql server, mssql, sqlserver, ms sql]
pitch: "SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche."
categorie: database/relational
licence_type: proprietary
hosted: both
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/Postgres|Postgres]]", "[[Dev/Services/MySQL|MySQL]]", "[[Dev/Services/MariaDB|MariaDB]]", "[[Dev/Services/SQLite|SQLite]]", "[[Dev/Services/CockroachDB|CockroachDB]]"]
remplace_par: []
status: actif
tags: [relational]
url_docs: https://learn.microsoft.com/en-us/sql/sql-server/
url_repo: 
---

# Microsoft SQL Server

## Pourquoi

SGBD relationnel d'entreprise de Microsoft. Intégration profonde avec l'écosystème **.NET / Windows / Azure**, dialecte **T-SQL** riche, et outillage mûr (SSMS, SSIS pour l'ETL, SSAS pour l'OLAP, SSRS pour le reporting). Fonctions haut de gamme : Always On, colonnes chiffrées, columnstore. Produit propriétaire, avec une édition Express gratuite et Linux/conteneurs supportés depuis 2017.

## Quand l'utiliser

- Environnement Microsoft établi (.NET, Active Directory, Azure).
- Besoin de l'outillage BI/ETL intégré (SSIS/SSAS/SSRS) et de T-SQL.
- Exigences entreprise : support éditeur, sécurité avancée, conformité.
- Migration ou consolidation sur Azure SQL Database / Managed Instance.

## Quand NE PAS l'utiliser

- Préférence open-source, sans coût de licence → [[Dev/Services/Postgres|Postgres]] ou [[Dev/Services/MariaDB|MariaDB]].
- Application embarquée locale → [[Dev/Services/SQLite|SQLite]].
- Scale horizontal distribué multi-région natif → [[Dev/Services/CockroachDB|CockroachDB]].

## Déploiement & coût

- Self-host (Windows, Linux, conteneurs) ou managé (Azure SQL Database, Managed Instance).
- Scaling vertical + réplicas de lecture ; haute dispo via Always On Availability Groups.
- **Propriétaire** : licences par cœur souvent coûteuses ; édition Express gratuite (limites de taille/CPU) ; Developer gratuite hors production.

## Pièges

- Coût de licence qui grimpe vite (modèle par cœur) — vérifier l'édition et les fonctionnalités incluses.
- Verrouillage T-SQL : SQL non portable vers d'autres moteurs sans réécriture.
- Limites strictes de l'édition Express (taille de base, RAM, CPU) à anticiper.
- Retours d'expérience détaillés : `Dev/REX/REX - Microsoft SQL Server.md`.

## Alternatives

- [[Dev/Services/Postgres|Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[Dev/Services/MySQL|MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Dev/Services/MariaDB|MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/CockroachDB|CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- `Dev/REX/REX - Microsoft SQL Server.md` — retours d'expérience
- Doc : https://learn.microsoft.com/en-us/sql/sql-server/
