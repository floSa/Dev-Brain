---
role: hub
nom: Ingestion de données
alias: [ingestion, extract-load, EL]
pitch: Amener la donnée d'une source — base, API, fichier, journal — jusqu'à sa destination, sans la remodeler, et savoir la recharger sans tout relire.
domaines: [data-eng]
tags: [data-ingestion, data-pipeline, cdc, logging]
---

# Ingestion de données

> Amener la donnée d'une source — base, API, fichier, journal — jusqu'à sa destination, sans la remodeler, et savoir la recharger sans tout relire.

## Ce qu'il faut comprendre

- Ce dossier porte le **E et le L** de l'[[ELT vs ETL & idempotence|ELT]] : lire une source, écrire une destination. Ce qui vient après (dériver des tables) est de la transformation, cf. [[Comparatif - Transformation SQL]] ; ce qui planifie et relance est de l'[[Orchestration]] ; ce qui juge la donnée chargée est de la [[Fiabilité des données]].
- **Quatre outils, quatre réponses à « qu'est-ce qu'on déplace ? »** : [[Airbyte]] déplace des sources vers des entrepôts par un catalogue de connecteurs ; [[dlt]] le fait par du code Python sans serveur ; [[Debezium]] ne déplace que les *changements* d'une base, lus dans son journal ; [[Apache NiFi]] achemine et route des flux de toute nature. Le détail est dans [[Comparatif - Ingestion de données]].
- **La licence n'est pas la même partout, et la plus restrictive est celle du plus répandu** : [[Airbyte]] est sous Elastic License 2.0 (source-available : utilisable chez un client, interdit comme service géré), [[dlt]] est en Apache-2.0 avec une extension commerciale à côté, [[Debezium]] et [[Apache NiFi]] sont en Apache-2.0 sans édition payante dans le dépôt.
- **Un broker n'est pas toujours requis** : seul [[Debezium]] en mode Kafka Connect exige Kafka ; Debezium Server, [[Airbyte]], [[dlt]] et [[Apache NiFi]] s'en passent. Les brokers eux-mêmes ne sont pas fichés ici.
- Le rechargement se juge sur ce que le curseur **ne voit pas** : suppressions, lignes tardives, reprise après échec. C'est l'objet de [[Ingestion incrémentale et curseurs]] ; la lecture du journal, qui règle les suppressions, est celui de [[Change Data Capture (CDC)]].
- **Deux autres familles cohabitent ici** : la collecte de logs et de métriques ([[Beats]] en agents, [[Logstash]] en pipeline, vers la pile Elastic), et le chargement d'un résultat SQL vers un DataFrame ([[connectorx]]).

## Choisir

- Charger beaucoup de sources API et bases vers un entrepôt, avec interface et catalogue → [[Airbyte]] (licence à lire avant de redistribuer).
- Charger des sources maison en Python, sans serveur → [[dlt]].
- Répliquer une base sans la recharger, suppressions comprises → [[Debezium]].
- Acheminer et router des flux de fichiers, MQTT, syslog, JDBC, avec provenance → [[Apache NiFi]].
- Collecter des logs sur des machines vers Elasticsearch → [[Beats]] puis [[Logstash]].
- Lire une table SQL vers un DataFrame → [[connectorx]].
- Comprendre pourquoi un rechargement rate des lignes → [[Ingestion incrémentale et curseurs]].
- Transformer ce qui vient d'être chargé → [[dbt Core]] ou [[SQLMesh]].

<!-- AUTO:START -->
### Notions
- [[Change Data Capture (CDC)]] — domaines : data-eng
- [[Ingestion incrémentale et curseurs]] — domaines : data-eng

### Briques
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes.
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker.
- [[Beats]] — Agents de collecte légers en Go (Apache-2.0, x-pack sous Elastic License) — Filebeat, Metricbeat, Auditbeat… expédient logs et métriques vers Elasticsearch ou Logstash.
- [[connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.
- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0).
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0).
- [[Logstash]] — Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire.

### Comparatifs
- [[Comparatif - Ingestion de données]]
<!-- AUTO:END -->
