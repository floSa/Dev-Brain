---
galaxie: wiki
type: concept
nom: Model-based RL
alias: [model-based RL, RL basé modèle, model-based reinforcement learning, RL avec modèle, world models, planification]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, model-based-rl, dynamic-programming]
---

# Model-based RL

## Aperçu

- L'agent apprend (ou reçoit) un **modèle de la dynamique** $\hat{P}(s'\mid s,a)$ et de la récompense $\hat{R}$, puis s'en sert pour **planifier** ou pour générer des expériences simulées — au lieu d'apprendre uniquement par essais réels (*model-free*, cf. [[Q-learning and DQN]], [[Policy gradient]]).
- Argument central : la **sample-efficiency**. Un modèle permet de « rejouer » mentalement des transitions, donc d'extraire bien plus de chaque interaction réelle — décisif quand collecter des données coûte cher (robotique).

## Concepts clés

### Modèle connu vs appris
- **Modèle connu** : la dynamique est donnée (jeux à règles, simulateur). On planifie directement — c'est le terrain de la **recherche arborescente** (MCTS) et de la [[Bellman equations|programmation dynamique]].
- **Modèle appris** : on estime $\hat{P}, \hat{R}$ à partir des données, puis on planifie ou on entraîne une politique dessus. Le risque devient l'**erreur de modèle**.

### Planifier ou simuler
- **Planification** : utiliser le modèle au moment de décider (MCTS, model predictive control / MPC déroule le modèle sur un horizon et optimise la séquence d'actions).
- **Dyna** : architecture hybride — alterner apprentissage model-free sur données réelles **et** sur transitions imaginées par le modèle (Dyna-Q).
- **World models** : apprendre un modèle latent compact de l'environnement et y entraîner la politique « dans le rêve » (PlaNet, Dreamer, MuZero qui apprend un modèle implicite suffisant pour planifier).

### L'erreur de modèle (le talon d'Achille)
- Un modèle imparfait se fait **exploiter** par l'optimiseur : la politique trouve les zones où le modèle prédit, à tort, de fortes récompenses (*model exploitation*).
- Garde-fous : horizons de déroulé courts, ensembles de modèles (incertitude), MPC qui re-planifie à chaque pas.

## Les maths, simplement

- Boucle Dyna : après chaque transition réelle, mettre à jour le modèle $\hat{P}, \hat{R}$, puis faire $n$ mises à jour de valeur sur des transitions **simulées** $(s,a) \to \hat{P}, \hat{R}$ — la cible reste un backup de Bellman (cf. [[Bellman equations]]).
- Objectif MPC : à l'état courant, $\max_{a_{t:t+H}} \sum_{k=0}^{H} \gamma^{k}\, \hat{R}(s_{t+k}, a_{t+k})$ sous $s_{t+k+1} = \hat{P}(\cdot\mid s_{t+k}, a_{t+k})$ — optimiser une séquence sur un horizon $H$, n'exécuter que la première action, re-planifier.

## En pratique

- À privilégier quand les **interactions réelles sont rares / coûteuses** et qu'un modèle raisonnable est apprenable (dynamique physique, simulateur disponible).
- Plus complexe que le model-free : il faut entraîner et **valider** le modèle, gérer son incertitude, et l'erreur composée sur les longs horizons.
- Pièges : sur-confiance dans un modèle faux (model exploitation), coût de la planification en ligne (MCTS/MPC), distribution shift entre données d'entraînement du modèle et états visités par la nouvelle politique.

## Approches voisines & alternatives

- [[Bellman equations]] — la planification exacte (value/policy iteration) est le cas « modèle connu, petit espace ».
- [[Q-learning and DQN]], [[Policy gradient]] — les approches **model-free** : apprendre la politique/valeur sans modèle explicite, plus simples mais plus gourmandes en données.
- [[Actor-Critic methods]] — souvent la brique d'apprentissage utilisée *à l'intérieur* d'un world model (Dreamer).
- [[Markov Decision Process]] — c'est précisément $P$ et $R$ du MDP que le modèle cherche à approximer.

## Pour aller plus loin

- Sutton (1991) — *Dyna* (intégration apprentissage / planification).
- Hafner et al. (2020-2023) — *Dreamer* (world models, apprentissage en latent).
- Schrittwieser et al. (2020) — *MuZero* (planification avec modèle appris implicite).
- Sutton & Barto — *Reinforcement Learning*, ch. 8 (*Planning and Learning with Tabular Methods*).
