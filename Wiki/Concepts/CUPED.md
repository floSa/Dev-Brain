---
galaxie: wiki
type: concept
nom: CUPED
alias: [Controlled-experiment Using Pre-Experiment Data, variance reduction, regression adjustment]
categorie: concept/stats
domaines: [data-sci]
tags: [experimentation, variance-reduction, ab-testing]
---

# CUPED

## Aperçu

- Technique de **réduction de variance** pour les [[A-B testing|tests A/B]] : on corrige la métrique de chaque unité avec une covariable mesurée **avant** l'expérience.
- Même effet estimé, mais erreur standard plus petite → test plus court ou MDE plus fin à trafic constant.
- Acronyme : Controlled-experiment Using Pre-Experiment Data (Microsoft, Deng et al., 2013).

## Concepts clés

### Covariable de pré-période
- Le meilleur prédicteur de la métrique post-expérience est, le plus souvent, la même métrique mesurée sur l'unité **avant** le test (ex. dépense de la semaine précédente).
- Comme elle précède le traitement, elle est par construction non affectée par lui → corriger avec elle n'introduit pas de biais.

### Ajustement
- On retranche la part de la métrique expliquée par la covariable : la variance résiduelle baisse d'autant que la covariable corrèle avec la métrique.
- Équivalent à un ajustement par régression (la pré-période en variable explicative).

### Gain
- Réduction de variance $\approx \rho^2$ (carré de la corrélation pré/post). $\rho = 0{,}7 \Rightarrow$ ~50 % de variance en moins ≈ moitié moins de trafic pour la même puissance.

## Les maths, simplement

- Métrique ajustée : $Y_{cuped} = Y - \theta\,(X - \bar{X})$, où $X$ = covariable de pré-période.
- Coefficient optimal : $\theta = \dfrac{\mathrm{Cov}(Y, X)}{\mathrm{Var}(X)}$ (la pente de la régression de $Y$ sur $X$).
- Variance obtenue : $\mathrm{Var}(Y_{cuped}) = \mathrm{Var}(Y)\,(1 - \rho^2)$ avec $\rho = \mathrm{corr}(Y, X)$.
- $\theta$ s'estime sur l'ensemble des données (A + B) : centrer par $\bar{X}$ garde l'estimateur de l'effet sans biais.

## En pratique

- Choisir une covariable fortement corrélée à la métrique et antérieure au traitement (la même métrique en pré-période est le défaut).
- Les nouveaux utilisateurs n'ont pas de pré-période → covariable absente : prévoir un repli (imputation à la moyenne, ou exclusion analysée à part).
- Estimer $\theta$ sur le pool global, pas par bras, pour ne pas réintroduire de biais.
- Generaliser : plusieurs covariables → ajustement par régression linéaire (CUPAC, modèles ML pour prédire la métrique).
- L'[[Intervalles de confiance|IC]] empirique de l'effet ajusté peut se calculer par [[Bootstrap]] quand la formule analytique est lourde.

## Approches voisines & alternatives

- [[Inférence causale]] — le cadre causal d'ensemble ; CUPED améliore l'efficacité de l'estimation dans un essai randomisé, sans toucher à l'identification.
- [[A-B testing]] — CUPED est une couche d'efficacité posée dessus, sans en changer le design.
- [[Analyse de puissance]] — la variance réduite se répercute directement sur le n nécessaire.
- [[Bootstrap]] — IC de l'estimateur ajusté quand l'analytique est pénible.
- Stratification / blocking — autre voie de réduction de variance, en amont (au moment de la randomisation) plutôt qu'en aval.

## Pour aller plus loin

- Réf : Deng, Xu, Kohavi, Walker — *Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data* (WSDM 2013).
- Extension CUPAC : covariable prédite par un modèle ML (Booking, DoorDash).
- Outils : `statsmodels` (OLS pour l'ajustement), implémentations maison sur `pandas`/`polars`.
