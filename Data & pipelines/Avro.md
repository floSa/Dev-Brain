---
role: brique
nom: Avro
alias: [avro, Apache Avro]
pitch: "Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka."
categorie: data/format
famille: specification
licence_type: open-source
maturite: production
langage: Java
alternatives: ["[[Parquet]]"]
complements: []
tags: [file-format, serialization, schema-evolution]
url_docs: https://avro.apache.org/docs/
url_repo: https://github.com/apache/avro
---

# Avro

<!-- AUTO:BANDEAU:START -->
> Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification Java | open-source | rien à exécuter | production | à jour · 2026-08-23 |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de sérialisation **orienté ligne** : chaque enregistrement est encodé en binaire
compact, et le schéma qui le décrit — écrit en JSON — accompagne les données, embarqué dans
l'en-tête du fichier ou résolu via un Schema Registry pour les flux. La caractéristique
signature est l'**évolution de schéma** : producteurs et consommateurs peuvent tourner sur
des versions différentes, Avro résolvant la compatibilité ascendante et descendante à la
lecture. Le prix de l'orientation ligne est le symétrique de son avantage : lire trois
colonnes d'un enregistrement large oblige à décoder l'enregistrement entier. Né dans Hadoop,
avec Doug Cutting.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Écriture ou append **enregistrement par enregistrement** : logs, événements, flux | Scans analytiques de quelques colonnes sur beaucoup de lignes → [[Parquet]] |
| Charges utiles de messages Kafka, gouvernées par un Schema Registry | Analytique en mémoire ou interop colonnaire : Apache Arrow, hors brain |
| Échange entre systèmes et langages où le schéma doit évoluer sans casser les lecteurs | Sémantique de table sur un data lake — ACID, time travel → [[Apache Iceberg]] |
| Lectures de **lignes entières**, tous champs confondus | Le schéma est indispensable à la lecture : sans registry, un flux Kafka est indéchiffrable — les fichiers, eux, l'embarquent |
| | Les règles de compatibilité se respectent ou cassent producteurs et consommateurs ; les schémas JSON sont verbeux et la génération de code parfois nécessaire |

## Mise en œuvre

- Installation — bibliothèques par langage : `uv add fastavro` en Python, implémentations Java, C et C++
- Point d'entrée — API de sérialisation de la bibliothèque ; côté Kafka, un serializer adossé au registry
- Prérequis — un Schema Registry (Confluent) dès que les schémas circulent hors fichier
- Exécution — dans le process qui sérialise ou désérialise ; format splittable, donc exploitable par les moteurs distribués
- Coût — gratuit, Apache-2.0 ; le Schema Registry, lui, est un service de plus à exploiter

## Écosystème

### Alternatives

- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.

## Ressources

- Documentation — https://avro.apache.org/docs/
- Dépôt — https://github.com/apache/avro

## Voir aussi

- [[Contrats de données & qualité]] — le contrat producteur / consommateur que ces règles de compatibilité matérialisent
- [[Stream processing]] — le contexte où Avro sert de format de charge utile
