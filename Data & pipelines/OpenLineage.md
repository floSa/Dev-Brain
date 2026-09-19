---
role: brique
nom: OpenLineage
alias: [openlineage, Open Lineage, OpenLineage spec]
pitch: "Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data)."
categorie: data/catalogue
famille: specification
licence_type: open-source
maturite: production
alternatives: []
complements: ["[[OpenMetadata]]", "[[DataHub]]", "[[Airflow]]", "[[Dagster]]", "[[dbt Core]]", "[[Spark]]", "[[Flink]]", "[[Kafka]]", "[[Great Expectations]]"]
tags: [data-lineage, data-governance, data-pipeline]
url_docs: https://openlineage.io/docs/
url_repo: https://github.com/OpenLineage/OpenLineage
---

# OpenLineage

<!-- AUTO:BANDEAU:START -->
> Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification | open-source | rien à exécuter | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Cadre ouvert de **collecte de lignage** : une spécification, définie en OpenAPI et JSON Schema,
que les outils qui exécutent un traitement utilisent pour dire ce qu'ils ont lu et écrit. Trois
entités — **Job** (le travail), **Run** (une exécution) et **Dataset** (la donnée), nommées de
façon uniforme — et des **facettes**, métadonnées extensibles qui les enrichissent (schéma,
requête SQL, statistiques, lignage colonne). Trois types d'événements : `RunEvent`, `JobEvent`,
`DatasetEvent`. L'outil qui exécute *émet*, un récepteur — un catalogue ou un magasin de lignage —
*reçoit* : la spécification ne stocke ni n'affiche rien.

Relevé le 2026-09-30 : version **1.53.0** du 2026-09-01 (une version toutes les deux à six
semaines), schéma de la spécification **2-0-2**, environ 2 680 étoiles, Apache-2.0, projet
« Graduate » de la LF AI & Data Foundation d'après le README.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire remonter le lignage **au moment de l'exécution**, sans crawler les entrepôts : Spark, Flink, dbt, Airflow émettent tout seuls | Un inventaire consultable, un glossaire, des propriétaires : la spécification ne les fournit pas → [[OpenMetadata]] ou [[DataHub]] |
| Un standard commun entre outils et catalogues, pour ne pas écrire un connecteur par couple | Un lignage colonne garanti : peu d'intégrations l'émettent, et surtout Spark et dbt |
| Un catalogue qui sait recevoir des événements OpenLineage, aujourd'hui ou plus tard | Un orchestrateur sans intégration maintenue : Prefect et Kestra n'ont aucune page dans la documentation lue |
| Garder les événements dans Kafka ou un fichier, et les rejouer vers un récepteur | Une intégration Dagster officielle : elle est communautaire (voir plus bas) |

## Mise en œuvre

- Installation — `openlineage-python` (1.53.0 sur PyPI, Python 3.10 ou plus), le client Java, le client Go ; chaque intégration est un paquet ou un JAR à part
- Point d'entrée — un écouteur ou un remplaçant de la commande : `spark.extraListeners` avec `OpenLineageSparkListener` pour Spark, `dbt-ol` en remplacement direct de `dbt`, le fournisseur `apache-airflow-providers-openlineage` pour Airflow
- Prérequis — un récepteur des événements : un catalogue ([[OpenMetadata]], [[DataHub]]) ou tout service qui accepte le protocole ; le client sait émettre en HTTP, sur Kafka (extra `kafka`), vers un fichier ou la console
- Exécution — aucune : la spécification et ses clients ne s'hébergent pas ; le coût est côté récepteur
- Coût — gratuit ; le prix est l'écart de maturité entre intégrations

## Licence et gouvernance

