---
role: brique
nom: TensorFlow Serving
alias: [tf-serving, tensorflow-serving, tfserving]
pitch: "Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[KServe]]", "[[Seldon Core]]", "[[TorchServe]]", "[[Ray Serve]]"]
complements: []
tags: [model-serving, inference, gpu]
url_docs: https://www.tensorflow.org/tfx/guide/serving
url_repo: https://github.com/tensorflow/serving
---

# TensorFlow Serving

<!-- AUTO:BANDEAU:START -->
> Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur d'inférence dédié aux modèles TensorFlow/Keras au format `SavedModel`. Cœur C++
éprouvé, taillé pour servir en continu : **API REST (JSON) et gRPC (Protobuf)**, **versionnage** des modèles
avec chargement et déchargement à chaud et politiques de version, **batching** des requêtes.
Un nouveau modèle se charge sans redémarrer le serveur. C'est la brique de déploiement
historique de l'écosystème TensorFlow, intégrée aux pipelines TFX. Mono-framework par
construction : il lui faut un `SavedModel`, et hors de TensorFlow il ne sert à rien.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Servir des modèles TensorFlow/Keras en production, avec versionnage et rechargement à chaud | La signature du `SavedModel` — noms d'entrées et de sorties — doit être exacte, sinon les erreurs d'inférence sont opaques |
| Besoin des deux protocoles REST et gRPC, du batching et de métriques de serving standard | Image GPU liée à une matrice CUDA/cuDNN précise, comme le reste de l'écosystème TF |
| Pipeline TFX déjà en place de bout en bout | |
| Latence serveur faible sur un parc mono-framework | |

## Mise en œuvre

- Installation — conteneur `tensorflow/serving`, ou binaire
- Point d'entrée — un `SavedModel` déposé dans le répertoire de modèles ; API REST et gRPC
- Prérequis — un modèle TensorFlow exporté en `SavedModel` ; GPU optionnel
- Exécution — self-hébergé, CPU ou GPU ; réplicas pilotés par l'orchestrateur
- Coût — Apache-2.0, aucune offre SaaS propre ; le coût est celui des serveurs

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Ressources

- Documentation — https://www.tensorflow.org/tfx/guide/serving
- Dépôt — https://github.com/tensorflow/serving

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[TensorFlow]] — le framework dont il sert les modèles
