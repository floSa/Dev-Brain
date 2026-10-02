---
role: notion
nom: Apprentissage contrastif
alias: [Contrastive learning, apprentissage par contraste, perte contrastive, InfoNCE, NT-Xent, SimCLR, MoCo, CLIP, BYOL, VICReg, SimSiam, SigLIP, négatifs, collapse de représentation, température]
categorie: ml/apprentissage-profond
domaines: [ml-eng, ai-eng]
tags: [self-supervised, representation-learning, metric-learning, multimodal]
---

# Apprentissage contrastif

## Aperçu

- Apprendre des **représentations** en rapprochant dans l'espace d'embedding les éléments qu'on sait liés (paires **positives**) et en éloignant ceux qui ne le sont pas (**négatifs**). Aucune étiquette de classe n'est nécessaire : la relation positive vient d'une construction (deux vues augmentées d'une image, une image et sa légende, deux passages d'un même document).
- Une même famille de pertes sert trois usages : le pré-entraînement **auto-supervisé** ([[Apprentissage auto-supervisé en vision]]), l'alignement **multimodal** (CLIP : image et texte dans le même espace) et l'apprentissage de **métrique** ([[Metric learning & ré-identification]]). Cette page porte la **perte** et ses réglages ; les deux autres portent leur domaine d'application.
- La perte de référence est **InfoNCE** (van den Oord et al., 2018). Tout le travail pratique tient dans trois réglages : **combien de négatifs**, **quelle température**, **quelles augmentations**.

## Concepts clés

### Paires positives et négatifs
- Une paire positive est construite : deux vues augmentées de la même image (SimCLR, MoCo), une image et son texte (CLIP). Les négatifs sont les **autres éléments** du lot ou d'une file.
- Un négatif tiré au hasard peut appartenir à la même classe que l'ancre : c'est un **faux négatif**. Chuang et al. (2020) corrigent ce biais d'échantillonnage par une perte « débiaisée » reposant sur un a priori de classe, et annoncent +4,26 % pour SimCLR sur STL10.

### InfoNCE et NT-Xent
- InfoNCE : parmi $N$ candidats (1 positif, $N-1$ négatifs), identifier le positif. C'est une **entropie croisée à $N$ classes**. Van den Oord et al. montrent que la perte minimisée donne une borne inférieure de l'information mutuelle, $I \ge \log N - L_N$, qui se resserre quand $N$ augmente.
- **NT-Xent** (SimCLR) : même perte, avec la **similarité cosinus** et une température $\tau$, calculée sur les deux sens de chaque paire positive du lot.

### Température
- $\tau$ règle la **netteté** de la distribution sur les candidats : petite, elle concentre le gradient sur les négatifs les plus proches (durs) ; grande, elle les traite de façon plus uniforme.
- SimCLR (table 5, 4096 exemples, vecteurs normalisés) : $\tau = 0{,}05 \to 59{,}7\ \%$, $0{,}1 \to 64{,}4\ \%$, $0{,}5 \to 60{,}7\ \%$, $1 \to 58{,}0\ \%$ en précision linéaire. Sans normalisation $\ell_2$, la tâche contrastive est plus facile mais la **représentation est moins bonne**.
- L'optimum **dépend de la tête** : MoCo v1 prend $\tau = 0{,}07$, MoCo v2 passe à $0{,}2$ avec une tête MLP (66,2 % contre 62,9 % au réglage précédent). CLIP **apprend** $\tau$ (initialisée à 0,07, bornée pour que les logits ne soient jamais multipliés par plus de 100).

### Taille de lot et file de négatifs
- Plus de négatifs resserre la borne d'information mutuelle, et donne un signal plus riche. **SimCLR** prend tous les autres éléments du lot : un lot de 8192 donne 16 382 négatifs par paire positive ; réglage par défaut : lot de 4096, 100 époques, 128 cœurs TPU v3 pour 1,5 h. Le lot compte surtout quand l'entraînement est court.
- **MoCo** (He et al., 2020) **découple** les négatifs du lot : une **file** FIFO de $K$ clés (65 536 dans les expériences) et un **encodeur momentum** $\theta_k \leftarrow m\,\theta_k + (1-m)\,\theta_q$, $m = 0{,}999$ (à $m = 0{,}9$, 55,2 % ; $m = 0$ ne converge pas). Lot de 256 sur 8 GPU.
- Résultat comparable de MoCo v2 (note technique) : 67,5 % à 200 époques avec un lot de 256, contre 66,6 % pour SimCLR à lot 8192 sur 200 époques ; le lot de 4096 en bout à bout est « intractable » sur 8 GPU.
- **CLIP** va dans l'autre sens : lot de **32 768**, 400 millions de paires image-texte, perte symétrique image→texte et texte→image.

