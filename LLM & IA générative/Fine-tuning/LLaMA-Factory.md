---
role: brique
nom: LLaMA-Factory
alias: [llama-factory, llamafactory, LLaMA Factory, hiyouga/LLaMA-Factory, LLaMA Board]
pitch: "Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis."
categorie: llm/finetuning
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[TRL]]", "[[Unsloth]]", "[[Axolotl]]", "[[Tunix]]"]
complements: []
tags: [fine-tuning, declarative-config, low-code, distributed-training, llm]
url_docs: https://llamafactory.readthedocs.io/en/latest/
url_repo: https://github.com/hiyouga/LLaMA-Factory
---

# LLaMA-Factory

<!-- AUTO:BANDEAU:START -->
> Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | à jour · 2026-05-30 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme unifiée de fine-tuning qui vise l'**ampleur de couverture** : plus de 100 familles
de LLM **et de VLM** — Llama, Mistral, Qwen, Gemma, DeepSeek, GLM, Phi, Qwen-VL, LLaVA — et
toutes les étapes du post-training, [[SFT]], DPO, PPO, KTO, ORPO, reward modeling, en [[PEFT]]
ou full fine-tuning. Trois modes de pilotage cohabitent : CLI (`llamafactory-cli train`), YAML,
et une **interface web no-code**, LLaMA Board, pour configurer et lancer un run sans écrire une
ligne. Sous le capot, l'écosystème Hugging Face et TRL, avec des accélérations optionnelles
(Unsloth, FlashAttention) et DeepSpeed pour le multi-GPU. Publié à ACL 2024, largement adopté.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| **Couverture de modèles** : viser une famille exotique ou un VLM sans chercher un outil dédié | **Surface fonctionnelle énorme** : beaucoup d'options et de templates de modèles, donc des erreurs de template silencieuses |
| Configurer un fine-tune **sans coder**, par l'interface web ou un YAML | L'interface web masque la complexité, pas les contraintes mémoire : un mauvais choix LoRA/quantization finit en OOM |
| Comparer rapidement plusieurs méthodes — SFT, puis DPO, puis PPO — dans un cadre homogène | Le **format des datasets** et le mapping de colonnes doivent suivre la spec attendue par la méthode |
| Multimodal : fine-tuner un modèle vision-langage avec le même outil que le texte | Couverture large n'est pas profondeur : sur un cas pointu, l'outil spécialisé reprend l'avantage |

## Mise en œuvre

- Installation — `uv add llamafactory`, image Docker, ou lancement de l'interface web en local
- Point d'entrée — trois voies équivalentes : la CLI `llamafactory-cli train`, un YAML, ou LLaMA Board
- Prérequis — un GPU ; poids et datasets viennent du hub Hugging Face, au format attendu par la méthode
- Exécution — multi-GPU et multi-nœuds via DeepSpeed ; sait appeler Unsloth et FlashAttention pour accélérer
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure GPU

## Écosystème

### Alternatives

- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

## Ressources

- Documentation — https://llamafactory.readthedocs.io/en/latest/
- Dépôt — https://github.com/hiyouga/LLaMA-Factory
- Papier — ACL 2024, *LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models*

## Voir aussi

- [[Fine-tuning]] — le hub du dossier
- [[Comparatif - Fine-tuning LLM]] — ce qui départage les outils du dossier
- [[RLHF and DPO]] · [[Quantization]] — les méthodes couvertes par sa config
- [[Entraînement distribué]] — DeepSpeed, pour le multi-GPU
- [[HuggingFace]] · [[DeepSpeed]] — les briques sous-jacentes
