---
galaxie: wiki
type: concept
nom: MCMC
alias: [Markov chain Monte Carlo, Monte-Carlo par chaînes de Markov, Metropolis-Hastings, NUTS, Gibbs]
categorie: concept/stats
domaines: [data-sci]
tags: [monte-carlo, markov, bayesian]
---

# MCMC

## Aperçu

- Famille d'algorithmes qui **échantillonnent** une distribution connue seulement à une constante de normalisation près, en construisant une [[Chaînes de Markov|chaîne de Markov]] dont la loi stationnaire est la cible.
- Outil central de l'[[Inférence bayésienne]] : sert à approcher l'a posteriori quand il n'a pas de forme fermée.

## Concepts clés

### Le principe
- Concevoir une chaîne dont l'équilibre (la stationnaire) est exactement la distribution voulue, la laisser tourner, puis traiter ses états comme un échantillon de la cible.
- La [[Loi des grands nombres]] valide ensuite l'estimation des espérances par moyenne des échantillons.

### Metropolis–Hastings
- Proposer un nouvel état, l'accepter avec une probabilité qui dépend du rapport des densités cibles.
- La constante de normalisation s'annule dans le rapport → on n'a jamais besoin de l'évidence.

### Gibbs
- Cas particulier : échantillonner tour à tour chaque variable selon sa conditionnelle complète.
- Pratique quand ces conditionnelles sont des lois connues (souvent avec des [[A priori conjugués]]).

### HMC / NUTS
- Hamiltonian Monte Carlo utilise le gradient de la densité pour proposer des sauts longs et peu corrélés.
- NUTS (No-U-Turn) règle automatiquement la longueur de trajectoire — le moteur par défaut de Stan, PyMC, NumPyro.

### Diagnostics
- Burn-in (rejeter le début), autocorrélation, taille d'échantillon effective (ESS), $\hat{R}$ (Gelman–Rubin) proche de 1 sur plusieurs chaînes.

## Les maths, simplement

- Acceptation Metropolis–Hastings : $\alpha = \min\!\left(1,\ \dfrac{p(x')\,q(x \mid x')}{p(x)\,q(x' \mid x)}\right)$, où $p$ est la cible (non normalisée) et $q$ la loi de proposition.
- Comme seul le rapport $p(x')/p(x)$ intervient, le facteur $1/Z$ disparaît — d'où l'intérêt pour l'a posteriori bayésien dont l'évidence est intraitable.
- Équilibre détaillé $p(x)\,T(x\to x') = p(x')\,T(x'\to x)$ → garantit que $p$ est stationnaire.

## En pratique

- Outils : [[Dev/Services/PyMC|PyMC]], [[Dev/Services/Stan|Stan]] (`cmdstanpy`), NumPyro / Pyro ; spécifier le modèle, lancer plusieurs chaînes, vérifier $\hat{R}$ et l'ESS avec [[Dev/Services/ArviZ|ArviZ]].
- Coûteux et corrélé : surveiller le mélange ; reparamétrer (centré vs non centré) si la chaîne traîne.
- Alternatives : [[A priori conjugués]] (a posteriori exact, sans simulation) ; inférence variationnelle (approchée mais rapide, passe à l'échelle).

## Approches voisines & alternatives

- [[Chaînes de Markov]] — le mécanisme sous-jacent ; MCMC en exploite la convergence vers la stationnaire.
- [[Inférence bayésienne]] — le principal débouché : échantillonner l'a posteriori.
- [[A priori conjugués]] — quand ils s'appliquent, ils rendent le MCMC inutile (forme fermée).
- [[Loi des grands nombres]] — fonde l'estimation Monte-Carlo des espérances a posteriori.

## Pour aller plus loin

- Metropolis (1953), Hastings (1970), Gelman–Rubin ($\hat{R}$), Hoffman & Gelman (NUTS, 2014).
- Réf : Gelman et al. — *Bayesian Data Analysis* ; doc PyMC / Stan sur les diagnostics de convergence.
