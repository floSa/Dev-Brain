---
galaxie: wiki
type: concept
nom: Contrats de données & qualité
alias: [data contract, contrat de données, data quality, qualité des données, freshness, fraîcheur, validation de données]
categorie: concept/data
domaines: [data-eng]
tags: [data-contract, data-quality, data-validation, schema-evolution]
---

# Contrats de données & qualité

## Aperçu

- Un **contrat de données** est l'interface explicite et versionnée entre un producteur et ses consommateurs : schéma, sémantique et garanties (fraîcheur, volumétrie, unicité) promises.
- La **qualité des données** est la vérification continue que la donnée livrée respecte ce contrat — détecter tôt, bloquer avant propagation, plutôt que déboguer un dashboard faux trois étages plus loin.

## Concepts clés

### Contrat de données
- Spécification stable du *quoi* : noms et types de colonnes, nullabilité, clés, énumérations, unités, sémantique métier.
- Versionné comme une API : le producteur s'engage, le consommateur s'appuie dessus. Casser le contrat est un *breaking change* négocié, pas une surprise.
- Lié à l'[[Migrations de schéma|évolution de schéma]] : ajouts compatibles vs changements destructifs.

### Validation de schéma
- Contrôle structurel à l'exécution : types, présence des colonnes, contraintes (plages, regex, valeurs admises, clés uniques).
- Outils Python : **Pandera** (schémas typés sur DataFrames pandas/polars, intégrable dans le code) et **Great Expectations** (suites d'« expectations », documentation et *data docs* générées). Côté transformation, **dbt tests** et **Soda** posent les contrôles en SQL.

### Dimensions de qualité
- **Fraîcheur** : la donnée est-elle à jour ? (délai depuis la dernière mise à jour vs SLA).
- **Volumétrie** : le nombre de lignes est-il dans la plage attendue ? (chute = ingestion cassée ; explosion = doublons).
- **Complétude** : taux de valeurs manquantes par colonne.
- **Unicité / distribution / cohérence** : pas de doublons de clé, distributions stables, cohérence inter-tables (intégrité référentielle).

### Validation en porte vs en observation
- **En porte (gate)** : le contrôle bloque le pipeline si la donnée est non conforme — *fail fast*, on ne charge pas du sale.
- **En observation (monitoring)** : on mesure et alerte sans bloquer, utile quand couper le flux coûte plus cher que laisser passer. Recoupe le suivi de [[Data drift]].

## En pratique

- Placer les contrôles **aux frontières** : à l'ingestion (le brut est-il valide ?) et à la sortie des transformations critiques (le produit est-il livrable ?).
- Câbler la validation dans l'orchestration : une expectation/un test échoué fait échouer la tâche [[Dev/Services/Airflow|Airflow]] ou matérialise un *asset check* [[Dev/Services/Dagster|Dagster]] — l'aval ne se déclenche pas sur de la donnée fausse.
- Choisir l'outil selon l'ancrage : **Pandera** quand la donnée vit en DataFrame dans du code Python ; **Great Expectations** pour des suites partagées et documentées ; **dbt tests** quand la transformation est déjà en SQL.
- Distinguer qualité **des données** (ce contrat) et qualité **du modèle** : la dérive de distribution relève aussi de [[Data drift]].
- Pièges : valider seulement le schéma en oubliant fraîcheur et volumétrie ; tout mettre en *gate* et bloquer la prod sur un faux positif ; des seuils figés qui ne suivent pas la saisonnalité.

## Approches voisines & alternatives

- [[ELT vs ETL & idempotence]] — les portes de qualité s'insèrent entre les étapes du pipeline.
- [[Migrations de schéma]] — versionner le schéma promis par le contrat.
- [[Change Data Capture (CDC)]] — appliquer un contrat sur un flux de changements.
- [[Data drift]] — versant monitoring statistique de la qualité.
- [[EDA automatisée & profiling]] — profiler un jeu de données pour *dériver* les attentes.
- Orchestrateurs où s'exécutent les contrôles : [[Dev/Services/Airflow|Airflow]], [[Dev/Services/Dagster|Dagster]].

## Pour aller plus loin

- Outils non encore fichés : **Great Expectations**, **Pandera**, **Soda**, **dbt tests** — candidats à des fiches `Dev/Services/` (`data/quality`).
- Lecture : *Data Contracts* (Chad Sanderson) — le contrat comme produit, géré côté producteur.
