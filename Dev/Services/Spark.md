---
galaxie: dev
type: service
nom: Spark
alias: [Apache Spark, spark, PySpark, pyspark]
pitch: "Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark."
categorie: compute/distributed
licence_type: open-source
hosted: both
maturite: production
langage: Scala / JVM
scaling: distributed
alternatives: ["[[Dev/Services/Dask|Dask]]", "[[Dev/Services/Ray|Ray]]"]
remplace_par: []
status: actif
tags: [distributed, dataframe, streaming, out-of-core]
url_docs: https://spark.apache.org/docs/latest/
url_repo: https://github.com/apache/spark
---

# Spark

## Pourquoi

**Moteur unifié de traitement de données à grande échelle**, écrit sur la JVM (Scala). Distribue le calcul sur un cluster avec un planificateur DAG et une exécution **en mémoire** (lazy, optimisée par Catalyst/Tungsten). Une seule plateforme couvre plusieurs charges : **Spark SQL / DataFrames** (le cœur analytique), **Structured Streaming** (flux), **MLlib** (ML distribué) et GraphX. L'API **PySpark** expose tout cela en Python, ce qui en fait le standard du big data côté data engineering. Spark 4.0 (2025) ajoute Spark Connect (client léger découplé), le type VARIANT, l'ANSI SQL par défaut et Java 21.

## Quand l'utiliser

- Traitement **ELT / batch** de très gros volumes (To+) sur un cluster, en SQL ou DataFrame.
- Écosystème **big data / lakehouse** établi (Hadoop, Hive, [[Dev/Services/Apache Iceberg|Iceberg]], Delta) et plateformes managées (Databricks, EMR, Dataproc).
- **Streaming structuré** unifié avec le batch (même API).
- Équipes déjà sur la **JVM** ou ayant besoin de la maturité opérationnelle de Spark.

## Quand NE PAS l'utiliser

- Rester **100 % Python** sans cluster JVM, en gardant l'API numpy/pandas → [[Dev/Services/Dask|Dask]].
- Paralléliser du **code Python arbitraire** / charges ML hétérogènes → [[Dev/Services/Ray|Ray]].
- Données qui tiennent sur une machine → [[Dev/Services/Polars|Polars]] / [[Dev/Services/DuckDB|DuckDB]] (souvent plus rapides, sans cluster).
- Faible latence interactive : le coût de démarrage et l'overhead JVM pèsent sur les petits jobs.

## Déploiement & coût

- Open-source (Apache-2.0). Self-host sur cluster (Standalone, YARN, **Kubernetes**) ou local pour le dev.
- PySpark s'installe via `uv add pyspark` ; Spark 4.0 ajoute un client léger `pyspark-client` (~1.5 Mo) avec Spark Connect.
- **Managé** : Databricks, AWS EMR, Google Dataproc, Azure Synapse — facturés à l'usage cluster.
- Coût = l'infra (mémoire surtout) ; bien dimensionner exécuteurs et partitions.

## Pièges

- L'overhead **JVM** et le démarrage de session pénalisent les petits jobs : Spark brille sur le gros volume, pas sur l'interactif léger.
- Le **shuffle** (tri, jointures larges, `groupBy`) est le principal goulet : partitionnement et skew de données à surveiller.
- PySpark = pont Python↔JVM : les **UDF Python** non vectorisées sont lentes (préférer les fonctions natives ou les UDF pandas/Arrow).
- Réglage mémoire (exécuteurs, partitions) souvent nécessaire ; les défauts conviennent rarement aux gros jobs.

## Alternatives

- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Dev/Services/Ray|Ray]] — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).

## Liens

- [[Comparatif - Calcul distribué]] — comparatif de la catégorie
- Formats / tables lus : [[Dev/Services/Parquet|Parquet]], [[Dev/Services/Apache Iceberg|Apache Iceberg]].
- Alternative single-node analytique : [[Dev/Services/DuckDB|DuckDB]].
- Doc : https://spark.apache.org/docs/latest/
