---
role: brique
nom: ClickHouse
alias: [clickhouse]
pitch: "SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence."
categorie: database/analytique
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[DuckDB]]", "[[Snowflake]]", "[[Trino]]"]
complements: ["[[dbt Core]]", "[[SQLMesh]]", "[[Airbyte]]", "[[dlt]]", "[[OpenMetadata]]", "[[DataHub]]", "[[Metabase]]"]
tags: [columnar, olap, distributed]
url_docs: https://clickhouse.com/docs
url_repo: https://github.com/ClickHouse/ClickHouse
---

# ClickHouse

<!-- AUTO:BANDEAU:START -->
> SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD **orienté colonnes** conçu pour l'OLAP. Les données sont stockées et traitées par
colonne, fortement compressées, avec une exécution **vectorisée** : le moteur balaie des
centaines de millions de lignes par seconde. Il se distribue par sharding, pour le volume, et
par réplication, pour la disponibilité. Le choix du moteur de table — la famille MergeTree —
et des clés de tri est la décision structurante : il se fait avant l'ingestion et commande
les performances de toutes les requêtes qui suivront.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analytique temps réel sur gros volumes : tableaux de bord, observabilité, événements | Mises à jour et suppressions fréquentes ligne à ligne : le modèle est pensé pour l'append, et les mutations sont asynchrones et coûteuses |
| Agrégations massives balayant beaucoup de lignes sur peu de colonnes | Lecture attendue juste après l'écriture : la cohérence de la réplication est éventuelle |
| Ingestion à fort débit de logs, métriques, télémétrie | OLTP transactionnel, beaucoup de petites écritures et de mises à jour ponctuelles → [[Postgres]] |
| Scale-out horizontal sur un cluster | |

## Mise en œuvre

- Installation — binaire ou cluster en self-host, ou managé sur ClickHouse Cloud
- Point d'entrée — SQL, depuis un client ou un pilote
- Prérequis — le moteur de table (famille MergeTree) et les clés de tri choisis avant l'ingestion
- Exécution — self-hébergé ou managé ; distribué, sharding pour le volume et réplication pour la disponibilité
- Coût — gratuit, licence Apache 2.0 ; le coût réel est l'exploitation du cluster

## Écosystème

### Alternatives

- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.
- [[Snowflake]] — Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement. — la même analytique colonnes, mais sans cluster à opérer et sans possibilité d'auto-hébergement ; rangé en plateforme, pas en base, cf. la règle D-R8 de la taxonomie.
- [[Trino]] — Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL, MySQL…) sans rien stocker lui-même ; Apache-2.0, coordinateur et workers en Java. — interroge des sources sans les stocker : ni ingestion ni stockage propre.

### Compléments

- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — `dbt-clickhouse` (1.10.3, 2026-09-15), maintenu par ClickHouse Inc. ; vues matérialisées et tables distribuées expérimentales ; en dbt v2 il est en *private beta*, sans `ON CLUSTER` ni matérialisations distribuées.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran. — moteur pris en charge mais contraint : pas d'upsert (échange de tables et de partitions qui copient l'existant), ne peut pas héberger l'état, et une issue ouverte le 2026-09-23 signale des échecs silencieux de l'échange.
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — destination certifiée en disponibilité générale.
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0). — destination documentée, utilisable sur site.
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — connecteur de base listé.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — source listée en GA.
- [[Metabase]] — BI auto-hébergée orientée utilisateurs métier : questions sans code et SQL natif, tableaux de bord, alertes, en un seul conteneur Java ; AGPL-3.0 avec SSO avancé, droits par ligne et embedding complet réservés aux éditions payantes. — ClickHouse y est un driver officiel.

## Ressources

- Documentation — https://clickhouse.com/docs
- Dépôt — https://github.com/ClickHouse/ClickHouse

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases colonnes]] — ce qui départage les moteurs du dossier
