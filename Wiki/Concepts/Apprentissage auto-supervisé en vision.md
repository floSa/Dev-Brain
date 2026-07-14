---
galaxie: wiki
type: concept
nom: Apprentissage auto-supervisé en vision
alias: [self-supervised learning, SSL, auto-supervisé, SimCLR, MoCo, BYOL, DINO, MAE, masked autoencoder, apprentissage contrastif]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [self-supervised, representation-learning, computer-vision, deep-learning]
---

# Apprentissage auto-supervisé en vision

## Aperçu

- Apprendre des **représentations visuelles sans étiquettes**, en résolvant une **tâche prétexte** construite à partir des images elles-mêmes. Les features apprises se transfèrent ensuite (linear probe, fine-tuning).
- Idée clé : la supervision vient des **données**, pas d'annotateurs — ce qui permet d'exploiter des milliards d'images brutes. C'est le moteur des [[Modèles de fondation vision|modèles de fondation]] (DINOv2).

## Concepts clés

### Contrastif (SimCLR, MoCo)
- Rapprocher deux **vues augmentées** de la même image (positives), éloigner les autres (négatives). **SimCLR** (Chen et al., 2020) y parvient avec de **très gros lots** (beaucoup de négatifs) ; **MoCo** (He et al., 2020) garde une **file d'attente** de négatifs et un **encodeur momentum** (EMA) → beaucoup de négatifs sans lot géant. Perte **InfoNCE**.

### Non-contrastif / self-distillation (BYOL, DINO)
- **Sans négatifs** : un réseau *student* prédit la sortie d'un *teacher* (moyenne mobile des poids du student). **BYOL** montre que ça marche sans paires négatives ; **DINO** (Caron et al., 2021) applique l'idée à un [[Vision Transformers (ViT)|ViT]] → les cartes d'attention **segmentent les objets** sans aucune supervision. Le *collapse* (sortie constante) est évité par *centering* / *sharpening* et *stop-gradient*.

### Masquage (MAE)
- **Masked Autoencoder** (He et al., 2022) : masquer ~75 % des patchs et **reconstruire** les pixels manquants. Reconstructif plutôt que contrastif, très **scalable** (l'encodeur ne voit que les patchs visibles). C'est l'analogue vision du pré-entraînement masqué de BERT.

### Comment on évalue
- *Linear probing* (geler le backbone, n'entraîner qu'une tête linéaire), **k-NN**, ou fine-tuning complet — pour mesurer la qualité des représentations apprises sans étiquettes.

## Les maths, simplement

- InfoNCE (contrastif) : $\mathcal{L} = -\log \dfrac{\exp(\text{sim}(z_i, z_j)/\tau)}{\sum_k \exp(\text{sim}(z_i, z_k)/\tau)}$ — pousse la paire positive $(i,j)$ au-dessus de tous les négatifs $k$ ; $\tau$ est la température, $\text{sim}$ le cosinus.
- Self-distillation (DINO) : minimiser l'entropie croisée entre les distributions *student* et *teacher* sur des vues différentes, le *teacher* étant l'EMA du *student* (gradient bloqué côté teacher).

## En pratique

- Régime de prédilection : **beaucoup d'images, peu d'étiquettes** — pré-entraîner sans annotation, puis transférer sur la tâche cible avec peu de labels.
- L'**augmentation forte** (recadrage, couleur) est le cœur du contrastif : elle définit ce que « même image » veut dire (cf. [[Augmentation d'images]]).
- Le produit concret n'est pas un classifieur mais un **backbone réutilisable** (DINOv2) → voir [[Modèles de fondation vision]].

## Approches voisines & alternatives

- [[Modèles de fondation vision]] — DINOv2 est le passage à l'échelle de DINO ; cette page décrit la **méthode**, la fondation en est le **produit**.
- [[Vision Transformers (ViT)]] — l'ossature qu'entraînent MAE et DINO.
- [[embeddings]] — les représentations apprises, exploitables par similarité.
- [[Metric learning & ré-identification]] — cousine **supervisée** : mêmes pertes contrastives / triplet, mais avec des étiquettes de similarité.
- [[Transfer learning vision]] — l'usage en aval des backbones auto-supervisés.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Chen et al. (2020) — *SimCLR* · He et al. (2020) — *MoCo*.
- Grill et al. (2020) — *BYOL* · Caron et al. (2021) — *DINO* (Emerging Properties in Self-Supervised ViTs).
- He et al. (2022) — *Masked Autoencoders Are Scalable Vision Learners* (MAE).
