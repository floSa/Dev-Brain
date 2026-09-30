---
role: brique
nom: pandera
alias: [Pandera, pandera-pandas]
pitch: "Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT)."
categorie: data/fiabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Great Expectations]]", "[[Soda Core]]"]
complements: ["[[pandas]]", "[[Polars]]", "[[Spark]]", "[[Pydantic]]", "[[Dagster]]"]
tags: [data-validation, data-quality, dataframe]
url_docs: https://pandera.readthedocs.io/
url_repo: https://github.com/unionai-oss/pandera
---

# pandera

<!-- AUTO:BANDEAU:START -->
> Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui valide un DataFrame contre un **schéma**. Le schéma se déclare en objet
(`DataFrameSchema`, `Column`, `Check`) ou en classe typée (`DataFrameModel`, sur le modèle de
Pydantic) : colonnes, types, et **checks** vectorisés — bornes, appartenance à une liste, contrôle
sur mesure. `schema.validate(df)` renvoie le DataFrame ou lève une erreur ; avec `lazy=True`, toutes
les violations sont collectées dans `SchemaErrors.failure_cases`. Des décorateurs (`check_types`,
`check_input`, `check_output`) valident aux frontières des fonctions. Le backend pandas est le plus
riche ; Polars, PySpark SQL et Ibis sont de première classe, Dask, Modin et GeoPandas passent par
le backend pandas.

Relevé le 2026-09-30 : **0.33.1** (2026-09-01), environ 4 470 étoiles, **MIT**, 8,17 M de
téléchargements PyPI en 30 jours, dernier commit le 2026-09-26, six versions stables en six mois.
Le dépôt est `unionai-oss/pandera` (une ancienne adresse `pandera-dev` y redirige) : projet open
source d'Union.ai, l'éditeur de Flyte, depuis le 2022-10-03 ; aucune fondation, aucun changement de
gouvernance récent trouvé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| La donnée vit dans un DataFrame en mémoire, au milieu d'un code Python : la validation se pose à la frontière d'une fonction ou dans les tests | Valider des tables **en base** sans les charger : pandera n'a aucune API de connexion SQL, et seul le backend Ibis s'en approche — la documentation ne cite ni PostgreSQL ni ClickHouse |
| Un schéma réutilisable comme type (`DataFrame[MonSchema]`), lisible comme un modèle Pydantic, avec coercition de types | Un rapport lisible par des non-développeurs, un historique ou des tendances : il n'y a que `failure_cases` et un rapport d'erreur JSON |
| Polars, PySpark ou pandas, sans serveur ni compte : c'est un `import` | Du profilage ou de la surveillance dans le temps : l'inférence de schéma ne produit qu'un brouillon, pandas seulement |
| Dagster : un paquet `dagster-pandera` existe (bêta) | Des volumes qui ne tiennent pas en mémoire pour les checks de valeurs en pandas : la documentation avertit d'un surcoût à l'exécution |

## Mise en œuvre

- Installation — `uv add "pandera[pandas]"` (import `pandera.pandas`) ; un extra par backend : `polars`, `pyspark`, `ibis`, `modin`, `dask`, `geopandas` ; `io` pour le YAML, `cli` pour la ligne de commande, `strategies` et `hypotheses` en option ; Python ≥ 3.10
- Point d'entrée — `pa.DataFrameSchema` ou `pa.DataFrameModel`, `.validate(df, lazy=True)`, `@pa.check_types` ; une commande `pandera` (`validate`, `infer`, `generate`) apparue en 0.33.0
- Prérequis — le DataFrame déjà chargé. Sur une `LazyFrame` Polars, seuls les noms et les types sont contrôlés sans `.collect()`. **Beaucoup de fonctions sont propres à pandas** : inférence de schéma, YAML, données synthétiques, tests d'hypothèse, *parsers*, intégrations FastAPI et Pydantic. Les variables `PANDERA_VALIDATION_ENABLED` et `PANDERA_VALIDATION_DEPTH` (`SCHEMA_ONLY`, `DATA_ONLY`, `SCHEMA_AND_DATA`) coupent le coût en production
- Exécution — un appel Python dans le code. Pour Dagster, `dagster-pandera` (0.29.24, 2026-09-21) est en bêta et limité aux DataFrames pandas ; pour Airflow et Prefect, aucune documentation côté pandera : un simple appel Python
- Coût — gratuit, MIT

## Limites à connaître

- **Aucun suivi historique** ni profilage : l'absence de ces fonctions est constatée dans la documentation, elle n'y est pas déclarée.
- **Couverture inégale selon le backend** : Ibis et PySpark n'ont pas `drop_invalid_rows`, Ibis n'a pas de types imbriqués paramétrés ni d'horodatages sans fuseau ; PyArrow passe par le backend Narwhals, où `coerce=True` n'est pas implémenté.
- **Ibis pour valider en base** : les checks de valeurs exécutent des requêtes sur le moteur, ceux de métadonnées non ; la nature exacte de la poussée vers le moteur n'est pas documentée. PostgreSQL et ClickHouse sont à essayer avant de l'affirmer à un client.
- **Changement d'import** : `import pandera as pa` pour pandas est remplacé par `pandera.pandas` ; les métadonnées PyPI pointent encore vers l'ancienne adresse du dépôt.

## Écosystème

### Alternatives

- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026.
- [[Soda Core]] — Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud.
- [[Evidently]] — voisin : surveille la dérive d'un jeu de données et la performance d'un modèle en production (Apache-2.0, 0.7.23 du 2026-09-11), là où cet outil teste des règles connues à l'avance sur un lot livré.

### Compléments

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — backend le plus riche : seul à offrir l'inférence de schéma, le YAML, les tests d'hypothèse et les intégrations FastAPI et Pydantic.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. — backend natif de première classe ; sur une `LazyFrame`, seuls les noms et les types sont contrôlés, sans `.collect()`.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — PySpark SQL est de première classe (schéma, modèle, checks, validation paresseuse), par l'extra `pyspark`.
- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires. — intégration dans les deux sens : un champ `DataFrame[Schema]` dans un modèle Pydantic, ou un modèle Pydantic comme validateur ligne à ligne, au prix d'une performance dégradée sur les gros jeux d'après la documentation.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés. — `dagster-pandera` (0.29.24, 2026-09-21, Apache-2.0, bêta) génère un type Dagster dont le contrôle appelle `validate()` ; pandas et Polars.

## Ressources

- Documentation — https://pandera.readthedocs.io/
- Dépôt — https://github.com/unionai-oss/pandera
- Documentation — https://pandera.readthedocs.io/en/stable/supported_libraries.html
- Article — https://www.union.ai/blog-post/pandera-joins-union-ai

## Voir aussi

- [[Fiabilité des données]] — le hub du dossier
- [[Comparatif - Qualité de données]] — ce qui départage Great Expectations, Soda Core et pandera
- [[Contrats de données & qualité]] — ce qu'un contrat de données garantit, et ce qu'un outil vérifie
