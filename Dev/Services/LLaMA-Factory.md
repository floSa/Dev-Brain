---
galaxie: dev
type: service
nom: LLaMA-Factory
alias: [llama-factory, llamafactory, LLaMA Factory, hiyouga/LLaMA-Factory, LLaMA Board]
pitch: "Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis."
categorie: llm/finetuning
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/TRL|TRL]]", "[[Dev/Services/Unsloth|Unsloth]]", "[[Dev/Services/Axolotl|Axolotl]]", "[[Dev/Services/Tunix|Tunix]]"]
remplace_par: []
status: actif
tags: [fine-tuning, declarative-config, low-code, distributed-training, llm]
url_docs: https://llamafactory.readthedocs.io/en/latest/
url_repo: https://github.com/hiyouga/LLaMA-Factory
---

# LLaMA-Factory

## Pourquoi

LLaMA-Factory (publié à ACL 2024) est une **plateforme unifiée** de fine-tuning qui vise l'ampleur de couverture : **100+ familles de LLM et VLM** (Llama, Mistral, Qwen, Gemma, DeepSeek, GLM, Phi, et les VLM Qwen-VL, LLaVA…) et toutes les étapes — [[SFT]], [[RLHF and DPO]] (DPO, PPO, KTO, ORPO), reward modeling — en [[PEFT]] (LoRA/QLoRA) ou full fine-tuning. Trois modes de pilotage : **CLI** (`llamafactory-cli train`), **YAML**, et une **interface web no-code** (LLaMA Board) pour configurer et lancer un run sans écrire de code. Sous le capot : écosystème [[Dev/Services/HuggingFace|HuggingFace]] + [[Dev/Services/TRL|TRL]] + `peft`, accélérations optionnelles ([[Dev/Services/Unsloth|Unsloth]], FlashAttention) et [[Entraînement distribué]] via [[Dev/Services/DeepSpeed|DeepSpeed]]. Adopté largement (70k+ étoiles, usages chez Amazon, NVIDIA, Aliyun).

## Quand l'utiliser

- **Couverture de modèles** : viser une famille exotique ou un VLM sans chercher un outil dédié.
- **Sans coder** : configurer un fine-tune via l'interface web (LLaMA Board) ou un YAML.
- Comparer rapidement plusieurs méthodes (SFT → DPO → PPO) dans un cadre homogène.
- Multimodal : fine-tuner un modèle vision-langage avec le même outil que le texte.

## Quand NE PAS l'utiliser

- On veut **écrire et contrôler la boucle**, ou une méthode hors catalogue → [[Dev/Services/TRL|TRL]].
- Pure optimisation **vitesse / VRAM sur 1 GPU** → [[Dev/Services/Unsloth|Unsloth]] (que LLaMA-Factory sait d'ailleurs intégrer).
- Workflow **GitOps strict YAML + cloud GPU** déjà rôdé avec [[Dev/Services/Axolotl|Axolotl]] : choix d'équipe, pas de gain à migrer.

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; install pip/`uv`, image Docker, ou interface web locale. Coût = l'infra GPU.
- Multi-GPU / multi-nœuds via DeepSpeed ; intègre Unsloth et FlashAttention pour accélérer.
- Très actif, releases fréquentes ; maintenu par hiyouga.

## Pièges

- **Surface fonctionnelle énorme** : beaucoup d'options et de templates de modèles → erreurs de template silencieuses.
- L'interface web masque la complexité mais pas les contraintes mémoire : un mauvais choix LoRA/quantization → OOM.
- Le **format des datasets** (et le mapping de colonnes) doit suivre la spec attendue par la méthode.
- Couverture large ≠ profondeur : pour un cas pointu, l'outil spécialisé (Unsloth, TRL) peut être préférable.

## Alternatives

- [[Dev/Services/TRL|TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Dev/Services/Unsloth|Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Dev/Services/Axolotl|Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[Dev/Services/Tunix|Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

Nuance : LLaMA-Factory et [[Dev/Services/Axolotl|Axolotl]] couvrent le même besoin (fine-tuning déclaratif multi-GPU). LLaMA-Factory mise sur la **largeur de modèles + interface web** ; Axolotl sur le **tout-YAML orienté cloud GPU**. Les deux enveloppent TRL/transformers et savent appeler Unsloth.

## Liens

- [[SFT]] · [[RLHF and DPO]] · [[PEFT]] · [[Quantization]] — méthodes couvertes.
- [[Entraînement distribué]] — DeepSpeed pour le multi-GPU.
- [[Dev/Services/TRL|TRL]] · [[Dev/Services/HuggingFace|HuggingFace]] · [[Dev/Services/Unsloth|Unsloth]] · [[Dev/Services/DeepSpeed|DeepSpeed]] — briques sous-jacentes et accélérateurs.
- [[Comparatif - Fine-tuning LLM]] — vue d'ensemble des outils de fine-tuning.
- Doc : https://llamafactory.readthedocs.io/en/latest/
