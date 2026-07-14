---
galaxie: wiki
type: concept
nom: Gaussian Mixture Models (GMM)
alias: [GMM, Mélange de gaussiennes, Modèle de mélange gaussien, Mixture models, Mélanges gaussiens]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised, maximum-likelihood]
---

# Gaussian Mixture Models (GMM)

## Aperçu

- Méthode de [[Clustering]] **probabiliste** : suppose que les données proviennent d'un mélange de $K$ lois gaussiennes, chacune correspondant à un cluster.
- Produit une affectation **souple** (chaque point a une probabilité d'appartenir à chaque cluster) et des clusters **ellipsoïdaux** (orientation et étirement libres), là où K-Means n'autorise que des sphères.

## Concepts clés

### Modèle génératif
- Densité : un point est tiré en choisissant d'abord une composante $k$ (poids $\pi_k$), puis en tirant dans sa gaussienne $\mathcal{N}(\mu_k, \Sigma_k)$. Trois jeux de paramètres : poids, moyennes, covariances.

### Responsabilités (affectation souple)
- Pour chaque point, la probabilité a posteriori d'appartenir à chaque composante. L'affectation « dure » s'obtient en prenant la composante la plus probable.

### Algorithme EM
- Ajusté par **maximum de vraisemblance** via *Expectation-Maximization* : (E) calculer les responsabilités à paramètres fixés ; (M) ré-estimer poids/moyennes/covariances pondérés par ces responsabilités. Converge vers un maximum local → init (souvent k-means) et relances recommandées.

### Type de covariance
- `full`, `tied`, `diag`, `spherical` : contrôle la forme des clusters et le nombre de paramètres. `spherical` + affectation dure ≈ [[K-Means]].

## Les maths, simplement

- Densité du mélange : $\displaystyle p(x) = \sum_{k=1}^{K} \pi_k \, \mathcal{N}(x \mid \mu_k, \Sigma_k)$, avec $\sum_k \pi_k = 1$.
- Responsabilité (étape E) : $\gamma_k(x) = \dfrac{\pi_k \, \mathcal{N}(x \mid \mu_k, \Sigma_k)}{\sum_j \pi_j \, \mathcal{N}(x \mid \mu_j, \Sigma_j)}$ — la part du point $x$ attribuée à la composante $k$.
- EM maximise la log-vraisemblance $\sum_i \log p(x_i)$, croissante à chaque itération.

## En pratique

- Choisir $K$ par **BIC / AIC** (vraisemblance pénalisée par le nombre de paramètres) — un avantage propre aux modèles probabilistes.
- Plus flexible que K-Means (clusters allongés, corrélés, recouvrants) mais plus de paramètres → besoin de plus de données, risque de surajustement avec `full` en grande dimension.
- Sensible à l'initialisation et aux composantes dégénérées (covariance qui s'effondre sur un point) — régulariser (`reg_covar`).
- La variante bayésienne (`BayesianGaussianMixture`) peut élaguer les composantes inutiles et estimer un $K$ effectif.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.mixture.GaussianMixture / BayesianGaussianMixture]].

## Approches voisines & alternatives

- [[Clustering]] — le cadre général et les autres familles.
- [[K-Means]] — cas limite de GMM (covariance sphérique, affectation dure) ; plus rapide, mais clusters sphériques et affectation tranchée.
- [[Classification hiérarchique (CAH)]] / [[DBSCAN]] — alternatives sans hypothèse gaussienne, géométrique ou par densité.

## Pour aller plus loin

- Dempster, Laird, Rubin (1977) — *Maximum Likelihood from Incomplete Data via the EM Algorithm*.
- Bishop — *Pattern Recognition and Machine Learning*, ch. 9 (Mixture Models and EM).
