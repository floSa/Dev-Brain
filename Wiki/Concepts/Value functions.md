---
galaxie: wiki
type: concept
nom: Value functions
alias: [fonctions de valeur, fonction de valeur, value function, V-function, Q-function, fonction Q, fonction de valeur d'état-action]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, value-function]
---

# Value functions

## Aperçu

- Une fonction de valeur mesure « combien vaut » une situation : la récompense **cumulée espérée** qu'un agent obtiendra à partir de là, en suivant une politique donnée.
- C'est le cœur des méthodes de [[Reinforcement learning|RL]] basées valeur : une fois la valeur connue, agir bien revient à choisir l'option de plus haute valeur.

## Concepts clés

### Fonction de valeur d'état $V^{\pi}(s)$
- Valeur d'un **état** sous la politique $\pi$ : le retour escompté espéré en partant de $s$ et en suivant $\pi$ ensuite.
- Répond à « à quel point cet état est-il prometteur ? ».

### Fonction de valeur d'action $Q^{\pi}(s, a)$
- Valeur d'une **paire état-action** : retour espéré en faisant $a$ dans $s$, puis en suivant $\pi$.
- Plus directement actionnable : comparer les $Q(s, \cdot)$ donne la meilleure action sans connaître la dynamique. Base de [[Q-learning and DQN]].

### Avantage et valeurs optimales
- **Avantage** $A^{\pi}(s,a) = Q^{\pi}(s,a) - V^{\pi}(s)$ : combien l'action $a$ fait mieux que la moyenne en $s$ — central en [[Actor-Critic methods|acteur-critique]] et [[Policy gradient]].
- $V^{*}, Q^{*}$ : valeurs sous la **politique optimale**. Les connaître, c'est résoudre le problème — elles vérifient les [[Bellman equations|équations de Bellman]] optimales.

## Les maths, simplement

- $V^{\pi}(s) = \mathbb{E}_{\pi}\!\left[\sum_{k\ge 0}\gamma^{k} r_{t+k+1} \mid s_t = s\right]$ — retour escompté espéré depuis $s$.
- $Q^{\pi}(s,a) = \mathbb{E}_{\pi}\!\left[\sum_{k\ge 0}\gamma^{k} r_{t+k+1} \mid s_t = s,\, a_t = a\right]$ — idem en fixant la première action.
- Lien : $V^{\pi}(s) = \sum_{a} \pi(a\mid s)\, Q^{\pi}(s,a)$ — la valeur d'état est la moyenne des valeurs d'action sous $\pi$.
- Politique gloutonne optimale : $\pi^{*}(s) = \arg\max_{a} Q^{*}(s,a)$.

## En pratique

- Petits espaces discrets → valeurs stockées dans un tableau (tabulaire). Grands espaces → **approximation de fonction** (réseau de neurones : [[Q-learning and DQN|DQN]]), au prix de l'instabilité.
- Estimation par **Monte-Carlo** (retours complets d'épisodes, sans biais, variance élevée) ou par **TD learning** (différence temporelle, bootstrap sur l'estimation courante, biaisé mais efficace).
- Piège : surestimation des $Q$ (maximisation sur des estimations bruitées) → Double Q-learning ; et la valeur dépend de $\pi$ — changer de politique invalide les valeurs apprises.

## Approches voisines & alternatives

- [[Bellman equations]] — la relation récursive qui définit et permet de calculer ces fonctions.
- [[Reinforcement learning]] — les méthodes basées valeur estiment $V$/$Q$ pour en déduire la politique.
- [[Markov Decision Process]] — cadre où ces espérances sont bien définies.
- [[Policy gradient|Méthodes basées politique]] — optimisent $\pi$ directement, sans passer par une valeur explicite (souvent guidées par l'avantage).

## Pour aller plus loin

- Sutton & Barto — *Reinforcement Learning*, ch. 3-6 (valeurs, prédiction TD, contrôle).
- Mnih et al. (2015) — *Human-level control through deep RL* (DQN, approximation de $Q$).
