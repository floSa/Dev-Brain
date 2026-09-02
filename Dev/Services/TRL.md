---
role: brique
nom: TRL
alias: [trl, transformer reinforcement learning, transformers reinforcement learning, SFTTrainer, DPOTrainer, GRPOTrainer]
pitch: "Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code."
categorie: llm/finetuning
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Unsloth]]", "[[Axolotl]]", "[[LLaMA-Factory]]", "[[Tunix]]"]
complements: []
tags: [fine-tuning, alignment, reinforcement-learning, transformers, llm]
url_docs: https://huggingface.co/docs/trl
url_repo: https://github.com/huggingface/trl
---

# TRL

## Pourquoi

TRL (*Transformer Reinforcement Learning*) est la bibliothèque de **post-training** de Hugging Face : une pile unifiée de *trainers* qui couvrent toutes les étapes après le pré-entraînement. Chaque méthode a sa classe, calquée sur le `Trainer` de [[HuggingFace]] : `SFTTrainer` ([[SFT]]), `RewardTrainer` ([[Reward modeling]]), `DPOTrainer` ([[RLHF and DPO]]), `GRPOTrainer` (le GRPO de DeepSeek-R1, plus économe que PPO) et `PPOTrainer`. C'est le **niveau code** du fine-tuning : on écrit du Python, on contrôle finement la boucle, et c'est la brique sur laquelle reposent la plupart des outils config-driven du domaine. Intégration native avec `transformers`, `peft` ([[PEFT]] : LoRA/QLoRA), `accelerate` et [[PyTorch]].

## Quand l'utiliser

- **Aligner un LLM** par préférences : DPO, GRPO, ou le pipeline RLHF complet (reward model + PPO).
- **Fine-tuner par code**, avec contrôle sur la boucle, la loss, le data collator, les callbacks.
- Travailler déjà dans l'écosystème [[HuggingFace]] (`transformers` + `datasets` + `peft`).
- Implémenter une méthode récente (GRPO, KTO, ORPO…) sans attendre qu'un wrapper la supporte.

## Quand NE PAS l'utiliser

- On veut **ne pas écrire de code** et tout piloter par fichier → [[Axolotl]] (YAML) ou [[LLaMA-Factory]] (YAML / CLI / web).
- On vise surtout la **vitesse et la VRAM** sur un seul GPU → [[Unsloth]] (qui patche justement les trainers TRL).
- Entraînement de zéro d'une architecture sur mesure → [[PyTorch]] directement.
- Stack **JAX / TPU** → [[Tunix]], le pendant JAX de TRL.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add trl`. Rien à héberger ; coût = l'infra GPU.
- Distribuée via `accelerate` (multi-GPU, multi-nœuds) et compatible [[DeepSpeed]] (ZeRO) pour les gros modèles.
- Versions actives (v1.x en 2026) ; suit de près les modèles et méthodes du Hub.

## Pièges

- API en **évolution rapide** : signatures de trainers et noms d'arguments changent entre versions — épingler la version.
- Le **chat template** et le formatage des données doivent matcher le modèle de base, sinon entraînement silencieusement faux.
- DPO/GRPO chargent souvent **plusieurs modèles** (policy + référence) : la VRAM grimpe vite, penser LoRA + quantization.
- Reward hacking et dérive KL sur les méthodes RL : surveiller, cf. [[RLHF and DPO]].

## Alternatives

- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

Nuance : TRL est le **moteur de bas niveau**. Axolotl et LLaMA-Factory l'enveloppent dans une config déclarative ; Unsloth en optimise les kernels ; Tunix joue le même rôle que TRL côté JAX/TPU. On choisit TRL quand on veut écrire le code et tout contrôler, les autres quand on veut déléguer la boucle (ou changer d'écosystème).

## Liens

- [[SFT]] · [[RLHF and DPO]] · [[Reward modeling]] · [[PEFT]] — les méthodes que les trainers TRL implémentent.
- [[GRPO]] · [[PPO]] · [[RL for LLMs]] — le post-training par RL (GRPOTrainer, PPOTrainer).
- [[HuggingFace]] — écosystème parent (`transformers`, `datasets`, `peft`, `accelerate`).
- [[PyTorch]] · [[DeepSpeed]] — backend et passage à l'échelle.
- [[Comparatif - Fine-tuning LLM]] — vue d'ensemble des outils de fine-tuning.
- Doc : https://huggingface.co/docs/trl
