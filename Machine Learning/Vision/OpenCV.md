---
role: brique
nom: OpenCV
alias: [opencv, cv2, opencv-python, Open Source Computer Vision Library]
pitch: "Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[Kornia]]"]
complements: ["[[albumentations]]", "[[supervision]]"]
tags: [computer-vision, object-detection, object-tracking]
url_docs: https://docs.opencv.org/
url_repo: https://github.com/opencv/opencv
---

# OpenCV

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque historique et la plus complète de vision par ordinateur **classique** : lecture,
écriture et transformation d'images et de vidéos, espaces colorimétriques, filtrage,
morphologie, contours, détection de features (ORB, SIFT) et appariement, **géométrie**
(homographies, calibration de caméra, stéréo, estimation de pose), flux optique et trackers.
Cœur C++ très optimisé — SIMD, CUDA en option — exposé en Python via `cv2`, ainsi qu'en Java
et JavaScript. Un module `dnn` exécute aussi des réseaux exportés (ONNX, Caffe). Une
convention historique à connaître : `cv2.imread` renvoie du **BGR**, pas du RGB, et les canaux
sont à convertir avant de passer à un modèle entraîné en RGB.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prétraitement et manipulation d'images ou de vidéos : redimensionnement, conversion, filtrage, ROI | Quatre paquets pip mutuellement exclusifs (`opencv-python`, `-contrib-`, `-headless`, `-contrib-headless`) : n'en installer qu'un, et `-headless` sur serveur |
| Vision géométrique : calibration, homographie, stéréo, estimation de pose, flux optique | L'accélération CUDA n'est pas dans les wheels : elle se compile depuis les sources |
| Détecteurs et trackers classiques — cascades de Haar, KCF, CSRT — quand un réseau est superflu | Entraîner ou fine-tuner un réseau de vision → [[PyTorch]], avec [[torchvision]] ou [[timm]] |
| Capture caméra et pipeline vidéo temps réel côté CPU | Opérations de vision **différentiables**, dans une boucle d'autograd sur GPU → [[Kornia]] |

## Mise en œuvre

- Installation — `uv add opencv-python`, ou l'un des trois autres paquets ; un seul des quatre à la fois
- Point d'entrée — le module Python `cv2` ; bindings Java et JavaScript par ailleurs
- Prérequis — Python et NumPy ; les images en BGR, à convertir en amont d'un modèle
- Exécution — bibliothèque locale, CPU ; rien à héberger
- Coût — Apache-2.0 depuis la 4.5 (les versions ≤ 4.4 étaient BSD-3-Clause), gratuit ; les wheels `opencv-python` sont maintenues séparément du dépôt cœur

## Écosystème

### Alternatives

- [[Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

### Compléments

- [[albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision. — bâtit son augmentation au-dessus d'OpenCV
- [[supervision]] — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application. — s'appuie sur OpenCV pour le rendu des annotations

## Ressources

- Documentation — https://docs.opencv.org/
- Dépôt — https://github.com/opencv/opencv

## Voir aussi

- [[Vision par ordinateur]] — le cadre dont OpenCV est la boîte à outils classique
- [[Suivi d'objets]] — les trackers classiques (KCF, CSRT) qu'il fournit
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
