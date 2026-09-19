---
role: brique
nom: Airbyte
alias: [airbyte, Airbyte Core, Airbyte Open Source, abctl]
pitch: "Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes."
categorie: data/ingestion
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: "Java, Kotlin, Python"
scaling: distributed
alternatives: ["[[dlt]]", "[[Apache NiFi]]", "[[Debezium]]"]
complements: ["[[Airflow]]", "[[Dagster]]", "[[Kestra]]", "[[Postgres]]", "[[MySQL]]", "[[Microsoft SQL Server]]", "[[MongoDB]]", "[[ClickHouse]]", "[[DuckDB]]", "[[Apache Iceberg]]", "[[Parquet]]"]
tags: [data-ingestion, data-pipeline, cdc, self-hosted]
url_docs: https://docs.airbyte.com/
url_repo: https://github.com/airbytehq/airbyte
---

# Airbyte

<!-- AUTO:BANDEAU:START -->
> Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java, Kotlin, Python | source-available | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme qui déplace des données d'une **source** (API, base, fichier) vers une **destination**
(entrepôt, lac, base) par des connecteurs standardisés, configurés dans une interface, par API ou
par Terraform. Chaque flux (*stream*) se synchronise en full refresh ou en incrémental, par curseur
ou par CDC ; le catalogue annonce plus de 600 connecteurs, dont un Connector Builder pour écrire
les manquants.

Relevé le 2026-09-30 : notes de version **2.3** du 2026-09-15 (le dernier tag publié sur GitHub est
`v2.0.0`, du 2025-10-15), environ 22 150 étoiles, dernier commit du jour. La licence, restrictive,
est détaillée plus bas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Beaucoup de sources hétérogènes (API SaaS, bases, fichiers) à charger sans écrire un connecteur par source | Une cible restreinte à quelques sources maison : [[dlt]] suffit, en simple bibliothèque Python |
| Une interface et une API pour configurer et suivre les synchronisations, sans code de pipeline | Aucun cluster Kubernetes disponible : Docker Compose n'est plus supporté, `abctl` en embarque un local |
| Capturer les changements de Postgres, MySQL, SQL Server ou MongoDB sans monter [[Debezium]] soi-même | Fournir Airbyte à des tiers comme service géré : l'ELv2 l'interdit |
| Écrire ses propres connecteurs en low-code (Connector Builder, CDK Python en MIT) | Des flux industriels (MQTT, syslog, SFTP, routage) : [[Apache NiFi]] est fait pour eux |
| | SSO, RBAC, plusieurs espaces de travail ou connecteurs « enterprise » (Oracle) : réservés aux offres payantes |

## Mise en œuvre

- Installation — `abctl local install` (crée un cluster Kubernetes local dans Docker) ou chart Helm, recommandé en production ; Docker Compose est abandonné depuis 2024
- Point d'entrée — l'interface web, l'API Airbyte ou le fournisseur Terraform ; une *connection* relie une source, une destination et un mode de synchronisation par flux
- Prérequis — Kubernetes, 4 CPU et 8 Go recommandés (2 CPU et 8 Go en `--low-resource-mode`, sans Connector Builder) d'après le quickstart ; une destination joignable (Postgres, ClickHouse, S3/MinIO…). Aucune page de connecteur lue ne demande un broker Kafka
- Exécution — auto-hébergé, distribué ; la version 2.3 impose une manipulation manuelle du MinIO embarqué avant la mise à jour
- Coût — gratuit en auto-hébergé sous ELv2 ; Cloud et offres payantes (SSO à partir de Plus, RBAC et espaces multiples à partir de Pro, déploiement hybride en Enterprise Flex)

## Licence et gouvernance

