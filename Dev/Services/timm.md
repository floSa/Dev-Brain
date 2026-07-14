---
galaxie: dev
type: service
nom: timm
alias: [pytorch-image-models, PyTorch Image Models, torch image models]
pitch: "La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/torchvision|torchvision]]"]
remplace_par: []
status: actif
tags: [computer-vision, cnn, vit, transfer-learning, fine-tuning, deep-learning, model-hub]
url_docs: https://huggingface.co/docs/timm/
url_repo: https://github.com/huggingface/pytorch-image-models
---

# timm

## Pourquoi

**PyTorch Image Models** : la plus vaste collection de backbones vision pour [[Dev/Services/PyTorch|PyTorch]] (1000+ architectures et variantes — ResNet/ResNeXt, EfficientNet, RegNet, ConvNeXt, MobileNet, [[Vision Transformers (ViT)|ViT]], Swin, MaxViT…), avec leurs **poids pré-entraînés**, des optimiseurs, schedulers, augmentations et des scripts d'entraînement/éval de référence. Une API unique — `timm.create_model(name, pretrained=True, num_classes=...)` — sert n'importe quel modèle, avec extraction de features (`features_only`) pour brancher un détecteur ou un segmenteur. C'est l'outil de référence pour le [[Transfer learning vision|transfert d'apprentissage]].

## Quand l'utiliser

- Récupérer un **backbone SOTA pré-entraîné** que torchvision n'a pas encore, en une ligne.
- **Fine-tuner** ou faire de l'extraction de features (`features_only=True`) pour un pipeline détection/segmentation.
- Comparer rapidement des dizaines d'architectures à budget donné (benchmarks `results/` du repo).
- Réutiliser les recettes d'entraînement éprouvées (RandAugment, Mixup/CutMix, EMA…).

## Quand NE PAS l'utiliser

- Besoin limité aux modèles classiques + datasets + tâches clés en main → [[Dev/Services/torchvision|torchvision]] (officiel, moins de dépendances).
- Modèles **multimodaux** ou hors vision pure (CLIP, détecteurs end-to-end packagés) → [[Dev/Services/HuggingFace|HuggingFace]] `transformers`.
- Augmentation seule, sans modèles → [[Dev/Services/albumentations|albumentations]] / [[Dev/Services/Kornia|Kornia]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add timm`. Rien à héberger.
- Maintenue sous l'organisation **Hugging Face** (repo `huggingface/pytorch-image-models`, créateur Ross Wightman) ; poids distribués via le **Hub HF**.
- Pur Python au-dessus de PyTorch ; s'exécute sur CPU/GPU, distribution déléguée à PyTorch.

## Pièges

- **Conventions de prétraitement par modèle** : récupérer `model.pretrained_cfg` (ou `resolve_data_config`) pour la bonne normalisation/résolution — sinon perte de précision silencieuse.
- Espace de noms touffu : suffixes (`.a1_in1k`, `.augreg`, `.fb_in22k_ft_in1k`) encodant recette et pré-entraînement ; lire la fiche du poids.
- Certains poids héritent de licences non commerciales du jeu d'origine — vérifier au cas par cas.

## Alternatives

- [[Dev/Services/torchvision|torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — le framework sous-jacent ; [[Dev/Services/HuggingFace|HuggingFace]] — Hub qui héberge les poids et organisation mainteneuse.
- [[Transfer learning vision]] — l'usage cœur (backbones pré-entraînés).
- [[Architectures CNN]] / [[CNN]] / [[Vision Transformers (ViT)|ViT]] — les familles d'ossatures fournies.
- [[Classification d'images]] — la tâche directe ; [[Vision par ordinateur]] — le cadre.
- Doc : https://huggingface.co/docs/timm/
