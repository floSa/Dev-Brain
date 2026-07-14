---
galaxie: dev
type: service
nom: TensorFlow Serving
alias: [tf-serving, tensorflow-serving, tfserving]
pitch: "Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX."
categorie: ml/serving
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/BentoML|BentoML]]", "[[Dev/Services/NVIDIA Triton|NVIDIA Triton]]", "[[Dev/Services/KServe|KServe]]", "[[Dev/Services/Seldon Core|Seldon Core]]", "[[Dev/Services/TorchServe|TorchServe]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: actif
tags: [model-serving, inference, gpu]
url_docs: https://www.tensorflow.org/tfx/guide/serving
url_repo: https://github.com/tensorflow/serving
---

# TensorFlow Serving

## Pourquoi

Serveur d'inférence dédié aux modèles **[[Dev/Services/TensorFlow|TensorFlow]]/Keras** au format `SavedModel`. Cœur **C++** haute performance, conçu pour la production : **API REST (JSON) et gRPC (Protobuf)**, **versionnage** de modèles (chargement/déchargement à chaud, politiques de version), **batching** de requêtes, et chargement de nouveaux modèles sans redémarrer. Brique de déploiement historique de l'écosystème TF, intégrée aux pipelines **TFX**. Mono-framework par nature, mais très éprouvée et toujours activement maintenue.

## Quand l'utiliser

- Servir des modèles **TensorFlow/Keras** (`SavedModel`) en production, avec versionnage et hot-reload.
- Besoin des **deux protocoles** REST et gRPC, du batching et de métriques de serving standard.
- Pipeline **TFX** bout-en-bout déjà en place.
- Recherche de **latence faible** côté serveur pour un parc mono-framework.

## Quand NE PAS l'utiliser

- Modèles **non-TensorFlow** (PyTorch, ONNX, scikit-learn…) → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] ou [[Dev/Services/BentoML|BentoML]].
- Logique métier riche autour de l'inférence en Python → [[Dev/Services/BentoML|BentoML]].
- Orchestration Kubernetes déclarative avec scale-to-zero → [[Dev/Services/KServe|KServe]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; distribué comme **conteneur** (`tensorflow/serving`) ou binaire.
- Self-host (CPU/GPU) ; pas d'offre SaaS propre.
- Scaling distribué via l'orchestrateur (réplicas K8s, souvent piloté par KServe).

## Pièges

- **Mono-framework** : il faut un `SavedModel` TF — pas une option pour un parc hétérogène.
- La **signature** du SavedModel (noms d'entrées/sorties) doit être correcte, sinon erreurs d'inférence opaques.
- Image GPU liée à une matrice CUDA/cuDNN précise (comme l'écosystème TF).

## Alternatives

- [[Dev/Services/BentoML|BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Dev/Services/KServe|KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Dev/Services/Seldon Core|Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[Dev/Services/TorchServe|TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Sert les modèles de [[Dev/Services/TensorFlow|TensorFlow]] (équivalent TF de [[Dev/Services/TorchServe|TorchServe]]).
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc : https://www.tensorflow.org/tfx/guide/serving
