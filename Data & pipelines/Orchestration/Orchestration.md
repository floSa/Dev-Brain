---
role: hub
nom: Orchestration
alias: [orchestrateurs data]
pitch: Faire tourner des traitements dans le bon ordre, à l'heure, et savoir quoi rejouer quand l'un d'eux échoue.
domaines: [data-eng, mlops]
tags: [orchestration, data-pipeline, durable-execution, idempotence]
---

# Orchestration

> Faire tourner des traitements dans le bon ordre, à l'heure, et savoir quoi rejouer quand l'un d'eux échoue.

## Ce qu'il faut comprendre

- Un orchestrateur ne calcule rien. Il tient l'**ordre**, les **reprises** et l'**observabilité** ; le calcul reste dans les tâches. C'est pourquoi le remplacer est moins coûteux qu'il n'y paraît, et pourquoi un orchestrateur ne compense jamais un pipeline non rejouable — cf. [[ELT vs ETL & idempotence]].
- Le clivage le plus profond du domaine est **qu'est-ce qu'on déclare**. La tradition déclare des **tâches** et leurs dépendances ([[Airflow]]) ; [[Dagster]] déclare les **données à produire** et en déduit le graphe. Le second modèle donne le lignage et les tests de données presque gratuitement, et impose de repenser ses pipelines — ce n'est pas une migration de syntaxe.
- Le second clivage est **où vit la définition** : en Python ([[Airflow]], [[Prefect]], [[Dagster]]), en YAML ([[Kestra]]), ou dans une UI par blocs ([[Mage]]). Ce choix décide de qui peut modifier un pipeline, ce qui est une question d'équipe plus que de technique.
- Le troisième sépare deux familles qu'on confond : l'orchestration **par lots planifiés** et l'**exécution durable**. [[Temporal]] n'est pas un ordonnanceur de DAG : il persiste l'état d'un programme à chaque étape pour qu'il reprenne après panne, y compris sur des exécutions de plusieurs jours. Le besoin « mon traitement ne doit jamais perdre son avancement » est le sien, pas celui d'[[Airflow]].
- La **planification statique contre le graphe dynamique** est la limite qu'on rencontre en dernier et qui fait migrer : un DAG déclaré à l'avance ne sait pas boucler sur un nombre d'éléments découvert à l'exécution. [[Prefect]] est né de ce point.

## Choisir

- Un standard éprouvé, un vaste catalogue de connecteurs, des compétences trouvables → [[Airflow]].
- Le lignage, la qualité des données et les assets au centre → [[Dagster]].
- Des workflows dynamiques, du Python idiomatique, sans DAG statique → [[Prefect]].
- Une orchestration déclarative en YAML, découplée du langage des tâches → [[Kestra]].
- Une UI type notebook, pour une équipe peu outillée en Python → [[Mage]].
- Un état applicatif à ne jamais perdre, des exécutions longues, des reprises exactes → [[Temporal]].
- Du traitement au fil de l'eau plutôt que planifié → [[Flink]], pas ce sous-domaine.

<!-- AUTO:START -->
### Briques
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

### Comparatifs
- [[Comparatif - Orchestrateurs data]]
<!-- AUTO:END -->
