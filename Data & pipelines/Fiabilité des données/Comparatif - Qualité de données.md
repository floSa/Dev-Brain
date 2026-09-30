---
role: comparatif
nom: Comparatif - Qualité de données
categorie: data/fiabilite
tags: [data-quality, data-validation, data-contract]
---

# Comparatif - Qualité de données

> On tranche sur : où vit la donnée qu'on vérifie (un DataFrame en mémoire ou une table en base), comment les règles se déclarent (du code ou un fichier), ce que l'outil sait dire de ses résultats sans service payant, l'intégration à l'orchestrateur, et la licence.

![[Comparatif - Qualité de données.base]]

## Ce qui départage

- [[Great Expectations]] — le **plus installé** (environ 19,3 M de téléchargements PyPI par mois) et le seul à produire un rapport HTML lisible par des non-développeurs, les Data Docs. Suites d'Expectations en Python, sur tables SQL (PostgreSQL, Trino, Oracle, SQL Server…), pandas et Spark. Le prix : cinq objets à chaîner pour une validation, une migration 0.x vers 1.x cassante qui a périmé les intégrations tierces, ClickHouse, DuckDB et Polars hors de la liste supportée, et un cloud (historique, alertes) vendu à FICO puis fermé au public le 2026-06-01.
- [[Soda Core]] — les règles en **YAML**, exécutées **dans la base** par une commande dont le code de sortie (0 à 4) se branche sur n'importe quel pipeline. Le prix : la licence, passée d'Apache-2.0 à Elastic 2.0 en v4 (source-available, PyPI affiche `Proprietary`), aucune documentation d'intégration Airflow, Dagster, Prefect ni dbt dans la v4, et un historique, des alertes et une détection d'anomalies réservés à Soda Cloud.
- [[pandera]] — le **schéma comme code** : `DataFrameSchema` ou `DataFrameModel` typé, checks vectorisés, validation paresseuse qui remonte toutes les erreurs, pour pandas, Polars, PySpark et Ibis, sans serveur. Le prix : il ne sait pas valider une table en base sans la charger, ne produit ni rapport ni historique, et beaucoup de ses fonctions (inférence, YAML, synthèse de données) sont propres à pandas.

**Critère par critère**

**Déclaratif ou code.** [[Soda Core]] est le seul déclaratif : un contrat YAML par jeu de données, versionnable et relisible hors des développeurs Python. [[Great Expectations]] en 1.x s'écrit entièrement en Python (source, asset, batch, suite, validation, checkpoint). [[pandera]] s'écrit en Python aussi, mais c'est un type : le schéma s'utilise en annotation (`DataFrame[MonSchema]`) et se valide aux frontières des fonctions.

**DataFrame ou base.** Vérifier **dans la base**, en SQL, sans rapatrier les lignes : [[Soda Core]] (PostgreSQL, Trino, SQL Server, Spark, Athena, BigQuery, Snowflake…) et [[Great Expectations]] (liste de compatibilité officielle, dont PostgreSQL et Trino). Vérifier un **DataFrame** : [[pandera]] pour pandas, Polars, PySpark et Ibis ; [[Great Expectations]] pour pandas et Spark seulement, pas Polars ; [[Soda Core]] enregistre un DataFrame pandas ou Polars comme table DuckDB en mémoire. ClickHouse : aucun des trois ne le supporte officiellement (GX : « déjà vu fonctionner, sans garantie » ; Soda v4 : absent ; pandera : uniquement via Ibis, non documenté).

**Intégration à l'orchestrateur.** [[Great Expectations]] : un provider [[Airflow]] officiel (1.0.0, 2026-01-28) ; `dagster-ge` exige GX < 1.0 et `prefect-great-expectations` n'a pas bougé depuis 2023. [[Soda Core]] : CLI et API Python, exécutables par n'importe quelle tâche ; les guides Airflow, Dagster, Prefect et dbt existent pour la v3, périmés. [[pandera]] : `dagster-pandera` (bêta, DataFrames pandas), sinon un simple appel Python dans une tâche.

