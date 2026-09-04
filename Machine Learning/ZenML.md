---
role: brique
nom: ZenML
alias: [zenml]
pitch: "Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique."
categorie: ml/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Metaflow]]", "[[Flyte]]"]
complements: []
tags: [orchestration, ml-pipeline]
url_docs: https://docs.zenml.io/
url_repo: https://github.com/zenml-io/zenml
---

# ZenML

<!-- AUTO:BANDEAU:START -->
> Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework MLOps Python qui sépare la **logique du pipeline** de l'**infrastructure
d'exécution**. On écrit des steps et des pipelines décorés en Python pur ; le « stack » —
orchestrateur, artifact store, container registry, experiment tracker — se branche par
configuration, si bien que le même pipeline passe du laptop à Kubernetes, Airflow, SageMaker ou
Vertex sans réécriture. ZenML **n'exécute rien lui-même** : il orchestre les outils MLOps déjà
en place (MLflow, W&B, BentoML, KServe) derrière une abstraction unifiée — le backend réel
reste donc à opérer, et son serveur de métadonnées est un composant de plus à héberger et à
sauvegarder. Une édition managée, ZenML Pro, s'adresse aux équipes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Portabilité : développer en local puis déployer sur plusieurs backends sans changer le code | L'abstraction **ne supprime pas l'infra** : le backend réel (Kubernetes, Airflow) reste à opérer |
| Fédérer un stack MLOps hétérogène — tracking, orchestration, serving — derrière une API unique | Le **serveur de métadonnées** est un composant à héberger et à sauvegarder |
| Garder la liberté multi-cloud et multi-orchestrateur, sans verrou propriétaire | Les concepts de stacks — stack, flavor, component — ajoutent une courbe d'apprentissage |
| Équipe data science cherchant des pipelines reproductibles sans devenir experte Kubernetes |  |
| | Simple ordonnancement de DAGs data sans dimension ML → [[Airflow]] / [[Dagster]] |

## Mise en œuvre

- Installation — `uv add zenml`
- Point d'entrée — steps et pipelines décorés en Python ; le stack se déclare par configuration
- Prérequis — un serveur ZenML pour les métadonnées, auto-hébergé via Docker ou Helm sur Kubernetes
- Exécution — déléguée au stack choisi : Kubernetes, Airflow, runners cloud
- Coût — gratuit, Apache-2.0, en self-host ; ZenML Pro (multi-tenant, RBAC, registre de modèles) est payant

## Écosystème

### Alternatives

- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.

## Ressources

- Documentation — https://docs.zenml.io/
- Dépôt — https://github.com/zenml-io/zenml

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[MLflow]] · [[BentoML]] · [[KServe]] — les outils existants qu'il orchestre
- [[Comparatif - Orchestrateurs ML]] — ce qui départage les orchestrateurs
