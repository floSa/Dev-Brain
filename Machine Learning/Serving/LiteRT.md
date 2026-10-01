---
role: brique
nom: LiteRT
alias: [TensorFlow Lite, TFLite, ai-edge-litert, Google AI Edge LiteRT, tflite-runtime]
pitch: "Runtime d'inférence de Google pour modèles .tflite (ex TensorFlow Lite, renommé en 2024), cœur C++ avec API Python, Kotlin, JavaScript et Swift : CPU via XNNPACK, GPU et NPU selon la plate-forme, conversion PyTorch par litert-torch encore en bêta, aucun serveur intégré ; Apache-2.0."
categorie: ml/serving
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[ONNX Runtime]]"]
complements: ["[[Ultralytics YOLO]]"]
tags: [inference, edge-inference, quantization, embedded]
url_docs: https://ai.google.dev/edge/litert
url_repo: https://github.com/google-ai-edge/LiteRT
---

# LiteRT

<!-- AUTO:BANDEAU:START -->
> Runtime d'inférence de Google pour modèles .tflite (ex TensorFlow Lite, renommé en 2024), cœur C++ avec API Python, Kotlin, JavaScript et Swift : CPU via XNNPACK, GPU et NPU selon la plate-forme, conversion PyTorch par litert-torch encore en bêta, aucun serveur intégré ; Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Runtime d'inférence **embarqué** de Google, héritier de TensorFlow Lite. Un modèle est converti en
`.tflite` (FlatBuffers) puis exécuté par une bibliothèque légère : sur CPU par XNNPACK, sur GPU et NPU
par des accélérateurs choisis selon la plate-forme. La nouvelle **Compiled Model API** (C++, Python,
Kotlin, JavaScript, Swift) est celle que le README impose pour tout code neuf ; l'`Interpreter`
historique reste disponible en Python (`ai_edge_litert.interpreter`). LiteRT n'entraîne rien et n'embarque
aucun serveur : c'est une bibliothèque liée à l'application.

Le nom a changé : Google a annoncé le 2024-09-04 (billet de blog lu par un résumeur) le passage de
« TensorFlow Lite » à « LiteRT » pour dire qu'il accepte aussi PyTorch, JAX et Keras. Le code
`tensorflow/lite` est en maintenance (correctifs de sécurité et de stabilité seulement, d'après son
README) et le développement a migré vers le dépôt `google-ai-edge/LiteRT`.

Relevé le 2026-10-01 : **v2.2.0** publiée le 2026-08-13 (PyPI `ai-edge-litert` 2.2.0 le 2026-08-12 en UTC),
3 461 étoiles, dernier commit du 2026-10-01, une version stable toutes les six à huit semaines d'après le
README.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un modèle déjà au format TensorFlow, Keras ou `.tflite`, à exécuter sur CPU Linux ou Windows, ARM64 ou x86_64, sans GPU | Un processeur Intel dont on veut tirer le GPU ou le NPU : [[OpenVINO]] |
| Un parc hétérogène où le même `.tflite` doit tourner du téléphone au PC industriel | L'ONNX comme format pivot : aucune lecture directe d'ONNX, la conversion passe par un outil tiers (`onnx2tf`) |
| Une bibliothèque minuscule à lier dans une application C++, sans serveur ni démon | Un serveur de modèles avec batching et API réseau : [[NVIDIA Triton]], [[BentoML]] ou [[KServe]] |
| Un détecteur YOLO exporté en `litert` depuis [[Ultralytics YOLO]] sur Linux x86 | Une cible Linux ARMv7 : pas de roue `ai-edge-litert` ; `tflite-runtime` n'a plus de version depuis 2023-10-03 |

## Mise en œuvre

