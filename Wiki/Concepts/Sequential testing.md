---
galaxie: wiki
type: concept
nom: Sequential testing
alias: [test séquentiel, analyse séquentielle, peeking, always-valid inference, SPRT, alpha spending]
categorie: concept/stats
domaines: [data-sci]
tags: [experimentation, sequential-analysis, hypothesis-testing]
---

# Sequential testing

## Aperçu

- Évaluer un test **en continu**, en regardant les données à mesure qu'elles arrivent, et décider de s'arrêter dès que la preuve est suffisante — sans gonfler l'erreur de type I.
- Répond au problème du *peeking* : un test à horizon fixe relu chaque jour avec un seuil à 5 % accumule les occasions de faux positif bien au-delà de 5 %.
- S'oppose au cadre « fixe » du [[A-B testing|test A/B]] classique, où la taille d'échantillon est figée d'avance.

## Concepts clés

### Le problème du peeking
- Tester un échantillon fixe au seuil α est valide **une seule fois**, à la fin. Le relire répété­ment et s'arrêter au premier franchissement multiplie les chances de rejeter H0 à tort.
- Avec des coups d'œil quotidiens, le taux de faux positif réel peut grimper à 20-30 % pour un α nominal de 5 %.

### SPRT — ratio de vraisemblance séquentiel
- Wald : on accumule le rapport de vraisemblance H1/H0 ; on continue tant qu'il reste entre deux bornes, on tranche dès qu'il en sort. Échantillon attendu minimal pour des risques α, β donnés.

### Group sequential & alpha spending
- On planifie K analyses intermédiaires et on « dépense » l'α total à chaque palier (O'Brien-Fleming : sévère au début, permissif à la fin ; Pocock : constant). L'α cumulé reste maîtrisé.

### Always-valid inference
- p-values et séquences de confiance valides **à tout instant d'arrêt** (mSPRT, confidence sequences). On peut regarder quand on veut, s'arrêter quand on veut : la garantie tient.

## Les maths, simplement

- SPRT : rapport $\Lambda_n = \prod_{i=1}^{n} \dfrac{f_1(x_i)}{f_0(x_i)}$ ; continuer tant que $B < \Lambda_n < A$, avec bornes $A \approx \tfrac{1-\beta}{\alpha}$, $B \approx \tfrac{\beta}{1-\alpha}$.
- Always-valid : une séquence de confiance $\{CI_n\}$ telle que $P\big(\exists n : \theta \notin CI_n\big) \le \alpha$ — couverture simultanée sur tout l'horizon, pas point par point.
- Prix à payer : ces bornes sont plus larges qu'un IC fixe à même n ; la flexibilité d'arrêt se paie en puissance.

## En pratique

- Choisir d'avance la méthode (alpha spending vs always-valid) et s'y tenir : improviser des coups d'œil sur un test fixe = p-hacking.
- Avantage : arrêter tôt un gagnant net (ou un perdant) → moins de trafic exposé, décisions plus rapides.
- Le peeking est une multiplicité **dans le temps** ; parente de la multiplicité **entre tests** traitée par [[Correction des tests multiples]].
- Beaucoup de plateformes d'expérimentation (Statsig, Eppo…) implémentent des p-values séquentielles par défaut.

## Approches voisines & alternatives

- [[A-B testing]] — le design fixe que le séquentiel assouplit ; ne jamais peeker un test fixe.
- [[Correction des tests multiples]] — même esprit (contrôler α malgré des regards multiples), mais entre hypothèses plutôt que dans le temps.
- [[Multi-armed bandits]] — autre réponse au « décider en continu », orientée allocation/gain plutôt que test d'hypothèse.
- [[Analyse de puissance]] — le séquentiel réduit l'échantillon **attendu**, pas le pire cas.

## Pour aller plus loin

- Réf : Wald — *Sequential Analysis* (1947) ; Johari, Pekelis, Walsh — *Always Valid Inference* (2017).
- Outils : `statsmodels` (group sequential partiel), bibliothèques de confidence sequences, plateformes d'A/B.
