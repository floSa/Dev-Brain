---
role: brique
nom: Detectron2
alias: [detectron2, detectron, Mask R-CNN, FAIR detection]
pitch: "Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python/C++
alternatives: ["[[Ultralytics YOLO]]", "[[segment-anything]]"]
complements: ["[[supervision]]"]
tags: [object-detection, segmentation, computer-vision, deep-learning, gpu]
url_docs: https://detectron2.readthedocs.io/
url_repo: https://github.com/facebookresearch/detectron2
---

# Detectron2

<!-- AUTO:BANDEAU:START -->
> Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python/C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de détection et segmentation de Meta AI (FAIR), successeure de Detectron, réécrite
sur PyTorch. Elle fournit les **implémentations de référence** des grands modèles — Faster
R-CNN, Mask R-CNN, RetinaNet, Cascade R-CNN, panoptique via Panoptic FPN, DensePose — avec un
**model zoo** de poids pré-entraînés. Son architecture est **modulaire** : backbones, RPN et
ROI heads sont interchangeables via des registres et des configs LazyConfig, et une brique se
remplace sans réécrire le pipeline. Elle embarque des ops C++/CUDA custom, ce qui la lie
étroitement à la paire torch ↔ CUDA installée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Reproduire ou étendre des modèles de référence : détection deux étages, segmentation d'instance et panoptique | Installation fragile : versions torch/CUDA strictes, ops CUDA à compiler, support Windows natif limité (WSL recommandé) |
| Customiser l'architecture — backbone, tête, loss — proprement, par configs et registres | Rythme de développement ralenti : projet stable, peu d'évolutions récentes ; pour du SOTA actif, regarder MMDetection ou les transformeurs de détection |
| Priorité à la précision plutôt qu'à la latence temps réel | Courbe d'apprentissage du système de config — YAML hérité, puis LazyConfig — plus raide que l'API YOLO |
| Benchmarks reproductibles sur COCO, LVIS et Cityscapes via le model zoo | Tâches de détection ou de segmentation standard sans dépendance lourde → [[torchvision]] |

## Mise en œuvre

- Installation — depuis les sources ou une wheel, avec compilation des ops C++/CUDA selon la paire torch ↔ CUDA
- Point d'entrée — une config (YAML hérité ou LazyConfig), puis `DefaultTrainer` et `DefaultPredictor` en Python
- Prérequis — PyTorch et une version de CUDA compatible ; WSL recommandé sous Windows
- Exécution — là où tourne PyTorch, surtout GPU NVIDIA ; entraînement single-node multi-GPU, mise à l'échelle déléguée à PyTorch
- Coût — Apache-2.0, gratuit et utilisable en produit fermé ; rien à héberger

## Écosystème

### Alternatives

- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0.
- [[segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte).

### Compléments

- [[supervision]] — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application. — l'outillage qui exploite ses sorties en aval

## Ressources

- Documentation — https://detectron2.readthedocs.io/
- Dépôt — https://github.com/facebookresearch/detectron2

## Voir aussi

- [[Détection d'objets]] — la tâche : deux étages, Faster R-CNN, mAP
- [[Segmentation]] — segmentation d'instance et panoptique, via Mask R-CNN
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
- [[PyTorch]] — le framework sous-jacent
- [[HuggingFace]] — où vivent les écosystèmes transformeurs de détection (DETR)
