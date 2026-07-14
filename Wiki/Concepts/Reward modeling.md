---
galaxie: wiki
type: concept
nom: Reward modeling
alias: [reward model, modèle de récompense, RM, preference model, modèle de préférence, RLAIF]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [alignment, reinforcement-learning, llm]
---

# Reward modeling

## Aperçu

- **Modèle de récompense (RM)** : un modèle qui prend un couple (prompt, réponse) et renvoie un **score scalaire** reflétant à quel point la réponse est préférée.
- C'est le **signal optimisé** par le RLHF : on l'entraîne sur des comparaisons humaines, puis on s'en sert pour récompenser la politique. Il est **explicite** dans [[RLHF and DPO|RLHF]] et la [[RL for LLMs]], **implicite** dans DPO.

## Concepts clés

### Apprendre une récompense à partir de comparaisons
- On part d'un modèle [[SFT]], on remplace la tête de génération par une **tête scalaire** (un seul nombre en sortie).
- On l'entraîne non pas sur des scores absolus (difficiles à annoter de façon cohérente) mais sur des **comparaisons** : « la réponse $y_w$ est meilleure que $y_l$ ». Modèle de **Bradley-Terry**.

### Où il sert
- Il fournit la récompense de la boucle RL ([[RL for LLMs]]) — [[PPO]], [[GRPO]]. Sans lui, pas de RLHF.
- **DPO** s'en passe : sa dérivation montre que la politique optimale **est** sa propre récompense implicite — on n'entraîne plus de RM séparé (cf. [[RLHF and DPO]]).

### Reward hacking / over-optimization
- La politique exploite les **failles** du RM (verbosité, flagornerie, mots-clés) au lieu de vraiment s'améliorer — un cas de **loi de Goodhart**.
- Garde-fous : pénalité **KL** vers le modèle de référence, données de préférence propres et diversifiées, **ensembles** de RM, et arrêt avant que le score RM ne décolle du jugement humain réel.

### Au-delà des préférences humaines
- **RLAIF** : un LLM joue l'annotateur ([[LLM-as-judge]]) pour produire les préférences à grande échelle, à la place des humains.
- **Récompenses vérifiables (RLVR)** : pour les maths et le code, la récompense est **calculée** (tests unitaires, vérification symbolique), pas apprise — pas de RM, pas de reward hacking sur les tâches vérifiables. Voie clé des [[Reasoning models]].
- **PRM vs ORM** : récompenser le **résultat** final (outcome) ou **chaque étape** de raisonnement (process). Le PRM donne un signal plus dense mais coûte plus cher à annoter.

## Les maths, simplement

- **Bradley-Terry** : la probabilité que $y_w$ soit préférée à $y_l$ est $\sigma\!\big(r(x,y_w) - r(x,y_l)\big)$, avec $r$ la récompense et $\sigma$ la sigmoïde.
- **Perte du RM** : $\mathcal{L}(r) = -\,\mathbb{E}_{(x,\,y_w,\,y_l)}\big[\log \sigma\!\big(r(x,y_w) - r(x,y_l)\big)\big]$ — on apprend à **classer** les réponses, pas à prédire un score absolu.

## En pratique

- Initialiser le RM depuis le modèle **SFT** (mêmes représentations) plutôt que de zéro.
- Soigner la **donnée de préférence** : accord inter-annotateurs, diversité des prompts, paires nettes. C'est le facteur dominant.
- Surveiller l'**over-optimization** : suivre la **divergence KL** et la **longueur** des réponses ; au-delà d'un point, plus de récompense RM = moins de qualité réelle.
- Si la tâche est **vérifiable** (maths, code), préférer une **récompense calculée** (RLVR) à un RM appris.
- Outils : `TRL` (RewardTrainer) sur l'écosystème [[Dev/Services/HuggingFace|HuggingFace]] / [[Dev/Services/PyTorch|PyTorch]].

## Approches voisines & alternatives

- [[RLHF and DPO]] — le RM est l'étape 2 du pipeline RLHF ; DPO le rend implicite.
- [[RL for LLMs]] — consomme la récompense du RM pour optimiser la politique.
- [[GRPO]] — peut utiliser un RM **ou** une récompense vérifiable comme signal.
- [[LLM-as-judge]] — un LLM évaluateur ; brique du **RLAIF** pour générer les préférences.
- [[Reward shaping and hacking]] — le RM appris est une cible privilégiée du **reward hacking** (over-optimization, sycophancy) ; les garde-fous (KL, ensembles) y sont détaillés.
- *Verifiable rewards / RLVR* (cf. [[Reasoning models]]) — récompense **calculée** plutôt qu'apprise, quand la correction est vérifiable.

## Pour aller plus loin

- Christiano et al. (2017) — *Deep RL from Human Preferences* (le RM par comparaisons).
- Stiennon et al. (2020) — *Learning to summarize from human feedback*.
- Ouyang et al. (2022) — *InstructGPT* (RM comme étape 2 du RLHF).
- Lightman et al. (2023) — *Let's Verify Step by Step* (process reward models).
