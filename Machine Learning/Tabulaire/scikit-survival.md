---
role: brique
nom: scikit-survival
alias: [sksurv, scikit survival, survival analysis scikit-learn]
pitch: "Analyse de survie « machine learning » au-dessus de scikit-learn — Cox pénalisé, forêts de survie aléatoires, gradient boosting et SVM de survie, avec les métriques adaptées à la censure (indice de concordance, AUC dynamique, score de Brier) ; licence GPL-3.0."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[lifelines]]"]
complements: []
tags: [survival-analysis, rul, supervised, ensemble]
url_docs: https://scikit-survival.readthedocs.io/
url_repo: https://github.com/sebp/scikit-survival
---

# scikit-survival

<!-- AUTO:BANDEAU:START -->
> Analyse de survie « machine learning » au-dessus de scikit-learn — Cox pénalisé, forêts de survie aléatoires, gradient boosting et SVM de survie, avec les métriques adaptées à la censure (indice de concordance, AUC dynamique, score de Brier) ; licence GPL-3.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Module Python d'analyse de survie construit sur scikit-learn : le temps jusqu'à un événement,
dont une partie des observations reste **censurée** (l'unité n'a pas encore connu la panne).
Il apporte à la survie ce que scikit-learn apporte au reste : des estimateurs `fit` /
`predict`, qui se glissent dans un `Pipeline`, une validation croisée et une recherche
d'hyperparamètres. Le catalogue couvre le modèle de Cox (avec ou sans pénalisation
élastique), les arbres, forêts et arbres extra-aléatoires de survie, le gradient boosting
(dont une variante composante par composante), plusieurs SVM de survie, et les estimateurs
non paramétriques (Kaplan-Meier, Nelson-Aalen, risques concurrents). Il fournit aussi les
métriques qui supportent la censure : indice de concordance (sans ou avec pondération par la
probabilité de censure), AUC dépendante du temps, score de Brier et son intégrale.
La cible `y` est un tableau structuré (indicateur d'événement, durée), construit par `Surv`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Beaucoup de covariables (capteurs agrégés, features de fenêtre) et des relations non linéaires : forêts de survie, boosting | Peu de covariables et besoin d'**interpréter** des rapports de risque, de tester des hypothèses : [[lifelines]] (Cox, AFT, tests, diagnostics) |
| Évaluer une prédiction de panne **sous censure** : indice de concordance pondéré, AUC dynamique, score de Brier intégré | Un RUL en unités de temps comme sortie directe : la bibliothèque rend un score de risque ou une fonction de survie, la durée résiduelle s'en dérive — voir [[RUL par analyse de survie]] |
| Rester dans l'écosystème scikit-learn (`Pipeline`, `GridSearchCV`, `ColumnTransformer`) | Livrable **distribué** à un client : la licence est la **GPL-3.0**, copyleft fort — un produit qui l'embarque doit lui-même être publié sous GPL ; à faire valider avant tout livrable d'ESN. L'usage interne ne distribue rien |
| Comparer plusieurs familles de modèles de survie sur le même protocole de validation | Covariables qui varient dans le temps (capteur en trajectoire) : le format est durée plus événement par ligne, sans équivalent du format long de [[lifelines]] |
| | Séries brutes de capteurs : la bibliothèque attend une table de features, à fabriquer en amont (par exemple avec [[tsfresh]]) |

## Mise en œuvre

- Installation — `conda install -c conda-forge scikit-survival` (voie recommandée par le README) ; `uv add scikit-survival` depuis PyPI
- Point d'entrée — API Python : `from sksurv.ensemble import RandomSurvivalForest`, `from sksurv.util import Surv`
- Prérequis — Python 3.11 ou plus récent ; NumPy 2, pandas 2.2, scikit-learn 1.9, SciPy ; le README liste aussi un compilateur C/C++ (installation depuis les sources)
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit, GPL-3.0 ; aucune infrastructure

Version 0.28.0 publiée le 2026-07-05 ; dépôt actif (dernier push le 2026-10-01).

## Écosystème

### Alternatives

- [[lifelines]] — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.

## Ressources

- Documentation — https://scikit-survival.readthedocs.io/
- Dépôt — https://github.com/sebp/scikit-survival
- Papier — Pölsterl, *scikit-survival: A Library for Time-to-Event Analysis Built on Top of scikit-learn*, JMLR 21(212), 2020 : https://jmlr.org/papers/v21/20-729.html

## Voir aussi

- [[RUL par analyse de survie]] — la notion qui le cite pour la survie « machine learning » et l'évaluation sous censure
- [[Maintenance prédictive et RUL]] — le cadre du pronostic dans lequel la survie s'insère
- [[Analyse de survie]] — la notion mère : censure, Kaplan-Meier, Cox
- [[Tabulaire]] — le hub du dossier
- [[Random Forest]] · [[Gradient Boosting (GBDT)]] — les ensembles d'arbres dont il décline la version pour des durées censurées
- [[Scikit-Learn]] — l'API dont il reprend les conventions
