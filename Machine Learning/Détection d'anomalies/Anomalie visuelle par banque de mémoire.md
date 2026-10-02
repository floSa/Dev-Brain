---
role: notion
nom: Anomalie visuelle par banque de mémoire
alias: [SPADE, PaDiM, PatchCore, Détection d'anomalies par plus proche voisin, Memory bank anomaly detection, Coreset]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, computer-vision, industrial-inspection, transfer-learning]
---

# Anomalie visuelle par banque de mémoire

## Aperçu

- Famille de détecteurs d'anomalies sur images qui **n'entraînent aucun réseau** : un réseau pré-entraîné sur ImageNet extrait des features de patchs, on **mémorise** celles des images de bon, et un patch de test est suspect s'il ressemble à rien de ce qui est mémorisé.
- Trois méthodes la fondent : SPADE (2020), PaDiM (2020), PatchCore (2022). PatchCore est restée la baseline que toute méthode neuve doit battre.
- Le prix est ailleurs que dans l'entraînement : **mémoire** et **latence** à l'inférence, et une sensibilité à l'alignement des pièces. Cadre général dans [[Détection d'anomalies visuelle]].

## Concepts clés

### Le schéma commun

- Un backbone pré-entraîné ([[Transfer learning vision]] : WideResNet50 dans les trois articles) donne, pour chaque position d'une image, un vecteur de features issu de couches intermédiaires.
- Sur les images d'**entraînement, sans défaut**, ces vecteurs sont stockés sous une forme ou une autre : c'est la « banque de mémoire ».
- Sur une image de test, chaque position est comparée à la banque. La carte des distances est la **carte d'anomalie** ; le score de l'image est, dans PaDiM et PatchCore, le **maximum** de cette carte.
- Aucune rétropropagation : l'« entraînement » se réduit à un passage avant sur les images de bon, ce qui le rend rapide.

### SPADE

Cohen et Hoshen (arXiv 2005.02357, preprint, aucune venue relevée dans le PDF) procèdent en deux temps. Un plus proche voisin sur les features globales d'image (2048 dimensions, après pooling) décide si l'image est anormale. Pour une image jugée anormale, une galerie des features de pixel de ses K plus proches images normales (K = 50 sur MVTec AD) sert à calculer un score par pixel, sur une pyramide de trois blocs ResNet. Résultat lu : 85,5 % d'AUROC image, 96,0 % d'AUROC pixel sur MVTec AD. La complexité de la recherche croît linéairement avec la taille de la galerie.

### PaDiM

Defard et al. (arXiv 2011.08785, atelier ICPR 2020 d'après la page arXiv) concatènent les activations de trois couches et modélisent chaque **position de patch** par une **gaussienne multivariée** apprise sur les images d'entraînement. Le score d'un patch est sa distance de Mahalanobis à la gaussienne de sa position. Une réduction **aléatoire** de dimensions (Rd) allège le calcul, jugée plus efficace qu'une ACP par les auteurs.

- Résultats lus (MVTec AD) : PaDiM-WR50-Rd550, 97,5 % d'AUROC pixel, 92,1 % de PRO, 95,3 % d'AUROC image ; avec EfficientNet-B5, 97,9 % d'AUROC image.
- La mémoire **ne dépend pas du nombre d'images d'entraînement** mais de la résolution : 0,17 Go (R18-Rd100) et 3,8 Go (WR50-Rd550) sur MVTec AD, en float32.

### PatchCore

Roth et al. (arXiv 2106.08265, CVPR 2022) font trois choix. Les patchs sont **localement agrégés** (voisinage de 3, deux niveaux de la hiérarchie) pour que chaque vecteur voie un contexte. Tous les patchs de bon forment la banque M. Un **coreset glouton** (problème de k-centre, accéléré par projection aléatoire de Johnson-Lindenstrauss) la réduit : à 1 % la banque est cent fois plus petite. Le score d'un patch est la distance à son plus proche voisin dans le coreset ; le score image est le maximum.

| Configuration (MVTec AD, valeurs du papier) | AUROC image | AUROC pixel | PRO |
|---|---|---|---|
| PatchCore-25 % | 99,1 | 98,1 | 93,4 |
| PatchCore-1 % | 99,0 | 98,0 | 93,1 |
| Ensemble, 1 %, image 320 | 99,6 | 98,2 | 94,9 |

Le 99,6 % de l'abstract (« jusqu'à ») est donc l'**ensemble** de trois backbones, pas la version de base. Code de référence : [[patchcore-inspection]] ; version intégrée à une bibliothèque : [[anomalib]].

### Mémoire et latence, telles que rapportées

- **PatchCore** (GPU, passe avant du backbone comprise, réimplémentations des auteurs pour SPADE et PaDiM) : 0,6 s par image sans réduction, 0,22 s à 10 %, 0,17 s à 1 % ; SPADE 0,66 s, PaDiM 0,19 s. Sans coreset, la banque grossit avec le nombre d'images, « ce qui coûte en inférence et en stockage » (§3.2).
- **PaDiM** (CPU i7-4710HQ, code série) : 0,23 s en R18-Rd100, 0,95 s en WR50-Rd550 ; SPADE 7,10 s sur le même CPU, avec 1,4 Go de mémoire sur MVTec AD et 37,0 Go sur un autre jeu (STC).
- **Un autre point de comparaison** : EfficientAD mesure sur un GPU A6000, sur un jeu de 32 datasets, 32 ms pour PatchCore, 148 ms pour son ensemble et 2,2 ms pour EfficientAD-S. Il en tire que le goulot des méthodes de plus proche voisin est la recherche de voisins. Conditions du papier, pas celles de PatchCore.
- **À haute résolution**, le papier MVTec AD 2 mesure environ 2 s par image sur la catégorie « Rice » pour PatchCore, avec temps et mémoire qui croissent « de plus d'un ordre de grandeur » ; l'inférence dépend de la taille de la banque, donc du nombre d'images d'entraînement.

