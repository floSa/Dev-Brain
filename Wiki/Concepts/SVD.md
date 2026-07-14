---
galaxie: wiki
type: concept
nom: SVD
alias: [décomposition en valeurs singulières, singular value decomposition, valeurs singulières]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [linear-algebra, matrix-decomposition, eigenvalue, dimensionality-reduction]
---

# SVD

## Aperçu

- Toute matrice $A$ (même rectangulaire) s'écrit $A = U \Sigma V^\top$ : une rotation, une mise à l'échelle par des **valeurs singulières** $\sigma_i \geq 0$, puis une autre rotation.
- La décomposition la plus générale et la plus stable de l'algèbre linéaire : socle de la [[PCA]], de la compression, du pseudo-inverse et de la recommandation.

## Concepts clés

### La factorisation
- $A = U \Sigma V^\top$ : $U$ et $V$ orthogonales (vecteurs singuliers gauche/droite), $\Sigma$ diagonale des $\sigma_1 \geq \sigma_2 \geq \dots \geq 0$.
- Les $\sigma_i$ mesurent « combien » chaque direction est étirée ; leur nombre non nul = rang de $A$.

### Lien avec l'eigendecomposition
- Les $\sigma_i^2$ sont les valeurs propres de $A^\top A$ (et $A A^\top$) ; $V$ et $U$ en sont les vecteurs propres. La SVD est donc l'[[Eigendecomposition]] des matrices $A^\top A$, mais calculée directement et sans perte de stabilité.
- Pour une matrice symétrique définie positive, SVD et eigendecomposition coïncident.

### Troncature de rang faible (Eckart-Young)
- Garder les $k$ plus grandes valeurs singulières donne la **meilleure** approximation de rang $k$ au sens de l'erreur quadratique : $A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^\top$.
- Fondement de la compression d'images, du débruitage et de la [[Réduction de dimension]] : l'information utile est dans les premiers $\sigma_i$, le bruit dans les derniers.

### Pseudo-inverse
- $A^+ = V \Sigma^+ U^\top$ résout les moindres carrés même quand $A$ n'est pas inversible (système sur/sous-déterminé).

## Les maths, simplement

- Forme : $A = U \Sigma V^\top$ avec $U^\top U = I$, $V^\top V = I$, $\Sigma = \mathrm{diag}(\sigma_i)$.
- Lecture : $A x$ projette $x$ sur les axes de $V$, étire par les $\sigma_i$, puis replace sur les axes de $U$.
- Lien PCA : sur un tableau centré $X$, $X = U\Sigma V^\top$ ; les colonnes de $V$ sont les axes principaux et $\sigma_i^2/n$ les variances portées (cf. [[PCA]]).

## En pratique

- Toujours préférer la SVD à l'inversion ou à l'eigendecomposition de $A^\top A$ quand la stabilité compte.
- SVD tronquée / randomisée pour les grandes matrices creuses (`scipy.sparse.linalg.svds`, `sklearn.decomposition.TruncatedSVD` — LSA en NLP).
- Coûteuse sur très grandes matrices denses : envisager une version randomisée.
- Outils : `numpy.linalg.svd`, `scipy.linalg.svd`, [[Dev/Services/Scikit-Learn|sklearn]] (`TruncatedSVD`, `PCA`), [[Dev/Services/numpy|numpy]].

## Approches voisines & alternatives

- [[Eigendecomposition]] — la SVD en est la généralisation à toute matrice ; reliées via $A^\top A$.
- [[PCA]] — l'application statistique directe : SVD du tableau centré.
- [[Réduction de dimension]] — la troncature de rang faible est le mécanisme commun à la famille.
- [[Matrix decompositions]] — la factorisation la plus générale du catalogue.

## Pour aller plus loin

- Eckart & Young (1936) — optimalité de l'approximation de rang faible.
- LSA / LSI (recherche d'information), filtrage collaboratif (Netflix Prize) — usages emblématiques.
- Halko, Martinsson, Tropp (2011) — SVD randomisée pour le passage à l'échelle.
