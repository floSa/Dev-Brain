---
role: brique
nom: PyTorch Lightning
alias: [pytorch-lightning, lightning, pl, lightning ai, fabric]
pitch: "Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Keras]]", "[[accelerate]]", "[[DeepSpeed]]"]
complements: ["[[PyTorch]]"]
tags: [deep-learning, gpu, distributed]
url_docs: https://lightning.ai/docs/pytorch/stable/
url_repo: https://github.com/Lightning-AI/pytorch-lightning
---

# PyTorch Lightning

<!-- AUTO:BANDEAU:START -->
> Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Une organisation imposée au code [[PyTorch]] : on garde son `nn.Module`, mais la logique se range dans un `LightningModule` (`training_step`, `validation_step`, configuration des optimiseurs) et le `Trainer` prend en charge l'ingénierie répétitive — boucle, déplacement sur GPU, accumulation de gradients, précision mixte, checkpointing, journalisation, early stopping. L'objectif est de découpler la recherche de l'ingénierie, pour des runs lisibles et reproductibles. La contrepartie est que le `Trainer` **masque la boucle** : tout comportement particulier passe par des hooks et des callbacks qu'il faut connaître, sous peine de se battre contre le framework. Le projet fournit pour cela **Fabric**, une variante bas niveau qui ajoute le scaling à une boucle existante sans imposer la structure du Trainer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Entraîner des modèles PyTorch sans réécrire la plomberie : multi-GPU, multi-nœuds, TPU, AMP, sans changer le code | Portabilité multi-backend (JAX, TensorFlow, PyTorch) → [[Keras]] : Lightning est **PyTorch uniquement**, et n'écrit pas le modèle à votre place |
| Standardiser des expériences reproductibles — seed, checkpoints, logs — en équipe ou sur la durée | Scaling minimal-intrusif, sans structure imposée, ou contrôle total de la boucle → [[accelerate]], [[PyTorch]] nu, ou **Fabric** |
| Garder PyTorch pur tout en factorisant le boilerplate : `LightningModule` plus `Trainer` | Sharding ZeRO et offload CPU/NVMe pour un modèle qui ne tient pas en VRAM → [[DeepSpeed]], que le Trainer sait d'ailleurs activer (`strategy="deepspeed"`) plutôt que remplacer |
| Besoin de scaling **sans** la structure imposée → Fabric, du même projet | Hors deep learning (tabulaire, ML classique) → [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add pytorch-lightning`, ou le méta-paquet `lightning` : les deux coexistent, les imports diffèrent, choisir et s'y tenir
- Point d'entrée — import Python : `LightningModule` pour le modèle, `Trainer` pour l'exécution
- Prérequis — [[PyTorch]] et ses devices (CUDA, ROCm, MPS) ; l'API évolue entre versions majeures, épingler la version et lire les notes de migration
- Exécution — dans le process appelant ; stratégies distribuées déléguées à PyTorch (DDP, FSDP, DeepSpeed)
- Coût — gratuit, Apache-2.0 ; maintenue par Lightning AI, les créateurs du projet

## Écosystème

### Alternatives

- [[Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework.
- [[accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.
- [[DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.

### Compléments

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche. — le framework dont Lightning organise le code.

## Ressources

- Documentation — https://lightning.ai/docs/pytorch/stable/
- Dépôt — https://github.com/Lightning-AI/pytorch-lightning

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[HuggingFace]] — son `Trainer` maison couvre le même besoin pour les transformeurs ; Lightning reste plus général
