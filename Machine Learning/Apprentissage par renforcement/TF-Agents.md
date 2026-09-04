---
role: brique
nom: TF-Agents
alias: [tf-agents, tf agents, tensorflow agents]
pitch: "Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Stable-Baselines3]]", "[[Acme]]", "[[RLax]]"]
complements: []
tags: [reinforcement-learning]
url_docs: https://www.tensorflow.org/agents
url_repo: https://github.com/tensorflow/agents
---

# TF-Agents

<!-- AUTO:BANDEAU:START -->
> Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque RL **officielle** de l'écosystème [[TensorFlow]] : agents prêts à l'emploi (DQN et
variantes, C51, DDPG, TD3, SAC, PPO, REINFORCE), **bandits contextuels** — sa couverture la
plus distinctive —, drivers de collecte, replay buffers dont Reverb, et métriques, le tout sous
une API homogène (`TimeStep`, `tf_env`, `Agent`). C'est l'équivalent TensorFlow de
[[Stable-Baselines3]], à ceci près que l'écosystème TF entier perd du terrain face à PyTorch et
JAX, et la bibliothèque avec lui : dernière release stable 0.19.0 fin 2023, calée sur TF 2.15,
le développement continuant surtout en nightly à rythme faible. La politique entraînée
s'exporte en SavedModel vers TF Serving ou TFLite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Stack **TensorFlow imposée** — codebase, infra de serving TF existante — et besoin d'agents RL standards |  |
| **Bandits contextuels** en production : la couverture de TF-Agents reste une des plus complètes du genre | Parier sur le long terme : dernière release stable fin 2023 sur TF 2.15, les TF récents ne sont couverts par aucune release stable |
| Déployer la politique entraînée en **SavedModel** vers TF Serving / TFLite | **Couplage de versions strict** TF / tf-agents / dm-reverb : sortir de la matrice de compatibilité casse l'installation, et Reverb est Linux uniquement |
| | API verbeuse — specs, drivers, conversions `py_env` / `tf_env` — et tutoriels qui vieillissent sans correction systématique |

## Mise en œuvre

- Installation — `uv add tf-agents` ; respecter la matrice de compatibilité TF / tf-agents / dm-reverb
- Point d'entrée — API Python : `TimeStep`, `tf_env`, `Agent`, drivers de collecte
- Prérequis — [[TensorFlow]] à la version appariée ; Linux pour Reverb
- Exécution — single-node, ou collecte **distribuée** par architecture acteur-learner via Reverb
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- [[Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.

## Ressources

- Documentation — https://www.tensorflow.org/agents
- Dépôt — https://github.com/tensorflow/agents

## Voir aussi

- [[Reinforcement learning]] — la notion du dossier
- [[TensorFlow]] — l'écosystème parent, et sa trajectoire
- [[Gymnasium]] — les environnements consommés via les suites et wrappers (`suite_gym`)
- [[Q-learning and DQN]] — `DqnAgent`, C51 et variantes
- [[PPO]] · [[Policy gradient]] — `PPOAgent`, `ReinforceAgent`
- [[Actor-Critic methods]] — SAC, TD3, DDPG
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
