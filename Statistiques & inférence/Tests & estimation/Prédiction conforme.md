---
role: notion
nom: Prédiction conforme
alias: [conformal prediction, conformal inference, inférence conforme, split conformal, conformal split, jackknife+, CV+, full conformal, ensembles de prédiction, prediction sets, intervalle de prédiction, distribution-free, couverture marginale, couverture conditionnelle, conformal risk control, adaptive conformal inference, ACI, MAPIE]
categorie: stats/inference
domaines: [data-sci]
tags: [statistical-inference, confidence-interval, model-evaluation]
---

# Prédiction conforme

## Aperçu

- Transformer **n'importe quel modèle** (une régression, un réseau, un LLM) en un générateur d'**ensembles de prédiction** : un intervalle pour une cible continue, un ensemble de classes pour une cible catégorielle, qui contient la vraie valeur avec une probabilité choisie à l'avance.
- La garantie est **sans hypothèse de loi** et **valable à taille finie** : elle ne suppose ni gaussianité, ni modèle bien spécifié, ni $n$ grand. Elle suppose en revanche que les données sont **échangeables**.
- Distinct d'un [[Intervalles de confiance|intervalle de confiance]] : celui-ci encadre un **paramètre** (une moyenne, un coefficient) ; l'ensemble de prédiction encadre une **observation future**.
- Distinct de la [[Calibration]] : celle-ci rend les probabilités prédites fiables ; la prédiction conforme n'exige pas de probabilités fiables et donne une garantie même si le modèle est mauvais — seule la taille de l'ensemble en souffre.

## Concepts clés

### Split conformal

Procédure en quatre temps (Angelopoulos et Bates, 2021) :

1. Séparer un jeu de **calibration** de $n$ points, non utilisé pour entraîner le modèle.
2. Choisir un **score de non-conformité** $s(x, y)$ : plus il est grand, plus $y$ s'accorde mal avec $x$. Pour une régression, la valeur absolue du résidu $|y - \hat f(x)|$ convient.
3. Calculer $\hat q$, le quantile d'ordre $\lceil (n+1)(1-\alpha) \rceil / n$ des scores de calibration.
4. L'ensemble de prédiction est $C(x) = \{ y : s(x, y) \le \hat q \}$.

- Le facteur $(n+1)$ compte : un quantile empirique « simple » d'ordre $1-\alpha$ sous-couvre légèrement. Ce détail a valu des correctifs de bibliothèque.
- Pas de ré-entraînement, un seul calcul de quantile : c'est la variante employée en pratique. Lei et al. (2018) la présentent comme réponse au coût du full conformal.

```python
n = len(cal_scores)
q_level = np.ceil((n + 1) * (1 - alpha)) / n
q_hat = np.quantile(cal_scores, q_level, method="higher")
```

### Full conformal, jackknife+ et CV+

- **Full conformal** (Vovk, Gammerman, Shafer ; reprise par Lei et al., 2018) : pour chaque valeur candidate $y$, ré-entraîner le modèle sur les données plus $(x, y)$ et tester si $y$ est « conforme ». Garantie sans perte de données, mais coût prohibitif : Lei et al. notent que le faire efficacement reste un problème ouvert pour le lasso et les estimateurs non linéaires.
- **Jackknife+** (Barber, Candès, Ramdas, Tibshirani, 2021) : sans jeu de calibration séparé, à partir des résidus *leave-one-out* et des prédictions leave-one-out **au point test**. Garantie démontrée : couverture $\ge 1 - 2\alpha$ (pas $1-\alpha$) pour tout algorithme symétrique. Les auteurs montrent que le facteur 2 ne peut pas être supprimé en général ; en pratique, la couverture observée est proche de $1-\alpha$.
- **CV+** : variante à $K$ plis du jackknife+, avec une garantie de même nature, plus faible d'un terme qui dépend de $K$ et $n$.
- Le jackknife « naïf » (sans le +) peut avoir une couverture nulle dans des cas pathologiques (Barber et al., Thm 2).

### Ensembles de prédiction en classification

- **Score « softmax »** (dit LAC) : $s = 1 - \hat p(y \mid x)$. Donne les ensembles **les plus petits** en moyenne, mais sous-couvre les exemples difficiles et sur-couvre les faciles.
- **APS** (Romano, Sesia, Candès, 2020) : cumule les probabilités des classes triées par ordre décroissant jusqu'à la vraie classe. Plus adaptatif à la difficulté de l'exemple, mais ensembles plus gros.
- **RAPS** (Angelopoulos et al., 2021) : APS avec un terme de régularisation qui pénalise les ensembles longs. Sur ImageNet (ResNeXt-101, $\alpha = 10\ \%$), les auteurs rapportent une taille moyenne de 19 pour APS contre 2 pour RAPS.
- **CQR** (Romano, Patterson, Candès, 2019) : en régression, part de deux régressions quantiles et ajoute une correction conforme ; les intervalles s'élargissent ou se resserrent selon $x$. Voir [[Régression quantile]].

### Échangeabilité et ce qui la casse