- **Apache-2.0**, dépôt non archivé, aucun changement de licence ni rachat relevé.
- **Gouvernance** : la documentation le présente comme un projet « Graduate » de la LF AI & Data Foundation. Aucune édition payante : les fonctions commerciales sont chez les récepteurs.
- **Marquez** — projet de la même fondation, autre récepteur du protocole, qui n'a pas de fiche ici. Relevé le 2026-09-30 : dernière version taguée **0.51.1** du 2025-03-27, dernière GitHub Release **0.50.0** du 2024-10-24, environ 2 280 étoiles, Apache-2.0, et cinq commits en douze mois dont les deux derniers montent React (2026-04-12). Aucun abandon annoncé, mais une activité quasi nulle : voir le comparatif.

## Limites à connaître

- **Des intégrations inégales** : les paquets du dépôt (Spark, Flink, dbt, Hive, SQL) sont maintenus avec le projet ; **Airflow** l'est côté Airflow ; **Dagster** ne l'est que par la communauté ; **Trino** émet par un plugin livré avec Trino.
- **Airflow a changé** : le paquet historique `openlineage-airflow` n'est plus maintenu ni corrigé (dernière version 1.41, Airflow < 2.7) ; le fournisseur actuel (2.20.2 du 2026-09-29) exige Airflow 2.11.0 ou plus et `openlineage-python` 1.52.0 ou plus, et gère l'interface d'écouteur d'Airflow 3 depuis la 2.1.0.
- **Flink en deux mondes** : Flink 1.x passe par un `JobListener` et demande de modifier le code, sans Flink SQL ; Flink 2.x utilise les interfaces natives (FLIP-314), sans changer le code et avec Flink SQL.
- **Un opérateur « boîte noire » reste opaque** : un `PythonOperator` n'expose pas ses jeux de données, sauf appel d'un crochet géré ; un opérateur non géré apparaît dans le graphe sans détail.
- **Lignage colonne** : la facette `ColumnLineageDatasetFacet` (1-2-0) distingue les dépendances directes (identité, transformation, agrégation) des indirectes (jointure, filtre, tri, fenêtre) ; côté dbt il faut activer l'analyse, côté Airflow la documentation n'en dit qu'un mot.
- **Récepteurs différents** : [[DataHub]] accepte les événements en HTTP ; [[OpenMetadata]] les lit sur Kafka ou Kinesis, en bêta, et annonce l'intégration « jusqu'à la 1.7.0 ».

## Écosystème

### Alternatives

- Aucun autre standard de lignage dans le brain. **Marquez** (LF AI & Data) reçoit ses événements mais n'est pas une alternative : c'est un récepteur, écarté du brain pour cause d'activité quasi nulle.

### Compléments

- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — récepteur : un connecteur lit les événements sur Kafka ou Kinesis, en bêta, annoncé intégré jusqu'à la 1.7.0.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — récepteur en HTTP sur GMS, avec un plugin Spark dédié.
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le fournisseur `apache-airflow-providers-openlineage` (2.20.2, 2026-09-29) vit dans l'écosystème Airflow et exige Airflow 2.11.0 ou plus.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés. — `dagster-openlineage` 0.2.1 (2026-05-22), maintenu par la communauté, Dagster 1.11.6 ou plus : facettes de schéma, de lignage colonne et de qualité ; l'ancien `openlineage-dagster` reste bloqué sur Dagster 1.6.9 ou moins.
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — `dbt-ol` (1.53.0), remplaçant direct de `dbt`, en mode artefacts ou journaux structurés ; lignage colonne si l'analyse est activée.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — écouteur `OpenLineageSparkListener` ; la documentation contient une section de lignage colonne.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch. — deux implémentations : Flink 1.x avec modification du code, Flink 2.x par les interfaces natives.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — transport d'événements côté client, et canal de réception du connecteur d'OpenMetadata.
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026. — intégration listée par la documentation d'OpenLineage, par la liste d'actions d'un checkpoint ; version et maintenance non relevées.

## Ressources

- Documentation — https://openlineage.io/docs/
- Dépôt — https://github.com/OpenLineage/OpenLineage

## Voir aussi

- [[Data & pipelines]] — le hub du dossier
