---
role: brique
nom: Delta Lake
alias: [delta lake, Delta, delta-rs, deltalake]
pitch: "Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source."
categorie: data/format
famille: specification
licence_type: open-source
maturite: production
langage: Scala
alternatives: ["[[Apache Iceberg]]"]
complements: ["[[Parquet]]", "[[Spark]]", "[[Flink]]", "[[DuckDB]]", "[[MinIO]]", "[[lakeFS]]"]
tags: [lakehouse, file-format, schema-evolution, data-versioning]
url_docs: https://docs.delta.io/
url_repo: https://github.com/delta-io/delta
---

# Delta Lake

<!-- AUTO:BANDEAU:START -->
> Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification Scala | open-source | rien à exécuter | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Format de **table** ouvert, pas un format de fichier : les données restent dans des fichiers Parquet, et
un dossier `_delta_log` tient le **journal de transactions**. Chaque commit écrit un fichier de journal
numéroté qui ajoute ou retire des fichiers ; l'état de la table à la version N est la somme des entrées
jusqu'à N, avec des points de contrôle (checkpoints) pour ne pas tout relire. De ce journal viennent les
transactions ACID par concurrence optimiste (un conflit lève une exception), le **time travel**
(`VERSION AS OF`, `TIMESTAMP AS OF`, `DESCRIBE HISTORY`, `RESTORE`), `MERGE`, `UPDATE` et `DELETE`,
l'évolution de schéma et le **Change Data Feed** (les lignes insérées, modifiées et supprimées entre deux
versions). Le protocole est publié (`PROTOCOL.md`) et a plusieurs implémentations : Scala pour Spark,
Rust pour `delta-rs` (le paquet Python `deltalake`, sans JVM), et **Delta Kernel** (Java et Rust) pour
écrire des connecteurs sans réimplémenter le protocole.

Relevé le 2026-09-30 : **Delta 4.4.0** du 2026-08-20 (9 000 étoiles, dernier commit le 2026-09-30),
`deltalake` (delta-rs) **1.6.6** du 2026-09-24 et crate Rust **rust-v1.0.0** du 2026-09-28 (3 300
étoiles), Apache-2.0 pour les deux dépôts.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un lakehouse déjà construit sur Spark ou Databricks, où le format de table est en place | Plusieurs moteurs en lecture et en écriture sur les mêmes tables, sans lien avec un éditeur → [[Apache Iceberg]], dont la fiche liste plusieurs catalogues (REST, Glue, Hive Metastore, Nessie, Polaris) |
| Lire et écrire des tables sans JVM, depuis Python ou Rust (`deltalake`), ou depuis [[DuckDB]] et Polars | Plusieurs écrivains sur un stockage S3 sans mécanisme de verrou : le mode par défaut n'admet qu'un seul driver Spark, plusieurs peuvent « provoquer des pertes de données » d'après la documentation |
| Des mises à jour ligne à ligne et un flux de modifications (`MERGE`, Change Data Feed) sur des tables analytiques | Conserver un état daté plusieurs mois : `VACUUM` efface les fichiers après 7 jours par défaut, le journal est nettoyé après 30 jours, et `RESTORE` échoue sur un fichier supprimé → un jeu figé par [[DVC]] ou [[lakeFS]] |
| Un retour à une version antérieure d'une table sans copie (`RESTORE`) | Les optimisations propres à Databricks : l'optimisation prédictive (OPTIMIZE, VACUUM, ANALYZE automatiques) n'existe que sur sa plateforme, et toutes les fonctions Delta ne sont pas dans toutes les versions de son environnement |
| | Un simple fichier, sans sémantique de table → [[Parquet]] seul |

## Mise en œuvre

- Installation — `pip install delta-spark` (Spark) ou `pip install deltalake` (sans JVM) ; Python 3.10 ou plus pour les deux ; la crate `deltalake` pour Rust
- Point d'entrée — aucune API propre côté serveur : un moteur lit et écrit les tables — [[Spark]] en natif, [[Flink]] en lecture et écriture (connecteur annoncé expérimental dans les notes de la 4.4.0), Trino, Hive et d'autres en lecture, [[DuckDB]] par son extension `delta`, pandas, Polars et DataFusion par `delta-rs`
- Prérequis — un stockage : S3, ADLS, GCS, HDFS, système de fichiers local, avec trois garanties (écriture visible atomiquement, exclusion mutuelle, listage cohérent). Sur S3, le mode par défaut de Delta Spark exige **un seul driver d'écriture** ; le mode multi-cluster passe par une table DynamoDB (`S3DynamoDBLogStore`, décrit comme expérimental). `delta-rs` s'appuie sur les écritures conditionnelles de S3 : avec MinIO, `aws_conditional_put: 'etag'`
- Exécution — rien à héberger en propre : le calcul est celui du moteur, le stockage celui du fichier ou de l'objet
- Coût — gratuit ; `VACUUM` et `OPTIMIZE` sont une maintenance à planifier

