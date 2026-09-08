---
role: brique
nom: Axolotl
alias: [axolotl, axolotl-ai-cloud, axolotl.ai]
pitch: "Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement."
categorie: llm/finetuning
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[TRL]]", "[[Unsloth]]", "[[LLaMA-Factory]]", "[[Tunix]]"]
complements: []
tags: [fine-tuning, declarative-config, distributed-training, llm]
url_docs: https://docs.axolotl.ai/
url_repo: https://github.com/axolotl-ai-cloud/axolotl
---

# Axolotl

<!-- AUTO:BANDEAU:START -->
> Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | à jour · 2026-07-17 |
<!-- AUTO:BANDEAU:END -->

## Définition

Axolotl transforme le fine-tuning en **fichier de configuration**. Un seul YAML décrit tout le
pipeline : modèle de base, datasets et leur format, méthode ([[SFT]], DPO, IPO, KTO, ORPO,
reward modeling), [[PEFT]] ou full fine-tuning, [[Quantization]], et la stratégie multi-GPU —
DeepSpeed ZeRO ou FSDP. On lance `axolotl train config.yml` sans écrire de boucle
d'entraînement. Sous le capot, c'est l'écosystème Hugging Face, TRL, `peft` et `accelerate` ;
Axolotl est la couche de pilotage déclarative qui les assemble et fige la recette dans un
fichier versionnable, donc rejouable à l'identique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| **Reproductibilité** : une recette de fine-tuning est un YAML committé, rejouable tel quel | La **surface de config est vaste** : un champ mal réglé — template, packing, ZeRO — casse l'entraînement sans erreur claire |
| Multi-GPU ou multi-nœuds sans écrire de code distribué : DeepSpeed et FSDP se règlent à la config | Le **format de dataset** doit matcher exactement le type attendu par la méthode : c'est la source d'erreur la plus fréquente |
| Itérer sur beaucoup de variantes — modèle, dataset, hyperparamètres — en éditant un fichier | Hérite des pièges de DeepSpeed et FSDP sur les gros runs distribués : OOM, wrapping fp32 |
| Couvrir tout le pipeline avec un outil unique : preprocess, train, eval, quantize, inference | |

## Mise en œuvre

- Installation — `uv add axolotl`, ou l'image Docker fournie
- Point d'entrée — la commande `axolotl train config.yml`, et le YAML qui porte toute la recette
- Prérequis — un GPU ; les poids et datasets viennent du hub Hugging Face
- Exécution — multi-GPU et multi-nœuds via DeepSpeed ou FSDP ; images prêtes pour les fournisseurs de GPU à la demande (RunPod, Modal)
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure GPU

## Écosystème

### Alternatives

- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

## Ressources

- Documentation — https://docs.axolotl.ai/
- Dépôt — https://github.com/axolotl-ai-cloud/axolotl

## Voir aussi

- [[Fine-tuning]] — le hub du dossier
- [[Comparatif - Fine-tuning LLM]] — ce qui départage les outils du dossier
- [[RLHF and DPO]] — les méthodes de préférence pilotées par la config
- [[Entraînement distribué]] — DeepSpeed et FSDP, exposés à la config
- [[HuggingFace]] · [[DeepSpeed]] — les briques sous-jacentes
