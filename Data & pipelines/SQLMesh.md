---
role: brique
nom: SQLMesh
alias: [sqlmesh, Tobiko SQLMesh]
pitch: "Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran."
categorie: data/transformation
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[dbt Core]]"]
complements: ["[[Postgres]]", "[[DuckDB]]", "[[ClickHouse]]", "[[Spark]]", "[[Kestra]]"]
tags: [data-transformation, data-pipeline, data-quality]
url_docs: https://sqlmesh.readthedocs.io/en/stable/
url_repo: https://github.com/SQLMesh/sqlmesh
---

# SQLMesh

<!-- AUTO:BANDEAU:START -->
> Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de transformation SQL qui garde un **état**. Chaque modèle, en SQL ou en Python, déclare son
*kind* — `FULL`, `VIEW`, `INCREMENTAL_BY_TIME_RANGE`, `INCREMENTAL_BY_UNIQUE_KEY`, `SCD_TYPE_2`… —
et SQLMesh suit les intervalles de temps déjà calculés : l'incrémental ne demande pas d'écrire la
logique de reprise. `sqlmesh plan` compare le projet à un environnement, classe chaque changement
(cassant, non cassant, *forward-only*) et ne recalcule que ce qui l'exige. Les environnements sont
**virtuels** : un ensemble de vues qui pointent vers des tables physiques identifiées par une
empreinte, si bien que promouvoir en production ne recopie rien. Le lignage au niveau colonne
vient de SQLGlot, la bibliothèque d'analyse SQL de la même équipe.

Relevé le 2026-09-30 : **0.236.2** (2026-09-08), environ 3 300 étoiles, **Apache-2.0**, dépôt
`SQLMesh/sqlmesh` (ancien `TobikoData/sqlmesh`), dernier commit le 2026-09-29, 436 820
téléchargements PyPI sur 30 jours — contre 22,5 M pour dbt-core. Tobiko Data, éditeur du projet, a
été racheté par Fivetran (annoncé le 2025-09-03) ; Fivetran a ensuite contribué SQLMesh à la
**Linux Foundation** (annoncé le 2026-03-25).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des environnements de développement et de recette qui ne recalculent pas ce qui n'a pas changé : la promotion en production met à jour des pointeurs | Un moteur sans support des **vues** : les environnements virtuels en dépendent, ce qui exclut par exemple les catalogues Trino/Iceberg de type `jdbc` et `nessie` hors REST |
| Un incrémental dont les intervalles traités sont suivis et les trous détectés, sans logique de reprise à écrire | Aucune base transactionnelle à côté pour l'état : ClickHouse, Spark et Trino ne peuvent pas le porter, DuckDB est déconseillé en production |
| Un plan qui dit, avant exécution, ce qu'un changement casse en aval, et un lignage colonne gratuit | Un orchestrateur natif sans payer : `sqlmesh run` s'exécute une fois puis s'arrête, et l'intégration Airflow documentée exige Tobiko Cloud |
| Essayer sur un projet dbt existant sans le migrer : `sqlmesh init -t dbt` l'exécute tel quel | Une exigence de gouvernance écrite sur l'avenir de l'outil : aucun texte officiel ne dit comment SQLMesh et dbt coexisteront chez Fivetran |

## Mise en œuvre

- Installation — `uv add "sqlmesh[postgres]"` (un extra par moteur : `clickhouse`, `mysql`, `trino`…), Python ≥ 3.9 ; `sqlmesh[lsp]` pour l'extension VS Code, `sqlmesh[dbt]` pour un projet dbt
- Point d'entrée — `sqlmesh init`, `sqlmesh plan [env]`, `sqlmesh run`, `sqlmesh test`, `sqlmesh table_diff` ; modèles dans `models/`, connexions dans `config.yaml`. L'interface web est **dépréciée** au profit de l'extension VS Code
- Prérequis — une base d'état séparée du moteur de données (`state_connection`) : Postgres recommandé, MySQL et SQL Server possibles mais moins testés. Contraintes par moteur : **ClickHouse** n'a pas d'upsert, SQLMesh passe par un *temp table swap* et un *partition swap* qui copient l'existant, à tenir sous environ 1 000 partitions par table, avec `join_use_nulls = 1` forcé pour SCD2 — et une issue ouverte le 2026-09-23 signale des échecs silencieux du swap ; **Trino** n'est testé que sur les connecteurs Hive, Iceberg et Delta Lake ; **Spark** ne gère qu'un seul catalogue. La page des moteurs liste seize moteurs sans publier de niveau de support par moteur
- Exécution — scheduler intégré, mais `sqlmesh run` ne tourne pas en continu : cron, CI ou orchestrateur ; Kestra figure dans la liste officielle des intégrations, Dagster non
- Coût — gratuit en Apache-2.0. Tobiko Cloud est payant (redevance de plateforme plus consommation) : ordonnancement sans cron, exécution parallèle, secrets centralisés, contrôle d'accès fin annoncé « coming soon » — et seul chemin de l'intégration Airflow officielle

