---
galaxie: wiki
type: concept
nom: Segment Anything (SAM)
alias: [SAM, Segment Anything Model, segmentation promptable, promptable segmentation, SAM 2, SAM 3, SA-1B]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [segmentation, computer-vision, transformers, deep-learning]
---

# Segment Anything (SAM)

## Aperçu

- **Modèle de fondation pour la segmentation** (Meta AI) : segmente n'importe quel objet **sur invite**, sans réentraînement par classe — capacité **zero-shot**.
- Renverse la logique « un modèle = une tâche fixe » : un encodeur d'image lourd, une **invite** légère (point, boîte, masque, puis texte) → masque.

## Concepts clés

### Segmentation promptable
- L'utilisateur **désigne** l'objet : clic(s), boîte, masque grossier. Le modèle renvoie un ou plusieurs masques candidats avec score. Recadre la segmentation comme une tâche **interactive** et générique.

### Architecture
- **Encodeur d'image** ViT (lourd, calculé une fois par image) + **encodeur d'invite** + **décodeur de masque** léger (rejoué à chaque nouvelle invite). Le coût lourd est amorti sur plusieurs prompts → interactif en temps réel.

### Données — SA-1B
- Entraîné sur **SA-1B** : ~1,1 milliard de masques sur 11 M d'images, annotés en boucle modèle-dans-la-boucle. L'échelle des données fait la généralisation zero-shot.

### Lignée SAM
- **SAM** (2023) : images, invites géométriques (points, boîtes, masques).
- **SAM 2** (2024) : unifie **image + vidéo** avec une mémoire qui suit l'objet à travers les images (occlusions, identité).
- **SAM 3** (2025) : ajoute les **invites texte / concept** (open-vocabulary) — détecte, segmente et suit *toutes* les instances d'un concept nommé ; **SAM 3.1** affine la vidéo temps réel.

## Les maths, simplement

- Pas de perte « phare » nouvelle : entraînement par combinaison [[Cross-entropy|focal / cross-entropy]] + **Dice** sur les masques. Gestion de l'ambiguïté : le modèle prédit plusieurs masques et n'est pénalisé que sur le meilleur. Évaluation par IoU ([[Métriques vision]]).

## En pratique

- Usage type : **annotation assistée** (pré-segmenter pour accélérer le labelling), masques zero-shot, brique d'un pipeline plus large.
- Pas toujours le bon choix : pour une classe fixe et une latence serrée, un [[Segmentation|U-Net / DeepLab]] dédié reste plus léger et plus précis sur son domaine.
- Écosystème : code et poids officiels [[Dev/Services/segment-anything|segment-anything]] ; poids et démos [[Dev/Services/HuggingFace|HuggingFace]] / [[Dev/Services/PyTorch|PyTorch]] ; variantes rapides (MobileSAM, FastSAM).

## Approches voisines & alternatives

- [[Segmentation]] — la tâche générale ; SAM en est l'approche **fondation / promptable**.
- [[Vision Language Models]] — autre fondation multimodale ; SAM 3 rejoint le texte-vers-masque.
- [[Métriques vision]] — IoU / Dice pour juger les masques.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Kirillov et al. (2023) — *Segment Anything* (SAM, SA-1B).
- Ravi et al. (2024) — *SAM 2* (vidéo) · Meta AI (2025) — *SAM 3* (concepts / texte).
