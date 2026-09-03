---
role: hub
nom: Statistiques & inférence
alias: [stats, inférence statistique]
pitch: Généraliser d'un échantillon à une population, et mesurer ce que cette généralisation vaut — tests, estimation, inférence causale.
domaines: [data-sci]
tags: [statistical-inference, bayesian, causal-inference, factor-analysis]
---

# Statistiques & inférence

> Généraliser d'un échantillon à une population, et mesurer ce que cette généralisation vaut — tests, estimation, inférence causale.

## Ce qu'il faut comprendre

- **Les quatre sous-dossiers rangent des pages, ils ne découpent pas la statistique** — et le critère est la `categorie:` de la page, pas la matière dont elle traite. Ce que chacun est réellement : [[Tests & estimation]] ce qu'on conclut d'un échantillon **déjà collecté** — tests, intervalles, estimation ponctuelle, survie ; [[Bayésien]] ce qui répond par une **distribution** plutôt que par un point ; [[Analyse factorielle]] ce qui résume un tableau par des **axes qu'on interprète** ; [[Probabilités]] les **théorèmes et processus** qui rendent tout le reste légitime, et qui ne touchent aucune donnée. Ce qui reste au niveau du domaine est ce qui n'entre dans aucun des quatre : concevoir une expérience ([[A-B testing]], [[CUPED]], [[Sequential testing]], [[Multi-armed bandits]]) et estimer un effet causal sans randomisation ([[Inférence causale]], [[Diff-in-Diff]], [[CausalImpact]]).
- **Concevoir la collecte et analyser la collecte sont deux métiers.** Un test A/B se dimensionne avant ([[Analyse de puissance]]), se protège du *peeking* pendant ([[Sequential testing]]), se rend plus sensible par une covariable de pré-période ([[CUPED]]) — et seulement ensuite se lit comme un [[Tests d'hypothèse|test d'hypothèse]] ordinaire. Les erreurs coûteuses sont presque toutes en amont du calcul.
- Ce domaine n'est pas du machine learning à petite échelle. Le ML prédit et se juge sur des données non vues ; la statistique **estime un paramètre et quantifie son incertitude**, et se juge sur la validité de ses hypothèses. Les deux se recouvrent sur les modèles linéaires et divergent partout ailleurs — c'est pourquoi [[statsmodels]] et [[Scikit-Learn]] ajustent la même régression et n'affichent pas la même chose.
- Deux écoles se partagent le domaine, et le choix de l'outil suit ce clivage plus que le besoin métier. Le **fréquentiste** répond par une p-value et un [[Intervalles de confiance|intervalle de confiance]] ([[scipy.stats]], [[statsmodels]], [[pingouin]]) ; le **bayésien** répond par une distribution a posteriori ([[PyMC]], [[Stan]]), au prix d'un a priori à assumer et d'un échantillonnage à faire converger. Cf. [[Inférence bayésienne]] et [[Tests d'hypothèse]].
- En bayésien, le moteur et le **diagnostic** sont deux briques distinctes, et la seconde n'est pas optionnelle : un [[MCMC]] qui n'a pas convergé produit des chiffres d'apparence normale. [[ArviZ]] est indépendant du moteur et se branche aussi bien sur [[PyMC]] que sur [[Stan]] — c'est le complément par défaut des deux.
- Le troisième clivage est le **niveau d'API**. [[scipy.stats]] donne les lois et les tests bruts, à assembler soi-même. [[statsmodels]] et [[pingouin]] donnent des modèles et des tables de résultats prêtes à lire. Descendre d'un niveau se paie en code, monter d'un niveau se paie en hypothèses implicites.
- L'[[Analyse factorielle]] ([[Prince]]) est une tradition française à part, distincte de la réduction de dimension du ML ([[t-SNE and UMAP]], [[ICA]], [[NMF]]) : elle vise l'interprétation des axes, pas la performance d'un modèle en aval. [[PCA]], [[CA]], [[MCA]], [[FAMD]] sont ses variantes selon la nature des variables, et [[Réduction de dimension]] porte l'arbre de décision qui les départage.
- Deux familles de questions ont leur outil dédié parce que la censure et la confusion ne se traitent pas par un test ordinaire : l'[[Analyse de survie]] ([[lifelines]]) et l'[[Inférence causale]] ([[CausalImpact]]).

## Choisir

- Une loi, un test brut, une brique dans son propre code → [[scipy.stats]].
- Un modèle statistique et sa table de résultats, façon R → [[statsmodels]].
- Quelques tests à lire vite, tailles d'effet incluses → [[pingouin]].
- Un modèle bayésien à écrire en Python, dans un pipeline Python → [[PyMC]].
- Un modèle bayésien difficile, ou une équipe déjà sur le langage Stan → [[Stan]].
- Diagnostiquer et comparer des a posteriori, quel que soit le moteur → [[ArviZ]].
- Un temps jusqu'à un événement, avec des observations censurées → [[lifelines]].
- L'effet d'une intervention datée sur une série, sans groupe témoin randomisé → [[CausalImpact]].
- Des axes latents à interpréter sur des variables mixtes → [[Prince]] (et non [[Fanalysis]], abandonné depuis 2018). Cf. [[Analyse factorielle]].
- Savoir combien de lignes collecter avant de lancer une expérience → [[Analyse de puissance]].
- Comprendre pourquoi un intervalle de confiance a le droit d'exister → [[Probabilités]].
- Prédire plutôt qu'estimer → [[Machine Learning]], pas ce domaine.

<!-- AUTO:START -->
### Sous-domaines
- [[Analyse factorielle]] · [[Bayésien]] · [[Probabilités]] · [[Tests & estimation]]

### Notions
- [[A-B testing|A/B testing]] — domaines : data-sci
- [[CUPED]] — domaines : data-sci
- [[Diff-in-Diff]] — domaines : data-sci
- [[Inférence causale]] — domaines : data-sci
- [[Multi-armed bandits]] — domaines : data-sci
- [[Sequential testing]] — domaines : data-sci

### Briques
- [[CausalImpact]] — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.

### Comparatifs
- [[Comparatif - Outils stats]]
<!-- AUTO:END -->
