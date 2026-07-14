---
galaxie: wiki
type: concept
nom: A/B testing
alias: [AB testing, test A/B, split testing, online controlled experiment, OCE, randomized experiment]
categorie: concept/stats
domaines: [data-sci]
tags: [experimentation, ab-testing, hypothesis-testing]
---

# A/B testing

## Aperçu

- Expérience contrôlée : on répartit aléatoirement les unités (utilisateurs, sessions) entre une variante A (contrôle) et une variante B (traitement), puis on compare une métrique.
- La randomisation rend les deux groupes comparables en espérance → la différence observée s'interprète comme l'effet causal de la variante.
- Cas particulier d'un [[Tests d'hypothèse|test d'hypothèse]] appliqué à une décision produit.

## Concepts clés

### Randomisation
- L'affectation aléatoire neutralise les facteurs de confusion (connus et inconnus) : c'est ce qui distingue l'A/B test d'une simple comparaison observationnelle.
- Unité de randomisation = grain de l'affectation (utilisateur le plus souvent, pas la requête) ; doit correspondre à l'unité d'analyse sous peine de variance sous-estimée.

### OEC — métrique de décision
- Overall Evaluation Criterion : la métrique unique qui tranche. Choisie avant l'expérience, alignée sur la valeur long terme.
- Métriques de garde-fou (guardrails) : ne doivent pas se dégrader (latence, désabonnement…).

### Significativité et taille d'effet
- Une p-value sous α signale un effet peu compatible avec « aucune différence » ; elle ne dit rien de l'ampleur → toujours rapporter l'effet et son [[Intervalles de confiance|intervalle de confiance]].
- Effet minimal détectable (MDE) fixé d'avance via [[Analyse de puissance]].

### Pièges
- Peeking : regarder les résultats en continu et s'arrêter au premier seuil franchi gonfle l'erreur de type I → cf. [[Sequential testing]].
- Effets de réseau / interférence : l'unité A peut influencer l'unité B (réseaux sociaux, marketplaces) → la randomisation simple biaise alors l'estimation.

## Les maths, simplement

- Effet estimé (différence de moyennes) : $\hat{\Delta} = \bar{Y}_B - \bar{Y}_A$.
- Erreur standard (groupes indépendants) : $SE = \sqrt{\dfrac{s_A^2}{n_A} + \dfrac{s_B^2}{n_B}}$, statistique de test $z = \hat{\Delta}/SE$.
- Taille d'échantillon (deux proportions, puissance 0,8, α 0,05 bilatéral) : $n \approx \dfrac{16\,\bar{p}(1-\bar{p})}{\text{MDE}^2}$ par groupe — l'effet à détecter pilote tout.
- Réduire $SE$ sans plus de trafic : exploiter le pré-période (cf. [[CUPED]]).

## En pratique

- Figer OEC, MDE, α et la durée **avant** de lancer ; ne pas s'arrêter au premier pic (sauf design séquentiel prévu).
- Vérifier l'absence de Sample Ratio Mismatch (le ratio observé A/B doit coller à l'allocation visée — sinon biais d'instrumentation).
- Laisser tourner au moins un cycle hebdomadaire complet (effets jour/semaine, nouveauté).
- Plusieurs variantes ou métriques en parallèle → corriger la multiplicité (cf. [[Correction des tests multiples]]).
- Randomisation impossible (déploiement géographique, changement global) → se rabattre sur du quasi-expérimental comme [[Diff-in-Diff]].

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — le socle inférentiel ; l'A/B test en est l'application décisionnelle.
- [[Analyse de puissance]] — dimensionne l'expérience (MDE → n) ; [[Intervalles de confiance]] — chiffre l'ampleur de l'effet.
- [[CUPED]] — réduit la variance à trafic constant, donc raccourcit le test.
- [[Multi-armed bandits]] — allocation dynamique du trafic vers la variante gagnante, au lieu d'un split fixe.
- [[Sequential testing]] — évaluer en continu sans gonfler le faux positif.
- [[Diff-in-Diff]] — estimer un effet quand la randomisation n'est pas possible.

## Pour aller plus loin

- Réf : Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments* (2020).
- Outils : `statsmodels`, `scipy.stats` ; plateformes : GrowthBook, Eppo, Optimizely.
- Tag `experimentation` : famille des expériences en ligne (A/B, bandits, séquentiel).
