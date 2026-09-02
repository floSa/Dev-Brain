---
role: hub
nom: Fine-tuning
alias: [post-training, ajustement de modèle]
pitch: Modifier les poids d'un modèle plutôt que son prompt — apprentissage supervisé, alignement sur des préférences, renforcement.
domaines: [ai-eng, ml-eng]
tags: [fine-tuning, alignment, reinforcement-learning, quantization, synthetic-data]
---

# Fine-tuning

> Modifier les poids d'un modèle plutôt que son prompt — apprentissage supervisé, alignement sur des préférences, renforcement.

## Ce qu'il faut comprendre

- Le fine-tuning apprend une **forme**, pas des faits. Il fait adopter un format de sortie, un ton, un vocabulaire métier, une tâche étroite — il n'injecte pas de connaissance fraîche, et tenter de le faire produit un modèle qui hallucine avec assurance. Pour de la connaissance, c'est [[RAG]] ; le fine-tune et le RAG se combinent plus souvent qu'ils ne s'excluent.
- Trois étages de post-training, dans cet ordre et pas un autre. **[[SFT]]** apprend à imiter des réponses de référence — c'est 90 % des besoins réels. **[[RLHF and DPO]]** apprend à préférer une réponse à une autre, à partir de paires comparées ; DPO l'obtient sans entraîner de modèle de récompense, ce qui a rendu l'étape accessible. **[[RL for LLMs]]** optimise contre un signal vérifiable — c'est là qu'agissent [[GRPO]] et le [[Reward modeling]], et c'est ce qui a produit les modèles de raisonnement.
- On n'entraîne presque jamais tous les poids. **[[PEFT]]** est le principe — n'ajuster qu'une petite fraction des paramètres — et [[LoRA et QLoRA]] son implémentation dominante : des matrices de rang faible ajoutées aux couches d'attention, plus la quantization du modèle de base pour QLoRA. C'est ce qui fait tenir un fine-tune de 7 à 13 milliards de paramètres sur un seul GPU grand public, et c'est l'hypothèse par défaut de toutes les briques de ce dossier.
- Le facteur limitant est **la VRAM**, et les leviers sont connus et cumulables : quantization du modèle de base, rang de LoRA, longueur de séquence, taille de lot et accumulation de gradient. [[Unsloth]] attaque ce point par des kernels sur mesure — ~2× plus rapide, 70-80 % de VRAM en moins, à précision annoncée constante.
- **La donnée décide du résultat, pas l'outil.** Quelques milliers d'exemples propres et cohérents battent des dizaines de milliers d'exemples bruités, et aucune bibliothèque ne rattrape un jeu mal construit. Fabriquer ce jeu avec un modèle est devenu la norme : [[Synthetic data generation]].
- Le choix de brique se ramène à **écrire du code ou remplir une configuration**. [[TRL]] et [[Tunix]] sont des bibliothèques : on écrit la boucle, on contrôle tout. [[Axolotl]] et [[LLaMA-Factory]] sont pilotés par un fichier YAML ou une interface, ce qui va beaucoup plus vite tant qu'on reste dans les cas prévus, et coûte cher dès qu'on en sort.
- **Fine-tuner en dernier recours, et le mesurer.** Un fine-tune est un artefact à versionner, réentraîner à chaque changement de modèle de base, et évaluer avant et après — sinon on ne sait pas s'il a apporté quoi que ce soit. Cf. [[LLM eval metrics]] et [[LLM benchmarks]].
- Le clivage matériel est réel et souvent oublié : [[Tunix]] est JAX/TPU, tout le reste est PyTorch/GPU. C'est une décision d'infrastructure, pas de préférence d'API.

## Choisir

- Écrire ma boucle de post-training en Python, sur l'écosystème Hugging Face → [[TRL]].
- La même chose sur TPU, en JAX → [[Tunix]].
- Un fine-tune sans écrire de code d'entraînement, tout en YAML → [[Axolotl]].
- Couvrir beaucoup de modèles et de méthodes, avec une interface web → [[LLaMA-Factory]].
- Tenir sur un seul GPU grand public, ou aller plus vite à matériel constant → [[Unsloth]].
- Apprendre un format ou un ton → [[SFT]] ; aligner sur des préférences → [[RLHF and DPO]] ; optimiser un signal vérifiable → [[GRPO]].
- Injecter de la connaissance à jour → [[RAG]], pas ce dossier.
- Changer seulement le comportement, sans entraînement → [[Prompt engineering]] d'abord.

<!-- AUTO:START -->
### Briques
- [[Axolotl]] — Fine-tuning de LLM piloté par un unique fichier YAML — préprocessing, SFT/DPO/RLHF, multi-GPU (DeepSpeed/FSDP) et quantization couverts par la config, sans écrire de code d'entraînement.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis.
- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code.
- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision.

### Comparatifs
- [[Comparatif - Fine-tuning LLM]]
<!-- AUTO:END -->
