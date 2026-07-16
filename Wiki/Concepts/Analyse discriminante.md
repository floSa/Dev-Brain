---
galaxie: wiki
type: concept
nom: Analyse discriminante
alias: [LDA, QDA, Linear Discriminant Analysis, Quadratic Discriminant Analysis, Analyse discriminante linéaire, Analyse factorielle discriminante, AFD, LinearDiscriminantAnalysis]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, classification, bayesian, linear-model]
---

# Analyse discriminante

## Aperçu

- Classifieur **génératif** qui suppose que, dans chaque classe, les données suivent une **loi normale multivariée**. On estime la moyenne et la covariance de chaque classe, puis on retourne l'inférence par le théorème de Bayes.
- Deux variantes selon une seule hypothèse : les classes partagent-elles la même matrice de covariance ? Oui → **LDA**, frontière linéaire. Non → **QDA**, frontière quadratique.
- LDA a une double vie : classifieur **et** méthode de [[Réduction de dimension|réduction de dimension]] supervisée — c'est la seule qui projette en maximisant la séparation des classes plutôt que la variance totale.

## Concepts clés

### L'hypothèse qui fait tout
- On modélise $P(x \mid y = k) = \mathcal{N}(\mu_k, \Sigma_k)$ : chaque classe est un nuage gaussien. C'est une hypothèse **forte** — et c'est précisément ce qui rend le modèle économe en données.
- Comme [[Naive Bayes]], c'est un modèle génératif ; mais là où Naive Bayes suppose les variables **indépendantes**, LDA/QDA modélisent leur **covariance**. C'est un Naive Bayes qui aurait cessé d'être naïf.

### LDA — covariance commune
- Hypothèse : $\Sigma_1 = \Sigma_2 = … = \Sigma_K = \Sigma$. Une seule matrice à estimer, mise en commun sur toutes les classes.
- Conséquence mathématique remarquable : les termes quadratiques **s'annulent** entre classes, et la frontière devient un **hyperplan**. La linéarité n'est pas un choix, c'est un produit de l'hypothèse.
- Peu de paramètres → très stable à petit $n$.

### QDA — covariance par classe
- Chaque classe garde sa propre $\Sigma_k$ : les nuages peuvent avoir des orientations et des étalements différents. Les termes quadratiques ne s'annulent plus → frontière **courbe**.
- Coût : $K$ matrices $d \times d$ à estimer. Le nombre de paramètres explose avec $d$, et QDA devient inutilisable dès que $d$ est grand devant $n$ par classe.

### LDA comme réduction de dimension
- Usage souvent oublié et pourtant précieux : LDA projette sur au plus $K - 1$ axes en maximisant le rapport **variance inter-classes / variance intra-classes**.
- La différence avec [[PCA]] est structurelle : PCA cherche les directions de plus grande variance **en ignorant les classes** ; LDA cherche celles qui **séparent les classes**. Sur un problème supervisé, la direction la plus variable n'est pas forcément la plus discriminante.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `solver` | `svd` (défaut, ne calcule pas $\Sigma$), `lsqr`, `eigen` | `svd` pour $d$ grand ; `eigen`/`lsqr` requis pour le `shrinkage` |
| `shrinkage` | Régularise $\Sigma$ vers une matrice diagonale | **Le paramètre décisif quand $n$ est petit.** `'auto'` (Ledoit-Wolf) est un excellent défaut |
| `n_components` | Axes conservés en mode réduction | Au maximum $K - 1$ — limite structurelle, pas un choix |
| `priors` | Probabilités a priori des classes | Par défaut estimées ; à forcer si l'échantillon ne reflète pas la réalité |
| `reg_param` (QDA) | Régularise chaque $\Sigma_k$ | Souvent indispensable, sinon $\Sigma_k$ est singulière |

## Les maths, simplement

