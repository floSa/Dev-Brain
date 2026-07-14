---
galaxie: wiki
type: concept
nom: Théorie des jeux
alias: [game theory, théorie des jeux, équilibre de Nash, Nash equilibrium, jeu à somme nulle, zero-sum, information imparfaite, minimax]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [game-theory, optimization]
---

# Théorie des jeux

## Aperçu

- Étude mathématique des **décisions stratégiques** : plusieurs agents aux objectifs propres, dont les gains dépendent des choix de tous. L'outil pour raisonner sur l'interaction, là où le RL mono-agent suppose un environnement fixe.
- Fournit le socle conceptuel des systèmes multi-agents en IA — équilibres, somme nulle, information imparfaite — et les cibles que visent le [[AlphaZero and self-play|self-play]] et [[Counterfactual Regret Minimization|CFR]].

## Concepts clés

### Équilibre de Nash

- Profil de stratégies où **aucun joueur n'a intérêt à dévier** unilatéralement : chacun joue au mieux compte tenu des autres.
- Existe toujours en stratégies **mixtes** (distributions sur les actions) — théorème de Nash (1950). N'est ni forcément unique ni collectivement optimal (cf. dilemme du prisonnier).

### Somme nulle et minimax

- **Jeu à somme nulle** : le gain de l'un est la perte de l'autre (échecs, poker heads-up). Le cas le plus traitable.
- **Théorème minimax** (von Neumann, 1928) : en somme nulle à deux joueurs, $\max\min = \min\max$ → il existe une valeur du jeu et des stratégies optimales. C'est ce qui rend le self-play convergent dans ce cadre.

### Information parfaite vs imparfaite

- **Parfaite** : tout l'état est connu de tous (Go, échecs) → résoluble par recherche dans l'arbre ([[Monte Carlo Tree Search|MCTS]], minimax).
- **Imparfaite** : information cachée (cartes, coups simultanés) → notion d'**information set**, et il faut souvent **randomiser** sa stratégie (bluffer). [[Counterfactual Regret Minimization|CFR]] y calcule l'équilibre.

## Les maths, simplement

- Équilibre de Nash : un profil $\sigma^* = (\sigma_i^*, \sigma_{-i}^*)$ tel que $\forall i,\; u_i(\sigma_i^*, \sigma_{-i}^*) \ge u_i(\sigma_i, \sigma_{-i}^*)$ — nul ne gagne à dévier seul ($u_i$ = gain du joueur $i$, $-i$ = les autres).
- Minimax (somme nulle) : valeur du jeu $v = \max_{\sigma_1}\min_{\sigma_2} u_1(\sigma_1,\sigma_2) = \min_{\sigma_2}\max_{\sigma_1} u_1(\sigma_1,\sigma_2)$ — calculable par programmation linéaire ou par minimisation du regret (cf. [[Counterfactual Regret Minimization|CFR]]).

## En pratique

- En IA : **multi-agent RL**, mécanismes d'enchères, robustesse adversariale, sécurité (jeux attaquant/défenseur), et les [[GANs]] (générateur vs discriminateur, un jeu à somme nulle).
- Le **self-play** exploite la structure somme nulle pour générer un curriculum convergent ([[AlphaZero and self-play]]) ; en information imparfaite, il faut passer par la minimisation du regret ([[Counterfactual Regret Minimization]]).
- Pièges : l'équilibre de Nash devient **intraitable** à calculer hors somme nulle ou au-delà de deux joueurs ; un équilibre n'est pas un optimum social ; l'hypothèse de rationalité parfaite est forte.
- Côté outils : [[Dev/Services/OpenSpiel|OpenSpiel]] — 70+ jeux et les algorithmes d'équilibre (CFR, fictitious play, best response / exploitabilité).

## Approches voisines & alternatives

- [[Counterfactual Regret Minimization]] — méthode constructive pour l'équilibre en information imparfaite.
- [[AlphaZero and self-play]] — exploite le minimax somme nulle en information parfaite.
- [[Monte Carlo Tree Search]] — recherche dans l'arbre de jeu (information parfaite).
- [[Reinforcement learning]] — le cas mono-agent (un joueur contre un environnement) ; la théorie des jeux en est la généralisation multi-agents.
- [[Multi-armed bandits]] — décision séquentielle sans adversaire, via le regret.

## Pour aller plus loin

- von Neumann & Morgenstern (1944) — *Theory of Games and Economic Behavior*.
- Nash (1950) — *Equilibrium Points in N-Person Games*.
- Shoham & Leyton-Brown (2009) — *Multiagent Systems* (jeux et apprentissage).
- Connexions brain : [[AlphaZero and self-play]], [[Counterfactual Regret Minimization]], [[Monte Carlo Tree Search]].
