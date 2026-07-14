---
galaxie: dev
type: service
nom: Detectron2
alias: [detectron2, detectron, Mask R-CNN, FAIR detection]
pitch: "Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python/C++
scaling: single-node
alternatives: ["[[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]]", "[[Dev/Services/segment-anything|segment-anything]]"]
remplace_par: []
status: actif
tags: [object-detection, segmentation, computer-vision, deep-learning, gpu]
url_docs: https://detectron2.readthedocs.io/
url_repo: https://github.com/facebookresearch/detectron2
---

# Detectron2

## Pourquoi

Plateforme de **détection et segmentation** de Meta AI (FAIR), successeure de Detectron, réécrite sur [[Dev/Services/PyTorch|PyTorch]]. Fournit les **implémentations de référence** des grands modèles — Faster R-CNN, Mask R-CNN, RetinaNet, Cascade R-CNN, panoptique (Panoptic FPN), DensePose — avec un **model zoo** de poids pré-entraînés. Architecture **modulaire** (backbones, RPN, ROI heads interchangeables, registres et configs LazyConfig) : on remplace une brique sans réécrire le pipeline. C'est l'outil de la recherche et des projets qui veulent customiser l'architecture, là où [[Dev/Services/Ultralytics YOLO|YOLO]] privilégie le temps réel clé en main.

## Quand l'utiliser

- Reproduire ou étendre des modèles de **référence** ([[Détection d'objets|détection]] deux étages, [[Segmentation|segmentation d'instance / panoptique]]).
- Besoin de **customiser l'architecture** (nouveau backbone, tête, loss) proprement via configs et registres.
- Priorité à la **précision** plutôt qu'à la latence temps réel.
- Benchmarks reproductibles sur COCO, LVIS, Cityscapes via le model zoo.

## Quand NE PAS l'utiliser

- Détecteur **temps réel** clé en main (edge, export, suivi intégré) → [[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]].
- Tâches de détection/segmentation **standard** sans dépendance lourde → [[Dev/Services/torchvision|torchvision]].
- Segmentation **promptable zero-shot** sans annoter de classes → [[Dev/Services/segment-anything|segment-anything]].
- Environnement où la **compilation des ops CUDA** custom est problématique (Windows natif, GPU exotique) : l'installation peut être pénible.

## Déploiement & coût

- Bibliothèque open-source sous **Apache-2.0** (permissive, utilisable en prod fermée), gratuite. Rien à héberger.
- Installée depuis les sources / wheels ; embarque des **ops C++/CUDA** custom → l'installation dépend de la paire torch ↔ CUDA et compile parfois localement.
- S'exécute là où tourne PyTorch (surtout GPU NVIDIA) ; entraînement single-node multi-GPU, mise à l'échelle déléguée à PyTorch.

## Pièges

- **Installation fragile** : versions torch/CUDA strictes, compilation des ops ; le support **Windows** natif est limité (WSL recommandé).
- **Rythme de développement ralenti** : projet stable mais peu d'évolutions récentes ; pour du SOTA actif, regarder MMDetection ou les écosystèmes transformeurs (DETR via [[Dev/Services/HuggingFace|HuggingFace]]).
- Courbe d'apprentissage du système de **config** (YAML hérité puis LazyConfig) plus raide que l'API YOLO.

## Alternatives

- [[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0.
- [[Dev/Services/segment-anything|segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte).

## Liens

- [[Détection d'objets]] — la tâche (deux étages, Faster R-CNN, mAP).
- [[Segmentation]] — segmentation d'instance et panoptique (Mask R-CNN).
- [[Dev/Services/supervision|supervision]] — outillage model-agnostic pour exploiter les sorties Detectron2.
- [[Dev/Services/PyTorch|PyTorch]] — le framework sous-jacent.
- Doc : https://detectron2.readthedocs.io/
