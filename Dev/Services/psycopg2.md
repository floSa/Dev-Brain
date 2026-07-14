---
galaxie: dev
type: service
nom: psycopg2
alias: [psycopg2, psycopg]
pitch: "Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3."
categorie: database/driver
licence_type: open-source
hosted: self
maturite: production
langage: C/Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [postgres, relational, db-driver]
url_docs: https://www.psycopg.org/docs/
url_repo: https://github.com/psycopg/psycopg2
---

# psycopg2

## Pourquoi

Le **driver PostgreSQL** le plus répandu pour Python. Il implémente la spécification **DB-API 2.0** et est écrit majoritairement en **C** comme wrapper de **libpq** — d'où son efficacité et sa sûreté. Thread-safe, il offre curseurs côté client et serveur, communication asynchrone et notifications, support de `COPY TO/FROM`. C'est la couche bas niveau sous de nombreux ORM (dont [[Dev/Services/SQLAlchemy|SQLAlchemy]], qui l'utilise comme dialecte Postgres par défaut). **Ce n'est pas un ORM** : aucun mapping objet, on écrit le SQL. Toujours largement utilisé et maintenu, mais **figé en fonctionnalités** : les nouveautés vont à **psycopg 3** (paquet `psycopg`).

## Quand l'utiliser

- Accès **SQL direct** à [[Dev/Services/Postgres|Postgres]] sans couche ORM (scripts, micro-services, contrôle fin et performance).
- **Driver sous-jacent** d'un ORM/toolkit ([[Dev/Services/SQLAlchemy|SQLAlchemy]]) ou d'un framework existant.
- Codebase **déjà sur psycopg2**, sans besoin d'async.

## Quand NE PAS l'utiliser

- **Nouveau projet** → préférer **psycopg 3** (`psycopg`) : async natif, meilleure gestion des types, pipeline mode.
- Besoin d'**async hautes performances** → psycopg 3 ou **asyncpg**.
- Vouloir un **mapping objet** et des **migrations** → [[Dev/Services/SQLAlchemy|SQLAlchemy]] + [[Dev/Services/Alembic|Alembic]].

## Déploiement & coût

- Bibliothèque Python (**LGPL**), gratuite, embarquée dans l'application : `single-node`, suit le déploiement de l'app. Requiert un PostgreSQL accessible.
- Distribution : `psycopg2` (compilation, nécessite libpq + toolchain) ou `psycopg2-binary` (wheels précompilés, pratique en dev).

## Pièges

- **`psycopg2-binary` en production** : les mainteneurs recommandent de compiler `psycopg2` contre la libpq du système — le paquet binaire embarque ses propres libs (SSL, locale), source de conflits.
- **Feature-frozen** : ne pas en attendre de nouveautés ; pour du neuf → psycopg 3.
- **Driver synchrone** : inadapté à l'async (utiliser psycopg 3 ou asyncpg).

## Alternatives

- _Successeur direct **psycopg 3** (`psycopg`) et alternative async **asyncpg** — pas encore fichés dans le brain._ [[Dev/Services/SQLAlchemy|SQLAlchemy]] n'est pas une alternative : il s'appuie sur psycopg2, il ne le remplace pas.

## Liens

- [[Dev/Services/Postgres|Postgres]] — la base pilotée.
- [[Dev/Services/SQLAlchemy|SQLAlchemy]] — ORM/toolkit qui utilise psycopg2 comme driver Postgres.
- Doc : https://www.psycopg.org/docs/
