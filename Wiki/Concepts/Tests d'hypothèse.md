---
galaxie: wiki
type: concept
nom: Tests d'hypothèse
alias: [hypothesis testing, test statistique, H0, significativité]
categorie: concept/stats
domaines: [data-sci]
tags: [statistical-inference, hypothesis-testing, p-value]
---

# Tests d'hypothèse

## Aperçu

- Démarche pour décider si un effet observé sur un échantillon est réel ou attribuable au seul hasard d'échantillonnage.
- Oppose une hypothèse nulle H0 (« pas d'effet ») à une alternative H1, puis mesure à quel point les données contredisent H0.
- Cadre commun à tous les tests concrets (cf. *Approches voisines*).

## Concepts clés

### H0 et H1
- H0 = statu quo (différence nulle, indépendance…). H1 = ce que l'on cherche à établir.
- On ne « prouve » jamais H0 : on la rejette, ou on échoue à la rejeter.

### Statistique de test et p-value
- Statistique de test = résumé numérique de l'écart à H0 (t, χ², F…).
- p-value = probabilité d'observer un écart au moins aussi extrême, si H0 est vraie.

### Seuil α et décision
- α = risque de rejeter H0 à tort (faux positif), fixé d'avance (souvent 0,05).
- p ≤ α → rejet de H0. Le seuil se fixe **avant** de voir les données.

### Erreurs de type I et II
- Type I (α) = faux positif. Type II (β) = faux négatif (rater un vrai effet).
- Puissance = 1 − β.

### Unilatéral vs bilatéral
- Bilatéral : « différent ». Unilatéral : « supérieur » (ou inférieur) — plus puissant, mais directionnel.

## Les maths, simplement

- p-value : $p = P(T \ge t_{obs} \mid H_0)$ — proba, sous H0, d'une statistique au moins aussi extrême que l'observée (bilatéral : on double / prend $|T|$).
- Décision : rejeter $H_0$ si $p \le \alpha$.
- Risques : $\alpha = P(\text{rejet} \mid H_0)$ (type I), $\beta = P(\text{non-rejet} \mid H_1)$ (type II).
- Piège d'interprétation : la p-value n'est **pas** $P(H_0 \mid \text{données})$ — c'est le conditionnement inverse.

## En pratique

- Fixer α et la direction du test **avant** de regarder les données (sinon p-hacking).
- Choisir le test selon les données : moyennes → [[Test t et ANOVA]] ; catégories → [[Test du khi-deux]] ; pas de normalité → [[Tests non paramétriques]].
- Une p-value significative ne dit rien de l'ampleur : toujours rapporter une taille d'effet et un [[Intervalles de confiance|intervalle de confiance]].
- Échantillon énorme → presque tout devient « significatif » ; minuscule → presque rien. Significativité ≠ importance.
- Plusieurs tests d'un coup → faux positifs gonflés (cf. [[Correction des tests multiples]]).

## Approches voisines & alternatives

- [[Intervalles de confiance]] — vue duale : un IC à 95 % contient les valeurs non rejetées au seuil 5 %.
- [[Test t et ANOVA]], [[Test du khi-deux]], [[Tests non paramétriques]] — tests concrets selon le type de données.
- [[Analyse de puissance]] — dimensionner avant de tester ; [[Correction des tests multiples]] — quand on en lance plusieurs.
- [[Bootstrap]] — inférence par rééchantillonnage quand la formule analytique manque.
- [[Théorème central limite]] — fonde la normalité asymptotique des statistiques de test (t, z).
- [[A-B testing|A/B testing]] — application décisionnelle directe : trancher entre deux variantes produit.
- [[Inférence bayésienne]] — raisonne sur $P(H \mid \text{données})$ via un a priori ; alternative au cadre fréquentiste ci-dessus.

## Pour aller plus loin

- Outils : `scipy.stats`, `statsmodels`, `pingouin` (Python).
- Tag-ombrelle `statistical-inference` : sujet « Inférence statistique » à créer un jour comme parent commun.
