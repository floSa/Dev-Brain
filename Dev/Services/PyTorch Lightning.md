---
galaxie: dev
type: service
nom: PyTorch Lightning
alias: [pytorch-lightning, lightning, pl, lightning ai, fabric]
pitch: "Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Keras|Keras]]", "[[Dev/Services/accelerate|accelerate]]", "[[Dev/Services/DeepSpeed|DeepSpeed]]"]
remplace_par: []
status: actif
tags: [deep-learning, gpu, distributed]
url_docs: https://lightning.ai/docs/pytorch/stable/
url_repo: https://github.com/Lightning-AI/pytorch-lightning
---

# PyTorch Lightning

## Pourquoi

Surcouche d'**organisation de code [[Dev/Services/PyTorch|PyTorch]]** : on garde son `nn.Module`, mais la logique se range dans un `LightningModule` (`training_step`, `validation_step`, configuration des optimiseurs) et le `Trainer` prend en charge l'ingénierie répétitive — boucle d'entraînement, déplacement sur GPU, accumulation de gradients, mixed precision, checkpointing, logging, early stopping. Objectif : **découpler la recherche de l'ingénierie** pour des runs lisibles et reproductibles. Le projet fournit aussi **Fabric**, une variante bas niveau qui ajoute le scaling à une boucle PyTorch existante sans imposer la structure du Trainer.

## Quand l'utiliser

- Entraîner des modèles PyTorch **sans réécrire la plomberie** (multi-GPU, multi-nœuds, TPU, AMP) — « zero code change » pour passer d'un GPU à plusieurs.
- Standardiser des **expériences reproductibles** (seed, checkpoints, logs) en équipe ou sur la durée.
- Garder PyTorch pur tout en factorisant le boilerplate → `LightningModule` + `Trainer`.
- Besoin de scaling **sans** la structure imposée → **Fabric**.

## Quand NE PAS l'utiliser

- Portabilité multi-backend (JAX / TF / PyTorch) → [[Dev/Services/Keras|Keras]] (Lightning est **PyTorch uniquement**).
- Contrôle total d'une boucle d'entraînement très spécifique → PyTorch nu, ou Fabric (moins d'abstraction).
- Hors deep learning (tabulaire, ML classique) → [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add pytorch-lightning` (ou le méta-paquet `lightning`). Rien à héberger.
- S'appuie sur [[Dev/Services/PyTorch|PyTorch]] : suit ses devices (CUDA, ROCm, MPS) et ses stratégies distribuées (DDP, FSDP, DeepSpeed).
- Maintenue par **Lightning AI** (créateurs du projet).

## Pièges

- Deux paquets coexistent : `pytorch-lightning` (historique mais maintenu) et `lightning` (méta-paquet) — choisir et s'y tenir, les imports diffèrent.
- L'abstraction du `Trainer` masque la boucle : un comportement custom passe par des **hooks** / callbacks qu'il faut connaître pour ne pas se battre contre le framework.
- API qui évolue entre versions majeures : épingler la version, lire les notes de migration.

## Alternatives

- [[Dev/Services/Keras|Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework.
- [[Dev/Services/accelerate|accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.
- [[Dev/Services/DeepSpeed|DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.

Nuance : Keras est **multi-backend** et fournit l'API de définition du modèle ; Lightning reste **PyTorch** et n'organise que l'entraînement (on écrit toujours son `nn.Module`). Face à **accelerate**, le partage est inverse : Lightning **impose une structure** (`LightningModule` + `Trainer`) là où accelerate reste bas niveau ; son pendant direct est **Fabric**. **DeepSpeed** n'est pas un concurrent mais un **backend** : Lightning sait l'activer comme stratégie (`strategy="deepspeed"`) pour le sharding ZeRO.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — le framework dont Lightning organise le code.
- [[Dev/Services/HuggingFace|HuggingFace]] — son `Trainer` maison est un concurrent pour les transformeurs ; Lightning reste plus général.
- Doc : https://lightning.ai/docs/pytorch/stable/
