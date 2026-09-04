---
role: comparatif
nom: Comparatif - Outils stats
categorie: stats/inference
tags: [hypothesis-testing, statistical-inference, bayesian, factor-analysis, causal-inference]
---

# Comparatif - Outils stats

> On tranche sur : l'étage — une fonction de test, un objet modèle avec ses diagnostics, ou un modèle bayésien qu'on écrit soi-même — puis sur la question posée : tester, factoriser, dater un effet, ou modéliser une durée.

![[Comparatif - Outils stats.base]]

## Ce qui départage

- [[scipy.stats]] — le **socle bas niveau**, déjà installé partout : une centaine de lois, les descriptives, les corrélations, la plupart des tests classiques, plus `bootstrap`, `permutation_test` et `monte_carlo_test`. API **par fonctions et non par modèles** — aucun état, aucun diagnostic, l'interprétation reste à la charge du lecteur — et pas de correction de tests multiples homogène.
- [[statsmodels]] — l'**objet modèle** avec son résumé annoté (coefficients, erreurs-types, p-values, IC, R², AIC/BIC) et sa batterie de tests de spécification, plus l'API formules à la R (`y ~ x1 + x2`). L'OLS **n'ajoute pas** la constante, l'API est double (`sm.OLS` contre `smf.ols`) et se mélange mal, et rien n'est homogène avec le `fit`/`predict` de scikit-learn.
- [[pingouin]] — les mêmes tests, mais chaque appel rend un DataFrame portant **p-value, taille d'effet, intervalle de confiance et puissance** d'un coup, ANOVA à mesures répétées, post-hoc et corrections compris. Son critère décisif n'est pas technique : **GPL-3.0**, copyleft, là où scipy et statsmodels sont en BSD — à vérifier avant intégration dans un produit fermé.
- [[lifelines]] — la seule **analyse de survie** : Kaplan-Meier, log-rank, régression de **Cox** à risques proportionnels et modèles paramétriques AFT, avec la **censure** traitée en première classe. Une censure mal encodée biaise tout, l'hypothèse des risques proportionnels se vérifie (résidus de Schoenfeld) sous peine de modèle faux, et ce n'est ni du gros volume ni du GPU.
- [[PyMC]] — la **programmation probabiliste** en Python pur : on décrit le modèle génératif dans un `with pm.Model()`, NUTS infère l'a posteriori. Backend historiquement mouvant (Theano → Aesara → PyTensor), divergences NUTS qui se traitent par **reparamétrage non centré** plutôt qu'en poussant `target_accept` à l'aveugle, et compilation du graphe au premier `sample`.
- [[Stan]] — le même travail, mais dans un **langage dédié compilé en C++** : le modèle devient un artefact `.stan` versionnable et réutilisable hors Python (R, Julia, ligne de commande), avec l'échantillonneur qui a popularisé NUTS. Coût de compilation à chaque modification, et toolchain C++ requise — source classique d'échecs d'installation en CI et sous Windows.
- [[ArviZ]] — le seul **indépendant du moteur** : il n'infère rien, il ingère la sortie de PyMC, Stan, NumPyro ou Pyro dans un `InferenceData` commun et rend les diagnostics ($\hat{R}$, ESS, énergie BFMI), les visualisations et la comparaison de modèles (LOO, WAIC). $\hat{R} \approx 1$ ne suffit pas à conclure — croiser avec ESS et divergences — et l'écosystème se modularise en `arviz-base` / `arviz-stats` / `arviz-plots`.
- [[CausalImpact]] — la seule question **causale datée** : l'effet d'une intervention ponctuelle, estimé par un **contrefactuel** BSTS bâti sur des séries de contrôle, avec son intervalle de crédibilité. Écosystème Python **fragmenté** — `tfcausalimpact` communautaire contre `tfp-causalimpact` de Google, API différentes —, hypothèse forte que les contrôles restent non affectés sur toute la période post, et sensibilité à la fenêtre pré-intervention.
- [[Prince]] — toute la famille **factorielle** sous une API scikit-learn : PCA, CA, MCA, FAMD, MFA, GPA, sur DataFrames indexés, testée contre FactoMineR. L'API a notablement évolué entre versions majeures, les visualisations Altair dépendent de l'environnement de rendu, et la décomposition reste en mémoire sur un seul nœud.
- [[Fanalysis]] — le même terrain réduit à PCA/CA/MCA, mais centré sur les **aides à l'interprétation** façon FactoMineR : contributions, cos², valeurs-tests, éboulis. **À l'arrêt en amont** — aucun commit depuis le 4 juin 2018, resté en v0.0.1 — avec le risque de friction que cela implique sur des NumPy/pandas récents, et une licence ambiguë entre README et PyPI.
