---
role: brique
nom: Metaflow
alias: [metaflow]
pitch: "Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds."
categorie: ml/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[ZenML]]", "[[Flyte]]"]
complements: []
tags: [orchestration, ml-pipeline]
url_docs: https://docs.metaflow.org/
url_repo: https://github.com/Netflix/metaflow
---

# Metaflow

<!-- AUTO:BANDEAU:START -->
> Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework ML créé et open-sourcé par **Netflix** en 2019, pensé pour la productivité du data
scientist. Un projet s'y structure en **flow** : une classe Python dont les `@step` forment un
graphe ; chaque étape peut demander plus de CPU, de RAM ou de GPU par décorateur et s'exécuter
à distance **sans changer le code**. Metaflow versionne automatiquement runs, artefacts et
données, permet la reprise (`resume`) et l'inspection a posteriori. L'expérience la plus
aboutie est celle d'**AWS** — Batch, Step Functions, S3 —, Kubernetes étant supporté mais moins
clé en main. Il n'embarque pas d'ordonnanceur temporel : la planification passe par Step
Functions ou Argo. La société Outerbounds, fondée par ses créateurs, en propose une plateforme
managée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Data scientist qui veut passer du local au cloud, AWS surtout, sans réécrire son code | L'expérience aboutie est celle d'**AWS** : les autres backends, Kubernetes compris, sont supportés mais moins clé en main → [[Flyte]] pour du Kubernetes-natif |
| Versionnage automatique des runs et artefacts, et reprise après échec | **Aucun ordonnanceur temporel intégré** : la planification passe par Step Functions ou Argo, donc par un déclencheur externe |
| Charges hétérogènes en ressources — une étape GPU, une étape CPU massive — sur AWS Batch ou K8s | Centré sur le flow Python : moins adapté à des DAGs purement data partagés entre équipes → [[Dagster]] / [[Airflow]] |
| Stack centrée AWS cherchant un framework éprouvé en production à grande échelle |  |

## Mise en œuvre

- Installation — `uv add metaflow` ; fonctionne en local sans infra
- Point d'entrée — une classe Python à `@step`, décorateurs de ressources pour l'exécution distante
- Prérequis — pour le distant : un déploiement AWS (Batch, Step Functions, S3) ou Kubernetes, templates CloudFormation/Terraform officiels fournis
- Exécution — self-hébergée, distribuée ; du poste local au cloud sans changement de code
- Coût — gratuit, Apache-2.0, en self-host ; Outerbounds propose un control plane managé avec UI et support entreprise, payant

## Écosystème

### Alternatives

- [[ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.
- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.

## Ressources

- Documentation — https://docs.metaflow.org/
- Dépôt — https://github.com/Netflix/metaflow

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[AWS S3]] — le datastore des artefacts
- [[Docker]] — la conteneurisation des étapes distantes
- [[MLflow]] — le suivi d'expériences avec lequel il s'intègre
- [[Comparatif - Orchestrateurs ML]] — ce qui départage les orchestrateurs
