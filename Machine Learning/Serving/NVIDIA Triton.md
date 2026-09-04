---
role: brique
nom: NVIDIA Triton
alias: [triton, triton-inference-server, dynamo-triton]
pitch: "Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[BentoML]]", "[[KServe]]", "[[Seldon Core]]", "[[TorchServe]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: ["[[TensorRT]]", "[[ONNX Runtime]]"]
tags: [model-serving, inference, gpu]
url_docs: https://docs.nvidia.com/deeplearning/triton-inference-server/
url_repo: https://github.com/triton-inference-server/server
---

# NVIDIA Triton

<!-- AUTO:BANDEAU:START -->
> Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur d'inférence de NVIDIA, pensé pour servir **plusieurs frameworks derrière une seule
API** : TensorRT, PyTorch/LibTorch, ONNX Runtime, TensorFlow, OpenVINO, Python, et FIL pour
les arbres. Cœur C++ optimisé pour le GPU — **batching dynamique** qui agrège les requêtes
pour saturer la carte, **exécution concurrente** de plusieurs modèles ou instances, ensembles
de modèles chaînés côté serveur, métriques Prometheus. Depuis mars 2025 il est intégré à la
plateforme NVIDIA Dynamo (« Dynamo-Triton »), mais le cœur reste le même projet, avec des
releases conteneur mensuelles sur NGC.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Débit et latence GPU maximaux en production : batching dynamique, concurrence d'instances | Le `model_repository` impose une arborescence et un `config.pbtxt` stricts — mal formé, il échoue en silence |
| Parc de modèles hétérogène : TensorRT, PyTorch, ONNX et TF derrière un seul serveur | Image GPU volumineuse, liée à une matrice CUDA/driver précise |
| Pipelines d'inférence par ensembles, chaînés côté serveur | L'optimisation TensorRT en amont n'est pas triviale : opérateurs non supportés, calibration → [[TensorRT]] |
| Stack NVIDIA où l'optimisation matérielle compte | |

## Mise en œuvre

- Installation — conteneur NGC `nvcr.io/nvidia/tritonserver`, releases mensuelles
- Point d'entrée — un `model_repository` sur disque et son `config.pbtxt` ; API HTTP/REST et gRPC
- Prérequis — GPU NVIDIA et une paire CUDA/driver compatible avec l'image
- Exécution — self-hébergé sur serveur GPU (data center, cloud) ; réplicas pilotés par l'orchestrateur, souvent KServe
- Coût — BSD-3-Clause ; support et packaging par NVIDIA AI Enterprise, optionnels et payants. Le coût réel est le parc GPU

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

### Compléments

- [[TensorRT]] — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM. — le backend qui exécute les moteurs compilés servis par Triton
- [[ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge. — le backend qui exécute les modèles exportés en ONNX

## Ressources

- Documentation — https://docs.nvidia.com/deeplearning/triton-inference-server/
- Dépôt — https://github.com/triton-inference-server/server

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[PyTorch]], [[TensorFlow]] — deux des frameworks dont il exécute les modèles
