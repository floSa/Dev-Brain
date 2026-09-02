---
role: hub
nom: Vision
alias: [CV]
pitch: Les bibliothèques dont l'entrée est une image ou une vidéo — détecter, segmenter, suivre, augmenter, et les backbones qu'on réutilise pour le faire.
domaines: [ml-eng, data-sci]
tags: [computer-vision, cnn, vit, object-detection, segmentation, image-classification, data-augmentation, object-tracking, transfer-learning]
---

# Vision

> Les bibliothèques dont l'entrée est une image ou une vidéo — détecter, segmenter, suivre, augmenter, et les backbones qu'on réutilise pour le faire.

## Ce qu'il faut comprendre

- **Ce dossier n'est pas « les modèles profonds appliqués aux images » — c'est le critère d'entrée qui range ici.** Le socle qui entraîne le réseau est dans [[Apprentissage profond]] ; un modèle qui *génère* une image à partir d'un texte relève de [[LLM & IA générative]] ; un modèle qui lit une image pour en parler ([[Vision Language Models]]) est à cheval, et son outillage est du côté LLM. Ce qui est ici prend des pixels en entrée et produit une structure : classe, boîte, masque, trajectoire, pose.
- **Quatre tâches, quatre sorties, et c'est la sortie qui décide de l'outil**, pas le sujet de l'image : [[Classification d'images]] rend une classe, [[Détection d'objets]] des boîtes, [[Segmentation]] des masques au pixel, [[Estimation de pose]] des points articulés. [[Suivi d'objets]] ajoute la persistance d'identité d'une image à la suivante — c'est un problème d'association, pas de détection, et il se résout après elle. [[Vision par ordinateur]] pose l'ensemble.
- **Les métriques de vision ne se lisent pas comme celles du tabulaire** : une mAP à 0,5 ne veut rien dire sans le seuil d'IoU et le protocole. [[Métriques vision]] est la page à lire avant de comparer deux modèles ou deux articles.
- **On n'entraîne presque jamais depuis zéro.** [[Transfer learning vision]] est la norme : on part d'un backbone pré-entraîné et on adapte la tête. Les deux familles de backbones sont [[Architectures CNN]] et [[Vision Transformers (ViT)]] — le premier reste meilleur à petites données grâce à son biais inductif, le second passe mieux à l'échelle. [[Modèles de fondation vision]] et [[Apprentissage auto-supervisé en vision]] expliquent d'où viennent ces poids sans annotation.
- **L'augmentation est le premier levier de performance, avant le changement de modèle** — et il est presque gratuit. [[Augmentation d'images]] ; attention, une transformation géométrique doit s'appliquer aussi aux boîtes et aux masques, ce qui est exactement le service que rendent les bibliothèques dédiées.
- Deux tâches spécialisées qui reviennent en industrie et méritent leur page : [[Metric learning & ré-identification]] — reconnaître que deux images montrent le *même* objet, pas la même classe — et [[Rendu neuronal 3D & estimation de profondeur]].
- **L'OCR est un pipeline, pas un modèle** : [[OCR]] combine détection de texte, reconnaissance et mise en page. L'outillage de bout en bout n'est pas ici mais dans [[Documents]] et [[Parsing]].
- [[Segment Anything (SAM)]] a changé la pratique de l'annotation : segmenter sans classe et sans réentraînement fait du masque une donnée bon marché, et déplace le travail vers la classification des masques.

## Choisir

- Le point de départ d'un projet vision sous PyTorch → [[torchvision]] : datasets, transformations et backbones dans une seule dépendance.
- Un backbone pré-entraîné, quel qu'il soit → [[timm]], la plus large collection avec une API unique.
- De la détection ou de la segmentation à faire tourner vite, entraînement et export compris → [[Ultralytics YOLO]], en vérifiant la licence AGPL avant tout usage fermé.
- Des implémentations de référence à étendre pour de la recherche → [[Detectron2]].
- Pré-segmenter sans classe, ou accélérer une campagne d'annotation → [[segment-anything]].
- Augmenter des images avec leurs boîtes et leurs masques → [[albumentations]].
- Rendre des opérations de vision différentiables et les mettre dans le graphe d'autograd → [[Kornia]].
- Du traitement d'image classique — géométrie, calibration, filtres, lecture vidéo → [[OpenCV]], sans modèle appris.
- Brancher annotateurs, zones et suivi sur un modèle déjà choisi → [[supervision]]. Cf. [[Comparatif - Détection & segmentation]].
- Entraîner le réseau lui-même → [[Apprentissage profond]] ; l'exposer ensuite en API → [[Serving]].

<!-- AUTO:START -->
### Briques
- [[albumentations]] — Bibliothèque d'augmentation d'images rapide — 70+ transformations gérant nativement boîtes, masques et keypoints (détection, segmentation), au-dessus d'OpenCV ; le standard de l'augmentation CPU dans les pipelines vision.
- [[Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.
- [[Kornia]] — Bibliothèque de vision par ordinateur différentiable pour PyTorch — opérations classiques (filtres, géométrie) et augmentations rendues différentiables sur GPU, intégrables dans le graphe d'autograd ; la CV qui se branche dans l'entraînement.
- [[OpenCV]] — Bibliothèque de vision par ordinateur classique de référence — traitement d'images, géométrie, calibration, détection de features et vidéo, cœur C++ optimisé exposé en Python ; le couteau suisse de la CV hors deep learning.
- [[segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte).
- [[supervision]] — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application.
- [[timm]] — La plus grande collection de backbones vision pour PyTorch — ResNet, EfficientNet, ConvNeXt, ViT, Swin… avec poids pré-entraînés et API create_model unifiée ; la référence du transfert d'apprentissage en vision.
- [[torchvision]] — Bibliothèque vision officielle de PyTorch — datasets, modèles pré-entraînés (backbones CNN et ViT) et transformations d'images (transforms.v2) intégrés au tenseur ; le point de départ d'un projet vision PyTorch.
- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0.

### Comparatifs
- [[Comparatif - Détection & segmentation]]
<!-- AUTO:END -->

## Notes