## Licence et gouvernance

- **Apache-2.0** : `delta-io/delta` (copyright « The Delta Lake Project Authors ») et `delta-rs`. Aucune clause restrictive relevée.
- **Linux Foundation depuis le 2019-10-16.** Le guide de contribution se dit projet indépendant, non contrôlé par une seule entreprise ; Databricks, créateur du projet, continue d'y contribuer activement. La part exacte de ses employés parmi les mainteneurs n'est pas établie : aucune liste de mainteneurs publiée n'a été trouvée.
- **Ce qui est propre à Databricks**, d'après sa propre documentation : l'optimisation prédictive, qui exige des tables gérées par Unity Catalog, et des fonctions qui dépendent de la version de son environnement. L'open source porte OPTIMIZE, Z-ORDER, l'auto-compaction, le data skipping, le liquid clustering, les deletion vectors et le Change Data Feed.
- **Écart entre protocole et implémentations** : le protocole décrit des fonctions que tous les clients n'implémentent pas ; `delta-rs` publie une table de prise en charge (les colonnes d'identité, par exemple, n'y figurent pas). Les **tables gérées par catalogue** (Delta 4.0.1 et suivantes) exigent un catalogue compatible comme Unity Catalog : l'accès par chemin de fichier n'y est plus pris en charge.
- **Désaccord entre sources** : les notes de `rust-v1.0.0` de delta-rs annoncent la suppression du verrou DynamoDB devenu inutile grâce aux écritures conditionnelles de S3, alors que la page de documentation S3 de la branche principale le présente encore comme le mécanisme d'exclusion. Probable retard de documentation.

## Limites à connaître

- **Historique borné** : 30 jours de journal et 7 jours de fichiers conservés par défaut ; le time travel par horodatage dépend du fichier de journal, donc copier une table peut le casser.
- **Compatibilité ascendante** : activer certaines fonctions (deletion vectors, mappage de colonnes) rend la table illisible par un client plus ancien.
- **UniForm est en lecture seule côté Iceberg** : il génère les métadonnées Iceberg d'une table Delta, de manière asynchrone, avec des versions qui ne s'alignent pas ; une écriture externe peut détruire la table Delta. La documentation de cette fonction impose encore le Hive Metastore, et peut être en retard sur Unity Catalog.
- **La convergence avec Iceberg est au stade des propositions** : deux RFC du dépôt (`iceberg-compat-v3`, `iceberg-v4-metadata`) sont « proposées » ; une adoption annoncée de la spécification V4 d'Iceberg par Delta 5.0 n'est attestée que par des sessions de conférence de Databricks, pas par la documentation de Delta.

## Écosystème

### Alternatives

- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — le même besoin de table transactionnelle sur Parquet : Delta naît autour de Spark et de Databricks, Iceberg se branche sur plusieurs catalogues (REST, Glue, Hive Metastore, Nessie, Polaris) ; UniForm rend une table Delta lisible comme une table Iceberg.

### Compléments

- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet. — format des fichiers de données d'une table Delta ; le journal ne remplace pas Parquet, il le pilote.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — moteur natif de Delta : lecture et écriture complètes, `MERGE`, Change Data Feed.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch. — connecteur de lecture et d'écriture listé par la documentation de Delta ; les notes de la 4.4.0 le disent expérimental.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — extension `delta` fondée sur `delta-kernel-rs` : lecture, et écriture limitée à des ajouts d'enregistrements.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire. — stockage S3-compatible que la documentation de delta-rs décrit avec `aws_conditional_put`, et que Delta cite parmi ses intégrations communautaires ; la brique est non maintenue.
- [[lakeFS]] — Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur. — versionne le dépôt d'objets qui contient les fichiers Delta : une branche entière de tables, là où Delta ne versionne qu'une table.

## Ressources

- Documentation — https://docs.delta.io/
- Documentation — https://github.com/delta-io/delta/blob/master/PROTOCOL.md
- Dépôt — https://github.com/delta-io/delta
- Dépôt — https://github.com/delta-io/delta-rs

## Voir aussi

- [[Formats de fichiers et de tables]] — le hub du dossier
- [[Partitionnement & layout de données]] — le partitionnement et la compaction que ce format automatise
- [[Versionnage de données]] — la notion : le time travel d'un format de table, face au versionnage de fichiers ou de dépôt
- [[Comparatif - Versionnage de données]] — ce qui départage Delta Lake, Apache Iceberg, DVC et lakeFS
