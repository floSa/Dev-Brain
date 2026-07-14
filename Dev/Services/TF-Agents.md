---
galaxie: dev
type: service
nom: TF-Agents
alias: [tf-agents, tf agents, tensorflow agents]
pitch: "Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Stable-Baselines3|Stable-Baselines3]]", "[[Dev/Services/Acme|Acme]]", "[[Dev/Services/RLax|RLax]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning]
url_docs: https://www.tensorflow.org/agents
url_repo: https://github.com/tensorflow/agents
---

# TF-Agents

## Pourquoi

Bibliothèque RL **officielle** de l'écosystème [[Dev/Services/TensorFlow|TensorFlow]] : agents prêts à l'emploi (DQN et variantes, C51, DDPG, TD3, SAC, PPO, REINFORCE), **bandits contextuels** (un point fort distinctif), drivers de collecte, replay buffers (dont Reverb) et métriques, le tout sous une API homogène (`TimeStep`, `tf_env`, `Agent`). C'est l'équivalent TensorFlow de [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] — avec la réserve que l'écosystème TF entier perd du terrain face à PyTorch et JAX, et la lib avec lui.

## Quand l'utiliser

- Stack **TensorFlow imposée** (codebase, infra de serving TF existante) et besoin d'agents RL standards.
- **Bandits contextuels** en production : la couverture bandits de TF-Agents reste une des plus complètes du genre.
- Déploiement de la politique entraînée en **SavedModel** vers TF Serving / TFLite.

## Quand NE PAS l'utiliser

- **Nouveau projet sans contrainte TF** → [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] : communauté, maintenance et écosystème (PyTorch) nettement plus vivants.
- Recherche moderne en JAX → [[Dev/Services/Acme|Acme]] ou [[Dev/Services/RLax|RLax]].
- Parier sur le long terme : la maintenance décline (dernière release stable 0.19.0 fin 2023, calée sur TF 2.15) — l'adopter aujourd'hui, c'est hériter de ce déclin.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add tf-agents`. Rien à héberger.
- Collecte **distribuée** possible (architecture acteur-learner via Reverb) en plus du mode single-node.
- Maintenance en **déclin** : dernière release stable fin 2023 (TF 2.15), le développement continue surtout en nightly, à un rythme faible. L'écosystème TensorFlow suit la même pente.

## Pièges

- **Couplage de versions strict** TF / tf-agents / dm-reverb : sortir de la matrice de compatibilité casse l'installation ; Reverb est Linux uniquement.
- Dernière release figée sur **TF 2.15** : les TF récents ne sont pas couverts par une release stable.
- API verbeuse (specs, drivers, conversions `py_env` / `tf_env`) — courbe d'apprentissage plus raide que SB3 pour le même résultat.
- Tutoriels et docs qui **vieillissent** sans correction systématique.

## Alternatives

- [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[Dev/Services/Acme|Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[Dev/Services/RLax|RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.

Nuance : à périmètre égal (agents prêts à l'emploi), SB3 est le choix par défaut en 2026 ; TF-Agents ne se justifie que par une contrainte TensorFlow ou le besoin de bandits contextuels.

## Liens

- [[Dev/Services/TensorFlow|TensorFlow]] — l'écosystème parent (et sa trajectoire).
- [[Dev/Services/Gymnasium|Gymnasium]] — environnements utilisables via les suites/wrappers (`suite_gym`).
- [[Reinforcement learning]] — le cadre général.
- [[Q-learning and DQN]] — `DqnAgent`, C51 et variantes.
- [[PPO]] · [[Policy gradient]] — `PPOAgent`, `ReinforceAgent`.
- [[Actor-Critic methods]] — SAC, TD3, DDPG.
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- Doc : https://www.tensorflow.org/agents
