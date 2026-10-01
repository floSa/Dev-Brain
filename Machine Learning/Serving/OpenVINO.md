---
role: brique
nom: OpenVINO
alias: [OpenVINO Toolkit, Intel OpenVINO, OpenVINO Runtime, openvino-toolkit]
pitch: "Boîte à outils d'inférence d'Intel en C++, API Python, C et Node.js : lit ONNX, PyTorch, TensorFlow et TFLite, optimise pour CPU, GPU intégré et NPU Intel, avec un plug-in CPU ARM listé comme supporté mais sans support AMD ; quantification NNCF et serveur OpenVINO Model Server ; Apache-2.0."
categorie: ml/serving
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[ONNX Runtime]]", "[[TensorRT]]"]
complements: ["[[NVIDIA Triton]]", "[[Ultralytics YOLO]]"]
tags: [inference, edge-inference, model-serving, quantization]
url_docs: https://docs.openvino.ai/
url_repo: https://github.com/openvinotoolkit/openvino
---

# OpenVINO

<!-- AUTO:BANDEAU:START -->
> Boîte à outils d'inférence d'Intel en C++, API Python, C et Node.js : lit ONNX, PyTorch, TensorFlow et TFLite, optimise pour CPU, GPU intégré et NPU Intel, avec un plug-in CPU ARM listé comme supporté mais sans support AMD ; quantification NNCF et serveur OpenVINO Model Server ; Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils d'**Intel** pour faire tourner un réseau déjà entraîné sur du matériel Intel : un runtime
en C++ avec des API Python, C et Node.js, des plug-ins par périphérique (CPU, GPU, NPU), un convertisseur
(`ovc`, `openvino.convert_model`) et un format intermédiaire, l'**IR** (paire `.xml` et `.bin`). Il lit
aussi ONNX, TensorFlow, TFLite et PaddlePaddle directement, et PyTorch ou JAX (expérimental) par
conversion en Python ; un backend `torch.compile` existe. S'y ajoutent **NNCF** (quantification et
compression des poids) et **OpenVINO Model Server** (OVMS), dépôts distincts.

