---
galaxie: wiki
type: concept
nom: Generalization bounds
alias: [Bornes de généralisation, borne de généralisation, generalization bound, erreur de généralisation, generalization gap]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [learning-theory, generalization-bound]
---

# Generalization bounds

## Aperçu

- Une borne de généralisation majore le **risque réel** $R(h)$ (erreur sur la vraie distribution) par le **risque empirique** $\hat R(h)$ (erreur observée) plus un terme de **pénalité de complexité**, avec une probabilité $1-\delta$.
- C'est la traduction quantitative du [[Compromis biais-variance]] : minimiser la somme « erreur d'entraînement + capacité » plutôt que l'erreur d'entraînement seule.

## Concepts clés

### La forme canonique
- $R(h) \le \hat R(h) + \underbrace{\text{complexité}(\mathcal H, n, \delta)}_{\text{generalization gap}}$.
- Le terme de complexité s'instancie selon l'outil : $\ln|\mathcal H|$ (classe finie, [[PAC learning]]), [[VC dimension]] $d$, ou [[Rademacher complexity]] (data-dependent).

### Convergence uniforme
- L'enjeu n'est pas une hypothèse mais **toute** la classe à la fois : il faut que $\sup_{h\in\mathcal H}|R(h)-\hat R(h)|$ soit petit, car l'apprentissage *choisit* $h$ après avoir vu les données. D'où la borne d'union et les [[Inégalités de concentration]] (Hoeffding, McDiarmid).

### Structural Risk Minimization (SRM)
- Plutôt que minimiser $\hat R$ seul, on minimise $\hat R(h) + \text{pénalité}(\mathcal H)$ sur une hiérarchie de classes emboîtées. La [[Régularisation]] (Ridge/Lasso) en est l'incarnation pratique : pénaliser la complexité = remonter la borne.

## Les maths, simplement

- Le gap décroît typiquement en $\sqrt{\dfrac{\text{capacité}}{n}}$ : **doubler les données** divise l'écart par $\sqrt 2$, **doubler la capacité** le multiplie par $\sqrt 2$.
- Borne VC : $R(h)\le \hat R(h)+\sqrt{\dfrac{d(\ln\frac{2n}{d}+1)+\ln\frac4\delta}{n}}$.
- Borne Rademacher : $R(h)\le \hat R(h)+2\hat{\mathfrak R}_S(\mathcal H)+3\sqrt{\dfrac{\ln(2/\delta)}{2n}}$ — souvent la plus serrée.
- Ces bornes sont **valides mais lâches** : informatives sur les *tendances* (effet de $n$, de la capacité), rarement numériquement utiles telles quelles.

## En pratique

- Les bornes classiques (VC) sont **vacuous** pour les réseaux profonds (capacité immense, pourtant bonne généralisation) → recherche active : bornes PAC-Bayes, à marge, fondées sur les normes.
- En pratique on **mesure** le gap au lieu de le borner : écart train/test via [[Validation croisée]], courbes d'apprentissage.
- Valeur opérationnelle : justifie la [[Régularisation]] et l'[[Optimisation d'hyperparamètres]] (choisir la capacité qui minimise la borne empirique = le creux de la courbe en U).
- Outils : courbes d'apprentissage via [[Dev/Services/Scikit-Learn|sklearn.model_selection.learning_curve]].

## Approches voisines & alternatives

- [[PAC learning]] — le cadre qui définit ce que borner veut dire (ε, δ, complexité d'échantillon).
- [[VC dimension]] — terme de complexité pour classes binaires infinies.
- [[Rademacher complexity]] — terme data-dependent, bornes plus fines.
- [[Inégalités de concentration]] — la machinerie probabiliste qui produit ces bornes.
- [[Compromis biais-variance]] — la borne est la version quantifiée de ce compromis (empirique = biais+bruit, pénalité = variance).

## Pour aller plus loin

- Shalev-Shwartz & Ben-David — *Understanding Machine Learning*, ch. 4-6.
- Zhang et al. (2017) — *Understanding deep learning requires rethinking generalization* (pourquoi les bornes classiques échouent).
