---
galaxie: dev
type: service
nom: NVIDIA Triton
alias: [triton, triton-inference-server, dynamo-triton]
pitch: "Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo."
categorie: ml/serving
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/BentoML|BentoML]]", "[[Dev/Services/KServe|KServe]]", "[[Dev/Services/Seldon Core|Seldon Core]]", "[[Dev/Services/TorchServe|TorchServe]]", "[[Dev/Services/TensorFlow Serving|TensorFlow Serving]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: actif
tags: [model-serving, inference, gpu]
url_docs: https://docs.nvidia.com/deeplearning/triton-inference-server/
url_repo: https://github.com/triton-inference-server/server
---

# NVIDIA Triton

## Pourquoi

Serveur d'inférence haute performance de NVIDIA, pensé pour servir **plusieurs frameworks** derrière une seule API (TensorRT, PyTorch/LibTorch, ONNX Runtime, TensorFlow, OpenVINO, Python, FIL pour les arbres). Cœur **C++** optimisé pour le GPU : **batching dynamique** (agrège les requêtes pour saturer le GPU), **exécution concurrente** de plusieurs modèles/instances, ensembles de modèles, métriques Prometheus. Depuis mars 2025, intégré à la plateforme **NVIDIA Dynamo** (« Dynamo-Triton »), mais le cœur reste le même projet open-source avec des releases conteneur mensuelles sur NGC.

## Quand l'utiliser

- **Débit et latence GPU** maximaux en production (batching dynamique, concurrence d'instances).
- Parc de modèles **hétérogène** : servir TensorRT, PyTorch, ONNX et TF derrière un seul serveur.
- Pipelines d'inférence par **ensembles** (chaînage de modèles côté serveur).
- Stack NVIDIA (TensorRT, GPU data center) où l'optimisation matérielle compte.

## Quand NE PAS l'utiliser

- Pas de GPU, besoin Python simple et packaging rapide → [[Dev/Services/BentoML|BentoML]].
- Orchestration K8s déclarative avec scale-to-zero → [[Dev/Services/KServe|KServe]] (qui peut d'ailleurs utiliser Triton comme runtime).
- Un seul modèle TensorFlow, sans le poids de Triton → [[Dev/Services/TensorFlow Serving|TensorFlow Serving]].

## Déploiement & coût

- Open-source (BSD-3-Clause), gratuit ; distribué surtout comme **conteneur NGC** (`nvcr.io/nvidia/tritonserver`), releases mensuelles.
- Self-host sur serveur GPU (data center, cloud) ; pas d'offre SaaS directe.
- Support entreprise et packaging via **NVIDIA AI Enterprise** (contrat de support, optionnel).
- Scaling distribué via l'orchestrateur (réplicas K8s, souvent piloté par KServe).

## Pièges

- Conversion/optimisation **TensorRT** parfois délicate (opérateurs non supportés, calibration) — gain réel mais setup non trivial.
- Le **model repository** impose une arborescence et un `config.pbtxt` stricts : erreurs silencieuses si mal formé.
- Image GPU volumineuse ; versions liées à une matrice CUDA/driver précise.

## Alternatives

- [[Dev/Services/BentoML|BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[Dev/Services/KServe|KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Dev/Services/Seldon Core|Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[Dev/Services/TorchServe|TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Dev/Services/TensorFlow Serving|TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Runtimes servis : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/TensorFlow|TensorFlow]] (et ONNX, TensorRT).
- Souvent déployé via [[Dev/Services/KServe|KServe]] comme runtime d'inférence sur Kubernetes.
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc : https://docs.nvidia.com/deeplearning/triton-inference-server/
