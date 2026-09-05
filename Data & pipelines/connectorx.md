---
role: brique
nom: connectorx
alias: [connector-x, connectorx]
pitch: "Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination."
categorie: data/ingestion
famille: paquet
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[ADBC]]"]
complements: ["[[Polars]]"]
tags: [dataframe, columnar]
url_docs: https://sfu-db.github.io/connector-x/
url_repo: https://github.com/sfu-db/connector-x
---

# connectorx

<!-- AUTO:BANDEAU:START -->
> Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque spécialisée dans une seule opération : sortir le résultat d'une requête SQL vers
un DataFrame Python, le plus vite possible et avec le moins de mémoire. Le principe est le
**zero-copy** — la donnée est copiée exactement une fois, de la source vers la destination,
sans objets Python intermédiaires — et la lecture se **parallélise** en partitionnant la
requête sur une colonne. Sources : PostgreSQL, MySQL, SQLite, SQL Server, Oracle, BigQuery.
Destinations : pandas, Polars, Arrow, Modin, Dask, NumPy. C'est le moteur derrière
`read_database(engine="connectorx")` côté Polars. Le corollaire de cette spécialisation est
qu'il ne fait rien d'autre : il charge, il n'écrit pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charger un gros résultat SQL en DataFrame nettement plus vite que `pandas.read_sql` | Écrire dans la base, transactions, connectivité complète → [[ADBC]], ou un driver DB-API comme [[psycopg2]] |
| Lire une grosse table en parallèle, en partitionnant sur une clé numérique | Mapping objet, migrations, modèle de domaine → [[SQLAlchemy]] |
| Alimenter [[pandas]] depuis une base sans monter un pipeline ELT | Requêtes analytiques locales sur fichiers ou Parquet, sans base distante → [[DuckDB]] |
| Minimiser l'empreinte mémoire d'une extraction : copie unique, aucun gonflement intermédiaire | Requête non partitionnable : sans colonne adaptée la lecture retombe en mono-flux, et une clé mal choisie déséquilibre les partitions |
| | Types exotiques — numerics larges, dates avec fuseau : le mapping est parfois imparfait, vérifier le schéma de sortie |
| | Pilote exotique, ou base dont la version compte : la couverture des sources est plus étroite qu'un driver générique, le projet est pré-1.0 et sa maintenance irrégulière |

## Mise en œuvre

- Installation — `uv add connectorx`, wheels précompilés
- Point d'entrée — `connectorx.read_sql(conn, query)`, ou `read_database(engine="connectorx")` côté Polars
- Prérequis — une chaîne de connexion vers une source supportée ; une colonne de partitionnement pour paralléliser
- Exécution — dans le process appelant, single-node ; le travail lourd se fait en Rust
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.

### Compléments

- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. Il appelle connectorx comme moteur de son `read_database`.

## Ressources

- Documentation — https://sfu-db.github.io/connector-x/
- Dépôt — https://github.com/sfu-db/connector-x

## Voir aussi

- [[ELT vs ETL & idempotence]] — l'étape d'extraction que cette bibliothèque exécute
- [[Comparatif - Manipulation de données]] — où atterrissent les DataFrames chargés
