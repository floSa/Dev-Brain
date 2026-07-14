---
galaxie: dev
type: service
nom: TorchServe
alias: [torchserve, torch-serve]
pitch: "Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025."
categorie: ml/serving
licence_type: open-source
hosted: self
maturite: deprecated
langage: Java/Python
scaling: distributed
alternatives: ["[[Dev/Services/BentoML|BentoML]]", "[[Dev/Services/NVIDIA Triton|NVIDIA Triton]]", "[[Dev/Services/KServe|KServe]]", "[[Dev/Services/Seldon Core|Seldon Core]]", "[[Dev/Services/TensorFlow Serving|TensorFlow Serving]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: abandonne
tags: [model-serving, inference, gpu]
url_docs: https://docs.pytorch.org/serve/
url_repo: https://github.com/pytorch/serve
---

# TorchServe

## Pourquoi

Serveur de modèles officiel de l'écosystème [[Dev/Services/PyTorch|PyTorch]] (créé avec AWS). Un modèle est empaqueté en archive **`.mar`** avec un **handler** Python (pré/post-traitement) ; le serveur — **frontend Java**, workers Python — expose des endpoints REST et gRPC, avec **batching**, versionnage de modèles, métriques et gestion multi-modèles. **Statut critique** : le projet est **archivé et n'est plus activement maintenu** (dépôt archivé le 7 août 2025) — plus de correctifs, de nouvelles fonctionnalités ni de patchs de sécurité. À ne plus retenir pour un nouveau déploiement.

## Quand l'utiliser

- Quasi exclusivement en **maintenance d'un existant** déjà bâti sur TorchServe.
- Pour un nouveau projet PyTorch → préférer une alternative maintenue ci-dessous.

## Quand NE PAS l'utiliser

- **Tout nouveau déploiement** : projet non maintenu, vulnérabilités non corrigées.
- Serving PyTorch moderne et maintenu → [[Dev/Services/BentoML|BentoML]] (packaging Python) ou [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] (backend LibTorch, perf GPU).
- Déploiement Kubernetes standardisé → [[Dev/Services/KServe|KServe]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; self-host (conteneur ou binaire), frontend Java + workers Python.
- **Plus de releases** : dépôt archivé en lecture seule depuis août 2025.
- Scaling distribué via réplicas (souvent sous KServe par le passé).

## Pièges

- **Non maintenu** : pas de correctif de sécurité — risque de conformité en production.
- Le couple **frontend Java / handler Python** complique le débogage et l'image (deux runtimes).
- Écrire un `handler` correct (batch, device, sérialisation) est moins trivial qu'il n'y paraît.

## Alternatives

- [[Dev/Services/BentoML|BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Dev/Services/KServe|KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Dev/Services/Seldon Core|Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[Dev/Services/TensorFlow Serving|TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Servait les modèles de [[Dev/Services/PyTorch|PyTorch]] (équivalent PyTorch de [[Dev/Services/TensorFlow Serving|TensorFlow Serving]]).
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc (archive) : https://docs.pytorch.org/serve/
