---
galaxie: wiki
type: concept
nom: Estimation de pose
alias: [pose estimation, keypoints, points-clés, pose humaine, OpenPose, HRNet, ViTPose, MediaPipe, OKS, PCK, heatmap]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [pose-estimation, computer-vision, deep-learning]
---

# Estimation de pose

## Aperçu

- Localiser des **points-clés** (keypoints) — articulations d'un corps, doigts d'une main, repères d'un visage — pour reconstruire une **pose** (le squelette).
- Sortie = une liste de coordonnées $(x, y)$ (2D) ou $(x, y, z)$ (3D) par point, souvent avec un score de visibilité.

## Concepts clés

### Top-down vs bottom-up
- **Top-down** : un [[Détection d'objets|détecteur]] localise d'abord chaque personne, puis on estime les keypoints dans chaque boîte. Précis ; coût ∝ nombre de personnes (HRNet, ViTPose, AlphaPose).
- **Bottom-up** : détecter tous les keypoints de l'image, puis les **grouper** par personne. Coût quasi constant, robuste en foule. OpenPose le fait via les *Part Affinity Fields* (champs d'orientation entre articulations).

### Régression par heatmaps
- Approche dominante : prédire une **carte de chaleur** par keypoint (gaussienne centrée sur la position attendue) ; la position = l'argmax (ou soft-argmax) de la heatmap. Plus stable que régresser directement les coordonnées.

### Au-delà du corps 2D
- **3D pose** (lever l'ambiguïté de profondeur), **mains / visage** (MediaPipe), **pose animale** (DeepLabCut), **DensePose** (correspondance dense surface 3D ↔ pixels).

### Évaluation
- **OKS** (Object Keypoint Similarity) : l'analogue de l'[[Métriques vision|IoU]] pour les keypoints, normalisé par l'échelle de la personne ; sert à calculer une AP « keypoints » (COCO). **PCK** : proportion de points sous un seuil de distance.

## Les maths, simplement

- OKS : $\text{OKS}=\dfrac{\sum_i \exp\!\left(-d_i^2 / 2s^2k_i^2\right)\,\delta(v_i>0)}{\sum_i \delta(v_i>0)}$ — $d_i$ distance prédiction/vérité du point $i$, $s$ l'échelle de l'objet, $k_i$ une tolérance par type d'articulation, $v_i$ la visibilité. Vaut ~1 si tous les points tombent juste.
- Heatmap : cible = gaussienne 2D autour de la vérité ; perte = MSE pixel à pixel ; prédiction = $\arg\max$ de la carte.

## En pratique

- Pile usuelle : **YOLO-pose** ou **MediaPipe** (temps réel, edge), **HRNet / ViTPose** (priorité précision, top-down).
- Backbone pré-entraîné + [[Transfer learning vision|fine-tuning]] ; attention à transformer aussi les keypoints lors de l'[[Augmentation d'images|augmentation]] (un flip horizontal échange gauche/droite).
- Usages : analyse sportive / biomécanique, AR, reconnaissance de gestes et d'actions, détection de chute.

## Approches voisines & alternatives

- [[Détection d'objets]] — l'étage amont du pipeline top-down (détecter la personne avant ses keypoints).
- [[Suivi d'objets]] — suivre une pose dans le temps (pose tracking) = estimation par frame + association.
- [[Segmentation]] — autre tâche dense ; DensePose relie pose et surface du corps.
- [[Métriques vision]] — OKS prolonge l'IoU au cas des points-clés.
- [[Vision par ordinateur]] / [[CNN]] — le cadre et les backbones.

## Pour aller plus loin

- Cao et al. (2017) — *OpenPose* (Part Affinity Fields, bottom-up).
- Sun et al. (2019) — *HRNet* (hautes résolutions parallèles) · Xu et al. (2022) — *ViTPose*.
