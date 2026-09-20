---
role: brique
nom: Apache NiFi
alias: [NiFi, MiNiFi]
pitch: "Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker."
categorie: data/ingestion
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Airbyte]]", "[[dlt]]", "[[Logstash]]"]
complements: ["[[Postgres]]", "[[MySQL]]", "[[Apache Iceberg]]", "[[OpenMetadata]]", "[[DataHub]]"]
tags: [data-ingestion, data-pipeline, low-code, self-hosted]
url_docs: https://nifi.apache.org/nifi-docs/
url_repo: https://github.com/apache/nifi
---

# Apache NiFi

<!-- AUTO:BANDEAU:START -->
> Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme qui achemine, route et transforme des flux de données. On dessine le flux dans une
interface web : des **processeurs** (lire un fichier, interroger une base, écouter un port,
publier ailleurs) reliés par des **connexions** qui sont des files persistantes, avec
contre-pression quand une file se remplit. Chaque donnée (*FlowFile*) est suivie de bout en bout par
la **provenance**, et la livraison est garantie par des dépôts sur le disque local. Un agent léger,
**MiNiFi**, sert à la périphérie. Aucun broker n'est nécessaire.

Relevé le 2026-09-30 : **2.12.0** du 2026-09-13, Apache-2.0, environ 6 240 étoiles, dernier commit du
jour, une version mineure environ chaque mois. Java 21 est requis. La branche 1.x est hors support
depuis le 2024-12-08 (1.28.1 est la dernière).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des flux hétérogènes à acheminer et à router : SFTP, MQTT, JMS, syslog, journaux Windows, JDBC, Kafka, S3, HDFS | Charger des API SaaS vers un entrepôt avec un catalogue de connecteurs prêts : [[Airbyte]] |
| Un pilotage à l'écran, avec provenance, rejeu et contre-pression, par des exploitants qui n'écrivent pas de code | Des pipelines définis en code, testés en CI : [[dlt]] |
| Un site isolé : rien à louer, gouvernance Apache, TLS, LDAP, OIDC et SAML documentés | Un petit volume et une petite machine : une JVM et un cluster ZooKeeper ou Kubernetes pèsent lourd |
| Des transformations d'enregistrements et du routage à l'ingestion, à l'échelle d'un cluster | Le CDC d'une base autre que MySQL : `CaptureChangeMySQL` est le seul processeur CDC |
| | OPC UA ou Modbus natifs : aucun processeur de ce nom sur la page des composants 2.x |

## Mise en œuvre

- Installation — archive binaire ou image Docker ; Java 21 ; processeurs Python (bêta) avec Python 3.10 à 3.12
- Point d'entrée — l'interface web (canevas de flux) ; les flux se versionnent par des clients de registre de flux (GitHub, GitLab, Bitbucket ou NiFi Registry)
- Prérequis — une JVM ; en cluster, ZooKeeper ou l'état dans des ConfigMap Kubernetes. Aucune valeur de RAM n'est publiée : le guide d'administration ne parle que du débit disque (environ 50 Mo/s sur des disques modestes)
- Exécution — auto-hébergé, distribué en cluster ; MiNiFi en agent (Java 2.12.0, C++ 1.0.0 du 2026-08-19)
- Coût — gratuit sous Apache-2.0 ; le coût réel est l'exploitation d'une JVM, de disques rapides et d'une équipe qui connaît l'outil. Cloudera commercialise des distributions fondées sur NiFi 2

## Licence et gouvernance

- **Apache-2.0**, projet de l'Apache Software Foundation. Aucune fonction n'est réservée à une édition payante dans le dépôt.
- **NiFi 2.0** (2024-11-04) a retiré des composants (HBase, Kudu, ListenBeats, ListenRELP, ListenSMTP…) et exige Java 21 ; il apporte une API Python pour écrire des processeurs et l'exécution *stateless* d'un groupe.
- Le développement est mené par quelques contributeurs très actifs, dont des membres du PMC associés à Cloudera d'après une recherche web : l'employeur de chacun n'a pas été vérifié.

## Limites à connaître

- **Incrémental par colonne** : `QueryDatabaseTable` et `GenerateTableFetch` retiennent la valeur maximale des colonnes désignées, dans l'état du processeur (portée cluster), et ne renvoient que les lignes plus grandes. Ils ne voient pas les suppressions ni les mises à jour sans horodatage.
- **CDC : MySQL seulement** — `CaptureChangeMySQL` émet insert, update et delete, ordonnés dans le temps ; rien pour Postgres, Oracle ou SQL Server.
- **Protocoles industriels** : aucun processeur OPC UA ni Modbus sur la page des composants ; MQTT existe (`ConsumeMQTT`). Un NAR tiers n'a pas été recherché.
- **Registre autonome** : NiFi Registry 1.28.1 est hors support comme la 1.x ; la page des composants 2.x liste des clients de registre de flux pour GitHub, GitLab et Bitbucket, à côté de celui de NiFi Registry.
- **Pas de transformation par modèles** : le flux transforme des enregistrements, il ne construit pas de tables dérivées ; c'est le rôle de [[dbt Core]] ou [[SQLMesh]] après le chargement.

## Écosystème

### Alternatives

- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes.
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0).
- [[Logstash]] — Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — lu et écrit par les processeurs JDBC (`ExecuteSQL`, `QueryDatabaseTable`, `PutDatabaseRecord`).
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — seule base dont le journal est lu par un processeur CDC (`CaptureChangeMySQL`).
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — destination par le processeur `PutIcebergRecord`.
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — connecteur de pipeline listé.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — source listée en GA.

## Ressources

- Documentation — https://nifi.apache.org/nifi-docs/
- Dépôt — https://github.com/apache/nifi

## Voir aussi

- [[Ingestion de données]] — le hub du dossier
- [[Comparatif - Ingestion de données]] — ce qui départage Apache NiFi, Airbyte, dlt et Debezium
- [[Beats]] — l'autre famille d'agents de collecte en périphérie, à comparer à MiNiFi
- [[Change Data Capture (CDC)]] — le principe derrière `CaptureChangeMySQL`
