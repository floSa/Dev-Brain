---
galaxie: wiki
type: concept
nom: PAC learning
alias: [Apprentissage PAC, Probably Approximately Correct, PAC, PAC learnability, apprenabilité PAC]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [learning-theory, pac-learning]
---

# PAC learning

## Aperçu

- Cadre formel (Valiant, 1984) qui définit ce que « apprendre » veut dire : à partir d'un échantillon fini, sortir une hypothèse **probablement** ($1-\delta$) **approximativement correcte** ($\le \varepsilon$ d'erreur).
- Fournit la notion de **complexité d'échantillon** : combien d'exemples faut-il pour garantir cette qualité ? C'est le socle théorique des [[Generalization bounds]].

## Concepts clés

### Le contrat PAC : (ε, δ)
- $\varepsilon$ = tolérance d'erreur (à quel point l'hypothèse peut se tromper), $\delta$ = risque d'échec (probabilité que la garantie ne tienne pas, à cause d'un échantillon malchanceux).
- Une classe $\mathcal H$ est **PAC-apprenable** s'il existe un algorithme qui, pour tout $\varepsilon,\delta$, atteint $\mathbb P(\text{erreur} \le \varepsilon)\ge 1-\delta$ avec un nombre d'exemples polynomial en $1/\varepsilon$ et $1/\delta$.

### Réalisable vs agnostique
- **Réalisable** : on suppose qu'une hypothèse parfaite ($0$ erreur) existe dans $\mathcal H$. Cas idéal, borne plus serrée.
- **Agnostique** : aucune hypothèse n'est parfaite ; on vise seulement à s'approcher de la **meilleure** de $\mathcal H$. C'est le cadre réaliste, qui se relie au [[Compromis biais-variance]] (la « meilleure de $\mathcal H$ » porte un biais d'approximation).

### Complexité d'échantillon et capacité
- Le nombre d'exemples requis croît avec la **capacité** de $\mathcal H$, mesurée par la [[VC dimension]] (cas binaire) ou la [[Rademacher complexity]] (cas réel, data-dependent). Plus la classe est riche, plus il faut de données pour la contraindre.

## Les maths, simplement

- Cas fini réalisable : $m \ge \dfrac{1}{\varepsilon}\big(\ln|\mathcal H| + \ln\tfrac{1}{\delta}\big)$ exemples suffisent. La taille de la classe entre en **logarithme** — doubler $|\mathcal H|$ coûte presque rien.
- Cas agnostique (Hoeffding + borne d'union) : $m \ge \dfrac{1}{2\varepsilon^2}\big(\ln|\mathcal H| + \ln\tfrac{2}{\delta}\big)$ — la dépendance passe en $1/\varepsilon^2$ car on borne un écart, pas une probabilité d'erreur exacte (cf. [[Inégalités de concentration]]).
- Pour une classe infinie, on remplace $\ln|\mathcal H|$ par un terme en [[VC dimension|dimension VC]] $d$.

## En pratique

- Le PAC dit *combien* de données et *quelle* garantie, pas *comment* optimiser : c'est un cadre d'analyse, pas un algorithme.
- Les bornes PAC sont souvent **pessimistes** (pire cas, distribution-libre) : utiles pour comparer des classes d'hypothèses, rarement pour dimensionner un dataset réel.
- Lien direct à la [[Validation croisée]] : le PAC formalise pourquoi l'erreur empirique sous-estime l'erreur vraie, ce que la validation croisée mesure empiriquement.

## Approches voisines & alternatives

- [[VC dimension]] — la mesure de capacité qui rend le PAC opérationnel pour les classes infinies.
- [[Rademacher complexity]] — alternative dépendante des données, bornes plus fines que la VC.
- [[Generalization bounds]] — les inégalités concrètes que le cadre PAC produit.
- [[No Free Lunch theorem]] — la limite : sans restreindre $\mathcal H$ (a priori), aucune apprenabilité PAC universelle.
- [[Compromis biais-variance]] — le PAC agnostique formalise le versant variance ; le choix de $\mathcal H$ fixe le biais.

## Pour aller plus loin

- Valiant (1984) — *A Theory of the Learnable*.
- Shalev-Shwartz & Ben-David — *Understanding Machine Learning*, ch. 2-4 (cadre PAC réalisable et agnostique).
