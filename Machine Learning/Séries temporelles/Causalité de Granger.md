---
role: notion
nom: Causalité de Granger
alias: [Granger, Granger causality, test de Granger, causalité au sens de Granger, grangercausalitytests]
categorie: ml/series-temporelles
domaines: [data-sci, ml-eng]
tags: [timeseries, causal-inference, hypothesis-testing]
---

# Causalité de Granger

## Aperçu

- Le test de Granger répond à la question : **le passé d'une série aide-t-il à prédire une autre série, au-delà de ce que son propre passé permet déjà ?** Si oui, on dit que la première « cause au sens de Granger » la seconde.
- **Ce n'est pas une preuve de cause.** Le mot « causalité » est trompeur : le test mesure un gain de **prédiction**, pas un effet que l'on obtiendrait en agissant. Deux séries peuvent s'entraîner l'une l'autre en apparence parce qu'une troisième les pilote toutes les deux.
- Exemple d'usine : la vibration d'une pompe A annonce, avec deux minutes d'avance, la hausse du courant d'un moteur B. Le test de Granger « A → B » sera positif. Cela ne dit pas que A abîme B : A et B peuvent suivre la même charge de ligne, A la ressentant simplement plus tôt.
- Où ça sert : trier des relations candidates entre capteurs avant une analyse de [[Cause racine d'une anomalie]], choisir des variables explicatives pour un modèle de prévision, ou repérer qu'un capteur en précède un autre.

## Concepts clés

### Le principe : deux régressions, une comparaison

- Première régression : prédire $y_t$ à partir de ses $p$ valeurs passées seulement. Seconde régression : ajouter les $p$ valeurs passées de $x$. Si la seconde prédit **significativement mieux**, $x$ Granger-cause $y$.
- Le sens est fixé par le temps : seule la cause **qui précède** peut prédire. Une corrélation instantanée (même instant) ne se teste pas.

### Ce qu'il faut régler : le nombre de retards

- Le résultat change avec $p$. Un retard trop court rate une influence lente ; trop long, il gaspille des degrés de liberté. En pratique on regarde plusieurs valeurs de $p$, et un critère d'information choisit l'ordre du modèle ([[ARIMA SARIMA]] pour la logique de l'ordre).

### Ce qui peut le piéger

- **Cause commune.** Un facteur caché, ou même observé mais absent du test, produit un faux positif. C'est le cas le plus fréquent dans une usine (charge, température ambiante, équipe).
- **Pas de temps trop grossier.** Si la mesure est moyennée à l'heure alors que l'effet dure quelques secondes, l'ordre temporel disparaît et le test se trompe de sens.
- **Séries non stationnaires.** Une tendance commune fabrique des liens apparents. Différencier, ou utiliser une version adaptée (Toda et Yamamoto, 1995, ajoutent des retards au modèle pour tolérer les racines unitaires). Voir [[Stationarity]].
- **Liens non linéaires.** Le test est linéaire ; un effet en seuil peut passer inaperçu.
- **Anticipation.** Une réaction déclenchée d'avance (l'opérateur baisse la consigne parce qu'il voit venir une montée de charge) précède l'événement qu'elle accompagne : le test lui attribue à tort le rôle de cause.
- **Beaucoup de couples.** Tester toutes les paires de 50 capteurs fait 2 450 tests ordonnés : sans [[Correction des tests multiples]], des faux positifs sont garantis.

## Les maths, simplement

- Modèle complet : $y_t=\sum_{k=1}^{p}a_k\,y_{t-k}+\sum_{k=1}^{p}b_k\,x_{t-k}+\varepsilon_t$. Hypothèse nulle : $b_1=\dots=b_p=0$. Test de Fisher sur le gain de somme des carrés des résidus.
- Avec `statsmodels`, `grangercausalitytests(data, maxlag)` prend un tableau à deux colonnes. La **deuxième colonne** est la cause supposée de la première : l'hypothèse nulle est « la série de la colonne 2 ne cause pas, au sens de Granger, celle de la colonne 1 ». La fonction rapporte quatre tests (`ssr_ftest`, `ssr_chi2test`, `lrtest`, `params_ftest`). La documentation lue ne parle pas de stationnarité : c'est à l'utilisateur de la vérifier.
- **Exemple exécuté** (simulation de cette page, graine 0, 2 000 points, `statsmodels` 0.15.0). Une charge commune $z$ autorégressive pilote deux capteurs : A la suit avec 1 pas de retard, B avec 2 pas. Aucun lien direct entre A et B.
  - Test « A cause B » : $p$ égal à 0,000 aux retards 1, 2 et 3 (F = 2 126 au retard 2). Test inverse « B cause A » : $p=0{,}14$ au retard 2 et $0{,}67$ au retard 3 (pour un retard 1, le test sort significatif aussi, car la charge a elle-même une mémoire).
  - Le test voit un faux lien **A → B**, parce que A reçoit la charge un pas avant B. Dans un VAR à retard 2 qui inclut aussi $z$, le test « A cause B » donne $p=0{,}27$ : le lien disparaît quand la cause commune est dans le modèle.

## En pratique

- **Lire le résultat comme « précède et prédit »**, jamais comme « provoque ». Pour établir une cause, il faut une intervention ou un cadre dédié : [[Inférence causale]], [[Découverte causale]].
- **Inclure les variables qui pourraient jouer le rôle de cause commune** (charge, régime, température ambiante) dans le modèle : c'est la version multivariée, qui réduit les faux positifs.
- **Vérifier la stationnarité d'abord** ([[Stationarity]], [[Autocorrelation]]).
- **Tester plusieurs retards et corriger les tests multiples** quand on explore beaucoup de paires.
- **Si la relation est non linéaire**, l'entropie de transfert est l'analogue sans modèle linéaire, fondé sur l'[[Mutual information]] conditionnelle ; elle est décrite avec ses limites dans [[Cause racine d'une anomalie]].

## Approches voisines & alternatives

- [[Cause racine d'une anomalie]] — où Granger sert à remonter une anomalie à sa source, avec l'entropie de transfert et les méthodes d'apprentissage profond.
- [[Inférence causale]] et [[Découverte causale]] — les cadres qui visent une cause, et non un gain de prédiction.
- [[Autocorrelation]] — la mémoire d'une série seule, que Granger retire avant de regarder l'autre.
- [[Time series anomaly detection]] — où des relations entre séries servent à détecter une rupture.
- [[statsmodels]] — la bibliothèque Python qui fournit `grangercausalitytests`.

## Pour aller plus loin

- Granger (1969), *Investigating Causal Relations by Econometric Models and Cross-spectral Methods*, Econometrica 37(3), 424-438 (référence reprise de [[Cause racine d'une anomalie]], texte non relu).
- Toda, Yamamoto (1995), *Statistical inference in vector autoregressions with possibly integrated processes*, Journal of Econometrics 66, 225-250 (référence confirmée par recherche, texte non relu).
- Eichler (2013), *Causal inference with multiple time series: principles and problems*, Philosophical Transactions of the Royal Society A 371 (référence confirmée par recherche, texte non relu) : sur les limites de Granger comme mesure de cause, « fortement discutée ».
- Documentation statsmodels, `grangercausalitytests` : https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.grangercausalitytests.html (lue)
