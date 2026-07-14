---
galaxie: wiki
type: concept
nom: Wasserstein distance
alias: [Distance de Wasserstein, Wasserstein, earth mover's distance, EMD, distance du transport optimal]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [information-theory, optimal-transport]
---

# Wasserstein distance

## Aperçu

- Mesure la distance entre deux distributions comme le **coût minimal pour transporter** la masse de l'une vers l'autre — d'où le nom *earth mover's distance* (déplacer un tas de terre). C'est une **vraie métrique**.
- Atout décisif sur les divergences ([[KL divergence|KL]], [[Jensen-Shannon divergence|JS]]) : elle reste **informative même sans support commun**, et varie continûment avec le décalage entre distributions.

## Concepts clés

### Transport optimal
- Issue du problème de [[Optimal transport|transport optimal]] (Monge, Kantorovich) : trouver le plan de couplage $\gamma$ (transport conjoint de $p$ vers $q$) qui minimise le coût total de déplacement.
- $W_p$ : ordre $p$ du coût ($W_1$ = distance linéaire, $W_2$ = quadratique, liée aux moyennes/covariances).

### Géométrie de l'espace sous-jacent
- Contrairement aux divergences qui ne regardent que les valeurs de probabilité point par point, Wasserstein intègre la **distance géométrique** entre les points du support : déplacer la masse loin coûte plus cher que près.

### Dualité de Kantorovich
- $W_1$ admet une forme duale : $W_1(p,q) = \sup_{\|f\|_L \le 1} \mathbb E_p[f] - \mathbb E_q[f]$, supremum sur les fonctions 1-lipschitziennes. C'est ce qui rend $W_1$ optimisable par un réseau (WGAN).

## Les maths, simplement

- $W_p(p,q) = \Big(\inf_{\gamma \in \Pi(p,q)} \int \|x-y\|^p \, d\gamma(x,y)\Big)^{1/p}$, où $\Pi(p,q)$ = couplages de marges $p$ et $q$.
- En 1D, forme close simple : $W_1 = \int |F_p^{-1}(u) - F_q^{-1}(u)|\,du$ — aire entre les fonctions quantiles inverses.
- Deux gaussiennes : $W_2^2 = \|\mu_1-\mu_2\|^2 + \text{tr}\big(\Sigma_1 + \Sigma_2 - 2(\Sigma_2^{1/2}\Sigma_1\Sigma_2^{1/2})^{1/2}\big)$.

## En pratique

- **WGAN** : remplacer la [[Jensen-Shannon divergence|JS]] saturante par $W_1$ donne un gradient exploitable même quand générées et réelles ne se recouvrent pas → entraînement plus stable.
- **Métrique d'évaluation générative** : le FID (Fréchet Inception Distance) est une $W_2$ entre gaussiennes d'activations.
- **Détection de dérive** continue et lisse (la distance bouge proportionnellement au décalage), contrairement à la KL qui sature ou diverge.
- Coût de calcul élevé en grande dimension → approximations : **Sinkhorn** (transport régularisé par l'entropie), sliced-Wasserstein. Outils : `scipy.stats.wasserstein_distance` ([[Dev/Services/scipy.stats|SciPy]], cas 1D), POT (Python Optimal Transport).

## Approches voisines & alternatives

- [[Optimal transport]] — le problème d'optimisation dont cette distance est la valeur optimale.
- [[KL divergence]] — diverge quand les supports ne se recouvrent pas ; Wasserstein reste fini et informatif.
- [[Jensen-Shannon divergence]] — bornée mais saturante ; Wasserstein garde un gradient (raison du WGAN).
- [[Shannon entropy]] — la régularisation entropique (Sinkhorn) rend le transport optimal calculable rapidement.

## Pour aller plus loin

- Peyré & Cuturi (2019) — *Computational Optimal Transport* (référence moderne).
- Arjovsky, Chintala & Bottou (2017) — *Wasserstein GAN*.