Relevé le 2026-10-01 : version **2026.4.0** (notes datées du 2026-09-16), correctif **2026.4.1** publié
sur PyPI le 2026-10-01 sans notes dédiées lues, 10 939 étoiles, dernier commit du 2026-10-01. Numérotation
`année.N` ; environ cinq versions par an en 2026, plus irrégulières en 2024. NNCF 3.4.0 (2026-09-17) ;
OVMS 2026.4.0 (2026-09-17), 940 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un parc de PC industriels à processeur Intel, sans GPU : le plug-in CPU et le GPU ou le NPU intégrés sont la cible nominale | Du matériel AMD : Intel écrit que les Ryzen « ne sont ni validés ni supportés » (article de support) |
| Une vision ou un modèle de maintenance prédictive exporté d'[[Ultralytics YOLO]], de PyTorch ou de TensorFlow, à servir sur place | Un GPU NVIDIA à exploiter à fond : [[TensorRT]], ou [[NVIDIA Triton]] |
| Quantifier en INT8 après entraînement avec NNCF, puis valider la précision | Un modèle déjà au format `.tflite`, sur un équipement non Intel : [[LiteRT]] |
| Un serveur de modèle léger en conteneur (OVMS : API KServe, 237 Mo compressés pour l'image CPU) | Un seul runtime pour tous les matériels de l'atelier : [[ONNX Runtime]] |

## Mise en œuvre

- Installation — `uv add openvino` (roues PyPI : Linux x86_64 et aarch64, Windows amd64, macOS ARM64 ; glibc 2.35 minimum pour aarch64 ; pas de roue armv7 ni Windows ARM) ; archives, APT, Docker et conda existent aussi
- Point d'entrée — `core = ov.Core()`, `model = core.read_model(...)`, `compiled = core.compile_model(model, "CPU")` ; `ovc` convertit en IR, recommandée en production face à la lecture directe d'ONNX ou de TensorFlow (« moins de performance et de stabilité »)
- Prérequis — Python 3.10 ou plus (3.10 abandonné en 2026.5) ; pilotes GPU et NPU installés à part
- Exécution — bibliothèque liée à l'application ; OVMS seul se déploie en conteneur ; indicateurs `LATENCY` (défaut) et `THROUGHPUT`, périphériques `AUTO` et `HETERO` (repli sur CPU des opérateurs non couverts)
- Coût — gratuit ; le support payant passe par Intel Premier Support

## Licence et gouvernance

- **Apache-2.0** pour OpenVINO, NNCF et OVMS (fichiers `LICENSE` et API GitHub). Aucun EULA séparé trouvé pour les roues PyPI ; l'archive et le paquet APT n'ont pas été lus.
- **Ce que permet la licence** : utiliser chez un client, embarquer dans un produit livré et le revendre, en conservant les notices. Les pilotes GPU et NPU d'Intel sont hors du paquet et leur licence n'a pas été lue ; le plug-in pour GPU NVIDIA vit dans `openvino_contrib`, hors de la distribution officielle. L'Open Model Zoo (Apache-2.0, en mode maintenance, dernière release 2024.6.0 du 2024-12-19) garde la licence amont de chaque modèle : la lire modèle par modèle. **Lecture, sans valeur juridique.**
- **Gouvernance** : Intel, sans fondation. Politique de support écrite : le dernier numéro de l'année devient une version à support long (2 ans de sécurité, 1 an de correctifs) mais aucune version 2025 ou 2026 n'est nommée ainsi dans ce qui a été lu, et NNCF et OVMS en sont exclus.
- **Télémétrie** : activée par défaut pour les outils (conversion, Model Downloader, NNCF), via Google Analytics ; `opt_in_out --opt_out` la coupe. À faire avant un déploiement hors ligne.

## Limites à connaître

- **Le matériel supporté, c'est Intel.** ARM figure dans la page des exigences (armv7a et arm64-v8a ; Ubuntu 22.04 ARM64, macOS), mais l'INT8 y est exécuté en simulation flottante, le BF16 n'y existe pas et Windows ARM64 n'est pas supporté. Les chiffres de performance d'Intel portent sur des périphériques Intel : aucun benchmark AMD ou ARM citable.
- **NPU : formes statiques**, avec un mode dynamique en préversion limité à la vision (2026.4) ; Core Ultra seulement, Windows 11 et Ubuntu.
- **Numérotation qui avance vite.** Le Kubernetes Operator d'OVMS est déprécié au profit de KServe, et l'API TensorFlow Serving d'OVMS est supprimée depuis la 2026.3. Épingler la version.
- **Contradiction non tranchée** : les notes de 2026.1 disent que le runtime ne demande que NumPy, mais les métadonnées PyPI de la 2026.4.1 listent encore `openvino-telemetry`.
- **Taille** : roue Linux x86_64 de 59,1 Mo compressés ; image Docker `ubuntu24_runtime` de 536 Mo compressés en 2026.4.0 contre 337 Mo en 2025.4.0.
- **Via ONNX Runtime**, le fournisseur d'exécution est un paquet séparé (`onnxruntime-openvino`) : 1.24.1 du 2026-02-26 quand `onnxruntime` en est à 1.30.0 ; Intel seulement.

## Écosystème

### Alternatives

- [[ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge. — le runtime neutre vis-à-vis du matériel, qui sait déléguer à OpenVINO sur Intel.
- [[TensorRT]] — SDK NVIDIA d'optimisation et d'exécution d'inférence sur GPU NVIDIA — compile un réseau en moteur optimisé (fusion de couches, quantization FP8/INT8, sélection de kernels) pour une latence et un débit maximaux ; cœur propriétaire, composants OSS Apache-2.0, décliné en TensorRT-LLM. — l'équivalent côté NVIDIA : un compilateur propre à un fabricant, à rebâtir pour chaque cible.

### Compléments

- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo. — son backend OpenVINO (CPU Intel seulement dans l'image publique) sert des modèles IR, ONNX, TensorFlow, TFLite et Paddle.
- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0. — il exporte au format `openvino` ; un détecteur entraîné s'exécute ensuite sur CPU et GPU Intel.

## Ressources

- Documentation — https://docs.openvino.ai/
- Dépôt — https://github.com/openvinotoolkit/openvino

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Inférence en bordure - modèles sur du matériel d'atelier]] — la notion : pourquoi et comment inférer sur place
- [[Comparatif - Runtimes d'inférence CPU et edge]] — ce qui départage les runtimes pour CPU et matériel d'atelier
- [[Quantization]] — la notion derrière NNCF
- [[anomalib]] — la bibliothèque de détection d'anomalies visuelles dont l'export `ExportType.OPENVINO` cible ce runtime
