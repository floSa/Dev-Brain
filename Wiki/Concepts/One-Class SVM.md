---
galaxie: wiki
type: concept
nom: One-Class SVM
alias: [OCSVM, SVM à une classe, OneClassSVM, SGDOneClassSVM, Novelty detection]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised]
---

# One-Class SVM

## Aperçu

- Détecteur d'anomalies qui apprend une **frontière enveloppant les données normales** : tout ce qui tombe à l'extérieur est déclaré anormal. Il n'a qu'une seule classe à disposition — d'où son nom.
- Troisième voie de la famille, à côté de la densité ([[Local Outlier Factor]]) et de l'isolement ([[Isolation Forest]]) : ici on trace un **contour**. Reprend la machinerie du [[SVM]] — marge et astuce du noyau — appliquée à un problème sans étiquettes.

## Concepts clés

### Apprendre une frontière sans contre-exemples
- Un classifieur ordinaire a besoin des deux camps. Ici on ne dispose que du « normal » : impossible de tracer une séparation entre deux classes.
- La parade de Schölkopf : séparer les données **de l'origine** dans l'espace du noyau, en maximisant la marge. La région qui contient les données devient l'enveloppe du normal.

### Le paramètre `nu` — le seul qui gouverne
- `nu` ∈ (0, 1] a une double signification, et c'est ce qui le rend élégant : c'est à la fois une **borne supérieure sur la fraction d'anomalies** tolérées à l'entraînement, et une **borne inférieure sur la fraction de vecteurs de support**.
- Concrètement, `nu=0.05` ≈ « j'admets que 5 % de mes données d'entraînement sont anormales ». Il joue le rôle du `contamination` d'[[Isolation Forest]], mais **il agit pendant l'entraînement**, pas seulement au seuillage : il déforme réellement la frontière.
- C'est une hypothèse imposée, pas une découverte. Le régler trop haut rogne l'enveloppe et fabrique des faux positifs.

### `gamma` — la souplesse du contour
- Comme pour le [[SVM]] à noyau RBF : `gamma` grand → contour qui épouse chaque point, enveloppe morcelée, surapprentissage. `gamma` petit → contour lisse et large, proche d'une ellipse.
- `nu` et `gamma` **interagissent** : ils se règlent ensemble, jamais l'un après l'autre.

### La faiblesse structurelle
- Le modèle suppose que les données d'entraînement sont **propres** — ou du moins que leur pollution est bornée par `nu`. S'il y a plus d'anomalies que prévu, elles sont incorporées dans l'enveloppe et deviennent « normales ».
- Réputé **très sensible aux hyperparamètres** et enclin au surapprentissage. Beaucoup de praticiens lui préfèrent [[Isolation Forest]] pour cette raison, à performance comparable et sans réglage.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `nu` | Fraction d'anomalies tolérée à l'entraînement + borne basse des vecteurs de support | **Le levier n°1.** ↑ = enveloppe plus serrée, plus de faux positifs |
| `gamma` | Portée d'influence d'un point (noyau RBF) | ↑ = contour contorsionné (surapprentissage) ; ↓ = contour lisse |
| `kernel` | `rbf` par défaut | `linear` seulement si l'enveloppe est convexe et simple |
| `max_iter` | Borne d'itérations | `-1` (illimité) par défaut ; le mettre si la convergence traîne |

## Les maths, simplement

- Le problème résolu : $\min_{w, \rho, \xi} \; \frac{1}{2}\lVert w \rVert^2 + \dfrac{1}{\nu n}\sum_i \xi_i - \rho$ sous contrainte $w^\top \phi(x_i) \ge \rho - \xi_i$, avec $\xi_i \ge 0$.
- Lecture : on cherche l'hyperplan qui sépare les données de l'**origine** avec la plus grande marge $\rho / \lVert w \rVert$, en tolérant des violations $\xi_i$ dont le coût est réglé par $\nu$.
- La fonction de décision est $f(x) = \operatorname{sign}\big(w^\top \phi(x) - \rho\big)$ : positif = normal, négatif = anomalie.
- Le noyau RBF $K(x, x') = \exp(-\gamma \lVert x - x' \rVert^2)$ projette dans un espace de dimension infinie où **toutes les données ont la même norme** et vivent dans un même orthant — ce qui rend la séparation d'avec l'origine possible et sensée.
- Complexité entre $O(n^2)$ et $O(n^3)$ : le facteur qui le disqualifie à grande échelle.

## En pratique

- **Standardiser est obligatoire**, comme pour tout [[SVM]] à noyau ([[Mise à l'échelle]]).
- **Ne passe pas à l'échelle** : impraticable au-delà de quelques dizaines de milliers de points. À grand $n$, utiliser `SGDOneClassSVM` (approximation linéaire par descente de gradient stochastique, complexité linéaire) — le plus souvent combiné à un `Nystroem` pour retrouver un effet de noyau. Ou passer à [[Isolation Forest]].
- **Sa vraie niche : la détection de nouveauté** (*novelty detection*) — entraîner sur un jeu **propre et certifié normal**, puis scorer du nouveau. C'est le cas d'usage où il est légitime, et où sa fragilité à la pollution cesse d'être un problème.
- **En détection d'outliers sur données polluées** (le cas courant), il est le moins recommandable des trois. [[Isolation Forest]] fait aussi bien sans réglage et en temps linéaire.
- Le régler est pénible en pratique : sans étiquettes, aucune [[Validation croisée|CV]] n'est possible pour choisir `nu` et `gamma`. On procède par balayage et jugement d'expert sur le haut du classement.
- Ne gère ni les NaN ni les catégorielles brutes : imputer et encoder en amont.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.svm.OneClassSVM]] ; `sklearn.linear_model.SGDOneClassSVM` à grande échelle ; [[Dev/Services/PyOD|PyOD]] pour comparer les détecteurs sous une API commune.

## Approches voisines & alternatives

- [[Isolation Forest]] — le concurrent recommandé par défaut : linéaire en $n$, sans standardisation ni réglage sensible.
- [[Local Outlier Factor]] — l'approche par densité locale ; seul à capter les anomalies contextuelles.
- [[SVM]] — le parent supervisé, dont il reprend la marge et l'astuce du noyau.
- [[Détection d'outliers multivariée]] — le chapeau : toutes les familles et leurs hypothèses.
- [[Gaussian Mixture Models (GMM)]] — l'approche par densité paramétrique, plus interprétable.
- [[Détection d'outliers univariée]] — quand une seule variable suffit ; à essayer d'abord.
- [[Apprentissage non supervisé]] — le cadre englobant.
- [[Types de données et choix de modèle]] — l'aiguillage amont.

## Pour aller plus loin

- Schölkopf et al. (2001) — *Estimating the Support of a High-Dimensional Distribution* : l'article fondateur et la double lecture de $\nu$.
- Documentation scikit-learn — *Novelty and Outlier Detection* : le comparatif visuel des trois détecteurs, et la distinction novelty / outlier detection.
