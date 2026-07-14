---
galaxie: dev
type: service
nom: Unsloth
alias: [unsloth, unslothai, unsloth.ai]
pitch: "Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision."
categorie: llm/finetuning
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/TRL|TRL]]", "[[Dev/Services/Axolotl|Axolotl]]", "[[Dev/Services/LLaMA-Factory|LLaMA-Factory]]", "[[Dev/Services/Tunix|Tunix]]"]
remplace_par: []
status: actif
tags: [fine-tuning, memory-optimization, quantization, gpu, llm]
url_docs: https://unsloth.ai/docs
url_repo: https://github.com/unslothai/unsloth
---

# Unsloth

## Pourquoi

Unsloth réécrit les passes critiques du fine-tuning en **kernels Triton sur mesure** (attention, autograd, opérations LoRA) pour entraîner un LLM **~2× plus vite avec 70-80 % de VRAM en moins**, sans approximation ni perte de précision. Concrètement : fine-tuner en [[PEFT]] (LoRA/QLoRA, [[Quantization]] 4-bit dynamique) un modèle de plusieurs dizaines de milliards de paramètres sur **un seul GPU grand public** (RTX 4090/5090). L'API reste celle de [[Dev/Services/HuggingFace|HuggingFace]] et de [[Dev/Services/TRL|TRL]] : on charge un `FastLanguageModel`, le reste du code de training ne change quasiment pas. Supporte aussi le full fine-tuning, la FP8, le GRPO ([[RLHF and DPO]], [[RL for LLMs]]) et l'export GGUF pour l'inférence locale.

## Quand l'utiliser

- **Mémoire / vitesse serrées** : fine-tuner le plus gros modèle possible sur 1 GPU (laptop, Colab, station perso).
- **LoRA / QLoRA** rapides, ou GRPO économe en VRAM pour le RL de raisonnement.
- Boucle d'itération courte : prototyper un fine-tune en quelques heures sur du matériel modeste.
- Exporter en **GGUF / 4-bit** pour servir le modèle en local ensuite.

## Quand NE PAS l'utiliser

- **Entraînement multi-GPU / multi-nœuds** à grande échelle → [[Dev/Services/Axolotl|Axolotl]] ou [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] (DeepSpeed/FSDP), ou [[Dev/Services/TRL|TRL]] + `accelerate`. La version open-source vise le **single-GPU**.
- On veut un pipeline **100 % déclaratif** sans toucher au code Python → [[Dev/Services/Axolotl|Axolotl]] / [[Dev/Services/LLaMA-Factory|LLaMA-Factory]].
- Architecture non supportée : la couverture est large (500+ modèles) mais pas universelle — vérifier le modèle visé.

## Déploiement & coût

- Open-source, gratuit ; `uv add unsloth`. Cœur sous Apache-2.0 (l'UI optionnelle Unsloth Studio est en AGPL-3.0).
- Rien à héberger ; coût = un GPU. Compile des kernels Triton à l'install → dépendance à la version CUDA.
- Single-node par conception : tout le gain vient de l'optimisation **sur une carte**.

## Pièges

- **Couplage CUDA / Triton / torch** sensible : les mises à jour cassent parfois l'install, épingler les versions.
- Le gain VRAM dépend du **modèle et de la config** : les chiffres annoncés (2×, 80 %) sont des cas favorables, à mesurer.
- Multi-GPU bridé en OSS : ne pas compter dessus pour passer à l'échelle horizontale.
- Patche en profondeur transformers/TRL → un décalage de version d'une de ces libs peut désactiver les optimisations silencieusement.

## Alternatives

- [[Dev/Services/TRL|TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Dev/Services/Axolotl|Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Dev/Services/Tunix|Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

Nuance : Unsloth est une **couche d'accélération** au-dessus de TRL/transformers, pas un cadre de pilotage. On le combine d'ailleurs avec eux ; on le préfère seul quand la contrainte dominante est le GPU unique.

## Liens

- [[PEFT]] — LoRA/QLoRA, le cœur de cible d'Unsloth.
- [[Quantization]] — 4-bit dynamique qui rend QLoRA possible sur petit GPU.
- [[SFT]] · [[RLHF and DPO]] · [[GRPO]] · [[RL for LLMs]] — méthodes supportées.
- [[Dev/Services/TRL|TRL]] · [[Dev/Services/HuggingFace|HuggingFace]] — API et trainers qu'Unsloth optimise.
- [[Comparatif - Fine-tuning LLM]] — vue d'ensemble des outils de fine-tuning.
- Doc : https://unsloth.ai/docs
