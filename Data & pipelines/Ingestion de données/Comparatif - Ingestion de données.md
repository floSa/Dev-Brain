---
role: comparatif
nom: Comparatif - Ingestion de données
categorie: data/ingestion
tags: [data-ingestion, data-pipeline]
---

# Comparatif - Ingestion de données

> On tranche sur : le modèle (code ou interface), l'étendue du catalogue de sources, l'incrémental et le CDC, le besoin d'un broker, le poids d'exploitation sur site, et la licence — dont une, ici, est restrictive.

![[Comparatif - Ingestion de données.base]]

## Ce qui départage

- [[Airbyte]] — le **catalogue** : plus de 600 connecteurs, une interface, une API et un Connector Builder, des modes de synchronisation par flux, du CDC pour Postgres, MySQL, SQL Server et MongoDB sans broker. Le prix : **Elastic License 2.0** sur le dépôt comme sur les connecteurs (source-available, pas de service géré pour des tiers), Kubernetes obligatoire, des connecteurs MySQL et SQL Server encore marqués alpha, et un SSO, un RBAC et un connecteur Oracle réservés aux offres payantes.
- [[dlt]] — la **bibliothèque** : des sources écrites en Python, un état rangé dans la destination, aucun serveur, Apache-2.0. Le prix : tout est du code, il n'y a ni interface ni ordonnanceur, le CDC libre se limite à Postgres, et dltHub — Iceberg, Delta, source MS SQL, contrôles de qualité — est une extension à licence commerciale.
- [[Debezium]] — la **capture de changements** et rien d'autre : le journal des bases, un événement avant/après par ligne, Apache-2.0. Le prix : il ne charge pas de destination à lui seul, demande Kafka en mode Kafka Connect (ou Debezium Server sans broker), et livre au moins une fois.
- [[Apache NiFi]] — le **flux** : une interface de flux, des centaines de processeurs (SFTP, MQTT, JMS, syslog, JDBC, Kafka), provenance et contre-pression, Apache-2.0, sans broker. Le prix : une JVM (Java 21) et un cluster à exploiter, du CDC pour MySQL seulement, aucun processeur OPC UA ni Modbus, et rien pour construire des tables dérivées.

**Critère par critère**

**Modèle.** [[Airbyte]] : une interface, une API et Terraform ; les connecteurs se configurent ou s'écrivent en low-code. [[dlt]] : du Python ; la définition du pipeline est un script versionné. [[Debezium]] : un fichier de propriétés ou un JSON de connecteur, sans logique de flux propre. [[Apache NiFi]] : un canevas graphique, les flux se versionnent par un registre (GitHub, GitLab, Bitbucket, NiFi Registry).

**Connecteurs.** [[Airbyte]] : plus de 600 annoncés, niveaux Airbyte, Enterprise, Marketplace (communauté, sans SLA) et Custom. [[dlt]] : REST, bases SQL par SQLAlchemy, fichiers, et une liste de sources vérifiées ; le reste s'écrit. [[Debezium]] : huit connecteurs stables, tous de bases (MongoDB, MariaDB, MySQL, PostgreSQL, SQL Server, Oracle, Db2, Cassandra). [[Apache NiFi]] : des centaines de processeurs génériques, orientés protocoles et fichiers.

**Incrémental.** [[Airbyte]] : cinq combinaisons lecture/écriture, curseur ou CDC, dédoublonnage par clé primaire. [[dlt]] : `dlt.sources.incremental`, fenêtre `lag`, `end_value` pour les backfills, fusion `delete-insert`, `upsert`, `scd2`. [[Debezium]] : offsets et snapshots incrémentaux à marques. [[Apache NiFi]] : colonnes à valeur maximale (`QueryDatabaseTable`) conservées dans l'état. Le principe est dans [[Ingestion incrémentale et curseurs]].

**CDC.** [[Debezium]] : le plus large (huit bases stables). [[Airbyte]] : Postgres (`pgoutput`), MySQL (binlog), SQL Server (Debezium) et MongoDB. [[dlt]] : la source `pg_replication` seulement, sans `scd2` ; MS SQL en dltHub. [[Apache NiFi]] : `CaptureChangeMySQL`. Cf. [[Change Data Capture (CDC)]].

**Broker.** [[Debezium]] : **oui** en mode Kafka Connect ; non avec Debezium Server (Redis, NATS, RabbitMQ, HTTP, JDBC…) ou Debezium Engine. [[Airbyte]], [[dlt]] et [[Apache NiFi]] : non ; NiFi sait en revanche produire vers Kafka ou MQTT et en consommer.

**Exploitation sur site.** [[Airbyte]] : Kubernetes obligatoire (`abctl` en embarque un local, Helm en production), 4 CPU et 8 Go recommandés. [[dlt]] : un processus Python, rien à héberger. [[Debezium]] : un cluster Kafka avec workers Connect, ou Debezium Server seul plus la base source. [[Apache NiFi]] : une JVM Java 21 par nœud, ZooKeeper ou Kubernetes en cluster, disques rapides.

**Licence.** [[Debezium]] et [[Apache NiFi]] : Apache-2.0, sans édition payante dans le dépôt. [[dlt]] : Apache-2.0 pour le paquet, licence commerciale pour dltHub. [[Airbyte]] : **Elastic License 2.0** — utilisable chez un client d'ESN, interdite comme service géré pour des tiers ; les connecteurs suivent la même licence.

**Membres du dossier hors de la confrontation** — ils occupent la même vue, mais ne répondent pas à la même question :

- [[Beats]] et [[Logstash]] — la collecte de **logs et de métriques** vers la pile Elastic ; Logstash est aussi un pipeline de transformation, et [[Apache NiFi]] en est la contrepartie généraliste (syslog, journaux Windows). Des sources et des destinations de bases ne sont pas leur rôle.
- [[connectorx]] — lire le résultat d'une requête SQL vers un DataFrame ; ce n'est pas un pipeline, et [[dlt]] peut s'en servir comme moteur de lecture.

**Pas de fiche ici**, faute d'être éprouvé pour l'on-prem ou faute d'apporter un choix de plus :

- **Meltano** — CLI pilotée par `meltano.yml` et écosystème Singer. Relevé le 2026-09-30 : v4.4.0 du 2026-09-29, MIT, environ 2 640 étoiles, mais le projet a changé de main (Matatika a acquis Meltano, annonce du billet officiel daté du 2026-03-01 ; deux agrégateurs donnent décembre 2025), son ancienne activité commerciale (Arch) est fermée, environ 194 000 téléchargements PyPI par mois contre 4,8 M pour dlt, et le tap Postgres de Wise (`pipelinewise-tap-postgres`) est archivé depuis 2024-09-23. Vivant mais petit, et recouvert par [[dlt]] pour une approche en code.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Ingestion de données]] — le hub du dossier.
- [[Ingestion incrémentale et curseurs]] — le principe commun de l'incrémental.
- [[Change Data Capture (CDC)]] — le principe commun de la capture par le journal.
- [[Comparatif - Transformation SQL]] — l'étape suivante du flux : ce que [[dbt Core]] et [[SQLMesh]] font des données chargées.
