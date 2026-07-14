---
galaxie: dev
type: service
nom: OpenCV
alias: [opencv, cv2, opencv-python, Open Source Computer Vision Library]
pitch: "Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/Kornia|Kornia]]"]
remplace_par: []
status: actif
tags: [computer-vision, object-detection, object-tracking]
url_docs: https://docs.opencv.org/
url_repo: https://github.com/opencv/opencv
---

# OpenCV

## Pourquoi

Bibliothèque historique et la plus complète de **vision par ordinateur classique** : lecture/écriture et transformation d'images et de vidéos, espaces colorimétriques, filtrage, morphologie, contours, détection de features (ORB, SIFT), appariement, **géométrie** (homographies, calibration de caméra, stéréo, pose), flux optique et trackers. Cœur **C++** très optimisé (SIMD, CUDA en option) exposé en Python via `cv2`, Java et JavaScript. Inclut aussi un module `dnn` qui exécute des réseaux exportés (ONNX, Caffe). C'est la brique de prétraitement et de CV géométrique sous des couches plus haut niveau (y compris l'I/O d'[[Dev/Services/albumentations|albumentations]]).

## Quand l'utiliser

- **Prétraitement** et manipulation d'images/vidéos : redimensionnement, conversion, filtrage, ROI.
- Vision **géométrique** : calibration, homographie, stéréo, estimation de pose, flux optique.
- Détecteurs et trackers **classiques** (cascades de Haar, KCF/CSRT) quand un réseau est superflu.
- Capture caméra / pipeline vidéo temps réel côté CPU.

## Quand NE PAS l'utiliser

- Entraîner ou fine-tuner un réseau de vision → [[Dev/Services/PyTorch|PyTorch]] + [[Dev/Services/torchvision|torchvision]] / [[Dev/Services/timm|timm]].
- Opérations de vision **différentiables** (dans une boucle d'autograd, sur GPU) → [[Dev/Services/Kornia|Kornia]].
- Pipeline d'**[[Augmentation d'images|augmentation]]** pour l'entraînement → [[Dev/Services/albumentations|albumentations]] (qui s'appuie justement sur OpenCV).

## Déploiement & coût

- Open-source, **Apache-2.0** depuis la 4.5 (OpenCV 5 confirme la bascule ; les versions ≤ 4.4 étaient BSD-3-Clause). Gratuit.
- Installation Python via les wheels `opencv-python` (et `opencv-contrib-python` pour les modules extra), maintenues séparément du dépôt cœur.
- Bibliothèque locale (CPU ; accélération CUDA optionnelle à compiler) ; pas d'infra à héberger.

## Pièges

- **BGR par défaut** (pas RGB) : `cv2.imread` renvoie du BGR — convertir avant de passer à un modèle entraîné en RGB, sinon canaux inversés.
- Quatre paquets pip mutuellement exclusifs (`opencv-python`, `-contrib-`, `-headless`, `-contrib-headless`) : en installer **un seul**, sinon conflits ; utiliser `-headless` sur serveur (pas de GUI).
- API impérative bas niveau, pas de batch/GPU/autograd : non adaptée à l'entraînement deep learning.

## Alternatives

- [[Dev/Services/Kornia|Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

## Liens

- [[Vision par ordinateur]] — le cadre ; OpenCV en est la boîte à outils classique.
- [[Dev/Services/albumentations|albumentations]] — bâtit son augmentation au-dessus d'OpenCV.
- [[Suivi d'objets]] — trackers classiques (KCF, CSRT) fournis.
- Doc : https://docs.opencv.org/
