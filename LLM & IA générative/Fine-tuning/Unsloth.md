---
role: brique
nom: Unsloth
alias: [unsloth, unslothai, unsloth.ai]
pitch: "Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision."
categorie: llm/finetuning
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[TRL]]", "[[Axolotl]]", "[[LLaMA-Factory]]", "[[Tunix]]"]
complements: []
tags: [fine-tuning, memory-optimization, quantization, gpu, llm]
url_docs: https://unsloth.ai/docs
url_repo: https://github.com/unslothai/unsloth
---

# Unsloth

<!-- AUTO:BANDEAU:START -->
> Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Unsloth réécrit les passes critiques du fine-tuning en **kernels Triton sur mesure** —
attention, autograd, opérations LoRA — pour entraîner **~2× plus vite avec 70 à 80 % de VRAM en
moins**, sans approximation ni perte de précision. Concrètement, cela met un modèle de
plusieurs dizaines de milliards de paramètres sur **un seul GPU grand public**. L'API reste
celle de Hugging Face et de TRL : on charge un `FastLanguageModel`, le reste du code
d'entraînement ne change quasiment pas. Couvre aussi le full fine-tuning, la FP8, le GRPO, et
l'export GGUF pour servir le modèle en local ensuite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Mémoire ou vitesse serrées : faire tenir le plus gros modèle possible sur un GPU — laptop, Colab, station perso | **Multi-GPU bridé** dans la version open-source : ne pas compter dessus pour passer à l'échelle horizontale |
| LoRA et QLoRA rapides, ou GRPO économe en VRAM pour le RL de raisonnement | Le gain dépend du **modèle et de la config** : les 2× et 80 % annoncés sont des cas favorables, à mesurer sur le sien |
| Boucle d'itération courte : prototyper un fine-tune en quelques heures sur du matériel modeste | **Couplage CUDA / Triton / torch** sensible : les mises à jour cassent parfois l'installation — épingler les versions |
| Exporter en GGUF ou 4-bit pour servir le modèle en local ensuite | Il **patche en profondeur** `transformers` et TRL : un décalage de version d'une de ces bibliothèques désactive les optimisations silencieusement |
| | Architecture non supportée : la couverture est large (500+ modèles) mais pas universelle — vérifier le modèle visé |

## Mise en œuvre

- Installation — `uv add unsloth` ; les kernels Triton se compilent à l'installation, d'où la dépendance à la version de CUDA
- Point d'entrée — import Python : `FastLanguageModel`, puis le code d'entraînement Hugging Face / TRL habituel
- Prérequis — un GPU NVIDIA, et des versions de `transformers`, TRL et torch accordées à celle d'Unsloth
- Exécution — en bibliothèque, mono-nœud par conception : tout le gain vient de l'optimisation **sur une carte**
- Coût — gratuit ; cœur sous Apache-2.0, l'interface optionnelle Unsloth Studio étant en AGPL-3.0. La dépense est le GPU

## Écosystème

### Alternatives

- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.

## Ressources

- Documentation — https://unsloth.ai/docs
- Dépôt — https://github.com/unslothai/unsloth

## Voir aussi

- [[Fine-tuning]] — le hub du dossier
- [[Comparatif - Fine-tuning LLM]] — ce qui départage les outils du dossier
- [[PEFT]] — LoRA et QLoRA, son cœur de cible
- [[Quantization]] — le 4-bit dynamique qui rend QLoRA possible sur petit GPU
- [[SFT]] · [[RLHF and DPO]] · [[GRPO]] · [[RL for LLMs]] — les méthodes supportées
- [[HuggingFace]] — l'API et les trainers qu'il optimise
