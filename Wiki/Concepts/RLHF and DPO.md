---
galaxie: wiki
type: concept
nom: RLHF and DPO
alias: [RLHF, DPO, alignement par préférences, preference tuning, direct preference optimization]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [alignment, fine-tuning, llm]
---

# RLHF and DPO

## Aperçu

- Famille de méthodes d'**alignement** qui entraînent un LLM à partir de **préférences humaines** (« la réponse A est meilleure que la B ») plutôt que de réponses cibles uniques.
- On optimise ce qui est **préféré**, pas seulement ce qui est imité ([[SFT]]) : utilité, honnêteté, innocuité, ton. **RLHF** passe par la RL ; **DPO** atteint le même but sans boucle de RL.

## Concepts clés

### Le pipeline RLHF
1. **[[SFT]]** — partir d'un modèle qui suit déjà les instructions.
2. **[[Reward modeling|Modèle de récompense]]** — entraîné sur des comparaisons humaines à prédire un score de préférence.
3. **Optimisation RL** — affiner la politique (le LLM) pour maximiser cette récompense, généralement par **[[PPO]]**, avec une pénalité **KL** qui empêche de trop s'éloigner du modèle SFT.

### DPO — Direct Preference Optimization
- Supprime le modèle de récompense **explicite** et la boucle RL : une dérivation montre que la politique optimale est sa **propre** récompense implicite. On optimise alors une simple **perte de classification** sur les paires (préférée, rejetée).
- Plus **stable et simple** que PPO (un seul modèle à entraîner, pas d'échantillonnage en ligne) ; devenu le défaut pour beaucoup d'équipes. Variantes : IPO, KTO, ORPO.

### RLHF (PPO) vs DPO
- **PPO** : plus de pièces mobiles (reward model + RL en ligne), plus dur à régler, mais plafond parfois plus haut et adapté aux récompenses non issues de préférences.
- **DPO** : hors-ligne, robuste, moins de calcul ; nécessite un bon jeu de paires de préférences.

### Pièges
- **Reward hacking** : la politique exploite les failles du reward model (verbosité, flagornerie) plutôt que de vraiment s'améliorer. La pénalité **KL** et des données de préférence propres limitent la dérive.

## Les maths, simplement

- Préférences modélisées par **Bradley-Terry** : $P(y_w \succ y_l \mid x) = \sigma\!\big(r(x,y_w) - r(x,y_l)\big)$, où $r$ est la récompense et $\sigma$ la sigmoïde.
- **RLHF** : $\max_\theta \; \mathbb{E}\,[\,r(x,y)\,] - \beta\, \mathrm{KL}\!\big(\pi_\theta \,\Vert\, \pi_{\text{ref}}\big)$ — maximiser la récompense en restant proche du modèle de référence.
- **DPO** réinjecte la solution analytique de ce problème dans Bradley-Terry et optimise directement $\pi_\theta$ : $-\log \sigma\!\big(\beta \log \tfrac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \tfrac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\big)$. Plus de reward model séparé.

## En pratique

- **Ordre** : [[SFT]] d'abord (le modèle doit déjà répondre), alignement préférences ensuite.
- **Commencer par DPO** : moins de calcul, plus stable, suffisant dans la plupart des cas. Passer à PPO si l'on a un reward model solide ou des signaux non-préférences.
- Faire l'alignement en **[[PEFT]]/LoRA** pour le rendre abordable.
- Outils : [[Dev/Services/TRL|TRL]] (DPOTrainer, RewardTrainer, GRPOTrainer, PPOTrainer) ; sans coder via [[Dev/Services/Axolotl|Axolotl]] / [[Dev/Services/LLaMA-Factory|LLaMA-Factory]], ou [[Dev/Services/Unsloth|Unsloth]] pour le GRPO économe en VRAM. Côté JAX/TPU : [[Dev/Services/Tunix|Tunix]] (DPO, ORPO, GRPO).
- Surveiller la **divergence KL** et la **longueur** des réponses (signes de reward hacking) ; garder un jeu de préférences propre et diversifié.
- Liens RL plus larges : [[RL for LLMs]], [[GRPO]] — variantes récentes pour le raisonnement.

## Approches voisines & alternatives

- [[PPO]] — l'algorithme RL qui optimise la politique dans RLHF (avec pénalité KL).
- [[SFT]] — préalable obligatoire ; imite des réponses là où l'alignement optimise des préférences.
- [[PEFT]] — rend RLHF/DPO réalisables sur peu de GPU.
- [[Reward modeling]] — le modèle de récompense au cœur du RLHF (et implicite dans DPO).
- [[RL for LLMs]], [[GRPO]] — la branche RL appliquée au raisonnement, au-delà des préférences humaines.

## Pour aller plus loin

- Ouyang et al. (2022) — *InstructGPT: Training language models to follow instructions with human feedback*.
- Rafailov et al. (2023) — *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*.
- Christiano et al. (2017) — *Deep RL from Human Preferences* (origine du reward model par comparaisons).
