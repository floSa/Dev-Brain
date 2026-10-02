---
role: hub
nom: Data & pipelines
alias: [pipelines de données]
pitch: Amener la donnée d'où elle est jusqu'à une forme exploitable — la collecter, la mettre en forme, la faire circuler, la regarder.
domaines: [data-eng, data-sci]
tags: [data-pipeline, dataframe, web-scraping, document-parsing, dataviz, data-transformation]
---

# Data & pipelines

> Amener la donnée d'où elle est jusqu'à une forme exploitable — la collecter, la mettre en forme, la faire circuler, la regarder.

## Ce qu'il faut comprendre

- Le domaine suit la trajectoire d'une donnée, et ses dix sous-dossiers sont dix étapes de cette trajectoire : on la **collecte** ([[Scraping]], [[Parsing]]), on l'**amène** d'une source à sa destination ([[Ingestion de données]]), on la **transporte** entre services ([[Messagerie]]), on la **capte à l'atelier** par les protocoles industriels ([[Données industrielles]]), on la **manipule** ([[DataFrames]]), on la **range** sur disque ou sur stockage objet ([[Formats de fichiers et de tables]]), on **planifie** son passage ([[Orchestration]]), on **s'y fie** ([[Fiabilité des données]]), on la **regarde** ([[Visualisation]]). Ce qui reste au niveau du domaine est ce qui **traverse** ces étapes : la génération de faux, le profilage, le fil de l'eau.
- Le clivage qui structure le plus les choix est **la donnée tient-elle en mémoire**. En dessous, tout marche et [[pandas]] suffit. Au-dessus, il faut un moteur qui construise un plan avant d'exécuter ([[Polars]]) ou qui distribue ([[Flink]]) — et le code change, pas seulement la machine.
- Le **format sur disque** n'est pas un détail d'implémentation, c'est ce qui décide de la vitesse de lecture. [[Parquet]] est colonnaire, donc rapide en analytique et lent à la ligne ; [[Avro]] est en lignes, donc adapté à l'échange et aux messages ; [[Apache Iceberg]] et [[Delta Lake]] ne sont ni l'un ni l'autre — ce sont des couches de table transactionnelles **par-dessus** ces fichiers, ce qui donne au [[Architecture médaillon|lakehouse]] ce que le stockage objet ne sait pas faire : l'ACID et le time travel. Cf. [[Formats de fichiers et de tables]] et [[Partitionnement & layout de données]].
- Un pipeline se juge sur sa **rejouabilité** avant sa vitesse. Rejouer un jour manquant sans dupliquer ni décaler est la propriété qui distingue un pipeline d'un script — cf. [[ELT vs ETL & idempotence]]. C'est le fil du dossier [[Fiabilité des données]], où quatre notions, trois outils de vérification et deux outils de versionnage répondent tous à « à quoi peut-on se fier » plutôt qu'à « comment ça tourne » : l'ordre d'assemblage et l'idempotence, le découpage en couches de raffinage ([[Architecture médaillon]]), ce qu'on promet au consommateur ([[Contrats de données & qualité]]), et l'état figé qui rend un résultat reproductible ([[Versionnage de données]]). L'orchestrateur exécute ; il ne garantit rien de tout ça.
- **Transformer** et **vérifier** sont deux gestes distincts, qu'un même projet porte souvent. La transformation dérive des tables d'autres tables par des modèles versionnés : [[dbt Core]] exécute dans le moteur sans état à héberger, [[SQLMesh]] garde un état et fabrique des environnements virtuels — cf. [[Comparatif - Transformation SQL]], et [[Modélisation dimensionnelle]] pour la forme des tables produites. La vérification, elle, teste des règles connues sur un lot livré ; elle vit dans [[Fiabilité des données]]. Ni l'une ni l'autre ne planifie quoi que ce soit : c'est le rôle d'[[Orchestration]].
- **Au fil de l'eau, deux pages distinctes que le mot « streaming » confond.** [[Change Data Capture (CDC)]] *produit* le flux — il lit le journal de transactions d'une base et en sort les changements ; [[Stream processing]] le *consomme* — fenêtrage, event-time, watermarks, exactly-once. L'un est de l'ingestion ([[Debezium]] en est l'outil de référence), l'autre du traitement, et leurs pièges n'ont rien à voir.
- **Décrire** la donnée est un travail distinct de la **garantir**. Un catalogue dit ce qui existe, qui en répond et d'où cela vient ; il n'impose ni contrat ni test. Le lignage se collecte de deux façons, tirée (le catalogue interroge les sources) ou poussée (l'outil qui exécute émet des événements) — cf. [[Catalogue de données et lignage]]. Les fiches [[OpenMetadata]], [[DataHub]] et [[OpenLineage]] sont ici, à côté de l'orchestration qui émet.
- La **donnée factice** et la **donnée synthétique** sont deux besoins distincts, souvent confondus. [[Faker]] et [[Mimesis]] fabriquent des valeurs plausibles champ par champ, indépendamment les unes des autres — parfait pour peupler des tests. [[SDV]] apprend la distribution jointe du réel — nécessaire dès qu'on veut que les corrélations tiennent. Cf. [[Synthetic data generation]].
- Le **profilage** ([[ydata-profiling]], [[sweetviz]], [[missingno]]) est le premier geste sur un jeu inconnu, et il précède toute modélisation : cf. [[EDA automatisée & profiling]].

## Choisir

- Extraire depuis des pages web → [[Scraping]].
- Extraire depuis des documents (PDF, Office, scans) → [[Parsing]].
- Amener la donnée d'une source vers un entrepôt ou un lac : catalogue de connecteurs → [[Airbyte]] (licence Elastic 2.0) ; en code Python → [[dlt]] ; flux de fichiers et de protocoles → [[Apache NiFi]] ; les changements d'une base par son journal → [[Debezium]]. Cf. [[Comparatif - Ingestion de données]], et [[Ingestion incrémentale et curseurs]] pour ce qu'un rechargement rate.
- Savoir d'où vient une donnée, qui l'utilise et qui en répond : un catalogue complet sans Kafka → [[OpenMetadata]] ; un catalogue par événements, avec Kafka → [[DataHub]] ; le lignage émis par Spark, Flink, dbt ou Airflow, quel que soit le catalogue → [[OpenLineage]] (une spécification, pas un catalogue). Cf. [[Comparatif - Catalogues et lignage de données]], et [[Catalogue de données et lignage]] pour ce qu'un catalogue ne remplace pas.
- Collecter des logs et des métriques sur des machines, et les transformer avant de les indexer dans [[Elasticsearch]] → [[Beats]] (agents) et [[Logstash]] (pipeline).
- Charger, filtrer, joindre, agréger en mémoire → [[DataFrames]].
- Faire tourner tout ça chaque nuit, avec dépendances et reprises → [[Orchestration]].
- En faire un graphique → [[Visualisation]].
- Donner à des équipes métier des tableaux de bord et des requêtes libres, sur site → [[Comparatif - BI auto-hébergée]] : [[Metabase]] (sans code, open-core AGPL) ou [[Apache Superset]] (Apache-2.0, plus de pièces à exploiter).
- Analyser en libre-service des séries de procédé branchées sur un historien, sans copier les données → [[Seeq]] (propriétaire, sur site ou cloud).
- Traiter au fil de l'eau plutôt que par lots → [[Flink]], et [[Stream processing]] pour la théorie.
- Faire circuler des événements ou des tâches entre services, sur site → [[Messagerie]] : [[Kafka]] (journal rejouable), [[NATS]] (un binaire léger), [[RabbitMQ]] (files et routage), [[Redpanda]] (protocole Kafka, licence BSL), et [[Celery]] pour les tâches Python.
- Recevoir les mesures de capteurs et d'automates par MQTT, sur site : un nœud léger sous licence libre → [[Mosquitto]] ; un cluster, sous licence BSL → [[EMQX]] ; le reste de l'atelier (OPC UA, Modbus, flux) est dans [[Données industrielles]]. Cf. [[Comparatif - Brokers MQTT]].
- Sortir vite une table SQL vers un DataFrame → [[connectorx]].
- Poser une table analytique durable sur du stockage objet → [[Parquet]] plus [[Apache Iceberg]], ou [[Delta Lake]] quand le socle est Spark (cf. [[Formats de fichiers et de tables]]).
- Échanger des messages à schéma versionné → [[Avro]].
- Peupler des tests → [[Faker]] (ou [[Mimesis]] si le volume compte) ; reproduire une distribution réelle → [[SDV]].
- Découvrir un jeu de données inconnu → [[ydata-profiling]] ; comparer deux jeux → [[sweetviz]] ; comprendre la structure des trous → [[missingno]].
- Répliquer une base source sans la recharger entière → [[Change Data Capture (CDC)]], outillée par [[Debezium]].
- Dériver des tables par des modèles SQL versionnés, testés et documentés → [[dbt Core]] ; avec un état, des environnements virtuels et un plan des changements → [[SQLMesh]].
- Vérifier qu'un lot livré respecte ses règles → [[Fiabilité des données]] ([[Great Expectations]], [[Soda Core]], [[pandera]]).
- Ranger les tables produites en faits et dimensions → [[Modélisation dimensionnelle]].
- Figer un état de données pour reproduire un entraînement : des fichiers dans un dépôt Git → [[DVC]] ; un dépôt d'objets avec branches → [[lakeFS]] (licence BSL depuis septembre 2026) ; une table → le time travel d'[[Apache Iceberg]] ou de [[Delta Lake]]. Cf. [[Comparatif - Versionnage de données]].
- Rendre un pipeline rejouable, contractuel, reproductible → [[ELT vs ETL & idempotence]], [[Contrats de données & qualité]], [[Versionnage de données]].
- Cinq notions **ne sont pas ici**, et c'est délibéré : [[ORM]], [[Migrations de schéma]], [[Bases de données vectorielles]] et [[Index ANN — internes]] sont descendues dans [[Bases de données]], [[Notebooks-as-code]] dans [[Outils de développement]]. Elles portaient toutes la même catégorie de notion, parce que la galaxie wiki n'avait pas de valeur plus fine ; leur sujet est le moteur ou l'outil, pas le pipeline.

<!-- AUTO:START -->
### Sous-domaines
- [[DataFrames]] · [[Données industrielles]] · [[Fiabilité des données]] · [[Formats de fichiers et de tables]] · [[Ingestion de données]] · [[Messagerie]] · [[Orchestration]] · [[Parsing]] · [[Scraping]] · [[Visualisation]]

### Notions
- [[Catalogue de données et lignage]] — domaines : data-eng
- [[EDA automatisée & profiling]] — domaines : data-sci, data-eng
- [[Stream processing]] — domaines : data-eng

### Briques
- [[Apache Superset]] — BI auto-hébergée Apache-2.0 tournée vers l'exploration : SQL Lab, constructeur de graphiques, tableaux de bord, droits par ligne, alertes et embedding sans édition payante ; exploitation plus lourde (base de métadonnées, Redis, Celery).
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud).
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit).
- [[Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch.
- [[Metabase]] — BI auto-hébergée orientée utilisateurs métier : questions sans code et SQL natif, tableaux de bord, alertes, en un seul conteneur Java ; AGPL-3.0 avec SSO avancé, droits par ligne et embedding complet réservés aux éditions payantes.
- [[Mimesis]] — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- [[missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.
- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data).
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate).
- [[SDV]] — Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL).
- [[Seeq]] — Application d'analyse en libre-service de séries temporelles de procédé — se branche sur des historiens dont PI System, sans copier les données ; installable sur site ou en cloud, propriétaire.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran.
- [[sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.

### Comparatifs
- [[Comparatif - BI auto-hébergée]]
- [[Comparatif - Catalogues et lignage de données]]
- [[Comparatif - Outils EDA - profiling]]
- [[Comparatif - Transformation SQL]]
<!-- AUTO:END -->
