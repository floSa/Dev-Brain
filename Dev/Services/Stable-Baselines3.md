---
galaxie: dev
type: service
nom: Stable-Baselines3
alias: [SB3, stable-baselines3, stable baselines 3, sb3]
pitch: "Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Acme|Acme]]", "[[Dev/Services/TF-Agents|TF-Agents]]", "[[Dev/Services/RLax|RLax]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning, deep-learning]
url_docs: https://stable-baselines3.readthedocs.io/
url_repo: https://github.com/DLR-RM/stable-baselines3
---

# Stable-Baselines3

## Pourquoi

Collection d'**implémentations de référence** d'algorithmes de [[Reinforcement learning|RL]] en [[Dev/Services/PyTorch|PyTorch]], pensées pour être **fiables et reproductibles** : code testé, couvert et documenté, avec des hyperparamètres réglés par algorithme (le « zoo »). On instancie un algorithme (`PPO`, `DQN`…), on lui passe un environnement [[Dev/Services/Gymnasium|Gymnasium]], puis `learn()` / `predict()` font le reste — une API volontairement proche de scikit-learn. Successeur PyTorch de Stable Baselines (lui-même fork d'OpenAI Baselines).

## Quand l'utiliser

- **Entraîner un agent sans réimplémenter** : PPO, A2C, DQN, SAC, TD3, DDPG dans le cœur ; variantes (QR-DQN, TQC, TRPO, RecurrentPPO, Maskable PPO, ARS, CrossQ) dans **SB3-Contrib**.
- **Baseline solide** pour démarrer ou comparer un projet de contrôle, robotique, jeux.
- **Reproductibilité** : hyperparamètres documentés (RL Baselines3 Zoo), seeds, évaluation standardisée.

## Quand NE PAS l'utiliser

- RL **distribué** à grande échelle (milliers d'acteurs) → RLlib (Ray) ou des frameworks orientés throughput (hors brain).
- Recherche sur un algorithme **nouveau** / très custom → implémentation minimale type CleanRL, ou from scratch sur [[Dev/Services/PyTorch|PyTorch]].
- Post-training **RL des LLM** (RLHF / GRPO) → outils dédiés (TRL…), pas SB3.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add stable-baselines3` (Python 3.10+). Rien à héberger.
- Maintenue par le **DLR-RM** (German Aerospace Center). Calcul porté par PyTorch (CPU / GPU).
- **Single-node** : la parallélisation est celle des environnements vectorisés (`VecEnv`), pas un entraînement multi-nœuds.

## Pièges

- L'efficacité tient surtout aux **hyperparamètres** : partir du zoo plutôt que des valeurs par défaut.
- Bien **vectoriser** les environnements (`VecEnv`) et normaliser observations/récompenses (`VecNormalize`) — sinon apprentissage lent ou instable.
- On-policy (PPO / A2C) vs off-policy (DQN / SAC / TD3) : budget d'interactions et réglages très différents.
- Migration **Gym → Gymnasium** : les versions récentes attendent l'API Gymnasium (`terminated` / `truncated`).

## Alternatives

- [[Dev/Services/Acme|Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[Dev/Services/TF-Agents|TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- [[Dev/Services/RLax|RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.

Nuance : SB3 est le **clé en main** maintenu ; les trois autres sont des choix de niche (contrainte TF, recherche JAX) à la maintenance plus fragile. En dehors du brain : RLlib (RL distribué, Ray), CleanRL (implémentations mono-fichier pour la recherche), Tianshou.

## Liens

- [[Dev/Services/Gymnasium|Gymnasium]] — l'API d'environnements sur laquelle SB3 entraîne ses agents.
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- [[Dev/Services/PyTorch|PyTorch]] — le framework de calcul sous-jacent.
- [[Reinforcement learning]] — le cadre théorique (agent, politique, récompense).
- [[PPO]] — l'algorithme on-policy phare de SB3.
- [[Q-learning and DQN]] — la famille basée valeur (`DQN`, `QR-DQN`).
- [[Actor-Critic methods]] — socle de `A2C`, `SAC`, `TD3`, `DDPG`.
- Doc : https://stable-baselines3.readthedocs.io/
