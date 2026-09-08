---
role: brique
nom: DeepSpeed
alias: [deepspeed, ds, ZeRO, DeepSpeed-Inference]
pitch: "Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[accelerate]]", "[[PyTorch Lightning]]"]
complements: ["[[PyTorch]]"]
tags: [distributed-training, memory-optimization, deep-learning, gpu, mixed-precision]
url_docs: https://www.deepspeed.ai/
url_repo: https://github.com/deepspeedai/DeepSpeed
---

# DeepSpeed

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-27 |
<!-- AUTO:BANDEAU:END -->

## Définition

Une boîte à outils pour les modèles que la VRAM d'un GPU ne peut pas contenir. Son cœur est **ZeRO** (*Zero Redundancy Optimizer*) : au lieu de répliquer tout l'état d'entraînement sur chaque carte comme le data parallel classique, ZeRO le **shardle** — étape 1, les états de l'optimiseur ; 2, plus les gradients ; 3, plus les paramètres — et reconstruit à la volée par communication. S'y ajoutent l'**offload** vers la RAM CPU ou le NVMe (ZeRO-Infinity), le **3D-parallelism** (données × pipeline × tenseur), la précision mixte et un moteur d'inférence optimisé. Deux bornes commandent l'usage : l'offload est un gros gain mémoire contre une **forte pénalité de débit**, à mesurer et non à activer par défaut ; et ZeRO-3 recouvre exactement le besoin de FSDP, l'équivalent natif de [[PyTorch]] — empiler les deux ou mélanger leurs conventions de wrapping et d'upcasting fp32 produit des bugs subtils.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Entraîner ou fine-tuner un gros modèle (LLM, plusieurs milliards de paramètres) qui ne tient pas sur un GPU → ZeRO-2/3 | Le modèle tient sur un GPU : DDP natif suffit, ZeRO ajoute de la communication pour rien → [[PyTorch]] |
| Repousser la limite mémoire sans ajouter de GPU : offload des états vers CPU ou NVMe (ZeRO-Infinity) | On veut surtout distribuer une boucle existante sans gérer la config DeepSpeed → [[accelerate]], qui sait la piloter, ou le FSDP natif de [[PyTorch]] |
| Combiner plusieurs axes de parallélisme — tenseur, pipeline, données — sur un cluster multi-nœuds | On cherche une structure d'entraînement complète (Trainer, callbacks, checkpointing organisé) → [[PyTorch Lightning]] |

## Mise en œuvre

- Installation — `uv add deepspeed` ; certaines fonctions (noyaux fusionnés, offload NVMe) compilent des extensions CUDA, dont l'installation échoue si la version de CUDA ou du compilateur n'est pas alignée
- Point d'entrée — `deepspeed.initialize` dans une boucle PyTorch, piloté par un fichier de **config JSON** ; cette config est vaste et capricieuse, un réglage ZeRO/offload incohérent donne un OOM ou un blocage NCCL silencieux
- Prérequis — [[PyTorch]] et NCCL ; un cluster GPU multi-cartes pour que ZeRO ait un sens
- Exécution — distribuée, multi-GPU et multi-nœuds ; souvent consommée **indirectement**, `accelerate` et le `Trainer` de [[HuggingFace]] l'exposant par simple config
- Coût — gratuit, MIT ; le coût réel est l'infrastructure GPU

## Écosystème

### Alternatives

- [[accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.
- [[PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.

### Compléments

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche. — le framework sous-jacent, dont FSDP est l'équivalent natif de ZeRO-3.

## Ressources

- Documentation — https://www.deepspeed.ai/
- Dépôt — https://github.com/deepspeedai/DeepSpeed

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[Entraînement distribué]] — ZeRO, sharding des états et 3D-parallelism, que DeepSpeed implémente
- [[Mixed precision]] — fp16/bf16, quasi systématiques avec ZeRO
- [[HuggingFace]] — expose DeepSpeed par config depuis son `Trainer`
