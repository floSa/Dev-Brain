---
role: brique
nom: dbt Core
alias: [dbt, dbt-core, dbt OSS, dbt v1, dbt v2]
pitch: "Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit)."
categorie: data/transformation
famille: cli
licence_type: open-source
maturite: production
langage: "Python, Rust"
alternatives: ["[[SQLMesh]]"]
complements: ["[[Airflow]]", "[[Dagster]]", "[[Prefect]]", "[[Kestra]]", "[[Postgres]]", "[[DuckDB]]", "[[ClickHouse]]", "[[Spark]]", "[[Parquet]]", "[[Apache Iceberg]]"]
tags: [data-transformation, data-pipeline, data-quality]
url_docs: https://docs.getdbt.com/
url_repo: https://github.com/dbt-labs/dbt-core
---

# dbt Core

<!-- AUTO:BANDEAU:START -->
> Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python, Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de transformation qui exécute, **dans le moteur de données**, des `SELECT` écrits comme des
**modèles** : un fichier SQL (avec Jinja) par modèle, `ref()` pour désigner son parent, et dbt en
déduit le graphe, l'ordre d'exécution et la matérialisation (vue, table, incrémental,
éphémère). Il ne charge rien : la donnée source doit déjà être dans le moteur, dbt ne fait que le
T de l'[[ELT vs ETL & idempotence|ELT]]. Tests de données, snapshots (dimensions à historique),
seeds, documentation générée et contrats de modèle vivent dans le même projet Git.

Relevé le 2026-09-30 : **deux lignes portent le même nom**. **dbt Core v1** — Python, 1.12.5 du
2026-09-15, Apache-2.0, environ 13 900 étoiles, 22,5 M de téléchargements PyPI en 30 jours —
pilote Postgres, Trino, ClickHouse, DuckDB et Spark. **dbt v2** — Rust, 2.0.0 du 2026-09-14 —
publie son code sous Apache-2.0 dans le même dépôt (paquet `dbt-oss`), mais la distribution
complète « dbt » est un binaire sous licence produit ; « dbt Core » n'y désigne plus rien.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des transformations en SQL sur un moteur déjà en place (Postgres, DuckDB, ClickHouse, Spark, Trino), relues en revue de code comme n'importe quel projet Git | Charger ou copier des données depuis une source : dbt ne transforme que ce qui est déjà dans le moteur |
| Tests de données, snapshots à historique, contrats de modèle et graphe au niveau modèle dans un seul outil, sans service à héberger | Du Python à exécuter sur le moteur : les modèles Python sont documentés pour Snowflake, BigQuery et Databricks, la page ne cite ni Postgres, ni Trino, ni ClickHouse |
| Le standard de fait : 22,5 M de téléchargements par mois, packages (`dbt_utils`), compétences trouvables | Le lignage au niveau **colonne** sans licence produit : v1 ne l'a pas, v2 l'exige dans la distribution complète et non dans `dbt-oss` |
| Un moteur exécutable en site isolé, avec un adaptateur `Trusted` maintenu (Postgres, Spark, ClickHouse, DuckDB, Trino) | Un traitement continu : dbt exécute des lots, il ne fait pas de flux |

## Mise en œuvre

- Installation — v1 : `uv add dbt-core dbt-postgres` (Python ≥ 3.10 ; un adaptateur par moteur : `dbt-duckdb`, `dbt-clickhouse`, `dbt-trino`, `dbt-spark`). v2 : binaire unique (brew, curl, winget, PowerShell) ou `pip install dbt-oss` (Python ≥ 3.11)
- Point d'entrée — `dbt build` (run + test + seed + snapshot dans l'ordre du graphe), `dbt run`, `dbt test`, `dbt docs generate` ; `dbt_project.yml`, dossier `models/`, connexion dans `profiles.yml`
- Prérequis — un moteur déjà rempli. **Choisir la ligne d'après l'adaptateur** : Postgres (`dbt-postgres` 1.11.0, 2026-07-16) et Trino (`dbt-trino` 1.10.5, 2026-09-23) n'existent **pas** en v2 (issues dbt-labs/dbt#13123 et #13131, sans échéance) ; ClickHouse y est en *private beta*, Spark en *beta*, DuckDB en disponibilité générale. Les adaptateurs communautaires v1 ne se chargent pas en v2. Au premier lancement, v2 télécharge ses pilotes ADBC depuis un CDN de dbt Labs puis fonctionne hors ligne : en site isolé, prévoir ce téléchargement
- Exécution — CLI lancée à la main, en CI ou par un orchestrateur ; **aucun ordonnanceur en édition libre** (le scheduler est dans dbt platform). Le calcul se fait dans le moteur cible. Plusieurs invocations dans un même processus ne sont pas sûres : sous-processus séparés
- Coût — gratuit. dbt Core v1 et `dbt-oss` : Apache-2.0. Binaire « dbt » v2 : licence produit dbt, utilisable **sans compte**, sans limite d'utilisateurs, en environnement isolé, et installable par une ESN chez ses clients tant que chaque déploiement reste autonome ; interdit seulement de fournir dbt en service géré à des tiers sans leur ouvrir les fonctions de dbt platform (FAQ des licences, modifiée le 2026-09-15). dbt platform (ex-dbt Cloud) est payant : IDE, scheduler, Catalog, Semantic Layer hébergé

## Licence et gouvernance

