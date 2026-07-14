---
galaxie: wiki
type: concept
nom: Architectures CNN
alias: [ResNet, MobileNet, EfficientNet, ConvNeXt, backbone vision, CNN architectures]
categorie: concept/dl
domaines: [ml-eng]
tags: [cnn, computer-vision, deep-learning]
---

# Architectures CNN

## Aperçu

- Catalogue des familles de [[CNN|réseaux convolutifs]] éprouvées, à reprendre comme **backbone** plutôt qu'à réinventer.
- Chaque famille répond à un compromis : précision, nombre de paramètres, latence, budget d'entraînement.

## Concepts clés

### ResNet — les connexions résiduelles
- Ajoute un **raccourci** $y = \mathcal{F}(x) + x$ qui laisse le gradient remonter : on entraîne des réseaux très profonds (50, 101, 152 couches) sans dégradation. Le bloc résiduel est devenu une brique universelle — y compris dans les [[Transformer architectures|Transformers]].

### MobileNet — la convolution séparable
- Décompose la convolution en **depthwise** (un filtre par canal) + **pointwise** (1×1 qui mélange les canaux) : ~8–9× moins de calcul pour une perte minime. Conçu pour le mobile/edge ; se marie avec la [[Quantization|quantization]].

### EfficientNet — le compound scaling
- Met à l'échelle **conjointement** profondeur, largeur et résolution selon un coefficient unique, au lieu d'agrandir une seule dimension. Meilleur rapport précision/FLOPs à budget donné — application directe des [[Scaling laws|lois d'échelle]].

### ConvNeXt — le CNN modernisé
- Reprend un ResNet et y injecte les recettes des Transformers (gros noyaux, LayerNorm, GELU, moins d'activations) : un **CNN pur** qui égale les ViT sur ImageNet. Montre que l'écart ViT↔CNN tenait surtout à l'entraînement et au design, pas à l'attention en soi.

## Les maths, simplement

- Bloc résiduel : $y = \mathcal{F}(x, W) + x$ — la couche n'apprend que le **résidu** $\mathcal{F}$, ce qui rend l'identité triviale à représenter (et le gradient direct).
- Convolution séparable : coût $\approx \left(\dfrac{1}{c_{\text{out}}} + \dfrac{1}{k^2}\right)$ fois celui d'une convolution standard.
- Compound scaling : profondeur $\propto \alpha^\phi$, largeur $\propto \beta^\phi$, résolution $\propto \gamma^\phi$, sous la contrainte $\alpha\,\beta^2\,\gamma^2 \approx 2$.

## En pratique

- Choisir selon la contrainte : précision max → ResNet / ConvNeXt ; latence / mobile → MobileNet / EfficientNet-lite.
- Partir des poids pré-entraînés (ImageNet) via [[Transfer learning vision|transfert]] ; alléger ensuite par [[Quantization|quantization]] ou [[Distillation|distillation]] pour l'[[Inference optimization|inférence]].
- Disponibles clés en main : [[Dev/Services/torchvision|torchvision]] ([[Dev/Services/PyTorch|PyTorch]]), [[Dev/Services/Keras|Keras]] Applications, et surtout [[Dev/Services/timm|timm]] (le catalogue le plus large).

## Approches voisines & alternatives

- [[CNN]] — les briques (convolution, pooling, résiduel) que ces familles assemblent.
- [[Vision par ordinateur]] — les tâches servies par ces backbones.
- [[Transformer architectures]] — les ViT, alternative à base d'attention ; ConvNeXt est la réponse « CNN » à cette concurrence.

## Pour aller plus loin

- He et al. (2015) — *Deep Residual Learning for Image Recognition* (ResNet).
- Howard et al. (2017) — *MobileNets* · Tan & Le (2019) — *EfficientNet*.
- Liu et al. (2022) — *A ConvNet for the 2020s* (ConvNeXt).
