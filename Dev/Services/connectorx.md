---
galaxie: dev
type: service
nom: connectorx
alias: [connector-x, connectorx]
pitch: "Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/ADBC|ADBC]]"]
remplace_par: []
status: actif
tags: [dataframe, columnar]
url_docs: https://sfu-db.github.io/connector-x/
url_repo: https://github.com/sfu-db/connector-x
---

# connectorx

## Pourquoi

Bibliothèque **spécialisée dans une seule chose** : sortir des données d'une base SQL vers un DataFrame Python le plus vite possible et avec le moins de mémoire. Écrite en **Rust**, elle applique le principe **zero-copy** — la donnée est copiée **exactement une fois**, directement de la source vers la destination, sans passer par des objets Python intermédiaires. Elle **parallélise** la lecture en partitionnant la requête sur une colonne. Sources : PostgreSQL, MySQL, SQLite, SQL Server, Oracle, BigQuery… Destinations : pandas, Polars, Arrow, Modin, Dask, NumPy. C'est le moteur derrière `pl.read_database(engine="connectorx")` de [[Dev/Services/Polars|Polars]].

## Quand l'utiliser

- Charger un gros résultat SQL en DataFrame nettement plus vite que `pandas.read_sql`.
- Lecture parallélisée d'une grosse table en partitionnant sur une clé numérique.
- Alimenter [[Dev/Services/pandas|pandas]] ou [[Dev/Services/Polars|Polars]] depuis une base sans pipeline ELT lourd.
- Minimiser l'empreinte mémoire d'une extraction (copie unique, pas de gonflement intermédiaire).

## Quand NE PAS l'utiliser

- Besoin d'**écrire** dans la base, de transactions ou d'une API de connectivité complète → [[Dev/Services/ADBC|ADBC]] ou un driver DB-API ([[Dev/Services/psycopg2|psycopg2]]).
- Mapping objet, migrations, modèle de domaine → [[Dev/Services/SQLAlchemy|SQLAlchemy]].
- Requêtes analytiques locales sur fichiers/Parquet sans base distante → [[Dev/Services/DuckDB|DuckDB]] directement.
- Pilote exotique non supporté : la couverture des sources est plus étroite qu'un driver générique.

## Déploiement & coût

- Bibliothèque (`uv add connectorx`), wheels précompilés. MIT, gratuit, single-node.
- Gain maximal quand la requête est **partitionnable** (clé numérique régulière) ; sinon lecture mono-flux.
- Pré-1.0 : vérifier la version et la matrice de sources/destinations supportées avant de s'engager.

## Pièges

- Lecture seule : connectorx **charge**, il n'écrit pas et n'exécute pas de DDL.
- Le partitionnement suppose une colonne adaptée ; mal choisie, les partitions sont déséquilibrées.
- Mapping de types parfois imparfait sur les types exotiques (numerics larges, dates/timezones) — vérifier le schéma de sortie.
- Projet à la maintenance irrégulière ; tester sur sa version de base de données cible.

## Alternatives

- [[Dev/Services/ADBC|ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.

## Liens

- [[Dev/Services/Polars|Polars]] — l'utilise comme moteur de `read_database`.
- [[Dev/Patterns/Comparatif - Manipulation de données]] — où atterrissent les DataFrames chargés.
- Doc : https://sfu-db.github.io/connector-x/
