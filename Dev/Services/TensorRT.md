---
galaxie: dev
type: service
nom: TensorRT
alias: [tensorrt, trt, TensorRT-LLM, NVIDIA TensorRT]
pitch: "SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM."
categorie: ml/serving
licence_type: proprietary
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/ONNX Runtime|ONNX Runtime]]"]
remplace_par: []
status: actif
tags: [inference, inference-optimization, model-serving, gpu, quantization]
url_docs: https://docs.nvidia.com/deeplearning/tensorrt/
url_repo: https://github.com/NVIDIA/TensorRT
---

# TensorRT

## Pourquoi

SDK d'inférence haute performance de NVIDIA, spécialisé pour ses propres GPU. À partir d'un modèle entraîné (souvent via [[Dev/Services/ONNX Runtime|ONNX]]), TensorRT le **compile en un « moteur » optimisé** pour une architecture GPU donnée : fusion de couches, sélection automatique des kernels les plus rapides (auto-tuning), calibration et **quantization** (FP16, INT8, FP8, NVFP4), gestion fine de la mémoire. Le gain en latence et en débit est important, au prix d'une étape de build et d'un couplage matériel fort. La déclinaison **TensorRT-LLM** (Apache-2.0) applique ces optimisations aux grands modèles de langage (paged attention, in-flight batching, décodage spéculatif), brique de la stack d'inférence NVIDIA (Triton, Dynamo, NIM).

## Quand l'utiliser

- **Latence/débit GPU NVIDIA maximaux** en production (vision, LLM) où chaque milliseconde et chaque token/s comptent.
- Servir des **LLM** efficacement sur GPU NVIDIA → TensorRT-LLM (FP8/NVFP4, batching in-flight).
- Stack NVIDIA de bout en bout : moteurs TensorRT servis par [[Dev/Services/NVIDIA Triton|NVIDIA Triton]].
- Edge NVIDIA (Jetson) où l'optimisation matérielle est décisive.

## Quand NE PAS l'utiliser

- **Pas de GPU NVIDIA** ou besoin de portabilité multi-cibles → [[Dev/Services/ONNX Runtime|ONNX Runtime]] (CPU, AMD, Intel, Apple, navigateur).
- On veut un **serveur** clé en main (API, multi-modèles, batching, métriques) → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]], qui exécute les moteurs TensorRT.
- Prototype ou faible volume : le **coût de build** et la complexité de conversion ne se rentabilisent pas.

## Déploiement & coût

- **Cœur propriétaire** (NVIDIA Software License Agreement), gratuit d'usage mais fermé ; composants OSS (parsers, plugins, samples) et **TensorRT-LLM** sous Apache-2.0 sur GitHub.
- Distribué via le SDK NVIDIA, pip (`tensorrt`) et surtout les conteneurs **NGC** ; lié à une matrice CUDA/driver/GPU précise.
- Self-host sur GPU NVIDIA (data center, cloud, Jetson) ; pas d'offre SaaS directe. Coût = matériel GPU + ingénierie de conversion.

## Pièges

- La **conversion ONNX → TensorRT** échoue sur les opérateurs non supportés ou les formes dynamiques mal gérées — débogage souvent pénible.
- Un moteur compilé est **figé sur l'architecture GPU** et la version de TensorRT : non portable, à rebuild pour chaque cible (et à versionner).
- La **quantization INT8** exige une calibration soignée sous peine de perte de précision silencieuse — valider la qualité, pas seulement la vitesse.
- Cœur propriétaire : pas de patch possible, dépendance forte à l'écosystème et au calendrier NVIDIA.

## Alternatives

- [[Dev/Services/ONNX Runtime|ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge.

Nuance : TensorRT vise la **performance maximale sur GPU NVIDIA**, au prix de la portabilité et d'une compilation figée ; ONNX Runtime privilégie le **« écrire une fois, exécuter partout »**. Ils se composent — ONNX Runtime peut déléguer à TensorRT via son Execution Provider.

## Liens

- [[Dev/Services/ONNX Runtime|ONNX Runtime]] — chemin d'entrée fréquent (export ONNX → build TensorRT) et alternative portable.
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — serveur exécutant les moteurs TensorRT.
- [[Dev/Services/PyTorch|PyTorch]] — `torch-tensorrt` compile directement depuis PyTorch.
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie.
- Doc : https://docs.nvidia.com/deeplearning/tensorrt/
