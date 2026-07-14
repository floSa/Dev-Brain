---
galaxie: wiki
type: concept
nom: Bellman equations
alias: [équations de Bellman, équation de Bellman, Bellman equation, Bellman optimality, optimalité de Bellman, Bellman backup]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, dynamic-programming, value-function]
---

# Bellman equations

## Aperçu

- Relation **récursive** qui relie la valeur d'un état à celle de ses successeurs : la valeur d'aujourd'hui = récompense immédiate + valeur escomptée de demain.
- Pierre angulaire du [[Reinforcement learning|RL]] : elle décompose un problème d'horizon infini en un pas local, ce qui rend les [[Value functions|fonctions de valeur]] calculables.

## Concepts clés

### Équation d'évaluation (politique fixée)
- Pour une politique $\pi$ donnée, $V^{\pi}$ se définit en fonction d'elle-même : la valeur d'un état dépend de la valeur des états atteints ensuite.
- Système d'équations linéaires (un par état) — résoluble exactement si la dynamique est connue.

### Équation d'optimalité
- Caractérise la **meilleure** valeur atteignable $V^{*}$ / $Q^{*}$ : au lieu de moyenner sur $\pi$, on prend le **max** sur les actions.
- Non linéaire (à cause du $\max$), mais elle a une solution unique — c'est elle qu'on cherche à résoudre.

### Programmation dynamique
- Appliquer l'équation de Bellman comme une **mise à jour itérative** (un *backup*) converge vers la valeur :
  - **value iteration** : itérer le backup d'optimalité jusqu'au point fixe ;
  - **policy iteration** : alterner évaluation (Bellman d'évaluation) et amélioration gloutonne.
- Le **TD learning** est un backup de Bellman échantillonné quand la dynamique est inconnue (cf. [[Value functions]]).

## Les maths, simplement

- Bellman d'évaluation : $V^{\pi}(s) = \sum_{a}\pi(a\mid s)\sum_{s'} P(s'\mid s,a)\big[R(s,a) + \gamma V^{\pi}(s')\big]$.
- Bellman d'optimalité : $V^{*}(s) = \max_{a} \sum_{s'} P(s'\mid s,a)\big[R(s,a) + \gamma V^{*}(s')\big]$.
- Forme $Q$ (la plus utilisée en RL) : $Q^{*}(s,a) = \sum_{s'} P(s'\mid s,a)\big[R(s,a) + \gamma \max_{a'} Q^{*}(s',a')\big]$.
- Le terme $R + \gamma V(s')$ est la **cible** ; l'écart à l'estimation courante est l'**erreur TD**.

## En pratique

- Dynamique $P, R$ connue + petit espace → programmation dynamique exacte (value/policy iteration).
- Dynamique inconnue ou espace immense → on **échantillonne** le backup ([[Q-learning and DQN|Q-learning]], TD) et on **approxime** $V$/$Q$ par un réseau ([[Q-learning and DQN|DQN]]).
- Pièges : combiner approximation de fonction + bootstrap + off-policy = la *deadly triad*, source classique de divergence ; le facteur $\gamma$ contrôle la stabilité (contraction de facteur $\gamma$).

## Approches voisines & alternatives

- [[Value functions]] — les quantités que ces équations définissent et permettent de calculer.
- [[Markov Decision Process]] — la structure markovienne est ce qui rend la récursion valide.
- [[Reinforcement learning]] — la plupart des algorithmes sont des façons d'approcher une équation de Bellman.
- Programmation dynamique classique (Bellman, 1957) — origine des équations, au-delà du RL (plus court chemin, contrôle optimal).

## Pour aller plus loin

- Sutton & Barto — *Reinforcement Learning*, ch. 3-4 (équations de Bellman, programmation dynamique).
- Bellman (1957) — *Dynamic Programming* (source historique).
