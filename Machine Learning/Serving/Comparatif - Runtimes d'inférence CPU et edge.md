---
role: comparatif
nom: Comparatif - Runtimes d'inférence CPU et edge
categorie: ml/serving
tags: [inference, edge-inference, quantization]
---

# Comparatif - Runtimes d'inférence CPU et edge

> On tranche sur : le matériel de la cible (Intel, ARM, NVIDIA, mixte), le format dont on part, et si l'on accepte de convertir le modèle pour chaque famille de machines.

![[Comparatif - Runtimes d'inférence CPU et edge.base]]

## Ce qui départage

- [[ONNX Runtime]] — le **seul qui ne soit pas lié à un fabricant** : un modèle exporté en ONNX, un même code, et des fournisseurs d'exécution par cible (XNNPACK, OpenVINO, CUDA, TensorRT). Les fournisseurs sont des paquets séparés et décalés : celui d'OpenVINO est à 1.24.1 quand le cœur est à 1.30.0 (PyPI, 2026-10-01).
- [[OpenVINO]] — le plus complet **sur du matériel Intel** : CPU, GPU intégré et NPU, conversion directe depuis ONNX, TensorFlow, TFLite et PyTorch, quantification NNCF, serveur OVMS à part. Le prix est le périmètre : AMD n'est pas validé, et l'INT8 est simulé sur ARM.
- [[LiteRT]] — la **bibliothèque la plus petite**, issue de TensorFlow Lite : un `.tflite` exécuté par XNNPACK sur CPU x86_64 ou ARM64. Il faut convertir (aucune lecture d'ONNX), et la conversion PyTorch est encore en bêta.
- [[TensorRT]] — la latence la plus basse, mais **uniquement sur GPU NVIDIA** ; hors sujet pour un PC industriel sans GPU, pertinent pour une carte embarquée NVIDIA ou une station équipée.

## Critères, un par un

| Critère | ONNX Runtime | OpenVINO | LiteRT | TensorRT |
|---|---|---|---|---|
| Matériel | CPU x86_64 et ARM64 (roues), accélérateurs par fournisseur | CPU, GPU et NPU Intel ; CPU ARM listé ; pas d'AMD validé | CPU x86_64 et ARM64 (XNNPACK), GPU et NPU selon la plate-forme | GPU NVIDIA seul |
| Format de départ | ONNX | IR, ONNX, TensorFlow, TFLite, Paddle ; PyTorch par conversion | `.tflite` | réseau compilé en moteur figé |
| Conversion | export ONNX depuis le framework | `ovc` ou `convert_model` | convertisseur TensorFlow, `litert-torch` en bêta, pas d'ONNX direct | construction du moteur par cible |
| Quantification | INT8 | NNCF : INT8, compression des poids ; INT8 simulé sur ARM | post-entraînement (dynamique, entière, float16) ; quantificateur en alpha | FP8, INT8 |
| Serveur intégré | non | OVMS, dépôt distinct | non | non (Triton) |
| Licence | MIT | Apache-2.0 | Apache-2.0 | cœur propriétaire, composants Apache-2.0 |
| Version relevée | 1.30.0 (2026-09-10) | 2026.4.0 / 2026.4.1 (2026-09-16 / 2026-10-01) | 2.2.0 (2026-08-13) | voir sa fiche |

**Performance sur CPU sans GPU : aucun chiffre comparatif cité.** Les benchmarks lus sont ceux des éditeurs, sur leur propre matériel (Intel pour OpenVINO) ; aucune mesure neutre, datée et reproductible des quatre runtimes sur un même PC industriel n'a été trouvée. À mesurer sur la machine cible avec le modèle réel.

## Voisins relevés, sans fiche

Relevé le 2026-10-01 (dernière publication PyPI ou tag, étoiles GitHub) :

- **ExecuTorch** (PyTorch, BSD, 1.5.1 du 2026-09-22, environ 5 100 étoiles) — runtime de la chaîne PyTorch pour mobile et embarqué, avec un backend XNNPACK ; à regarder quand tout le parc est en PyTorch.
- **ncnn** (Tencent, BSD-3-Clause, 1.0.20260526, environ 23 900 étoiles) et **MNN** (Alibaba, Apache-2.0, 3.6.1, environ 16 200 étoiles) — moteurs CPU ARM et x86 actifs, avec leurs propres outils de conversion ; écartés ici par le plafond du lot, pas par leur maturité.
- **Apache TVM** (Apache-2.0, 0.27.0.post1 du 2026-09-29, environ 13 800 étoiles) — un compilateur à intégrer, à l'effort élevé ; ONNX Runtime le liste en fournisseur communautaire en préversion.
- **TensorFlow Lite Micro** — microcontrôleurs et DSP : hors du périmètre d'un PC industriel.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Comparatif - Serving de modèles]] — le même dossier, vu des serveurs et des plateformes plutôt que des moteurs d'exécution.
- [[Inférence en bordure - modèles sur du matériel d'atelier]] — la notion : pourquoi et comment inférer sur du matériel d'atelier.
