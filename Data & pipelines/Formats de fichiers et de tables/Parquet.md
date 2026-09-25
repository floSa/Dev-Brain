---
role: brique
nom: Parquet
alias: [parquet, Apache Parquet]
pitch: "Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet."
categorie: data/format
famille: specification
licence_type: open-source
maturite: production
langage: Java
alternatives: ["[[Avro]]"]
complements: ["[[dbt Core]]", "[[Airbyte]]", "[[dlt]]", "[[Delta Lake]]", "[[Apache Arrow]]"]
tags: [file-format, columnar, olap]
url_docs: https://parquet.apache.org/docs/
url_repo: https://github.com/apache/parquet-format
---

# Parquet

<!-- AUTO:BANDEAU:START -->
> Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification Java | open-source | rien à exécuter | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Format de fichier **orienté colonnes**, inspiré de Google Dremel. Une table est découpée
horizontalement en *row groups* (128 Mo à 1 Go) ; à l'intérieur, la donnée est rangée colonne
par colonne, chaque colonne portant son propre encodage (dictionnaire, RLE, delta), son codec
de compression (Snappy, Zstd, GZIP) et des statistiques min/max. De là viennent les deux
gains : un moteur ne lit que les colonnes demandées (projection pushdown) et saute les row
groups hors filtre (predicate pushdown). Les colonnes imbriquées passent par les *definition*
et *repetition levels* de Dremel. La contrepartie du modèle est l'immutabilité : mettre une
ligne à jour, c'est réécrire un fichier entier.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Scans analytiques lisant peu de colonnes sur beaucoup de lignes | Écriture ou append enregistrement par enregistrement, messages de flux → [[Avro]] |
| Stockage durable de tables sur object storage (S3, [[MinIO]] — projet archivé, voir sa fiche ; [[SeaweedFS]], [[Garage]] ou [[Ceph]] comme alternatives), lu par [[DuckDB]], [[Spark]], [[Polars]], ClickHouse | Mises à jour fréquentes de lignes, OLTP → [[Postgres]] |
| Interop colonnaire via Apache Arrow / PyArrow, en lecture quasi zéro-copie | Sémantique de table — ACID, time travel, évolution de schéma → [[Apache Iceberg]], couche posée par-dessus Parquet |
| Compression forte et requêtes sélectives sur de gros volumes | Le *small files problem* : beaucoup de petits fichiers font exploser le coût des métadonnées, prévoir une compaction |
| | Taille de row group à régler selon le moteur et le stockage ; schéma à tenir cohérent entre les fichiers d'un même jeu, et rien n'est lisible à l'œil |

## Mise en œuvre

- Installation — bibliothèques de lecture / écriture : Arrow et PyArrow (`uv add pyarrow`), parquet-java, fastparquet
- Point d'entrée — l'API du moteur ou de la bibliothèque ; il n'y a aucun service à appeler
- Prérequis — un système de fichiers ou un stockage objet, rien d'autre
- Exécution — dans le process du moteur ; format splittable, un row group par tâche côté distribué
- Coût — gratuit, Apache-2.0 ; le coût réel est celui du stockage et des requêtes

## Écosystème

### Alternatives

- [[Avro]] — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.

### Compléments

- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — dbt-duckdb écrit du Parquet par la matérialisation `external` (`format: parquet`) et dbt-spark le prend comme `file_format`.
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — la destination S3 écrit des fichiers Parquet.
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0). — format d'écriture de la destination `filesystem`, à côté de JSONL (défaut) et CSV.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — les fichiers de données d'une table Delta sont du Parquet ; le journal `_delta_log` décrit l'état de la table, il ne remplace pas le format.
- [[Apache Arrow]] — Format colonnaire en mémoire et bibliothèques multi-langages pour échanger des données entre moteurs sans copie ni conversion : spécification, IPC, Flight, C++ et pyarrow (Apache-2.0). — pyarrow lit et écrit le Parquet vers des structures Arrow en mémoire.

## Ressources

- Documentation — https://parquet.apache.org/docs/
- Dépôt — https://github.com/apache/parquet-format

## Voir aussi

- [[Partitionnement & layout de données]] — le data skipping que les statistiques par row group rendent possible
- [[Architecture médaillon]] — les couches de tables qui reposent sur ces fichiers
