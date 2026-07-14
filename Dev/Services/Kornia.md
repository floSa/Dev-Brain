---
galaxie: dev
type: service
nom: Kornia
alias: [kornia, kornia.augmentation]
pitch: "Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/albumentations|albumentations]]", "[[Dev/Services/torchvision|torchvision]]", "[[Dev/Services/OpenCV|OpenCV]]"]
remplace_par: []
status: actif
tags: [computer-vision, data-augmentation, deep-learning, gpu, autograd]
url_docs: https://kornia.readthedocs.io/
url_repo: https://github.com/kornia/kornia
---

# Kornia

## Pourquoi

Bibliothèque de **vision par ordinateur différentiable** bâtie sur [[Dev/Services/PyTorch|PyTorch]] : elle réimplémente les opérations classiques de [[Dev/Services/OpenCV|OpenCV]] (filtres, transformations géométriques, espaces colorimétriques, détection de features, épipolaire) en **opérateurs tensoriels différentiables**. Conséquence : tout s'exécute par **batch sur GPU**, traverse l'**autograd** (gradients qui remontent à travers les transformations) et s'insère directement dans un modèle. Son module `kornia.augmentation` fait de l'[[Augmentation d'images|augmentation]] sur GPU, et les briques géométriques servent la Spatial AI (homographies, profondeur, pose) apprenables de bout en bout.

## Quand l'utiliser

- Faire l'**augmentation sur GPU** (et non CPU) pour décharger le `DataLoader` quand l'I/O est le goulot.
- Avoir besoin d'opérations CV **dans le graphe** : STN, photometric/geometric loss, transformations apprenables, self-supervised.
- Vision **géométrique différentiable** : homographie, épipolaire, profondeur, calibration intégrées à l'entraînement.

## Quand NE PAS l'utiliser

- Augmentation **CPU** la plus rapide, avec boîtes/masques → [[Dev/Services/albumentations|albumentations]].
- Transformations standard sans besoin de différentiabilité → `transforms.v2` de [[Dev/Services/torchvision|torchvision]].
- Vision classique **hors PyTorch** / temps réel CPU → [[Dev/Services/OpenCV|OpenCV]].

## Déploiement & coût

- Open-source **Apache-2.0**, gratuit ; `uv add kornia`. Pur Python au-dessus de PyTorch.
- S'exécute sur CPU/GPU (différentiable, vectorisé par batch) ; mise à l'échelle déléguée à PyTorch, single-node.
- Aucune infra à héberger.

## Pièges

- Tout est **tenseur PyTorch** (BCHW, float normalisé) : penser la conversion en amont/aval, pas de NumPy/PIL au milieu.
- Le gain GPU n'est réel que si l'augmentation est le goulot **et** le batch assez gros ; sinon albumentations sur CPU suffit.
- Couverture de transformations un peu moindre qu'albumentations sur certains cas détection/segmentation.

## Alternatives

- [[Dev/Services/albumentations|albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- [[Dev/Services/torchvision|torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- [[Dev/Services/OpenCV|OpenCV]] — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — le socle tensoriel et l'autograd dont Kornia hérite.
- [[Augmentation d'images]] — l'augmentation, ici différentiable et sur GPU.
- [[Vision par ordinateur]] — le cadre ; [[CNN]] — les modèles dans lesquels Kornia s'insère.
- [[Dev/Services/OpenCV|OpenCV]] — l'équivalent classique, non différentiable.
- Doc : https://kornia.readthedocs.io/
