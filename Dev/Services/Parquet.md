---
galaxie: dev
type: service
nom: Parquet
alias: [parquet, Apache Parquet]
pitch: "Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet."
categorie: data/format
licence_type: open-source
hosted: self
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Dev/Services/Avro|Avro]]"]
remplace_par: []
status: actif
tags: [file-format, columnar, olap]
url_docs: https://parquet.apache.org/docs/
url_repo: https://github.com/apache/parquet-format
---

# Parquet

## Pourquoi

Apache Parquet est un format de fichier **orienté colonnes**, inspiré de Google Dremel. Une table est découpée horizontalement en **row groups** (≈ 128 Mo – 1 Go) ; à l'intérieur, les données sont rangées **colonne par colonne** (column chunks). Chaque colonne porte son propre **encodage** (dictionnaire, RLE, delta) et son **codec** de compression (Snappy, Zstd, GZIP), plus des **statistiques min/max** par row group. Résultat : un moteur ne lit que les colonnes demandées (projection pushdown) et saute les row groups hors filtre (predicate pushdown). Les colonnes imbriquées sont gérées via les **definition / repetition levels** de Dremel. Apache-2.0 ; format de fait du stockage analytique.

## Quand l'utiliser

- Scans analytiques (OLAP) lisant peu de colonnes sur beaucoup de lignes.
- Stockage durable de tables sur object storage (S3, MinIO) lu par DuckDB, Spark, [[Dev/Services/Polars|Polars]], ClickHouse.
- Interop colonnaire via Apache Arrow / PyArrow (lecture quasi zéro-copie).
- Compression forte et requêtes sélectives recherchées sur de gros volumes.

## Quand NE PAS l'utiliser

- Écriture / append **enregistrement par enregistrement** ou messages de flux → [[Dev/Services/Avro|Avro]] (orienté ligne).
- Mises à jour fréquentes de lignes / OLTP → base relationnelle ([[Dev/Services/Postgres|Postgres]]).
- Besoin de **sémantique de table** (ACID, time travel, évolution de schéma au niveau table) → [[Dev/Services/Apache Iceberg|Apache Iceberg]] (couche table par-dessus Parquet).

## Déploiement & coût

- Ce n'est pas un service mais un **format ouvert** + des bibliothèques : Arrow / PyArrow, parquet-java, fastparquet. Gratuit (Apache-2.0).
- Les fichiers vivent sur object storage ou système de fichiers ; rien à héberger.
- **Splittable** : conçu pour les moteurs distribués (un row group par tâche).

## Pièges

- Fichiers immuables : une mise à jour impose de **réécrire** des fichiers entiers.
- Le « small files problem » : trop de petits fichiers → surcoût de métadonnées, prévoir une compaction.
- Taille de row group à régler selon le moteur et le stockage.
- Non lisible à l'œil ; le schéma doit rester cohérent entre fichiers d'un même jeu.

## Alternatives

- [[Dev/Services/Avro|Avro]] — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.

## Liens

- [[Dev/Services/Apache Iceberg|Apache Iceberg]] — format de table transactionnel qui stocke ses données en Parquet.
- Format mémoire complémentaire : Apache Arrow (colonnaire en RAM) — interop directe.
- Doc : https://parquet.apache.org/docs/
