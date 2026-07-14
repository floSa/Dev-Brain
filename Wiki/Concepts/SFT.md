---
galaxie: wiki
type: concept
nom: SFT
alias: [supervised fine-tuning, fine-tuning supervisé, instruction tuning, instruction fine-tuning]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [fine-tuning, llm]
---

# SFT

## Aperçu

- **Fine-tuning supervisé** : poursuivre l'entraînement d'un modèle pré-entraîné sur des paires **(prompt, réponse attendue)**, en lui faisant imiter les réponses cibles.
- Étape qui transforme un modèle « complétion brute » en modèle qui **suit des instructions** (instruction tuning) ; première brique du pipeline d'alignement, avant [[RLHF and DPO]].

## Concepts clés

### Objectif d'entraînement
- Même perte que le pré-entraînement — prédiction du token suivant — mais sur des données **curées** de démonstrations. On masque souvent la perte sur le prompt pour n'apprendre que la **réponse**.

### Instruction tuning
- SFT sur un mélange de tâches formulées en instructions → généralisation à des instructions nouvelles. C'est ce qui rend un modèle « utilisable » en chat.

### La donnée prime
- Quelques **milliers d'exemples de haute qualité** battent souvent un gros volume bruité (hypothèse « less is more », LIMA). La qualité, la diversité et le format des démonstrations dominent le résultat — d'où le recours à la [[Synthetic data generation]].

### Coût et plein vs efficient
- **Full fine-tuning** : mettre à jour tous les poids — coûteux en mémoire (optimiseur, gradients). En pratique on fait du SFT en **[[PEFT]]** (LoRA) pour ne toucher qu'une fraction des paramètres.

### Pièges
- **Catastrophic forgetting** : trop fine-tuner dégrade les capacités générales. **Surapprentissage** sur un petit jeu. Mauvais formatage (chat template) qui casse l'inférence.

## Les maths, simplement

- On minimise la log-vraisemblance négative des réponses : $\mathcal{L}(\theta) = -\sum_{(x,y)} \sum_{t} \log p_\theta(y_t \mid y_{<t}, x)$, où $x$ est le prompt et $y$ la réponse cible.
- Identique à l'entraînement d'un modèle de langue, mais la somme ne porte (souvent) que sur les tokens de $y$ — on apprend à **répondre**, pas à recopier la question.

## En pratique

- Avant de fine-tuner, épuiser le moins cher : [[Prompt engineering]] puis [[RAG]]. SFT quand le **comportement / format** doit être appris durablement, pas juste de la connaissance.
- Faire du SFT en **[[PEFT]]/LoRA** par défaut : 10–100× moins de mémoire, résultats proches du full fine-tuning.
- Soigner la **donnée** (qualité > quantité) et le **chat template** exact du modèle de base.
- Outils : [[Dev/Services/TRL|TRL]] (SFTTrainer) et l'écosystème [[Dev/Services/HuggingFace|HuggingFace]] ; sans coder, [[Dev/Services/Axolotl|Axolotl]] / [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] (config) ou [[Dev/Services/Unsloth|Unsloth]] (1 GPU, rapide). Entraînement sur [[Dev/Services/PyTorch|PyTorch]].
- SFT seul imite des démonstrations ; pour optimiser selon des **préférences** (ce qui est *mieux*), enchaîner avec [[RLHF and DPO]].

## Approches voisines & alternatives

- [[PEFT]] — comment faire du SFT à moindre coût (LoRA, QLoRA) au lieu de mettre à jour tous les poids.
- [[RLHF and DPO]] — étape suivante : aligner sur des préférences au-delà de l'imitation ; le SFT en est le point de départ.
- [[Prompt engineering]] — levier sans entraînement à épuiser avant le SFT.
- [[RAG]] — pour injecter de la **connaissance** à jour ; le SFT est meilleur pour le **comportement / format**.
- [[Synthetic data generation]] — produit les démonstrations quand les données humaines manquent.

## Pour aller plus loin

- Ouyang et al. (2022) — *InstructGPT* (SFT comme étape 1 du pipeline RLHF).
- Wei et al. (2021) — *Finetuned Language Models Are Zero-Shot Learners* (FLAN, instruction tuning).
- Zhou et al. (2023) — *LIMA: Less Is More for Alignment*.
