---
role: comparatif
nom: Comparatif - Fine-tuning LLM
categorie: llm/finetuning
tags: [fine-tuning, llm, alignment]
---

# Comparatif - Fine-tuning LLM

> On tranche sur : écrire la boucle ou la déclarer, le matériel visé — un GPU grand public, un cluster, un TPU —, et la largeur du catalogue de modèles.

![[Comparatif - Fine-tuning LLM.base]]

## Ce qui départage

- [[TRL]] — le **niveau code**, et la brique sur laquelle les autres reposent : un trainer par méthode (`SFTTrainer`, `RewardTrainer`, `DPOTrainer`, `GRPOTrainer`, `PPOTrainer`), donc le seul endroit où implémenter une méthode récente sans attendre qu'un wrapper la supporte. API en évolution rapide — épingler la version.
- [[Axolotl]] — la même chose pilotée par **un seul YAML** : la recette devient un fichier versionnable, et DeepSpeed/FSDP se règlent à la config plutôt qu'en code distribué. La surface de config est vaste, et un champ mal réglé (template, packing, ZeRO) casse l'entraînement sans erreur claire.
- [[LLaMA-Factory]] — la **couverture** : 100+ familles de LLM **et de VLM**, donc le seul à fine-tuner du multimodal avec le même outil que le texte, et le seul à offrir une **interface web** no-code (LLaMA Board). Largeur n'est pas profondeur — sur un cas pointu, l'outil spécialisé reprend l'avantage.
- [[Unsloth]] — des **kernels Triton sur mesure** : ~2× plus rapide et 70-80 % de VRAM en moins, ce qui met un modèle de plusieurs dizaines de milliards de paramètres sur **un seul GPU grand public**. C'est aussi sa borne — le multi-GPU est bridé dans la version open-source.
- [[Tunix]] — le pendant **JAX/TPU** de TRL, sur Flax NNX, avec le RL agentique multi-tour et des rollouts sur vLLM ou SGLang-JAX. L'avantage ne se matérialise que sur TPU, et le projet est en 0.1.x : breaking changes fréquents.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
