---
galaxie: wiki
type: concept
nom: Q-learning and DQN
alias: [Q-learning, DQN, Deep Q-Network, deep Q-learning, Q-apprentissage, apprentissage par Q]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, value-function, temporal-difference, deep-learning]
---

# Q-learning and DQN

## Aperçu

- Famille de méthodes **basées valeur** : apprendre la fonction $Q^{*}(s,a)$ (cf. [[Value functions]]), puis agir gloutonnement en choisissant l'action de plus haut $Q$. La politique n'est jamais représentée explicitement — elle découle de la valeur.
- **Q-learning** est l'algorithme tabulaire fondateur (off-policy, par différence temporelle) ; **DQN** est sa version *deep* qui remplace la table par un réseau de neurones, ce qui a rendu le RL viable sur des entrées riches (pixels Atari).

## Concepts clés

### Q-learning tabulaire
- Met à jour $Q(s,a)$ vers une **cible de Bellman** échantillonnée à chaque transition observée (cf. [[Bellman equations]]) : pas besoin de connaître la dynamique $P$.
- **Off-policy** : la cible utilise $\max_{a'} Q(s',a')$ (l'action gloutonne), peu importe l'action réellement jouée pour explorer. On peut donc apprendre la politique optimale tout en explorant (souvent en [[Exploration vs exploitation|$\varepsilon$-greedy]]).
- Différence avec **SARSA** (on-policy) : SARSA met à jour vers le $Q$ de l'action **effectivement** jouée — plus prudent près des zones risquées.

### DQN — passage au deep
- Un réseau $Q_\theta(s,a)$ approxime la table quand les états sont trop nombreux (images, espaces continus). Mais combiner approximation + bootstrap + off-policy, c'est la **deadly triad** → instabilité, divergence.
- Deux stabilisateurs clés :
  - **Experience replay** : stocker les transitions dans un buffer et les rejouer en mini-batches → casse la corrélation temporelle des données.
  - **Target network** : un second réseau $\theta^{-}$, copie figée et mise à jour lentement, fournit la cible → évite que la cible bouge en même temps que l'estimation.

### Surestimation et variantes
- Le $\max$ sur des $Q$ bruités **surestime** systématiquement les valeurs → **Double DQN** (découple sélection et évaluation de l'action).
- Autres briques : **Dueling** (séparer valeur d'état et avantage), **Prioritized replay** (rejouer les transitions à forte erreur TD), **Rainbow** (combinaison de ces améliorations).

## Les maths, simplement

- Mise à jour Q-learning : $Q(s,a) \leftarrow Q(s,a) + \alpha\big[\underbrace{r + \gamma \max_{a'} Q(s',a')}_{\text{cible}} - Q(s,a)\big]$ — on glisse vers la cible de Bellman d'un pas $\alpha$ ; le crochet est l'**erreur TD**.
- Perte DQN : $\mathcal{L}(\theta) = \mathbb{E}\big[(r + \gamma \max_{a'} Q_{\theta^{-}}(s',a') - Q_\theta(s,a))^2\big]$ — régression de $Q_\theta$ sur la cible fournie par le réseau cible $\theta^{-}$.
- Double DQN : remplacer $\max_{a'} Q_{\theta^{-}}(s',a')$ par $Q_{\theta^{-}}(s', \arg\max_{a'} Q_\theta(s',a'))$ — l'un choisit, l'autre évalue.

## En pratique

- Adapté aux espaces d'actions **discrets** et pas trop grands (le $\max$ se calcule par énumération). Actions continues → plutôt acteur-critique ([[Actor-Critic methods]], DDPG/SAC).
- Sample-inefficient : beaucoup d'interactions nécessaires ; le replay buffer amortit le coût en réutilisant les transitions.
- Pièges : $\varepsilon$ qui décroît trop vite (sous-exploration), récompenses non normalisées, fréquence de mise à jour du target network mal réglée, deadly triad qui fait diverger silencieusement les $Q$.

## Approches voisines & alternatives

- [[Value functions]] — la quantité $Q$ que ces méthodes estiment ; le socle conceptuel.
- [[Bellman equations]] — la cible de la mise à jour est un backup de Bellman échantillonné.
- [[Policy gradient]] — l'alternative : optimiser la politique directement, sans passer par $Q$ ; plus naturel pour les actions continues et stochastiques.
- [[Actor-Critic methods]] — hybride qui garde un critique de valeur mais représente la politique explicitement.
- [[Exploration vs exploitation]] — Q-learning a besoin d'une stratégie d'exploration ($\varepsilon$-greedy) pour collecter ses données.

## Pour aller plus loin

- Watkins & Dayan (1992) — *Q-learning* (l'algorithme et sa preuve de convergence tabulaire).
- Mnih et al. (2015) — *Human-level control through deep reinforcement learning* (DQN, Nature).
- van Hasselt et al. (2016) — *Deep RL with Double Q-learning* ; Hessel et al. (2018) — *Rainbow*.
- Sutton & Barto — *Reinforcement Learning*, ch. 6 (TD learning, Q-learning).
- Implémentation de référence : [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] (`DQN`, `QR-DQN`) sur environnements [[Dev/Services/Gymnasium|Gymnasium]]. Aussi dans [[Dev/Services/TF-Agents|TF-Agents]] (`DqnAgent`, C51) et [[Dev/Services/Acme|Acme]] (R2D2) ; pertes TD et distributionnelles en briques JAX dans [[Dev/Services/RLax|RLax]].
