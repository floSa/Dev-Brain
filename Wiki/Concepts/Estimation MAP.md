---
galaxie: wiki
type: concept
nom: Estimation MAP
alias: [MAP, maximum a posteriori, maximum a posteriori estimation, estimation maximum a posteriori]
categorie: concept/stats
domaines: [data-sci]
tags: [bayesian, point-estimation, prior]
---

# Estimation MAP

## Aperçu

- Estimation ponctuelle **bayésienne** : prend le **mode** de la distribution a posteriori — la valeur la plus probable du paramètre une fois les données vues.
- C'est le [[Maximum de vraisemblance|MLE]] auquel on ajoute un a priori : maximise vraisemblance × a priori.
- Pont entre fréquentiste et bayésien : un seul point, mais teinté par une croyance a priori.

## Concepts clés

### Mode de l'a posteriori
- $\text{MAP} = \arg\max_\theta P(\theta\mid D) \propto \arg\max_\theta P(D\mid\theta)\,P(\theta)$. On n'a pas besoin de l'évidence $P(D)$ : seul le sommet compte.

### A priori comme régularisation
- L'a priori tire l'estimation vers des valeurs plausibles → équivaut à une pénalité. A priori gaussien ⇒ régularisation L2 (ridge) ; a priori de Laplace ⇒ L1 (lasso).

### MAP vs moyenne a posteriori
- MAP = mode ; l'autre résumé courant est la **moyenne** a posteriori. Ils diffèrent dès que l'a posteriori est asymétrique.
- Le MAP ne capte pas l'incertitude (un seul point) — pour ça, il faut l'a posteriori complet.

## Les maths, simplement

- $\hat\theta_{MAP} = \arg\max_\theta P(\theta\mid D) = \arg\max_\theta \big[\log P(D\mid\theta) + \log P(\theta)\big]$.
- Comparé au MLE — $\hat\theta_{MLE} = \arg\max_\theta \log P(D\mid\theta)$ — le MAP ajoute le terme $\log P(\theta)$.
- A priori plat (uniforme) ⇒ $\log P(\theta)$ constant ⇒ MAP = MLE.
- A priori gaussien $\mathcal{N}(0,\tau^2)$ ⇒ terme $-\frac{1}{2\tau^2}\lVert\theta\rVert^2$ ⇒ exactement la pénalité ridge ($\lambda = 1/\tau^2$).

## En pratique

- Le voir comme un MLE régularisé : choisir l'a priori, c'est choisir la régularisation (force = inverse de la variance de l'a priori).
- Donne un point, pas une incertitude → si l'intervalle de crédibilité importe, faire l'[[Inférence bayésienne]] complète.
- Sensible à la paramétrisation : le mode se déplace lors d'un changement de variable, contrairement à la moyenne a posteriori.
- Calcul : souvent le même optimiseur que le MLE, avec un terme de pénalité en plus.

## Approches voisines & alternatives

- [[Maximum de vraisemblance]] — le MAP sans a priori (ou à a priori plat).
- [[Régularisation]] — la lecture fréquentiste de l'a priori : Ridge ⇔ gaussien, Lasso ⇔ Laplace.
- [[Inférence bayésienne]] — le MAP n'est qu'un résumé ponctuel de l'a posteriori complet.
- [[A priori conjugués]] — rendent le mode a posteriori (donc le MAP) calculable en forme fermée.

## Pour aller plus loin

- Lien régularisation : ridge ⇔ a priori gaussien, lasso ⇔ a priori de Laplace — un même calcul, deux lectures.
- Outils : `scikit-learn` (régressions pénalisées = MAP implicite), [[Dev/Services/PyMC|PyMC]] (`find_MAP`).
