---
role: brique
nom: KServe
alias: [kserve, kfserving]
pitch: "Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[Seldon Core]]", "[[TorchServe]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: []
tags: [model-serving, inference, kubernetes]
url_docs: https://kserve.github.io/website/
url_repo: https://github.com/kserve/kserve
---

# KServe

<!-- AUTO:BANDEAU:START -->
> Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | à jour · 2026-08-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche d'inférence native Kubernetes : le déploiement d'un modèle se décrit dans une ressource
déclarative **`InferenceService`**, et l'opérateur gère serveur, routes, autoscaling et
rollout. L'intégration **Knative** apporte l'autoscaling au trafic, le **scale-to-zero** — pas
de coût quand aucune requête n'arrive — et les déploiements canary. Multi-framework
(scikit-learn, PyTorch, TensorFlow, XGBoost, ONNX, Triton), et désormais serving génératif.
Né en 2019 comme KFServing sous Kubeflow, renommé KServe en 2022, projet CNCF en incubation
depuis fin 2025 — gouvernance neutre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déjà sur Kubernetes : les modèles se déploient et se versionnent comme le reste de l'infra (GitOps, CRD) | Knative et une couche réseau (Istio…) sont à opérer en plus : la courbe d'apprentissage est celle de Kubernetes, pas celle de KServe |
| Charge variable ou sporadique : le scale-to-zero ne fait payer le GPU que sous trafic | Le scale-from-zero ajoute une latence de démarrage à froid, critique sur un gros modèle GPU |
| Parc multi-framework à standardiser derrière une abstraction commune | Deux modes de déploiement, Serverless et RawDeployment, aux comportements différents : à choisir tôt |
| Rollouts progressifs en canary, transformers et explainers branchés dans le graphe de service | |

## Mise en œuvre

- Installation — manifests ou Helm sur un cluster Kubernetes, avec Knative et une gateway (Istio) en mode Serverless
- Point d'entrée — la CRD `InferenceService`, déclarée en YAML
- Prérequis — un cluster Kubernetes déjà opéré ; Knative et sa couche réseau pour le mode Serverless
- Exécution — sur le cluster, autoscaling au trafic et scale-to-zero par Knative ; managé indirectement par les distributions K8s/ML des cloud providers
- Coût — Apache-2.0, aucune offre SaaS propre ; le coût est celui du cluster, et il tombe à zéro hors trafic

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Ressources

- Documentation — https://kserve.github.io/website/
- Dépôt — https://github.com/kserve/kserve

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[Docker]] — les images de modèles que le cluster exécute
