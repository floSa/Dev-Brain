---
galaxie: dev
type: service
nom: Postgres
alias: [postgres, postgresql, pg]
pitch: "SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne."
categorie: database/relational
licence_type: open-source
hosted: both
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Dev/Services/MySQL|MySQL]]", "[[Dev/Services/MariaDB|MariaDB]]", "[[Dev/Services/SQLite|SQLite]]", "[[Dev/Services/CockroachDB|CockroachDB]]", "[[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]]"]
remplace_par: []
status: actif
tags: [relational, postgres]
url_docs: https://www.postgresql.org/docs/
url_repo: https://github.com/postgres/postgres
---

# Postgres

## Pourquoi

SGBD relationnel-objet conforme SQL, réputé pour sa robustesse et son **extensibilité** : types personnalisés, fonctions, et un écosystème d'extensions (PostGIS pour le géospatial, pgvector pour le vectoriel, TimescaleDB pour les séries). Transactions ACID solides via MVCC, et `JSONB` pour le semi-structuré. Le défaut raisonnable pour une base applicative.

## Quand l'utiliser

- Base applicative transactionnelle (OLTP) généraliste.
- Besoin de types riches, de `JSONB`, de requêtes complexes ou de contraintes d'intégrité fortes.
- Tirer parti des extensions : géospatial (PostGIS), vectoriel ([[Dev/Services/pgvector|pgvector]]), séries (TimescaleDB).
- Cohérence transactionnelle stricte sur un nœud, avec réplicas en lecture.

## Quand NE PAS l'utiliser

- Base embarquée dans l'application, sans serveur → [[Dev/Services/SQLite|SQLite]].
- Scale horizontal des écritures, multi-région natif → [[Dev/Services/CockroachDB|CockroachDB]].
- Stack 100 % Microsoft / .NET imposée → [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]].

## Déploiement & coût

- Self-host : Docker ou paquet système ; managé partout (RDS, Cloud SQL, Supabase, Neon…).
- Scaling vertical + réplicas en lecture ; sharding via l'extension Citus si nécessaire.
- Gratuit (licence PostgreSQL, permissive).

## Pièges

- VACUUM et bloat à surveiller sous forte charge d'`UPDATE`/`DELETE`.
- Connexions coûteuses : passer un pooler (PgBouncer) au-delà de quelques centaines.
- Paramètres par défaut conservateurs (`work_mem`, `shared_buffers`) — tuning souvent nécessaire.
- Retours d'expérience détaillés : `Dev/REX/REX - Postgres.md`.

## Alternatives

- [[Dev/Services/MySQL|MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Dev/Services/MariaDB|MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/CockroachDB|CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- `Dev/REX/REX - Postgres.md` — retours d'expérience
- Doc : https://www.postgresql.org/docs/
