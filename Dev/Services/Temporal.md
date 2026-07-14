---
galaxie: dev
type: service
nom: Temporal
alias: [temporal, Temporal.io]
pitch: "Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage."
categorie: data/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/Airflow|Airflow]]", "[[Dev/Services/Dagster|Dagster]]", "[[Dev/Services/Prefect|Prefect]]", "[[Dev/Services/Mage|Mage]]", "[[Dev/Services/Kestra|Kestra]]"]
remplace_par: []
status: actif
tags: [orchestration, durable-execution, distributed]
url_docs: https://docs.temporal.io/
url_repo: https://github.com/temporalio/temporal
---

# Temporal

## Pourquoi

Temporal est une plateforme d'**exécution durable**. On écrit ses workflows comme du **code ordinaire** (Go, Java, Python, TypeScript, .NET, PHP) ; le moteur **persiste chaque étape** (historique event-sourced) de sorte que l'exécution survit aux crashs, retente les **activités**, gère les timeouts et peut durer des jours ou des mois. Distinction clé : les **Workflows** (orchestration déterministe) sont séparés des **Activities** (effets de bord, I/O). À la différence des orchestrateurs data orientés DAG batch, Temporal cible n'importe quel **processus métier long et fiable**. Serveur écrit en Go, licence MIT ; issu des créateurs de Cadence (Uber) et AWS SWF.

## Quand l'utiliser

- Processus métier longs et multi-étapes exigeant la fiabilité : commandes, paiements / sagas, provisioning, human-in-the-loop, orchestration d'agents IA.
- Garantir retries et persistance d'état **sans** recâbler à la main files d'attente + machines à états.
- Orchestration de microservices résiliente, pilotée par du code.
- Besoin de reprise exacte après panne (pas de progrès perdu, pas de processus orphelin).

## Quand NE PAS l'utiliser

- DAGs data/ETL planifiés avec lignage et catalogue de connecteurs → [[Dev/Services/Airflow|Airflow]] / [[Dev/Services/Dagster|Dagster]].
- Traitement de flux temps réel → [[Dev/Services/Flink|Flink]].
- Simple cron / tâche planifiée → un scheduler suffit.
- Tâche unique fire-and-forget → une file (Celery) est plus légère.

## Déploiement & coût

- Open-source (MIT), auto-hébergé : Temporal Server (Go) + une persistance (Cassandra, [[Dev/Services/Postgres|Postgres]] ou MySQL) + Elasticsearch optionnel pour la visibilité.
- Managé : **Temporal Cloud** (facturé à l'action / au stockage d'état).
- Architecture distribuée et horizontalement scalable ; plusieurs composants à opérer en self-host.

## Pièges

- Le code de workflow doit être **déterministe** : pas d'I/O direct, pas d'horloge murale, pas d'aléatoire dans le chemin du workflow — tout passe par des activités ou les API du SDK.
- Le **versioning** des workflows longue durée est délicat (instances en cours pendant un déploiement).
- Courbe d'apprentissage : bien tracer la frontière Workflow / Activity.
- Opérer la persistance et le store de visibilité demande du soin.

## Alternatives

- [[Dev/Services/Airflow|Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dev/Services/Dagster|Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/Mage|Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Dev/Services/Kestra|Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie.
- Doc : https://docs.temporal.io/
