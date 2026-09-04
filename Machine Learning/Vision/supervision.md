---
role: brique
nom: supervision
alias: [roboflow supervision, sv]
pitch: "Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[Ultralytics YOLO]]", "[[Detectron2]]", "[[segment-anything]]", "[[OpenCV]]"]
tags: [object-detection, object-tracking, computer-vision]
url_docs: https://supervision.roboflow.com/
url_repo: https://github.com/roboflow/supervision
---

# supervision

<!-- AUTO:BANDEAU:START -->
> Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils **model-agnostic** de Roboflow, qui fournit l'outillage **autour** des modèles
de vision et non les modèles eux-mêmes. Son pivot est une API **`Detections`** unifiée, avec
des connecteurs pour les sorties d'Ultralytics, Detectron2, SAM, Transformers ou Roboflow
Inference. Au-dessus viennent les **annotateurs** (boîtes, masques, labels, traces), le
**suivi** par ByteTrack, les **zones** — polygones et lignes — pour le comptage et le
franchissement, la conversion de datasets (COCO, YOLO, Pascal VOC) et les métriques (mAP,
matrice de confusion). Elle ne fait aucune inférence : il lui faut un modèle en amont qui
produit les détections.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualiser proprement des détections, masques ou poses sur images et vidéos | API en évolution rapide, sous la 1.0 : épingler la version et surveiller les changements de signature entre releases |
| Suivre et compter des objets — zones, lignes de franchissement, tracking — sans réécrire la plomberie | Les connecteurs supposent un format de sortie attendu par modèle ; un format inhabituel demande une conversion manuelle vers `Detections` |
| Rester indépendant du modèle : changer de détecteur sans toucher au code aval | |
| Manipuler et convertir des datasets entre formats d'annotation, et évaluer un modèle (mAP) | |

## Mise en œuvre

- Installation — `uv add supervision`
- Point d'entrée — l'objet `Detections`, alimenté par un connecteur depuis la sortie du modèle
- Prérequis — NumPy et OpenCV ; surtout, un modèle exécuté ailleurs qui produit les détections
- Exécution — CPU, single-node ; temps réel sur flux vidéo selon le détecteur en amont
- Coût — MIT, gratuit ; aucun modèle ni poids embarqué, rien à héberger

## Écosystème

### Compléments

- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0. — un des modèles en amont dont il exploite les sorties
- [[Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture. — un des modèles en amont dont il exploite les sorties
- [[segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte). — le modèle dont il exploite les masques
- [[OpenCV]] — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning. — la couche bas niveau sur laquelle il s'appuie pour le rendu

## Ressources

- Documentation — https://supervision.roboflow.com/
- Dépôt — https://github.com/roboflow/supervision

## Voir aussi

- [[Détection d'objets]], [[Segmentation]], [[Suivi d'objets]] — les tâches dont il exploite les sorties
- [[Vision par ordinateur]] — le cadre d'ensemble
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
