---
role: comparatif
nom: Comparatif - Détection & segmentation
categorie: ml/vision
tags: [object-detection, segmentation, computer-vision]
---

# Comparatif - Détection & segmentation

> On tranche sur : l'étage de la chaîne vision — ce qui alimente le modèle, le modèle lui-même, ce qui exploite sa sortie — puis, entre modèles, temps réel clé en main, architecture modulaire ou segmentation sans classes.

![[Comparatif - Détection & segmentation.base]]

## Ce qui départage

- [[Ultralytics YOLO]] — détecteur **un étage temps réel** : une seule API couvre détection, segmentation, pose et suivi, et l'export TensorRT/ONNX vise l'edge. Le critère qui tranche n'est pas technique mais juridique — **AGPL-3.0**, qui peut obliger à ouvrir le code appelant d'un service distribué.
- [[Detectron2]] — les implémentations de **référence** (Faster/Mask R-CNN, RetinaNet, panoptique) dans une architecture modulaire : on remplace backbone, RPN ou tête sans réécrire le pipeline. Priorité à la précision, pas à la latence — et installation fragile, versions torch/CUDA strictes, Windows natif limité.
- [[segment-anything]] — segmentation **promptable zero-shot** : un point ou une boîte suffit, sans dataset annoté par classe. Mais il **ne classe pas** — il segmente et ne dit pas *quoi* ; le nommage vient d'un modèle en amont, et l'encodeur ViT est prohibitif hors gros GPU.
- [[supervision]] — **model-agnostic** : il ne fait aucune inférence, il exploite celle des autres. `Detections` unifie les sorties de YOLO, Detectron2 ou SAM, puis ajoute annotateurs, ByteTrack, zones et comptage — c'est la colle entre un détecteur et une application.
- [[albumentations]] — le seul du lot en **amont** de l'entraînement : 70+ transformations qui propagent **cohéremment** la transformation aux boîtes, masques et keypoints. CPU et NumPy (HWC) par construction : hors du graphe d'autograd, contrairement à Kornia.
- [[OpenCV]] — la vision **classique** sous les autres : filtrage, contours, features, géométrie (homographie, calibration, stéréo, flux optique), cœur C++ exposé en `cv2`. Ni batch, ni GPU, ni autograd — inadapté à l'entraînement, et il renvoie du **BGR**, pas du RGB.