### Limites relevées

- **L'alignement.** PaDiM modélise une gaussienne *par position* : il suppose des pièces toujours cadrées pareil, comme dans MVTec AD. Sur sa variante avec rotation de ±10° et recadrage, l'AUROC de PaDiM-WR50-Rd550 baisse de 5,3 points (92,2 en tout), contre 8,8 pour SPADE. PatchCore se présente comme moins dépendant de l'alignement ; un travail ultérieur (FR-PatchCore, *Sensors* 2024) écrit pourtant que PatchCore « impose des exigences strictes d'alignement » et localise mal sur des échantillons tournés ou retournés.
- **Le transfert des features.** Les auteurs de PatchCore le disent : la performance dépend de la transférabilité des features ImageNet vers la texture et l'objet inspectés.
- **Un terrain moins facile.** Sur MVTec AD 2, PatchCore tombe à 53,8 % d'AU-PRO de segmentation (seuil 0,30), contre 92,7 % sur MVTec AD dans le même tableau ; EfficientAD y atteint 58,7 %, le meilleur des sept méthodes testées. Le jeu ajoute des éclairages absents de l'entraînement, des objets transparents ou réfléchissants et des défauts minuscules.

## Les maths, simplement

- Banque $\mathcal{M}$ de vecteurs de patchs de bon ; pour un patch de test $p$ de features $\phi_p$ : $s(p)=\min_{m\in\mathcal{M}}\lVert\phi_p-m\rVert_2$, et $s(x)=\max_p s(p)$ pour l'image (forme simplifiée : PatchCore ajoute une pondération par les $b$ plus proches voisins).
- Coreset glouton (k-centre) : on ajoute à chaque étape le point de $\mathcal{M}$ le plus éloigné de ceux déjà choisis, ce qui couvre l'espace avec peu de points.
- PaDiM, position $(i,j)$ : $M(x_{ij})=\sqrt{(x_{ij}-\mu_{ij})^{\top}\Sigma_{ij}^{-1}(x_{ij}-\mu_{ij})}$, avec $\mu_{ij}$ et $\Sigma_{ij}$ estimés sur les images de bon.

## En pratique

- **Point de départ raisonnable** pour une nouvelle pièce : des images de bon vérifiées, un backbone pré-entraîné, un coreset (PatchCore annonce 99,1 % à 25 % et 99,0 % à 1 % sur MVTec AD). Pas de réseau à entraîner.
- **Réserver la mémoire** : la banque se charge à l'inférence ; compter son poids avant de viser un poste sans GPU, et mesurer la latence sur la **résolution réelle** des images d'atelier, pas sur celle de MVTec AD.
- **Surveiller le cadrage** : un bac, un gabarit ou un détourage évitent à la méthode de confondre un décalage de pièce avec un défaut.
- **Ne pas lire 99 % comme une garantie** : MVTec AD est saturé ([[Détection d'anomalies visuelle]]), et le chiffre du jeu public ne prédit ni l'éclairage, ni la variabilité d'une ligne.
- Les images de bon doivent être **vérifiées** : un défaut présent dans la banque devient du normal ([[Types d'anomalies et régimes de supervision]], contamination).

## Approches voisines & alternatives

- [[Anomalie visuelle par reconstruction, distillation et flux]] — apprendre un réseau au lieu de mémoriser : plus rapide à l'inférence, entraînement en plus.
- [[Anomalie visuelle zero-shot et few-shot]] — quand il n'y a aucune image de bon, ou très peu.
- [[Détection d'anomalies visuelle]] — le cadre général.
- [[Local Outlier Factor]] — voisinage aussi, mais sur des vecteurs de variables tabulaires au lieu de patchs d'image.
- [[Modèles de fondation vision]] — les backbones plus récents (DINOv2) réutilisés comme extracteurs.
- [[patchcore-inspection]], [[anomalib]] — les implémentations.

## Pour aller plus loin

- Cohen, Hoshen, *Sub-Image Anomaly Detection with Deep Pyramid Correspondences*. arXiv : https://arxiv.org/abs/2005.02357
- Defard, Setkov, Loesch, Audigier, *PaDiM: a Patch Distribution Modeling Framework for Anomaly Detection and Localization*. arXiv : https://arxiv.org/abs/2011.08785
- Roth, Pemula, Zepeda, Schölkopf, Brox, Gehler (2022), *Towards Total Recall in Industrial Anomaly Detection*, CVPR. arXiv : https://arxiv.org/abs/2106.08265
- Batzner et al. (2024), *EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies*, WACV. arXiv : https://arxiv.org/abs/2303.14535
- Heckler-Kram et al., *The MVTec AD 2 Dataset: Advanced Scenarios for Unsupervised Anomaly Detection*. arXiv : https://arxiv.org/abs/2503.21622
- Jiang et al., *FR-PatchCore*, *Sensors* 2024 : https://pmc.ncbi.nlm.nih.gov/articles/PMC10934034/