### Augmentations et tête de projection
- Pour SimCLR, la **composition** des augmentations (recadrage + distorsion de couleur, puis flou) est décisive ; la perte contrastive travaille à travers elles.
- Une **tête de projection** (MLP à 2 couches, vers 128 dimensions) est entraînée avec la perte puis **jetée** : la couche *avant* la tête donne de meilleures représentations que la sortie de la tête (+3 % pour un MLP non linéaire contre un linéaire, plus de 10 % contre l'absence de tête).

### CLIP : le contrastif multimodal
- Deux encodeurs (image, texte) projettent dans un espace commun ; la perte maximise le cosinus des $N$ vraies paires du lot et minimise celui des $N^2 - N$ fausses. Projection linéaire seulement ; un seul recadrage carré comme augmentation.
- Résultat annoncé : 76,2 % de précision **zéro-shot** sur ImageNet (11,5 % pour Visual N-Grams), « équivalent au ResNet-50 supervisé d'origine » ; l'ingénierie de prompts ajoute près de 5 points.

### Collapse, et méthodes sans négatifs
- **Collapse** : l'encodeur renvoie une sortie constante (ou occupe un sous-espace trop petit) : la similarité des positifs est alors parfaite, et l'information nulle. Les négatifs l'empêchent par construction.
- **BYOL** (Grill et al., 2020) : un réseau en ligne prédit la sortie d'un réseau cible, moyenne mobile des poids du premier ; **prédicteur** MLP sur une branche seulement, **stop-gradient** côté cible. 74,3 % de précision linéaire avec un ResNet-50.
- **SimSiam** (Chen et He, 2021) retire négatifs, grands lots **et** encodeur momentum : le **stop-gradient** est essentiel (sans lui, collapse complet et 0,1 % de précision ; avec : 67,7 %).
- **VICReg** (Bardes, Ponce, LeCun, 2022) évite le collapse par **régularisation explicite** : un terme de **variance** (hinge sur l'écart-type de chaque dimension) contre le collapse de norme, un terme de **covariance** (décorrélation des dimensions) contre la redondance, plus un terme d'invariance (MSE) ; $\lambda = \mu = 25$, $\nu = 1$. 73,2 % de précision linéaire ; ni partage de poids, ni BatchNorm, ni stop-gradient requis.
- **Désaccord sur ce qui empêche le collapse dans BYOL** : le papier BYOL en attribue le mérite à son **prédicteur** (avec un encodeur momentum) ; SimSiam montre qu'on peut se passer du momentum, le stop-gradient restant indispensable. Laissé tel quel.

## Les maths, simplement

- InfoNCE pour une ancre $z$, son positif $z^+$ et $N-1$ négatifs $z^-_k$, avec similarité cosinus $s$ et température $\tau$ :
  $$\mathcal{L} = -\log \frac{\exp\!\big(s(z, z^+)/\tau\big)}{\exp\!\big(s(z, z^+)/\tau\big) + \sum_{k=1}^{N-1} \exp\!\big(s(z, z^-_k)/\tau\big)}$$
- C'est une **entropie croisée softmax** où le positif est la bonne « classe ». Plus $N$ est grand, plus la tâche est difficile, et plus la borne $\log N - L_N$ sur l'information mutuelle peut monter.
- Wang et Isola (2020) montrent que, quand le nombre de négatifs tend vers l'infini, la perte se décompose en deux termes : un **alignement** (les positifs proches) et une **uniformité** (les embeddings répartis uniformément sur l'hypersphère). Optimiser directement ces deux quantités donne des représentations comparables ou meilleures que la perte contrastive.

## En pratique

- Quand on peut **construire** des positifs sûrs et qu'on a peu d'étiquettes : contrastif (ou auto-distillation) pour pré-entraîner, puis [[Transfer learning vision|transfert]] et sonde linéaire pour évaluer.
- **Pas de grand lot, pas de TPU** : file de négatifs façon MoCo, ou méthode sans négatifs (BYOL, SimSiam, VICReg).
- **Lot limité en mémoire sur un modèle image-texte** : SigLIP (Zhai et al., 2023) remplace le softmax par une perte **sigmoïde par paire** : chaque paire est une classification binaire indépendante, sans normalisation globale. Les auteurs annoncent qu'elle permet de grossir encore le lot **et** qu'elle fait mieux à petit lot ; poussé jusqu'à un million, le gain d'un lot plus grand s'estompe vite, un lot de 32 000 suffisant. Résultat annoncé : un modèle SigLiT à 84,5 % de précision zéro-shot sur ImageNet en deux jours sur quatre puces TPUv4. Le papier SigLIP 2 (2025) combine cette perte à de l'auto-distillation, de la prédiction masquée et de la légende.
- **Fine-tuner un encodeur de texte** sur son domaine : `sentence-transformers` fournit les pertes contrastives (`MultipleNegativesRankingLoss`) ; le lot sert de négatifs, donc **un lot plus grand donne plus de négatifs gratuits**.
- Évaluer un encodeur contrastif : sonde linéaire sur le backbone gelé, $k$-NN, ou zéro-shot pour CLIP. La précision de la **tâche contrastive elle-même** n'est pas un bon indicateur (SimCLR : plus haute sans normalisation $\ell_2$, représentation pourtant moins bonne).
- Une borne d'information mutuelle plus serrée ne donne **pas** de meilleures représentations : Tschannen et al. (2019) montrent que des estimateurs plus lâches peuvent mieux apprendre, et que le succès tient aux biais inductifs de l'encodeur et à la paramétrisation de l'estimateur, pas à la valeur de la borne.
- Un collapse **dimensionnel** existe aussi avec des négatifs : Jing et al. (2022) montrent que les embeddings peuvent occuper un sous-espace trop petit ; lu par résumé seulement.

## Approches voisines & alternatives

- [[Apprentissage auto-supervisé en vision]] — le domaine d'application historique ; la perte y est décrite en trois lignes, détaillée ici.
- [[Metric learning & ré-identification]] — pertes par paires, triplets et marges angulaires ; InfoNCE s'y rattache, Tschannen et al. le réécrivent comme le *K-pair loss* de la métrique profonde.
- [[Transfer learning vision]] — l'usage aval des représentations contrastives.
- [[Distillation]] — BYOL et DINO sont des auto-distillations (étudiant et enseignant en moyenne mobile).
- [[embeddings]] — ce que produit l'encodeur ; [[Choisir un modèle d'embedding]] pour le choix côté texte.
- [[Régularisation]] — VICReg est une régularisation explicite de la variance et de la covariance.
- [[Normalisation et initialisation des réseaux]] — la BatchNorm calcule ses statistiques sur le lot, ce qui peut faire fuiter de l'information entre échantillons : MoCo y répond par un *shuffling BN* ; VICReg n'exige pas de BatchNorm ; les sorties sont normalisées $\ell_2$ avant les similarités cosinus.
- [[sentence-transformers]] — pertes contrastives pour fine-tuner un encodeur de texte.
- [[SetFit]] — fine-tuning contrastif d'un sentence-transformer, puis tête de classification, avec quelques dizaines d'exemples.

