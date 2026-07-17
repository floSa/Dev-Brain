---
galaxie: wiki
type: concept
nom: PCA
alias: [ACP, Analyse en composantes principales, Principal Component Analysis]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis, unsupervised]
---

# PCA

## Aperçu

- Réduction de dimension linéaire pour variables **quantitatives** : trouve des axes orthogonaux (composantes principales) qui captent le maximum de variance.
- Décorrèle les variables et concentre l'information dans les premiers axes.

## Concepts clés

### Composantes principales
- Combinaisons linéaires des variables d'origine, deux à deux orthogonales (non corrélées).
- Classées par variance décroissante : la 1ʳᵉ porte le plus d'inertie, etc.

### Centrage et réduction
- Centrer (moyenne nulle) est obligatoire ; réduire (variance 1) dès que les unités diffèrent → PCA sur la corrélation plutôt que la covariance.
- Sans réduction, une variable à forte variance écrase les autres.

### Choisir le nombre d'axes
- Éboulis (scree plot) : chercher le coude. Critère de Kaiser ($\lambda > 1$ sur corrélation). Inertie cumulée (ex. 80 %).

### Lecture
- Cercle des corrélations (variables), plan factoriel (individus). Individus / variables supplémentaires projetés sans influencer les axes.

## Les maths, simplement

- Soit $X$ le tableau centré ($n$ individus, $p$ variables). On diagonalise la covariance $C = \frac{1}{n}X^\top X$ ([[Eigendecomposition]]).
- Vecteurs propres $u_j$ = axes principaux, valeurs propres $\lambda_j$ = variance portée. Composante : $c_j = X u_j$.
- De façon équivalente, [[SVD]] $X = U \Sigma V^\top$ : les colonnes de $V$ sont les axes, $\Sigma^2/n$ les $\lambda_j$.
- Inertie de l'axe $j$ : $\lambda_j / \sum_k \lambda_k$.

## En pratique

- Standardiser dès que les variables n'ont pas la même unité.
- Sensible aux valeurs extrêmes (la variance) → inspecter / robustifier.
- Axes = combinaisons → interprétation parfois floue ; s'aider des contributions et du cos².
- Outils : [[Dev/Services/Scikit-Learn|sklearn.decomposition.PCA]], [[Dev/Services/Prince|prince.PCA]], `FactoMineR::PCA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille dont PCA est le socle.
- [[Eigendecomposition]] — la machinerie algébrique : PCA diagonalise la matrice de covariance.
- [[SVD]] — la voie numériquement stable pour obtenir les mêmes axes sans former la covariance.
- [[CA]] — l'analogue pour une table de contingence.
- [[MCA]] — l'analogue pour des variables qualitatives.
- [[FAMD]] — l'extension aux données mixtes (PCA + MCA).
- [[MFA]] — quand les variables sont structurées en groupes.
- [[GPA]] — superposition de plusieurs configurations.
- [[PGA]] — la généralisation aux variétés riemanniennes.
- [[HCPC]] — clustering sur les composantes principales.
- [[ICA]] — le contraste majeur : décorréler (ordre 2) ne suffit pas, l'ICA vise l'indépendance (ordres supérieurs). Le blanchiment qu'elle exige *est* une PCA.
- [[NMF]] — la factorisation contrainte au positif : parties additives interprétables, au prix de l'orthogonalité et de la qualité de reconstruction.
- [[Autoencodeurs]] — la généralisation non linéaire : un autoencodeur linéaire retrouve exactement le sous-espace de la PCA.
- kernel PCA, [[t-SNE and UMAP]] — les autres voies non linéaires.

## Pour aller plus loin

- Pearson (1901), Hotelling (1933).
- Jolliffe — *Principal Component Analysis*.
