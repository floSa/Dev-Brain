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

## Pourquoi

ZenML est un framework MLOps Python qui sépare la **logique du pipeline** de l'**infrastructure d'exécution**. On écrit des steps et pipelines décorés en Python pur ; le « stack » (orchestrateur, artifact store, container registry, experiment tracker…) se branche par configuration. Le même pipeline passe ainsi du laptop à Kubernetes, Airflow, SageMaker ou Vertex sans réécriture. ZenML ne remplace pas les outils MLOps existants : il les **orchestre** (MLflow, W&B, BentoML, KServe…) derrière une abstraction unifiée. Cœur Apache-2.0 ; édition managée **ZenML Pro** pour les équipes.

## Quand l'utiliser

- Portabilité : développer en local puis déployer sur plusieurs backends sans changer le code.
- Fédérer un stack MLOps hétérogène (tracking + orchestration + serving) derrière une API unique.
- Garder la liberté multi-cloud / multi-orchestrateur, sans verrou propriétaire.
- Équipe data science cherchant des pipelines reproductibles sans devenir experte Kubernetes.

## Quand NE PAS l'utiliser

- Stack déjà tout-AWS, scaling natif voulu sans couche d'abstraction → [[Metaflow]].
- Orchestration Kubernetes-native à grande échelle, typage fort et isolation des ressources → [[Flyte]].
- Simple ordonnancement de DAGs data sans dimension ML → [[Airflow]] / [[Dagster]].

## Déploiement & coût

- Open-source (Apache-2.0), `uv add zenml`. Serveur ZenML (métadonnées) auto-hébergé via Docker/Helm sur Kubernetes.
- Exécution distribuée déléguée au stack choisi (Kubernetes, Airflow, runners cloud).
- Managé : ZenML Pro (multi-tenant, RBAC, registre de modèles ; payant).

## Pièges

- ZenML orchestre d'autres outils : il faut quand même opérer le backend réel (K8s, etc.) — l'abstraction ne supprime pas l'infra.
- Le serveur de métadonnées est un composant à héberger et sauvegarder.
- Les concepts de stacks (stack, flavor, component) ajoutent une courbe d'apprentissage.

## Alternatives

- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.

## Liens

- [[Comparatif - Orchestrateurs ML]] — comparatif de la catégorie
- Orchestre des outils existants : [[MLflow]], [[BentoML]], [[KServe]].
- Doc : https://docs.zenml.io/
