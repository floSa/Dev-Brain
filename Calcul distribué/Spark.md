---
role: brique
nom: Spark
alias: [Apache Spark, spark, PySpark, pyspark]
pitch: "Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark."
categorie: compute/distribue
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Scala / JVM
scaling: distributed
alternatives: ["[[Dask]]", "[[Ray]]"]
complements: ["[[Databricks]]", "[[dbt Core]]", "[[SQLMesh]]", "[[Great Expectations]]", "[[pandera]]", "[[OpenLineage]]", "[[DataHub]]"]
tags: [distributed, dataframe, streaming, out-of-core]
url_docs: https://spark.apache.org/docs/latest/
url_repo: https://github.com/apache/spark
---

# Spark

<!-- AUTO:BANDEAU:START -->
> Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Scala / JVM | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-31 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur unifié de traitement de données à grande échelle, écrit sur la **JVM** en Scala. Il
distribue le calcul sur un cluster avec un planificateur DAG et une exécution en mémoire,
paresseuse et optimisée par Catalyst et Tungsten. Une seule plateforme couvre plusieurs
charges : Spark SQL et DataFrames pour l'analytique, Structured Streaming pour les flux,
MLlib pour le ML distribué, GraphX pour les graphes. L'API **PySpark** expose tout cela en
Python, au prix d'un pont Python↔JVM qui commande la performance des UDF. Spark 4.0 (2025)
ajoute Spark Connect, le type VARIANT, l'ANSI SQL par défaut et Java 21.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Traitement ELT ou batch de très gros volumes (To et plus) sur cluster, en SQL ou DataFrame | L'overhead **JVM** et le démarrage de session pénalisent les petits jobs et l'interactif à faible latence |
| Écosystème big data ou lakehouse établi — Hadoop, Hive, [[Apache Iceberg]], Delta — et plateformes managées | Le **shuffle** — tri, jointures larges, `groupBy` — est le goulet principal : partitionnement et skew à surveiller |
| Streaming structuré unifié avec le batch, sous la même API | Les **UDF Python** non vectorisées traversent lentement le pont Python↔JVM : préférer les fonctions natives ou les UDF pandas/Arrow |
| Équipe déjà sur la JVM, ou besoin de la maturité opérationnelle de Spark | Réglage mémoire (exécuteurs, partitions) presque toujours nécessaire : les défauts conviennent rarement aux gros jobs |
| | Données qui tiennent sur une machine → [[Polars]] ou [[DuckDB]], souvent plus rapides et sans cluster |

## Mise en œuvre

- Installation — `uv add pyspark` ; Spark 4.0 ajoute un client léger `pyspark-client` (~1,5 Mo) via Spark Connect
- Point d'entrée — session Spark depuis Python (PySpark), SQL ou DataFrames ; Structured Streaming et MLlib sur la même session
- Prérequis — une JVM, et un gestionnaire de cluster : Standalone, YARN ou Kubernetes
- Exécution — self-hébergé ou managé, distribué ; managé chez Databricks, AWS EMR, Google Dataproc, Azure Synapse, facturés à l'usage cluster
- Coût — gratuit, Apache-2.0 ; le coût réel est l'infrastructure, la mémoire surtout

## Écosystème

### Alternatives

- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Ray]] — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).

### Compléments

- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — la plateforme écrite par ses auteurs : elle l'exploite pour vous, et les compétences se transfèrent dans les deux sens.
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — `dbt-spark` (1.11.0, 2026-07-16), maintenu par dbt Labs ; connexions ODBC, Thrift, HTTP et session, formats de fichier `parquet`, `delta`, `iceberg` et `hudi` ; en dbt v2 il est en bêta, limité à Spark 3.0.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran. — moteur pris en charge, conçu et testé pour un seul catalogue, qui ne peut pas héberger l'état.
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026. — les DataFrames Spark se valident par `add_spark(...)` (extra `spark`) et Spark figure dans la liste de compatibilité officielle.
- [[pandera]] — Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT). — PySpark SQL est de première classe (schéma, modèle, checks, validation paresseuse), par l'extra `pyspark`.
- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data). — écouteur `OpenLineageSparkListener` (`spark.extraListeners`), avec une section de lignage colonne dans la documentation.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — agent Spark propre à DataHub, qui complète l'écouteur OpenLineage (PathSpec, lignage colonne).

## Ressources

- Documentation — https://spark.apache.org/docs/latest/
- Dépôt — https://github.com/apache/spark

## Voir aussi

- [[Calcul distribué]] — le hub du domaine
- [[Parquet]] · [[Apache Iceberg]] — les formats et tables qu'il lit
- [[Comparatif - Calcul distribué]] — ce qui départage les moteurs du dossier
