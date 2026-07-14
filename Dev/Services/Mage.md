---
galaxie: dev
type: service
nom: Mage
alias: [mage, Mage AI, mage-ai]
pitch: "Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation."
categorie: data/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Airflow|Airflow]]", "[[Dev/Services/Dagster|Dagster]]", "[[Dev/Services/Prefect|Prefect]]", "[[Dev/Services/Kestra|Kestra]]", "[[Dev/Services/Temporal|Temporal]]"]
remplace_par: []
status: actif
tags: [orchestration, data-pipeline, low-code]
url_docs: https://docs.mage.ai/
url_repo: https://github.com/mage-ai/mage-ai
---

# Mage

## Pourquoi

Mage (Mage AI) est un orchestrateur **ELT hybride low-code**. Un pipeline s'assemble par **blocs** (data loader → transformer → exporter) dans une UI type notebook, chaque bloc restant du vrai code Python / SQL / R éditable, avec prévisualisation des données à chaque étape. Il vise un démarrage rapide pour l'ingénierie de données sans la lourdeur opérationnelle d'Airflow. Open-source (Apache-2.0), avec une offre managée Mage Pro.

## Quand l'utiliser

- Démarrer vite un pipeline ELT avec un éditeur visuel et un feedback immédiat (preview des données par bloc).
- Petite équipe ou profils data analysts à l'aise en notebook, sans vouloir opérer un cluster Airflow.
- Intégration et transformation de données avec dbt et les connecteurs courants.

## Quand NE PAS l'utiliser

- Orchestration à grande échelle, distribuée, mission-critique → [[Dev/Services/Airflow|Airflow]] ou [[Dev/Services/Kestra|Kestra]].
- Modèle orienté **assets** et lignage de données → [[Dev/Services/Dagster|Dagster]].
- Workflows Python dynamiques et résilients définis par code → [[Dev/Services/Prefect|Prefect]].

## Déploiement & coût

- Open-source (Apache-2.0), auto-hébergeable : application unique avec scheduler intégré (déploiement Docker ; Kubernetes avec executors pour répartir les tâches).
- Offre managée : Mage Pro (RBAC, multi-environnements, assistance IA, monitoring).
- Positionnement plus léger (single-node par défaut) que les orchestrateurs distribués de la catégorie.

## Pièges

- L'OSS avance moins vite depuis le virage vers Mage Pro (offre managée) — surveiller la vélocité du projet.
- L'UI par blocs masque des conventions de structure de projet — utile de comprendre l'arborescence générée.
- Moins de connecteurs et d'écosystème qu'Airflow.

## Alternatives

- [[Dev/Services/Airflow|Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dev/Services/Dagster|Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/Kestra|Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Dev/Services/Temporal|Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie
- Doc : https://docs.mage.ai/
