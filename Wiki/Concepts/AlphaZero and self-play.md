---
galaxie: wiki
type: concept
nom: AlphaZero and self-play
alias: [AlphaZero, self-play, jeu contre soi-même, AlphaGo Zero, MuZero, apprentissage par self-play]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [self-play, planning, deep-learning, reinforcement-learning]
---

# AlphaZero and self-play

## Aperçu

- Paradigme où l'agent apprend **uniquement en jouant contre lui-même**, sans données humaines : ses propres parties, de plus en plus fortes, fournissent son curriculum d'entraînement.
- **AlphaZero** combine ce self-play avec [[Monte Carlo Tree Search|MCTS]] et un réseau profond unique (politique + valeur), et atteint un niveau surhumain au Go, aux échecs et au shogi à partir des seules règles.

## Concepts clés

### La boucle de self-play

- Le réseau $f_\theta(s) = (\mathbf{p}, v)$ produit une politique a priori $\mathbf{p}$ (probabilité des coups) et une estimation de valeur d'état $v$ — à la différence de l'action-value $Q$ de [[Q-learning and DQN]].
- MCTS s'appuie sur $f_\theta$ pour guider la recherche et renvoie une politique améliorée $\boldsymbol\pi$ (issue des visites des nœuds). On joue le coup, on génère des parties entières.
- Le réseau est ré-entraîné pour rapprocher $\mathbf{p}$ de $\boldsymbol\pi$ et $v$ du résultat $z$ de la partie. MCTS agit donc comme un **opérateur d'amélioration de politique** (cf. [[Policy gradient]], [[Value functions]]).

### Pourquoi le self-play marche

- **Curriculum auto-généré** : l'adversaire a toujours exactement le niveau de l'agent → opposition ni triviale ni insurmontable, le signal d'apprentissage reste dense en permanence.
- Pas de plafond humain : le système peut dépasser toute connaissance humaine du jeu (les coups « extraterrestres » d'AlphaGo).

### La lignée

- **AlphaGo** (2016) : amorcé sur des parties humaines, deux réseaux ; bat Lee Sedol.
- **AlphaGo Zero** (2017) : zéro donnée humaine, un seul réseau, plus fort.
- **AlphaZero** (2018) : généralise à échecs et shogi, mêmes principes.
- **MuZero** (2020) : apprend en plus un **modèle** de la dynamique → planifie sans connaître les règles (cf. [[Model-based RL]]).

## Les maths, simplement

- Perte d'entraînement : $\ell = (z - v)^2 - \boldsymbol\pi^\top \log \mathbf{p} + c\lVert\theta\rVert^2$ — terme de valeur (régression sur l'issue $z$), terme de politique (entropie croisée vers la cible MCTS $\boldsymbol\pi$, cf. [[Cross-entropy]]), régularisation.
- Intuition : le réseau apprend à **prédire ce que la recherche va conclure** (politique) et **qui va gagner** (valeur) ; à l'itération suivante, une meilleure prédiction rend la recherche encore meilleure.

## En pratique

- Exige un **environnement à dynamique connue et simulable**, idéalement à somme nulle et deux joueurs — cf. [[Théorie des jeux]]. Hors de ce cadre, le self-play se transpose mal tel quel.
- Très **coûteux en calcul** : des millions de parties, du MCTS à chaque coup.
- L'idée essaime hors des jeux : auto-amélioration des LLM, génération de données par débats agent-contre-agent — cf. [[RL for LLMs]], [[GRPO]].
- En information imparfaite (poker), le self-play naïf ne converge pas vers l'équilibre → préférer [[Counterfactual Regret Minimization|CFR]].
- Côté outils : [[Dev/Services/OpenSpiel|OpenSpiel]] inclut une implémentation pédagogique d'AlphaZero (self-play + MCTS) sur ses jeux à information parfaite.

## Approches voisines & alternatives

- [[Monte Carlo Tree Search]] — le moteur de planification qu'AlphaZero guide par réseau.
- [[Policy gradient]] — autre lecture : MCTS améliore la politique, le réseau la généralise (itération politique).
- [[Value functions]] — la tête « valeur » du réseau, qui remplace les rollouts aléatoires.
- [[Model-based RL]] — MuZero apprend le modèle au lieu de le supposer connu.
- [[Counterfactual Regret Minimization]] — l'alternative en information imparfaite, où le self-play par MCTS échoue.

## Pour aller plus loin

- Silver et al. (2016, Nature) — *Mastering the game of Go with deep neural networks and tree search*.
- Silver et al. (2017, Nature) — *Mastering the game of Go without human knowledge* (AlphaGo Zero).
- Silver et al. (2018, Science) — *A general reinforcement learning algorithm that masters chess, shogi and Go through self-play* (AlphaZero).
- Schrittwieser et al. (2020, Nature) — *Mastering Atari, Go, chess and shogi by planning with a learned model* (MuZero).
