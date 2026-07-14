---
galaxie: dev
type: service
nom: Gymnasium
alias: [gymnasium, gym, openai gym, farama gymnasium]
pitch: "Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/OpenSpiel|OpenSpiel]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning]
url_docs: https://gymnasium.farama.org/
url_repo: https://github.com/Farama-Foundation/Gymnasium
---

# Gymnasium

## Pourquoi

**Standard d'API** pour les environnements de [[Reinforcement learning|RL]] à agent unique : un environnement expose `reset()` (état initial) et `step(action)` qui renvoie `(observation, reward, terminated, truncated, info)`, avec des `spaces` typés (`Discrete`, `Box`…) décrivant observations et actions. C'est le **contrat commun** entre un agent et son environnement — ce qui rend les algorithmes interchangeables. Gymnasium est le successeur **maintenu** d'OpenAI Gym (repris par la **Farama Foundation** en 2022) ; il fournit aussi un catalogue d'environnements de référence (classic control, Box2D, MuJoCo, Atari via dépendances).

## Quand l'utiliser

- **Brancher un agent** sur un environnement standardisé, ou **exposer son propre problème** (simulation, jeu, contrôle) derrière l'API `Env` pour le rendre compatible avec les libs RL.
- Utiliser des **environnements de référence** pour prototyper / benchmarker (CartPole, MountainCar, LunarLander, MuJoCo…).
- Composer des **wrappers** (normalisation, frame stacking, time limit) et **vectoriser** les environnements pour une collecte parallèle.

## Quand NE PAS l'utiliser

- RL **multi-agents** → PettingZoo (même fondation), pas Gymnasium (mono-agent) ; jeux formels et information imparfaite → [[Dev/Services/OpenSpiel|OpenSpiel]].
- Besoin des **algorithmes** d'apprentissage : Gymnasium ne fournit que les environnements → [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] pour entraîner.
- Code historique figé sur l'ancien `gym` : valider la migration (`terminated` / `truncated`) avant de basculer.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add gymnasium` (extras : `gymnasium[box2d]`, `[mujoco]`, `[atari]`…). Rien à héberger.
- Maintenue par la **Farama Foundation** (association à but non lucratif ; écosystème RL : PettingZoo, Minari, Gymnasium-Robotics).
- **Single-node** ; la vectorisation parallélise la simulation sur une machine.

## Pièges

- **API Gym → Gymnasium** : `step` renvoie désormais `terminated` **et** `truncated` (fin naturelle vs coupure de temps) — distinction à respecter dans les calculs de cible RL.
- `reset(seed=...)` pour la reproductibilité ; l'aléa par état global de l'ancien Gym a disparu.
- Les environnements lourds (MuJoCo, Atari) tirent des **dépendances natives** : installer les bons extras.

## Alternatives

- [[Dev/Services/OpenSpiel|OpenSpiel]] — Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python.

Nuance : Gymnasium pour le mono-agent standard, OpenSpiel dès que le problème est un jeu multi-joueurs ou à information imparfaite. En dehors du brain : PettingZoo (multi-agents, même fondation), dm_env / dm_control (DeepMind).

## Liens

- [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] — les algorithmes RL qui consomment les environnements Gymnasium.
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- [[Reinforcement learning]] — le cadre agent-environnement que cette API matérialise.
- [[Markov Decision Process]] — `step` / `reset` et les `spaces` traduisent directement états, actions et transitions d'un MDP.
- Doc : https://gymnasium.farama.org/
