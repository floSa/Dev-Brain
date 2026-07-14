---
galaxie: wiki
type: concept
nom: KL divergence
alias: [Divergence de Kullback-Leibler, Kullback-Leibler, KL, relative entropy, entropie relative, divergence KL]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [information-theory, kl-divergence]
---

# KL divergence

## Aperçu

- Mesure l'**écart dirigé** d'une distribution $q$ à une distribution de référence $p$ : le surcoût d'information payé quand on encode $p$ en croyant que c'est $q$.
- Pierre angulaire de l'apprentissage probabiliste : entraîner par maximum de vraisemblance, par [[Cross-entropy|entropie croisée]] ou par inférence variationnelle revient à minimiser une KL.

## Concepts clés

### Asymétrie : ce n'est pas une distance
- $D_{KL}(p\,\|\,q) \ne D_{KL}(q\,\|\,p)$ et l'inégalité triangulaire ne tient pas. C'est une **divergence**, pas une métrique. Pour un substitut symétrique, voir la [[Jensen-Shannon divergence]] ou la [[Wasserstein distance]].
- Toujours $\ge 0$ (inégalité de Gibbs), nulle ssi $p = q$ presque partout.

### Forward vs reverse KL
- **Forward** $D_{KL}(p\,\|\,q)$ (« mean-seeking ») : $q$ doit couvrir tout le support de $p$ → tend à étaler $q$. C'est la KL minimisée par le maximum de vraisemblance.
- **Reverse** $D_{KL}(q\,\|\,p)$ (« mode-seeking ») : $q$ se concentre sur un mode → tend à sous-estimer la variance. C'est celle de l'inférence variationnelle.

### Lien à l'entropie croisée
- $D_{KL}(p\,\|\,q) = H(p,q) - H(p)$ : divergence = entropie croisée − entropie de $p$. L'entropie de $p$ étant fixe, minimiser l'une minimise l'autre.

## Les maths, simplement

- $D_{KL}(p\,\|\,q) = \sum_i p_i \log\dfrac{p_i}{q_i}$ (discret) ; $\int p(x)\log\dfrac{p(x)}{q(x)}\,dx$ (continu).
- Cas gaussien (forme close) : entre $\mathcal N(\mu_1,\sigma_1^2)$ et $\mathcal N(\mu_2,\sigma_2^2)$, $D_{KL} = \log\dfrac{\sigma_2}{\sigma_1} + \dfrac{\sigma_1^2 + (\mu_1-\mu_2)^2}{2\sigma_2^2} - \dfrac12$.
- Attention au support : si $q_i = 0$ là où $p_i > 0$, la divergence explose ($+\infty$) — d'où le lissage des distributions estimées.

## En pratique

- **Inférence bayésienne / variationnelle** : l'ELBO maximisé en VI est exactement la log-évidence moins $D_{KL}$ entre l'approximation et l'a posteriori vrai (cf. [[Inférence bayésienne]]).
- **Régularisation d'alignement** : RLHF/PPO pénalisent la KL entre la politique entraînée et le modèle de référence pour éviter la dérive (cf. [[RLHF and DPO]]).
- **Détection de dérive** (data drift) : KL entre la distribution d'entraînement et celle de production ; surveiller sa montée.
- Outils : `scipy.stats.entropy(p, q)` ([[Dev/Services/scipy.stats|scipy.stats]]) calcule la KL ; `torch.nn.functional.kl_div` côté [[Dev/Services/PyTorch|PyTorch]].

## Approches voisines & alternatives

- [[Cross-entropy]] — la KL augmentée de l'entropie de $p$ ; ce qu'on minimise réellement en classification.
- [[Jensen-Shannon divergence]] — version symétrisée et bornée de la KL, utilisable comme distance.
- [[Wasserstein distance]] — distance qui reste informative même sans support commun, là où la KL diverge.
- [[Mutual information]] — c'est une KL entre la loi conjointe et le produit des marges.
- [[Inférence bayésienne]] — l'inférence variationnelle minimise une KL à l'a posteriori.
- [[Shannon entropy]] — la KL s'annule quand $q = p$, ramenant l'entropie croisée à l'entropie.

## Pour aller plus loin

- Kullback & Leibler (1951) — *On Information and Sufficiency*.
- Blei, Kucukelbir & McAuliffe (2017) — *Variational Inference: A Review for Statisticians*.
