---
galaxie: wiki
type: concept
nom: Augmentation d'images
alias: [data augmentation, augmentation de données, Mixup, CutMix, RandAugment]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [data-augmentation, regularization, computer-vision, deep-learning]
---

# Augmentation d'images

## Aperçu

- Générer des variantes plausibles des images d'entraînement (mêmes labels) pour **agrandir et diversifier** le jeu sans nouvelle annotation.
- C'est une **régularisation** : le modèle apprend des invariances et surapprend moins ; quasi systématique en vision.

## Concepts clés

### Transformations classiques
- **Géométriques** : flip, rotation, crop aléatoire, scale, translation. **Photométriques** : luminosité, contraste, teinte, bruit, flou. Le choix doit **préserver le label** (ne pas flip horizontalement un « 2 »).

### Politiques aléatoires
- **RandAugment** : tire $N$ opérations au hasard dans un catalogue, toutes à une magnitude $M$ commune — 2 hyperparamètres seulement, sans la recherche coûteuse d'AutoAugment.

### Augmentations par mélange
- **Mixup** : combine **linéairement** deux images *et* leurs labels — lisse les frontières de décision.
- **CutMix** : **colle un patch** d'une image dans une autre et mélange les labels au **prorata de l'aire** — garde des régions nettes (mieux pour la localisation) tout en régularisant.
- Cousins du **label smoothing** : tous fabriquent des cibles « molles ».

## Les maths, simplement

- Mixup : $\tilde x = \lambda x_i + (1-\lambda)x_j,\quad \tilde y = \lambda y_i + (1-\lambda)y_j$, avec $\lambda \sim \mathrm{Beta}(\alpha,\alpha)$.
- CutMix : même mélange de labels, mais $\lambda$ = **fraction d'aire** conservée de l'image d'origine (le reste vient du patch collé).
- Effet : pénalise la sur-confiance et réduit la variance — cf. [[Compromis biais-variance|compromis biais-variance]].

## En pratique

- Baseline solide : flips + random crop + RandAugment ; ajouter Mixup/CutMix pour pousser la précision sur gros entraînement.
- Ne pas casser la sémantique du label, et **désactiver** les augmentations fortes en validation/test.
- Utile aussi contre le déséquilibre ([[Imbalanced classification]]) en sur-générant les classes rares ; perte [[Cross-entropy|entropie croisée]] (souple, compatible Mixup).
- Outils : `transforms.v2` de [[Dev/Services/torchvision|torchvision]], [[Dev/Services/albumentations|albumentations]] (rapide, gère boîtes/masques), [[Dev/Services/Kornia|Kornia]] (différentiable, sur GPU).

## Approches voisines & alternatives

- [[Transfer learning vision]] — l'autre grand levier « petites données » ; on les combine.
- [[CNN]] / [[Vision par ordinateur]] — ce que l'augmentation régularise.
- [[Distillation]] — autre forme de régularisation par cibles molles (d'un modèle maître).

## Pour aller plus loin

- Zhang et al. (2017) — *mixup: Beyond Empirical Risk Minimization*.
- Yun et al. (2019) — *CutMix* · Cubuk et al. (2019) — *RandAugment*.