- La garantie suppose que les points de calibration et le point test sont **échangeables** (en particulier i.i.d.) et, pour full conformal et jackknife+, que l'algorithme traite les données **symétriquement**.
- **Décalage de covariables** : si la loi de $X$ change mais pas celle de $Y \mid X$, une pondération par le rapport de vraisemblance rétablit la garantie (Tibshirani et al., 2019) — à condition de connaître ou d'estimer ce rapport.
- **Dérive progressive** : Barber et al. (2023) pondèrent les points (plus de poids aux récents) et bornent la perte de couverture par une somme pondérée de distances en variation totale entre jeu de données et jeu permuté. Poids uniformes : on retrouve le cas classique.
- **Séries temporelles** : des points voisins ne sont ni i.i.d. ni échangeables. Deux voies :
  - **ACI** (Gibbs et Candès, 2021) : met à jour le niveau $\alpha_t$ en ligne selon que le dernier intervalle a manqué ou non ; garantit que la **fréquence de couverture à long terme** tend vers $1-\alpha$ sans hypothèse sur la loi, mais pas la couverture à chaque pas. Zaffran et al. (2022) relèvent que l'ACI produit souvent des intervalles infinis.
  - **EnbPI** (Xu et Xie) : garanties **asymptotiques** seulement, sous des hypothèses sur les erreurs, pas de borne à $n$ fini du type ci-dessus.
- Voir [[Stationarity]] pour ce qui change dans une série.

### Marginale ou conditionnelle

