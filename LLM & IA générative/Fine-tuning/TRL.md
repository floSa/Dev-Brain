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

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

*Transformer Reinforcement Learning*, la pile de **post-training** de Hugging Face : une classe
de *trainer* par méthode, calquée sur le `Trainer` de `transformers` — `SFTTrainer`,
`RewardTrainer`, `DPOTrainer`, `GRPOTrainer`, `PPOTrainer`. C'est le **niveau code** du
fine-tuning : on écrit du Python, on contrôle la boucle, la loss, le *data collator* et les
callbacks. C'est aussi la brique sur laquelle reposent la plupart des outils déclaratifs du
domaine, ce qui en fait le seul endroit où implémenter une méthode récente — GRPO, KTO, ORPO —
sans attendre qu'un wrapper la supporte. Intégration native avec `transformers`, `datasets`,
`peft` et `accelerate`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Aligner un LLM par préférences : DPO, GRPO, ou le pipeline RLHF complet — reward model puis PPO | **API en évolution rapide** : signatures de trainers et noms d'arguments changent entre versions — épingler la version |
| Fine-tuner par code, avec la main sur la boucle, la loss, le collator et les callbacks | Le **chat template** et le formatage des données doivent matcher le modèle de base, faute de quoi l'entraînement est silencieusement faux |
| Implémenter une méthode récente sans attendre qu'un outil de plus haut niveau la supporte | DPO et GRPO chargent souvent **plusieurs modèles** — policy et référence : la VRAM grimpe vite, prévoir LoRA et quantization |
| Travailler déjà dans l'écosystème Hugging Face : `transformers`, `datasets`, `peft` | *Reward hacking* et dérive KL sur les méthodes RL : à surveiller pendant le run, rien ne le signale tout seul |
| | Entraîner de zéro une architecture sur mesure : ce n'est pas du post-training → [[PyTorch]] |

## Mise en œuvre

- Installation — `uv add trl`
- Point d'entrée — import Python : un trainer par méthode, `SFTTrainer`, `RewardTrainer`, `DPOTrainer`, `GRPOTrainer`, `PPOTrainer`
- Prérequis — l'écosystème Hugging Face en place, et un chat template accordé au modèle de base
- Exécution — en bibliothèque, dans le process d'entraînement ; distribution par `accelerate` sur plusieurs GPU et nœuds, compatible DeepSpeed ZeRO pour les gros modèles
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure GPU

## Écosystème

### Alternatives

- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

## Ressources

- Documentation — https://huggingface.co/docs/trl
- Dépôt — https://github.com/huggingface/trl

## Voir aussi

- [[Fine-tuning]] — le hub du dossier
- [[Comparatif - Fine-tuning LLM]] — ce qui départage les outils du dossier
- [[SFT]] · [[Reward modeling]] · [[RLHF and DPO]] · [[PEFT]] — les méthodes que ses trainers implémentent
- [[GRPO]] · [[PPO]] · [[RL for LLMs]] — le post-training par renforcement
- [[HuggingFace]] — l'écosystème parent
- [[DeepSpeed]] — le passage à l'échelle sur les gros modèles
