---
role: brique
nom: Soda Core
alias: [Soda, soda-core, Soda Core 4, SodaCL]
pitch: "Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud."
categorie: data/fiabilite
famille: cli
licence_type: source-available
maturite: production
langage: Python
alternatives: ["[[Great Expectations]]", "[[pandera]]"]
complements: ["[[Postgres]]", "[[DuckDB]]"]
tags: [data-quality, data-contract, data-validation]
url_docs: https://docs.soda.io/
url_repo: https://github.com/sodadata/soda-core
---

# Soda Core

<!-- AUTO:BANDEAU:START -->
> Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | source-available | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de vérification de la qualité des données par **contrats**. Un fichier YAML décrit un jeu de
données (`dataset`), ses contrôles de table (schéma, nombre de lignes) et ceux de chaque colonne
(`missing`, `invalid` avec `valid_values`…) ; `soda contract verify` les exécute **dans la
source**, en SQL, et rend un code de sortie exploitable par un pipeline : 0 tout passe, 1 au moins
un contrôle échoue, 2 avertissements seulement, 3 vérification impossible à exécuter, 4 résultats
non envoyés à Soda Cloud. Une API Python (`verify_contract_locally`) fait la même chose dans du
code. La v4, sortie le 2026-01-28, a remplacé le langage de contrôles SodaCL de la v3 par ces
contrats.

Relevé le 2026-09-30 : **4.25.0** (2026-09-23), environ 2 430 étoiles, une version par semaine
depuis juillet. **Licence : Elastic License 2.0** sur la branche `main`, depuis le passage annoncé
le 2026-01-27 — avant, Apache-2.0. Les sources sont lisibles, la licence n'est pas OSI :
usage interne, production, modification, conseil, intégration, formation et support restent
permis ; offrir Soda Core comme service hébergé ou managé à des tiers, ou contourner une fonction
de clé de licence, ne l'est pas. La branche `v3` (3.5.6 du 2025-09-24, figée) reste Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des contrôles écrits en YAML, lisibles hors des développeurs Python, versionnés dans Git et lancés en CLI avec un code de sortie exploitable en CI ou par un orchestrateur | Une licence OSI exigée par le client, ou Soda Core à héberger ou redistribuer à des tiers : l'ELv2 l'interdit, et la v3 Apache est figée depuis septembre 2025 |
| Vérifier **dans la base**, sans rapatrier les lignes : PostgreSQL, Trino, SQL Server, DuckDB, Spark, Athena, BigQuery, Snowflake… | Des tables **ClickHouse** : absentes de la documentation v4 (la v3 annonçait un support indirect par `soda-mysql`) |
| Un usage interne ou de conseil : l'ELv2 le couvre explicitement | Un historique des mesures, de la détection d'anomalies, des alertes ou des tableaux de bord **sans** Soda Cloud : ils lui sont réservés |
| Des DataFrames pandas ou Polars vérifiés avec le même langage de contrats, via DuckDB | Une migration à faible coût depuis des contrôles v3 : l'outil de conversion est sur le PyPI privé, et réconciliation, *group by* et détection d'anomalies ne sont pas migrés |

## Mise en œuvre

- Installation — `uv add soda-postgres` (un paquet par source : `soda-trino`, `soda-duckdb`, `soda-sqlserver`, `soda-sparkdf`, `soda-athena`…) ; Python ≥ 3.10
- Point d'entrée — `soda contract verify -ds ds_config.yml -c contract.yml` ; `soda contract publish` pour publier vers Soda Cloud ; API Python `verify_contract_locally`
- Prérequis — un fichier de configuration de la source. **Oracle et MySQL** viennent du PyPI **privé** de Soda, sous licence Team ou Enterprise. Les métadonnées PyPI des paquets v4 affichent `Proprietary` alors que le dépôt porte l'ELv2 : la contradiction n'est pas tranchée par Soda, à faire lever avant toute redistribution. Le code n'a pas été lu ici pour confirmer l'absence d'un verrou de clé de licence dans le CLI local
- Exécution — un processus CLI ou Python, sans serveur ; résultats en console, en logs et en codes de sortie, **sans rapport HTML**. L'historique passe par `--publish` vers Soda Cloud ou par un *Runner* (ex-Agent) hébergé par Soda ou sur Kubernetes. La documentation v4 ne contient aucune page Airflow, Dagster, Prefect ni dbt : les guides v3 existent, périmés
- Coût — Core gratuit. Soda Cloud : offre gratuite « pour petits projets » (trois jeux de données d'après le README), Team à 750 $ par mois, Enterprise sur devis (soda.io/pricing, relevé le 2026-09-30)

## Limites à connaître

- **Rupture v3 → v4** : le langage de contrôles change, la migration automatique est payante, et les paquets v3 figés restent plus téléchargés que les v4 pour Postgres et Trino — le parc n'a pas suivi.
- **Documentation à deux vitesses** : une partie n'est visible que connecté à Soda Cloud. La page de déploiement liste l'observabilité comme dépendante d'un *Runner*.
- **Installation ambiguë** : la documentation renvoie parfois vers `pypi.cloud.soda.io --pre` alors que pypi.org héberge la 4.25.0.
- **Adoption difficile à lire** : le paquet `soda-core` totalise 1,78 M de téléchargements en 30 jours, sans commune mesure avec les paquets par source (3 653 pour `soda-postgres`) ; ce chiffre n'est pas interprété ici.

## Écosystème

### Alternatives

- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026.
- [[pandera]] — Validation de DataFrames en Python par schémas déclaratifs ou modèles typés (pandas, Polars, PySpark, Ibis) : checks vectorisés, validation paresseuse qui remonte toutes les erreurs, sans rapport ni historique (MIT).
- [[Evidently]] — voisin : surveille la dérive d'un jeu de données et la performance d'un modèle en production (Apache-2.0, 0.7.23 du 2026-09-11), là où cet outil teste des règles connues à l'avance sur un lot livré.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — paquet `soda-postgres` : les contrôles s'exécutent en SQL dans la base.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — un DataFrame pandas ou Polars est enregistré dans un DuckDB en mémoire, puis le contrat est vérifié sur cette vue (paquet `soda-duckdb`).

## Ressources

- Documentation — https://docs.soda.io/
- Dépôt — https://github.com/sodadata/soda-core
- Article — https://soda.io/blog/soda-core-license-update-moving-to-elastic-license
- Documentation — https://docs.soda.io/reference/migrate-from-v3-to-v4

## Voir aussi

- [[Fiabilité des données]] — le hub du dossier
- [[Comparatif - Qualité de données]] — ce qui départage Great Expectations, Soda Core et pandera
- [[Contrats de données & qualité]] — ce qu'un contrat de données garantit, et ce qu'un outil vérifie
- [[Architecture médaillon]] — les portes de qualité entre couches
