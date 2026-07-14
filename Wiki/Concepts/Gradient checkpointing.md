---
galaxie: wiki
type: concept
nom: Gradient checkpointing
alias: [Gradient checkpointing, activation checkpointing, recomputation, rematerialization, rematérialisation, recalcul d'activations, checkpoint]
categorie: concept/dl
domaines: [ml-eng]
tags: [memory-optimization, deep-learning, gpu]
---

# Gradient checkpointing

## Aperçu

- Échanger du **calcul contre de la mémoire** : au lieu de garder en VRAM toutes les **activations** du forward (nécessaires au backward), on n'en conserve que quelques-unes et on **recalcule** les autres au moment de la rétropropagation.
- Permet d'entraîner des modèles plus profonds ou avec un **batch plus grand** sur une VRAM donnée, au prix d'un forward supplémentaire (~+20-30 % de temps).

## Concepts clés

### Le coût caché des activations
- La rétropropagation a besoin des activations de chaque couche. Les stocker toutes coûte une mémoire **proportionnelle à la profondeur** du réseau — souvent le vrai goulot, devant les poids eux-mêmes.

### Checkpoints & recomputation
- On marque certaines couches comme **checkpoints** : seules leurs sorties sont gardées. Les activations intermédiaires sont **libérées**, puis **recalculées** par un mini-forward local lors du backward de ce segment.

### Le compromis $\sqrt{n}$
- En plaçant les checkpoints tous les $\sqrt{n}$ couches, la mémoire d'activations passe de $O(n)$ à $O(\sqrt{n})$ pour un seul forward supplémentaire — le résultat classique de Chen et al. (2016).

## Les maths, simplement

- Sans checkpointing : mémoire $O(n)$, calcul $1$ forward $+ 1$ backward.
- Avec checkpointing optimal : mémoire $O(\sqrt{n})$, calcul $\approx 2$ forwards $+ 1$ backward. On paie $\sim 33\%$ de compute pour un facteur $\sqrt{n}$ sur la mémoire.

## En pratique

- Levier décisif quand l'erreur est *out-of-memory* alors que le **temps** n'est pas critique — typiquement pour augmenter la longueur de séquence ou le batch.
- Se combine avec [[Mixed precision]] (activations 16 bits) et le sharding de l'[[Entraînement distribué]] (FSDP/ZeRO) : ce sont des leviers **mémoire orthogonaux**, souvent activés ensemble.
- API : envelopper un bloc dans une fonction `checkpoint`, ou activer un drapeau `gradient_checkpointing` dans les surcouches (HuggingFace, Lightning).
- Pièges : incompatible naïvement avec des couches **non déterministes** (Dropout, BatchNorm) si le recalcul ne reproduit pas l'état aléatoire — gérer le RNG ; ralentit l'entraînement, donc inutile si la mémoire n'est pas le facteur limitant.

## Approches voisines & alternatives

- [[Entraînement distribué]] — sharding mémoire (FSDP/ZeRO) ; complémentaire, agit sur les états plutôt que sur les activations.
- [[Mixed precision]] — réduit la taille des activations ; cumulable.
- [[Dev/Services/PyTorch|PyTorch]] — `torch.utils.checkpoint` natif.

## Pour aller plus loin

- Chen et al. (2016) — *Training Deep Nets with Sublinear Memory Cost*.
- Griewank & Walther (2000) — *Revolve* (rematérialisation optimale, fondement théorique).
