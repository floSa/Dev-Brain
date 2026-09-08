---
role: brique
nom: accelerate
alias: [hf accelerate, huggingface accelerate, 🤗 accelerate]
pitch: "Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyTorch Lightning]]", "[[DeepSpeed]]"]
complements: ["[[PyTorch]]"]
tags: [distributed-training, mixed-precision, gpu, deep-learning]
url_docs: https://huggingface.co/docs/accelerate
url_repo: https://github.com/huggingface/accelerate
---

# accelerate

<!-- AUTO:BANDEAU:START -->
> Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-11 |
<!-- AUTO:BANDEAU:END -->

## Définition

La colle entre une boucle [[PyTorch]] et n'importe quel backend distribué. On garde sa boucle d'entraînement standard ; `Accelerator()` enveloppe modèle, optimiseur et dataloader, et le **même script** tourne ensuite sur un GPU, plusieurs GPU, plusieurs nœuds ou un TPU, sans code spécifique au device. Sous le capot, accelerate unifie DDP, **FSDP**, **DeepSpeed** (ZeRO, offload CPU), Megatron-LM et XLA, plus la précision mixte automatique (fp16, bf16, jusqu'à fp8). C'est le moteur d'entraînement sous le `Trainer` de `transformers`. Ce que l'abstraction ne fait pas disparaître, c'est le **multi-process** : journaliser et sauvegarder doivent rester réservés au process principal (`is_main_process`), sinon doublons et checkpoints corrompus ; et une métrique se calcule après `gather` ou `reduce`, faute de quoi chaque shard rapporte sa valeur partielle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Distribuer une boucle PyTorch existante (multi-GPU, multi-nœuds) sans la réécrire ni adopter un framework complet | On veut une structure complète d'entraînement — Trainer, callbacks, journalisation, checkpointing organisés → [[PyTorch Lightning]] |
| Précision mixte sans gérer `autocast` ni `GradScaler` à la main | Entraînement mono-GPU simple sans contrainte mémoire : `torch.amp` natif suffit, accelerate ajoute peu → [[PyTorch]] |
| Gros modèles : activer FSDP ou [[DeepSpeed]] ZeRO-3 par configuration, sans changer le code du modèle | Hors PyTorch (JAX, TensorFlow) : accelerate est centré PyTorch → [[JAX]], [[TensorFlow]] |
| Socle du fine-tuning `transformers` et `PEFT` | |

## Mise en œuvre

- Installation — `uv add accelerate` ; DeepSpeed et Megatron-LM sont des intégrations optionnelles, à installer à part
- Point d'entrée — `Accelerator()` dans la boucle, puis `accelerate config` pour générer le fichier de lancement et `accelerate launch` pour orchestrer les process
- Prérequis — [[PyTorch]] et ses backends distribués (`torch.distributed`, NCCL) ; une config dont le nombre de process ne correspond pas aux GPU réels donne un blocage NCCL ou un OOM silencieux
- Exécution — du laptop au cluster multi-nœuds, sans changer le script ; FSDP et DeepSpeed diffèrent sur le wrapping et l'upcasting fp32, alignement à vérifier
- Coût — gratuit, Apache-2.0 ; aucun service ajouté, le coût est l'infrastructure GPU

## Écosystème

### Alternatives

- [[PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.
- [[DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.

### Compléments

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche. — le framework dont accelerate distribue la boucle.

## Ressources

- Documentation — https://huggingface.co/docs/accelerate
- Dépôt — https://github.com/huggingface/accelerate

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[Entraînement distribué]] — DDP, FSDP, ZeRO et les parallélismes qu'accelerate expose
- [[Mixed precision]] — fp16, bf16 et fp8, gérés automatiquement
- [[HuggingFace]] — bibliothèque sœur ; moteur sous le `Trainer` de `transformers`
- [[datasets]] — la source de données de l'entraînement
