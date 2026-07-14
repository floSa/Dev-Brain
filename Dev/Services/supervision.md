---
galaxie: dev
type: service
nom: supervision
alias: [roboflow supervision, sv]
pitch: "Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [object-detection, object-tracking, computer-vision]
url_docs: https://supervision.roboflow.com/
url_repo: https://github.com/roboflow/supervision
---

# supervision

## Pourquoi

Bibliothèque **model-agnostic** de Roboflow qui fournit l'**outillage autour** des modèles de vision, pas les modèles eux-mêmes. Pivot : une API **`Detections`** unifiée avec des connecteurs pour les sorties de [[Dev/Services/Ultralytics YOLO|Ultralytics]], [[Dev/Services/Detectron2|Detectron2]], [[Dev/Services/segment-anything|SAM]], [[Dev/Services/HuggingFace|Transformers]], Roboflow Inference… Au-dessus : **annotateurs** (boîtes, masques, labels, traces), **suivi** ([[Suivi d'objets|ByteTrack]]), **zones** (polygones, lignes) pour le comptage et le franchissement, conversion de **datasets** (COCO/YOLO/Pascal VOC) et métriques (mAP, matrice de confusion). C'est la **colle** entre un détecteur et une application livrable.

## Quand l'utiliser

- **Visualiser** proprement des détections / masques / poses sur images et vidéos.
- **Suivre** et **compter** des objets (zones, lignes de franchissement, [[Suivi d'objets|tracking]]) sans réécrire la plomberie.
- Rester **indépendant du modèle** : changer de détecteur sans toucher le code aval.
- Manipuler et **convertir des datasets** entre formats d'annotation, évaluer un modèle (mAP).

## Quand NE PAS l'utiliser

- Besoin du **modèle** de détection/segmentation lui-même → [[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]], [[Dev/Services/Detectron2|Detectron2]], [[Dev/Services/segment-anything|segment-anything]].
- Vision **classique** bas niveau (filtres, calibration, features) → [[Dev/Services/OpenCV|OpenCV]].
- Augmentation d'images pour l'entraînement → [[Dev/Services/albumentations|albumentations]].

## Déploiement & coût

- Bibliothèque Python open-source sous **MIT** (permissive), gratuite ; `uv add supervision`. Rien à héberger.
- N'embarque **aucun modèle ni poids** : se branche sur les sorties d'un modèle exécuté ailleurs ; dépendances légères (NumPy, OpenCV).
- S'exécute partout où tourne Python ; traitement single-node, temps réel sur flux vidéo selon le détecteur en amont.

## Pièges

- **Ne fait pas d'inférence** : il faut un modèle qui produit les détections en amont — supervision ne fait que les exploiter.
- API en évolution rapide (< 1.0) : épingler la version, surveiller les changements de signature entre releases.
- Les connecteurs supposent un **format de sortie attendu** par modèle ; un format inhabituel demande une conversion manuelle vers `Detections`.

## Liens

- [[Détection d'objets]] / [[Segmentation]] / [[Suivi d'objets]] — les tâches dont supervision exploite les sorties.
- [[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]] / [[Dev/Services/Detectron2|Detectron2]] / [[Dev/Services/segment-anything|segment-anything]] — les modèles en amont.
- [[Dev/Services/OpenCV|OpenCV]] — la couche bas niveau sur laquelle supervision s'appuie pour le rendu.
- [[Vision par ordinateur]] — le cadre d'ensemble.
- Doc : https://supervision.roboflow.com/
