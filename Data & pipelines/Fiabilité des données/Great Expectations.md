---
role: brique
nom: Great Expectations
alias: [GX, GX Core, great_expectations, great-expectations]
pitch: "Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026."
categorie: data/fiabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Soda Core]]", "[[pandera]]"]
complements: ["[[Airflow]]", "[[Postgres]]", "[[pandas]]", "[[Spark]]"]
tags: [data-quality, data-validation, data-contract]
url_docs: https://docs.greatexpectations.io/
url_repo: https://github.com/fivetran/great_expectations
---

# Great Expectations

<!-- AUTO:BANDEAU:START -->
> Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui vérifie qu'un jeu de données respecte ce qu'on en attend. On déclare des
**Expectations** — assertions sur une table ou une colonne : valeurs entre deux bornes, non
nulles, uniques, dans une liste — groupées en **suite**. Une **Validation Definition** relie une
suite à un **Batch Definition** (la tranche d'un *Data Asset* : table SQL, DataFrame, fichier),
et un **Checkpoint** exécute une ou plusieurs validations puis déclenche des actions (e-mail,
Slack, Teams, action sur mesure). Les résultats se rendent en **Data Docs**, un site HTML
statique où les règles et leurs résultats sont lisibles par des non-développeurs. Depuis la 1.0,
tout s'écrit en Python.

Relevé le 2026-09-30 : **1.23.2** (PyPI le 2026-09-25, tag GitHub le 2026-09-28), environ 11 850
étoiles, **Apache-2.0**, cadence de deux semaines sans trou depuis juin, environ 19,3 M de
téléchargements PyPI en 30 jours. Le dépôt vit désormais sous `fivetran/great_expectations`
(l'ancienne adresse redirige) : le 2026-05-06, GX a annoncé que **FICO acquiert GX Cloud**, fermé
au public le 2026-06-01, et que **Fivetran devient le « steward »** de GX Core, qui continue « piloté par la
communauté ».

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des suites de règles versionnées dans le code, partagées entre équipes, avec un rapport HTML publiable sur un serveur web interne | Des tables **ClickHouse** : la documentation les classe « déjà vues fonctionner, sans garantie » ; DuckDB est absent de la liste des sources et Polars n'est pas supporté |
| Valider des tables PostgreSQL, Trino, Oracle (21c), SQL Server, Snowflake ou des DataFrames pandas et Spark, d'après la liste officielle de compatibilité | Un historique des résultats, des alertes évoluées ou une interface : c'était GX Cloud, qui n'est plus vendu ; il reste les Data Docs et les actions de Checkpoint |
| Airflow comme orchestrateur : un provider officiel existe (1.0.0, 2026-01-28) | Des déclarations en YAML plutôt qu'en code : la 1.x n'en a pas |
| Une bibliothèque sans compte, sans cloud, sans serveur | Dagster ou Prefect : leurs intégrations pour GX sont bloquées sur la série 0.x |

## Mise en œuvre

- Installation — `uv add great-expectations` (Python 3.10 à 3.13, le 3.14 est expérimental derrière une variable d'environnement) ; un extra par source : `postgresql`, `trino`, `spark`, `oracle`…
- Point d'entrée — `gx.get_context()`, puis source de données → *Data Asset* → *Batch Definition* → suite d'Expectations → *Validation Definition* → *Checkpoint*, lancé par `checkpoint.run()`
- Prérequis — **cinq objets à enchaîner** pour une seule validation. La migration de la 0.x vers la 1.x est cassante (plus de *Validator*, plus de `batch_request`, Custom Expectations réécrites) et la 0.18 est en fin de vie depuis le 2025-10-01 : beaucoup de tutoriels et d'intégrations tierces sont périmés. Windows est indiqué « non supporté » par la table de compatibilité, même si des déploiements y fonctionnent
- Exécution — un processus Python (script, tâche d'orchestrateur, CI), sans serveur. Les Data Docs sont des fichiers à publier soi-même (`uncommitted/data_docs/local_site/` par défaut) ; seul `base_directory` est configurable
- Coût — gratuit en Apache-2.0. GX Cloud, l'offre payante, n'est plus disponible au public depuis le 2026-06-01 ; il n'existe plus d'édition GX payante à comparer

## Limites à connaître

- **Deux changements de propriétaire en 2026** (FICO pour le cloud, Fivetran pour le cœur) et une feuille de route non documentée sous Fivetran. La licence du cœur n'a pas changé.
- **Un contributeur domine le flux récent** : 10 des 20 derniers commits relevés viennent d'un seul auteur.
- **Dagster** : `dagster-ge` (0.29.24, 2026-09-21) impose `great-expectations<1.0.0` ; **Prefect** : `prefect-great-expectations` n'a pas eu de version depuis 2023-11-13. La documentation de GX dit que l'outil « devrait fonctionner avec tout orchestrateur qui exécute du Python ».
- **dbt** : un tutoriel Docker Compose (Postgres, dbt, GX, Airflow), pas de plugin.
- Les rapports décrivent le passé d'une exécution : GX ne garde ni tendance, ni comparaison entre deux jours.

## Écosystème

### Alternatives

- [[Soda Core]] — Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud.
- [[pandera]] — Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT).
- [[Evidently]] — voisin : surveille la dérive d'un jeu de données et la performance d'un modèle en production (Apache-2.0, 0.7.23 du 2026-09-11), là où cet outil teste des règles connues à l'avance sur un lot livré.

### Compléments

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — provider officiel `airflow-provider-great-expectations` (1.0.0, 2026-01-28, Apache-2.0, maintenu par Astronomer avec GX) : trois opérateurs, pour un DataFrame pandas ou Spark en mémoire, pour des données externes par une Batch Definition, et pour un Checkpoint.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — source SQL de la liste de compatibilité officielle de GX (extra `postgresql`).
- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — les DataFrames pandas se valident par `context.data_sources.add_pandas(...)` ; Polars n'est pas supporté.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — les DataFrames Spark se valident par `add_spark(...)` (extra `spark`) et Spark figure dans la liste de compatibilité officielle.

## Ressources

- Documentation — https://docs.greatexpectations.io/
- Dépôt — https://github.com/fivetran/great_expectations
- Documentation — https://docs.greatexpectations.io/docs/help/compatibility_reference
- Documentation — https://docs.greatexpectations.io/docs/reference/learn/migration_guide
- Article — https://greatexpectations.io/blog/an-update-from-great-expectations/

## Voir aussi

- [[Fiabilité des données]] — le hub du dossier
- [[Comparatif - Qualité de données]] — ce qui départage Great Expectations, Soda Core et pandera
- [[Contrats de données & qualité]] — ce qu'un contrat de données garantit, et ce qu'un outil vérifie
- [[Architecture médaillon]] — les portes de qualité entre couches
