---
galaxie: wiki
type: concept
nom: CNN
alias: [convnet, réseau convolutif, convolutional neural network, convolution, pooling, champ réceptif]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [cnn, computer-vision, deep-learning]
---

# CNN

## Aperçu

- Réseau de neurones spécialisé pour les données en grille (images) : il applique les mêmes petits filtres **convolutifs** partout sur l'entrée.
- Deux biais inductifs qui collent aux images : **localité** (un pixel dépend surtout de ses voisins) et **invariance par translation** (un motif est le même où qu'il soit).

## Concepts clés

### Convolution
- Un **noyau** (filtre) $k \times k$ glisse sur l'image et calcule un produit scalaire local → une **carte d'activation**. Les poids du noyau sont **partagés** sur toute l'image : peu de paramètres, et le même motif est détecté partout.
- Hyperparamètres : taille du noyau, **stride** (pas), **padding** (bordure), nombre de filtres (= profondeur de sortie).

### Pooling
- Sous-échantillonnage (max ou moyenne sur une fenêtre) : réduit la résolution spatiale, apporte une invariance locale aux petites translations, baisse le coût. De plus en plus remplacé par des convolutions à stride 2.

### Champ réceptif
- Région de l'image d'entrée qui influence une activation donnée. Il **grandit avec la profondeur** : les premières couches voient des bords, les profondes des parties puis des objets entiers. Un champ réceptif suffisant est nécessaire pour « voir » de grands objets.

### Hiérarchie de features
- Empilement conv → non-linéarité (ReLU) → (pooling). Les features vont du bas niveau (bords, textures) au haut niveau (parties, objets). La **batch normalization** stabilise et accélère l'entraînement.

## Les maths, simplement

- Convolution 2D : $(I * K)(i,j) = \sum_{m}\sum_{n} I(i+m,\,j+n)\,K(m,n)$ — somme des produits du noyau et de la fenêtre locale.
- Taille de sortie : $o = \left\lfloor \dfrac{n + 2p - k}{s} \right\rfloor + 1$ (entrée $n$, noyau $k$, padding $p$, stride $s$).
- Une couche conv a $k^2 \cdot c_{\text{in}} \cdot c_{\text{out}}$ poids — **indépendant de la taille de l'image** (partage de poids), là où une couche dense en exigerait beaucoup plus.

## En pratique

- Entraînement par rétropropagation + [[Gradient descent|descente de gradient]] (SGD+momentum ou [[Adam optimizer|Adam]]), perte [[Cross-entropy|entropie croisée]].
- Quasi jamais de zéro : on réutilise un backbone via [[Transfer learning vision|transfert]] et on densifie le jeu par [[Augmentation d'images|augmentation]].
- Implémentation : [[Dev/Services/PyTorch|PyTorch]] (`nn.Conv2d`) ou [[Dev/Services/Keras|Keras]] ; backbones convolutifs prêts à l'emploi via [[Dev/Services/torchvision|torchvision]] / [[Dev/Services/timm|timm]].

## Approches voisines & alternatives

- [[Architectures CNN]] — les familles concrètes (ResNet, MobileNet…) bâties sur ces briques.
- [[Vision par ordinateur]] — le cadre et les tâches que les CNN servent.
- [[Classification d'images]] / [[Détection d'objets]] / [[Segmentation]] — les tâches bâties sur un backbone convolutif.
- [[Classification audio par spectrogramme]] — le CNN appliqué hors vision, sur des spectrogrammes audio.
- [[Transformer architectures]] — le ViT remplace la convolution par l'[[Self-attention|attention]] sur des patchs : biais inductif plus faible, plus gourmand en données.

## Pour aller plus loin

- LeCun et al. (1998) — *Gradient-Based Learning Applied to Document Recognition* (LeNet).
- Krizhevsky et al. (2012) — *AlexNet*.
- Luo et al. (2016) — *Understanding the Effective Receptive Field in Deep CNNs*.
