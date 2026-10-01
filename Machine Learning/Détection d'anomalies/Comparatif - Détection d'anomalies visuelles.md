---
role: comparatif
nom: Comparatif - Détection d'anomalies visuelles
categorie: ml/anomalie
tags: [industrial-inspection, computer-vision]
---

# Comparatif - Détection d'anomalies visuelles

> On tranche sur : le point de départ — une bibliothèque qui outille plusieurs méthodes, ou le code d'une méthode précise (banque de mémoire, reconstruction multi-classe, zero-shot).

![[Comparatif - Détection d'anomalies visuelles.base]]

## Ce qui départage

- [[anomalib]] — la seule brique **outil** : une trentaine de modèles sous une CLI et un `Engine`, des chargeurs de jeux (dont un dossier maison) et un export ONNX et OpenVINO. Les trois autres sont le code d'**une** méthode ; les jeux publics qu'il télécharge sont non commerciaux.
- [[patchcore-inspection]] — la référence de la **banque de mémoire** : pas de réseau à entraîner, seulement une banque de patchs réduite par coreset. Dépôt figé depuis mars 2023 ; la mémoire croît avec le nombre d'images de référence.
- [[Dinomaly]] — le **multi-classe** : un seul modèle pour toutes les catégories, encodeur DINOv2 gelé. Le plus fort sur les jeux publics (99,6 % d'AUROC image sur MVTec AD), mais ViT lourd et dépendances anciennes (torch 1.12).
- [[AnomalyCLIP]] — le **zero-shot** : des prompts appris sur un jeu auxiliaire, aucune image de bon de la pièce cible. Plus bas en score (91,5 % sur MVTec AD) ; le statut des poids CLIP pour un usage commercial est à lire avant livraison.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Détection d'anomalies]] — le dossier qui range ces briques et les notions qui les expliquent
