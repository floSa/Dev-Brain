---
galaxie: wiki
type: concept
nom: Metric learning & ré-identification
alias: [metric learning, apprentissage de métrique, ré-identification, re-identification, re-id, person re-id, reconnaissance faciale, face recognition, triplet loss, contrastive loss, ArcFace, CosFace, Siamese, CMC, Rank-1]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [metric-learning, re-identification, representation-learning, computer-vision, deep-learning]
---

# Metric learning & ré-identification

## Aperçu

- **Apprendre un espace d'[[embeddings]]** où la distance traduit la similarité : deux images de la **même** identité tombent proches, deux identités différentes loin.
- Application phare : la **ré-identification** — retrouver la même instance (personne, véhicule, visage) à travers le temps et les caméras, là où la classification échoue (les identités de test sont inconnues à l'entraînement).

## Concepts clés

### Pourquoi pas une simple classification
- Le nombre de classes (identités) est ouvert et change : on n'apprend pas « qui », mais une **fonction de comparaison** réutilisable. À l'inférence : encoder, puis chercher le plus proche voisin.

### Pertes par paires et triplets
- **Contrastive** : rapprocher une paire positive, éloigner une paire négative au-delà d'une marge.
- **Triplet** : ancre $a$, positif $p$ (même identité), négatif $n$ (autre) — pousser $a$ vers $p$ et loin de $n$. Le **choix des triplets durs** (hard negative mining) fait l'essentiel de la difficulté.

### Pertes à marge angulaire (ArcFace)
- **ArcFace** reformule le problème en classification sur une **hypersphère** et ajoute une **marge angulaire** au logit de la bonne classe → classes plus compactes, mieux séparées. Famille SphereFace → CosFace → ArcFace, reine de la **reconnaissance faciale**.

### Ré-identification en vision
- Opère sur des **crops détectés** (sortie d'un [[Détection d'objets|détecteur]]) ; fournit l'embedding d'apparence qui robustifie le [[Suivi d'objets|suivi multi-cibles]] (DeepSORT). Évaluation : **Rank-1 / courbe CMC** et **mAP** de récupération.

## Les maths, simplement

- Triplet loss : $\mathcal{L}=\max\!\big(0,\; d(a,p)-d(a,n)+m\big)$ — $d$ une distance (euclidienne sur vecteurs normalisés ≈ cosinus), $m$ la marge.
- ArcFace : logit cible $s\cdot\cos(\theta_{y}+m)$ contre $s\cdot\cos\theta_j$ pour les autres, puis [[Cross-entropy|entropie croisée]] ($\theta$ = angle entre embedding et vecteur de classe, $s$ un facteur d'échelle).

## En pratique

- Normaliser les embeddings (travail au cosinus) ; soigner l'échantillonnage des triplets (batch-hard).
- Recherche du plus proche voisin à l'échelle → index ANN d'une [[Bases de données vectorielles|base vectorielle]].
- Usages : reconnaissance / vérification faciale, person re-id inter-caméras, recherche d'images, déduplication.

## Approches voisines & alternatives

- [[embeddings]] — l'espace de représentation que le metric learning façonne (apprentissage contrastif type InfoNCE).
- [[Suivi d'objets]] — consomme l'embedding de ré-id pour l'association d'apparence (DeepSORT).
- [[Détection d'objets]] — fournit les crops sur lesquels la ré-id opère.
- [[Bases de données vectorielles]] — recherche du plus proche voisin à grande échelle.
- [[Vision par ordinateur]] / [[CNN]] — le cadre et les backbones.

## Pour aller plus loin

- Schroff et al. (2015) — *FaceNet* (triplet loss, embeddings de visages).
- Deng et al. (2019) — *ArcFace* (marge angulaire additive).
