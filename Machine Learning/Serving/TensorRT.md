---
role: brique
nom: TensorRT
alias: [tensorrt, trt, TensorRT-LLM, NVIDIA TensorRT]
pitch: "SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM."
categorie: ml/serving
famille: paquet
licence_type: proprietary
maturite: production
langage: C++
alternatives: ["[[ONNX Runtime]]"]
complements: ["[[NVIDIA Triton]]"]
tags: [inference, inference-optimization, model-serving, gpu, quantization]
url_docs: https://docs.nvidia.com/deeplearning/tensorrt/
url_repo: https://github.com/NVIDIA/TensorRT
---

# TensorRT

<!-- AUTO:BANDEAU:START -->
> SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++ | propriétaire | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

SDK d'inférence de NVIDIA, spécialisé pour ses propres GPU. À partir d'un modèle entraîné,
souvent passé par un export ONNX, il le **compile en un « moteur »** optimisé pour une
architecture GPU donnée : fusion de couches, sélection automatique des kernels les plus
rapides, calibration et **quantization** (FP16, INT8, FP8, NVFP4), gestion fine de la mémoire.
Le gain en latence et en débit est important, au prix d'une étape de build et d'un couplage
matériel fort. La déclinaison **TensorRT-LLM** applique ces optimisations aux grands modèles de
langage — paged attention, in-flight batching, décodage spéculatif.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Latence et débit GPU NVIDIA maximaux en production, quand la milliseconde ou le token/s comptent | La conversion ONNX → TensorRT échoue sur les opérateurs non supportés et les formes dynamiques mal gérées, et le débogage est pénible |
| Servir des LLM sur GPU NVIDIA via TensorRT-LLM (FP8/NVFP4, batching in-flight) | Un moteur compilé est figé sur une architecture GPU et une version de TensorRT : à rebuild pour chaque cible, et à versionner |
| Stack NVIDIA de bout en bout, moteurs exécutés par un serveur d'inférence | La quantization INT8 exige une calibration soignée : valider la précision, pas seulement la vitesse |
| Edge NVIDIA (Jetson), où l'optimisation matérielle est décisive | Cœur fermé : aucun patch possible, et une dépendance forte au calendrier NVIDIA |

## Mise en œuvre

- Installation — SDK NVIDIA, `pip install tensorrt`, ou surtout les conteneurs NGC
- Point d'entrée — un build de moteur depuis un ONNX (`trtexec` ou l'API), puis le runtime C++/Python
- Prérequis — GPU NVIDIA, et une matrice CUDA/driver/GPU précise
- Exécution — self-hébergé sur GPU NVIDIA (data center, cloud, Jetson) ; aucune offre SaaS
- Coût — cœur sous NVIDIA Software License Agreement, gratuit d'usage mais fermé ; parsers, plugins, samples et TensorRT-LLM sous Apache-2.0. Le coût réel est le GPU et l'ingénierie de conversion

## Écosystème

### Alternatives

- [[ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge.

### Compléments

- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo. — le serveur qui exécute les moteurs compilés

## Ressources

- Documentation — https://docs.nvidia.com/deeplearning/tensorrt/
- Dépôt — https://github.com/NVIDIA/TensorRT

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[PyTorch]] — `torch-tensorrt` compile un moteur directement depuis PyTorch
