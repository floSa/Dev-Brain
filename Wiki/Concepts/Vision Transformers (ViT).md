---
galaxie: wiki
type: concept
nom: Vision Transformers (ViT)
alias: [ViT, Vision Transformer, vision transformers, DeiT, Swin Transformer, transformeur de vision]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [vit, transformers, computer-vision, deep-learning]
---

# Vision Transformers (ViT)

## Aperçu

- Application des [[Transformer architectures|Transformers]] aux images : on découpe l'image en **patchs** traités comme des tokens, puis on applique la [[Self-attention|self-attention]] habituelle — sans convolution.
- Idée clé : *« An Image is Worth 16×16 Words »* (Dosovitskiy et al., 2020). À grande échelle de données, le ViT **rivalise ou dépasse** les [[CNN]] ; il est devenu le backbone des [[Modèles de fondation vision|modèles de fondation]] et des [[Vision Language Models|VLM]].

## Concepts clés

### Patchs comme tokens
- Image découpée en $N$ patchs (souvent 16×16), chacun **aplati puis projeté** linéairement en un vecteur → une séquence de tokens. On y ajoute un token de classe `[CLS]` et un [[Positional encoding|encodage de position]] (l'attention étant permutation-invariante).
- Le reste est un Transformer standard : blocs *multi-head attention* + FFN, résiduels, normalisation.

### Pas de biais inductif local
- Contrairement au [[CNN]] (localité, invariance par translation **câblées**), le ViT n'impose presque aucun a priori : il apprend les relations globales par attention. Revers : il lui faut **beaucoup de données** (pré-entraînement type JFT-300M) ou une recette de régularisation / [[Distillation|distillation]] (DeiT) pour égaler un CNN sur ImageNet seul.

### Variantes marquantes
- **DeiT** : ViT *data-efficient*, entraîné sur ImageNet seul via distillation d'un CNN.
- **Swin Transformer** : attention par **fenêtres glissantes** et hiérarchie multi-échelle → coût maîtrisé, adapté à la détection et la [[Segmentation|segmentation]] (backbone dense).
- Backbone de [[Segment Anything (SAM)|SAM]], de DINOv2 et de l'encodeur visuel CLIP.

### Coût et efficacité
- L'attention est en $O(N^2)$ sur le nombre de patchs → haute résolution coûteuse. Réponses : fenêtrage (Swin), [[Flash Attention and efficient attention|attention efficace]], réduction du nombre de tokens.

## Les maths, simplement

- Découpage : une image $H\times W$ donne $N = HW/P^2$ patchs de côté $P$. Séquence d'entrée : $z_0 = [\,x_{\text{cls}};\, x_p^1 E;\, \dots;\, x_p^N E\,] + E_{\text{pos}}$, où $E$ projette chaque patch aplati et $E_{\text{pos}}$ encode sa position.
- Cœur inchangé : $\text{Attn}(Q,K,V) = \text{softmax}\!\left(QK^\top/\sqrt{d_k}\right)V$ — la même attention que sur du texte, appliquée à des patchs.

## En pratique

- Ne pas entraîner de zéro : partir d'un ViT pré-entraîné (timm, [[Dev/Services/HuggingFace|HuggingFace]]) et faire du [[Transfer learning vision|transfert]] ; le ViT est plus gourmand en données que le CNN à budget égal.
- Choix CNN vs ViT : peu de données / contrainte edge → CNN ; gros volume, backbone pré-entraîné fort, tâches multimodales → ViT.
- Sert de backbone bien au-delà de la classification : détection (DETR), segmentation, [[Rendu neuronal 3D & estimation de profondeur|profondeur (DPT)]], encodeurs de VLM.

## Approches voisines & alternatives

- [[Transformer architectures]] — l'architecture mère ; le ViT en est l'application aux images (patchs au lieu de tokens texte).
- [[Self-attention]] / [[Positional encoding]] — le mécanisme central et l'ajout d'ordre, indispensables aux patchs.
- [[CNN]] / [[Architectures CNN]] — l'ossature concurrente (biais local) ; ViT et CNN cohabitent (hybrides, ConvNeXt en réponse).
- [[Modèles de fondation vision]] — CLIP et DINOv2 reposent sur un backbone ViT.
- [[Apprentissage auto-supervisé en vision]] — MAE et DINO pré-entraînent précisément des ViT sans étiquettes.
- [[Vision par ordinateur]] — le cadre d'ensemble, où ViT et CNN sont les deux ossatures.

## Pour aller plus loin

- Dosovitskiy et al. (2020) — *An Image is Worth 16×16 Words* (ViT).
- Touvron et al. (2021) — *Training data-efficient image transformers* (DeiT).
- Liu et al. (2021) — *Swin Transformer* (attention par fenêtres, hiérarchique).
