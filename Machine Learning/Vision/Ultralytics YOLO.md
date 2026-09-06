---
role: brique
nom: Ultralytics YOLO
alias: [YOLO, ultralytics, YOLOv8, YOLO11, YOLO26]
pitch: "Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0."
categorie: ml/vision
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Detectron2]]"]
complements: ["[[supervision]]"]
tags: [object-detection, segmentation, pose-estimation, object-tracking, computer-vision, deep-learning, gpu]
url_docs: https://docs.ultralytics.com/
url_repo: https://github.com/ultralytics/ultralytics
---

# Ultralytics YOLO

<!-- AUTO:BANDEAU:START -->
> Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation et maintenance de la famille **YOLO** — *You Only Look Once*, des détecteurs
**un étage temps réel** — par Ultralytics. Une seule API, `from ultralytics import YOLO`,
couvre détection, segmentation d'instance, pose, classification et suivi ; entraînement,
validation, export (ONNX, TensorRT, CoreML) et inférence tiennent en quelques lignes. Lignée
récente : YOLOv8, puis YOLO11 en septembre 2024, puis YOLO26, cette dernière supprimant la NMS
pour une inférence end-to-end optimisée pour l'edge. C'est le défaut pragmatique quand on veut
un détecteur qui marche vite, sans assembler soi-même backbone, têtes et post-traitement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un détecteur temps réel entraîné sur boîtes custom, prêt en quelques heures | Projet commercial fermé : l'AGPL-3.0 peut obliger à publier le code appelant d'un service distribué — prévoir la licence Enterprise |
| Une seule bibliothèque pour détection, segmentation, pose et suivi, sans changer d'API | Les poids COCO couvrent 80 classes génériques : un domaine spécifique exige du fine-tuning sur données annotées |
| Déploiement edge ou embarqué : export TensorRT/ONNX, variantes nano à extra-large | Numérotation mouvante — v5, v8, 11, 26, plus les forks v7, v9 et v10 hors Ultralytics : épingler la version dans le lockfile |
| Prototypage rapide et fine-tuning depuis des poids COCO pré-entraînés | L'API clé en main masque les hyperparamètres ; sur cas difficile, descendre dans la config reste nécessaire |
| | Briques de détection et de segmentation dans l'écosystème PyTorch officiel, sans contrainte de licence → [[torchvision]] |

## Mise en œuvre

- Installation — `uv add ultralytics`
- Point d'entrée — la classe `YOLO` en Python, ou la CLI `yolo` ; export vers ONNX, TensorRT et CoreML
- Prérequis — PyTorch ; des données annotées en boîtes dès que le domaine sort des 80 classes COCO
- Exécution — là où tourne PyTorch (CPU, GPU NVIDIA, MPS), single-node ; export vers un runtime optimisé pour la production
- Coût — AGPL-3.0, copyleft fort : gratuite en recherche, en open source et en usage interne, mais redistribuer un produit qui l'intègre impose d'en publier le code source. Licence Enterprise payante pour l'usage propriétaire

## Écosystème

### Alternatives

- [[Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.

### Compléments

- [[supervision]] — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application. — l'outillage qui annote et suit ses sorties en aval

## Ressources

- Documentation — https://docs.ultralytics.com/
- Dépôt — https://github.com/ultralytics/ultralytics
- Documentation — https://www.ultralytics.com/license — les termes AGPL-3.0 et l'offre Enterprise

## Voir aussi

- [[Détection d'objets]] — la tâche cœur : un étage, anchors, NMS, mAP
- [[Segmentation]], [[Estimation de pose]], [[Suivi d'objets]] — les autres tâches couvertes par la même API
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
- [[PyTorch]] — le framework sous-jacent
