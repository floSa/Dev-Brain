---
role: brique
nom: dlt
alias: [dlt, data load tool, dlt-hub]
pitch: "Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0)."
categorie: data/ingestion
famille: paquet
licence_type: open-core
maturite: production
langage: Python
alternatives: ["[[Airbyte]]", "[[Apache NiFi]]"]
complements: ["[[Airflow]]", "[[Dagster]]", "[[Kestra]]", "[[connectorx]]", "[[Postgres]]", "[[DuckDB]]", "[[ClickHouse]]", "[[Parquet]]"]
tags: [data-ingestion, data-pipeline, schema-evolution]
url_docs: https://dlthub.com/docs/
url_repo: https://github.com/dlt-hub/dlt
---

# dlt

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-core | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui charge des données dans une destination : on écrit une **source** (un
générateur décoré par `@dlt.resource`, ou une source prête pour une API REST, une base SQL ou des
fichiers), et `dlt` enchaîne trois étapes dans le même processus — *extract*, *normalize*, *load* —
en inférant le schéma et en le faisant évoluer. Il n'y a ni serveur ni interface : le pipeline est un
script, lancé par cron, CI ou un orchestrateur.

Relevé le 2026-09-30 : **1.30.0** du 2026-08-11 (Python ≥ 3.10, < 3.15), Apache-2.0, environ 5 910
étoiles, dernier commit du jour, environ 4,8 M de téléchargements PyPI sur 30 jours d'après pypistats.
Une extension commerciale distincte, **dltHub** (paquet `dlthub`), existe à côté.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des sources écrites en Python : une API interne, une base maison, des fichiers déposés | Un catalogue de centaines de connecteurs prêts à cocher dans une interface : [[Airbyte]] |
| Un pipeline qui vit dans un dépôt Git, se teste et se relance comme du code, sans plateforme à héberger | Une équipe qui ne veut pas écrire de Python : la définition d'un pipeline est du code |
| Charger vers DuckDB, Postgres, ClickHouse ou des fichiers Parquet, sur site | Iceberg ou Delta en destination : ces destinations relèvent de dltHub, sous licence commerciale |
| Un incrémental par curseur avec dédoublonnage et reprise après échec, sans base d'état à héberger | Des flux industriels ou du routage d'événements : [[Apache NiFi]] |
| Un schéma qui évolue tout seul, avec des contrats (`evolve`, `freeze`, `discard_row`, `discard_value`) pour le cadrer | Le CDC d'une base autre que Postgres : seul `pg_replication` existe en source libre |

## Mise en œuvre

- Installation — `uv add dlt`, avec un extra par destination (`dlt[duckdb]`, `dlt[clickhouse]`, `dlt[filesystem]`)
- Point d'entrée — `dlt.pipeline(pipeline_name=…, destination=…, dataset_name=…)` puis `pipeline.run(source)` ; la CLI `dlt init` échafaude une source
- Prérequis — Python et une destination joignable ; aucun broker
- Exécution — dans le processus appelant, mono-nœud ; Airflow (`PipelineTasksGroup`), Dagster (`dagster-dlt`), un plugin Kestra et GitHub Actions sont documentés
- Coût — gratuit sous Apache-2.0 ; dltHub (destinations Iceberg et Delta, source MS SQL, contrôles de qualité, exécution managée) demande une licence commerciale

## Licence et gouvernance

- Le paquet `dlt` est en **Apache-2.0** (GitHub et PyPI, 2026-09-30). Le fournisseur est dltHub, Inc.
- **dltHub est une extension commerciale** : la page de comparaison des éditions place chez lui les destinations Iceberg et Delta, la source MS SQL (CDC par Change Tracking), les transformations, la qualité de données et l'exécution managée ; « toutes les composantes de dltHub sont disponibles avec une licence commerciale », la plupart en source-available sous leur propre licence. La page de la destination Iceberg est rangée sous `hub/ingestion` avec la mention d'une licence commerciale dltHub.
- **Désaccord non tranché** : la page de la destination `filesystem` liste aussi les formats de table `delta` et `iceberg` sans mention de licence. Laquelle des deux voies est libre n'est pas écrit : à tester avant de promettre de l'Iceberg en libre.

## Limites à connaître

- **Le curseur relit la ligne au curseur** : `range_start="closed"` (défaut) réacquiert les lignes égales à la dernière valeur, puis les dédoublonne par clé primaire ou par empreinte du contenu ; en `"open"`, pas de dédoublonnage. Un curseur ne voit jamais une ligne supprimée.
- **CDC restreint** : la source `pg_replication` lit le slot logique `pgoutput`, sans Kafka, mais ne prend pas en charge la stratégie de fusion `scd2`. Aucune source CDC MySQL n'a été trouvée.
- **Stratégies de fusion** : `delete-insert` (défaut), `scd2`, `upsert` et `insert-only` ; `upsert` et `insert-only` ne fonctionnent que sur certaines destinations (Postgres, MSSQL, BigQuery, Snowflake, Databricks, Athena, LanceDB, Delta et Iceberg sur fichiers).
- **Pas d'interface, pas d'ordonnanceur** : le suivi et la planification restent à un outil tiers.

## Écosystème

### Alternatives

- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes.
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker.

### Compléments

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — la page de déploiement documente le groupe de tâches `PipelineTasksGroup` (modes sérialisé, parallèle, parallèle isolé).
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés. — `dagster-dlt` (0.29.24, 2026-09-21) expose les ressources dlt comme assets.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — Kestra publie un plugin dlt.
- [[connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination. — l'un des quatre moteurs de lecture de la source `sql_database` (avec SQLAlchemy, PyArrow et pandas).
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — destination, et source CDC par la source `pg_replication`.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — destination locale la plus simple pour essayer un pipeline.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — destination documentée, utilisable sur site.
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet. — format d'écriture de la destination `filesystem`, à côté de JSONL (défaut) et CSV.

## Ressources

- Documentation — https://dlthub.com/docs/
- Dépôt — https://github.com/dlt-hub/dlt

## Voir aussi

- [[Ingestion de données]] — le hub du dossier
- [[Comparatif - Ingestion de données]] — ce qui départage dlt, Airbyte, Debezium et Apache NiFi
- [[Ingestion incrémentale et curseurs]] — curseurs, dédoublonnage, reprise
- [[ELT vs ETL & idempotence]] — l'ordre d'assemblage dont dlt est l'étape de chargement
- [[MinIO]] — destination S3 : la destination `filesystem` accepte un `endpoint_url` pour un stockage compatible S3, MinIO cité ; le dépôt MinIO est archivé
- [[dbt Core]] et [[SQLMesh]] — la transformation qui suit le chargement
