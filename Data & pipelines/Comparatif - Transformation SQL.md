---
role: comparatif
nom: Comparatif - Transformation SQL
categorie: data/transformation
tags: [data-transformation, data-pipeline]
---

# Comparatif - Transformation SQL

> On tranche sur : ce que l'outil garde en mémoire d'un run à l'autre (rien, ou un état), la façon de fabriquer un environnement de recette, le lignage au niveau colonne, l'incrémental, et le prix d'entrée pour une équipe qui vient de l'un ou de l'autre.

![[Comparatif - Transformation SQL.base]]

## Ce qui départage

- [[dbt Core]] — le **standard** : un `SELECT` par fichier, le graphe déduit de `ref()`, 22,5 M de téléchargements PyPI par mois, des adaptateurs `Trusted` maintenus pour Postgres, Spark, ClickHouse, DuckDB et Trino, et aucun état à héberger. Le prix : le paysage v1/v2 (Postgres et Trino n'existent pas en v2), un lignage colonne qui demande la distribution complète v2 sous licence produit, et des environnements qui sont des schémas à reconstruire.
- [[SQLMesh]] — l'outil **à état** : un plan qui classe les changements avant de les appliquer, des environnements virtuels par pointeurs, un incrémental dont les intervalles sont suivis, le lignage colonne dans l'édition libre. Le prix : une base d'état à côté (Postgres), un vivier de compétences bien plus étroit (436 820 téléchargements PyPI par mois contre 22,5 M), et un avenir que le propriétaire n'a pas écrit — Tobiko racheté par Fivetran, SQLMesh donné à la Linux Foundation, Fivetran ayant ensuite fusionné avec dbt Labs.

**Critère par critère**

**Modèles.** [[dbt Core]] : SQL avec Jinja, matérialisations `view`, `table`, `incremental`, `ephemeral`, `materialized view` ; les modèles Python sont documentés pour Snowflake, BigQuery et Databricks seulement. [[SQLMesh]] : SQL ou Python, un *kind* par modèle (`FULL`, `VIEW`, `INCREMENTAL_BY_TIME_RANGE`, `INCREMENTAL_BY_UNIQUE_KEY`, `SCD_TYPE_2_BY_TIME`…), dialectes traduits par SQLGlot.

**Tests.** [[dbt Core]] : tests de données génériques (`unique`, `not_null`, `accepted_values`, `relationships`) et singuliers, tests unitaires depuis la 1.8, contrats de modèle qui font échouer le build. [[SQLMesh]] : **audits** — des requêtes qui doivent renvoyer zéro ligne, bloquantes par défaut — et tests unitaires en YAML qui tournent sur DuckDB par défaut ; un projet dbt exécuté par SQLMesh voit ses tests devenir des audits.

**Lignage au niveau colonne.** [[dbt Core]] v1 : non, seulement le graphe de modèles. v2 : oui en local, mais dans la distribution complète et non dans `dbt-oss` ; sur dbt platform, dans le Catalog des offres Enterprise. La feuille de route de juin 2026 et la documentation de septembre 2026 ne s'accordent pas sur la nécessité d'un compte. [[SQLMesh]] : oui, dans l'édition libre, par l'analyse SQL de SQLGlot.

**Environnements.** [[dbt Core]] : un environnement est un schéma reconstruit ; `--defer` évite de recalculer les parents, `dbt clone` crée de vraies copies seulement sur Snowflake, Databricks et BigQuery et de simples vues ailleurs. [[SQLMesh]] : environnements **virtuels**, des vues vers des tables physiques identifiées par empreinte ; le calcul déjà fait est réutilisé et la promotion en production ne recopie rien — au prix d'un moteur qui supporte les vues.

**Exécution incrémentale.** [[dbt Core]] : le développeur écrit la branche `is_incremental()`, et le SQL doit rester valide dans les deux cas ; stratégies `append`, `merge`, `delete+insert`, `insert_overwrite`, `microbatch`. [[SQLMesh]] : les intervalles traités sont suivis, les trous détectés et comblés par le plan ; trois kinds ne sont pas idempotents (`UNIQUE_KEY`, `PARTITION`, `UNMANAGED`).

**Moteurs on-prem.** [[dbt Core]] : Postgres, DuckDB, ClickHouse, Spark, Trino, tous `Trusted` sur docs.getdbt.com. [[SQLMesh]] : seize moteurs listés sans niveau de support publié ; Postgres pour l'état ; ClickHouse et Trino y ont des contraintes documentées (swap de partitions, connecteurs Hive/Iceberg/Delta), et ni ClickHouse, ni Spark, ni Trino ne peut héberger l'état.

**Ordonnancement.** Ni l'un ni l'autre n'a d'ordonnanceur libre qui tienne : dbt n'en a aucun hors dbt platform, `sqlmesh run` s'exécute une fois puis s'arrête. Pour dbt, les intégrations documentées passent par [[Airflow]], [[Dagster]], [[Prefect]] et [[Kestra]] ; pour SQLMesh, Kestra figure dans la liste officielle, l'intégration Airflow exige Tobiko Cloud.

**Licence.** [[dbt Core]] v1 et `dbt-oss` : Apache-2.0 ; le binaire « dbt » v2 : licence produit dbt, gratuit et sans compte, y compris hors ligne et chez un client d'ESN dont le déploiement reste autonome. [[SQLMesh]] : Apache-2.0, marques à la Linux Foundation.

**Coût d'adoption.** Partir de [[dbt Core]] : compétences trouvables, exemples partout, un projet Git et un `profiles.yml`. Partir de [[SQLMesh]] : un modèle mental de plan/apply, une base d'état, un cron à poser ; l'adaptateur `sqlmesh[dbt]` exécute un projet dbt tel quel pour essayer sans migrer, mais aucun outil officiel ne convertit en modèles SQLMesh, et les modèles incrémentaux se réécrivent.

**Pas de fiche ici**, faute d'être un outil distinct ou faute d'être éprouvé pour l'on-prem :

- **dbt Fusion** — n'existe plus comme produit à part : son code, d'abord publié sous Elastic License 2.0 (2025-05-28), a été relicencié Apache-2.0 et versé dans `dbt-core` le 2026-06-01 (le dépôt `dbt-fusion` est archivé) ; il est devenu dbt v2, traité dans la fiche [[dbt Core]]. Le binaire complet reste sous licence produit, et Postgres et Trino n'y sont pas supportés.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Data & pipelines]] — le hub du dossier.
- [[ELT vs ETL & idempotence]] — l'ordre d'assemblage dont ces outils sont le T.
- [[Modélisation dimensionnelle]] — ce que ces outils construisent : faits, dimensions, dimensions à historique.
