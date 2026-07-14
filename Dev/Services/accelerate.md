---
galaxie: dev
type: service
nom: accelerate
alias: [hf accelerate, huggingface accelerate, 🤗 accelerate]
pitch: "Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config."
categorie: ml/training
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/PyTorch Lightning|PyTorch Lightning]]", "[[Dev/Services/DeepSpeed|DeepSpeed]]"]
remplace_par: []
status: actif
tags: [distributed-training, mixed-precision, gpu, deep-learning]
url_docs: https://huggingface.co/docs/accelerate
url_repo: https://github.com/huggingface/accelerate
---

# accelerate

## Pourquoi

Bibliothèque de l'écosystème [[Dev/Services/HuggingFace|HuggingFace]] qui sert de **colle entre une boucle [[Dev/Services/PyTorch|PyTorch]] et tout backend distribué**. On garde sa boucle d'entraînement standard ; `Accelerator()` enveloppe modèle, optimiseur et dataloader, et le **même script** tourne ensuite sur un GPU, plusieurs GPU, plusieurs nœuds ou un TPU, sans code spécifique au device. Sous le capot, accelerate unifie DDP, **FSDP**, **DeepSpeed** (ZeRO, offload CPU), Megatron-LM et XLA, plus la **précision mixte** automatique (fp16/bf16, jusqu'à fp8). `accelerate config` génère le fichier de lancement, `accelerate launch` orchestre les processus. C'est le moteur d'entraînement sous le `Trainer` de `transformers`.

## Quand l'utiliser

- **Distribuer une boucle PyTorch existante** (multi-GPU, multi-nœuds) sans la réécrire ni adopter un framework complet.
- **Précision mixte** sans gérer `autocast`/`GradScaler` à la main.
- **Gros modèles** : activer FSDP ou DeepSpeed ZeRO-3 par configuration, sans changer le code du modèle.
- Socle du fine-tuning `transformers` / `PEFT` ([[Dev/Services/HuggingFace|HuggingFace]]).

## Quand NE PAS l'utiliser

- On veut une **structure complète** d'entraînement (Trainer, callbacks, logging, checkpointing organisés) → [[Dev/Services/PyTorch Lightning|PyTorch Lightning]].
- Entraînement mono-GPU simple sans contrainte mémoire : `torch.amp` natif suffit, accelerate ajoute peu.
- Hors PyTorch (JAX/TF) : accelerate est centré PyTorch.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add accelerate`. Rien à héberger.
- S'appuie sur [[Dev/Services/PyTorch|PyTorch]] et ses backends distribués (`torch.distributed`, NCCL).
- DeepSpeed et Megatron-LM sont des intégrations optionnelles (paquets à installer).
- Coût = l'infra GPU/cluster sous-jacente ; accelerate n'ajoute aucun service.

## Pièges

- `accelerate config` mal réglé (nombre de process ≠ GPU réels) → blocages NCCL ou OOM silencieux.
- En multi-process, journaliser et sauvegarder **uniquement sur le process principal** (`is_main_process`), sinon doublons et corruptions de checkpoint.
- FSDP vs DeepSpeed : conventions de wrapping et d'upcasting fp32 différentes ; vérifier l'alignement de la précision mixte entre les deux.
- `gather`/`reduce` oubliés au moment de calculer une métrique → valeurs partielles par shard.

## Alternatives

- [[Dev/Services/PyTorch Lightning|PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.
- [[Dev/Services/DeepSpeed|DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.

Nuance : accelerate est **bas niveau** (on garde sa boucle, scaling minimal-intrusif) ; Lightning **impose une structure** (`LightningModule` + `Trainer`). Le pendant direct d'accelerate côté Lightning est **Fabric**. Face à **DeepSpeed**, le partage est différent : DeepSpeed est le **moteur** d'optimisation mémoire (ZeRO/offload) qu'accelerate sait justement activer par config — on les combine plus qu'on ne les oppose.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — le framework dont accelerate distribue la boucle (`torch.distributed`, DDP, FSDP).
- [[Dev/Services/HuggingFace|HuggingFace]] — bibliothèque sœur ; moteur sous le `Trainer` de `transformers`.
- [[Dev/Services/datasets|datasets]] — source de données de l'entraînement.
- [[Entraînement distribué]] — DDP, FSDP, ZeRO et parallélismes qu'accelerate expose.
- [[Mixed precision]] — fp16/bf16/fp8 gérés automatiquement.
- Doc : https://huggingface.co/docs/accelerate
