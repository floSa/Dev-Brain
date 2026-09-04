---
role: brique
nom: timm
alias: [pytorch-image-models, PyTorch Image Models, torch image models]
pitch: "La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[torchvision]]"]
complements: []
tags: [computer-vision, cnn, vit, transfer-learning, fine-tuning, deep-learning, model-hub]
url_docs: https://huggingface.co/docs/timm/
url_repo: https://github.com/huggingface/pytorch-image-models
---

# timm

<!-- AUTO:BANDEAU:START -->
> La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

**PyTorch Image Models** : la plus vaste collection de backbones vision pour PyTorch — plus de
mille architectures et variantes (ResNet, ResNeXt, EfficientNet, RegNet, ConvNeXt, MobileNet,
ViT, Swin, MaxViT), leurs poids pré-entraînés, plus des optimiseurs, schedulers, augmentations
et scripts d'entraînement et d'évaluation de référence. Une API unique —
`timm.create_model(name, pretrained=True, num_classes=...)` — sert n'importe lequel, et
`features_only=True` en extrait les cartes de features pour brancher un détecteur ou un
segmenteur. L'espace de noms est touffu : les suffixes (`.a1_in1k`, `.augreg`,
`.fb_in22k_ft_in1k`) encodent la recette et le pré-entraînement, et se lisent.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Récupérer en une ligne un backbone pré-entraîné que torchvision n'a pas encore | Les conventions de prétraitement varient par modèle : sans `model.pretrained_cfg` ou `resolve_data_config`, la précision baisse en silence |
| Fine-tuner, ou extraire des features (`features_only=True`) pour un pipeline détection ou segmentation | Certains poids héritent d'une licence non commerciale du jeu d'origine : à vérifier au cas par cas |
| Comparer des dizaines d'architectures à budget donné, benchmarks du dépôt à l'appui | Besoin limité aux modèles classiques, aux datasets et aux tâches clés en main → [[torchvision]] |
| Réutiliser des recettes d'entraînement éprouvées : RandAugment, Mixup/CutMix, EMA | Modèles multimodaux ou hors vision pure — CLIP, détecteurs end-to-end packagés → `transformers` de [[HuggingFace]] |

## Mise en œuvre

- Installation — `uv add timm`
- Point d'entrée — `timm.create_model(...)`, complété par `resolve_data_config` pour le prétraitement du poids choisi
- Prérequis — PyTorch ; les poids se téléchargent depuis le Hub Hugging Face
- Exécution — CPU ou GPU, single-node ; distribution déléguée à PyTorch
- Coût — Apache-2.0 pour la bibliothèque ; certains poids portent leur propre licence, parfois non commerciale

## Écosystème

### Alternatives

- [[torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.

## Ressources

- Documentation — https://huggingface.co/docs/timm/
- Dépôt — https://github.com/huggingface/pytorch-image-models

## Voir aussi

- [[Transfer learning vision]] — l'usage cœur : partir d'un backbone pré-entraîné
- [[Architectures CNN]], [[CNN]], [[Vision Transformers (ViT)]] — les familles d'ossatures fournies
- [[Classification d'images]] — la tâche directe
- [[Vision]] — le hub du dossier ; timm n'entre pas dans la vue du comparatif, filtrée sur détection et segmentation
- [[PyTorch]] — le framework sous-jacent ; [[HuggingFace]] — l'organisation mainteneuse et le Hub des poids
