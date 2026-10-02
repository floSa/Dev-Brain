---
role: notion
nom: Double descente et généralisation des grands modèles
alias: [Double descente, double descent, deep double descent, model-wise double descent, epoch-wise double descent, seuil d'interpolation, interpolation threshold, surparamétrisation, overparameterization, benign overfitting, surapprentissage bénin, interpolation, multiple descent]
categorie: math/theorie-apprentissage
domaines: [data-sci, ml-eng]
tags: [learning-theory, deep-learning, regularization]
---

# Double descente et généralisation des grands modèles

## Aperçu

- Le récit classique dit : trop peu de capacité sous-apprend, trop de capacité sur-apprend, donc l'erreur de test dessine un **U** en fonction de la complexité du modèle (voir [[Compromis biais-variance]]). Les réseaux modernes, qui ont plus de paramètres que d'exemples et ajustent parfaitement leurs données d'entraînement (**interpolation**), contredisent ce récit : leur erreur de test peut **redescendre** après le point où le modèle interpole.
- La **double descente** (Belkin et al., 2019) nomme cette courbe : U classique, pic au **seuil d'interpolation**, puis seconde descente dans le régime **surparamétré**. Le **surapprentissage bénin** (Bartlett et al., 2020) est le résultat théorique associé : sous conditions, un interpolant de données bruitées prédit presque aussi bien que l'optimum.
- Le sujet reste **ouvert**. Les courbes existent et sont reproduites ; leur cause, leur universalité et la bonne mesure de « complexité » sont discutées (section *Désaccords*).

## Concepts clés

### Ce que la théorie classique prédit, et pourquoi elle échoue ici
- Les bornes de [[Generalization bounds|généralisation]] reposent sur la complexité de la classe de fonctions ([[VC dimension]], [[Rademacher complexity]]) : plus elle croît, plus la borne s'élargit, ce qui redonne le U.
- Trois raisons distinctes, d'après les sources lues, pour lesquelles ces bornes n'expliquent pas la généralisation des réseaux surparamétrés :
  - **Zhang et al. (2017)** : des réseaux standard ajustent à 100 % des **étiquettes aléatoires** (et des pixels aléatoires) ; leur capacité suffit à mémoriser le jeu entier. Le test ne vaut alors que le hasard, et les auteurs notent que la complexité de Rademacher empirique est proche de 1 : la borne est triviale. La régularisation explicite n'est ni nécessaire ni suffisante.
  - **Bartlett, Montanari, Rakhlin (2021)** : avec du **bruit**, les bornes de convergence uniforme sur l'excès de risque d'un interpolant « ne peuvent jamais descendre sous une constante », quelle que soit la taille d'échantillon.
  - **Nagarajan et Kolter (2019)** : ils exhibent un classifieur linéaire surparamétré et deux réseaux entraînés par descente de gradient pour lesquels toute borne par convergence uniforme bilatérale donne une garantie supérieure à $1-\varepsilon$, même restreinte aux classifieurs d'erreur de test $\le \varepsilon$ ; les bornes publiées peuvent croître avec la taille du jeu d'entraînement.

### Le seuil d'interpolation et la double descente
- **Belkin et al. (2019)** identifient la capacité d'une classe au nombre de paramètres. Sous le **seuil d'interpolation** (le plus petit modèle qui ajuste parfaitement l'entraînement), la courbe est un U ; au seuil, le risque est élevé ; au-delà, il redescend, souvent sous le minimum du U.
- Exemples du papier : *random Fourier features* sur MNIST (pic quand le nombre de features égale le nombre d'exemples, $N = n = 10^4$, solution de norme $\ell_2$ minimale), réseau à une couche cachée (seuil à $n \times K$, $K$ classes), forêts aléatoires.
- Mécanisme proposé : un biais inductif de **petite norme**. Plus de capacité donne des interpolants plus lisses, donc de plus petite norme (en *random features*, la norme décroît après le seuil).
- Réserves des auteurs : le pic est **difficile à observer en réseau profond** (non-convexité, arrêt précoce qui masque le pic).

### Deep double descent : trois axes
- **Nakkiran et al. (2019, ICLR 2020)** montrent la double descente **en fonction de la taille du modèle** (ResNet18 de largeur variable sur CIFAR-10 avec 15 % d'étiquettes bruitées), **du nombre d'époques** (même modèle entraîné plus longtemps : *epoch-wise*) et **du nombre d'échantillons** (*sample-wise*) : un Transformer sur IWSLT'14 est parfois **pire avec plus de données**.
- Ils généralisent le phénomène par la **complexité effective du modèle** (EMC) : le plus grand $n$ pour lequel la procédure d'entraînement atteint une erreur d'entraînement $\le \varepsilon$. L'EMC dépend de la **procédure d'entraînement**, pas seulement de l'architecture. Hypothèse : régime sous-paramétré (EMC nettement sous $n$), surparamétré (nettement au-dessus) et **critique** (EMC $\approx n$) ; c'est dans le régime critique qu'augmenter la complexité peut aggraver l'erreur. Les auteurs reconnaissent qu'ils ne formalisent pas « nettement ».
- Le **bruit d'étiquettes** n'est pas la cause mais un proxy de la mauvaise spécification (le pic est plus net avec du bruit). Les bornes de VC et de Rademacher ne **localisent pas le pic**, car elles ne dépendent ni des étiquettes ni de la procédure d'entraînement.

### Théorie asymptotique : régression à haute dimension
- **Hastie, Montanari, Rosset, Tibshirani** étudient l'interpolation de norme $\ell_2$ minimale (régression « sans ridge ») dans le régime proportionnel $\gamma = p/n$ ; ils retrouvent la double descente du risque et les bénéfices possibles de la surparamétrisation. **Mei et Montanari** donnent l'asymptotique exacte de la régression par *random features* et reproduisent la courbe de double descente sans hypothèse ad hoc.

### Surapprentissage bénin
- **Bartlett, Long, Lugosi, Tsigler (2020)** caractérisent à taille finie quand un ajustement parfait de données bruitées est compatible avec une bonne prédiction, en régression linéaire. Le risque en excès de l'interpolant de norme minimale est de l'ordre de $k^*/n + n/R_{k^*}$, où $k^*$ et $R_{k^*}$ dépendent des **rangs effectifs** de la covariance $\Sigma$ des covariables.
- « Bénin » : le risque est proche de l'optimal malgré l'ajustement parfait. Condition qualitative : beaucoup de **directions de faible variance** où le bruit des étiquettes peut se « cacher ». En dimension infinie, avec des valeurs propres $\lambda_k = k^{-\alpha}\ln^{-\beta}(k+1)$, c'est bénin si et seulement si $\alpha = 1$ et $\beta > 1$.
- **Limites écrites** par les auteurs : leurs hypothèses ne s'appliquent pas directement au noyau tangent neuronal ; l'extension aux réseaux profonds est un « important problème ouvert ».

## Désaccords et débats (laissés tels quels)

- **Antériorité.** Belkin et al. écrivent que la double descente « a pu être historiquement négligée ». **Loog et al. (2020)** le contestent : Vallet et al. (1989) montrent une double descente en courbe d'apprentissage sur des données artificielles, Opper et al. (1990) donnent des résultats théoriques, Duin (2000) la montre sur données réelles ; le SVM linéaire reste monotone dans ces travaux.
- **Quelle mesure de complexité ?** Belkin : le **nombre de paramètres**. Nakkiran : l'**EMC**, qui dépend de la procédure d'entraînement. **Curth, Jeffares, van der Schaar (2023)** : pour les arbres, le boosting et la régression linéaire des expériences de Belkin et al., il y a **deux axes de complexité implicites** ; la seconde descente apparaît à la transition de l'un à l'autre, sans lien intrinsèque avec $p = n$, et les courbes se replient en U avec un nombre effectif de paramètres. Ils limitent explicitement leur propos aux modèles **non profonds**.
- **La forme de la courbe est-elle une propriété du modèle ?** **Chen et al. (2021)** montrent, en régression linéaire, qu'on peut concevoir des courbes à plusieurs descentes : nombre et position des pics se contrôlent par la distribution des features ; selon eux, ces courbes viennent de l'interaction entre données et biais inductif, non du modèle seul, et elles se voient rarement en pratique. **Schaeffer et al. (2023)** : la double descente exige trois facteurs simultanés (de petites valeurs singulières non nulles dans les données d'entraînement, une forte projection des résidus sur ce mode, une variation notable des features de test sur ce mode) ; en retirer un supprime le phénomène, dans un cadre linéaire.
- **La régularisation efface-t-elle la double descente ?** **Nakkiran, Venkat, Kakade, Ma (2021)** : en régression linéaire à données isotropes, la ridge **optimale** est monotone en taille d'échantillon et en taille de modèle ; la monotonie peut échouer avec des covariables non gaussiennes et un bruit hétéroscédastique, et leurs résultats sur *random features* et CNN sont empiriques. Nakkiran et al. (2019) n'ont pas observé de « plus de données nuit » avec un arrêt précoce optimal, sans l'exclure.

### Travaux récents (préprints, 2026)
- **Farghly, Dupuis, Durmus, Simsekli (juillet 2026)**, modèles de diffusion : sauf taille d'échantillon exponentielle en la dimension, le sur-ajustement et la bonne généralisation sont incompatibles ; la lissité temporelle de la fonction de score et l'arrêt précoce protègent.
- **Urfin, Bonnaire, Biroli, Mézard (septembre 2026)**, diffusion : le pic d'interpolation se situe à un ratio paramètres/échantillons bien plus grand qu'en régression ($p \sim nm$ contre $p \sim n$), mais la dégradation du test commence dès $p \sim n$ ; une régularisation (ridge ou arrêt précoce) l'atténue.

## Les maths, simplement

- Régression linéaire à $p$ paramètres et $n$ exemples avec $p > n$ : il existe une infinité d'interpolants ; celui de **norme $\ell_2$ minimale** s'écrit $\hat\theta = X^{+} y = X^{\top}(XX^{\top})^{-1} y$. C'est le modèle des études asymptotiques, avec $\gamma = p/n$.
- Le risque de cet interpolant **diverge** au seuil $\gamma = 1$ (le jeu de données le plus « difficile » à interpoler, valeurs singulières proches de zéro), puis **décroît** quand $\gamma$ augmente : la variance baisse avec $\gamma$.
- Bartlett et al. : excès de risque $\asymp k^*/n + n/R_{k^*}$, avec $r_k = \sum_{i>k}\lambda_i/\lambda_{k+1}$, $R_k = (\sum_{i>k}\lambda_i)^2/\sum_{i>k}\lambda_i^2$ et $k^* = \min\{k : r_k \ge bn\}$. Le premier terme est le **biais effectif** (dimension utile), le second la **variance** du bruit absorbé.

## En pratique

- **Ne pas dimensionner un modèle avec la seule courbe en U**, ni conclure que « plus gros est toujours mieux ». Un pic peut exister autour de l'interpolation ; avec peu de données ou beaucoup de bruit d'étiquettes, plus de données peut même nuire (Nakkiran).
- La double descente existe aussi selon les **époques** (Nakkiran) : l'erreur de validation peut remonter puis redescendre. Avant de couper un entraînement à la première remontée, tracer la courbe sur toute la durée prévue.
- **Bruit d'étiquettes** : il accentue le pic ; nettoyer les étiquettes ou régulariser ([[Régularisation]]) est un levier plus sûr que de grossir le modèle.
- La double descente se **mesure** (tracer l'erreur en fonction de la taille du modèle, des époques ou des échantillons) ; elle ne s'invoque pas pour justifier un modèle surparamétré sans mesure.
- Une garantie à la VC ou à la Rademacher ne dit rien d'utile sur un réseau surparamétré qui interpole : s'attendre à des bornes vides ou triviales.

## Approches voisines & alternatives

- [[Compromis biais-variance]] — le récit classique en U, que la double descente complète sans le réfuter dans le régime sous-paramétré.
- [[Generalization bounds]] — les garanties à la VC et à la Rademacher, qui échouent dans le régime surparamétré (Zhang, Nagarajan-Kolter).
- [[VC dimension]] et [[Rademacher complexity]] — les mesures de complexité qui ne localisent pas le pic.
- [[PAC learning]] — le cadre de garantie classique ; il s'appuie sur la complexité de la classe, là où le surapprentissage bénin s'appuie sur le spectre de la covariance.
- [[No Free Lunch theorem]] — pas de généralisation sans biais inductif ; ici le biais de petite norme.
- [[Régularisation]] — la ridge optimale peut effacer le pic dans les cas linéaires isotropes (Nakkiran et al., 2021).
- [[Régression linéaire]] — le cadre où l'interpolation de norme minimale se calcule et se démontre.
- [[Scaling laws]] — l'autre cadre où « plus gros » est étudié, côté perte de pré-entraînement des modèles de langage ; les sources lues pour cette page ne relient pas les deux littératures.
- [[Perceptron et MLP]] — le réseau à une couche cachée de l'expérience de Belkin et al.
- [[Apprentissage supervisé]] — le cadre général de la généralisation à partir d'exemples étiquetés.
- *Briques voisines* : sans objet, aucune brique du vault n'implémente cette notion.

## Pour aller plus loin

- Belkin, Hsu, Ma & Mandal (2019) — [*Reconciling modern machine-learning practice and the classical bias-variance trade-off*](https://arxiv.org/abs/1812.11118), PNAS 116(32).
- Nakkiran, Kaplun, Bansal, Yang, Barak & Sutskever (2019) — [*Deep Double Descent: Where Bigger Models and More Data Hurt*](https://arxiv.org/abs/1912.02292), ICLR 2020.
- Bartlett, Long, Lugosi & Tsigler (2020) — [*Benign overfitting in linear regression*](https://arxiv.org/abs/1906.11300), PNAS 117(48).
- Zhang, Bengio, Hardt, Recht & Vinyals (2017) — [*Understanding deep learning requires rethinking generalization*](https://arxiv.org/abs/1611.03530), ICLR 2017.
- Hastie, Montanari, Rosset & Tibshirani — [*Surprises in High-Dimensional Ridgeless Least Squares Interpolation*](https://arxiv.org/abs/1903.08560) ; Mei & Montanari — [*The generalization error of random features regression*](https://arxiv.org/abs/1908.05355).
- Bartlett, Montanari & Rakhlin (2021) — [*Deep learning: a statistical viewpoint*](https://arxiv.org/abs/2103.09177), Acta Numerica ; Nagarajan & Kolter (2019) — [*Uniform convergence may be unable to explain generalization in deep learning*](https://arxiv.org/abs/1902.04742), NeurIPS 2019.
- Loog, Viering, Mey, Krijthe & Tax (2020) — [*A Brief Prehistory of Double Descent*](https://arxiv.org/abs/2004.04328), PNAS.
- Curth, Jeffares & van der Schaar (2023) — [*A U-turn on Double Descent*](https://arxiv.org/abs/2310.18988), NeurIPS 2023 ; Chen, Min, Belkin & Karbasi (2021) — [*Multiple Descent: Design Your Own Generalization Curve*](https://arxiv.org/abs/2008.01036) ; Schaeffer et al. (2023) — [*Double Descent Demystified*](https://arxiv.org/abs/2303.14151).
- Nakkiran, Venkat, Kakade & Ma (2021) — [*Optimal Regularization Can Mitigate Double Descent*](https://arxiv.org/abs/2003.01897), ICLR 2021.
- Farghly, Dupuis, Durmus & Simsekli (2026) — [*Benign Overfitting Does Not Occur in Diffusion Models*](https://arxiv.org/abs/2607.02671) ; Urfin, Bonnaire, Biroli & Mézard (2026) — [*Double Descent and Malign Overfitting in Diffusion Models*](https://arxiv.org/abs/2609.26392).