## Licence et gouvernance

- La licence n'a pas changé : Apache-2.0 avant et après le rachat comme après le don à la Linux Foundation.
- **Gouvernance** (fichier `GOVERNANCE.md`) : un comité de pilotage technique de six sièges, dont un seul chez Fivetran, décide au consensus, à la majorité simple avec un quorum de 50 %. La Linux Foundation détient les marques. Membres fondateurs annoncés : Benzinga, CloudKitchens, Harness, Infinite Lambda, Jump AI, Minerva.
- **Rapprochement avec dbt** : Fivetran a fusionné avec dbt Labs (clôture le 2026-06-01) et a donné SQLMesh à la fondation plutôt que de le garder. Les analyses tierces qui prédisent une fusion des deux outils ou un abandon sont des opinions, l'une d'elles concluant elle-même que c'est trop tôt pour le dire ; l'annonce officielle du don parle de « vendor neutral ».
- Le rachat du 2025-09-03 ne donne aucun engagement explicite sur l'open source (« nothing changes on day 1 »).

## Limites à connaître

- **Dépendances épinglées** : `pandas<3.0.0` et `sqlglot~=30.8.0` ; chaque montée de sqlglot est signalée comme cassante dans les notes de version (0.235.0, 0.236.0).
- **Cadence** : environ une version par semaine début 2026, puis une toutes les trois à sept semaines depuis mai ; 234 issues ouvertes au 2026-09-30.
- **Kinds non idempotents** : `INCREMENTAL_BY_UNIQUE_KEY`, `INCREMENTAL_BY_PARTITION` et `INCREMENTAL_UNMANAGED` ; `UNIQUE_KEY` n'admet pas de restatement partiel. Les modèles Python ne supportent ni `VIEW`, ni `SEED`, ni `EMBEDDED`, ni `MANAGED`.
- **Courbe d'apprentissage** : plan/apply, empreintes et snapshots sont un autre modèle mental ; le vivier de compétences est plus étroit que celui de dbt.
- **Migration depuis dbt** : aucun outil officiel de conversion. L'adaptateur `sqlmesh[dbt]` exécute un projet tel quel mais ne prend pas en charge `invalidate_hard_deletes: false` sur les snapshots ni quelques méthodes Jinja, et les modèles incrémentaux se réécrivent avec un `start`.

## Écosystème

### Alternatives

- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit).

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — moteur d'exécution pris en charge (extra `postgres`) et base d'état recommandée (`state_connection`), à côté du moteur de données.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — moteur pris en charge, à utilisateur unique et recommandé pour le développement seulement ; c'est aussi le moteur des tests unitaires par défaut, et la documentation le déconseille comme base d'état en production.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — moteur pris en charge mais contraint : pas d'upsert (échange de tables et de partitions qui copient l'existant), ne peut pas héberger l'état, et une issue ouverte le 2026-09-23 signale des échecs silencieux de l'échange.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — moteur pris en charge, conçu et testé pour un seul catalogue, qui ne peut pas héberger l'état.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — Kestra figure dans la liste officielle des intégrations de SQLMesh, avec un plugin dédié ; l'intégration Airflow documentée, elle, exige Tobiko Cloud.

## Ressources

- Documentation — https://sqlmesh.readthedocs.io/en/stable/
- Dépôt — https://github.com/SQLMesh/sqlmesh
- Documentation — https://github.com/SQLMesh/sqlmesh/blob/main/GOVERNANCE.md
- Article — https://www.linuxfoundation.org/press/linux-foundation-welcomes-sqlmesh-project
- Article — https://www.fivetran.com/blog/fivetran-acquires-tobiko-data-to-power-enterprise-grade-transformations

## Voir aussi

- [[Data & pipelines]] — le hub du dossier
- [[Comparatif - Transformation SQL]] — ce qui départage dbt Core et SQLMesh
- [[ELT vs ETL & idempotence]] — l'ordre d'assemblage dont SQLMesh est le T, et l'idempotence de ses kinds
- [[Architecture médaillon]] — les couches que les modèles raffinent
