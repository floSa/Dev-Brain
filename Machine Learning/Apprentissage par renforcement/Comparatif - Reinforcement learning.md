---
role: comparatif
nom: Comparatif - Reinforcement learning
categorie: ml/rl
tags: [reinforcement-learning, self-play]
---

# Comparatif - Reinforcement learning

> On tranche sur : la couche dont on a besoin — l'environnement, l'agent tout fait ou la brique mathématique —, l'écosystème de calcul, et l'état de la maintenance.

![[Comparatif - Reinforcement learning.base]]

## Ce qui départage

- [[Gymnasium]] — ne fournit **aucun algorithme** : c'est le contrat `reset`/`step` entre un agent et son environnement, mono-agent, et le seul par lequel on expose son propre problème aux autres.
- [[OpenSpiel]] — le seul à couvrir l'information **imparfaite** et le multi-joueurs formel : 70+ jeux, CFR, MCTS et le calcul d'exploitabilité, sous une API à lui et non celle de Gymnasium.
- [[Stable-Baselines3]] — le clé en main PyTorch : `learn()` / `predict()`, code testé et **zoo d'hyperparamètres réglés** — c'est ce zoo, pas les défauts, qui fait la différence de résultat.
- [[Acme]] — structure un agent en acteurs / learners / replay pour passer du single-process aux centaines d'acteurs sans réécriture, mais Reverb et Launchpad sont **Linux seulement** et la dernière release date de 2022.
- [[RLax]] — la couche mathématique nue en JAX (pertes TD, λ-returns, V-trace) : ni agents, ni environnements, ni replay, ni boucle — tout le reste est à écrire.
- [[TF-Agents]] — l'équivalent SB3 côté TensorFlow, et le seul dont la couverture des **bandits contextuels** soit complète ; figé sur TF 2.15, avec un couplage de versions TF / tf-agents / Reverb strict.
