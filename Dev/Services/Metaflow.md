---
galaxie: dev
type: service
nom: Metaflow
alias: [metaflow]
pitch: "Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds."
categorie: ml/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/ZenML|ZenML]]", "[[Dev/Services/Flyte|Flyte]]"]
remplace_par: []
status: actif
tags: [orchestration, ml-pipeline]
url_docs: https://docs.metaflow.org/
url_repo: https://github.com/Netflix/metaflow
---

# Metaflow

## Pourquoi

Metaflow est un framework ML créé et open-sourcé par **Netflix** (2019), pensé pour la productivité du data scientist. Un projet se structure en **flow** : une classe Python dont les `@step` forment un graphe ; chaque étape peut demander plus de CPU/RAM/GPU par décorateur et s'exécuter à distance sans changer le code. Metaflow **versionne automatiquement** runs, artefacts et données, permet la reprise (`resume`) et l'inspection a posteriori. Particulièrement optimisé pour AWS (Batch, Step Functions, S3), il tourne aussi sur Kubernetes. La société **Outerbounds**, fondée par ses créateurs, en propose une plateforme managée.

## Quand l'utiliser

- Data scientist qui veut passer du local au cloud (AWS surtout) sans réécrire son code.
- Besoin de versionnage automatique des runs/artefacts et de reprise après échec.
- Charges hétérogènes en ressources (une étape GPU, une étape CPU massive) sur AWS Batch / K8s.
- Stack centrée AWS cherchant un framework éprouvé en production à grande échelle.

## Quand NE PAS l'utiliser

- Besoin de neutralité d'infrastructure / multi-orchestrateur derrière une abstraction → [[Dev/Services/ZenML|ZenML]].
- Orchestration Kubernetes-native avec typage fort des données et cache d'exécution → [[Dev/Services/Flyte|Flyte]].
- Orchestration data généraliste (ELT, connecteurs, assets) plutôt que ML → [[Dev/Services/Dagster|Dagster]] / [[Dev/Services/Airflow|Airflow]].

## Déploiement & coût

- Open-source (Apache-2.0), `uv add metaflow`. Fonctionne en local sans infra.
- Self-host : déploiement AWS (Batch + Step Functions + S3) ou Kubernetes ; templates CloudFormation/Terraform officiels.
- Managé : Outerbounds (control plane managé, UI, support entreprise ; payant).

## Pièges

- L'expérience la plus aboutie est sur **AWS** ; les autres backends (K8s) sont supportés mais moins clé en main.
- Pas d'ordonnanceur temporel intégré : la planification passe par Step Functions / Argo (déclencheurs externes).
- Centré sur le flow Python — moins adapté à des DAGs purement data partagés entre équipes.

## Alternatives

- [[Dev/Services/ZenML|ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.
- [[Dev/Services/Flyte|Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.

## Liens

- [[Comparatif - Orchestrateurs ML]] — comparatif de la catégorie
- S'appuie sur : [[Dev/Services/AWS S3|AWS S3]] (datastore), [[Dev/Services/Docker|Docker]] / Kubernetes.
- S'intègre avec : [[Dev/Services/MLflow|MLflow]].
- Doc : https://docs.metaflow.org/
