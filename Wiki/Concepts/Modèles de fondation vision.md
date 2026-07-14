---
galaxie: wiki
type: concept
nom: Modèles de fondation vision
alias: [foundation models vision, vision foundation models, CLIP, DINOv2, DINOv3, SigLIP, OpenCLIP, modèles de fondation visuels]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [foundation-model, vision-language, self-supervised, representation-learning, computer-vision]
---

# Modèles de fondation vision

## Aperçu

- Gros modèles visuels **pré-entraînés à grande échelle**, généralistes : leurs features se réutilisent par **transfert** ou en **zero-shot** sur quantité de tâches sans réentraîner le backbone.
- Deux familles dominantes : **alignées au langage** (CLIP — image ↔ texte) et **purement visuelles auto-supervisées** (DINOv2/DINOv3 — features denses sans étiquettes).

## Concepts clés

### CLIP — alignement image-texte contrastif
- Deux encodeurs (image, souvent un [[Vision Transformers (ViT)|ViT]] ; et texte) entraînés par **contraste** sur ~400 M paires image-texte du web : rapprocher chaque image de sa légende, éloigner les autres. Donne des [[embeddings]] image et texte **dans le même espace**.
- Débloque la **classification zero-shot** : comparer l'embedding d'une image à ceux de prompts *« une photo de {classe} »*. CLIP (Radford et al., 2021) ; **SigLIP** (perte sigmoïde) est l'encodeur de référence des [[Vision Language Models|VLM]] récents.

### DINOv2 / DINOv3 — features visuelles auto-supervisées
- **Sans texte ni étiquettes** : entraînement par [[Apprentissage auto-supervisé en vision|self-distillation]] (lignée DINO). Produit des **features denses** fortes (segmentation, profondeur, correspondance) exploitables avec un simple *linear probe* ou backbone **gelé**.
- DINOv2 (Meta, 2023) : ~142 M images curées. DINOv3 (2023→2025, arXiv 2508.10104) : ~1,7 Md d'images, ViT teacher de 7 Md de paramètres, *Gram anchoring* contre la dégradation des features denses — premier SSL à **dépasser le faiblement supervisé** sur un large éventail de sondes.

### Ce qui en fait des « fondations »
- **Échelle** (données + paramètres) + **généralité** : on les consomme gelés ou par transfert léger. Deux modes d'usage : **zero-shot** (CLIP, via le langage) ou **linear probe / k-NN** (DINO, sur features).

## Les maths, simplement

- Objectif CLIP (InfoNCE symétrique) : pour un lot de paires, maximiser la similarité cosinus $\langle e^{\text{img}}_i, e^{\text{txt}}_i\rangle/\tau$ de la bonne paire contre toutes les autres du lot — un softmax sur les similarités, dans les deux sens.
- Zero-shot : $\hat y = \arg\max_c \cos\!\big(e^{\text{img}},\, e^{\text{txt}}_c\big)$, où $e^{\text{txt}}_c$ est l'embedding du prompt de la classe $c$.

## En pratique

- **CLIP / SigLIP** : recherche multimodale, classification zero-shot, filtrage de datasets, et surtout **encodeur visuel des VLM**. Outillage : OpenCLIP, [[Dev/Services/HuggingFace|HuggingFace]].
- **DINOv2/v3** : features denses prêtes à l'emploi (segmentation, profondeur, *retrieval* visuel) **sans annotation** — idéal quand les étiquettes manquent.
- Piège : un backbone gelé n'est pas magique sur un domaine très éloigné (imagerie médicale, satellite) — un fine-tuning ciblé reste parfois nécessaire.

## Approches voisines & alternatives

- [[Vision Language Models]] — un VLM **branche** un encodeur de fondation (CLIP/SigLIP) sur un LLM ; la fondation vision en est la brique perceptive.
- [[embeddings]] — CLIP produit des embeddings image-texte **alignés** dans un espace commun.
- [[Vision Transformers (ViT)]] — le backbone quasi systématique de ces modèles.
- [[Apprentissage auto-supervisé en vision]] — la **méthode** d'entraînement de DINOv2 (DINO, MAE) ; la fondation en est le produit passé à l'échelle.
- [[Transfer learning vision]] — l'usage gelé / par transfert de ces backbones.
- [[Segment Anything (SAM)]] — autre fondation vision, dédiée à la segmentation promptable.

## Pour aller plus loin

- Radford et al. (2021) — *Learning Transferable Visual Models from Natural Language Supervision* (CLIP).
- Oquab et al. (2023) — *DINOv2: Learning Robust Visual Features without Supervision*.
- Siméoni et al. (2025) — *DINOv3* (arXiv 2508.10104).
- Zhai et al. (2023) — *Sigmoid Loss for Language Image Pre-Training* (SigLIP).
