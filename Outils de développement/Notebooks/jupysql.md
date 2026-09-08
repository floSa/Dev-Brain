---
role: brique
nom: jupysql
alias: [JupySQL, jupysql]
pitch: "SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats."
categorie: devtools/notebook
famille: extension
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[DuckDB]]"]
tags: [notebook, dataframe]
url_docs: https://jupysql.readthedocs.io/
url_repo: https://github.com/ploomber/jupysql
---

# jupysql

<!-- AUTO:BANDEAU:START -->
> SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Python | open-source | dans le moteur hôte, rien à héberger | production | à jour · 2025-03-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Exécute du SQL **directement dans un notebook** Jupyter, par des *magics* : `%sql` en ligne,
`%%sql` en cellule, `%sqlplot` pour tracer. Maintenu par **Ploomber**, c'est un fork
activement développé d'ipython-sql — drop-in dans la quasi-totalité des cas — qui ajoute le
tracé de gros volumes sans tout rapatrier en mémoire, la composition de requêtes en **CTE**
réparties sur plusieurs cellules, et la paramétrisation. La connexion passe par SQLAlchemy,
donc tout moteur qu'il supporte est accessible : bases classiques (PostgreSQL, MySQL, SQL
Server), entrepôts (Snowflake, BigQuery, Redshift), moteurs embarqués. Les résultats se
convertissent en DataFrame.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Explorer une base en SQL dans le notebook, sans coller du SQL dans des chaînes Python | Hors notebook — script, application, pipeline → un client SQLAlchemy ou un driver direct ([[psycopg2]]) |
| Analyser interactivement des fichiers Parquet locaux en SQL | Transformations versionnées et testées en production : des cellules ne font pas une brique réutilisable |
| Composer des requêtes longues en CTE multi-cellules, plus lisibles qu'un bloc unique | Manipulation purement Python sur DataFrame → [[pandas]] ou [[Polars]] |
| Tracer directement de gros résultats (`%sqlplot`) sans les rapatrier en mémoire | Charger un gros résultat en DataFrame reste borné par la RAM, et plusieurs connexions dans un même notebook demandent de nommer et sélectionner la connexion active |

## Mise en œuvre

- Installation — `uv add jupysql`
- Point d'entrée — `%load_ext sql` dans le notebook, puis les magics `%sql`, `%%sql` et `%sqlplot`
- Prérequis — un kernel Jupyter ; la connexion passe par SQLAlchemy, avec le driver du moteur visé
- Exécution — dans le kernel de l'utilisateur ; rien à héberger
- Coût — gratuit sous licence Apache 2.0

## Écosystème

### Compléments

- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — le compagnon le plus fréquent : SQL analytique local, sur fichiers et Parquet

## Ressources

- Documentation — https://jupysql.readthedocs.io/
- Dépôt — https://github.com/ploomber/jupysql

## Voir aussi

- [[Notebooks]] — le hub du dossier
