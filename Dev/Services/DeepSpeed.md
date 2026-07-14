---
galaxie: dev
type: service
nom: DeepSpeed
alias: [deepspeed, ds, ZeRO, DeepSpeed-Inference]
pitch: "Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/accelerate|accelerate]]", "[[Dev/Services/PyTorch Lightning|PyTorch Lightning]]"]
remplace_par: []
status: actif
tags: [distributed-training, memory-optimization, deep-learning, gpu, mixed-precision]
url_docs: https://www.deepspeed.ai/
url_repo: https://github.com/deepspeedai/DeepSpeed
---

# DeepSpeed

## Pourquoi

Bibliothèque d'optimisation de deep learning de Microsoft, taillée pour les modèles que la VRAM d'un GPU ne peut pas contenir. Son cœur est **ZeRO** (*Zero Redundancy Optimizer*) : au lieu de répliquer tout l'état d'entraînement sur chaque GPU comme le data parallel classique, ZeRO le **shardle** entre les cartes — étape 1 = états de l'optimiseur, 2 = + gradients, 3 = + paramètres — et reconstruit à la volée par communication. S'y ajoutent l'**offload** des états vers la RAM CPU ou le NVMe (ZeRO-Infinity), le **3D-parallelism** (données × pipeline × tenseur), la précision mixte (fp16/bf16) et un moteur d'inférence optimisé. S'intègre à [[Dev/Services/PyTorch|PyTorch]] avec une intrusion minimale (`deepspeed.initialize`) et se pilote par un fichier de config JSON.

## Quand l'utiliser

- **Entraîner / fine-tuner un gros modèle** (LLM, plusieurs milliards de paramètres) qui ne tient pas sur un GPU → ZeRO-2/3.
- **Repousser la limite mémoire** sans ajouter de GPU : offload des états vers CPU/NVMe (ZeRO-Infinity).
- Combiner plusieurs axes de parallélisme (tenseur + pipeline + données) sur un cluster multi-nœuds.
- Cf. le concept [[Entraînement distribué]] pour situer ZeRO face à DDP et FSDP.

## Quand NE PAS l'utiliser

- Le modèle tient sur un GPU → DDP natif suffit, ZeRO ajoute de la communication pour rien.
- On veut surtout **distribuer une boucle existante** sans gérer la config DeepSpeed → [[Dev/Services/accelerate|accelerate]] (qui sait piloter DeepSpeed) ou le sharding natif **FSDP** de [[Dev/Services/PyTorch|PyTorch]].
- On cherche une **structure d'entraînement** complète (Trainer, callbacks) → [[Dev/Services/PyTorch Lightning|PyTorch Lightning]].

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add deepspeed`. Rien à héberger ; coût = l'infra GPU/cluster.
- S'appuie sur PyTorch et NCCL ; certaines features (kernels fusionnés, offload NVMe) compilent des extensions CUDA à l'installation.
- Souvent consommé **indirectement** : `accelerate` et le `Trainer` de [[Dev/Services/HuggingFace|HuggingFace]] exposent DeepSpeed via une simple config.

## Pièges

- La **config JSON** est vaste et capricieuse : un réglage ZeRO/offload incohérent → OOM ou blocage NCCL silencieux.
- Compilation des **extensions CUDA** sensible à la version de CUDA/compilateur ; échecs d'install fréquents si l'environnement n'est pas aligné.
- ZeRO-3 et FSDP couvrent le même besoin : empiler les deux ou mélanger leurs conventions de wrapping/upcasting fp32 mène à des bugs subtils.
- Offload CPU/NVMe = gros gain mémoire mais **forte pénalité de débit** : à mesurer, pas à activer par défaut.

## Alternatives

- [[Dev/Services/accelerate|accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.
- [[Dev/Services/PyTorch Lightning|PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.

Nuance : DeepSpeed est le **moteur** d'optimisation mémoire (ZeRO) ; accelerate et Lightning sont des **surcouches** qui savent l'orchestrer. On les combine plus souvent qu'on ne les oppose — DeepSpeed seul quand on veut le contrôle fin de ZeRO/offload, via accelerate/Lightning quand on veut l'activer sans quitter sa boucle.

## Liens

- [[Entraînement distribué]] — ZeRO, sharding des états, 3D-parallelism que DeepSpeed implémente.
- [[Mixed precision]] — fp16/bf16 quasi systématiques avec ZeRO.
- [[Dev/Services/PyTorch|PyTorch]] — framework sous-jacent (FSDP en est l'équivalent natif de ZeRO-3).
- [[Dev/Services/accelerate|accelerate]], [[Dev/Services/HuggingFace|HuggingFace]] — exposent DeepSpeed par config.
- Doc : https://www.deepspeed.ai/
