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
complements: []
tags: [distributed, dataframe, streaming, out-of-core]
url_docs: https://spark.apache.org/docs/latest/
url_repo: https://github.com/apache/spark
---

# Spark

<!-- AUTO:BANDEAU:START -->
> Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Scala / JVM | open-source | self-hébergé ou managé · distribué | production |
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

## Ressources

- Documentation — https://spark.apache.org/docs/latest/
- Dépôt — https://github.com/apache/spark

## Voir aussi

- [[Calcul distribué]] — le hub du domaine
- [[Parquet]] · [[Apache Iceberg]] — les formats et tables qu'il lit
- [[Comparatif - Calcul distribué]] — ce qui départage les moteurs du dossier
