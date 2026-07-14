---
galaxie: dev
type: pattern
contexte: IA de jeu où la logique de règles et l'algorithme de décision sont découplés — le moteur joue les règles, l'agent décide.
created: 2026-06-11
modified: 2026-06-11
services_cles: [Gymnasium, Stable-Baselines3, PyTorch]
projets_appliques: []
tags: [pattern, reinforcement-learning, self-play, game-theory, planning]
---

# Pattern — Moteur de jeu pur + IA séparée

## Contexte

Développer une IA de jeu (jeu de plateau, jeu à somme nulle, simulation) sans coupler la **logique de jeu** et l'**algorithme de décision**. Le moteur sait jouer les règles ; l'IA décide quel coup jouer. Ce découplage rend possibles le self-play, les tests déterministes et le remplacement de l'agent (heuristique → MCTS → RL) sans toucher aux règles.

## Stack

- **Moteur de jeu pur** — Python pur, sans dépendance ML : état, coups légaux, transition, condition de fin. Déterministe et testable isolément.
- [[Gymnasium]] — interface standard environnement ↔ agent (`reset`/`step`, espaces d'observation/action), en wrapper autour du moteur
- [[Stable-Baselines3]] — algorithmes RL prêts (PPO, DQN…) quand l'agent apprend par renforcement
- [[PyTorch]] — réseau politique/valeur pour un MCTS ou un AlphaZero maison

## Décisions clés

### 1. Le moteur ne connaît pas l'IA
Il expose les règles et l'état, rien d'autre. L'agent (heuristique, MCTS, RL) se branche par-dessus. Inverser la dépendance — du code de décision qui fuit dans le moteur — casse les tests et rend le self-play impossible.

### 2. L'interface Gymnasium comme frontière
Standardiser l'échange env ↔ agent permet de substituer un agent aléatoire, un PPO ou un MCTS sans rien changer au moteur. La frontière est un contrat (espaces, récompense), pas un appel direct.

### 3. Self-play : génération et apprentissage séparés
Le moteur produit les parties ; l'entraînement les consomme. Deux boucles distinctes (cf. AlphaZero) : on peut paralléliser la génération et réentraîner sur un buffer sans coupler les deux rythmes.

## Pièges

- **Règles qui fuient dans l'agent** (ou l'inverse) → couplage, bugs de simulation difficiles à isoler.
- **Moteur non déterministe** (états cachés mal gérés, RNG non seedé) → reproductibilité perdue, debug RL quasi impossible.
- **Espaces d'observation/action mal définis** → l'agent apprend du bruit ou exploite une faille de modélisation plutôt que le jeu.

## Voir aussi

- Services : [[Gymnasium]], [[Stable-Baselines3]], [[PyTorch]]
- Concepts : [[Reinforcement learning]], [[Monte Carlo Tree Search]], [[AlphaZero and self-play]], [[Markov Decision Process]], [[Théorie des jeux]], [[Counterfactual Regret Minimization]]
