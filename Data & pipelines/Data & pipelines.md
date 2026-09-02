---
role: hub
nom: Data & pipelines
alias: [data engineering, pipelines de données]
pitch: Amener la donnée d'où elle est jusqu'à une forme exploitable — la collecter, la mettre en forme, la faire circuler, la regarder.
domaines: [data-eng, data-sci]
tags: [data-pipeline, dataframe, web-scraping, document-parsing, dataviz]
---

# Data & pipelines

> Amener la donnée d'où elle est jusqu'à une forme exploitable — la collecter, la mettre en forme, la faire circuler, la regarder.

## Ce qu'il faut comprendre

- Le domaine suit la trajectoire d'une donnée, et ses cinq sous-dossiers sont les cinq étapes de cette trajectoire : on la **collecte** ([[Scraping]], [[Parsing]]), on la **manipule** ([[DataFrames]]), on **planifie** son passage ([[Orchestration]]), on la **regarde** ([[Visualisation]]). Ce qui reste au niveau du domaine est ce qui traverse toutes les étapes : les formats sur disque, la génération de faux, le profilage.
- Le clivage qui structure le plus les choix est **la donnée tient-elle en mémoire**. En dessous, tout marche et [[pandas]] suffit. Au-dessus, il faut un moteur qui construise un plan avant d'exécuter ([[Polars]]) ou qui distribue ([[Flink]]) — et le code change, pas seulement la machine.
- Le **format sur disque** n'est pas un détail d'implémentation, c'est ce qui décide de la vitesse de lecture. [[Parquet]] est colonnaire, donc rapide en analytique et lent à la ligne ; [[Avro]] est en lignes, donc adapté à l'échange et aux messages ; [[Apache Iceberg]] n'est ni l'un ni l'autre — c'est une couche de table transactionnelle **par-dessus** ces fichiers, ce qui donne au [[Architecture médaillon|lakehouse]] ce que le stockage objet ne sait pas faire : l'ACID et le time travel. Cf. [[Partitionnement & layout de données]].
- Un pipeline se juge sur sa **rejouabilité** avant sa vitesse. Rejouer un jour manquant sans dupliquer ni décaler est la propriété qui distingue un pipeline d'un script — cf. [[ELT vs ETL & idempotence]] et [[Contrats de données & qualité]].
- La **donnée factice** et la **donnée synthétique** sont deux besoins distincts, souvent confondus. [[Faker]] et [[Mimesis]] fabriquent des valeurs plausibles champ par champ, indépendamment les unes des autres — parfait pour peupler des tests. [[SDV]] apprend la distribution jointe du réel — nécessaire dès qu'on veut que les corrélations tiennent. Cf. [[Synthetic data generation]].
- Le **profilage** ([[ydata-profiling]], [[sweetviz]], [[missingno]]) est le premier geste sur un jeu inconnu, et il précède toute modélisation : cf. [[EDA automatisée & profiling]].

## Choisir

- Extraire depuis des pages web → [[Scraping]].
- Extraire depuis des documents (PDF, Office, scans) → [[Parsing]].
- Charger, filtrer, joindre, agréger en mémoire → [[DataFrames]].
- Faire tourner tout ça chaque nuit, avec dépendances et reprises → [[Orchestration]].
- En faire un graphique → [[Visualisation]].
- Traiter au fil de l'eau plutôt que par lots → [[Flink]], et [[Stream processing]] pour la théorie.
- Sortir vite une table SQL vers un DataFrame → [[connectorx]].
- Poser une table analytique durable sur du stockage objet → [[Parquet]] plus [[Apache Iceberg]].
- Échanger des messages à schéma versionné → [[Avro]].
- Peupler des tests → [[Faker]] (ou [[Mimesis]] si le volume compte) ; reproduire une distribution réelle → [[SDV]].
- Découvrir un jeu de données inconnu → [[ydata-profiling]] ; comparer deux jeux → [[sweetviz]] ; comprendre la structure des trous → [[missingno]].

<!-- AUTO:START -->
### Sous-domaines
- [[DataFrames]] · [[Orchestration]] · [[Parsing]] · [[Scraping]] · [[Visualisation]]

### Briques
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB).
- [[Avro]] — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.
- [[connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.
- [[Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch.
- [[Mimesis]] — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- [[missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.
- [[SDV]] — Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL).
- [[sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.

### Comparatifs
- [[Comparatif - Outils EDA - profiling]]
<!-- AUTO:END -->
