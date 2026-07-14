---
galaxie: wiki
type: concept
nom: Intervalles de confiance
alias: [confidence interval, confidence intervals, IC]
categorie: concept/stats
domaines: [data-sci]
tags: [statistical-inference, confidence-interval]
---

# Intervalles de confiance

## Aperçu

- Intervalle calculé sur l'échantillon, censé contenir le vrai paramètre (moyenne, proportion…) avec un niveau de confiance donné.
- Donne l'ampleur **et** l'incertitude, là où un test ne renvoie qu'un oui/non.

## Concepts clés

### Niveau de confiance
- 95 % = si l'on répétait l'échantillonnage, 95 % des IC ainsi construits contiendraient le vrai paramètre.
- Ce n'est **pas** « 95 % de proba que le paramètre soit dans *cet* intervalle » (lecture fréquentiste).

### Largeur de l'IC
- Diminue avec la taille d'échantillon (en $1/\sqrt{n}$) et avec une variance plus faible.
- Augmente avec le niveau de confiance (99 % plus large que 90 %).

### Erreur standard
- Écart-type de l'estimateur ; brique de la marge d'erreur.

### Dualité test / IC
- Un IC à 95 % d'une différence qui exclut 0 ⇔ test significatif au seuil 5 %.

## Les maths, simplement

- IC d'une moyenne : $\bar{x} \pm t_{1-\alpha/2,\,n-1}\,\dfrac{s}{\sqrt{n}}$ — moyenne ± (quantile) × erreur standard.
- Erreur standard de la moyenne : $SE = \dfrac{s}{\sqrt{n}}$ ; $s$ = écart-type échantillon, $n$ = taille.
- Niveau de confiance $1-\alpha$ : pour 95 %, $\alpha = 0{,}05$.
- Largeur $\propto 1/\sqrt{n}$ : quadrupler $n$ pour deux fois plus de précision.

## En pratique

- Préférer un IC à une p-value seule : il montre l'ampleur plausible de l'effet.
- Petit échantillon ou loi inconnue → IC par [[Bootstrap]] (percentiles) plutôt que formule normale.
- Proportions : la formule normale dérape près de 0 ou 1 → utiliser Wilson ou Clopper-Pearson.
- Ne pas confondre IC (incertitude sur le paramètre) et intervalle de prédiction (incertitude sur une future observation, plus large).

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — vue duale : un IC résume une famille de tests.
- [[Théorème central limite]] — justifie la forme normale de l'IC pour de grands échantillons.
- [[Bootstrap]] — IC sans hypothèse de distribution, par rééchantillonnage.
- [[Analyse de puissance]] — viser une précision cible (largeur d'IC) pour fixer $n$.
- [[Inférence bayésienne]] — son intervalle de crédibilité est l'analogue, avec interprétation probabiliste directe.

## Pour aller plus loin

- Outils : `scipy.stats`, `statsmodels` (`.conf_int()`).
- Concepts liés : [[Tests d'hypothèse]], [[Bootstrap]].
