---
galaxie: wiki
type: concept
nom: Gradient descent
alias: [Descente de gradient, GD, SGD, Stochastic gradient descent, Descente de gradient stochastique, Mini-batch]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, gradient-descent]
---

# Gradient descent

## Aperçu

- Méthode du **premier ordre** : on minimise une fonction en avançant à petits pas dans la direction opposée au gradient, $\theta \leftarrow \theta - \eta\,\nabla L(\theta)$.
- C'est le moteur d'entraînement de presque tout le ML moderne — du modèle linéaire au réseau profond — parce qu'il ne demande que le gradient, calculable par différentiation automatique.

## Concepts clés

### Batch / stochastique / mini-batch
- **Batch** : gradient sur tout le jeu de données — exact mais coûteux.
- **Stochastique (SGD)** : gradient sur un seul exemple — bruité mais rapide, et le bruit aide à fuir les [[Loss landscape and saddle points|points-selles]].
- **Mini-batch** : compromis dominant (32–1024 exemples), bon usage du GPU.

### Le pas $\eta$
- Hyperparamètre le plus sensible : trop grand → divergence, trop petit → lenteur. Sa variation au cours de l'entraînement est gérée par les [[Learning rate schedules]].

### Accélérations
- **Momentum** : moyenne mobile des gradients, lisse les oscillations dans les ravins.
- **Nesterov** : momentum « anticipé ». Les optimiseurs adaptatifs ([[Adam optimizer|Adam]], RMSprop) ajustent un pas par paramètre.

## Les maths, simplement

- Mise à jour : $\theta_{t+1} = \theta_t - \eta\,\nabla L(\theta_t)$ — descente de plus forte pente locale.
- Sur une fonction convexe lisse : convergence en $O(1/t)$ ; fortement convexe : convergence **linéaire**, d'autant plus lente que le conditionnement $\kappa$ est grand (cf. [[Convexity]]).
- SGD : le gradient est un estimateur non biaisé du vrai gradient ; sa variance impose un pas décroissant pour converger.

## En pratique

- **Standardiser** les variables : sinon la surface est étirée et la descente zigzague.
- Forme close vs itératif : OLS a une solution exacte (équations normales) mais GD passe mieux à l'échelle sur gros $X$ ; la [[Régression logistique]] n'a **pas** de forme close → GD ou Newton.
- **Gradient clipping** par la norme L2 pour stabiliser les réseaux profonds (cf. [[Vector norms]]).
- Outils : `torch.optim.SGD`, `sklearn.linear_model.SGDRegressor` / `SGDClassifier`.

## Approches voisines & alternatives

- [[Adam optimizer]] — variante adaptative : momentum + pas par paramètre, l'optimiseur par défaut du deep learning.
- [[Newton & quasi-Newton]] — méthode du second ordre : moins d'itérations, mais hessienne coûteuse.
- [[Convexity]] — détermine si la descente atteint l'optimum global.
- [[Learning rate schedules]] — la planification du pas $\eta$.
- [[Loss landscape and saddle points]] — la géométrie que la descente doit traverser.
- [[Régularisation]] — l'objectif pénalisé se minimise par descente de (sous-)gradient.
- [[Régression linéaire]] — alternative itérative aux équations normales quand $X$ est grand.
- [[Gradient Boosting (GBDT)]] — descente de gradient dans l'espace des fonctions (boosting).

## Pour aller plus loin

- Robbins & Monro (1951) — approximation stochastique, racine du SGD.
- Ruder (2016) — *An overview of gradient descent optimization algorithms*.
