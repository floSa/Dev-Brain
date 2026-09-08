---
role: brique
nom: Flyte
alias: [flyte, flytekit]
pitch: "Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai."
categorie: ml/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[ZenML]]", "[[Metaflow]]"]
complements: []
tags: [orchestration, ml-pipeline, kubernetes]
url_docs: https://docs.flyte.org/
url_repo: https://github.com/flyteorg/flyte
---

# Flyte

<!-- AUTO:BANDEAU:START -->
> Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur de workflows ML et data **Kubernetes-natif**, conçu dès l'origine pour exécuter
des pipelines à grande échelle. Le SDK Python **flytekit** décrit des tâches **fortement
typées** et conteneurisées ; chaque tâche s'exécute dans un pod isolé, avec ses ressources
propres. Le backend, écrit en Go, gère le versionnage, le **cache d'exécution** — la
memoization qui évite de recalculer —, les reprises et le data lineage. Il n'existe pas de mode
purement local : un cluster, même sandbox, est requis pour exécuter. Né chez Lyft,
open-sourcé en 2020, projet gradué de la LF AI & Data Foundation ; l'édition entreprise est
portée par Union.ai, et une migration vers **Flyte 2** est en cours.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pipelines ML/data lourds, déjà sur **Kubernetes**, à exécuter de façon isolée et reproductible | **Dépendance Kubernetes forte** : pas de mode local, et opérer Flyte demande une vraie compétence cluster → [[Metaflow]] ou [[ZenML]] |
| Typage fort des entrées/sorties et cache d'exécution pour éviter de recalculer | Migration en cours vers **Flyte 2** : nouveau SDK, URLs de doc en bascule sous union.ai — vérifier la version ciblée avant de s'engager |
| Multi-tenant à l'échelle : plusieurs équipes et projets versionnés sur un même cluster | Public visé : ingénieurs plateforme plus que data scientists en solo |
| Workflows mixtes data + ML demandant une isolation forte des ressources | Orchestration ELT généraliste, orientée assets et connecteurs → [[Dagster]] / [[Airflow]] |

## Mise en œuvre

- Installation — SDK `uv add flytekit` ; control plane Flyte à déployer, plus ses plugins
- Point d'entrée — tâches et workflows Python décorés, typés de bout en bout
- Prérequis — un cluster **Kubernetes**, même sandbox léger : aucune exécution sans lui
- Exécution — self-hébergé sur Kubernetes uniquement, distribué, une tâche par pod
- Coût — gratuit, Apache-2.0, en self-host ; Union.ai propose un control plane entreprise managé, payant

## Écosystème

### Alternatives

- [[ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.
- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.

## Ressources

- Documentation — https://docs.flyte.org/
- Dépôt — https://github.com/flyteorg/flyte

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[Docker]] — la conteneurisation sur laquelle repose l'isolation des tâches
- [[Comparatif - Orchestrateurs ML]] — ce qui départage les orchestrateurs
