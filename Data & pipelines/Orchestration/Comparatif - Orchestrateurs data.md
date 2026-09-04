---
role: comparatif
nom: Comparatif - Orchestrateurs data
categorie: data/orchestration
tags: [orchestration, data-pipeline, scheduler, durable-execution]
---

# Comparatif - Orchestrateurs data

> On tranche sur : ce que le pipeline déclare — une tâche, une donnée produite, un YAML, ou un processus métier qui doit survivre au crash.

![[Comparatif - Orchestrateurs data.base]]

## Ce qui départage

- [[Airflow]] — le **DAG de tâches** en Python et le plus large catalogue d'**operators / providers**, donc le standard de fait et les compétences les plus répandues. Trois pièges structurels : la `logical_date` est le **début de l'intervalle**, pas l'instant d'exécution ; le code des DAGs est ré-importé à chaque parse, donc le top-level doit rester léger ; XCom transporte des métadonnées, pas du volume.
- [[Dagster]] — l'unité n'est pas la tâche mais l'**asset** : on déclare la donnée à produire, et le graphe, le **lignage** et les rematérialisations s'en déduisent, avec typage et tests de données de première classe. Changement de modèle mental réel en venant d'Airflow, et des concepts renommés au fil des versions.
- [[Prefect]] — des décorateurs `@flow` / `@task` sur des fonctions ordinaires, **sans DAG statique** : le graphe se construit à l'exécution, donc boucles et branches conditionnelles sont naturelles. La contrepartie est directe — on ne visualise pas un pipeline avant de l'avoir lancé. Refonte majeure entre la v1 et les v2/v3 : les patterns d'avant sont obsolètes.
- [[Kestra]] — le seul **déclaratif YAML**, sur un moteur **JVM** event-driven : la logique d'orchestration est découplée du langage des tâches, donc l'équipe n'a pas à être Python. Autre stack à opérer et monitorer, et le tout-YAML devient verbeux dès que la logique se complique — d'où le découpage en sous-flows.
- [[Mage]] — l'**ELT low-code par blocs** dans une UI type notebook, avec prévisualisation de la donnée à chaque étape, chaque bloc restant du vrai code Python, SQL ou R. L'OSS avance moins vite depuis le virage vers l'offre managée Mage Pro, et le catalogue de connecteurs est en retrait.
- [[Temporal]] — le seul qui n'est pas un orchestrateur data : de l'**exécution durable**, où chaque étape est persistée en historique event-sourced, l'exécution survit aux crashs et peut durer des mois. Le prix est une discipline — le code de workflow doit être **déterministe** (ni I/O direct, ni horloge murale, ni aléatoire) — et le versioning des instances longues est délicat.
