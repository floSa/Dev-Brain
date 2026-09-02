---
role: hub
nom: Serving
alias: [serving de modèles, inférence]
pitch: Exposer un modèle déjà entraîné derrière une API — et tenir la latence, le débit et les versions.
domaines: [mlops, ml-eng]
tags: [model-serving, inference, deployment-strategy, kubernetes, gpu, inference-optimization]
---

# Serving

> Exposer un modèle déjà entraîné derrière une API — et tenir la latence, le débit et les versions.

## Ce qu'il faut comprendre

- **Ce dossier commence là où l'entraînement s'arrête.** Rien ici n'entraîne : ce sont [[Apprentissage profond]], [[Tabulaire]] ou [[Séries temporelles]] qui produisent l'artefact, [[Suivi d'expériences]] qui dit lequel, et ce dossier qui l'expose. La confusion voisine est avec [[Runtimes]] : servir un LLM génératif est un métier distinct — batching continu, cache d'attention, tokens en flux — et il a son propre outillage.
- **Un serveur de modèle n'est pas un serveur web avec un `model.predict` dedans**, et c'est l'erreur la plus fréquente. Ce qu'il apporte est le batching dynamique (regrouper des requêtes arrivées séparément pour une seule passe GPU), l'exécution concurrente de plusieurs modèles, le versionnage avec bascule, et la métrologie. [[Déploiement de modèles]] pose le cadre, [[Model registry & versioning]] la traçabilité de ce qui est servi.
- **Le premier arbitrage est le socle, pas la performance** : Kubernetes ou pas. Si le cluster existe déjà, l'outillage déclaratif s'y greffe et le scaling vient avec. Sinon, un serveur autonome évite d'importer une plateforme entière pour trois endpoints.
- **Le second arbitrage est le format**. Servir le framework d'entraînement tel quel est simple mais lie la production à PyTorch ou TensorFlow. Exporter vers un format intermédiaire découple les deux et ouvre l'optimisation matérielle — au prix d'une étape de conversion qui peut échouer sur les opérateurs exotiques, et qu'il faut donc tester tôt.
- **La latence se gagne surtout avant le serveur.** [[Quantization]], [[Pruning]] et [[Distillation]] réduisent le modèle lui-même, et gagnent des ordres de grandeur là où le réglage du serveur gagne des pourcents. Un modèle non compressé servi parfaitement reste un modèle lent.
- **Servir n'est pas surveiller** : un endpoint qui répond en 20 ms peut répondre faux depuis trois semaines. [[Monitoring de modèle en production]] et [[Data drift]] sont la moitié manquante, outillée au niveau du domaine par [[Evidently]].
- Le décalage entre les features d'entraînement et celles calculées à l'inférence est l'autre panne silencieuse classique — [[Feature store — concept]], et [[Feast]] au niveau du domaine.

## Choisir

- Un socle Kubernetes déjà en place, du déclaratif, de l'autoscaling jusqu'à zéro → [[KServe]].
- Le débit maximal sur GPU, plusieurs frameworks sur le même serveur → [[NVIDIA Triton]].
- Packager n'importe quel modèle Python en service, sans Kubernetes obligatoire → [[BentoML]].
- Composer plusieurs modèles dans un même graphe d'inférence, en Python → [[Ray Serve]].
- Un modèle exporté à faire tourner partout — CPU, GPU, embarqué → [[ONNX Runtime]].
- La dernière fraction de latence sur GPU NVIDIA → [[TensorRT]], après export.
- Un existant TensorFlow / TFX → [[TensorFlow Serving]].
- Des graphes d'inférence multi-étapes sur Kubernetes → [[Seldon Core]], en vérifiant sa licence BSL depuis 2024.
- Un projet PyTorch historique → [[TorchServe]], à ne plus retenir pour du neuf : archivé depuis août 2025. Cf. [[Comparatif - Serving de modèles]].
- Servir un LLM génératif → [[Runtimes]], pas ce dossier.

<!-- AUTO:START -->
### Briques
- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[TensorRT]] — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.

### Comparatifs
- [[Comparatif - Serving de modèles]]
<!-- AUTO:END -->

## Notes
