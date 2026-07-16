---
galaxie: wiki
type: concept
nom: Régression quantile
alias: [Quantile regression, QuantileRegressor, Perte pinball, Pinball loss, Régression médiane, Intervalles de prédiction]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regression, supervised, linear-model, non-parametric]
---

# Régression quantile

## Aperçu

- Au lieu de prédire la **moyenne** conditionnelle $\mathbb{E}[y \mid x]$ comme toute [[Régression|régression]] ordinaire, elle prédit un **quantile** conditionnel : la médiane, le 5ᵉ centile, le 95ᵉ. Le changement tient en une ligne — remplacer la perte quadratique par la perte *pinball*.
- Deux bénéfices d'un coup : des **intervalles de prédiction** sans hypothèse de loi (entraîner à $\tau = 0{,}05$ et $\tau = 0{,}95$ borne 90 % des cas), et une **robustesse** aux valeurs extrêmes que la moyenne n'a jamais.

## Concepts clés

### La perte décide de ce qu'on estime
- C'est le fait central, et il est sous-estimé : le choix de la fonction de perte **détermine la statistique estimée**. Ce n'est pas un détail d'optimisation.
- Perte quadratique $(y - \hat{y})^2$ → **moyenne**. Perte absolue $|y - \hat{y}|$ → **médiane**. Perte pinball $\rho_\tau$ → **quantile $\tau$**. La médiane n'est que le cas $\tau = 0{,}5$.

### La perte pinball, ou l'asymétrie assumée
- L'idée : **pénaliser différemment** sous-estimation et sur-estimation. Pour $\tau = 0{,}9$, sous-estimer coûte 9 fois plus que sur-estimer — le modèle est donc poussé à viser haut, et se cale naturellement là où 90 % des valeurs sont en dessous.
- Le nom vient de la forme du graphe : deux segments de pentes différentes se rejoignant en zéro, comme un flipper.

### Pourquoi c'est robuste
- La perte quadratique croît **au carré** : un point aberrant à 10 écarts pèse 100 fois plus qu'un point à 1 écart. Il tire la prédiction à lui.
- La perte pinball croît **linéairement** : ce même point ne pèse que 10 fois plus. Le modèle ne se laisse pas kidnapper. C'est exactement pourquoi la médiane résiste là où la moyenne cède.

### Hétéroscédasticité — là où elle est irremplaçable
- Quand la dispersion de $y$ **dépend de $x$** (les résidus dessinent un entonnoir), un intervalle de largeur constante est faux partout : trop large où c'est calme, trop étroit où c'est agité.
- La régression quantile ajuste **chaque quantile séparément**, donc l'intervalle se resserre et s'élargit tout seul selon $x$. Aucune autre méthode simple ne fait ça.

### Le croisement des quantiles
- Défaut structurel à connaître : les quantiles étant ajustés **indépendamment**, rien ne garantit que la courbe à $\tau = 0{,}9$ reste au-dessus de celle à $\tau = 0{,}5$. Elles peuvent se croiser — résultat absurde.
- Parades : ré-ordonner les prédictions a posteriori, ou utiliser une méthode à quantiles non croisés.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `quantile` ($\tau$) | Le quantile visé | Ce n'est **pas** un hyperparamètre à régler : c'est la question posée |
| `alpha` | Pénalité L1 ([[Régularisation]]) | sklearn en met **1,0 par défaut** — un piège : le mettre à 0 pour une régression quantile pure |
| `solver` | Solveur de programme linéaire | `highs` recommandé ; le défaut historique est lent |
| `objective='quantile'` + `alpha` (LightGBM) | Le même objectif côté boosting d'arbres | Ici `alpha` désigne le quantile — **collision de noms** avec sklearn |

## Les maths, simplement

- Perte pinball pour le quantile $\tau \in (0, 1)$, avec le résidu $u = y - \hat{y}$ :
  $$\rho_\tau(u) = \begin{cases} \tau \cdot u & \text{si } u \ge 0 \quad (\text{sous-estimation}) \\ (\tau - 1) \cdot u & \text{si } u < 0 \quad (\text{sur-estimation}) \end{cases}$$