- Installation — `uv add ai-edge-litert` (Python 3.10 à 3.14 ; roues Linux x86_64 et aarch64, Windows amd64, macOS ARM64) ; `tflite-runtime`, dernier publié le 2023-10-03, n'est plus alimenté
- Point d'entrée — `from ai_edge_litert.compiled_model import CompiledModel`, puis `CompiledModel.from_file("model.tflite")` ; l'ancien `Interpreter` demande seulement de changer le nom du paquet
- Prérequis — pour convertir un modèle PyTorch, `litert-torch` (0.9.4 du 2026-08-24, Linux, torch 2.4 ou plus, TensorFlow nightly, convertisseur en bêta) ; le paquet `ai-edge-torch` est déprécié au profit de `litert-torch`
- Exécution — bibliothèque liée à l'application ; sur CPU, XNNPACK ; GPU par WebGPU (Vulkan) sous Linux, Direct3D sous Windows ; NPU Intel sous Linux et Windows via OpenVINO d'après la doc
- Coût — gratuit ; aucune offre commerciale trouvée

## Licence et gouvernance

- **Apache-2.0** (fichier `LICENSE` et API GitHub) pour LiteRT, `litert-torch` et `ai-edge-quantizer`.
- **Ce que permet la licence** : utiliser chez un client, embarquer dans un produit livré et le revendre, en conservant les notices. Les licences des modèles convertis sont une autre question : l'[[Ultralytics YOLO]] qui sert à les produire est sous AGPL-3.0. **Lecture, sans valeur juridique.**
- **Gouvernance** : Google AI Edge. Le dépôt a été créé le 2024-09-04 et le renommage a déplacé la documentation à deux reprises (tensorflow.org, ai.google.dev, developers.google.com) : vérifier les noms de paquets et les liens avant de s'appuyer sur un tutoriel plus ancien.

## Limites à connaître

- **Linux industriel : support qui se précise.** Le tableau du README donne Linux et Windows avec CPU, GPU et NPU Intel ou Broadcom, mais marque le Raspberry Pi « coming soon », alors qu'un billet de blog du 2026-08-11 l'utilise avec un Pi 5 : contradiction non tranchée. Les instructions de compilation ne couvrent que les hôtes Linux, macOS, Windows et Android, pas la compilation croisée vers ARM embarqué.
- **Pas d'ONNX direct.** `onnx2tf` (MIT, communautaire, 2.6.9 du 2026-09-14) existe, mais son README recommande déjà `litert-torch`. L'export `litert` d'Ultralytics refuse tout hôte hors Linux x86 et macOS, d'après son code.
- **Edge TPU : à ne pas planifier.** Le dépôt `pycoral` est archivé ; la compatibilité d'`ai-edge-litert` avec le délégué Edge TPU n'a pas pu être établie.
- **NNAPI** concerne Android, pas l'atelier ; le README déconseille d'ailleurs les délégués manuels pour du code neuf.
- **Jeu d'opérateurs.** Trois niveaux : opérateurs natifs, opérateurs TensorFlow sélectionnés (runtime plus gros), opérateurs sur mesure. Un modèle qui en sort demande du travail.
- **Quantification** : `ai-edge-quantizer` est en alpha (0.9.0). Les ratios de taille et d'accélération de la doc de Google ne sont pas repris ici : chiffres d'éditeur, non datés.

## Écosystème

### Alternatives

- [[ONNX Runtime]] — Moteur d'inférence cross-plateforme de Microsoft pour modèles au format ONNX — un même modèle exporté tourne sur CPU, GPU et accélérateurs variés via des Execution Providers (CUDA, TensorRT, OpenVINO, DirectML…), du serveur à l'edge. — le format pivot ONNX et un seul runtime pour tous les matériels, là où LiteRT exige de convertir en `.tflite`.

### Compléments

- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0. — exporte vers `litert`, `openvino`, `onnx` et d'autres formats selon son `exporter.py`.

## Ressources

- Documentation — https://ai.google.dev/edge/litert
- Dépôt — https://github.com/google-ai-edge/LiteRT

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Inférence en bordure - modèles sur du matériel d'atelier]] — la notion : pourquoi et comment inférer sur place
- [[Comparatif - Runtimes d'inférence CPU et edge]] — ce qui départage les runtimes pour CPU et matériel d'atelier
- [[TensorFlow]], [[PyTorch]] — les frameworks dont on convertit les modèles
