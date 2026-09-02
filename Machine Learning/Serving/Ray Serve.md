---
role: brique
nom: Ray Serve
alias: [ray serve, ray.serve, rayserve]
pitch: "Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[KServe]]", "[[Seldon Core]]", "[[TorchServe]]", "[[TensorFlow Serving]]"]
complements: []
tags: [model-serving, inference, distributed]
url_docs: https://docs.ray.io/en/latest/serve/
url_repo: https://github.com/ray-project/ray
---

# Ray Serve

## Pourquoi

Bibliothèque de **serving de modèles** de l'écosystème [[Ray]], écrite en Python pur et agnostique au framework (PyTorch, TensorFlow, scikit-learn, transformers, code custom). Une **deployment** est une classe Python décorée (`@serve.deployment`) que Ray réplique et autoscale sur le cluster ; plusieurs deployments se composent en **graphes d'inférence** (deployment graphs) pour les pipelines multi-modèles ou multi-étapes. Hérite du scaling de Ray (du laptop au cluster) et s'intègre à FastAPI pour l'API HTTP. Volet LLM dédié (Ray Serve LLM) pour le serving haut débit.

## Quand l'utiliser

- Déjà sur [[Ray]] : servir les modèles dans le **même runtime** que l'entraînement / le traitement.
- **Composition multi-modèles** : pipelines, ensembles, routage, business logic Python autour de l'inférence.
- Besoin d'**autoscaling** (y compris scale-to-zero) piloté en Python, sans écrire d'opérateur Kubernetes.
- Servir des modèles de **tout framework** derrière une API FastAPI.

## Quand NE PAS l'utiliser

- Packaging d'un artefact portable standardisé (Bento) hors cluster Ray → [[BentoML]].
- Débit/latence GPU maximal avec batching dynamique multi-framework → [[NVIDIA Triton]].
- Standard d'inférence déclaratif natif Kubernetes (CRD, scale-to-zero Knative) → [[KServe]].
- Pas de cluster Ray et pas l'intention d'en opérer un → un serveur mono-modèle plus simple suffit.

## Déploiement & coût

- Open-source (Apache-2.0), `uv add "ray[serve]"`. Tourne partout où Ray tourne.
- **Self-host** : sur un cluster Ray (local, Kubernetes via KubeRay, cloud).
- **Managé** : Anyscale (payant) — clusters Ray opérés avec Serve intégré.
- Scaling distribué natif (réplicas par deployment, autoscaling) ; coût = l'infra du cluster.

## Pièges

- Indissociable de [[Ray]] : on hérite aussi de sa complexité (cluster, object store, sérialisation).
- L'**autoscaling** demande un réglage fin (min/max réplicas, fenêtres) pour éviter le ping-pong ou la latence de démarrage à froid.
- Pour la latence GPU pure, le serveur Python n'a pas le batching fin d'un [[NVIDIA Triton]] : on les combine parfois (Serve devant, Triton en runtime).

## Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.

## Liens

- Famille Ray : [[Ray]] (cœur distribué), [[Ray Tune]] (HPO).
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Sert des modèles de tout framework : [[PyTorch]], [[Scikit-Learn]], [[HuggingFace]].
- Doc : https://docs.ray.io/en/latest/serve/
