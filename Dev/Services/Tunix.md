---
galaxie: dev
type: service
nom: Tunix
alias: [tunix, google tunix, google-tunix, tune-in-jax]
pitch: "Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL."
categorie: llm/finetuning
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/TRL|TRL]]", "[[Dev/Services/Unsloth|Unsloth]]", "[[Dev/Services/Axolotl|Axolotl]]", "[[Dev/Services/LLaMA-Factory|LLaMA-Factory]]"]
remplace_par: []
status: actif
tags: [llm, reinforcement-learning, fine-tuning]
url_docs: https://tunix.readthedocs.io/
url_repo: https://github.com/google/tunix
---

# Tunix

## Pourquoi

Bibliothèque Google de **post-training de LLM en [[Dev/Services/JAX|JAX]]** (*Tune-in-JAX*), construite sur Flax NNX : [[SFT]] (full weights ou PEFT), alignement par préférences (DPO, ORPO), RL ([[GRPO]], PPO et variantes GSPO-Token, DAPO, Dr.GRPO, jusqu'au **RL agentique** multi-tour avec appels d'outils) et **distillation**. Les rollouts d'inférence s'appuient nativement sur [[Dev/Services/vLLM|vLLM]] ou SGLang-JAX. Pensée pour la performance sur **TPU** et le passage à l'échelle — c'est le pendant JAX/TPU de [[Dev/Services/TRL|TRL]] (qui est PyTorch).

## Quand l'utiliser

- Post-training sur **TPU** (GCP) : c'est le cas d'usage cible, avec les gains de coût des TPU à grande échelle.
- Stack **JAX** existante (MaxText, Flax NNX) : rester dans l'écosystème plutôt que de passer par PyTorch.
- **GRPO et RL de raisonnement à l'échelle**, y compris agentique (rollouts asynchrones, multi-tour).

## Quand NE PAS l'utiliser

- Écosystème **PyTorch / Hugging Face** en place → [[Dev/Services/TRL|TRL]] : intégration native `transformers`/`peft`, communauté et recettes incomparablement plus larges.
- Fine-tuning sur **un GPU grand public** → [[Dev/Services/Unsloth|Unsloth]] (kernels optimisés VRAM), pas une lib pensée TPU.
- Besoin de **stabilité** : projet récent (2025), encore en 0.1.x — API mouvante, écosystème et docs en construction.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add google-tunix`. Rien à héberger ; coût = l'infra TPU/GPU.
- **Distributed** par conception : sharding et data/model parallelism JAX, ciblant les pods TPU.
- Jeune mais **activement développée** (v0.1.7 en juin 2026, releases fréquentes) ; portée par Google.

## Pièges

- **Maturité** : versions 0.1.x — breaking changes fréquents, épingler la version et lire le changelog.
- L'avantage se matérialise sur **TPU** ; sur GPU NVIDIA, le couple PyTorch/TRL reste le chemin balisé.
- Coût d'entrée JAX/Flax NNX réel pour une équipe PyTorch (sharding, gestion d'état NNX).
- Conversion de poids HuggingFace ↔ formats JAX à intégrer au pipeline (et à re-vérifier à chaque release).

## Alternatives

- [[Dev/Services/TRL|TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Dev/Services/Unsloth|Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Dev/Services/Axolotl|Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.

Nuance : tout ce cluster fait du post-training de LLM, mais Tunix est le seul ancré **JAX/TPU** — les quatre autres vivent dans l'écosystème **PyTorch/Hugging Face** (TRL comme moteur, Unsloth pour l'accélération GPU, Axolotl/LLaMA-Factory pour le pilotage déclaratif). On prend Tunix quand on tourne sur TPU ou qu'on reste en JAX ; sinon le chemin balisé reste PyTorch. En dehors du brain : verl, OpenRLHF (RL de LLM à grande échelle, PyTorch).

## Liens

- [[RL for LLMs]] — le cadre : post-entraîner un LLM par renforcement.
- [[RLHF and DPO]] · [[GRPO]] · [[SFT]] — les méthodes implémentées.
- [[Dev/Services/TRL|TRL]] — le voisin PyTorch ; même rôle, autre écosystème.
- [[Dev/Services/JAX|JAX]] — le socle de calcul (Flax NNX).
- [[Dev/Services/vLLM|vLLM]] — moteur de rollouts pour le RL.
- [[Comparatif - Fine-tuning LLM]] — vue d'ensemble des outils de fine-tuning.
- Doc : https://tunix.readthedocs.io/