- **ELv2 partout** : le fichier `LICENSE` du dépôt, `LICENSE_SHORT` (« Airbyte, Inc., all rights reserved ») et le `metadata.yaml` des connecteurs (Postgres, MySQL, SQL Server, MongoDB, ClickHouse, DuckDB, S3, S3 Data Lake) indiquent `ELv2`. La documentation ne réserve le MIT qu'au **protocole** ; `abctl` (MIT) et le CDK Python `airbyte-cdk` (MIT, 7.32.0 du 2026-09-28) sont les seuls composants ouverts que le relevé a trouvés. Les badges du README affichent MIT et ELv2 ensemble, ce qui est trompeur.
- **Ce que l'ELv2 interdit** : fournir le logiciel à des tiers comme service hébergé ou géré donnant accès à l'essentiel de ses fonctions. Installer Airbyte chez un client, pour son propre usage, est permis : c'est le cas d'une ESN.
- **Historique** : plateforme en MIT jusqu'au 2021-09-27, puis ELv2 ; les connecteurs suivent en 2023. Des billets anciens qui disent « connecteurs en MIT » sont périmés. Airbyte 2.0 a été annoncé le 2025-10-14 ; Airbyte Agents a été lancé le 2026-05-04, avec la promesse écrite que le moteur de réplication et l'open source restent. **Self-Managed Enterprise n'est plus vendu** (2.3). Aucun rachat ni changement de direction n'a été trouvé.
- **Ce que Core n'a pas** : aucune page à jour ne l'énumère. La page des offres réserve le SSO aux plans Plus, le RBAC et les espaces multiples à Pro ; le connecteur Oracle et son CDC (LogMiner) sont réservés à Pro et Flex.

## Limites à connaître

- **Kubernetes obligatoire** : « Airbyte is built to be deployed into a Kubernetes cluster ». Sur un serveur seul, `abctl` ou k3s ; le chart Helm V1 n'est plus supporté depuis la 2.1.
- **Maturité inégale des connecteurs** : le fichier `metadata.yaml` de `source-mysql` (3.53.5) et de `source-mssql` (5.0.1) indique `releaseStage: alpha` alors que leur niveau de support est `certified` ; Postgres et MongoDB sont en disponibilité générale. Côté destinations, S3 Data Lake (Iceberg) est en alpha, DuckDB en bêta communautaire.
- **CDC** : seul le mode CDC voit les suppressions. Postgres exige un slot de réplication `pgoutput` ; si `max_slot_wal_keep_size` est dépassé, le slot peut être invalidé.

## Écosystème

### Alternatives

- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0).
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker.
- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — pour la seule capture des changements d'une base, Debezium se déploie sans le reste d'Airbyte ; Airbyte embarque de son côté Debezium pour la capture SQL Server d'après le journal de son connecteur.

### Compléments

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le fournisseur `apache-airflow-providers-airbyte` (6.1.0, 2026-09-29) déclenche et surveille les synchronisations.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés. — `dagster-airbyte` (0.29.24, 2026-09-21) charge les connexions Airbyte comme assets Dagster.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — Kestra publie un plugin Airbyte pour déclencher des synchronisations.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — source GA (`source-postgres` 3.8.5) en curseur, en `xmin` ou en CDC par slot `pgoutput` ; destination GA.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — source avec CDC par le binlog (`binlog_format = ROW`), marquée alpha dans son `metadata.yaml`.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche. — source avec CDC (SQL Server 2016 SP1 ou plus, Debezium), marquée alpha.
- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding. — source GA (`source-mongodb-v2`) qui lit les change streams.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — destination certifiée en disponibilité générale.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — destination communautaire en bêta (`destination-duckdb` 0.6.0).
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — destination « S3 Data Lake », certifiée mais en alpha.
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet. — la destination S3 écrit des fichiers Parquet.

## Ressources

- Documentation — https://docs.airbyte.com/
- Dépôt — https://github.com/airbytehq/airbyte

## Voir aussi

- [[Ingestion de données]] — le hub du dossier
- [[Comparatif - Ingestion de données]] — ce qui départage Airbyte, dlt, Debezium et Apache NiFi
- [[Ingestion incrémentale et curseurs]] — ce que veulent dire les modes de synchronisation
- [[Change Data Capture (CDC)]] — le principe derrière les modes CDC
- [[MinIO]] — destination S3 : la doc de la destination accepte un point d'accès MinIO, et le déploiement embarque son propre MinIO ; le dépôt MinIO est archivé
- [[dbt Core]] et [[SQLMesh]] — la transformation qui suit le chargement
