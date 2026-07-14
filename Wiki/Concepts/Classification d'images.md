---
galaxie: wiki
type: concept
nom: Classification d'images
alias: [image classification, classification d'image, top-1, top-5, ImageNet]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [image-classification, computer-vision, cnn, deep-learning]
---

# Classification d'images

## Aperçu

- Attribuer **une étiquette de classe à l'image entière** (chat/chien, type de défaut, espèce). La tâche fondatrice de la vision profonde.
- Brique de base : un **backbone** (CNN ou ViT) encode l'image en vecteur, puis une tête linéaire + softmax sur $K$ classes.

## Concepts clés

### Pipeline canonique
- Image → backbone pré-entraîné ([[Architectures CNN|ResNet, EfficientNet, ConvNeXt]] ou ViT) → pooling global → couche dense → softmax. Perte = [[Cross-entropy|entropie croisée]].

### Mono-label vs multi-label
- **Mono-label** : softmax, une seule classe par image. **Multi-label** : une sigmoïde par classe, plusieurs étiquettes simultanées. Change la dernière activation et la perte.

### Top-k accuracy
- En mono-label sur beaucoup de classes (ImageNet, 1000), on mesure **top-1** (la bonne classe en tête) et **top-5** (la bonne classe parmi les 5 premières) — top-5 amortit l'ambiguïté entre classes proches.

### Fine-grained & longue traîne
- Classification **fine** (races de chiens) : classes très proches, peu de signal discriminant. **Longue traîne** / déséquilibre des classes : cf. [[Imbalanced classification]].

## Les maths, simplement

- Softmax : $\hat p_c = \dfrac{e^{z_c}}{\sum_{k} e^{z_k}}$ ; perte $-\sum_c y_c \log \hat p_c$ (un seul $y_c = 1$ en mono-label).
- Multi-label : sigmoïde indépendante par classe $\sigma(z_c)$ + binary cross-entropy (chaque classe est un oui/non).

## En pratique

- Rarement de zéro : [[Transfer learning vision|transfert]] depuis ImageNet + [[Augmentation d'images|augmentation]] ; c'est le levier « petites données ».
- Évaluer avec top-1/top-5 et les [[Classification metrics|métriques de classification]] (F1 macro en déséquilibre) ; vérifier la [[Calibration]] des probabilités.
- Implémentation : torchvision / timm sur [[Dev/Services/PyTorch|PyTorch]], modèles pré-entraînés [[Dev/Services/HuggingFace|HuggingFace]].

## Approches voisines & alternatives

- [[Détection d'objets]] — plusieurs objets à localiser, pas une seule étiquette globale.
- [[Segmentation]] — étiquette au pixel plutôt qu'au niveau image.
- [[CNN]] / [[Architectures CNN]] — les backbones qui produisent la représentation.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Krizhevsky et al. (2012) — AlexNet, la classification ImageNet qui lance la vision profonde.
- He et al. (2015) — ResNet · Dosovitskiy et al. (2020) — ViT.