- Par Bayes : $P(y = k \mid x) \propto \pi_k \, \mathcal{N}(x; \mu_k, \Sigma_k)$, avec $\pi_k$ la proportion de la classe $k$.
- En passant au log et en jetant ce qui est commun aux classes, on obtient la **fonction discriminante** de LDA : $\delta_k(x) = x^\top \Sigma^{-1} \mu_k - \frac{1}{2}\mu_k^\top \Sigma^{-1} \mu_k + \log \pi_k$. Elle est **linéaire en $x$** — d'où le nom, et d'où l'hyperplan.
- En QDA, $\Sigma_k$ diffère par classe : le terme $-\frac{1}{2} x^\top \Sigma_k^{-1} x$ ne se simplifie plus et subsiste. La frontière devient quadratique.
- Nombre de paramètres de covariance : LDA en estime $\frac{d(d+1)}{2}$ ; QDA en estime $K \times \frac{d(d+1)}{2}$. Avec $d = 50$ et $K = 3$ : 1 275 contre 3 825. C'est toute la différence de robustesse.
- Critère de la version réduction : $\max_w \dfrac{w^\top S_B \, w}{w^\top S_W \, w}$ — maximiser la dispersion **entre** classes ($S_B$) rapportée à la dispersion **dans** les classes ($S_W$).

## En pratique

- **La baseline oubliée.** Rapide, sans hyperparamètre obligatoire, souvent compétitive — et solution *fermée*, sans optimisation itérative. À essayer au même titre qu'une [[Régression logistique]].
- **LDA vs [[Régression logistique]]** — même frontière linéaire, deux philosophies. LDA fait plus d'hypothèses (gaussiennes, covariance commune) : elle est **meilleure quand $n$ est petit** et que les hypothèses tiennent à peu près. La logistique, discriminante, est plus robuste quand elles sont violées, et gère mieux les valeurs aberrantes.
- **Choisir entre LDA et QDA est un arbitrage [[Compromis biais-variance|biais-variance]]** : QDA est plus flexible (moins de biais) mais estime $K$ fois plus de paramètres (plus de variance). À petit $n$ par classe, LDA gagne presque toujours. Ne pas trancher a priori — comparer par [[Validation croisée|CV]].
- **Le `shrinkage` sauve LDA** quand $n$ est petit ou les variables corrélées : $\Sigma$ estimée est alors mal conditionnée et son inversion instable. `shrinkage='auto'` devrait être un réflexe.
- **Standardiser n'est pas requis** mathématiquement (le $\Sigma^{-1}$ absorbe les échelles), mais reste conseillé pour la stabilité numérique ([[Mise à l'échelle]]).
- **Sensible aux variables non gaussiennes et aux outliers** : les moyennes et covariances sont des estimateurs peu robustes. Si les distributions sont franchement asymétriques, transformer ou passer à un modèle sans hypothèse ([[Gradient Boosting (GBDT)]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.discriminant_analysis]] — `LinearDiscriminantAnalysis` (aussi utilisable en `transform` pour la projection), `QuadraticDiscriminantAnalysis`.

## Approches voisines & alternatives

- [[Régression logistique]] — même frontière linéaire, mais discriminante : le comparatif de référence, et le choix par défaut quand $n$ est confortable.
- [[Naive Bayes]] — le génératif voisin, en plus radical : suppose les variables indépendantes au lieu d'estimer leur covariance.
- [[PCA]] — l'autre projection linéaire, non supervisée : maximise la variance, pas la séparation des classes.
- [[Réduction de dimension]] — LDA en est le membre supervisé.
- [[Gaussian Mixture Models (GMM)]] — la version non supervisée de la même idée : des gaussiennes, mais sans classes connues.
- [[MANOVA et tests multivariés]] — le pendant inférentiel : tester si les groupes diffèrent, plutôt que prédire l'appartenance.
- [[Classification]] — le chapeau de la tâche.
- [[Types de données et choix de modèle]] — quand ses hypothèses gaussiennes sont tenables.

## Pour aller plus loin

- Fisher (1936) — *The Use of Multiple Measurements in Taxonomic Problems* : l'article fondateur, et le jeu de données iris.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 4.3.
- Ledoit & Wolf (2004) — l'estimateur de shrinkage derrière `shrinkage='auto'`.
