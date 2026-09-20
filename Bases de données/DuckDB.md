---
role: brique
nom: DuckDB
alias: [duckdb]
pitch: "Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur."
categorie: database/analytique
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[ClickHouse]]", "[[Snowflake]]"]
complements: ["[[pandas]]", "[[Polars]]", "[[jupysql]]", "[[dbt Core]]", "[[SQLMesh]]", "[[Soda Core]]", "[[Airbyte]]", "[[dlt]]", "[[Delta Lake]]"]
tags: [columnar, olap, embedded]
url_docs: https://duckdb.org/docs/
url_repo: https://github.com/duckdb/duckdb
---

# DuckDB

<!-- AUTO:BANDEAU:START -->
> Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-22 |
<!-- AUTO:BANDEAU:END -->

## Définition

Base analytique **in-process**, le « SQLite de l'OLAP » : pas de serveur, elle tourne dans le
process hôte — Python, R, ou la ligne de commande. Stockage en **colonnes** et exécution
**vectorisée**, sans dépendance externe : un compilateur C++17 suffit à la bâtir. Elle
requête directement des fichiers Parquet, CSV et JSON, sans étape de chargement préalable, et
s'interface avec pandas, Polars et Arrow. La base est soit en mémoire, soit un fichier unique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analytique locale et exploration sur un poste : data science, notebooks | Un seul écrivain à la fois, comme SQLite : les écritures concurrentes transactionnelles ne passent pas |
| Requêter des fichiers Parquet, CSV ou JSON en SQL sans monter d'infra | Elle tient sur une machine : la RAM et le disque local bornent le volume |
| ETL léger et transformations au sein d'un pipeline Python | Elle n'est pas conçue pour servir des milliers de clients simultanés, ni pour la haute disponibilité |
| Tests et prototypes analytiques jetables | OLTP et écritures concurrentes transactionnelles → [[Postgres]] |

## Mise en œuvre

- Installation — `uv add duckdb` ; aucune dépendance externe à installer
- Point d'entrée — SQL depuis Python, R ou la CLI ; requêtes directes sur Parquet, CSV et JSON
- Prérequis — aucun serveur ; la base est en mémoire ou dans un fichier unique
- Exécution — dans le process appelant, single-node, mais tous les cœurs locaux sont exploités
- Coût — gratuit, licence MIT garantie à perpétuité par la DuckDB Foundation ; option managée via MotherDuck

## Écosystème

### Alternatives

- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.
- [[Snowflake]] — Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement. — l'extrême opposé : rien ne tourne en local, tout est managé, et le volume n'est plus borné par le poste ; rangé en plateforme, pas en base, cf. la règle D-R8 de la taxonomie.

### Compléments

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — intégration directe, dans les deux sens.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. — intégration directe via Arrow.
- [[jupysql]] — SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats. — le compagnon notebook : du SQL analytique local en magic cell
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — `dbt-duckdb` (1.11.0, 2026-08-07) lit des fichiers CSV, Parquet et JSON et en écrit par la matérialisation `external` ; adaptateur intégré et en disponibilité générale dans dbt v2, dont le pilote embarqué ne charge pas d'extensions.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran. — moteur pris en charge, à utilisateur unique et recommandé pour le développement seulement ; c'est aussi le moteur des tests unitaires par défaut, et la documentation le déconseille comme base d'état en production.
- [[Soda Core]] — Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud. — un DataFrame pandas ou Polars est enregistré dans un DuckDB en mémoire, puis le contrat est vérifié sur cette vue (paquet `soda-duckdb`).
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — destination communautaire en bêta (`destination-duckdb` 0.6.0).
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0). — destination locale, la plus simple pour essayer un pipeline.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — extension `delta` fondée sur `delta-kernel-rs` : lecture, et écriture limitée à des ajouts d'enregistrements.

## Ressources

- Documentation — https://duckdb.org/docs/
- Dépôt — https://github.com/duckdb/duckdb

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases colonnes]] — ce qui départage les moteurs du dossier
