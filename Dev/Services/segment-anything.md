---
galaxie: dev
type: service
nom: segment-anything
alias: [SAM, Segment Anything Model, sam2, sam3]
pitch: "Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte)."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Detectron2|Detectron2]]"]
remplace_par: []
status: actif
tags: [segmentation, foundation-model, computer-vision, transformers, deep-learning, gpu]
url_docs: https://segment-anything.com/
url_repo: https://github.com/facebookresearch/segment-anything
---

# segment-anything

## Pourquoi

Dépôt officiel de Meta AI pour le **Segment Anything Model (SAM)** — code d'inférence, poids pré-entraînés et notebooks. SAM est un [[Modèles de fondation vision|modèle de fondation]] pour la [[Segmentation|segmentation]] **promptable** : à partir d'une **invite** (point, boîte, masque grossier), il renvoie un masque **sans réentraînement par classe** — capacité **zero-shot**. Encodeur d'image ViT lourd (calculé une fois) + décodeur léger rejoué par invite → interactif. La lignée s'est prolongée dans des dépôts dédiés : **SAM 2** (`sam2`, image + vidéo avec mémoire) et **SAM 3** (`sam3`, invites texte / concept open-vocabulary). C'est la brique de référence pour **pré-segmenter et annoter**, pas un détecteur à classes fixes. Concept : [[Segment Anything (SAM)]].

## Quand l'utiliser

- **Annotation assistée** : pré-segmenter pour accélérer le labelling de masques.
- Masques **zero-shot** sur des objets quelconques sans dataset d'entraînement par classe.
- Brique d'un pipeline plus large : détecteur ([[Dev/Services/Ultralytics YOLO|YOLO]]) qui propose des boîtes → SAM qui en tire les masques.
- Segmentation **interactive** pilotée par l'utilisateur (clics, boîtes).

## Quand NE PAS l'utiliser

- **Classes fixes**, latence serrée, précision sur un domaine donné → un U-Net / DeepLab / Mask R-CNN dédié via [[Dev/Services/Detectron2|Detectron2]] ou [[Dev/Services/torchvision|torchvision]].
- Besoin de **détecter et nommer** des objets (boîtes + classes) → [[Dev/Services/Ultralytics YOLO|Ultralytics YOLO]] ou [[Détection d'objets|un détecteur]].
- Contraintes mobiles/temps réel sur l'encodeur lourd → variantes allégées (MobileSAM, FastSAM) plutôt que SAM original.

## Déploiement & coût

- Code et poids open-source sous **Apache-2.0** (permissive), gratuits. Rien à héberger.
- Le dépôt `segment-anything` fournit l'**inférence** (pas de code d'entraînement) ; `pip install` depuis les sources, poids (ViT-B/L/H) à télécharger à part.
- Encodeur ViT **gourmand en VRAM** → GPU recommandé ; single-node. Pour vidéo/temps réel et texte, basculer sur les dépôts `sam2` / `sam3`.

## Pièges

- **Trois dépôts distincts** : `segment-anything` (SAM 1, images), `sam2` (vidéo), `sam3` (texte/concept) — ne pas confondre les installations ni les poids.
- SAM **ne classe pas** les masques : il segmente, il ne dit pas *quoi*. Le nommage vient d'un autre modèle en amont.
- Encodeur lourd : sur CPU ou petit GPU, latence et mémoire deviennent prohibitives — viser MobileSAM/FastSAM.
- Ambiguïté des invites : un point peut renvoyer plusieurs masques candidats ; gérer le choix du meilleur.

## Alternatives

- [[Dev/Services/Detectron2|Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.

## Liens

- [[Segment Anything (SAM)]] — le concept : segmentation promptable, architecture, lignée SAM/SAM 2/SAM 3.
- [[Segmentation]] — la tâche générale ; SAM en est l'approche fondation / promptable.
- [[Modèles de fondation vision]] — la famille à laquelle SAM appartient.
- [[Dev/Services/supervision|supervision]] — connecteur pour exploiter les masques SAM.
- [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/HuggingFace|HuggingFace]] — exécution et poids/démos.
- Repos : `segment-anything` · `sam2` · `sam3` (Meta AI / facebookresearch).
