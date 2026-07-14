---
galaxie: dev
type: service
nom: Ultralytics YOLO
alias: [YOLO, ultralytics, YOLOv8, YOLO11, YOLO26]
pitch: "Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Detectron2|Detectron2]]"]
remplace_par: []
status: actif
tags: [object-detection, segmentation, pose-estimation, object-tracking, computer-vision, deep-learning, gpu]
url_docs: https://docs.ultralytics.com/
url_repo: https://github.com/ultralytics/ultralytics
---

# Ultralytics YOLO

## Pourquoi

Implémentation et maintenance de la famille **YOLO** (You Only Look Once) — des détecteurs **un étage temps réel** — par Ultralytics. Une seule API (`from ultralytics import YOLO`) couvre [[Détection d'objets|détection]], [[Segmentation|segmentation d'instance]], [[Estimation de pose|pose]], classification et [[Suivi d'objets|suivi]] ; entraînement, validation, export (ONNX, TensorRT, CoreML) et inférence tiennent en quelques lignes. Lignée récente : **YOLOv8** → **YOLO11** (sept. 2024) → **YOLO26**, cette dernière supprimant la [[Détection d'objets|NMS]] pour une inférence **end-to-end** optimisée edge. C'est le défaut pragmatique quand on veut un détecteur qui marche vite, sans assembler soi-même backbone, têtes et post-traitement.

## Quand l'utiliser

- Besoin d'un **détecteur temps réel** entraîné sur boîtes custom, prêt en quelques heures.
- Une seule lib pour détection **+** segmentation **+** pose **+** suivi, sans changer d'API.
- Déploiement **edge / embarqué** : export TensorRT/ONNX, variantes nano à extra-large.
- Prototypage rapide et fine-tuning à partir de poids COCO pré-entraînés.

## Quand NE PAS l'utiliser

- Architecture de détection **modulaire et customisable** (têtes, RPN, panoptique) pour la recherche → [[Dev/Services/Detectron2|Detectron2]].
- Briques de détection/segmentation **dans** l'écosystème PyTorch officiel sans contrainte de licence → [[Dev/Services/torchvision|torchvision]] (Faster/Mask R-CNN, RetinaNet).
- Segmentation **promptable zero-shot** sans entraîner de classes → [[Dev/Services/segment-anything|segment-anything]].
- Projet **commercial fermé** réticent à l'AGPL-3.0 → prévoir la licence Enterprise (voir ci-dessous) ou une alternative permissive.

## Déploiement & coût

- Bibliothèque Python open-source sous **AGPL-3.0** (copyleft fort) ; `uv add ultralytics`. Rien à héberger.
- **Licence à double régime** : AGPL-3.0 gratuite (recherche, open source, usage interne), mais redistribuer un produit qui l'intègre impose d'en publier le code source ; pour un usage propriétaire/fermé, Ultralytics vend une **licence Enterprise** payante.
- S'exécute là où tourne PyTorch (CPU, GPU NVIDIA, MPS) ; mise à l'échelle single-node, export vers runtimes optimisés pour la prod.

## Pièges

- **Piège licence AGPL-3.0** : intégrer YOLO dans un service distribué peut obliger à ouvrir tout le code appelant — vérifier avant la prod.
- Les **poids COCO** sont entraînés sur 80 classes génériques ; un domaine spécifique exige du fine-tuning sur données annotées.
- Numérotation marketing mouvante (v5, v8, 11, 26, plus les forks YOLOv7/v9/v10 hors Ultralytics) : épingler la version dans le lockfile.
- L'API « clé en main » masque les hyperparamètres ; sur cas difficiles, descendre dans la config reste nécessaire.

## Alternatives

- [[Dev/Services/Detectron2|Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.

## Liens

- [[Détection d'objets]] — la tâche cœur (un étage, anchors, NMS, mAP).
- [[Segmentation]] / [[Estimation de pose]] / [[Suivi d'objets]] — les autres tâches couvertes par la même API.
- [[Dev/Services/supervision|supervision]] — outillage model-agnostic pour annoter et suivre les sorties YOLO.
- [[Dev/Services/PyTorch|PyTorch]] — le framework sous-jacent.
- Doc : https://docs.ultralytics.com/ · Licence : https://www.ultralytics.com/license
