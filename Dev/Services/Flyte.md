---
galaxie: dev
type: service
nom: Flyte
alias: [flyte, flytekit]
pitch: "Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai."
categorie: ml/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/ZenML|ZenML]]", "[[Dev/Services/Metaflow|Metaflow]]"]
remplace_par: []
status: actif
tags: [orchestration, ml-pipeline, kubernetes]
url_docs: https://docs.flyte.org/
url_repo: https://github.com/flyteorg/flyte
---

# Flyte

## Pourquoi

Flyte est un orchestrateur de workflows ML et data **Kubernetes-natif**, conçu dès l'origine pour exécuter des pipelines à grande échelle. Le SDK Python **flytekit** décrit des **tâches fortement typées** et conteneurisées ; chaque tâche s'exécute en pod isolé avec ses ressources propres. Le backend (en **Go**) gère versionnage, **cache d'exécution** (memoization), reprises et data lineage. Né chez Lyft, open-sourcé en 2020, c'est un projet **gradué** de la LF AI & Data Foundation. L'édition entreprise est portée par **Union.ai**.

## Quand l'utiliser

- Pipelines ML/data lourds, déjà sur **Kubernetes**, à exécuter de façon isolée et reproductible.
- Besoin de typage fort des entrées/sorties et de cache d'exécution pour éviter de recalculer.
- Multi-tenant à l'échelle : plusieurs équipes / projets versionnés sur un même cluster.
- Workflows mixtes data + ML nécessitant une isolation forte des ressources.

## Quand NE PAS l'utiliser

- Pas de Kubernetes ni d'équipe infra pour l'opérer → [[Dev/Services/Metaflow|Metaflow]] (AWS) ou [[Dev/Services/ZenML|ZenML]] (abstraction).
- Simple portabilité local→cloud sans gérer un cluster → [[Dev/Services/ZenML|ZenML]].
- Orchestration ELT généraliste orientée assets/connecteurs → [[Dev/Services/Dagster|Dagster]] / [[Dev/Services/Airflow|Airflow]].

## Déploiement & coût

- Open-source (Apache-2.0). Self-host **sur Kubernetes** uniquement (control plane Flyte + plugins) ; SDK `uv add flytekit`.
- Pas de mode purement local : un cluster (même sandbox léger) est requis pour l'exécution.
- Managé : Union.ai (control plane entreprise sur EKS, support ; payant).

## Pièges

- **Dépendance Kubernetes forte** : opérer Flyte demande une vraie compétence cluster — barrière à l'entrée élevée.
- Migration en cours vers **Flyte 2** (nouveau SDK, backend open-source annoncé) : vérifier la version ciblée et la stabilité des URLs de doc (en bascule sous union.ai).
- Plus orienté ingénieurs plateforme que data scientists en solo.

## Alternatives

- [[Dev/Services/ZenML|ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.
- [[Dev/Services/Metaflow|Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.

## Liens

- [[Comparatif - Orchestrateurs ML]] — comparatif de la catégorie
- S'appuie sur : Kubernetes, [[Dev/Services/Docker|Docker]].
- Doc : https://docs.flyte.org/ · Édition entreprise : Union.ai
