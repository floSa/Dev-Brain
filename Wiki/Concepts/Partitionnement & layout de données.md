---
galaxie: wiki
type: concept
nom: Partitionnement & layout de données
alias: [partitionnement, partitioning, data layout, layout de données, bucketing, partition pruning, taille de fichiers, small files problem]
categorie: concept/data
domaines: [data-eng]
tags: [partitioning, file-format, lakehouse, olap]
---

# Partitionnement & layout de données

## Aperçu

- Comment ranger physiquement une table sur stockage objet pour que les moteurs lisent **le moins de données possible** et en parallèle.
- Trois leviers : **partitionnement** (par quelle clé découper en répertoires/fichiers), **bucketing** (hachage en N seaux fixes), **taille de fichiers** (ni trop petits, ni trop gros).

## Concepts clés

### Partitionnement
- Découper la table par valeur(s) d'une colonne (souvent une date : `dt=2026-06-10/`), chaque partition étant un répertoire de fichiers.
- À la lecture, un filtre sur la clé de partition élimine des répertoires entiers avant toute I/O : c'est le **partition pruning**.
- Choisir une clé **alignée sur les filtres fréquents** et de **cardinalité moyenne** : trop fine (ex. par seconde, ou par `user_id`) → explosion de petits fichiers ; trop grossière → partitions énormes peu sélectives.

### Bucketing
- Répartir les lignes en un **nombre fixe** de seaux par hachage d'une colonne (`hash(id) % N`).
- Utile sur une colonne de **forte cardinalité** (clé de jointure) où le partitionnement par valeur serait ingérable.
- Bénéfice : jointures et agrégations co-localisées (mêmes seaux des deux côtés → moins de shuffle) ; lecture ciblée d'un seau pour une valeur donnée.

### Partition pruning & data skipping
- **Pruning** : sauter des partitions entières grâce au chemin (niveau répertoire).
- **Data skipping** : à l'intérieur d'un fichier, sauter des blocs grâce aux **statistiques min/max** par row group ([[Dev/Services/Parquet|Parquet]]) — un prédicat hors bornes ne lit pas le bloc.
- Les deux supposent que la donnée est **triée/regroupée** sur les colonnes filtrées (sinon les min/max se recouvrent et ne filtrent rien). D'où le tri à l'écriture (Z-order / clustering).

### Taille de fichiers & small files problem
- Cible usuelle : **128 Mo – 1 Go** par fichier. En dessous, le surcoût domine (ouverture, métadonnées, planification, listing du store objet).
- Le **small files problem** vient surtout des sinks de [[Stream processing|streaming]] et des écritures fréquentes : des milliers de micro-fichiers ruinent les scans.
- Remède : **compaction** périodique (réécrire les petits fichiers en gros), gérée nativement par les formats de table ([[Dev/Services/Apache Iceberg|Apache Iceberg]] : `rewrite_data_files`, expiration des snapshots).

## Les maths, simplement

- Coût d'un scan ≈ (données lues) + (nb de fichiers) × (surcoût fixe par fichier). Pruning et skipping réduisent le **premier** terme ; le sizing réduit le **second**.
- Sélectivité du pruning : si un filtre garde une fraction $f$ des partitions, on lit ≈ $f$ de la table — mais seulement si la clé filtrée **est** la clé de partition. Sinon $f = 1$ (full scan).
- Parallélisme : un moteur distribué assigne ≈ un fichier (ou row group) par tâche. Trop peu de gros fichiers → cœurs inactifs ; trop de petits → ordonnancement qui domine le calcul. Le bon sizing équilibre les deux.

## En pratique

- Partitionner sur la (les) colonne(s) des **filtres les plus fréquents**, souvent la date d'événement ; rester à 1–2 niveaux pour ne pas fragmenter.
- Préférer le **partitionnement caché** d'[[Dev/Services/Apache Iceberg|Apache Iceberg]] (la clé dérive d'une colonne, ex. `day(ts)`) : on requête sur la colonne brute, le moteur prune sans clause spéciale, et le schéma de partition peut évoluer sans réécrire l'historique.
- Surveiller et **compacter** : taille moyenne de fichiers et nombre de fichiers par partition sont les métriques santé d'une table.
- Pièges : sur-partitionnement (1 fichier par partition = small files), clé de partition de très forte cardinalité, filtrer sur une colonne **non** partitionnée (aucun pruning), oublier la compaction d'un sink streaming.
- Lien d'idempotence : aligner l'**unité d'écriture sur la partition** rend rerun et backfill sûrs (réécrire une partition entière). Cf. [[ELT vs ETL & idempotence]].

## Approches voisines & alternatives

- [[Dev/Services/Parquet|Parquet]] — le format de fichier qui porte les statistiques rendant le data skipping possible.
- [[Dev/Services/Apache Iceberg|Apache Iceberg]] — couche de table : partitionnement caché, évolution de partitionnement, compaction.
- [[Architecture médaillon]] — chaque couche se partitionne selon ses propres requêtes.
- [[ELT vs ETL & idempotence]] — la partition comme unité de rejeu.
- [[Stream processing]] — source classique du small files problem, à compacter en aval.

## Pour aller plus loin

- Z-ordering / clustering liquide (Delta), tri multi-colonnes à l'écriture — pousser le data skipping au-delà d'une seule colonne.
- Indexation complémentaire : Bloom filters par fichier pour les recherches d'égalité sur forte cardinalité.
