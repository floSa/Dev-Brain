---
galaxie: dev
type: service
nom: jupysql
alias: [JupySQL, jupysql]
pitch: "SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats."
categorie: tooling/notebook
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [notebook, dataframe]
url_docs: https://jupysql.ploomber.io/
url_repo: https://github.com/ploomber/jupysql
---

# jupysql

## Pourquoi

Exécute du **SQL directement dans un notebook** Jupyter via des *magics* : `%sql SELECT ...` en ligne, `%%sql` en cellule, `%sqlplot` pour tracer. Maintenu par **Ploomber**, c'est un **fork activement développé d'ipython-sql** (drop-in dans 99 % des cas) qui ajoute le tracé de gros volumes sans saturer la RAM, la composition de requêtes en **CTE** sur plusieurs cellules, et la paramétrisation. Compatible avec les grandes bases (PostgreSQL, MySQL, SQL Server), les entrepôts (Snowflake, BigQuery, Redshift) et les moteurs embarqués ([[Dev/Services/DuckDB|DuckDB]], SQLite) via SQLAlchemy. Les résultats se convertissent en DataFrame [[Dev/Services/pandas|pandas]] ou [[Dev/Services/Polars|Polars]].

## Quand l'utiliser

- Explorer une base en SQL **dans le notebook**, sans coller du SQL dans des chaînes Python.
- Coupler SQL et [[Dev/Services/DuckDB|DuckDB]] pour analyser des fichiers/Parquet locaux interactivement.
- Composer des requêtes longues en **CTE multi-cellules**, plus lisibles qu'un gros bloc.
- Tracer directement de gros résultats (`%sqlplot`) sans tout rapatrier en mémoire.

## Quand NE PAS l'utiliser

- Hors notebook (script, app, pipeline) → un client SQLAlchemy ou un driver direct ([[Dev/Services/psycopg2|psycopg2]]).
- Transformations versionnées et testées en production → un outil de transformation dédié, pas des cellules.
- Manipulation purement Python sur DataFrame → [[Dev/Services/pandas|pandas]] / [[Dev/Services/Polars|Polars]] directement.
- Besoin d'écriture transactionnelle structurée : jupysql vise l'exploration interactive, pas l'applicatif.

## Déploiement & coût

- Bibliothèque (`uv add jupysql`) ; `%load_ext sql` dans le notebook. Apache 2.0, gratuit, single-node.
- S'appuie sur SQLAlchemy pour la connexion : tout moteur supporté par SQLAlchemy est accessible.
- Coût nul côté infra ; suit le kernel Jupyter de l'utilisateur.

## Pièges

- Dépendance à un kernel Jupyter : c'est un outil d'exploration, pas une brique réutilisable hors notebook.
- Fork d'ipython-sql : quelques différences de comportement sur les cas limites lors d'une migration.
- Charger un gros résultat en DataFrame reste borné par la RAM — utiliser le tracé natif ou `LIMIT`.
- Connexions multiples dans un même notebook : bien nommer/sélectionner la connexion active.

## Alternatives

- _Prédécesseur direct : ipython-sql (catherinedevlin), désormais éclipsé par jupysql — pas fiché dans le brain. Pas d'autre outil « SQL en notebook » fiché à ce jour._

## Liens

- [[Dev/Services/DuckDB|DuckDB]] — compagnon fréquent : SQL analytique local dans le notebook.
- Sortie : [[Dev/Services/pandas|pandas]] / [[Dev/Services/Polars|Polars]] — conversion des résultats en DataFrame.
- Doc : https://jupysql.ploomber.io/
