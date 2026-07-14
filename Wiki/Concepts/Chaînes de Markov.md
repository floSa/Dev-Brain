---
galaxie: wiki
type: concept
nom: Chaînes de Markov
alias: [Markov chains, propriété de Markov, Markov property]
categorie: concept/stats
domaines: [data-sci]
tags: [stochastic-process, markov, probability]
---

# Chaînes de Markov

## Aperçu

- Processus aléatoire dont l'état futur ne dépend que de l'état présent, pas du chemin parcouru pour y arriver — la **propriété de Markov** (« sans mémoire »).
- Décrit par une matrice de transition entre états ; brique des [[MCMC]], de PageRank, des files d'attente et des modèles de séquences.

## Concepts clés

### Propriété de Markov
- Tout le passé est résumé par l'état courant : connaître l'historique n'apporte rien de plus pour prédire le pas suivant.
- Hypothèse forte mais souvent réaliste (position, niveau de stock, état d'un système).

### Matrice de transition
- $P_{ij}$ = probabilité de passer de l'état $i$ à l'état $j$ ; chaque ligne somme à 1.
- La loi après $k$ pas se lit dans $P^k$.

### Distribution stationnaire
- Loi $\pi$ invariante par la dynamique : une fois atteinte, elle se reproduit pas après pas.
- C'est l'« équilibre » de long terme de la chaîne.

### Ergodicité
- Chaîne irréductible (tout état atteignable) et apériodique → convergence vers une **unique** stationnaire, quel que soit le point de départ.
- Cette convergence est exactement ce que le [[MCMC]] exploite pour échantillonner.

## Les maths, simplement

- Propriété de Markov : $P(X_{n+1}=j \mid X_n=i, X_{n-1},\dots) = P(X_{n+1}=j \mid X_n=i) = P_{ij}$.
- Évolution de la loi : $\mu_{n+1} = \mu_n P$, donc $\mu_n = \mu_0 P^{n}$.
- Stationnaire : $\pi P = \pi$ (vecteur propre à gauche de valeur propre 1).

## En pratique

- Temps discret + états finis ici ; en **temps continu**, les sauts mènent au [[Processus de Poisson]], la diffusion continue au [[Mouvement brownien]].
- Usages : MCMC (échantillonnage), PageRank (marche aléatoire sur le web), files d'attente, modèles de langage n-gram, fiabilité.
- Piège : la propriété de Markov est une hypothèse — si le futur dépend vraiment de l'historique, enrichir l'état (ordre supérieur) ou changer de modèle.

## Approches voisines & alternatives

- [[MCMC]] — construit une chaîne dont la stationnaire est la distribution cible à échantillonner ; moteurs : [[Dev/Services/PyMC|PyMC]], [[Dev/Services/Stan|Stan]].
- [[Processus de Poisson]] — chaîne de Markov à temps continu, à sauts (comptage).
- [[Mouvement brownien]] — processus de Markov à temps et espace continus (diffusion).
- [[Markov Decision Process]] — chaîne de Markov enrichie d'actions et de récompenses ; le cadre formel du reinforcement learning.
- Modèles de Markov cachés (HMM) — états non observés derrière des émissions.

## Pour aller plus loin

- Équilibre détaillé (réversibilité), théorème ergodique, temps de mélange (mixing time).
- Outils : `numpy` (puissances de matrice), `scipy.sparse` pour les grands espaces d'états.
