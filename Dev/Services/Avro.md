---
galaxie: dev
type: service
nom: Avro
alias: [avro, Apache Avro]
pitch: "Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka."
categorie: data/format
licence_type: open-source
hosted: self
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Dev/Services/Parquet|Parquet]]"]
remplace_par: []
status: actif
tags: [file-format, serialization, schema-evolution]
url_docs: https://avro.apache.org/docs/
url_repo: https://github.com/apache/avro
---

# Avro

## Pourquoi

Apache Avro est un système de **sérialisation orienté ligne** : chaque enregistrement est encodé en **binaire compact**, et le **schéma** (décrit en **JSON**) accompagne les données — embarqué dans l'en-tête du fichier, ou résolu via un Schema Registry pour les flux. Sa caractéristique signature est l'**évolution de schéma** : producteurs et consommateurs peuvent utiliser des versions différentes, Avro gère la compatibilité ascendante et descendante (ajout / retrait de champs). Né dans Hadoop (Doug Cutting). Apache-2.0.

## Quand l'utiliser

- Écriture / append **enregistrement par enregistrement** : logs, événements, flux.
- Charges utiles de messages Kafka, couplé à un Schema Registry (Confluent).
- Échange de données entre systèmes et langages où le **schéma doit évoluer** sans casser les lecteurs.
- Lectures de **lignes entières** (tous les champs) plutôt que de quelques colonnes.

## Quand NE PAS l'utiliser

- Scans analytiques de quelques colonnes sur de gros volumes → [[Dev/Services/Parquet|Parquet]] (orienté colonnes).
- Analytique en mémoire / interop colonnaire → Apache Arrow.
- Stockage de tables de data lake avec sémantique transactionnelle → [[Dev/Services/Apache Iceberg|Apache Iceberg]].

## Déploiement & coût

- Format + système de sérialisation ouvert ; bibliothèques Java, Python (fastavro), C / C++, etc. Gratuit (Apache-2.0).
- Souvent associé au Confluent Schema Registry pour gouverner les schémas des topics Kafka.
- Splittable : exploitable par les moteurs distribués.

## Pièges

- Le schéma est **indispensable** à la lecture : pour Kafka, prévoir un registry ; les fichiers, eux, l'embarquent.
- Les **règles de compatibilité** doivent être respectées sous peine de casser producteurs ou consommateurs.
- Mauvais choix pour l'analytique colonnaire (lecture large de peu de colonnes).
- Schémas JSON verbeux ; outillage de génération de code parfois nécessaire.

## Alternatives

- [[Dev/Services/Parquet|Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.

## Liens

- [[Dev/Services/Apache Iceberg|Apache Iceberg]] — utilise Avro pour ses fichiers de métadonnées (manifests).
- Schéma de flux : Confluent Schema Registry (gouvernance des schémas Kafka).
- Doc : https://avro.apache.org/docs/
