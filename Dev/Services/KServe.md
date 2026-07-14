---
galaxie: dev
type: service
nom: KServe
alias: [kserve, kfserving]
pitch: "Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif."
categorie: ml/serving
licence_type: open-source
hosted: self
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/BentoML|BentoML]]", "[[Dev/Services/NVIDIA Triton|NVIDIA Triton]]", "[[Dev/Services/Seldon Core|Seldon Core]]", "[[Dev/Services/TorchServe|TorchServe]]", "[[Dev/Services/TensorFlow Serving|TensorFlow Serving]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: actif
tags: [model-serving, inference, kubernetes]
url_docs: https://kserve.github.io/website/
url_repo: https://github.com/kserve/kserve
---

# KServe

## Pourquoi

Couche d'inférence **native Kubernetes** : on décrit le déploiement d'un modèle dans une ressource déclarative **`InferenceService`** (CRD), et KServe gère serveur, routes, autoscaling et rollout. Intégration **Knative** pour le serverless — **autoscaling basé sur le trafic et scale-to-zero** (pas de coût quand aucune requête) — et déploiements canary. Multi-framework (scikit-learn, PyTorch, TensorFlow, XGBoost, ONNX, Triton…) et désormais aussi serving génératif (LLM). Né en 2019 comme **KFServing** sous Kubeflow, devenu KServe en 2022, **projet CNCF en incubation** depuis fin 2025 — gouvernance neutre.

## Quand l'utiliser

- Déjà sur **Kubernetes** : modèles déployés et versionnés comme du reste de l'infra (GitOps, CRD).
- **Charge variable / sporadique** : scale-to-zero pour ne payer le GPU que sous trafic.
- Stack **multi-framework** voulue standardisée derrière une abstraction commune.
- Rollouts progressifs (canary), transformers et explainers branchés dans le graphe de service.

## Quand NE PAS l'utiliser

- Pas de cluster Kubernetes / besoin d'un serveur simple en local → [[Dev/Services/BentoML|BentoML]].
- Performance GPU brute d'un runtime unique → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] (souvent utilisé *dans* KServe).
- Un seul modèle TensorFlow à exposer → [[Dev/Services/TensorFlow Serving|TensorFlow Serving]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; s'installe **sur un cluster Kubernetes** (avec Knative + Istio/gateway selon le mode).
- Pas d'offre SaaS propre ; managé indirectement via les distributions K8s/ML des cloud providers et de Red Hat.
- Scaling distribué et serverless par conception (Knative).

## Pièges

- **Dépendances lourdes** : Knative + une couche réseau (Istio…) à opérer ; la courbe d'apprentissage est K8s, pas juste KServe.
- Le **scale-from-zero** ajoute une latence de démarrage à froid (cold start), critique pour les gros modèles/GPU.
- Deux modes de déploiement (Serverless vs RawDeployment) aux comportements différents : choisir tôt.

## Alternatives

- [[Dev/Services/BentoML|BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Dev/Services/Seldon Core|Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[Dev/Services/TorchServe|TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Dev/Services/TensorFlow Serving|TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Runtime d'inférence fréquent : [[Dev/Services/NVIDIA Triton|NVIDIA Triton]].
- Tourne sur Kubernetes ([[Dev/Services/Docker|Docker]] pour les images de modèles).
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc : https://kserve.github.io/website/