- Lecture concrète pour $\tau = 0{,}9$ : sous-estimer de 1 coûte $0{,}9$ ; sur-estimer de 1 coûte $|{-0{,}1}| = 0{,}1$. Rapport 9 pour 1 — d'où un modèle qui vise haut.
- Pour $\tau = 0{,}5$ : les deux coûtent $0{,}5$, la perte est symétrique et proportionnelle à $|u|$. On retrouve exactement la perte absolue, donc la **médiane**.
- Objectif : $\min_\beta \sum_i \rho_\tau(y_i - x_i^\top \beta)$. La perte est convexe mais **non différentiable en 0** : pas de solution fermée, on passe par la **programmation linéaire** ([[Programmation linéaire en nombres entiers (MIP)|programmation linéaire]]) — et non par les moindres carrés.

## En pratique

- **Le cas d'usage massif : les intervalles de prédiction.** Entraîner trois modèles ($\tau = 0{,}05$, $0{,}5$, $0{,}95$) donne une prédiction centrale et un intervalle à 90 %, **sans supposer la normalité des résidus**. C'est souvent plus honnête que l'intervalle gaussien d'une [[Régression linéaire|OLS]].
- **Attention au `alpha=1.0` par défaut de sklearn** : `QuantileRegressor` applique une pénalité L1 d'office. Une régression quantile pure demande `alpha=0`. Erreur silencieuse classique — le modèle marche, il est juste régularisé à l'insu de l'utilisateur.
- **Le [[Gradient Boosting (GBDT)|boosting]] fait de la régression quantile** : `objective='quantile'` en LightGBM, `loss='quantile'` en `GradientBoostingRegressor`. On garde la puissance des arbres **et** les intervalles. C'est souvent le meilleur des deux mondes en pratique.
- **Piège de nommage** : `alpha` désigne la **pénalité** chez sklearn et le **quantile** chez LightGBM. Vérifier la doc à chaque fois.
- **Ne pas confondre robustesse et exactitude** : la médiane est robuste, mais si la vraie question métier est un total attendu (chiffre d'affaires cumulé), c'est la **moyenne** qu'il faut — la médiane ne s'additionne pas.
- Coût : $k$ quantiles = $k$ modèles à entraîner. Et la programmation linéaire passe moins bien à l'échelle que les moindres carrés.
- Évaluer avec la **perte pinball elle-même** (`mean_pinball_loss`), pas avec le RMSE — qui mesurerait une moyenne qu'on n'a jamais cherché à prédire ([[Regression metrics]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.linear_model.QuantileRegressor]] et `mean_pinball_loss` ; [[Dev/Services/LightGBM|LightGBM]] (`objective='quantile'`) ; [[Dev/Services/statsmodels|statsmodels]] (`QuantReg`, avec l'inférence et les tests).

## Approches voisines & alternatives

- [[Régression]] — le chapeau : la perte choisie décide de la statistique estimée, et c'est ici que ça se joue.
- [[Régression linéaire]] — le pendant par moindres carrés : estime la moyenne, sensible aux valeurs extrêmes.
- [[Regression metrics]] — la perte pinball comme métrique d'évaluation.
- [[Gradient Boosting (GBDT)]] — la version non linéaire, souvent le meilleur choix pratique.
- [[Gaussian Process]] — l'autre façon d'obtenir de l'incertitude : native et probabiliste, mais gaussienne et en $O(n^3)$.
- [[Bootstrap]] — l'alternative non paramétrique pour des intervalles autour de n'importe quel modèle.
- [[GLM]] — l'autre extension de la régression linéaire, côté lois non normales plutôt que côté quantiles.
- [[Détection d'outliers univariée]] — les quantiles comme outil de détection (règle de l'IQR).
- [[Intervalles de confiance]] — à ne pas confondre : incertitude sur un **paramètre**, pas sur une prédiction future.

## Pour aller plus loin

- Koenker & Bassett (1978) — *Regression Quantiles* : l'article fondateur.
- Koenker (2005) — *Quantile Regression* : la référence complète.
- Documentation scikit-learn — *Quantile regression* : l'exemple compare explicitement moyenne et médiane sous hétéroscédasticité.
