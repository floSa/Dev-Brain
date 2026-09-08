---
role: brique
nom: Gymnasium
alias: [gymnasium, gym, openai gym, farama gymnasium]
pitch: "Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[OpenSpiel]]"]
complements: ["[[Stable-Baselines3]]"]
tags: [reinforcement-learning]
url_docs: https://gymnasium.farama.org/
url_repo: https://github.com/Farama-Foundation/Gymnasium
---

# Gymnasium

<!-- AUTO:BANDEAU:START -->
> Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-04-22 |
<!-- AUTO:BANDEAU:END -->

## Définition

**Standard d'API** pour les environnements de [[Reinforcement learning|RL]] à agent unique. Un
environnement expose `reset()`, qui rend l'état initial, et `step(action)`, qui rend
`(observation, reward, terminated, truncated, info)`, avec des `spaces` typés (`Discrete`,
`Box`…) décrivant observations et actions. C'est le **contrat commun** entre un agent et son
environnement — ce qui rend les algorithmes interchangeables. La distinction `terminated`
(fin naturelle de l'épisode) / `truncated` (coupure par limite de temps) est la rupture
majeure avec l'ancien OpenAI Gym, et elle se répercute dans le calcul des cibles RL. Successeur
maintenu de Gym, repris par la **Farama Foundation** en 2022, il fournit aussi un catalogue
d'environnements de référence.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exposer son propre problème (simulation, jeu, contrôle) derrière l'API `Env` pour le rendre compatible avec les libs RL | L'API est **mono-agent** par construction : les jeux formels, multi-joueurs ou à information imparfaite relèvent d'[[OpenSpiel]] ; le multi-agents général, de PettingZoo (même fondation, pas encore en fiche) |
| Brancher un agent sur un environnement standardisé | **Aucun algorithme** d'apprentissage n'est fourni : Gymnasium ne livre que les environnements → [[Stable-Baselines3]] pour entraîner |
| Prototyper ou benchmarker sur les environnements de référence (CartPole, MountainCar, LunarLander, MuJoCo) | Code historique figé sur l'ancien `gym` : le passage à `terminated` / `truncated` est une migration à valider, pas un simple changement d'import |
| Composer des wrappers (normalisation, frame stacking, time limit) et vectoriser les environnements pour une collecte parallèle | Les environnements lourds (MuJoCo, Atari) tirent des **dépendances natives** — installation à préparer, pas un simple `add` |

## Mise en œuvre

- Installation — `uv add gymnasium` ; extras selon le catalogue visé (`gymnasium[box2d]`, `[mujoco]`, `[atari]`…)
- Point d'entrée — `gymnasium.make("CartPole-v1")`, puis la boucle `reset` / `step` ; `reset(seed=...)` pour la reproductibilité, l'aléa par état global de l'ancien Gym ayant disparu
- Prérequis — Python seul pour les environnements de base ; bibliothèques natives pour MuJoCo et Atari
- Exécution — single-node ; la vectorisation parallélise la simulation sur une machine
- Coût — gratuit, MIT, rien à héberger ; maintenu par la Farama Foundation, association à but non lucratif

## Écosystème

### Alternatives

- [[OpenSpiel]] — Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python.
- PettingZoo — l'API multi-agents de la même fondation (pas encore en fiche).
- dm_env / dm_control — le contrat d'environnement de DeepMind (pas encore en fiche).

### Compléments

- [[Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter — les algorithmes qui consomment ces environnements.

## Ressources

- Documentation — https://gymnasium.farama.org/
- Dépôt — https://github.com/Farama-Foundation/Gymnasium

## Voir aussi

- [[Reinforcement learning]] — la notion du dossier : le cadre agent-environnement que cette API matérialise
- [[TF-Agents]] — les consomme aussi, via ses suites et wrappers (`suite_gym`)
- [[Markov Decision Process]] — `step` / `reset` et les `spaces` traduisent directement états, actions et transitions d'un MDP
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
