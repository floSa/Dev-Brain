---
galaxie: wiki
type: concept
nom: VC dimension
alias: [Dimension VC, Vapnik-Chervonenkis dimension, dimension de Vapnik-Chervonenkis, VC dim, shattering]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [learning-theory, vc-dimension]
---

# VC dimension

## Aperçu

- Mesure la **capacité** (richesse) d'une classe d'hypothèses binaires : le plus grand nombre de points qu'elle peut classer de **toutes** les façons possibles.
- C'est l'ingrédient qui rend le [[PAC learning]] opérationnel sur des classes infinies : elle remplace $\ln|\mathcal H|$ dans les [[Generalization bounds]].

## Concepts clés

### Shattering (pulvérisation)
- Un ensemble de $n$ points est **shattered** par $\mathcal H$ si, pour chacun des $2^n$ étiquetages binaires possibles, il existe une hypothèse de $\mathcal H$ qui le réalise.
- La **dimension VC** $d_{VC}$ est le plus grand $n$ tel qu'il existe **au moins un** ensemble de $n$ points shattered. Il suffit d'un seul ensemble qui marche (∃), mais il faut que *tous* les étiquetages soient atteints (∀).

### Exemples qui ancrent l'intuition
- Seuils sur $\mathbb R$ : $d_{VC}=1$. Intervalles : $d_{VC}=2$.
- Séparateurs linéaires (perceptron) en dimension $p$ : $d_{VC}=p+1$.
- Plus $\mathcal H$ est flexible, plus $d_{VC}$ est grande — donc plus elle risque de surapprendre.

### Capacité = variance
- Une grande $d_{VC}$ signifie que $\mathcal H$ peut coller à n'importe quel jeu de données, y compris au bruit : c'est le versant **variance** du [[Compromis biais-variance]]. Une petite $d_{VC}$ bride l'expressivité (biais) mais généralise mieux.

## Les maths, simplement

- **Lemme de Sauer-Shelah** : si $d_{VC}=d$, le nombre d'étiquetages distincts sur $n$ points est borné par $O(n^d)$ — une croissance **polynomiale**, pas exponentielle dès que $n>d$. C'est ce passage de $2^n$ à $n^d$ qui rend la généralisation possible.
- **Borne VC** (agnostique) : avec probabilité $1-\delta$,
- $R(h) \le \hat R(h) + \sqrt{\dfrac{d\,(\ln\frac{2n}{d}+1) + \ln\frac{4}{\delta}}{n}}$ — l'écart train/test décroît en $\sqrt{d/n}$.
- Conséquence : il faut $n \gg d$ exemples pour que la borne soit utile.

## En pratique

- La VC est **distribution-libre** (pire cas sur toutes les distributions) → bornes souvent trop lâches pour dimensionner un dataset réel ; la [[Rademacher complexity]] (dépendante des données) les resserre.
- Difficile à calculer exactement hors cas scolaires ; pour les réseaux profonds elle est énorme voire infinie, ce qui explique pourquoi la VC seule n'explique pas leur généralisation.
- Valeur pratique : **comparer** la capacité de familles de modèles et justifier la [[Régularisation]] (réduire la capacité effective) et la sélection via [[Validation croisée]].

## Approches voisines & alternatives

- [[PAC learning]] — le cadre que la VC dimension rend applicable aux classes infinies.
- [[Rademacher complexity]] — mesure de capacité dépendante des données, généralise la VC au cas réel.
- [[Generalization bounds]] — où la VC s'injecte comme terme de pénalité de complexité.
- [[Compromis biais-variance]] — capacité élevée ↔ variance ; la VC en est la quantification formelle.
- [[No Free Lunch theorem]] — pourquoi restreindre la capacité (donc $d_{VC}$) est nécessaire pour apprendre.

## Pour aller plus loin

- Vapnik & Chervonenkis (1971) — *On the Uniform Convergence of Relative Frequencies of Events*.
- Vapnik — *The Nature of Statistical Learning Theory*. ESL ch. 7.9 (VC dimension et complexité de modèle).
