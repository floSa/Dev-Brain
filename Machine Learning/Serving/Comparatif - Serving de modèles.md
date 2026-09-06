---
role: comparatif
nom: Comparatif - Serving de modèles
categorie: ml/serving
tags: [model-serving, inference, kubernetes]
---

# Comparatif - Serving de modèles

> On tranche sur : un moteur d'exécution ou un serveur complet, un seul framework ou tous, et l'infrastructure qu'on accepte d'opérer.

![[Comparatif - Serving de modèles.base]]

## Ce qui départage

- [[BentoML]] — le **Bento** : un artefact versionné qui fige modèle, code et environnement, conteneurisable. C'est du Python de bout en bout, donc la logique métier autour de l'inférence est libre — mais le batching GPU fin lui manque.
- [[NVIDIA Triton]] — cœur C++ : **batching dynamique** et exécution concurrente de plusieurs modèles sur le même GPU, derrière une seule API. Le prix est un `model_repository` à arborescence stricte, qui échoue en silence s'il est mal formé.
- [[KServe]] — le déploiement est une **ressource déclarative Kubernetes** (`InferenceService`), avec scale-to-zero Knative et canary. Le scale-from-zero coûte un démarrage à froid, sensible sur un gros modèle GPU.
- [[Ray Serve]] — l'autoscaling et la composition de graphes s'écrivent **en Python**, sans opérateur Kubernetes, dans le même runtime que l'entraînement ; indissociable de [[Ray]] et de sa complexité.
- [[Seldon Core]] — le graphe d'inférence complet, explainers (Alibi) et détection de drift compris. Le critère décisif n'est pas technique : depuis le 22 janvier 2024 il est en **BSL**, gratuit hors production, payant en production.
- [[TensorFlow Serving]] — mono-framework par construction (`SavedModel`), mais avec versionnage, hot-reload et les deux protocoles REST et gRPC ; hors de TensorFlow, il ne sert à rien.
- [[TorchServe]] — l'équivalent PyTorch historique, frontend Java et handlers Python : **dépôt archivé le 7 août 2025**, plus aucun correctif de sécurité. Maintenance d'existant seulement.
- [[ONNX Runtime]] — pas un serveur mais un **moteur** : un modèle exporté une fois, exécuté partout via les Execution Providers (CUDA, TensorRT, OpenVINO, CoreML, WASM). Un opérateur non couvert retombe sur CPU sans le dire.
- [[TensorRT]] — compile le réseau en un **moteur figé sur une architecture GPU et une version**, avec quantization FP8/INT8 : la latence la plus basse sur NVIDIA, à rebuild pour chaque cible, et à valider en précision et pas seulement en vitesse.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
