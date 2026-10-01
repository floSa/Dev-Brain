---
role: brique
nom: ONNX Runtime
alias: [onnxruntime, ort, ONNX RT]
pitch: "Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge."
categorie: ml/serving
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[TensorRT]]", "[[OpenVINO]]", "[[LiteRT]]"]
complements: ["[[NVIDIA Triton]]"]
tags: [inference, edge-inference, model-serving, inference-optimization, gpu, quantization]
url_docs: https://onnxruntime.ai/docs/
url_repo: https://github.com/microsoft/onnxruntime
---

# ONNX Runtime

<!-- AUTO:BANDEAU:START -->
> Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur d'inférence pour les modèles exportés au format **ONNX**, le standard d'échange de
réseaux entre PyTorch, TensorFlow et scikit-learn. Cœur C++ avec bindings Python, C#, Java et
JS : on entraîne dans le framework qu'on veut, on exporte une fois, et le même artefact
s'exécute partout. Sa force est l'abstraction des **Execution Providers** — une même API de
session route le calcul vers le meilleur backend disponible (CPU, CUDA, TensorRT, OpenVINO,
DirectML, CoreML, ROCm, NNAPI) sans toucher au code applicatif — à quoi s'ajoutent les
optimisations de graphe (fusion d'opérateurs, constant folding) et la quantization INT8. Ce
n'est pas un serveur : ni API gérée, ni batching dynamique, ni gestion multi-modèles.

Relevé le 2026-10-01 : **1.30.0** du 2026-09-10 sur PyPI, licence MIT (fichier `LICENSE`). Les roues `onnxruntime` couvrent Linux x86_64 et aarch64, Windows amd64 et ARM64, macOS ARM64 (Python 3.11 ou plus). Pour le CPU et le matériel modeste, la page officielle des fournisseurs liste XNNPACK, oneDNN et OpenVINO (Intel), ainsi que Arm ACL et Arm NN, maintenus par la communauté.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Découpler entraînement et déploiement : exporter une fois, servir sur des cibles hétérogènes (serveur, mobile, edge, navigateur via WASM) | L'export ONNX est le point de friction : opérateur non supporté, opset à aligner, formes dynamiques mal capturées — valider l'égalité numérique avant et après |
| Accélérer l'inférence CPU ou GPU sans réécrire le modèle | Installer le mauvais paquet (`onnxruntime` au lieu d'`onnxruntime-gpu`) fait tourner sur CPU sans le dire |
| Cible matérielle variable ou non-NVIDIA : DirectML, OpenVINO, CoreML via le bon Execution Provider | Un Execution Provider listé ne garantit pas que tout le modèle y tourne : les opérateurs non couverts retombent sur CPU, et le gain avec |
| Embarquer un runtime d'inférence derrière un serveur de modèles | Les versions de l'EP TensorRT/CUDA sont à appairer précisément avec le driver |
| Un parc CPU x86_64 ou ARM64 sans GPU : les roues `onnxruntime` suffisent, XNNPACK en complément | Le fournisseur OpenVINO est un paquet à part (`onnxruntime-openvino`, 1.24.1 du 2026-02-26, quand le cœur est à 1.30.0), réservé à Intel : pour un parc Intel, comparer avec [[OpenVINO]] en direct |

## Mise en œuvre

- Installation — `uv add onnxruntime` (CPU) ou `onnxruntime-gpu` (CUDA) ; un paquet distinct par Execution Provider
- Point d'entrée — une `InferenceSession` en Python, ou les bindings C#, Java, JS
- Prérequis — un modèle exporté en ONNX ; pour un EP accéléré, la paire driver/CUDA correspondante
- Exécution — bibliothèque liée dans l'application, empreinte légère, adaptée à l'edge ; rien à héberger
- Coût — MIT ; aucun service managé propre, le coût est celui du matériel sous-jacent

## Écosystème

### Alternatives

- [[TensorRT]] — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM.
- [[OpenVINO]] — Boîte à outils d'inférence d'Intel en C++, API Python, C et Node.js : lit ONNX, PyTorch, TensorFlow et TFLite, optimise pour CPU, GPU intégré et NPU Intel, avec un plug-in CPU ARM listé comme supporté mais sans support AMD ; quantification NNCF et serveur OpenVINO Model Server ; Apache-2.0. — le même objectif sur matériel Intel, avec ses propres conversion, quantification et serveur ; ONNX Runtime peut aussi lui déléguer.
- [[LiteRT]] — Runtime d'inférence de Google pour modèles .tflite (ex TensorFlow Lite, renommé en 2024), cœur C++ avec API Python, Kotlin, JavaScript et Swift : CPU via XNNPACK, GPU et NPU selon la plate-forme, conversion PyTorch par litert-torch encore en bêta, aucun serveur intégré ; Apache-2.0. — le format `.tflite` et une bibliothèque plus petite, mais sans lecture directe d'ONNX.

### Compléments

- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo. — le serveur qui l'embarque comme backend d'inférence

## Ressources

- Documentation — https://onnxruntime.ai/docs/
- Dépôt — https://github.com/microsoft/onnxruntime

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[Comparatif - Runtimes d'inférence CPU et edge]] — ce qui départage les moteurs d'exécution pour CPU et matériel d'atelier
- [[Inférence en bordure - modèles sur du matériel d'atelier]] — la notion : inférer sur place, avec ce moteur ou un autre
- [[PyTorch]], [[TensorFlow]] — les frameworks d'entraînement qui exportent vers ONNX
