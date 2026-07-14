---
galaxie: wiki
type: concept
nom: A priori conjugués
alias: [conjugate priors, conjugate prior, lois a priori conjuguées, prior conjugué, conjugaison]
categorie: concept/stats
domaines: [data-sci]
tags: [bayesian, prior]
---

# A priori conjugués

## Aperçu

- A priori choisi pour que l'a posteriori reste dans la **même famille** de lois que lui.
- Conséquence : la mise à jour bayésienne se réduit à une mise à jour de paramètres, en **forme fermée** — pas d'intégrale, pas de MCMC.
- Outil de tractabilité de l'[[Inférence bayésienne]], précieux pour les calculs analytiques et la mise à jour en ligne.

## Concepts clés

### Conjugaison
- Un a priori est conjugué d'une vraisemblance si la famille est stable par la mise à jour. Exemple : la loi Beta est conjuguée de la Bernoulli / Binomiale.

### Couples classiques
- Beta–Binomiale (proportions), Gamma–Poisson (taux d'événements), Normale–Normale (moyenne, variance connue), Dirichlet–Multinomiale (catégories).

### Pseudo-comptes
- Les hyperparamètres de l'a priori s'interprètent comme des observations « virtuelles » : $\text{Beta}(\alpha,\beta)$ ≈ $\alpha-1$ succès et $\beta-1$ échecs déjà vus. Peu de pseudo-comptes ⇒ a priori faiblement informatif.

## Les maths, simplement

- Beta–Binomiale : a priori $\theta \sim \text{Beta}(\alpha,\beta)$, données $k$ succès sur $n$ ⇒ a posteriori $\text{Beta}(\alpha+k,\ \beta+n-k)$.
- Forme générale : a posteriori = même famille, hyperparamètres mis à jour par les statistiques exhaustives des données.
- Gamma–Poisson : $\lambda\sim\text{Gamma}(\alpha,\beta)$, somme $S$ sur $n$ observations ⇒ a posteriori $\text{Gamma}(\alpha+S,\ \beta+n)$.
- L'évidence $P(D)$ — l'intégrale gênante du théorème de Bayes — devient calculable analytiquement.

## En pratique

- Idéal pour une mise à jour incrémentale et rapide : ex. Thompson sampling Beta–Bernoulli dans les [[Multi-armed bandits]], ou un [[A-B testing]] bayésien.
- Limite : la famille conjuguée peut ne pas refléter la vraie croyance a priori → on échange un peu de fidélité contre la tractabilité.
- Au-delà des modèles simples, aucun conjugué n'existe → recourir au MCMC (PyMC, Stan) ou à l'inférence variationnelle.
- Avec un a priori conjugué, le mode a posteriori — l'[[Estimation MAP|estimation MAP]] — a aussi une forme fermée.

## Approches voisines & alternatives

- [[Inférence bayésienne]] — la conjugaison est l'astuce qui la rend analytique.
- [[Estimation MAP]] — mode a posteriori en forme fermée quand l'a priori est conjugué.
- [[MCMC]] / inférence variationnelle — l'alternative générale quand aucun conjugué n'existe.

## Pour aller plus loin

- Couples conjugués classiques : Beta–Binomiale, Gamma–Poisson, Dirichlet–Multinomiale, Normale–Normale, Normale–Inverse-Gamma.
- Liens : [[Multi-armed bandits]] (Thompson sampling), [[A-B testing]] bayésien.
- Outils : `scipy.stats` (lois conjuguées), PyMC.
