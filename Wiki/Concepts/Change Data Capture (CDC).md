---
galaxie: wiki
type: concept
nom: Change Data Capture (CDC)
alias: [CDC, change data capture, capture de changements, log-based replication]
categorie: concept/data
domaines: [data-eng]
tags: [cdc, streaming, data-pipeline]
---

# Change Data Capture (CDC)

## Aperçu

- Capturer les **changements** (insert / update / delete) d'une base source au fil de l'eau, plutôt que recopier toute la table à chaque run.
- Permet une réplication incrémentale, à faible latence et faible charge sur la source : la base de référence reste opérationnelle pendant qu'un flux de changements alimente l'analytique.

## Concepts clés

### Log-based CDC
- Lit le **journal de transactions** de la base (WAL Postgres, binlog MySQL, redo log Oracle) — la source de vérité des écritures.
- Capture *tous* les changements, y compris les `DELETE`, sans requêter les tables ni charger la base. Faible latence, ordre préservé.
- Coût : couplage au moteur et à son format de log, configuration (slots de réplication, rétention du WAL), opérationnellement plus exigeant. Outil de référence : **Debezium**.

### Query-based CDC
- Interroge périodiquement la table sur une colonne **témoin** (`updated_at`, ou un id auto-incrémenté) pour récupérer les lignes modifiées depuis le dernier passage.
- Simple, sans accès au log ni privilège spécial. Mais : rate les `DELETE` (la ligne a disparu), dépend d'un horodatage fiable, et le polling crée une charge et une latence.

### Snapshot + flux incrémental
- Démarrage typique : un **snapshot** initial complet de la table, puis bascule sur le flux de changements. La gestion de la cohérence à la bascule (ne rien perdre, ne pas dupliquer) est le point délicat.

### Sémantique de livraison
- *At-least-once* le plus souvent : un même changement peut être rejoué → la cible doit appliquer les événements de façon **idempotente** (upsert par clé). Cf. [[ELT vs ETL & idempotence]].
- Ordre par clé primaire à préserver pour ne pas appliquer un vieux état après un récent.

## En pratique

- Préférer le **log-based** (Debezium) quand on a la main sur la base source et qu'on vise faible latence + capture des suppressions ; le **query-based** comme repli simple quand l'accès au log est impossible.
- CDC alimente le *Load* d'un pipeline incrémental : la couche de transformation reste de l'[[ELT vs ETL & idempotence|ELT]] côté cible.
- Souvent posé sur un bus de streaming (Kafka) entre la source et la cible ; l'orchestration ([[Dev/Services/Airflow|Airflow]], [[Dev/Services/Dagster|Dagster]]) pilote les snapshots, le monitoring et les transformations aval plutôt que le flux lui-même.
- Poser un [[Contrats de données & qualité|contrat]] sur le flux : un changement de schéma à la source ne doit pas casser silencieusement l'aval.
- Pièges : WAL non purgé qui sature le disque source, `DELETE` perdus en query-based, drift de schéma à la source, retraitement non idempotent à la cible.

## Approches voisines & alternatives

- [[ELT vs ETL & idempotence]] — la cible applique les changements de façon idempotente.
- [[Contrats de données & qualité]] — garde-fou de schéma sur le flux capturé.
- [[Versionnage de données]] — figer des états cohérents en aval d'un flux continu.
- Alternative naïve : rechargement complet (*full load*) périodique — simple mais lourd et sans historique des changements.
- Orchestrateurs : [[Dev/Services/Airflow|Airflow]], [[Dev/Services/Dagster|Dagster]].

## Pour aller plus loin

- Outils non encore fichés : **Debezium** (log-based, connecteurs Kafka), Fivetran / Airbyte (CDC managé/intégré) — candidats `Dev/Services/` (`data/ingestion`).
- Notion connexe : *outbox pattern* — publier les changements applicatifs de façon transactionnelle.
