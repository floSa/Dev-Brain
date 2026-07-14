---
galaxie: dev
type: service
nom: torchvision
alias: [torch vision, tv, torchvision.transforms]
pitch: "Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python/C++
scaling: single-node
alternatives: ["[[Dev/Services/timm|timm]]", "[[Dev/Services/albumentations|albumentations]]", "[[Dev/Services/Kornia|Kornia]]"]
remplace_par: []
status: actif
tags: [computer-vision, cnn, transfer-learning, data-augmentation, deep-learning, gpu]
url_docs: https://docs.pytorch.org/vision/
url_repo: https://github.com/pytorch/vision
---

# torchvision

## Pourquoi

Paquet vision **officiel** de l'écosystème [[Dev/Services/PyTorch|PyTorch]], maintenu par la même équipe. Trois briques : **datasets** (téléchargement et préparation de jeux publics), **models** (architectures et poids pré-entraînés — ResNet, EfficientNet, ConvNeXt, ViT, Faster R-CNN, Mask R-CNN…) et **transforms** (prétraitement et augmentation). La génération `transforms.v2` opère sur des tenseurs (GPU possible), gère boîtes et masques, et remplace l'ancienne API `transforms`. C'est l'outillage par défaut pour le [[Transfer learning vision|transfert d'apprentissage]] et le chargement d'images en PyTorch.

## Quand l'utiliser

- Charger un **backbone pré-entraîné** ImageNet (CNN ou ViT) pour faire du [[Transfer learning vision|transfert]] sans dépendance supplémentaire.
- Pipelines d'**[[Augmentation d'images|augmentation]]** standard (flip, crop, RandAugment, Mixup/CutMix) via `transforms.v2`.
- Tâches clés en main : [[Classification d'images|classification]], [[Détection d'objets|détection]] et [[Segmentation|segmentation]] (Faster/Mask R-CNN, RetinaNet, DeepLab).
- Décodage d'images/vidéos et `datasets` pour prototyper vite.

## Quand NE PAS l'utiliser

- Catalogue de backbones beaucoup plus large et poids SOTA → [[Dev/Services/timm|timm]].
- Augmentation CPU plus rapide et plus riche (détection/segmentation) → [[Dev/Services/albumentations|albumentations]].
- Augmentations **différentiables** sur GPU dans le graphe d'autograd → [[Dev/Services/Kornia|Kornia]].
- Vision **classique** hors deep learning (calibration, features, vidéo) → [[Dev/Services/OpenCV|OpenCV]].

## Déploiement & coût

- Bibliothèque open-source (BSD-3-Clause), gratuite ; `uv add torchvision`. Rien à héberger.
- Versionnée **en lockstep avec PyTorch** (une version de torchvision par version de torch) ; opérations C++/CUDA pour le décodage et certains modèles.
- S'exécute là où tourne PyTorch (CPU, GPU NVIDIA/ROCm, MPS) ; la mise à l'échelle distribuée est déléguée à PyTorch.

## Pièges

- **Poids ≠ BSD** : certains poids pré-entraînés ont leur propre licence (ex. SWAG en CC-BY-NC 4.0, non commercial) — vérifier avant usage en prod.
- Couples de versions stricts torch ↔ torchvision : une mauvaise paire casse l'import.
- Migrer vers `transforms.v2` : l'ancienne API `transforms` (v1) ne gère pas nativement boîtes/masques.

## Alternatives

- [[Dev/Services/timm|timm]] — La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision.
- [[Dev/Services/albumentations|albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- [[Dev/Services/Kornia|Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — le framework dont torchvision est l'extension vision officielle.
- [[Vision par ordinateur]] — le cadre et les tâches servies.
- [[CNN]] / [[Architectures CNN]] — les backbones convolutifs exposés par `models`.
- [[Transfer learning vision]] / [[Augmentation d'images]] — les deux usages cœur.
- Doc : https://docs.pytorch.org/vision/
