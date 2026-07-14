---
galaxie: wiki
type: concept
nom: PPO
alias: [PPO, Proximal Policy Optimization, optimisation proximale de politique, clipped surrogate]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, policy-gradient]
---

# PPO

## Aperçu

- **Proximal Policy Optimization** : une méthode de [[Policy gradient|gradient de politique]] qui limite l'ampleur de chaque mise à jour pour rester **proche** de la politique précédente — d'où *proximal*. Stable, simple à implémenter, peu de réglages.
- Devenu le **standard de fait** du RL appliqué : contrôle continu, robotique, et surtout le post-training des LLM, où c'est l'algorithme historique du [[RLHF and DPO|RLHF]] (cf. [[RL for LLMs]]).

## Concepts clés

### Le problème : pas trop grand, mais pas trop petit
- Un pas de gradient de politique trop grand peut **effondrer** la politique (on s'éloigne d'une zone où l'estimation d'avantage est valide). TRPO résolvait ça par une contrainte KL dure mais coûteuse (second ordre).
- PPO obtient le même effet avec un **objectif clippé** du premier ordre : simple SGD, pas de contrainte explicite.

### L'objectif clippé (surrogate)
- On forme le **ratio d'importance** $\rho = \pi_\theta(a\mid s) / \pi_{\text{old}}(a\mid s)$ entre nouvelle et ancienne politique.
- On maximise $\min(\rho\,\hat{A},\ \mathrm{clip}(\rho, 1-\epsilon, 1+\epsilon)\,\hat{A})$ : tant que le ratio reste dans $[1-\epsilon, 1+\epsilon]$, mise à jour normale ; au-delà, le gradient est **coupé** → plus d'incitation à bouger trop loin.

### Réutilisation des données
- Contrairement au gradient de politique pur (un échantillon = une mise à jour), le clip rend sûr de faire **plusieurs epochs** sur le même mini-lot → bien plus efficace en données. PPO reste néanmoins **on-policy**.
- Composants usuels : un **critique** de valeur ([[Actor-Critic methods]]) pour estimer $\hat{A}$ via **GAE**, un terme d'**entropie** pour l'exploration, et — côté LLM — une pénalité **KL** vers le modèle de référence.

## Les maths, simplement

- Objectif clippé : $\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}\big[\min(\rho\,\hat{A},\ \mathrm{clip}(\rho, 1-\epsilon, 1+\epsilon)\,\hat{A})\big]$, avec $\rho = \dfrac{\pi_\theta(a\mid s)}{\pi_{\text{old}}(a\mid s)}$.
- Le $\min$ rend l'objectif **pessimiste** : il prend la borne la moins favorable, ce qui retire le bénéfice d'un ratio qui dérape.
- Côté LLM (RLHF) : on ajoute $-\beta\,\mathrm{KL}(\pi_\theta \,\Vert\, \pi_{\text{ref}})$ pour ne pas trop s'éloigner du modèle SFT (cf. [[RLHF and DPO]]).

## En pratique

- Bon défaut quand on **doit** faire du RL en boucle (récompense non issue de préférences, contrôle, signal vérifiable). $\epsilon \approx 0,2$, quelques epochs par lot, avantages normalisés.
- En LLM : lourd à opérer (politique + critique + reward model + modèle de référence en mémoire). Si l'on n'a que des préférences, [[RLHF and DPO|DPO]] est plus simple ; pour le raisonnement, [[GRPO]] retire le critique.
- Pièges : critique mal entraîné → avantages biaisés ; KL qui explose (réponses qui dérivent) ; *reward hacking* quand la récompense est un modèle appris ([[Reward modeling]]).

## Approches voisines & alternatives

- [[Policy gradient]] — PPO en est la variante stabilisée ; même fondation théorique.
- [[Actor-Critic methods]] — PPO est un acteur-critique on-policy (critique pour l'avantage via GAE).
- [[RLHF and DPO]] — PPO est l'optimiseur RL du pipeline RLHF ; DPO est l'alternative sans boucle RL.
- [[GRPO]] — retire le modèle de valeur de PPO (avantage estimé par groupe) ; dominant pour le raisonnement.
- [[RL for LLMs]] — le cadre où PPO post-entraîne un LLM.

## Pour aller plus loin

- Schulman et al. (2017) — *Proximal Policy Optimization Algorithms*.
- Schulman et al. (2015) — *Trust Region Policy Optimization* (TRPO, l'ancêtre à contrainte KL).
- Ouyang et al. (2022) — *InstructGPT* (PPO pour le RLHF).
- OpenAI — *Spinning Up in Deep RL* (implémentation pédagogique de PPO).
- Implémentation de référence : [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] (`PPO`) sur environnements [[Dev/Services/Gymnasium|Gymnasium]]. Aussi dans [[Dev/Services/TF-Agents|TF-Agents]] (`PPOAgent`) ; le surrogate clippé est fourni en brique JAX par [[Dev/Services/RLax|RLax]].
