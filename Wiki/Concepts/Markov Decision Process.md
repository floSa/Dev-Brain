---
galaxie: wiki
type: concept
nom: Markov Decision Process
alias: [MDP, processus de décision markovien, processus décisionnel de Markov, Markov decision process]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, markov-decision-process, markov]
---

# Markov Decision Process

## Aperçu

- Cadre mathématique standard du [[Reinforcement learning|reinforcement learning]] : une [[Chaînes de Markov|chaîne de Markov]] enrichie d'**actions** et de **récompenses**. À chaque pas, l'agent choisit une action qui influence la transition vers l'état suivant et le gain reçu.
- Hypothèse fondatrice : la **propriété de Markov** — l'état présent résume tout le passé utile, le futur ne dépend que de l'état courant et de l'action choisie.

## Concepts clés

### Le quintuplet $(S, A, P, R, \gamma)$
- $S$ : ensemble des **états** ; $A$ : ensemble des **actions** disponibles.
- $P(s' \mid s, a)$ : **dynamique** de transition — probabilité d'arriver en $s'$ depuis $s$ en faisant $a$.
- $R(s, a)$ : **récompense** attendue ; $\gamma$ : facteur d'escompte du futur.

### Différence avec une chaîne de Markov
- Une [[Chaînes de Markov|chaîne de Markov]] évolue toute seule selon une matrice de transition fixe. Le MDP ajoute un **levier de décision** : l'action modifie la transition.
- Choisir une **politique** $\pi(a \mid s)$ revient à figer les actions → le MDP redevient une chaîne de Markov (la *Markov reward process* induite par $\pi$).

### Ce que le MDP permet de définir
- Une **politique** optimale $\pi^{*}$ et les [[Value functions|fonctions de valeur]] $V^{\pi}, Q^{\pi}$ associées.
- Les [[Bellman equations|équations de Bellman]], qui exploitent précisément la structure markovienne pour calculer ces valeurs de proche en proche.

## Les maths, simplement

- Propriété de Markov (avec action) : $P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \dots) = P(s_{t+1} \mid s_t, a_t)$ — l'historique n'apporte rien de plus.
- Objectif sur un MDP : $\max_{\pi}\; \mathbb{E}_{\pi}\!\left[\sum_{t\ge 0} \gamma^{t} R(s_t, a_t)\right]$ — maximiser le retour escompté espéré.
- Une politique $\pi$ + le MDP induisent une distribution sur les trajectoires $(s_0, a_0, s_1, a_1, \dots)$.

## En pratique

- Cadre de modélisation avant tout : poser un problème de contrôle séquentiel comme un MDP, c'est définir $S, A, P, R, \gamma$ — l'étape qui conditionne tout le reste.
- $P$ et $R$ connus → résolution exacte par programmation dynamique (cf. [[Bellman equations]]). $P$ et $R$ inconnus → c'est le RL : apprendre par interaction.
- Pièges : espace d'états trop grand (malédiction de la dimension), propriété de Markov violée (état mal défini → enrichir l'état), observation partielle (POMDP, état caché).

## Approches voisines & alternatives

- [[Chaînes de Markov]] — le MDP sans action ni récompense ; brique probabiliste sous-jacente.
- [[Reinforcement learning]] — résout un MDP dont la dynamique et les récompenses sont inconnues.
- [[Bellman equations]] — caractérisent les valeurs optimales sur un MDP.
- [[Value functions]] — les quantités qu'on cherche à estimer pour évaluer une politique.
- POMDP *(à créer)* — MDP à observation partielle, l'état n'est pas directement observé.

## Pour aller plus loin

- Sutton & Barto — *Reinforcement Learning*, ch. 3 (*Finite Markov Decision Processes*).
- Puterman — *Markov Decision Processes: Discrete Stochastic Dynamic Programming* (référence formelle).
