---
galaxie: wiki
type: concept
nom: RL for LLMs
alias: [RL for language models, reinforcement learning for LLMs, RL appliqué aux LLM, RL post-training, post-training RL, RLVR]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, alignment, fine-tuning, llm]
---

# RL for LLMs

## Aperçu

- Appliquer l'**apprentissage par renforcement** à un LLM : la **politique** est le modèle, l'**action** est la génération de tokens, la **récompense** note la sortie produite.
- Étape de **post-training** après le [[SFT]] : au lieu d'imiter des réponses cibles, on **optimise** ce qui obtient une bonne récompense — préférences humaines ([[RLHF and DPO|RLHF]]) ou correction vérifiable (RLVR) pour le raisonnement.

## Concepts clés

### Le cadre RL adapté au LLM
- Génération vue comme un **MDP** : à chaque pas, l'état est le préfixe, l'action est le token suivant, la politique $\pi_\theta$ est le LLM. La récompense arrive surtout **en fin de séquence** (signal rare).
- On maximise la récompense **tout en restant proche** du modèle de référence (SFT) via une pénalité **KL** — sinon la politique dérive et oublie ses capacités générales.
- Bases RL générales : [[Reinforcement learning]], [[Policy gradient]], [[PPO]] (cluster `concept/rl`).

### Deux sources de récompense
- **Préférences humaines** → [[Reward modeling]] entraîné sur comparaisons (RLHF). Pour l'utilité, le ton, l'innocuité.
- **Récompenses vérifiables (RLVR)** → la récompense est **calculée** (tests unitaires, vérification d'un résultat mathématique), pas apprise. C'est ce qui entraîne les [[Reasoning models]] (OpenAI o1, DeepSeek-R1).

### Les algorithmes
- **[[PPO]]** (online, avec critic) — le standard du RLHF historique ; puissant mais lourd à régler (cf. [[RLHF and DPO]]).
- **DPO** (offline, sans RL en boucle) — contourne la RL en optimisant une perte de classification sur des paires.
- **[[GRPO]]** (online, **sans critic**) — estime l'avantage par groupe d'échantillons ; populaire pour le raisonnement.

### Pièges
- **Reward hacking** : exploiter les failles de la récompense plutôt que de s'améliorer.
- **Instabilité et coût** : la RL online échantillonne à l'entraînement → cher et capricieux. Surveiller **KL** et **longueur** des réponses.

## Les maths, simplement

- Objectif commun : $\max_\theta \; \mathbb{E}_{x,\,y\sim\pi_\theta}\big[\,r(x,y)\,\big] \;-\; \beta\,\mathrm{KL}\!\big(\pi_\theta \,\Vert\, \pi_{\text{ref}}\big)$ — maximiser la récompense en restant proche du modèle de référence, $\beta$ réglant la fermeté de la contrainte.
- $r$ vient d'un [[Reward modeling|modèle de récompense]] (RLHF) **ou** d'un vérificateur (RLVR) ; les algorithmes diffèrent surtout par la façon d'**estimer l'avantage** et de faire la mise à jour.

## En pratique

- **Ordre** : [[SFT]] d'abord, RL ensuite. Le modèle doit déjà répondre avant qu'on optimise des préférences.
- **Commencer simple** : DPO (offline, stable) pour l'alignement de préférences ; passer à PPO/[[GRPO]] si l'on a un bon signal (RM solide ou récompense vérifiable).
- **Raisonnement** : GRPO + récompenses vérifiables (maths, code) est la recette des modèles de raisonnement récents.
- Faire le RL en **[[PEFT]]/LoRA** pour le rendre abordable sur peu de GPU.
- Outils : `TRL`, `verl`, `OpenRLHF` sur [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/HuggingFace|HuggingFace]] ; échantillonnage rapide via [[Dev/Services/vLLM|vLLM]]. Côté JAX/TPU : [[Dev/Services/Tunix|Tunix]] (GRPO, PPO, RL agentique).

## Approches voisines & alternatives

- [[RLHF and DPO]] — les deux algorithmes d'alignement de préférences (PPO online, DPO offline).
- [[Reward modeling]] — fournit la récompense apprise quand elle n'est pas calculable.
- [[GRPO]] — la variante sans critic, dominante pour le raisonnement.
- [[SFT]] — préalable obligatoire ; le RL vient après.
- [[PEFT]] — rend le RL réalisable à moindre coût (LoRA).
- [[Reasoning models]] — le débouché principal du RLVR.
- [[Reinforcement learning]], [[PPO]], [[Policy gradient]] — le socle RL général réutilisé ici.

## Pour aller plus loin

- Ouyang et al. (2022) — *InstructGPT* (RLHF par PPO).
- Schulman et al. (2017) — *Proximal Policy Optimization*.
- DeepSeek-AI (2025) — *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*.
