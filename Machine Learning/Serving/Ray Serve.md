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

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-23 |
<!-- AUTO:BANDEAU:END -->

## Définition

Volet serving de l'écosystème Ray, en Python pur et agnostique au framework (PyTorch,
TensorFlow, scikit-learn, transformers, code custom). Une **deployment** est une classe
décorée `@serve.deployment` que Ray réplique et autoscale sur le cluster ; plusieurs
deployments se composent en **graphes d'inférence** pour les pipelines multi-modèles ou
multi-étapes. L'API HTTP passe par FastAPI, et un volet dédié — Ray Serve LLM — couvre le
serving haut débit de grands modèles. Le corollaire tient en une phrase : elle est
indissociable de Ray, dont on hérite le cluster, l'object store et la sérialisation.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déjà sur Ray : servir les modèles dans le même runtime que l'entraînement et le traitement | L'autoscaling demande un réglage fin — min/max réplicas, fenêtres — sous peine de ping-pong ou de démarrage à froid |
| Composition multi-modèles : pipelines, ensembles, routage, logique métier Python autour de l'inférence | Le cluster Ray est un prérequis à opérer, avec sa complexité propre : object store, sérialisation, ordonnancement |
| Autoscaling, scale-to-zero compris, piloté en Python sans écrire d'opérateur Kubernetes | |
| Servir des modèles de tout framework derrière une API FastAPI | |

## Mise en œuvre

- Installation — `uv add "ray[serve]"`
- Point d'entrée — une classe Python décorée `@serve.deployment`, exposée via FastAPI
- Prérequis — un cluster Ray, du laptop au cluster Kubernetes via KubeRay
- Exécution — self-hébergé partout où Ray tourne ; managé par Anyscale
- Coût — Apache-2.0 ; le coût est celui du cluster, et Anyscale est payant

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.

## Ressources

- Documentation — https://docs.ray.io/en/latest/serve/
- Dépôt — https://github.com/ray-project/ray

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[Ray]] — le socle distribué dont Serve est le volet inférence
- [[Ray Tune]] — le volet optimisation d'hyperparamètres de la même famille
