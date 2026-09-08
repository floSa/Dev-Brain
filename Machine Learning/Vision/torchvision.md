---
role: brique
nom: torchvision
alias: [torch vision, tv, torchvision.transforms]
pitch: "Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python/C++
alternatives: ["[[timm]]", "[[albumentations]]", "[[Kornia]]"]
complements: []
tags: [computer-vision, cnn, transfer-learning, data-augmentation, deep-learning, gpu]
url_docs: https://docs.pytorch.org/vision/
url_repo: https://github.com/pytorch/vision
---

# torchvision

<!-- AUTO:BANDEAU:START -->
> Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python/C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Paquet vision **officiel** de l'écosystème PyTorch, maintenu par la même équipe. Trois
briques : `datasets` (téléchargement et préparation de jeux publics), `models` (architectures
et poids pré-entraînés — ResNet, EfficientNet, ConvNeXt, ViT, Faster R-CNN, Mask R-CNN,
RetinaNet, DeepLab) et `transforms` (prétraitement et augmentation). La génération
`transforms.v2` opère sur des tenseurs, GPU compris, gère nativement boîtes et masques, et
remplace l'ancienne API `transforms` qui ne les gérait pas. C'est l'outillage par défaut du
transfert d'apprentissage et du chargement d'images en PyTorch.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charger un backbone pré-entraîné ImageNet, CNN ou ViT, pour du transfert sans dépendance supplémentaire | Catalogue de backbones beaucoup plus large et poids SOTA → [[timm]] |
| Pipelines d'augmentation standard — flip, crop, RandAugment, Mixup/CutMix — via `transforms.v2` | Augmentation CPU plus rapide et plus riche pour la détection et la segmentation → [[albumentations]] |
| Tâches clés en main : classification, détection et segmentation (Faster/Mask R-CNN, RetinaNet, DeepLab) | Augmentations différentiables sur GPU, dans le graphe d'autograd → [[Kornia]] |
| Décodage d'images et de vidéos, et `datasets` publics pour prototyper vite | Vision classique hors deep learning — calibration, features, vidéo → [[OpenCV]] |

## Mise en œuvre

- Installation — `uv add torchvision`
- Point d'entrée — les trois modules `datasets`, `models` et `transforms.v2`
- Prérequis — PyTorch, en version appairée : une version de torchvision par version de torch, sinon l'import casse
- Exécution — là où tourne PyTorch (CPU, GPU NVIDIA ou ROCm, MPS) ; mise à l'échelle distribuée déléguée à PyTorch
- Coût — BSD-3-Clause pour la bibliothèque ; certains poids ont leur propre licence, dont SWAG en CC-BY-NC 4.0, non commerciale

## Écosystème

### Alternatives

- [[timm]] — La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision.
- [[albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- [[Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

## Ressources

- Documentation — https://docs.pytorch.org/vision/
- Dépôt — https://github.com/pytorch/vision

## Voir aussi

- [[Vision par ordinateur]] — le cadre et les tâches servies
- [[Transfer learning vision]], [[Augmentation d'images]] — les deux usages cœur
- [[Architectures CNN]], [[CNN]] — les backbones convolutifs exposés par `models`
- [[Vision]] — le hub du dossier ; torchvision n'entre pas dans la vue du comparatif, filtrée sur détection et segmentation
- [[PyTorch]] — le framework dont torchvision est l'extension vision officielle
