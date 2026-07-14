---
galaxie: wiki
type: concept
nom: Segmentation
alias: [segmentation d'image, image segmentation, segmentation sémantique, segmentation d'instance, segmentation panoptique, U-Net, Mask R-CNN, DeepLab]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [segmentation, computer-vision, deep-learning]
---

# Segmentation

## Aperçu

- Étiqueter **chaque pixel** de l'image — la prédiction la plus fine de la vision. Sortie = carte de masques, pas une boîte.
- Trois variantes selon ce qu'on distingue : sémantique, d'instance, panoptique.

## Concepts clés

### Trois granularités
- **Sémantique** : une classe par pixel, sans distinguer les instances (toutes les « voitures » forment un seul masque).
- **Instance** : sépare les objets comptables (voiture 1, voiture 2) — détecte puis masque chaque instance.
- **Panoptique** : unifie les deux — *things* (objets comptables, par instance) + *stuff* (zones non comptables : ciel, route, par classe).

### Encodeur-décodeur — U-Net
- **U-Net** : encodeur (contraction) + décodeur (expansion) reliés par des **skip connections** qui réinjectent le détail spatial perdu au down-sampling. Référence en imagerie médicale et sur peu de données.

### Convolutions dilatées — DeepLab
- **DeepLab** : convolutions **atrous (dilatées)** pour élargir le champ réceptif sans perdre en résolution, + **ASPP** (mise en commun multi-échelle). Forte en segmentation sémantique.

### Instance par détection — Mask R-CNN
- **Mask R-CNN** : Faster R-CNN + une branche masque par boîte (RoIAlign aligne précisément les features). Le pont [[Détection d'objets|détection]] → segmentation d'instance.

## Les maths, simplement

- Perte par pixel : [[Cross-entropy|entropie croisée]] pixel à pixel, souvent combinée à la **perte Dice** $1-\dfrac{2|A\cap B|}{|A|+|B|}$ (robuste au déséquilibre fond/objet). Métriques dans [[Métriques vision]].

## En pratique

- Sémantique générale : DeepLabv3+ ou backbone + tête FPN. Médical / peu de données : U-Net. Instance : Mask R-CNN. Promptable / zero-shot : [[Segment Anything (SAM)|SAM]].
- Annotation coûteuse (masques au pixel) → [[Augmentation d'images|augmentation]] et [[Transfer learning vision|transfert]] essentiels.
- Évaluer en **mIoU** (sémantique) et **Dice** (médical) ; AP de masque en instance. Cf. [[Métriques vision]].

## Approches voisines & alternatives

- [[Segment Anything (SAM)]] — segmentation **promptable** et généraliste (fondation), sans entraîner par classe.
- [[Détection d'objets]] — boîtes plutôt que masques ; brique de la segmentation d'instance.
- [[Métriques vision]] — IoU, mIoU, Dice.
- [[Vision par ordinateur]] / [[CNN]] — cadre et backbones.

## Pour aller plus loin

- Ronneberger et al. (2015) — U-Net · He et al. (2017) — Mask R-CNN.
- Chen et al. (2017) — DeepLab (convolutions atrous, ASPP).