**Rapports et historique.** [[Great Expectations]] : Data Docs, un site statique à publier soi-même ; pas d'historique depuis la fermeture de GX Cloud. [[Soda Core]] : console, logs et codes de sortie ; l'historique passe par Soda Cloud ou un *Runner*. [[pandera]] : `failure_cases` (un DataFrame) et un rapport d'erreur JSON ; rien d'autre.

**Licence.** [[Great Expectations]] : Apache-2.0. [[pandera]] : MIT. [[Soda Core]] : Elastic License 2.0 sur `main` — usage interne, production et conseil permis, service hébergé à des tiers interdit — avec une branche v3 Apache-2.0 figée depuis 2025-09-24. À dire au client avant de livrer.

**Gouvernance.** [[Great Expectations]] : dépôt sous `fivetran/great_expectations` depuis 2026, Fivetran « steward » du cœur. [[pandera]] : Union.ai depuis 2022, sans fondation. [[Soda Core]] : Soda Data N.V., une version par semaine.

**À quoi ressemble une règle**, extraits des documentations officielles (raccourcis) :

[[Great Expectations]], guide *Try GX* — une Expectation, à enchaîner avec une *Validation Definition* et un *Checkpoint* :

```python
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
    column="passenger_count", min_value=1, max_value=6, severity="warning"))
```

[[Soda Core]], README — un contrat, lancé par `soda contract verify -ds ds_config.yml -c contract.yml` :

```yaml
dataset: postgres_ds/db/schema/dataset
checks:
  - schema:
  - row_count:
columns:
  - name: size
    checks:
      - invalid:
          valid_values: ['S', 'M', 'L']
```

[[pandera]], *Quick Start* — un schéma, appliqué par `schema.validate(df)` :

```python
schema = pa.DataFrameSchema({
    "column1": pa.Column(int, pa.Check.ge(0)),
    "column2": pa.Column(float, pa.Check.lt(10)),
    "column3": pa.Column(str, [pa.Check.isin([*"abc"])]),
})
```

**Voisin, pas alternative** : [[Evidently]] surveille la **dérive** d'un jeu de données et la performance d'un modèle en production (rapports, métriques), là où ces trois outils testent des règles connues à l'avance sur un lot livré. On les pose côte à côte plutôt que l'un à la place de l'autre.

**Pas de fiche ici**, faute de passer le critère « éprouvé et utile en on-prem » (le plafond du lot est de cinq briques, atteint avec ces trois outils et les deux de transformation) :

- **Deequ / PyDeequ** (awslabs, Apache-2.0) — Deequ 2.1.0 (2026-09-16), environ 3 650 étoiles ; PyDeequ 1.7.0 (2026-09-14), environ 830 étoiles. Bibliothèque Scala sur Apache Spark : à considérer seulement si Spark est déjà sur le site.
- **Pointblank** (Posit, MIT) — 0.27.0 (2026-08-13), environ 490 étoiles, environ 17 000 téléchargements mensuels. Valide directement PostgreSQL, DuckDB, Polars, pandas et produit un rapport HTML ; à surveiller, l'adoption est faible.
- **Elementary** (Apache-2.0) — 0.26.0 (2026-09-10), environ 2 400 étoiles. Une couche d'observabilité au-dessus des tests dbt (rapport HTML, alertes) et non un concurrent des trois : une fiche se justifierait avec [[dbt Core]] déjà en place, sa version Cloud est payante.
- **dbt-expectations** — le dépôt d'origine (calogica) n'est plus maintenu ; le fork `metaplane/dbt-expectations` (Apache-2.0, 0.10.10 du 2025-12-02, environ 160 étoiles) reprend les tests de type Great Expectations comme paquet dbt. À mentionner, pas à fiche.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Fiabilité des données]] — le hub du dossier.
- [[Contrats de données & qualité]] — la notion : ce qu'un contrat garantit, où poser les portes de qualité.
- [[Architecture médaillon]] — le passage Bronze vers Silver où ces outils se posent.
