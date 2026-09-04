---
role: brique
nom: Seldon Core
alias: [seldon, seldon-core]
pitch: "Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024."
categorie: ml/serving
famille: plateforme
licence_type: source-available
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[KServe]]", "[[TorchServe]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: []
tags: [model-serving, inference, kubernetes]
url_docs: https://docs.seldon.ai/
url_repo: https://github.com/SeldonIO/seldon-core
---

# Seldon Core

<!-- AUTO:BANDEAU:START -->
> Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Go | source-available | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de serving et d'**orchestration d'inférence** sur Kubernetes. Au-delà d'exposer un
modèle, elle compose des **graphes d'inférence** multi-étapes — transformers, routeurs,
combiners, détecteurs de drift, explainers — déployés comme un seul service. Multi-framework,
elle s'appuie sur **MLServer**, son serveur d'inférence de bas niveau au protocole V2,
compatible KServe. Brique historique du serving ML sur Kubernetes, et co-créatrice de KServe.
Deux générations coexistent, Core v1 et v2/MLServer, aux architectures différentes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pipelines d'inférence complexes : pré/post-traitement, routage A/B, ensembles, explainers en un seul graphe | Usage en production sous contrainte d'open-source strict : la BSL 1.1 impose une licence commerciale, et l'éligibilité se vérifie avant, pas après |
| Explicabilité (Alibi Explain) et détection de drift ou d'outliers (Alibi Detect) intégrées au serving | Deux générations aux architectures différentes, Core v1 et v2/MLServer : ne pas mélanger les documentations |
| Déjà sur Kubernetes, avec une équipe à l'aise pour opérer une plateforme MLOps complète | Surface opérationnelle large : Kubernetes, réseau et observabilité restent à câbler |
| Termes BSL acceptés : gratuit hors production, licence commerciale en production | |

## Mise en œuvre

- Installation — opérateurs et CRD posés sur un cluster Kubernetes, via Helm
- Point d'entrée — un graphe d'inférence déclaré en CRD ; MLServer comme serveur de bas niveau, protocole V2
- Prérequis — un cluster Kubernetes déjà opéré, et l'éligibilité aux termes BSL vérifiée avant toute mise en production
- Exécution — self-hébergé sur Kubernetes ; réplicas et graphes répartis sur le cluster
- Coût — BSL 1.1 depuis le 22 janvier 2024 : gratuit hors production, licence commerciale en production, conversion en Apache-2.0 quatre ans après chaque release. MLServer seul reste Apache-2.0

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Ressources

- Documentation — https://docs.seldon.ai/
- Dépôt — https://github.com/SeldonIO/seldon-core

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[Docker]] — les images de modèles déployées sur le cluster
