---
role: brique
nom: Prefect
alias: [prefect]
pitch: "Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Airflow]]", "[[Dagster]]", "[[Mage]]", "[[Kestra]]", "[[Temporal]]"]
complements: []
tags: [orchestration, data-pipeline]
url_docs: https://docs.prefect.io/
url_repo: https://github.com/PrefectHQ/prefect
---

# Prefect

## Pourquoi

Prefect est un orchestrateur **Python natif**. Des décorateurs `@flow` et `@task` transforment des fonctions ordinaires en workflows observables, sans DAG statique à déclarer : le graphe se construit à l'exécution, ce qui rend les pipelines **dynamiques** (boucles, branches conditionnelles) naturels. Prefect 3.0 (2024) ajoute des sémantiques transactionnelles (rollback) et réduit fortement l'overhead par rapport à la v2. Conçu pour rendre du code Python existant résilient avec un minimum de friction.

## Quand l'utiliser

- Transformer rapidement des scripts Python en workflows orchestrés — retries et observabilité inclus.
- Pipelines **dynamiques** dont le graphe dépend des données ou de la logique au runtime.
- Préférence pour du code impératif plutôt qu'un DAG déclaré d'avance.
- Déploiement hybride : workers proches de l'infra, plan de contrôle managé via Cloud.

## Quand NE PAS l'utiliser

- Besoin du plus grand catalogue de connecteurs et du standard historique → [[Airflow]].
- Orientation **assets** et lignage de données de première classe → [[Dagster]].
- Déclaratif YAML, indépendant du langage → [[Kestra]].
- ELT visuel low-code → [[Mage]].

## Déploiement & coût

- Open-source (Apache-2.0), auto-hébergeable : serveur Prefect + workers rattachés à des work pools. Exécution distribuée ; intégrations [[Dask]] / Ray pour le parallélisme.
- Offre managée : Prefect Cloud (palier gratuit, Pro à partir d'environ 100 $/mois).

## Pièges

- Refonte majeure entre Prefect 1 (« Core », DAG) et 2/3 (dynamique) : docs et patterns d'avant la 2.0 obsolètes.
- L'absence de DAG statique complique la visualisation a priori d'un pipeline avant son exécution.
- Bien dimensionner work pools et workers pour la concurrence sous charge.

## Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie
- Doc : https://docs.prefect.io/