- **2025-05-28** — dbt Fusion (moteur Rust) est annoncé sous **Elastic License 2.0**. **2025-10-13** — accord de fusion Fivetran / dbt Labs, avec l'engagement écrit de garder dbt Core ouvert sous sa licence actuelle ; MetricFlow passe sous Apache-2.0.
- **2026-06-01** — clôture de la fusion. Le code de Fusion est relicencié **Apache-2.0** et versé dans `dbt-core` (le dépôt `dbt-fusion` est archivé) ; `dbt-labs/dbt-core` redirige vers `dbt-labs/dbt`, dont `main` porte le code Rust.
- **2026-09-14** — dbt 2.0.0 ; la v1 continue sur la branche `1.latest`. 1.13 sera la **dernière mineure** de la série 1.x, 1.12 est en support actif jusqu'au 2027-07-15, avec un support critique de « plusieurs (3-5) ans » sans date d'arrêt fixée.

Deux sources se contredisent sur le lignage colonne : la feuille de route de juin 2026 le range derrière `dbt login`, la documentation du 2026-09-28 le dit utilisable **sans compte** dans la distribution complète. À revérifier avant de le promettre à un client.

## Limites à connaître

- **Pas d'environnements virtuels.** Un environnement de développement est un schéma que dbt reconstruit ; `--defer` évite de recalculer les parents, `dbt clone` crée des objets — de vraies copies seulement sur Snowflake, Databricks et BigQuery, de simples vues `SELECT *` ailleurs (Postgres compris).
- **Incrémental** : le SQL du modèle doit rester valide que `is_incremental()` soit vrai ou faux, et il est faux avec `--full-refresh`.
- **Jinja n'est pas un langage de programmation** (mise en garde de la documentation) : la logique lourde se cache dans des macros difficiles à relire. v2 parse plus strictement et fait échouer les macros inexistantes ; migrer d'abord vers la dernière v1 sans avertissement de dépréciation. SQLFluff n'y est pas compatible nativement : `dbt lint`, dans la distribution complète seulement, le remplace.

## Écosystème

### Alternatives

- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran.

### Compléments

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le paquet distinct `astronomer-cosmos` (Apache-2.0, 1.15.1 du 2026-08-04) rend un projet dbt en DAG ou en groupe de tâches Airflow, une tâche par modèle, avec reprises et tests lancés juste après chaque modèle ; Airflow 2.9 à 3.3 et dbt Core 1.8 à 1.12 d'après la politique de compatibilité de la branche principale.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés. — `dagster-dbt` (0.29.24, 2026-09-21, Apache-2.0) représente les modèles, seeds et snapshots dbt comme des assets Dagster et les tests comme des asset checks ; dbt Core 1.7 à 1.12, et Fusion en preview sans lignage au niveau colonne d'après la documentation de Dagster.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer. — `prefect-dbt` (0.7.25, 2026-06-05, Apache-2.0) lance dbt Core depuis un flow : `PrefectDbtRunner` observe chaque nœud dbt comme une tâche, `PrefectDbtOrchestrator` (bêta) fait piloter chaque nœud par Prefect, avec reprises et cache par nœud.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — le plugin dbt de Kestra (Apache-2.0) lance n'importe quelle commande dbt dans un conteneur par la tâche `DbtCLI` et parse les résultats ; il sait aussi déclencher un job dbt Cloud.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — `dbt-postgres` (1.11.0, 2026-07-16), adaptateur `Trusted` maintenu par dbt Labs ; il n'existe pas en dbt v2.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — `dbt-duckdb` (1.11.0, 2026-08-07) lit des fichiers CSV, Parquet et JSON et en écrit par la matérialisation `external` ; adaptateur intégré et en disponibilité générale dans dbt v2, dont le pilote embarqué ne charge pas d'extensions.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — `dbt-clickhouse` (1.10.3, 2026-09-15), maintenu par ClickHouse Inc. ; vues matérialisées et tables distribuées expérimentales ; en dbt v2 il est en *private beta*, sans `ON CLUSTER` ni matérialisations distribuées.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — `dbt-spark` (1.11.0, 2026-07-16), maintenu par dbt Labs ; connexions ODBC, Thrift, HTTP et session, formats de fichier `parquet`, `delta`, `iceberg` et `hudi` ; en dbt v2 il est en bêta, limité à Spark 3.0.
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet. — dbt-duckdb écrit du Parquet par la matérialisation `external` (`format: parquet`) et dbt-spark le prend comme `file_format`.
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — dbt-spark accepte `file_format: iceberg` ; la documentation dbt des catalogues Iceberg (`catalogs.yml`, dbt 1.10) détaille Snowflake, BigQuery, Databricks et DuckDB (ce dernier en dbt v2 seulement) et ne dit rien d'Iceberg pour Trino ni pour ClickHouse.

## Ressources

- Documentation — https://docs.getdbt.com/
- Dépôt — https://github.com/dbt-labs/dbt-core
- Documentation — https://www.getdbt.com/licenses-faq
- Article — https://docs.getdbt.com/blog/dbt-core-v2-is-here

## Voir aussi

- [[Data & pipelines]] — le hub du dossier
- [[Comparatif - Transformation SQL]] — ce qui départage dbt Core et SQLMesh
- [[ELT vs ETL & idempotence]] — l'ordre d'assemblage dont dbt est le T
- [[Architecture médaillon]] — les couches que les modèles dbt raffinent
