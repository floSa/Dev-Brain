---
galaxie: wiki
type: concept
nom: Multi-armed bandits
alias: [MAB, bandit manchot, bandits, Epsilon-Greedy, Thompson Sampling, exploration-exploitation]
categorie: concept/stats
domaines: [data-sci]
tags: [experimentation, multi-armed-bandit]
---

# Multi-armed bandits

## Aperçu

- Cadre d'allocation **dynamique** : à chaque étape on choisit un bras (variante), on observe une récompense, et on réajuste les choix futurs pour maximiser le gain cumulé.
- Arbitre en continu le dilemme exploration (tester les bras incertains) vs exploitation (jouer le meilleur connu).
- Vu comme un [[A-B testing|A/B test]] où le split n'est pas fixe : le trafic migre vers la variante qui gagne, ce qui réduit le coût d'opportunité.

## Concepts clés

### Exploration vs exploitation
- Tout exploiter → on reste coincé sur un bras sous-optimal mal estimé. Tout explorer → on gaspille du trafic sur des bras perdants. Un bon algorithme dose les deux.
- Objectif : minimiser le **regret** = écart cumulé au bras optimal.

### Epsilon-Greedy
- Avec probabilité $\varepsilon$ : choisir un bras au hasard (explorer). Sinon : jouer le bras d'estimation la plus haute (exploiter).
- Simple, mais $\varepsilon$ fixe explore autant en fin qu'en début ; un $\varepsilon$ décroissant corrige ce gaspillage.

### Thompson Sampling
- Bayésien : on garde une distribution a posteriori de la valeur de chaque bras, on en tire un échantillon, et on joue le bras au tirage le plus élevé.
- L'exploration émerge de l'incertitude : un bras mal connu est parfois tiré haut, donc testé. Très performant en pratique.

### UCB
- Upper Confidence Bound : jouer le bras maximisant moyenne + borne d'incertitude → optimisme face à l'incertitude.

## Les maths, simplement

- Regret : $R_T = \sum_{t=1}^{T}\big(\mu^{*} - \mu_{a_t}\big)$ — somme des écarts au meilleur bras $\mu^{*}$ ; on cherche à le rendre sous-linéaire en $T$.
- Thompson (récompense binaire) : a posteriori Beta $\;\theta_k \sim \mathrm{Beta}(\alpha_k + s_k,\; \beta_k + f_k)$ ($s_k$ succès, $f_k$ échecs) ; jouer $\arg\max_k$ d'un tirage.
- UCB1 : jouer $\arg\max_k \big(\hat{\mu}_k + \sqrt{2\ln t / n_k}\big)$ — le terme de droite gonfle pour les bras peu tirés.

## En pratique

- Pertinent quand exploiter tôt rapporte (campagnes courtes, contenus périssables, beaucoup de bras) ; moins adapté si on veut un effet propre et interprétable sur chaque variante.
- Récompense différée ou bruitée → l'allocation peut converger trop vite vers un faux gagnant ; ralentir l'apprentissage.
- Inférence post-hoc piégeuse : l'allocation adaptative casse l'i.i.d., les IC classiques par bras sont biaisés (sous-représentation des bras perdants).
- Variantes : bandits contextuels (la récompense dépend de features utilisateur) — pont vers le reinforcement learning.

## Approches voisines & alternatives

- [[A-B testing]] — split fixe, conçu pour mesurer proprement chaque variante ; le bandit privilégie le gain pendant le test.
- [[Sequential testing]] — autre réponse au « décider en continu », mais côté test d'hypothèse plutôt qu'allocation.
- [[Inégalités de concentration]] — Hoeffding/Chernoff fournissent la borne d'incertitude de l'UCB.
- [[Exploration vs exploitation]] — le dilemme que le bandit incarne sous sa forme la plus pure ($\varepsilon$-greedy, UCB, Thompson).
- [[Reinforcement learning]] — généralisation avec états et transitions ; le bandit en est le cas sans état.

## Pour aller plus loin

- Réf : Sutton & Barto — *Reinforcement Learning* (ch. bandits) ; Russo et al. — *A Tutorial on Thompson Sampling* (2018).
- Outils : implémentations `numpy` directes, `Vowpal Wabbit` (bandits contextuels), `River` (streaming).
