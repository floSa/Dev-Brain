---
role: brique
nom: Temporal
alias: [temporal, Temporal.io]
pitch: "Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Airflow]]", "[[Dagster]]", "[[Prefect]]", "[[Mage]]", "[[Kestra]]"]
complements: []
tags: [orchestration, durable-execution, distributed]
url_docs: https://docs.temporal.io/
url_repo: https://github.com/temporalio/temporal
---

# Temporal

<!-- AUTO:BANDEAU:START -->
> Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'**exécution durable**, et le seul membre du dossier qui ne soit pas un
orchestrateur data. On écrit ses workflows comme du **code ordinaire** — Go, Java, Python,
TypeScript, .NET, PHP — et le moteur persiste chaque étape dans un historique
event-sourced : l'exécution survit aux crashs, retente les **activités**, gère les timeouts
et peut durer des mois. La distinction structurante est celle des **Workflows**
(orchestration déterministe) et des **Activities** (effets de bord et I/O) : le code de
workflow ne peut faire ni I/O direct, ni lecture d'horloge murale, ni tirage aléatoire —
tout passe par une activité ou par les API du SDK. Issu des créateurs de Cadence (Uber) et
d'AWS SWF.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Processus métier longs et multi-étapes exigeant la fiabilité : commandes, paiements et sagas, provisioning, human-in-the-loop | Traitement de flux temps réel : Temporal orchestre des processus, il ne calcule pas sur un flux → [[Flink]] |
| Retries et persistance d'état garantis sans recâbler à la main files d'attente et machines à états | Le code de workflow doit être **déterministe** — ni I/O direct, ni horloge murale, ni aléatoire hors des activités |
| Orchestration de microservices résiliente, pilotée par du code | Le versionnage des workflows longue durée est délicat : des instances tournent pendant le déploiement |
| Reprise exacte après panne : aucun progrès perdu, aucun processus orphelin | Un simple cron, ou une tâche fire-and-forget, se traite avec un scheduler ou une file — la persistance d'état y est de trop |
| | Plusieurs composants à opérer en self-host : le serveur, sa persistance, et le store de visibilité |

## Mise en œuvre

- Installation — `temporal server start-dev` sur le poste ; images Docker ou chart Helm pour un cluster
- Point d'entrée — SDK dans le langage applicatif (Go, Java, Python, TypeScript, .NET, PHP) et workers rattachés à des task queues
- Prérequis — une persistance (Cassandra, [[Postgres]] ou MySQL), Elasticsearch en option pour la visibilité avancée
- Exécution — self-hébergé ou managé ; architecture distribuée, scalable horizontalement
- Coût — gratuit en MIT ; Temporal Cloud est facturé à l'action et au stockage d'état

## Écosystème

### Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.

## Ressources

- Documentation — https://docs.temporal.io/
- Dépôt — https://github.com/temporalio/temporal

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
