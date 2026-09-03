---
role: hub
nom: Analyse factorielle
alias: [analyse de données, analyse multivariée descriptive]
pitch: Résumer un grand tableau par quelques axes qu'on puisse interpréter — l'école française de l'analyse de données, et ses variantes selon le type de variables.
domaines: [data-sci]
tags: [factor-analysis, dimensionality-reduction, unsupervised, manifold, clustering, projection]
---

# Analyse factorielle

> Résumer un grand tableau par quelques axes qu'on puisse interpréter — l'école française de l'analyse de données, et ses variantes selon le type de variables.

## Ce qu'il faut comprendre

- **Le but est l'interprétation des axes, pas la performance d'un modèle en aval.** C'est ce qui sépare ce dossier de la réduction de dimension du ML — [[t-SNE and UMAP]], [[Manifold learning]], [[ICA]], [[NMF]], autoencodeurs —, qui cherche une représentation utile à une tâche et se juge sur elle. Ici on regarde le biplot et on nomme les axes. La frontière est réelle mais fine : les deux familles partagent le tag `dimensionality-reduction`, et elles sont désormais **rangées de part et d'autre** — [[umap-learn]] et les cinq pages ci-dessus vivent dans [[Non supervisé]], sous [[Machine Learning]].
- **La méthode se dérive du type de variables, elle ne se choisit pas.** [[Réduction de dimension]] porte l'arbre de décision complet, et c'est la page par laquelle entrer : tout quantitatif → [[PCA]] ; une table de contingence → [[CA]] ; plusieurs qualitatives → [[MCA]] ; un mélange des deux → [[FAMD]] ; des variables groupées en blocs → [[MFA]]. L'erreur classique est une PCA sur des codes catégoriels, qui produit des axes sans signification.
- **Toutes ces méthodes sont la même SVD sur un tableau différemment prétraité** — centrage, pondération, codage disjonctif, distance du khi-deux. Ce n'est pas une remarque d'esthète : c'est ce qui explique qu'elles se lisent toutes pareil (inertie par axe, éboulis, proximités sur le biplot) et qu'une seule bibliothèque les couvre toutes.
- **Deux branches sortent du tableau rectangulaire.** [[GPA]] superpose plusieurs configurations décrivant les mêmes individus ; [[PGA]] généralise la PCA aux données qui vivent sur une variété courbe (formes, matrices SPD, rotations) — et la géométrie y est **connue d'avance**, ce qui la garde ici. Quand la variété est au contraire *apprise* des données, on est de l'autre côté de la frontière : [[Manifold learning]] et ses méthodes (Isomap, LLE, Kernel PCA) sont dans [[Non supervisé]] depuis le lot 4 — elles déplient une variété pour en tirer des coordonnées réutilisables, elles ne nomment pas d'axes.
- **Le débouché naturel d'une projection est un clustering sur les composantes** : [[HCPC]] enchaîne méthode factorielle, classification ascendante hiérarchique et consolidation k-means. Projeter d'abord débruite — le bruit se concentre dans les derniers axes —, ce qui rend la classification plus stable que sur les variables brutes.

## Choisir

- Des axes latents à interpréter, sur des variables de tout type → [[Prince]], API scikit-learn sur DataFrames pandas.
- Une PCA seule dans un pipeline ML → [[Scikit-Learn]] suffit, ce dossier n'apporte rien de plus.
- [[Fanalysis]] → non : dépôt sans commit depuis juin 2018, resté en v0.0.1. Il est ici pour mémoire.
- La référence de l'école, si R est une option → `FactoMineR`, dont [[Prince]] reprend le périmètre.
- Visualiser un nuage en 2D pour l'œil, sans interpréter d'axes → [[umap-learn]] ou [[PaCMAP]], dans [[Machine Learning]].

<!-- AUTO:START -->
### Notions
- [[CA]] — domaines : data-sci
- [[FAMD]] — domaines : data-sci
- [[GPA]] — domaines : data-sci
- [[HCPC]] — domaines : data-sci
- [[MCA]] — domaines : data-sci
- [[MFA]] — domaines : data-sci
- [[PCA]] — domaines : data-sci
- [[PGA]] — domaines : data-sci
- [[Réduction de dimension]] — domaines : data-sci

### Briques
- [[Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.
- [[Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
<!-- AUTO:END -->
