---
galaxie: wiki
type: concept
nom: Maximum de vraisemblance
alias: [MLE, maximum likelihood estimation, maximum likelihood, vraisemblance maximale]
categorie: concept/stats
domaines: [data-sci]
tags: [maximum-likelihood, point-estimation, statistical-inference]
---

# Maximum de vraisemblance

## Aperçu

- Estime les paramètres d'un modèle en cherchant la valeur qui rend les **données observées les plus probables**.
- Estimation ponctuelle fréquentiste : un seul jeu de paramètres, sans a priori.
- Socle implicite d'une grande partie des modèles : régression, GLM, et beaucoup de réseaux de neurones (entraînés en minimisant une log-vraisemblance négative).

## Concepts clés

### Vraisemblance
- $L(\theta) = P(\text{données} \mid \theta)$, vue comme fonction de $\theta$ à données fixées. Ce n'est **pas** une probabilité sur $\theta$ (contraste avec l'[[Inférence bayésienne|a posteriori]]).

### Log-vraisemblance
- On maximise $\log L$ plutôt que $L$ : le produit devient une somme, numériquement stable, et l'argmax est inchangé.

### Estimateur MLE
- $\hat{\theta} = \arg\max_\theta L(\theta)$. Forme fermée pour les lois simples (Bernoulli, gaussienne) ; sinon optimisation numérique.

### Propriétés asymptotiques
- Convergent, asymptotiquement efficace et normal quand $n$ grandit. Mais variance élevée en petit échantillon → tendance au surajustement.

## Les maths, simplement

- Vraisemblance i.i.d. : $L(\theta) = \prod_{i=1}^n p(x_i \mid \theta)$.
- Log-vraisemblance : $\ell(\theta) = \sum_i \log p(x_i\mid\theta)$, et $\hat{\theta}_{MLE} = \arg\max_\theta \ell(\theta)$.
- Condition du premier ordre : $\partial \ell / \partial\theta = 0$ (score nul).
- Exemples : Bernoulli → $\hat{p} = \frac{1}{n}\sum_i x_i$ (fréquence empirique) ; gaussienne → $\hat\mu = \bar{x}$.
- Lien perte : maximiser $\ell$ ⇔ minimiser la log-vraisemblance négative (NLL) — soit l'entropie croisée (classification), soit le MSE (régression gaussienne).

## En pratique

- Les pertes usuelles du ML sont du MLE déguisé : cross-entropy et MSE découlent d'une hypothèse de vraisemblance.
- Surajustement en petit $n$ ou modèle riche → ajouter un a priori = passer à l'[[Estimation MAP]] (≡ régularisation).
- Au-delà des lois simples, pas de forme fermée → optimiseurs (Newton-Raphson, L-BFGS, descente de gradient).
- Vraisemblance plate ou multimodale → estimateur instable, attention aux maxima locaux et à la non-identifiabilité.

## Approches voisines & alternatives

- [[Estimation MAP]] — MLE augmenté d'un a priori ; MAP = MLE quand l'a priori est plat.
- [[Inférence bayésienne]] — renvoie toute la distribution a posteriori au lieu d'un point ; le MLE en est le mode de la vraisemblance seule.
- [[Tests d'hypothèse]] — le test du rapport de vraisemblance compare deux modèles ajustés par MLE.
- [[GLM]], [[Régression logistique]] — modèles supervisés ajustés par MLE (la [[Régression linéaire]] gaussienne aussi).
- Méthode des moments — estimation alternative, parfois plus simple à dériver, en général moins efficace.

## Pour aller plus loin

- Réf : Casella & Berger — *Statistical Inference*.
- Outils : `scipy.stats` (`.fit`), `scipy.optimize`, `statsmodels` (GLM / MLE), `scikit-learn`, PyTorch (NLL par descente de gradient).
