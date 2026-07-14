---
galaxie: dev
type: service
nom: Airflow
alias: [airflow, Apache Airflow]
pitch: "Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data."
categorie: data/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Dagster|Dagster]]", "[[Dev/Services/Prefect|Prefect]]", "[[Dev/Services/Mage|Mage]]", "[[Dev/Services/Kestra|Kestra]]", "[[Dev/Services/Temporal|Temporal]]"]
remplace_par: []
status: actif
tags: [orchestration, data-pipeline, scheduler]
url_docs: https://airflow.apache.org/docs/
url_repo: https://github.com/apache/airflow
---

# Airflow

## Pourquoi

Apache Airflow est l'ordonnanceur de workflows de référence en data engineering. Un pipeline s'exprime comme un **DAG** (graphe orienté acyclique) de tâches défini en **Python** ; un scheduler en planifie l'exécution (cron ou intervalle), gère les dépendances, les reprises et les back-fills. Son écosystème d'**operators / providers** (des centaines de connecteurs) en fait le couteau suisse de l'orchestration batch. Projet de l'Apache Software Foundation ; Airflow 3.0 (GA avril 2025) introduit une architecture client-serveur (Task Execution API) et l'Edge Executor pour l'exécution distante.

## Quand l'utiliser

- Orchestrer des pipelines batch planifiés (ETL/ELT, entraînements ML, rapports) avec dépendances complexes.
- Besoin d'un large catalogue de connecteurs prêts à l'emploi (bases, cloud, outils data).
- Écosystème mûr et compétences répandues recherchés — le standard de fait, large communauté.
- Exécution distribuée via Celery, Kubernetes ou Edge Executor.

## Quand NE PAS l'utiliser

- Pipelines pensés autour des **données produites** plutôt que des tâches → [[Dev/Services/Dagster|Dagster]] (assets, lignage, tests).
- Workflows très dynamiques et pythoniques sans DAG statique → [[Dev/Services/Prefect|Prefect]].
- Équipe non-Python ou besoin déclaratif YAML → [[Dev/Services/Kestra|Kestra]].
- ELT léger et visuel, prototypage rapide → [[Dev/Services/Mage|Mage]].
- Streaming temps réel — Airflow est un orchestrateur batch, pas un moteur de flux.

## Déploiement & coût

- Open-source (Apache-2.0), gratuit, auto-hébergé : scheduler + webserver + workers + une base de métadonnées ([[Dev/Services/Postgres|Postgres]]). Distribution via CeleryExecutor ou KubernetesExecutor.
- Offres managées : Amazon MWAA, Google Cloud Composer, Astronomer (Astro).
- Lourd à opérer soi-même (plusieurs composants + broker) — c'est le prix de sa flexibilité.

## Pièges

- Le scheduler raisonne en intervalles : la `logical_date` (ex-`execution_date`) est le **début** de l'intervalle, pas l'instant d'exécution — confusion classique.
- Le code des DAGs est ré-importé à chaque parse → garder le top-level léger, pas de travail lourd au niveau module.
- Passage de données entre tâches via XCom limité (métadonnées, pas gros volumes) → passer par un stockage externe.
- Migration 2.x → 3.0 : changements d'architecture et d'API non triviaux.

## Alternatives

- [[Dev/Services/Dagster|Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/Mage|Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Dev/Services/Kestra|Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Dev/Services/Temporal|Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie
- Doc : https://airflow.apache.org/docs/
