---
role: hub
nom: Apprentissage par renforcement
alias: [RL]
pitch: Apprendre par interaction plutôt que sur un jeu de données figé — un agent agit, reçoit une récompense, et ajuste sa politique.
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, markov-decision-process, policy-gradient, value-function, exploration-exploitation, offline-rl, imitation-learning, game-theory, self-play]
---

# Apprentissage par renforcement

> Apprendre par interaction plutôt que sur un jeu de données figé — un agent agit, reçoit une récompense, et ajuste sa politique.

## Ce qu'il faut comprendre

- **Ce dossier n'est pas « les agents ».** Un agent LLM qui appelle des outils dans une boucle ne fait pas de RL : il n'apprend rien, il exécute — c'est [[Agents]]. Ici, quelque chose est *appris par interaction*, et le prix à payer est un environnement simulable. Le RL utilisé pour aligner un modèle de langage est encore ailleurs : c'est du [[Fine-tuning]], parce que ce qui est mis à jour est un modèle de langage, pas une politique de contrôle.
- **La différence avec le supervisé est la nature du signal**, et elle change tout. Pas de bonne réponse fournie, seulement une récompense — souvent rare, souvent retardée, toujours conséquence d'une suite d'actions et non d'une seule. [[Reinforcement learning]] pose le cadre, [[Markov Decision Process]] la formalisation minimale : états, actions, transitions, récompense.
- **Deux façons d'apprendre, et le choix se fait tôt.** Estimer la valeur des états ou des actions, puis agir au mieux : [[Value functions]], [[Bellman equations]], [[Q-learning and DQN]]. Ou paramétrer directement la politique et la pousser dans la direction du gradient : [[Policy gradient]], [[Actor-Critic methods]] qui combine les deux, [[PPO]] qui est le défaut pratique parce qu'il limite l'ampleur de chaque mise à jour.
- **Le dilemme exploration / exploitation est le problème structurel**, pas un détail d'implémentation : [[Exploration vs exploitation]]. Un agent qui exploite trop tôt converge vers un optimum local sans jamais le savoir.
- **La récompense est le vrai point de fragilité, et elle se conçoit comme une spécification.** [[Reward shaping and hacking]] : un agent optimise ce qu'on écrit, pas ce qu'on veut, et il trouve les failles de la formulation plus vite que son auteur.
- **Trois échappatoires quand l'interaction coûte cher** — et c'est le cas dès qu'on sort du simulateur. [[Model-based RL]] apprend un modèle de l'environnement pour s'entraîner dedans ; [[Offline RL]] apprend depuis des traces déjà collectées, sans interagir ; [[Imitation learning]] part de démonstrations humaines. En industrie, ces trois-là sont plus souvent la bonne réponse que le RL en ligne.
- **La planification n'est pas l'apprentissage**, et les deux se combinent : [[Monte Carlo Tree Search]] cherche dans l'arbre des suites possibles au moment de décider, [[AlphaZero and self-play]] montre ce que donne le mariage des deux quand l'environnement est un jeu.
- Le multi-agent change la nature du problème plutôt que sa taille : l'environnement cesse d'être stationnaire, puisque les autres apprennent aussi. [[Théorie des jeux]] et [[Counterfactual Regret Minimization]] sont les outils de ce cas, notamment à information imparfaite.

## Choisir

- Un premier agent qui doit marcher, sur un environnement standard → [[Stable-Baselines3]] : implémentations testées, API homogène, PPO/SAC/DQN prêts.
- Définir ou brancher un environnement → [[Gymnasium]], le standard d'interface que tout le reste suppose.
- De la recherche à distribuer, en JAX ou TensorFlow → [[Acme]].
- Composer soi-même sa boucle en JAX, avec les pertes déjà écrites → [[RLax]].
- Des jeux, de l'information imparfaite, du multi-agent → [[OpenSpiel]].
- Un projet TensorFlow existant → [[TF-Agents]]. Cf. [[Comparatif - Reinforcement learning]].
- Aligner un modèle de langage par RL → [[Fine-tuning]], pas ce dossier.

<!-- AUTO:START -->
### Notions
- [[Actor-Critic methods]] — domaines : ml-eng
- [[AlphaZero and self-play]] — domaines : ml-eng, ai-eng
- [[Bellman equations]] — domaines : ml-eng
- [[Counterfactual Regret Minimization]] — domaines : ml-eng, ai-eng
- [[Exploration vs exploitation]] — domaines : ml-eng, ai-eng
- [[Imitation learning]] — domaines : ml-eng, ai-eng
- [[Markov Decision Process]] — domaines : ml-eng
- [[Model-based RL]] — domaines : ml-eng
- [[Monte Carlo Tree Search]] — domaines : ml-eng, ai-eng
- [[Offline RL]] — domaines : ml-eng
- [[Policy gradient]] — domaines : ml-eng, ai-eng
- [[PPO]] — domaines : ml-eng, ai-eng
- [[Q-learning and DQN]] — domaines : ml-eng
- [[Reinforcement learning]] — domaines : ml-eng, ai-eng
- [[Reward shaping and hacking]] — domaines : ml-eng, ai-eng
- [[Théorie des jeux]] — domaines : ml-eng, ai-eng
- [[Value functions]] — domaines : ml-eng

### Briques
- [[Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[Gymnasium]] — Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements.
- [[OpenSpiel]] — Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python.
- [[RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.
- [[Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.

### Comparatifs
- [[Comparatif - Reinforcement learning]]
<!-- AUTO:END -->

## Notes
