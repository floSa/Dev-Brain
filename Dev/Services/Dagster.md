---
galaxie: dev
type: service
nom: Dagster
alias: [dagster]
pitch: "Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés."
categorie: data/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Airflow|Airflow]]", "[[Dev/Services/Prefect|Prefect]]", "[[Dev/Services/Mage|Mage]]", "[[Dev/Services/Kestra|Kestra]]", "[[Dev/Services/Temporal|Temporal]]"]
remplace_par: []
status: actif
tags: [orchestration, data-pipeline]
url_docs: https://docs.dagster.io/
url_repo: https://github.com/dagster-io/dagster
---

# Dagster

## Pourquoi

Dagster est un orchestrateur **orienté assets**. Plutôt que d'ordonnancer des tâches opaques, on déclare des **software-defined assets** — les tables, fichiers ou modèles que le pipeline doit produire — et Dagster en déduit le graphe, le **lignage** et les rematérialisations. Typage, tests de données et catalogue d'assets sont de première classe. Écrit en Python par Dagster Labs ; pensé pour la maintenabilité et l'observabilité des plateformes data.

## Quand l'utiliser

- Plateforme data où l'unité utile est la **donnée produite** (tables, datasets) et son lignage, pas la tâche.
- Besoin de tests de données, de typage et d'un catalogue d'assets natif.
- Boucle de développement local soignée (dev loop rapide) et intégration dbt forte.
- Orchestration ELT moderne avec observabilité intégrée.

## Quand NE PAS l'utiliser

- Existant massif en DAGs de tâches ou besoin du plus large catalogue de connecteurs → [[Dev/Services/Airflow|Airflow]].
- Approche purement impérative par fonctions Python → [[Dev/Services/Prefect|Prefect]].
- Déclaratif YAML, indépendant du langage → [[Dev/Services/Kestra|Kestra]].
- ELT visuel low-code → [[Dev/Services/Mage|Mage]].

## Déploiement & coût

- Open-source (Apache-2.0), auto-hébergeable : webserver Dagster + daemon + run launchers. Exécution distribuée sur Kubernetes, Celery, etc.
- Offre managée : Dagster+ (ex-Dagster Cloud), tarification à l'usage (crédits).

## Pièges

- Changement de modèle mental : penser **assets** plutôt que tâches demande un temps d'adaptation en venant d'Airflow.
- API historiquement en évolution rapide (concepts renommés au fil des versions).
- Le tout-asset n'est pas toujours le bon grain pour des jobs purement impératifs — les ops/jobs restent disponibles pour ces cas.

## Alternatives

- [[Dev/Services/Airflow|Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/Mage|Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Dev/Services/Kestra|Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Dev/Services/Temporal|Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie
- Doc : https://docs.dagster.io/
