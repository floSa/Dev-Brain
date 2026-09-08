---
role: brique
nom: Tunix
alias: [tunix, google tunix, google-tunix, tune-in-jax]
pitch: "Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL."
categorie: llm/finetuning
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[TRL]]", "[[Unsloth]]", "[[Axolotl]]", "[[LLaMA-Factory]]"]
complements: ["[[vLLM]]"]
tags: [llm, reinforcement-learning, fine-tuning]
url_docs: https://tunix.readthedocs.io/
url_repo: https://github.com/google/tunix
---

# Tunix

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | à jour · 2026-08-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

*Tune-in-JAX* : la bibliothèque de post-training de Google, construite sur **Flax NNX**. Elle
couvre le [[SFT]] (full weights ou PEFT), l'alignement par préférences (DPO, ORPO), le RL
([[GRPO]], PPO et ses variantes GSPO-Token, DAPO, Dr.GRPO, jusqu'au **RL agentique** multi-tour
avec appels d'outils) et la **distillation**. Les rollouts d'inférence s'appuient nativement
sur vLLM ou SGLang-JAX. C'est le pendant JAX/TPU de TRL, avec le même périmètre de méthodes
mais un autre socle de calcul — et c'est là que se joue tout le choix : l'avantage ne se
matérialise que sur TPU.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Post-training sur **TPU** : c'est le cas d'usage cible, avec les gains de coût des TPU à grande échelle | **Maturité** : versions 0.1.x, breaking changes fréquents — épingler la version et lire le changelog |
| Stack **JAX** déjà en place (MaxText, Flax NNX) : rester dans l'écosystème plutôt que passer par PyTorch | L'avantage se matérialise sur TPU ; sur GPU NVIDIA, le chemin balisé reste ailleurs |
| GRPO et RL de raisonnement à l'échelle, y compris agentique : rollouts asynchrones, multi-tour | Coût d'entrée JAX / Flax NNX réel pour une équipe PyTorch : sharding, gestion d'état NNX |
| | Conversion de poids Hugging Face ↔ formats JAX à intégrer au pipeline, et à re-vérifier à chaque release |

## Mise en œuvre

- Installation — `uv add google-tunix`
- Point d'entrée — import Python, sur Flax NNX : un entraîneur par méthode, plus les rollouts délégués à un moteur d'inférence
- Prérequis — une stack JAX, et des poids convertis depuis les formats Hugging Face
- Exécution — distribué par conception : sharding et parallélisme de données et de modèle JAX, ciblant les pods TPU
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure TPU ou GPU

## Écosystème

### Alternatives

- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.

### Compléments

- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — le moteur sur lequel il délègue les rollouts d'inférence du RL.

## Ressources

- Documentation — https://tunix.readthedocs.io/
- Dépôt — https://github.com/google/tunix

## Voir aussi

- [[Fine-tuning]] — le hub du dossier
- [[Comparatif - Fine-tuning LLM]] — ce qui départage les outils du dossier
- [[RL for LLMs]] — le cadre : post-entraîner un LLM par renforcement
- [[RLHF and DPO]] — les méthodes de préférence implémentées
- [[JAX]] — le socle de calcul, via Flax NNX
