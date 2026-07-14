---
galaxie: dev
type: service
nom: ADBC
alias: [arrow-adbc, Arrow Database Connectivity]
pitch: "Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow."
categorie: database/driver
licence_type: open-source
hosted: self
maturite: production
langage: C / Go / Java
scaling: single-node
alternatives: ["[[Dev/Services/connectorx|connectorx]]"]
remplace_par: []
status: actif
tags: [db-driver, columnar]
url_docs: https://arrow.apache.org/adbc/
url_repo: https://github.com/apache/arrow-adbc
---

# ADBC

## Pourquoi

**Arrow Database Connectivity** : une API standard d'accès aux bases, par le projet **Apache Arrow**, où les résultats et les paramètres de requête sont des **données Arrow** (colonnaires). C'est à l'analytique ce qu'ODBC/JDBC sont au transactionnel : une interface **indépendante du fournisseur**, mais orientée colonnes. Les drivers (PostgreSQL, SQLite, Snowflake, BigQuery, tout moteur Flight SQL…) optimisent la conversion vers/depuis Arrow, ce qui évite le coûteux passage ligne-à-ligne d'une API DB-API/ODBC vers un DataFrame colonnaire. Implémentations en C/C++, Go, Java, avec bindings Python, C#, Ruby. Apache 2.0.

## Quand l'utiliser

- Accès à une base depuis un pipeline **colonnaire** (Arrow, [[Dev/Services/Polars|Polars]], [[Dev/Services/DuckDB|DuckDB]]) sans payer la conversion ligne→colonne.
- Lire **et écrire** (ingestion en masse) avec une API unique, vendor-independent.
- Remplacer ODBC/JDBC quand la charge est analytique/OLAP et que la destination est Arrow.
- Standardiser l'accès à plusieurs bases derrière une seule interface Arrow-native.

## Quand NE PAS l'utiliser

- Lecture seule la plus rapide possible vers un DataFrame, sans besoin d'écriture → [[Dev/Services/connectorx|connectorx]] (plus simple, taillé pour ça).
- Application transactionnelle Postgres classique, ligne-à-ligne → driver DB-API [[Dev/Services/psycopg2|psycopg2]].
- Mapping objet, migrations, modèle de domaine → [[Dev/Services/SQLAlchemy|SQLAlchemy]].
- Base sans driver ADBC disponible : l'écosystème de drivers est plus jeune qu'ODBC/JDBC.

## Déploiement & coût

- Bibliothèque + drivers (`uv add adbc-driver-postgresql adbc-driver-manager`). Apache 2.0, gratuit, single-node.
- Driver chargé dynamiquement (driver manager) ou paquet Python dédié par base.
- Coût quasi nul côté infra : suit l'application, comme tout driver.

## Pièges

- Écosystème de drivers encore en construction : tous les SGBD n'ont pas de driver ADBC mûr.
- Gains réels surtout si **toute la chaîne** est colonnaire ; vers du code ligne-à-ligne, l'avantage Arrow s'évapore.
- Packaging par base (un paquet driver par moteur) ; attention aux versions appariées driver/manager.
- Sémantique des types Arrow ↔ types SQL à vérifier sur les cas limites (decimals, timestamps).

## Alternatives

- [[Dev/Services/connectorx|connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.

## Liens

- [[Dev/Services/Polars|Polars]] — `read_database(engine="adbc")` s'appuie dessus.
- [[Dev/Services/psycopg2|psycopg2]] — le driver DB-API row-based, à l'opposé du modèle colonnaire d'ADBC.
- Doc : https://arrow.apache.org/adbc/
