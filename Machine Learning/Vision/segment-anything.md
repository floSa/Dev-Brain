---
role: brique
nom: segment-anything
alias: [SAM, Segment Anything Model, sam2, sam3]
pitch: "Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte)."
categorie: ml/vision
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Detectron2]]"]
complements: ["[[supervision]]"]
tags: [segmentation, foundation-model, computer-vision, transformers, deep-learning, gpu]
url_docs: https://segment-anything.com/
url_repo: https://github.com/facebookresearch/segment-anything
---

# segment-anything

<!-- AUTO:BANDEAU:START -->
> Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Dépôt officiel de Meta AI pour le **Segment Anything Model (SAM)** — code d'inférence, poids
pré-entraînés et notebooks. SAM est un modèle de fondation pour la segmentation
**promptable** : à partir d'une invite (point, boîte, masque grossier), il renvoie un masque
**sans réentraînement par classe**, donc en zero-shot. L'architecture tient en deux temps —
un encodeur d'image ViT lourd, calculé une fois, et un décodeur léger rejoué à chaque invite,
ce qui rend l'usage interactif. La lignée s'est prolongée dans des dépôts dédiés : **SAM 2**
pour l'image et la vidéo avec mémoire, **SAM 3** pour les invites texte en vocabulaire ouvert.
SAM segmente mais ne nomme pas : le nommage vient d'un modèle en amont.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Annotation assistée : pré-segmenter pour accélérer le labelling de masques | Trois dépôts distincts — `segment-anything` (images), `sam2` (vidéo), `sam3` (texte) : ne pas confondre les installations ni les poids |
| Masques zero-shot sur des objets quelconques, sans dataset annoté par classe | Une invite est ambiguë par nature : un point peut renvoyer plusieurs masques candidats, et le choix du meilleur reste à gérer |
| Brique d'un pipeline plus large : un détecteur propose des boîtes, SAM en tire les masques | Contraintes mobiles ou temps réel : viser les variantes allégées MobileSAM ou FastSAM plutôt que SAM original |
| Segmentation interactive pilotée par l'utilisateur, au clic ou à la boîte | Le dépôt ne fournit que l'inférence : aucun code d'entraînement |

## Mise en œuvre

- Installation — `pip install` depuis les sources du dépôt ; poids ViT-B, ViT-L ou ViT-H à télécharger à part
- Point d'entrée — `SamPredictor` (invite par invite) ou `SamAutomaticMaskGenerator` en Python
- Prérequis — PyTorch et un GPU : l'encodeur ViT est gourmand en VRAM
- Exécution — single-node, inférence seule ; pour la vidéo ou le texte, basculer sur les dépôts `sam2` et `sam3`
- Coût — Apache-2.0 pour le code comme pour les poids ; rien à héberger

## Écosystème

### Alternatives

- [[Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture.

### Compléments

- [[supervision]] — Boîte à outils CV model-agnostic de Roboflow — API Detections unifiée, annotateurs, suivi (ByteTrack), zones et comptage qui se branchent sur n'importe quel modèle (YOLO, Detectron2, SAM, Transformers) ; la colle entre un détecteur et une application. — le connecteur qui exploite les masques SAM en aval

## Ressources

- Documentation — https://segment-anything.com/
- Dépôt — https://github.com/facebookresearch/segment-anything

## Voir aussi

- [[Segment Anything (SAM)]] — la notion : segmentation promptable, architecture, lignée SAM / SAM 2 / SAM 3
- [[Segmentation]] — la tâche générale, dont SAM est l'approche promptable
- [[Modèles de fondation vision]] — la famille à laquelle SAM appartient
- [[Comparatif - Détection & segmentation]] — ce qui départage les briques du dossier
- [[PyTorch]], [[HuggingFace]] — l'exécution, les poids et les démos
