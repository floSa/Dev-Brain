---
galaxie: dev
type: service
nom: BentoML
alias: [bentoml, bento]
pitch: "Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes)."
categorie: ml/serving
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/NVIDIA Triton|NVIDIA Triton]]", "[[Dev/Services/KServe|KServe]]", "[[Dev/Services/Seldon Core|Seldon Core]]", "[[Dev/Services/TorchServe|TorchServe]]", "[[Dev/Services/TensorFlow Serving|TensorFlow Serving]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: actif
tags: [model-serving, inference]
url_docs: https://docs.bentoml.com/
url_repo: https://github.com/bentoml/BentoML
---

# BentoML

## Pourquoi

Framework **Python** pour empaqueter un modèle entraîné en service d'inférence. Une classe `Service` décrit les dépendances, le code de pré/post-traitement et les endpoints ; BentoML construit un artefact versionné (le **Bento**) qui contient modèle, code et environnement, prêt à conteneuriser. Agnostique au framework (scikit-learn, PyTorch, transformers, ONNX, modèles custom) et orienté du prototype local au déploiement scalable, avec un volet LLM (serving haut débit, files de jobs, pipelines multi-modèles). L'offre managée **BentoCloud** déploie ces Bentos sans opérer l'infra.

## Quand l'utiliser

- Exposer un modèle **Python** comme API d'inférence sans écrire le serveur HTTP à la main.
- **Packaging reproductible** : figer modèle + code + dépendances dans un artefact conteneurisable.
- Pipelines **multi-modèles** ou logique métier autour de l'inférence (pré/post-traitement riche).
- Aller vite du notebook à un déploiement scalable, éventuellement managé via BentoCloud.

## Quand NE PAS l'utiliser

- Débit/latence maximal sur GPU avec batching dynamique multi-framework → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]].
- Standard d'inférence déclaratif déjà sur Kubernetes (CRD, scale-to-zero) → [[Dev/Services/KServe|KServe]].
- Serving mono-framework strict sans couche Python → [[Dev/Services/TensorFlow Serving|TensorFlow Serving]].

## Déploiement & coût

- Open-source (Apache-2.0), `uv add bentoml`. Serveur local en une commande, build d'un Bento puis image OCI.
- Self-host : conteneur Bento sur n'importe quel runtime (Docker, Kubernetes).
- Managé : **BentoCloud** (payant) — déploiement, autoscaling et scale-to-zero sans gérer l'infra.
- Scaling distribué côté orchestrateur (réplicas K8s / BentoCloud).

## Pièges

- L'image d'un Bento peut devenir lourde (modèle + dépendances) : soigner le `python` et les exclusions.
- Le serveur Python n'a pas le batching GPU fin d'un [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] ; pour la latence GPU pure, combiner les deux (BentoML devant, Triton comme runtime).
- API remaniée en profondeur en 1.2+ : beaucoup de tutoriels anciens ne s'appliquent plus.

## Alternatives

- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Dev/Services/KServe|KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Dev/Services/Seldon Core|Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[Dev/Services/TorchServe|TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Dev/Services/TensorFlow Serving|TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Sert des modèles de tout framework : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/Scikit-Learn|Scikit-Learn]], [[Dev/Services/HuggingFace|HuggingFace]].
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc : https://docs.bentoml.com/