## Pour aller plus loin

- van den Oord, Li & Vinyals (2018) — [*Representation Learning with Contrastive Predictive Coding*](https://arxiv.org/abs/1807.03748) (préprint).
- Chen, Kornblith, Norouzi & Hinton (2020) — [*A Simple Framework for Contrastive Learning of Visual Representations*](https://arxiv.org/abs/2002.05709) (SimCLR).
- He, Fan, Wu, Xie & Girshick (2020) — [*Momentum Contrast for Unsupervised Visual Representation Learning*](https://arxiv.org/abs/1911.05722) (MoCo, CVPR 2020) ; Chen, Fan, Girshick & He (2020) — [*Improved Baselines with Momentum Contrastive Learning*](https://arxiv.org/abs/2003.04297).
- Radford et al. (2021) — [*Learning Transferable Visual Models From Natural Language Supervision*](https://arxiv.org/abs/2103.00020) (CLIP).
- Grill et al. (2020) — [*Bootstrap Your Own Latent*](https://arxiv.org/abs/2006.07733) ; Chen & He (2021) — [*Exploring Simple Siamese Representation Learning*](https://arxiv.org/abs/2011.10566) ; Bardes, Ponce & LeCun (2022) — [*VICReg*](https://arxiv.org/abs/2105.04906), ICLR 2022.
- Wang & Isola (2020) — [*Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere*](https://arxiv.org/abs/2005.10242), ICML 2020.
- Tschannen et al. (2019) — [*On Mutual Information Maximization for Representation Learning*](https://arxiv.org/abs/1907.13625), ICLR 2020 ; Chuang et al. (2020) — [*Debiased Contrastive Learning*](https://arxiv.org/abs/2007.00224), NeurIPS 2020 ; Jing et al. (2022) — [*Understanding Dimensional Collapse in Contrastive Self-supervised Learning*](https://arxiv.org/abs/2110.09348).
- Zhai, Mustafa, Kolesnikov & Beyer (2023) — [*Sigmoid Loss for Language Image Pre-Training*](https://arxiv.org/abs/2303.15343), ICCV 2023 ; Tschannen et al. (2025) — [*SigLIP 2*](https://arxiv.org/abs/2502.14786).
