---
galaxie: wiki
type: concept
nom: Vision par ordinateur
alias: [computer vision, CV, vision]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [computer-vision, cnn, deep-learning]
---

# Vision par ordinateur

## Aperçu

- Discipline qui fait **extraire du sens d'images et de vidéos** par un modèle : étiqueter, localiser, segmenter, décrire, générer.
- Depuis 2012 (AlexNet sur ImageNet), le champ est dominé par le [[MOC/Concepts/Deep learning|deep learning]] : les features sont **apprises de bout en bout**, plus dessinées à la main (SIFT, HOG).

## Concepts clés

### Les grandes tâches
- **[[Classification d'images|Classification]]** : une étiquette par image (chat / chien).
- **[[Détection d'objets]]** : boîtes englobantes + classes (YOLO, Faster R-CNN, DETR).
- **[[Segmentation]]** : une classe par pixel — sémantique, d'instance (Mask R-CNN) ou promptable ([[Segment Anything (SAM)|SAM]]).
- **Au-delà** : [[Estimation de pose|estimation de pose]], [[Rendu neuronal 3D & estimation de profondeur|profondeur et reconstruction 3D]], [[Suivi d'objets|suivi multi-cibles]], [[OCR|lecture de texte (OCR)]], [[Metric learning & ré-identification|ré-identification]], et le versant **génératif** ([[GANs|GAN]], synthèse d'images).

### Deux ossatures
- Le **[[CNN]]** (réseau convolutif) : l'ossature historique, biais inductif local et invariance par translation.
- Le **[[Vision Transformers (ViT)|Vision Transformer (ViT)]]** : applique la [[Self-attention|self-attention]] des [[Transformer architectures|Transformers]] à des patchs d'image ; rivalise avec les CNN dès qu'il y a beaucoup de données.

### Ce qui fait marcher un projet vision
- Rarement entraîner de zéro : on part d'un backbone pré-entraîné via [[Transfer learning vision|transfert d'apprentissage]].
- Les backbones les plus puissants sont des [[Modèles de fondation vision|modèles de fondation]] (CLIP, DINOv2), souvent pré-entraînés en [[Apprentissage auto-supervisé en vision|auto-supervisé]] sans étiquettes.
- Les données sont l'enjeu : [[Augmentation d'images|augmentation]] pour étendre et régulariser le jeu.

## Les maths, simplement

- La brique commune reste la **convolution** (détaillée dans [[CNN]]) ; le ViT, lui, repose sur l'attention $\text{softmax}\!\left(QK^\top/\sqrt{d_k}\right)V$.
- Une intuition transverse : une image est une grille où **le voisinage porte le sens** — convolution et attention exploitent cette structure différemment (local figé vs global appris).

## En pratique

- Pile de référence : [[Dev/Services/PyTorch|PyTorch]] (+ [[Dev/Services/torchvision|torchvision]]) ou [[Dev/Services/Keras|Keras]] ; backbones pré-entraînés via [[Dev/Services/timm|timm]] ; vision classique et prétraitement avec [[Dev/Services/OpenCV|OpenCV]].
- Évaluer avec les bonnes métriques : [[Classification metrics|accuracy top-k]] en classification, [[Métriques vision|mAP en détection, IoU/Dice en segmentation]] ; perte d'entraînement = [[Cross-entropy|entropie croisée]].
- Cible contrainte (mobile, edge) : architecture légère + [[Quantization|quantization]] / [[Distillation|distillation]].

## Approches voisines & alternatives

- [[Classification d'images]] / [[Détection d'objets]] / [[Segmentation]] / [[Segment Anything (SAM)]] — les grandes tâches en détail, et [[Métriques vision|leurs métriques]].
- [[Estimation de pose]] / [[Suivi d'objets]] / [[OCR]] / [[Metric learning & ré-identification]] — les tâches de vision au-delà des trois grandes.
- [[CNN]] / [[Architectures CNN]] — l'ossature convolutive et ses familles concrètes.
- [[Vision Transformers (ViT)]] / [[Modèles de fondation vision]] / [[Apprentissage auto-supervisé en vision]] — l'ossature attentionnelle, les grands backbones pré-entraînés (CLIP, DINOv2) et leur entraînement sans étiquettes.
- [[Transfer learning vision]] / [[Augmentation d'images]] — comment entraîner avec peu de données.
- [[MOC/Concepts/Deep learning|Deep learning]] — la famille mère (optimisation, attention, génératif).
- [[Vision Language Models]] — relier image et texte (VLM).
- [[Image generation]] / [[Diffusion models]] / [[GANs]] — le versant génératif de la vision.
- [[Rendu neuronal 3D & estimation de profondeur]] — le versant 3D : reconstruction de scènes et profondeur.

## Pour aller plus loin

- Krizhevsky et al. (2012) — *ImageNet Classification with Deep CNNs* (AlexNet, le déclic).
- Dosovitskiy et al. (2020) — *An Image is Worth 16×16 Words* (ViT).
- Szeliski — *Computer Vision: Algorithms and Applications* (référence générale).
