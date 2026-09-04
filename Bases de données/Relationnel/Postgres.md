---
role: brique
nom: Postgres
alias: [postgres, postgresql, pg]
pitch: "SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne."
categorie: database/relationnel
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[MySQL]]", "[[MariaDB]]", "[[SQLite]]", "[[CockroachDB]]", "[[Microsoft SQL Server]]"]
complements: ["[[pgvector]]", "[[pgAdmin]]"]
tags: [relational, postgres]
url_docs: https://www.postgresql.org/docs/
url_repo: https://github.com/postgres/postgres
---

# Postgres

<!-- AUTO:BANDEAU:START -->
> SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD relationnel-objet conforme SQL, bâti sur MVCC : les lecteurs ne bloquent pas les
écrivains, et les transactions ACID tiennent sous charge. Sa particularité est
l'**extensibilité** — types personnalisés, fonctions, langages procéduraux, et des extensions
qui ajoutent un domaine entier au même moteur : PostGIS pour le géospatial, pgvector pour le
vectoriel, TimescaleDB pour les séries. Le type `JSONB` absorbe le semi-structuré sans quitter
le relationnel. C'est le défaut raisonnable pour une base applicative.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Base applicative transactionnelle (OLTP) généraliste | VACUUM et bloat à surveiller sous forte charge d'`UPDATE` / `DELETE` |
| Types riches, `JSONB`, requêtes complexes ou contraintes d'intégrité fortes | Connexions coûteuses : au-delà de quelques centaines, un pooler (PgBouncer) devient obligatoire |
| Tirer parti des extensions : PostGIS, pgvector, TimescaleDB, toutes dans le même moteur | Paramètres par défaut conservateurs (`work_mem`, `shared_buffers`) : sans tuning, les performances restent en deçà |
| Cohérence transactionnelle stricte sur un nœud, avec réplicas en lecture | |

## Mise en œuvre

- Installation — paquet système ou image Docker officielle ; managé partout (RDS, Cloud SQL, Supabase, Neon)
- Point d'entrée — serveur SQL sur le port 5432 ; client `psql`, pilotes standard ([[psycopg2]], [[SQLAlchemy]])
- Prérequis — un serveur à administrer ; les extensions s'installent une par une, par `CREATE EXTENSION`
- Exécution — un primaire plus des réplicas de lecture ; scaling vertical, sharding par l'extension Citus si nécessaire
- Coût — gratuit, licence PostgreSQL permissive ; la dépense est celle du serveur et de son exploitation

## Écosystème

### Alternatives

- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

### Compléments

- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place. — la recherche vectorielle dans la base métier, sans second moteur
- [[pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur. — l'administration et la supervision graphiques du serveur

## Ressources

- Documentation — https://www.postgresql.org/docs/
- Dépôt — https://github.com/postgres/postgres

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
