---
galaxie: wiki
type: concept
nom: GLM
alias: [Modèles linéaires généralisés, Generalized Linear Model, Modèle linéaire généralisé]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regression, linear-model, supervised, maximum-likelihood]
---

# GLM

## Aperçu

- Étend la régression linéaire aux cibles **non normales** : comptages, proportions, durées, montants positifs.
- Trois briques : une **loi** de la famille exponentielle, un **prédicteur linéaire**, une **fonction de lien** entre les deux.

## Concepts clés

### Les trois composantes
- Composante aléatoire : la loi de $y$ (normale, binomiale, Poisson, Gamma…).
- Composante systématique : $\eta = X\beta$ (prédicteur linéaire).
- Lien : $g(\mathbb{E}[y]) = \eta$, avec $g$ monotone (identité, logit, log…).

### Liens canoniques
- Normale → identité ([[Régression linéaire]]). Binomiale → logit ([[Régression logistique]]). Poisson → log (comptages). Gamma → log/inverse (montants positifs).

### Estimation
- Maximum de vraisemblance par IRLS (moindres carrés repondérés itérés).

### Évaluation
- Déviance et résidus de déviance, AIC. Surveiller la surdispersion en Poisson (→ quasi-Poisson, binomiale négative).

## Les maths, simplement

- $g(\mu) = X\beta$ avec $\mu = \mathbb{E}[y]$ et $y$ dans la famille exponentielle.
- Poisson (lien log) : $\log \mu = X\beta \Rightarrow \mu = e^{X\beta}$ (taux toujours positif).
- Ajustement par [[Maximum de vraisemblance]] ; régression linéaire et logistique en sont deux cas particuliers.

## En pratique

- Choisir la loi selon la cible : comptage → Poisson ; proportion → binomiale ; montant positif asymétrique → Gamma.
- Vérifier la surdispersion (variance $>$ moyenne en Poisson).
- `offset` pour modéliser des taux (exposition).
- Régularisation possible ([[Régularisation]]).
- Outils : `statsmodels.GLM` (référence Python), `sklearn` (`PoissonRegressor`, `GammaRegressor`, `TweedieRegressor`), `glm()` en R.

## Approches voisines & alternatives

- [[Régression linéaire]] — cas GLM lien identité + loi normale.
- [[Régression logistique]] — cas GLM lien logit + loi binomiale.
- [[Régularisation]] — GLM pénalisés (déviance + L1/L2).
- [[GAM]] — relâche la linéarité du prédicteur via des fonctions de lissage.
- [[Maximum de vraisemblance]] — le principe d'estimation commun.

## Pour aller plus loin

- Nelder & Wedderburn (1972).
- McCullagh & Nelder — *Generalized Linear Models*.
