---
galaxie: wiki
type: concept
nom: Intermittent demand
alias: [Demande intermittente, Croston, SBA, TSB, demande sporadique, slow movers]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries]
---

# Intermittent demand

## Aperçu

- Séries où la demande est **sporadique** : beaucoup de périodes à zéro entrecoupées de demandes non nulles (pièces détachées, articles à faible rotation).
- Les modèles classiques et les métriques en pourcentage échouent (division par zéro, prévision « moyenne » non nulle absurde). D'où des méthodes dédiées centrées sur **taille × fréquence** de la demande.

## Concepts clés

### Caractérisation : ADI & CV²
- **ADI** (intervalle moyen entre demandes) et **CV²** (variabilité au carré des tailles non nulles) classent le portefeuille en quatre régimes (Syntetos-Boylan) : *smooth*, *erratic*, *intermittent*, *lumpy*. Cette classification guide le choix de méthode.

### Croston
- Décompose la série en deux : la **taille** des demandes non nulles et l'**intervalle** qui les sépare, chacune lissée par un [[Exponential smoothing|lissage exponentiel]] séparé, mis à jour **seulement aux périodes de demande**. Prévision = taille / intervalle.

### SBA (Syntetos-Boylan Approximation)
- Croston est **biaisé** (sur-estime). SBA applique un facteur correctif $(1-\alpha/2)$ ; c'est souvent le défaut recommandé.

### TSB
- Met à jour la **probabilité de demande** à chaque période (et pas seulement aux demandes), ce qui gère l'**obsolescence** : une demande qui s'éteint voit sa prévision décroître, là où Croston reste figé.

### Évaluation adaptée
- MAPE inutilisable (zéros au dénominateur). Utiliser des métriques **scaled** (MASE, RMSSE) ou juger sur la demande cumulée / le niveau de service.

## Les maths, simplement

- Croston aux périodes de demande : taille $z_t=\alpha y_t+(1-\alpha)z_{t-1}$, intervalle $p_t=\alpha q_t+(1-\alpha)p_{t-1}$ ($q_t$ = périodes depuis la dernière demande). Prévision $\hat y = z_t/p_t$.
- SBA : $\hat y=(1-\alpha/2)\,z_t/p_t$ — la correction de biais.

## En pratique

- **Classer le portefeuille** (ADI/CV²) avant de choisir : Croston/SBA pour l'intermittent, TSB si risque d'obsolescence.
- Les décisions de stock se prennent sur des **quantiles** (niveau de service), pas sur la moyenne — cadrer l'objectif en amont ([[Forecasting framing]]).
- Outils : [[Dev/Services/statsforecast|statsforecast — CrostonClassic, CrostonSBA, TSB, ADIDA, IMAPA]].

## Approches voisines & alternatives

- [[Forecasting metrics]] — pourquoi MAPE casse ici et pourquoi MASE/RMSSE sont robustes aux zéros.
- [[Exponential smoothing]] — Croston applique un SES séparé à la taille et à l'intervalle.
- [[Forecasting framing]] — cadrer l'objectif (quantile, niveau de service) avant la moyenne.

## Pour aller plus loin

- Croston (1972) — *Forecasting and stock control for intermittent demands*.
- Syntetos & Boylan (2005) — la correction de biais (SBA).
- Teunter, Syntetos & Babai (2011) — TSB et la gestion de l'obsolescence.
