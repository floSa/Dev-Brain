---
galaxie: dev
type: service
nom: ONNX Runtime
alias: [onnxruntime, ort, ONNX RT]
pitch: "Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge."
categorie: ml/serving
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/TensorRT|TensorRT]]"]
remplace_par: []
status: actif
tags: [inference, model-serving, inference-optimization, gpu, quantization]
url_docs: https://onnxruntime.ai/docs/
url_repo: https://github.com/microsoft/onnxruntime
---

# ONNX Runtime

## Pourquoi

Moteur d'inférence haute performance pour les modèles exportés au format **ONNX** (standard d'échange de réseaux, entre PyTorch, TensorFlow, scikit-learn…). Cœur **C++** avec des bindings Python, C#, Java, JS : on entraîne dans n'importe quel framework, on exporte en ONNX, et le même artefact s'exécute partout. Sa force est l'abstraction des **Execution Providers** : une même API de session route le calcul vers le meilleur backend matériel disponible — CPU, CUDA, **TensorRT**, OpenVINO, DirectML, CoreML, ROCm, NNAPI — sans changer le code applicatif. Applique aussi des optimisations de graphe (fusion d'opérateurs, constant folding) et la **quantization** (INT8/dynamique) pour alléger le modèle.

## Quand l'utiliser

- **Découpler l'entraînement du déploiement** : exporter une fois en ONNX, servir sur des cibles hétérogènes (serveur, mobile, edge, navigateur via WASM).
- **Accélérer l'inférence CPU** ou GPU sans réécrire le modèle (optimisations de graphe, quantization).
- Cible matérielle variable ou non-NVIDIA : DirectML (Windows), OpenVINO (Intel), CoreML (Apple) via le bon Execution Provider.
- Embarqué comme **runtime** derrière un serveur de modèles ([[Dev/Services/NVIDIA Triton|NVIDIA Triton]] l'utilise comme backend).

## Quand NE PAS l'utiliser

- Besoin d'un **serveur** complet (batching dynamique, multi-modèles, API gérée, métriques) → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] ou [[Dev/Services/BentoML|BentoML]] ; ONNX Runtime n'est qu'un moteur d'exécution.
- **Latence GPU NVIDIA absolument minimale** → [[Dev/Services/TensorRT|TensorRT]] compile un moteur plus agressif (ONNX Runtime peut d'ailleurs déléguer à TensorRT via son EP).
- Modèle PyTorch jamais exporté et boucle d'inférence simple : `torch` natif suffit, l'export ONNX ajoute une étape.

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add onnxruntime` (CPU) ou `onnxruntime-gpu` (CUDA). Paquets distincts par Execution Provider.
- Self-host : bibliothèque liée dans l'application, pas de service à exploiter. Empreinte légère, adaptée à l'edge.
- Coût = le matériel sous-jacent ; aucun service managé propre (Microsoft l'utilise dans Azure ML et Windows ML).

## Pièges

- L'**export ONNX** est le point de friction : opérateurs non supportés, opset à aligner, formes dynamiques mal capturées → divergence ou échec de conversion. Toujours valider l'égalité numérique avant/après export.
- Installer le **mauvais paquet** (`onnxruntime` au lieu d'`onnxruntime-gpu`) → exécution silencieusement sur CPU.
- Un Execution Provider listé ne garantit pas que **tout** le modèle y tourne : les opérateurs non couverts retombent sur CPU (fallback), annulant le gain.
- Versions de l'EP TensorRT/CUDA à appairer précisément avec le driver et CUDA.

## Alternatives

- [[Dev/Services/TensorRT|TensorRT]] — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM.

Nuance : ONNX Runtime est **portable et multi-backend** (le même artefact partout) ; TensorRT est **mono-vendeur** (NVIDIA) et pousse l'optimisation GPU plus loin. Les deux se composent : l'Execution Provider TensorRT d'ONNX Runtime délègue les sous-graphes compilables à TensorRT et garde le reste portable.

## Liens

- [[Dev/Services/TensorRT|TensorRT]], OpenVINO, DirectML — Execution Providers d'accélération.
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — serveur qui utilise ONNX Runtime comme backend d'inférence.
- [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/TensorFlow|TensorFlow]] — frameworks d'entraînement exportant vers ONNX.
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie.
- Doc : https://onnxruntime.ai/docs/
