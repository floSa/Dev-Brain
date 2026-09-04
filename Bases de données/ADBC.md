---
role: brique
nom: ADBC
alias: [arrow-adbc, Arrow Database Connectivity]
pitch: "Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow."
categorie: database/driver
famille: specification
licence_type: open-source
maturite: production
langage: C / Go / Java
alternatives: ["[[connectorx]]"]
complements: ["[[Polars]]"]
tags: [db-driver, columnar]
url_docs: https://arrow.apache.org/adbc/
url_repo: https://github.com/apache/arrow-adbc
---

# ADBC

<!-- AUTO:BANDEAU:START -->
> Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Spécification C / Go / Java | open-source | rien à exécuter | production |
<!-- AUTO:BANDEAU:END -->

## Définition

**Arrow Database Connectivity** : une API d'accès aux bases, portée par le projet Apache
Arrow, où les résultats et les paramètres de requête sont des données **colonnaires** Arrow.
C'est à l'analytique ce qu'ODBC et JDBC sont au transactionnel — une interface indépendante
du fournisseur, mais orientée colonnes. Chaque driver (PostgreSQL, SQLite, Snowflake,
BigQuery, tout moteur Flight SQL) supprime le passage ligne à ligne vers un DataFrame
colonnaire. Le gain n'existe que si **toute la chaîne** est colonnaire : vers du code ligne à
ligne, l'avantage Arrow s'évapore. Ce n'est ni un ORM ni un driver transactionnel — aucun
mapping objet, aucune migration.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Accéder à une base depuis un pipeline colonnaire sans payer la conversion ligne → colonne | Le moteur visé n'a pas de driver ADBC mûr : l'écosystème est plus jeune que ceux d'ODBC et JDBC |
| Lire **et** écrire, ingestion en masse comprise, derrière une API unique indépendante du fournisseur | Packaging par moteur : un paquet driver par base, aux versions appariées avec le driver manager |
| Remplacer ODBC/JDBC quand la charge est analytique et que la destination est Arrow | Sémantique des types Arrow ↔ SQL à vérifier sur les cas limites : décimaux, timestamps |
| Standardiser l'accès à plusieurs bases derrière une seule interface Arrow-native | |

## Mise en œuvre

- Installation — un paquet par moteur, plus le gestionnaire de drivers : `uv add adbc-driver-manager adbc-driver-postgresql`
- Point d'entrée — bindings Python, C#, Ruby, ou l'API native C/C++, Go, Java ; le driver est chargé dynamiquement
- Prérequis — un driver ADBC existant pour le moteur visé, à version appariée avec le gestionnaire
- Exécution — dans le process appelant, single-node ; rien à héberger
- Coût — gratuit, licence Apache 2.0

## Écosystème

### Alternatives

- [[connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.

### Compléments

- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. — son `read_database(engine="adbc")` s'appuie dessus.

## Ressources

- Documentation — https://arrow.apache.org/adbc/
- Dépôt — https://github.com/apache/arrow-adbc

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[psycopg2]] — le driver DB-API ligne à ligne, à l'opposé du modèle colonnaire
