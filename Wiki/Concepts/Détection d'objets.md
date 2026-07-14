---
galaxie: wiki
type: concept
nom: Détection d'objets
alias: [object detection, détection d'objet, bounding box, boîtes englobantes, anchors, NMS, YOLO, Faster R-CNN, RetinaNet, DETR]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [object-detection, computer-vision, deep-learning]
---

# Détection d'objets

## Aperçu

- Localiser **et** classer chaque objet : sortie = liste de **boîtes englobantes** $(x, y, w, h)$ + classe + score de confiance.
- Deux familles historiques : **deux étages** (proposer des régions puis les classer) et **un étage** (boîtes prédites directement, plus rapide).

## Concepts clés

### Anchors (ancres)
- Boîtes de référence (tailles/ratios prédéfinis) posées en grille ; le réseau prédit un **décalage** par rapport à l'ancre plutôt qu'une boîte absolue. Simplifie l'apprentissage de la localisation. DETR s'en passe (voir plus bas).

### NMS (Non-Maximum Suppression)
- Post-traitement : un même objet déclenche plusieurs boîtes redondantes. On garde la plus confiante et on **supprime celles qui la recouvrent trop** (IoU > seuil). Étape clé, source de réglages et d'erreurs sur objets qui se chevauchent.

### Deux étages vs un étage
- **Deux étages — Faster R-CNN** : un Region Proposal Network propose des régions, une tête les classe et affine. Précis, plus lent.
- **Un étage — YOLO, RetinaNet, SSD** : prédiction dense en une passe. Rapide (temps réel). **RetinaNet** introduit la **focal loss** pour gérer le déséquilibre massif fond/objet.

### Détection par transformer — DETR
- **DETR** pose la détection comme une **prédiction d'ensemble** : un [[Transformer architectures|Transformer]] + un appariement bipartite (algorithme hongrois) entre prédictions et vérité terrain. **Plus d'anchors ni de NMS** — pipeline end-to-end. Élégant mais lent à converger (variantes : Deformable DETR).

### Évaluation
- Métrique reine : **mAP** (mean Average Precision) à différents seuils d'IoU. Détail dans [[Métriques vision]].

## Les maths, simplement

- IoU (recouvrement) : $\text{IoU}=\dfrac{|A\cap B|}{|A\cup B|}$ — sert au NMS et au matching prédiction/vérité.
- Focal loss : $-(1-\hat p)^\gamma \log \hat p$ — le facteur $(1-\hat p)^\gamma$ atténue les exemples faciles (le fond), concentre l'apprentissage sur les durs.

## En pratique

- Choix usuel : **YOLO** (famille très utilisée, temps réel, bon défaut), **Faster R-CNN** (priorité précision), **DETR** (pipeline simple, sans NMS).
- Backbone pré-entraîné + [[Transfer learning vision|fine-tuning]] sur boîtes annotées ; [[Augmentation d'images|augmentation]] adaptée (transformer aussi les boîtes).
- Frameworks : [[Dev/Services/torchvision|torchvision]], [[Dev/Services/Ultralytics YOLO|Ultralytics]] (YOLO), [[Dev/Services/Detectron2|Detectron2]], [[Dev/Services/HuggingFace|HuggingFace]] (DETR) ; outillage des sorties via [[Dev/Services/supervision|supervision]].

## Approches voisines & alternatives

- [[Segmentation]] — un masque au pixel plutôt qu'une boîte ; la segmentation d'instance = détection + masque.
- [[Classification d'images]] — sans localisation, une étiquette globale.
- [[Métriques vision]] — mAP, IoU : le vocabulaire d'évaluation.
- [[Suivi d'objets]] / [[Estimation de pose]] / [[OCR]] / [[Metric learning & ré-identification]] — tâches bâties **sur** la détection (suivi par détection, pose top-down, détection de texte, ré-id de crops).
- [[Vision par ordinateur]] / [[CNN]] — cadre et backbones.

## Pour aller plus loin

- Ren et al. (2015) — Faster R-CNN · Redmon et al. (2016) — YOLO.
- Lin et al. (2017) — RetinaNet / Focal Loss · Carion et al. (2020) — DETR.
