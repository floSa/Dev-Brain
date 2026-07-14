---
galaxie: dev
type: service
nom: albumentations
alias: [albu, albumentations-team]
pitch: "Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/torchvision|torchvision]]", "[[Dev/Services/Kornia|Kornia]]"]
remplace_par: []
status: actif
tags: [computer-vision, data-augmentation, object-detection, segmentation, deep-learning]
url_docs: https://albumentations.ai/docs/
url_repo: https://github.com/albumentations-team/albumentations
---

# albumentations

## Pourquoi

Bibliothèque d'**[[Augmentation d'images|augmentation]]** la plus rapide et la plus riche de l'écosystème Python : 70+ transformations géométriques et photométriques, déclarées comme un pipeline (`A.Compose([...])`) avec probabilités par opération. Sa force distinctive : elle propage **cohéremment** la transformation aux **cibles** — boîtes englobantes, masques de segmentation et keypoints — ce qui en fait le défaut pour la [[Détection d'objets|détection]] et la [[Segmentation|segmentation]], pas seulement la classification. Bâtie sur [[Dev/Services/OpenCV|OpenCV]] et NumPy, elle est sensiblement plus rapide que l'ancienne API torchvision sur CPU.

## Quand l'utiliser

- Augmenter un dataset de **détection / segmentation** en gardant boîtes et masques alignés.
- Pipeline d'augmentation **CPU** performant dans le `Dataset`/`DataLoader` PyTorch (via `ToTensorV2`).
- Besoin d'un large catalogue de transformations (météo, distorsions, dropout spatial) déclaré de façon lisible.

## Quand NE PAS l'utiliser

- Rester dans l'écosystème officiel sans dépendance en plus → `transforms.v2` de [[Dev/Services/torchvision|torchvision]].
- Augmentation **sur GPU** et **différentiable** (dans le graphe d'autograd) → [[Dev/Services/Kornia|Kornia]].
- Augmentation hors image (texte, audio, tabulaire) → outils dédiés.

## Déploiement & coût

- Open-source **MIT**, gratuit ; `uv add albumentations`. Pur Python au-dessus d'OpenCV/NumPy, CPU, single-node.
- **Attention licence** : l'équipe développe désormais un fork **AlbumentationsX** en double licence **AGPL-3.0 / commerciale**, présenté comme remplaçant direct. Le paquet `albumentations` historique reste MIT et maintenu (v2.x en 2025), mais les nouveautés sont poussées vers la version sous AGPL — vérifier l'implication de licence avant d'adopter le fork en contexte propriétaire.

## Pièges

- **Format des boîtes** à déclarer explicitement (`bbox_params` : `pascal_voc`, `coco`, `yolo`) — un mauvais format décale silencieusement les annotations.
- Travaille sur des tableaux **NumPy** (HWC), pas des tenseurs : terminer le pipeline par `ToTensorV2`.
- Ne pas confondre `albumentations` (MIT) et `AlbumentationsX` (AGPL/commercial) : mêmes imports, licences opposées.

## Alternatives

- [[Dev/Services/torchvision|torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- [[Dev/Services/Kornia|Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

## Liens

- [[Augmentation d'images]] — le concept dont albumentations est l'outil de référence.
- [[Dev/Services/OpenCV|OpenCV]] — le moteur d'image sous-jacent.
- [[Détection d'objets]] / [[Segmentation]] — les tâches où la propagation aux cibles compte.
- [[Dev/Services/PyTorch|PyTorch]] — intégration `Dataset`/`DataLoader`.
- Doc : https://albumentations.ai/docs/
