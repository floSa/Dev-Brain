---
galaxie: wiki
type: concept
nom: Policy gradient
alias: [policy gradient, gradient de politique, méthodes basées politique, policy-based methods, REINFORCE, policy optimization]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, policy-gradient]
---

# Policy gradient

## Aperçu

- Méthodes **basées politique** : au lieu d'estimer une valeur puis d'en déduire l'action (cf. [[Q-learning and DQN]]), on paramètre directement la politique $\pi_\theta(a\mid s)$ et on **monte le gradient** du retour espéré.
- Naturel pour les **actions continues** et les **politiques stochastiques**, là où le $\max_a Q$ des méthodes valeur devient impraticable. C'est le socle du post-training RL des LLM (cf. [[RL for LLMs]], [[PPO]], [[GRPO]]).

## Concepts clés

### Le théorème du gradient de politique
- Astuce du *log-ratio* (REINFORCE) : le gradient de l'objectif s'écrit comme une espérance qu'on peut **échantillonner** depuis les trajectoires, sans dériver la dynamique de l'environnement.
- Intuition : augmenter la probabilité des actions qui ont mené à un **bon** retour, diminuer celle des mauvaises — pondéré par à quel point le retour dépasse une référence.

### Baseline et avantage
- Le retour brut a une **variance énorme** → estimateur très bruité. On soustrait une **baseline** $b(s)$ (typiquement $V(s)$) sans introduire de biais.
- Le retour moins la baseline ≈ l'**avantage** $A(s,a)$ : « cette action fait-elle mieux que la moyenne en $s$ ? » (cf. [[Value functions]]). Estimer $A$ par un critique mène aux [[Actor-Critic methods]].

### On-policy et coût
- Les méthodes pures sont **on-policy** : chaque mise à jour exige des données fraîches échantillonnées par la politique courante → coûteux en interactions. PPO atténue cela en réutilisant un mini-lot sur quelques epochs.

## Les maths, simplement

- Objectif : $J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]$ — retour espéré sur les trajectoires $\tau$.
- Théorème du gradient : $\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\big[\nabla_\theta \log \pi_\theta(a\mid s)\, \hat{A}(s,a)\big]$ — pousser $\log \pi_\theta$ dans le sens de l'avantage $\hat{A}$.
- REINFORCE : $\hat{A}$ = retour escompté $G_t$ (parfois moins une baseline). Variance réduite si $\hat{A} = G_t - V(s_t)$.

## En pratique

- Préférer quand l'espace d'actions est **continu / haute dimension** (robotique, contrôle) ou quand une **politique stochastique** est souhaitable (exploration, jeux à information imparfaite).
- Réduire la variance est le nerf de la guerre : baseline/critique, **GAE** (generalized advantage estimation), normalisation des avantages.
- Pièges : pas d'apprentissage trop grand → effondrement de la politique ; sensibilité aux récompenses non normalisées ; gaspillage de données si on n'introduit pas de réutilisation contrôlée (cf. [[PPO]]).
- Côté outils : pertes REINFORCE et surrogate clippé en briques JAX dans [[Dev/Services/RLax|RLax]] ; agents complets dans [[Dev/Services/TF-Agents|TF-Agents]] (`ReinforceAgent`) et [[Dev/Services/Acme|Acme]] (IMPALA, MPO).

## Approches voisines & alternatives

- [[PPO]] — la variante robuste et dominante du gradient de politique (ratio clippé) ; à privilégier en pratique.
- [[Actor-Critic methods]] — remplacent le retour Monte-Carlo par un critique de valeur pour réduire la variance.
- [[Q-learning and DQN]] — l'approche duale (basée valeur) ; plus efficace en données sur actions discrètes, mais inadaptée au continu.
- [[Value functions]] — fournissent la baseline / l'avantage qui stabilise le gradient.
- [[GRPO]] — gradient de politique sans critic, avantage estimé par groupe ; usage LLM.

## Pour aller plus loin

- Williams (1992) — *REINFORCE* (estimateur du gradient de politique).
- Sutton et al. (2000) — *Policy Gradient Methods for RL with Function Approximation*.
- Schulman et al. (2016) — *High-Dimensional Continuous Control Using GAE*.
- Sutton & Barto — *Reinforcement Learning*, ch. 13 (*Policy Gradient Methods*).
