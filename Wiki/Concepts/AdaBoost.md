---
galaxie: wiki
type: concept
nom: AdaBoost
alias: [Adaptive Boosting, Boosting adaptatif, AdaBoostClassifier, SAMME]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, ensemble, boosting, tree-based, classification]
---

# AdaBoost

## Aperçu

- Le **premier** algorithme de [[Boosting|boosting]] qui ait vraiment fonctionné (1995), et la réponse positive à une question théorique ouverte : peut-on transformer un apprenant à peine meilleur que le hasard en un apprenant arbitrairement bon ? Oui.
- Le mécanisme : entraîner un modèle faible, **repondérer les exemples qu'il a ratés** pour que le suivant s'y concentre, recommencer. Le vote final est pondéré par la qualité de chaque modèle.

## Concepts clés

### Repondérer plutôt que corriger
- C'est la différence de fond avec le [[Gradient Boosting (GBDT)|gradient boosting]] : AdaBoost ne touche pas à la cible, il change le **poids des observations**. Un point mal classé pèse plus lourd au tour suivant, jusqu'à ce qu'un apprenant s'en occupe.
- Le gradient boosting, lui, garde les poids constants et change la **cible** (les pseudo-résidus). Deux façons de dire « occupe-toi de ce que j'ai raté ».

### Les apprenants faibles
- Typiquement des **souches** (*decision stumps*) : des [[Arbres de décision|arbres]] à un seul niveau, donc une seule question. À peine mieux que le hasard isolément.
- L'exigence est minimale : il suffit que l'apprenant fasse mieux que 50 % en binaire. C'est le point théorique remarquable — la médiocrité garantie suffit.

### Le vote pondéré
- Chaque apprenant reçoit un poids $\alpha_m$ fonction de son erreur : précis → voix forte, médiocre → voix faible. Un apprenant à 50 % d'erreur reçoit un poids nul (il n'apporte rien), et un apprenant *pire* que le hasard reçoit un poids négatif — on l'écoute à l'envers.

### Ce qu'il est réellement
- Résultat majeur d'après-coup : AdaBoost **est** du gradient boosting avec la **perte exponentielle**. Ce n'était pas le point de vue de départ ; c'est Friedman, Hastie et Tibshirani qui l'ont montré, unifiant les deux familles.
- Conséquence directe et pratique : la perte exponentielle $e^{-y F(x)}$ croît de façon explosive quand un point est mal classé avec confiance. D'où sa **sensibilité notoire au bruit et aux valeurs aberrantes** — un point mal étiqueté voit son poids exploser et monopolise les apprenants suivants.

### Les paramètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_estimators` | Nombre d'apprenants faibles | ↑ = plus de capacité, surapprentissage tardif mais réel |
| `learning_rate` | Rétrécit la contribution de chaque apprenant | ↓ = meilleure généralisation, mais exige plus d'estimateurs |
| `estimator` | L'apprenant faible (souche par défaut) | Plus profond = moins « faible », s'éloigne de l'esprit AdaBoost |
| `algorithm` | Plus rien à régler | `SAMME.R` retiré en sklearn 1.6 ; le paramètre lui-même est déprécié depuis 1.6 et disparaît en 1.8 — ne plus le passer |

- `learning_rate` et `n_estimators` **s'échangent** : diviser le premier par deux demande de doubler le second. Les régler ensemble, jamais séparément.

## Les maths, simplement

- Erreur pondérée de l'apprenant $m$ : $\varepsilon_m = \dfrac{\sum_i w_i \, \mathbb{1}[y_i \ne h_m(x_i)]}{\sum_i w_i}$ — la proportion d'erreurs, comptée avec les poids courants.
- Poids de vote de l'apprenant : $\alpha_m = \frac{1}{2} \ln\!\left(\dfrac{1 - \varepsilon_m}{\varepsilon_m}\right)$. Lecture : $\varepsilon_m \to 0$ → $\alpha_m \to +\infty$ (on lui fait totalement confiance) ; $\varepsilon_m = 0{,}5$ → $\alpha_m = 0$ (voix nulle) ; $\varepsilon_m > 0{,}5$ → $\alpha_m < 0$ (on inverse sa réponse).
- Mise à jour des poids : $w_i \leftarrow w_i \, e^{\alpha_m \mathbb{1}[y_i \ne h_m(x_i)]}$, puis renormalisation. Les points ratés voient leur poids croître **exponentiellement**.
- Prédiction finale : $F(x) = \operatorname{sign}\left(\sum_{m=1}^{M} \alpha_m h_m(x)\right)$.
- L'équivalence avec le gradient boosting : AdaBoost minimise $\sum_i e^{-y_i F(x_i)}$ par étapes. C'est cette exponentielle qui explique à la fois sa vitesse de convergence et sa fragilité au bruit.

## En pratique

- **Aujourd'hui, on ne l'utilise plus.** Sur tabulaire, [[Gradient Boosting (GBDT)|LightGBM/XGBoost/CatBoost]] le dominent en performance comme en robustesse. Sa valeur est **pédagogique et historique** : il rend le boosting intelligible en trois lignes là où le gradient boosting demande de penser en espace de fonctions.
- **Fragile aux étiquettes bruitées** — c'est sa faiblesse structurelle, pas un défaut de réglage. Un jeu avec des erreurs d'étiquetage le fait sur-apprendre sur ces erreurs précisément. Si les étiquettes sont douteuses, prendre un [[Random Forest]] (insensible) ou un gradient boosting à perte robuste.
- **Pas besoin de standardiser** : ses apprenants sont des arbres ([[Types de données et choix de modèle]]).
- Il surapprend **plus lentement** qu'on ne s'y attend — une curiosité empirique restée longtemps inexpliquée, dont la marge de classification donne une lecture partielle.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.AdaBoostClassifier / AdaBoostRegressor]].

## Approches voisines & alternatives

- [[Boosting]] — le chapeau de la famille ; AdaBoost en est le membre fondateur.
- [[Gradient Boosting (GBDT)]] — le successeur qui l'a rendu obsolète ; AdaBoost en est le cas particulier à perte exponentielle.
- [[Random Forest]] — l'autre grande famille d'ensembles d'arbres : parallèle et insensible au bruit, là où AdaBoost est séquentiel et fragile.
- [[Bagging]] — le pendant parallèle : rééchantillonner plutôt que repondérer.
- [[Ensembling]] — la vue d'ensemble (bagging, boosting, stacking, voting).
- [[Arbres de décision]] — l'apprenant faible qu'il empile (souches).
- [[Compromis biais-variance]] — le boosting attaque le biais, le bagging la variance.

## Pour aller plus loin

- Freund & Schapire (1997) — *A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting* : l'article fondateur, prix Gödel 2003.
- Friedman, Hastie, Tibshirani (2000) — *Additive Logistic Regression: A Statistical View of Boosting* : la démonstration qu'AdaBoost = perte exponentielle.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 10.1-10.4.
