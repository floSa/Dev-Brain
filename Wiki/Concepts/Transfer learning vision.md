---
galaxie: wiki
type: concept
nom: Transfer learning vision
alias: [transfer learning, transfert d'apprentissage, fine-tuning vision, feature extraction, backbone gelé]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [transfer-learning, fine-tuning, computer-vision, deep-learning]
---

# Transfer learning vision

## Aperçu

- Réutiliser un modèle **pré-entraîné** sur un grand jeu (ImageNet) comme point de départ d'une tâche cible, au lieu d'entraîner de zéro.
- Gain massif quand les données étiquetées sont rares : les premières couches (bords, textures) sont quasi universelles et se transfèrent presque telles quelles.

## Concepts clés

### Deux régimes
- **Extraction de features** : on **gèle** le backbone et on n'entraîne qu'une tête (classifieur) neuve. Rapide, peu de données, peu de risque de surapprentissage.
- **Fine-tuning** : on **dégèle** tout ou partie du backbone et on ré-entraîne à **faible** taux d'apprentissage. Plus performant si assez de données, mais plus coûteux et plus risqué.

### Quoi dégeler, à quel rythme
- Heuristique : geler les couches basses (génériques), affiner les hautes (spécifiques). **Taux d'apprentissage différentiels** (discriminatifs) : plus faible en bas qu'en haut (cf. [[Learning rate schedules|plannings de LR]]).
- Plus le domaine cible est proche d'ImageNet, moins il faut dégeler.

### Pièges
- **Fuite de données** ([[Data leakage]]) si la normalisation/les stats sont calculées avant le split, ou si le pré-entraînement a déjà vu les données de test.
- Oublier d'aligner le **prétraitement** (normalisation, taille d'entrée) sur celui du pré-entraînement.
- *Catastrophic forgetting* si le LR sur le backbone est trop grand.

## Les maths, simplement

- On initialise $\theta = \theta_{\text{pré}}$ et on minimise la perte cible ; en extraction, $\theta_{\text{backbone}}$ est figé et seul $\theta_{\text{tête}}$ évolue.
- LR discriminatif : couche $l$ entraînée avec $\eta_l = \eta \cdot \rho^{\,L-l}$, $\rho < 1$ — décroît vers les couches basses.

## En pratique

- Défaut raisonnable : extraction de features d'abord (baseline rapide), puis fine-tuning si le budget data le permet.
- Coupler systématiquement avec l'[[Augmentation d'images|augmentation]] pour limiter le surapprentissage sur petit jeu.
- Backbones via [[Architectures CNN|architectures CNN]] (ou [[Vision Transformers (ViT)|ViT]]) pré-entraînés, voire des [[Modèles de fondation vision|modèles de fondation]] (CLIP, DINOv2) gelés ; backbones pré-entraînés via [[Dev/Services/timm|timm]] / [[Dev/Services/torchvision|torchvision]], écosystème [[Dev/Services/HuggingFace|HuggingFace]] / [[Dev/Services/PyTorch|PyTorch]].

## Approches voisines & alternatives

- [[PEFT]] / [[SFT]] — les analogues côté LLM (LoRA/adapters, fine-tuning supervisé) : même idée, autre modalité.
- [[Distillation]] — transférer le savoir d'un gros modèle vers un petit, complémentaire du transfert de poids.
- [[Architectures CNN]] / [[CNN]] — ce que l'on transfère ; [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Yosinski et al. (2014) — *How transferable are features in deep neural networks?*
- Howard & Ruder (2018) — *ULMFiT* (LR discriminatifs, dégel progressif).
- Kornblith et al. (2019) — *Do Better ImageNet Models Transfer Better?*
