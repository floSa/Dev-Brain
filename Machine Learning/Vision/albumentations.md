---
role: brique
nom: albumentations
alias: [albu, albumentations-team]
pitch: "Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision."
categorie: ml/vision
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[torchvision]]", "[[Kornia]]"]
complements: ["[[OpenCV]]"]
tags: [computer-vision, data-augmentation, object-detection, segmentation, deep-learning]
url_docs: https://albumentations.ai/docs/
url_repo: https://github.com/albumentations-team/albumentations
---

# albumentations

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'augmentation d'images la plus rapide et la plus riche de l'écosystème Python :
70+ transformations géométriques et photométriques, déclarées comme un pipeline
(`A.Compose([...])`) avec une probabilité par opération. Sa force distinctive est qu'elle
propage **cohéremment** la transformation aux **cibles** — boîtes englobantes, masques de
segmentation, keypoints — ce qui en fait le défaut pour la détection et la segmentation, pas
seulement pour la classification. Bâtie sur OpenCV et NumPy, elle travaille sur des tableaux
HWC, en CPU et hors du graphe d'autograd.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Augmenter un dataset de détection ou de segmentation en gardant boîtes et masques alignés | Le format des boîtes est à déclarer explicitement dans `bbox_params` (`pascal_voc`, `coco`, `yolo`) — un mauvais format décale silencieusement les annotations |
| Pipeline d'augmentation CPU performant dans un `Dataset`/`DataLoader` PyTorch | Le fork `AlbumentationsX` porte les **mêmes imports** que le paquet historique, sous une licence opposée : la confusion est facile |
| Large catalogue de transformations — météo, distorsions, dropout spatial — déclaré de façon lisible | Rester dans l'écosystème officiel, sans dépendance supplémentaire → [[torchvision]] |
| | Augmenter autre chose que de l'image (texte, audio, tabulaire) : hors périmètre |
| | Augmentation **sur GPU** et **différentiable**, dans le graphe d'autograd → [[Kornia]] |

## Mise en œuvre

- Installation — `uv add albumentations`
- Point d'entrée — un pipeline `A.Compose([...])`, terminé par `ToTensorV2` pour sortir un tenseur PyTorch
- Prérequis — Python, NumPy et OpenCV ; le format des boîtes déclaré dans `bbox_params`
- Exécution — CPU, single-node, dans le `DataLoader` ; rien à héberger
- Coût — MIT pour le paquet `albumentations` historique, maintenu en 2.x ; le fork `AlbumentationsX`, présenté comme remplaçant direct, est en double licence AGPL-3.0 / commerciale et concentre les nouveautés

## Écosystème

### Alternatives

- [[torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- [[Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.

### Compléments

- [[OpenCV]] — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning. — le moteur d'image sur lequel albumentations est bâtie

## Ressources

- Documentation — https://albumentations.ai/docs/
- Dépôt — https://github.com/albumentations-team/albumentations

## Voir aussi

- [[Augmentation d'images]] — la notion dont albumentations est l'outil de référence
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
- [[Détection d'objets]], [[Segmentation]] — les tâches où la propagation aux cibles compte
- [[PyTorch]] — l'intégration `Dataset` / `DataLoader`
