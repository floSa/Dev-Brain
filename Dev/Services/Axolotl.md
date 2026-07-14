---
galaxie: dev
type: service
nom: Axolotl
alias: [axolotl, axolotl-ai-cloud, axolotl.ai]
pitch: "Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement."
categorie: llm/finetuning
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/TRL|TRL]]", "[[Dev/Services/Unsloth|Unsloth]]", "[[Dev/Services/LLaMA-Factory|LLaMA-Factory]]", "[[Dev/Services/Tunix|Tunix]]"]
remplace_par: []
status: actif
tags: [fine-tuning, declarative-config, distributed-training, llm]
url_docs: https://docs.axolotl.ai/
url_repo: https://github.com/axolotl-ai-cloud/axolotl
---

# Axolotl

## Pourquoi

Axolotl transforme le fine-tuning en **fichier de configuration**. Un seul YAML décrit tout le pipeline : modèle de base, datasets et leur format, méthode ([[SFT]], [[RLHF and DPO]] : DPO/IPO/KTO/ORPO, reward modeling), [[PEFT]] (LoRA/QLoRA) ou full fine-tuning, [[Quantization]], et la stratégie multi-GPU ([[Entraînement distribué]] via [[Dev/Services/DeepSpeed|DeepSpeed]] ZeRO ou FSDP). On lance `axolotl train config.yml`, sans écrire de boucle d'entraînement. Sous le capot, c'est l'écosystème [[Dev/Services/HuggingFace|HuggingFace]] + [[Dev/Services/TRL|TRL]] + `peft` + `accelerate` ; Axolotl est la **couche de pilotage déclarative** qui les assemble et fige la recette dans un fichier versionnable et reproductible.

## Quand l'utiliser

- **Reproductibilité** : une recette de fine-tuning = un YAML committé, rejouable à l'identique.
- **Multi-GPU / multi-nœuds** sans gérer le code distribué : DeepSpeed et FSDP à la config.
- Itérer sur de nombreuses variantes (modèle, dataset, hyperparams) en éditant un fichier.
- Couvrir tout le pipeline (preprocess → train → eval → quantize → inference) avec un outil unique.

## Quand NE PAS l'utiliser

- On veut **contrôler finement la boucle** ou implémenter une méthode non prévue → [[Dev/Services/TRL|TRL]] en code.
- Contrainte **single-GPU** où la VRAM et la vitesse priment → [[Dev/Services/Unsloth|Unsloth]].
- On préfère une **interface web** no-code et la plus large couverture de modèles → [[Dev/Services/LLaMA-Factory|LLaMA-Factory]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; `uv add axolotl` (ou image Docker fournie). Coût = l'infra GPU.
- Pensé pour le **cloud GPU** : images prêtes pour RunPod, Modal, etc. ; multi-nœuds supporté.
- Maintenu par axolotl-ai-cloud ; suit les modèles récents du Hub (Llama, Mistral, Qwen, GPT-OSS…).

## Pièges

- La **surface de config est vaste** : un champ YAML mal réglé (template, packing, ZeRO) casse l'entraînement sans erreur claire.
- Le **format de dataset** doit matcher exactement le type attendu par la méthode — source d'erreurs fréquente.
- Hérite des pièges de DeepSpeed/FSDP (OOM, wrapping fp32) sur les gros runs distribués.
- Moins rapide / économe en VRAM qu'Unsloth à GPU unique : ce n'est pas son terrain.

## Alternatives

- [[Dev/Services/TRL|TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Dev/Services/Unsloth|Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Dev/Services/Tunix|Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

Nuance : Axolotl et [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] occupent la même case (fine-tuning déclaratif multi-GPU). Axolotl est plus orienté **YAML / cloud GPU / reproductibilité** ; LLaMA-Factory ajoute une **interface web** et une couverture de modèles plus large. Les deux s'appuient sur TRL/transformers.

## Liens

- [[SFT]] · [[RLHF and DPO]] · [[PEFT]] · [[Quantization]] — méthodes pilotées par la config.
- [[Entraînement distribué]] — DeepSpeed/FSDP exposés à la config.
- [[Dev/Services/TRL|TRL]] · [[Dev/Services/HuggingFace|HuggingFace]] · [[Dev/Services/DeepSpeed|DeepSpeed]] — briques sous-jacentes.
- [[Comparatif - Fine-tuning LLM]] — vue d'ensemble des outils de fine-tuning.
- Doc : https://docs.axolotl.ai/
