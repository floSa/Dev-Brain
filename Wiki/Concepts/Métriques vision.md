---
galaxie: wiki
type: concept
nom: Métriques vision
alias: [métriques de vision, vision metrics, mAP, mean average precision, IoU, intersection over union, Dice, mIoU, AP]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [model-evaluation, object-detection, segmentation, computer-vision]
---

# Métriques vision

## Aperçu

- Comment **noter** détection et segmentation, là où l'accuracy de classification ne suffit plus : il faut mesurer un **recouvrement spatial**.
- Brique commune : l'**IoU**. De là dérivent mAP (détection) et Dice / mIoU (segmentation).

## Concepts clés

### IoU (Intersection over Union)
- Recouvrement prédiction / vérité terrain : aire de l'intersection / aire de l'union. Vaut 1 si parfait, 0 si disjoint. Sert de **critère de réussite** : une boîte ou un masque est « bon » si IoU > seuil (p. ex. 0,5).

### AP et mAP (détection)
- Pour une classe : on trie les détections par confiance, on trace la courbe **précision-rappel**, l'**AP** = aire sous cette courbe. **mAP** = moyenne des AP sur les classes.
- Conventions : **mAP@0.5** (PASCAL VOC) ou **mAP@[.5:.95]** (COCO, moyennée sur 10 seuils d'IoU — bien plus exigeante).

### Dice & mIoU (segmentation)
- **Dice** (= F1 des pixels) et **IoU** mesurent le recouvrement des masques. **mIoU** = IoU moyenné sur les classes (métrique reine en sémantique). Dice pénalise moins les petits objets, d'où son usage en imagerie médicale.

## Les maths, simplement

- $\text{IoU}=\dfrac{|A\cap B|}{|A\cup B|}$ ; $\text{Dice}=\dfrac{2|A\cap B|}{|A|+|B|}$. Lien : $\text{Dice}=\dfrac{2\,\text{IoU}}{1+\text{IoU}}$ (donc Dice $\ge$ IoU).
- $\text{AP}=\int_0^1 p(r)\,dr$ (aire sous précision-rappel) ; $\text{mAP}=\dfrac{1}{C}\sum_c \text{AP}_c$.

## En pratique

- **Détection** : rapporter mAP@[.5:.95] (COCO). Le seuil d'IoU du NMS et celui du matching prédiction/vérité sont distincts — ne pas les confondre.
- **Segmentation** : mIoU en sémantique, Dice en médical, AP de masque en instance (COCO mask AP).
- Lien classification : ces métriques **complètent** les [[Classification metrics|métriques de classification]] (qui jugent l'étiquette, pas la localisation).

## Approches voisines & alternatives

- [[Classification metrics]] — l'équivalent côté étiquette (précision, rappel, F1) ; mAP réutilise la courbe précision-rappel.
- [[Détection d'objets]] — produit ce que mAP évalue.
- [[Segmentation]] — produit ce que mIoU / Dice évaluent.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Everingham et al. (2010) — PASCAL VOC (mAP@0.5).
- Lin et al. (2014) — MS COCO (mAP@[.5:.95], mask AP).