- **Marginale** : la probabilité de couvrir est $\ge 1-\alpha$ **en moyenne** sur les calibrations et les points test.
- **Conditionnelle** : la probabilité de couvrir est $\ge 1-\alpha$ **pour chaque valeur de $x$**. Bien plus forte.
- Exemple d'Angelopoulos et Bates : deux groupes à 90 % et 10 % de fréquence ; 100 % de couverture sur le premier et 0 % sur le second donnent 90 % de couverture marginale sans aucune garantie sur le second groupe.
- **Impossibilité** (Vovk 2012 ; Barber et al. 2021, *The limits of distribution-free conditional predictive inference*) : une méthode qui garantit la couverture conditionnelle exacte, sans hypothèse sur la loi, produit des intervalles de **longueur moyenne infinie** (en presque tout point $x$ qui n'est pas un atome de la loi de $X$). Seules des **relaxations** sont atteignables : couverture conditionnelle approchée sur des régions de masse minimale, ou garantie par groupes définis à l'avance.

## Les maths, simplement

- Garantie du split conformal, données échangeables :
  $$1 - \alpha \;\le\; \mathbb P\big(Y_{n+1} \in C(X_{n+1})\big) \;\le\; 1 - \alpha + \frac{1}{n+1}.$$
  La borne supérieure suppose des scores à loi continue (sinon, briser les égalités au hasard).
- Pourquoi : le score du point test est, par échangeabilité, également susceptible d'occuper chacun des $n+1$ rangs parmi les $n+1$ scores ; il dépasse le $\lceil (n+1)(1-\alpha) \rceil$-ième avec probabilité au plus $\alpha$.
- Couverture **conditionnelle au jeu de calibration** (Angelopoulos et Bates, §3, attribuée à Vovk) : elle est aléatoire et suit une loi $\mathrm{Beta}(n+1-l,\, l)$ avec $l = \lfloor (n+1)\alpha \rfloor$ ; plus $n$ est grand, plus elle se resserre autour de $1-\alpha$.
- Jackknife+ : intervalle $[\,q^-_{\alpha}\{\hat\mu_{-i}(x) - R_i\},\ q^+_{\alpha}\{\hat\mu_{-i}(x) + R_i\}\,]$, où $R_i$ est le résidu *leave-one-out* du point $i$ et $\hat\mu_{-i}$ le modèle entraîné sans lui.
- Contrôle du risque (Angelopoulos et al., *Conformal risk control*) : généralise de la non-couverture à l'espérance d'une perte monotone (taux de faux négatifs, F1 par jeton) ; mêmes ingrédients, garantie $\mathbb E[L] \le \alpha$.

## En pratique

- **Pas besoin de refaire le modèle** : un jeu de calibration de quelques centaines à quelques milliers de points suffit à fixer $\hat q$ ; plus il est petit, plus la couverture réelle fluctue (voir la loi Beta).
- **Choisir le score, c'est choisir la forme des ensembles** : la garantie ne change pas, leur taille et leur adaptativité oui. Mesurer la taille moyenne et la couverture **par sous-groupe**, pas seulement globale.
- **Valider sur des données qui ressemblent à la production** : la garantie est conditionnelle à l'échangeabilité. Une dérive la casse sans bruit ; surveiller la couverture empirique en ligne.
- **Un intervalle large n'est pas une erreur de la méthode** : c'est un modèle peu informatif ou un score mal adapté.
- **Séries temporelles** : ne pas appliquer le split conformal tel quel sur des données ordonnées dans le temps. Calibrer sur une fenêtre récente, ou passer à ACI / EnbPI, en sachant ce que chacun garantit.

### En Python

- **MAPIE** (version 1.5.0, 2026-08-05, BSD-3, Python ≥ 3.10, relevé sur PyPI) : régression (`SplitConformalRegressor`, `CrossConformalRegressor`, `ConformalizedQuantileRegressor`, `TimeSeriesRegressor`), classification (`SplitConformalClassifier` avec scores `lac`, `aps`, `raps`), contrôle du risque.
- `crepes` (0.9.1), `TorchCP` (1.2.1, 2025-10-14) : alternatives, la seconde tournée vers PyTorch.
- `scikit-learn` n'a pas de module conforme : deux demandes ouvertes (#16383, #26430) sans suite visible ; c'est établi par ces indices, pas par une lecture du code source.
- Prévision de séries : `statsforecast` calcule des intervalles conformes par validation croisée (classe `ConformalIntervals`, `n_windows` d'au moins 2) ; `darts` propose des modèles conformes (`ConformalNaiveModel`).

### Travaux récents

Prépublications de septembre 2026, lues au niveau du résumé :

- Cheng, Liang, Barber — *Rolling Conformal Prediction in Sequential Model Training* (arXiv 2609.26951) : calibre chaque observation contre le prédicteur courant puis l'intègre à l'entraînement, sans jeu de validation ; garantie de couverture au pire $1-2\alpha$ pour viser $1-\alpha$.
- Zhai, Cheng, Wu — *Conformal Coverage of Time Series: Validity and Inference* (arXiv 2609.33868) : bornes non asymptotiques de l'erreur de couverture marginale du split conformal sous dépendance temporelle, et un théorème central limite sur la couverture réalisée.

Aucune enquête générale récente de qualité n'a été retrouvée dans cette recherche.

## Approches voisines & alternatives

- [[Intervalles de confiance]] — encadrent un paramètre, avec une loi supposée ou asymptotique ; l'ensemble conforme encadre une observation, sans loi.
- [[Calibration]] — probabilités fiables ; l'ensemble conforme n'en a pas besoin, mais un modèle bien calibré donne des ensembles plus petits.
- [[Régression quantile]] — prédit directement des quantiles conditionnels, sans garantie à taille finie ; CQR les corrige par un terme conforme.
- [[Bootstrap]] — rééchantillonne pour approcher une loi ; le jackknife+ lui est apparenté par le principe *leave-one-out*, mais en garde une garantie démontrée.
- [[Inférence bayésienne]] — intervalles de crédibilité : valides si le modèle et l'a priori sont justes, sans garantie fréquentielle sinon.
- [[Forecasting metrics]] — mesurer la qualité d'une prévision ponctuelle ; la prédiction conforme ajoute un encadrement de l'incertitude.
- [[statsforecast]] — intervalles conformes pour séries, par validation croisée.
- [[darts]] — modèles conformes autour d'un prévisionniste global.

## Pour aller plus loin

- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World*, Springer — fondement historique ; seules les métadonnées ont été vues, le texte n'a pas été lu.
- Lei, G'Sell, Rinaldo, Tibshirani, Wasserman (2018), *Distribution-free predictive inference for regression*, JASA 113(523) : <https://arxiv.org/abs/1604.04173>
- Angelopoulos & Bates (2021), *A gentle introduction to conformal prediction and distribution-free uncertainty quantification* : <https://arxiv.org/abs/2107.07511>
- Barber, Candès, Ramdas, Tibshirani (2021), *Predictive inference with the jackknife+*, Ann. Stat. 49(1) : <https://arxiv.org/abs/1905.02928>
- Barber, Candès, Ramdas, Tibshirani (2023), *Conformal prediction beyond exchangeability*, Ann. Stat. 51(2) : <https://arxiv.org/abs/2202.13415>
- Barber, Candès, Ramdas, Tibshirani (2021), *The limits of distribution-free conditional predictive inference*, Information and Inference : <https://arxiv.org/abs/1903.04684> ; Vovk (2012), *Conditional validity of inductive conformal predictors* : <https://arxiv.org/abs/1209.2673>
- Romano, Sesia, Candès (2020), *Classification with valid and adaptive coverage* : <https://arxiv.org/abs/2006.02544> ; Angelopoulos, Bates, Malik, Jordan (2021), RAPS : <https://arxiv.org/abs/2009.14193> ; Romano, Patterson, Candès (2019), CQR : <https://arxiv.org/abs/1905.03222>
- Tibshirani, Barber, Candès, Ramdas (2019), *Conformal prediction under covariate shift* : <https://arxiv.org/abs/1904.06019>
- Gibbs & Candès (2021), *Adaptive conformal inference under distribution shift* : <https://arxiv.org/abs/2106.00170> ; Zaffran et al. (2022), *Adaptive conformal predictions for time series* : <https://arxiv.org/abs/2202.07282> ; Xu & Xie, *Conformal prediction for time series* : <https://arxiv.org/abs/2010.09107>
- Angelopoulos, Bates, Fisch, Lei, Schuster, *Conformal risk control* : <https://arxiv.org/abs/2208.02814>
- Connexions brain : [[Calibration]], [[Intervalles de confiance]], [[Régression quantile]], [[statsforecast]], [[darts]].
