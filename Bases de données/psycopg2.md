---
role: brique
nom: psycopg2
alias: [psycopg2, psycopg]
pitch: "Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3."
categorie: database/driver
famille: paquet
licence_type: open-source
maturite: production
langage: C/Python
alternatives: []
complements: ["[[Postgres]]", "[[SQLAlchemy]]"]
tags: [postgres, relational, db-driver]
url_docs: https://www.psycopg.org/docs/
url_repo: https://github.com/psycopg/psycopg2
---

# psycopg2

<!-- AUTO:BANDEAU:START -->
> Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C/Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-04-21 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le **driver PostgreSQL** le plus répandu pour Python. Il implémente la spécification **DB-API
2.0** et est écrit majoritairement en **C**, comme un wrapper de **libpq** — d'où son
efficacité et sa sûreté. Thread-safe, il offre curseurs côté client et côté serveur,
communication asynchrone, notifications et `COPY TO/FROM`. C'est la couche bas niveau sous de
nombreux ORM. Ce n'est **pas** un ORM : aucun mapping objet, aucune migration, on écrit le
SQL. Il reste largement utilisé et maintenu, mais **figé en fonctionnalités** — les
nouveautés vont à psycopg 3, le paquet `psycopg`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Accès **SQL direct** à PostgreSQL sans couche ORM : scripts, micro-services, contrôle fin et performance | Nouveau projet : psycopg 3 apporte l'async natif, une meilleure gestion des types et le mode pipeline, que psycopg2 n'aura pas |
| Driver sous-jacent d'un ORM, d'un toolkit ou d'un framework existant | Driver **synchrone** : inadapté à une application async à hautes performances |
| Codebase déjà sur psycopg2, sans besoin d'async | `psycopg2-binary` en production : les mainteneurs recommandent de compiler `psycopg2` contre la libpq du système, le paquet binaire embarquant ses propres bibliothèques (SSL, locale), source de conflits |
| | Vouloir un **mapping objet** et des **migrations** → [[SQLAlchemy]] et [[Alembic]] |

## Mise en œuvre

- Installation — `uv add psycopg2` (compilation, libpq et chaîne d'outils requises) ou `psycopg2-binary` (wheels précompilés, pratique en dev)
- Point d'entrée — l'API DB-API 2.0 : connexion, curseurs côté client ou serveur, `COPY TO/FROM`
- Prérequis — un PostgreSQL accessible ; libpq et un compilateur pour la variante compilée
- Exécution — dans le process de l'application, single-node ; rien à héberger
- Coût — gratuit, licence LGPL

## Écosystème

### Alternatives

- _Successeur direct **psycopg 3** (`psycopg`) et alternative async **asyncpg** — pas encore fichés dans le brain._

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — la base pilotée.
- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0. — l'ORM qui s'appuie dessus comme dialecte Postgres par défaut ; il ne le remplace pas.

## Ressources

- Documentation — https://www.psycopg.org/docs/
- Dépôt — https://github.com/psycopg/psycopg2

## Voir aussi

- [[Bases de données]] — le hub du domaine
