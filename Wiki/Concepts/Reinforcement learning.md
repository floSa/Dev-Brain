---
galaxie: wiki
type: concept
nom: Reinforcement learning
alias: [RL, apprentissage par renforcement, reinforcement learning, agent-environnement]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, markov-decision-process]
---

# Reinforcement learning

## Aperçu

- Cadre d'apprentissage où un **agent** interagit avec un **environnement** : il observe un état, choisit une action, reçoit une récompense, et ajuste son comportement pour maximiser la récompense **cumulée** à long terme.
- Pas de jeu de données étiqueté : le signal est une récompense scalaire, souvent rare et différée — l'agent doit découvrir lui-même quelles actions paient, par essais et erreurs.

## Concepts clés

### Les briques du problème
- **Agent / environnement** : l'agent agit, l'environnement renvoie un nouvel état et une récompense. La boucle se répète sur des épisodes ou en continu.
- **Politique** ($\pi$) : la stratégie de l'agent — quelle action prendre dans chaque état. C'est l'objet qu'on cherche à optimiser.
- **Récompense / retour** : le retour est la somme (escomptée) des récompenses futures. L'agent maximise le retour espéré, pas la récompense immédiate.
- Le problème se formalise comme un [[Markov Decision Process]] : états, actions, transitions, récompenses.

### Trois familles de méthodes
- **Basées valeur** : estimer la valeur des états/actions (cf. [[Value functions]]) puis agir gloutonnement — [[Q-learning and DQN]].
- **Basées politique** : optimiser directement $\pi$ par montée de gradient — [[Policy gradient]], [[PPO]].
- **Acteur-critique** : combiner les deux — un acteur (politique) guidé par un critique (valeur) — [[Actor-Critic methods|Actor-Critic]].

### Tensions propres au RL
- [[Exploration vs exploitation]] : tester des actions incertaines vs exploiter ce qui marche déjà.
- **Crédit différé** : une récompense tardive doit être attribuée aux bonnes actions passées — c'est le rôle des [[Bellman equations|équations de Bellman]].

## Les maths, simplement

- Retour escompté : $G_t = \sum_{k=0}^{\infty} \gamma^{k} r_{t+k+1}$ — somme des récompenses futures, pondérées par le facteur d'escompte $\gamma \in [0,1[$ (le futur compte moins que le présent).
- Objectif : trouver $\pi^{*} = \arg\max_{\pi}\; \mathbb{E}_{\pi}[G_t]$ — la politique qui maximise le retour espéré.
- $\gamma$ proche de 1 → agent prévoyant (horizon long) ; $\gamma$ faible → agent myope.

## En pratique

- Pertinent quand le problème est **séquentiel** et que les décisions influencent les états futurs : robotique, jeux, contrôle, recommandation, allocation de ressources.
- Coûteux et instable : besoin de beaucoup d'interactions (sample inefficiency), récompense difficile à concevoir, entraînement sensible aux hyperparamètres.
- En AI engineering, le RL post-entraîne les LLM : cf. [[RL for LLMs]], [[RLHF and DPO]], [[Reward modeling]], [[GRPO]].
- Le [[Multi-armed bandits|bandit manchot]] est le cas dégénéré sans état (une seule décision répétée) — bon point d'entrée pour comprendre l'arbitrage exploration/exploitation.
- Côté outils : [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] fournit des algorithmes prêts à l'emploi (PyTorch) sur des environnements [[Dev/Services/Gymnasium|Gymnasium]] (API standard agent-environnement) — le stack par défaut pour entraîner un agent sans repartir de zéro.
- Pour la recherche : [[Dev/Services/Acme|Acme]] (agents distribués DeepMind) et [[Dev/Services/RLax|RLax]] (briques de perte en pur JAX) ; [[Dev/Services/TF-Agents|TF-Agents]] côté TensorFlow ; [[Dev/Services/OpenSpiel|OpenSpiel]] pour les jeux multi-agents.

## Approches voisines & alternatives

- [[Markov Decision Process]] — la formalisation mathématique du problème RL.
- [[Value functions]] — ce que les méthodes basées valeur estiment.
- [[Bellman equations]] — la relation récursive qui sous-tend la plupart des algorithmes.
- [[Exploration vs exploitation]] — le dilemme central de la collecte de données.
- [[Multi-armed bandits]] — RL sans état ; introduit le regret et les stratégies d'exploration.

## Pour aller plus loin

- Sutton & Barto — *Reinforcement Learning: An Introduction* (2e éd.) — la référence.
- David Silver — *RL Course* (UCL/DeepMind) ; OpenAI *Spinning Up in Deep RL*.
- Suites du cluster (`concept/rl`) : [[Q-learning and DQN]], [[Policy gradient]], [[PPO]], [[Actor-Critic methods]], [[Model-based RL]], [[Offline RL]], [[Imitation learning]], [[Reward shaping and hacking]].
- Jeux & planification : [[Monte Carlo Tree Search]], [[AlphaZero and self-play]], [[Counterfactual Regret Minimization]], [[Théorie des jeux]].
