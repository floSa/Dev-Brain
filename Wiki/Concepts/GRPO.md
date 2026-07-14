---
galaxie: wiki
type: concept
nom: GRPO
alias: [Group Relative Policy Optimization, optimisation de politique par groupes, optimisation de politique relative par groupe]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, reasoning, alignment, llm]
---

# GRPO

## Aperçu

- **Group Relative Policy Optimization** : un algorithme de gradient de politique introduit par DeepSeek, **sans modèle de valeur** (critic-free).
- Idée centrale : au lieu d'un réseau critique pour estimer le **baseline**, on échantillonne **plusieurs réponses** par prompt et on calcule l'avantage en **normalisant les récompenses à l'intérieur du groupe**. Brique de la [[RL for LLMs]], au cœur de DeepSeek-R1.

## Concepts clés

### Le problème de PPO
- [[PPO]] a besoin d'un **value model** (critic) — un second réseau, de taille comparable à la politique, qui double la mémoire et le coût et ajoute de l'instabilité (cf. [[RLHF and DPO]]).

### L'idée de GRPO
- Pour un prompt $x$, échantillonner un **groupe** de $G$ réponses avec l'ancienne politique. Noter chacune (par un [[Reward modeling|modèle de récompense]] ou une récompense **vérifiable**).
- L'**avantage** d'une réponse = son écart à la **moyenne du groupe**, normalisé par l'écart-type. Le baseline n'est plus appris : c'est la moyenne des autres réponses au même prompt. Plus de critic.

### Pourquoi ça marche bien pour le raisonnement
- Se marie avec les **récompenses vérifiables (RLVR)** : sur un problème de maths ou de code, on sait si la réponse est juste → signal propre, peu de reward hacking.
- Recette de **DeepSeek-R1** ; et de **DeepSeek-R1-Zero**, entraîné en **RL pur** (sans [[SFT]] préalable), d'où l'émergence de chaînes de raisonnement longues et de l'« aha moment ». Voir [[Reasoning models]].

### Pièges & variantes
- **Biais de longueur** et débats sur la **normalisation** par l'écart-type (variante *Dr. GRPO*), réglage de la **taille de groupe** $G$ (plus grand = baseline plus stable, mais plus de calcul).
- Famille en mouvement rapide : DAPO, GSPO et autres dérivés.

## Les maths, simplement

- Avantage d'une réponse $i$ du groupe : $\hat{A}_i = \dfrac{r_i - \mathrm{mean}(r_1,\dots,r_G)}{\mathrm{std}(r_1,\dots,r_G)}$ — la récompense **relative au groupe**, sans réseau de valeur.
- Mise à jour de type PPO (ratio d'importance **clippé** + pénalité **KL** vers la référence), mais l'avantage $\hat{A}_i$ vient du groupe au lieu d'un critic : $\mathcal{J}(\theta) = \mathbb{E}\big[\min(\rho\,\hat{A},\ \mathrm{clip}(\rho,1\!-\!\epsilon,1\!+\!\epsilon)\,\hat{A})\big] - \beta\,\mathrm{KL}$, avec $\rho = \pi_\theta/\pi_{\text{old}}$.

## En pratique

- Exige un **signal de récompense** par réponse : récompense **vérifiable** (maths/code) de préférence, sinon un [[Reward modeling|RM]].
- Régler la **taille de groupe** $G$ (souvent 8–64) et le budget d'échantillonnage — c'est le poste de coût principal.
- Idéal pour entraîner le **raisonnement** ; combinable avec [[PEFT]]/LoRA pour le coût.
- Outils : `TRL` (GRPOTrainer), `verl`, `OpenRLHF` ; échantillonnage via [[Dev/Services/vLLM|vLLM]].

## Approches voisines & alternatives

- [[RL for LLMs]] — GRPO est l'un de ses algorithmes (la branche sans critic).
- [[RLHF and DPO]] — **PPO** (avec critic) et **DPO** (sans RL) sont les alternatives directes.
- [[Reward modeling]] — fournit la récompense quand elle n'est pas vérifiable.
- [[Reasoning models]] — le débouché phare de GRPO.
- [[PPO]] — l'algorithme dont GRPO retire le modèle de valeur.

## Pour aller plus loin

- Shao et al. (2024) — *DeepSeekMath* (introduction de GRPO).
- DeepSeek-AI (2025) — *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL*.
- Schulman et al. (2017) — *Proximal Policy Optimization* (le point de départ).
