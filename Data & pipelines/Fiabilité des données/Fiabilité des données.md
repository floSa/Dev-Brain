---
role: hub
nom: Fiabilité des données
alias: []
pitch: Savoir à quoi se fier dans une donnée — la rejouer sans doublon, la raffiner par couches, la contractualiser, la vérifier, la figer.
domaines: [data-eng]
tags: [data-quality, data-contract, idempotence, data-versioning, data-validation]
---

# Fiabilité des données

> Savoir à quoi se fier dans une donnée — la rejouer sans doublon, la raffiner par couches, la contractualiser, la vérifier, la figer.

## Ce qu'il faut comprendre

- La question de ce dossier n'est pas « comment déplacer la donnée » (c'est l'affaire d'[[Orchestration]] et de l'ingestion) mais **à quoi peut-on se fier une fois qu'elle a bougé**. Quatre notions répondent chacune sous un angle : l'ordre d'assemblage et la rejouabilité ([[ELT vs ETL & idempotence]]), les couches de raffinage ([[Architecture médaillon]]), les garanties passées au consommateur ([[Contrats de données & qualité]]), l'état figé et reproductible ([[Versionnage de données]]).
- Un contrat est une **promesse**, un outil de vérification est ce qui la **teste**. [[Great Expectations]], [[Soda Core]] et [[pandera]] vérifient ; aucun ne décide de ce qu'il faut promettre, ni ne rend un traitement rejouable.
- Le clivage qui départage les trois est **où vit la donnée qu'on vérifie**. Une table en base se vérifie sur place, en SQL, sans rapatrier les lignes ([[Soda Core]], et [[Great Expectations]] sur ses sources SQL) ; un DataFrame en mémoire se vérifie dans le code ([[pandera]]). Le détail est dans [[Comparatif - Qualité de données]].
- Les licences ne sont pas les mêmes, et la plus restrictive n'est pas celle qu'on croit : [[Soda Core]] est passé d'Apache-2.0 à Elastic License 2.0 avec la v4 (sources lisibles, service hébergé à des tiers interdit), là où [[Great Expectations]] reste Apache-2.0 et [[pandera]] MIT.
- Une porte de qualité se pose là où une erreur coûte le moins cher à corriger : au passage entre couches, avant que la donnée ne soit propagée — cf. [[Architecture médaillon]].

## Choisir

- Rendre un traitement rejouable sans doublon ni décalage → [[ELT vs ETL & idempotence]].
- Organiser bronze, silver et gold → [[Architecture médaillon]].
- Écrire ce que la donnée promet à ses consommateurs → [[Contrats de données & qualité]].
- Figer un état reproductible d'un jeu de données → [[Versionnage de données]].
- Vérifier une table en base avec un rapport HTML lisible par des non-développeurs → [[Great Expectations]].
- Vérifier une table en base par des contrats YAML, avec un code de sortie pour la CI → [[Soda Core]] (licence à lire avant de redistribuer).
- Vérifier un DataFrame pandas, Polars ou PySpark dans le code → [[pandera]].
- Surveiller la dérive d'un jeu de données et d'un modèle en production plutôt que tester des règles connues → [[Evidently]], qui vit dans le domaine Machine Learning.

<!-- AUTO:START -->
### Notions
- [[Architecture médaillon]] — domaines : data-eng
- [[Contrats de données & qualité]] — domaines : data-eng
- [[ELT vs ETL & idempotence]] — domaines : data-eng
- [[Versionnage de données]] — domaines : data-eng, mlops

### Briques
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026.
- [[pandera]] — Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT).
- [[Soda Core]] — Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud.

### Comparatifs
- [[Comparatif - Qualité de données]]
<!-- AUTO:END -->
