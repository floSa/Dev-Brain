---
role: brique
nom: Kornia
alias: [kornia, kornia.augmentation]
pitch: "Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[albumentations]]", "[[torchvision]]", "[[OpenCV]]"]
complements: []
tags: [computer-vision, data-augmentation, deep-learning, gpu, autograd]
url_docs: https://kornia.readthedocs.io/
url_repo: https://github.com/kornia/kornia
---

# Kornia

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de vision par ordinateur **différentiable** bâtie sur PyTorch. Elle réimplémente
les opérations classiques d'OpenCV — filtres, transformations géométriques, espaces
colorimétriques, détection de features, géométrie épipolaire — en **opérateurs tensoriels
différentiables**. Conséquence : tout s'exécute par batch sur GPU, traverse l'**autograd**,
les gradients remontant à travers les transformations, et s'insère directement dans un modèle.
Le module `kornia.augmentation` fait l'augmentation sur GPU, et les briques géométriques
servent la Spatial AI apprenable de bout en bout. Le prix est l'uniformité du format : tout
est tenseur BCHW en float normalisé, sans NumPy ni PIL au milieu.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire l'augmentation sur GPU pour décharger le `DataLoader` quand l'I/O est le goulot | Le gain GPU n'est réel que si l'augmentation est bien le goulot **et** que le batch est assez gros |
| Opérations de vision **dans le graphe** : STN, perte photométrique ou géométrique, transformations apprenables, auto-supervision | Augmentation CPU la plus rapide, avec boîtes et masques → [[albumentations]] |
| Vision géométrique différentiable — homographie, épipolaire, profondeur, calibration — intégrée à l'entraînement | Transformations standard sans besoin de différentiabilité → `transforms.v2` de [[torchvision]] |
| | Vision classique hors PyTorch, ou temps réel CPU → [[OpenCV]] |

## Mise en œuvre

- Installation — `uv add kornia`
- Point d'entrée — des `nn.Module` posés dans le graphe PyTorch, dont le module `kornia.augmentation`
- Prérequis — PyTorch, et des tenseurs BCHW en float normalisé de bout en bout
- Exécution — CPU ou GPU, vectorisé par batch ; single-node, mise à l'échelle déléguée à PyTorch
- Coût — Apache-2.0, gratuit ; rien à héberger

## Écosystème

### Alternatives

- [[albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- [[torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- [[OpenCV]] — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning.

## Ressources

- Documentation — https://kornia.readthedocs.io/
- Dépôt — https://github.com/kornia/kornia

## Voir aussi

- [[Augmentation d'images]] — l'augmentation, ici différentiable et sur GPU
- [[Vision par ordinateur]] — le cadre
- [[Vision]] — le hub du dossier ; Kornia n'entre pas dans la vue du comparatif, filtrée sur détection et segmentation
- [[PyTorch]] — le socle tensoriel et l'autograd dont Kornia hérite
- [[CNN]] — les modèles dans lesquels Kornia s'insère
