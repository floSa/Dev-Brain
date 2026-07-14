---
galaxie: wiki
type: concept
nom: Actor-Critic methods
alias: [actor-critic, acteur-critique, méthodes acteur-critique, A2C, A3C, advantage actor-critic]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, policy-gradient, value-function]
---

# Actor-Critic methods

## Aperçu

- Hybride des deux grandes familles : un **acteur** (la politique $\pi_\theta$, cf. [[Policy gradient]]) qui choisit les actions, et un **critique** (une fonction de valeur, cf. [[Value functions]]) qui les note.
- Le critique remplace le retour Monte-Carlo bruité du gradient de politique par une estimation **bootstrapée** (TD) → mise à jour à **faible variance** et possible à chaque pas, sans attendre la fin de l'épisode.

## Concepts clés

### Acteur et critique
- **Acteur** : optimisé par gradient de politique, mais guidé par l'**avantage** estimé par le critique plutôt que par le retour brut.
- **Critique** : apprend $V(s)$ (ou $Q(s,a)$) par différence temporelle (cf. [[Bellman equations]]). Son rôle est de fournir une **baseline** informée qui réduit la variance du gradient de l'acteur.
- Le signal qui relie les deux est l'**erreur TD** $\delta$, qui sert d'estimateur de l'avantage.

### Le compromis biais-variance du critique
- Gradient de politique pur (Monte-Carlo) : **sans biais**, variance haute. Critique bootstrapé : variance basse, mais **biais** si le critique est imparfait.
- **GAE** (generalized advantage estimation) interpole entre les deux via un paramètre $\lambda$ → réglage fin du compromis.

### Variantes
- **A2C / A3C** : acteur-critique on-policy avec avantage, en synchrone (A2C) ou asynchrone multi-workers (A3C).
- **DDPG / TD3 / SAC** : acteur-critique **off-policy** pour actions **continues** (replay buffer, critique $Q$) ; SAC ajoute un bonus d'**entropie** (max-entropy RL).
- **PPO** est un acteur-critique on-policy avec objectif clippé (cf. [[PPO]]).

## Les maths, simplement

- Erreur TD (estimateur de l'avantage) : $\delta_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)$.
- Mise à jour de l'**acteur** : $\theta \leftarrow \theta + \alpha\, \nabla_\theta \log \pi_\theta(a_t\mid s_t)\, \delta_t$ — pousser la politique dans le sens de l'avantage estimé.
- Mise à jour du **critique** : $\phi \leftarrow \phi + \beta\, \delta_t\, \nabla_\phi V_\phi(s_t)$ — régression de $V_\phi$ vers la cible de Bellman.

## En pratique

- Bon compromis général : variance plus basse que le gradient de politique pur, applicable au **continu** (contrairement à [[Q-learning and DQN]]).
- Off-policy (SAC/TD3) → meilleure efficacité en données pour la robotique ; on-policy (A2C/PPO) → plus stable et simple à régler.
- Pièges : **deux** réseaux à équilibrer (un critique en retard fausse l'avantage) ; sensibilité aux pas d'apprentissage relatifs acteur/critique ; surestimation du critique $Q$ (TD3 corrige par double critique).
- Côté outils : SAC, TD3 et DDPG prêts dans [[Dev/Services/TF-Agents|TF-Agents]] ; D4PG et MPO dans [[Dev/Services/Acme|Acme]] ; pertes acteur/critique en briques JAX dans [[Dev/Services/RLax|RLax]].

## Approches voisines & alternatives

- [[Policy gradient]] — l'acteur en est une instance ; le critique ne fait que réduire sa variance.
- [[Value functions]] — ce que le critique apprend (V ou Q).
- [[Q-learning and DQN]] — l'extrême « tout critique, pas d'acteur explicite » ; limité aux actions discrètes.
- [[PPO]] — l'acteur-critique on-policy le plus utilisé en pratique.
- [[GRPO]] — supprime le critique appris, remplacé par une baseline calculée sur un groupe d'échantillons.

## Pour aller plus loin

- Mnih et al. (2016) — *Asynchronous Methods for Deep RL* (A3C).
- Lillicrap et al. (2016) — *DDPG* ; Fujimoto et al. (2018) — *TD3* ; Haarnoja et al. (2018) — *Soft Actor-Critic*.
- Sutton & Barto — *Reinforcement Learning*, ch. 13.5 (acteur-critique).
