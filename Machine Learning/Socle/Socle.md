---
role: hub
nom: Socle
alias: [Socle ML, Socle généraliste]
pitch: Cadrer le problème avant de choisir l'algorithme, puis la boîte classique qui le résout — celle qui ne suppose rien de la nature des données.
domaines: [data-sci, ml-eng]
tags: [supervised, classification, regression, linear-model, ml-pipeline]
---

# Socle

> Cadrer le problème avant de choisir l'algorithme, puis la boîte classique qui le résout — celle qui ne suppose rien de la nature des données.

## Ce qu'il faut comprendre

- **Ce dossier est celui qu'on lit en premier, et le seul qui ne suppose rien de la donnée.** Les huit autres sous-dossiers du domaine se définissent par une entrée — une image, du texte, une série, des colonnes — ou par un moment du cycle de vie — servir, suivre, expliquer. Ici, rien de tel : ce sont les régimes d'apprentissage, les formes de problème et les modèles qui marchent partout. C'est aussi ce qui range [[Scikit-Learn]] à côté d'eux plutôt qu'ailleurs.
- **Le premier choix n'est pas l'algorithme, c'est le cadrage**, et c'est là que les projets se perdent. [[Types de données et choix de modèle]] pose les questions dans l'ordre : quelle est la cible, à quelle granularité, avec quelles données disponibles *au moment de la prédiction*. [[Apprentissage supervisé]] dit ce que change le fait d'avoir une cible annotée ; sans elle, on est dans [[Non supervisé]] et la preuve change de nature.
- **Trois formes de problème, pas trois familles d'algorithmes.** [[Classification]] quand la cible est catégorielle, [[Régression]] quand elle est continue, [[Régression et classification multi-sorties]] quand il y en a plusieurs à la fois. [[Systèmes de recommandation]] est la quatrième et la plus déguisée : elle ressemble à une prédiction, elle se juge comme un ordre — cf. [[Ranking metrics]] dans [[Évaluation de modèles]]. Un cadrage faux ne se rattrape par aucun modèle.
- **Les modèles simples ne sont pas des modèles pauvres.** [[Régression linéaire]] et [[Régression logistique]] sont la référence de comparaison obligatoire — un modèle plus complexe qui ne les bat pas ne se justifie pas. [[GLM]] les étend aux lois non gaussiennes (comptages, durées, proportions), [[GAM]] à la non-linéarité qui reste lisible, [[Régression quantile]] à la prédiction d'un intervalle plutôt que d'une moyenne. [[Régularisation]] est ce qui les rend utilisables en grande dimension, et c'est le réglage le plus rentable de la famille.
- **Le reste de la boîte classique se choisit sur une hypothèse, pas sur un classement.** [[Naive Bayes]] suppose l'indépendance conditionnelle et gagne son pari en très grande dimension ; [[k-NN]] ne suppose rien mais repousse tout le coût à la prédiction ; [[Analyse discriminante]] suppose la normalité par classe ; [[SVM]] cherche la marge maximale et passe au non linéaire par le noyau ; [[Gaussian Process]] est le seul à rendre nativement son incertitude — il sait qu'il ne sait pas ; [[Perceptron et MLP]] est l'origine des réseaux, et la porte vers [[Apprentissage profond]].
- **Sur des colonnes, ce dossier n'est pas le dernier mot** : le gradient boosting bat ces modèles-là sur données hétérogènes, et il est rangé dans [[Tabulaire]] avec la préparation des variables. Le partage est net — ici ce qui vaut quelle que soit la donnée, là ce qui suppose des colonnes.

## Choisir

- Ne pas savoir par où commencer → [[Types de données et choix de modèle]], puis [[Scikit-Learn]].
- Une baseline honnête à battre, quelle que soit la suite → [[Régression linéaire]] ou [[Régression logistique]].
- Une cible qui n'est ni gaussienne ni bornée comme la logistique le suppose → [[GLM]].
- De la non-linéarité qu'il faut pouvoir montrer et défendre → [[GAM]].
- Un intervalle plutôt qu'une valeur → [[Régression quantile]], ou [[Gaussian Process]] si l'incertitude doit être calibrée par construction.
- Beaucoup de variables pour peu de lignes → [[Régularisation]], Lasso pour trancher, Ridge pour amortir.
- Du texte en sac de mots, ou un premier tri quasi gratuit → [[Naive Bayes]].
- Peu de données, une frontière tordue, pas de contrainte de latence → [[SVM]].
- Apprendre en flux, sur une donnée qui n'entre pas en mémoire → [[River]].
- Des colonnes et une cible, une fois la baseline posée → [[Tabulaire]].
- Un réseau de neurones → [[Apprentissage profond]].

<!-- AUTO:START -->
### Notions
- [[Analyse discriminante]] — domaines : data-sci, ml-eng
- [[Apprentissage supervisé]] — domaines : data-sci, ml-eng
- [[Classification]] — domaines : data-sci, ml-eng
- [[GAM]] — domaines : data-sci, ml-eng
- [[Gaussian Process]] — domaines : data-sci, ml-eng
- [[GLM]] — domaines : data-sci, ml-eng
- [[k-NN]] — domaines : data-sci, ml-eng
- [[Naive Bayes]] — domaines : data-sci, ml-eng
- [[Perceptron et MLP]] — domaines : data-sci, ml-eng
- [[Régression]] — domaines : data-sci, ml-eng
- [[Régression et classification multi-sorties]] — domaines : data-sci
- [[Régression linéaire]] — domaines : data-sci, ml-eng
- [[Régression logistique]] — domaines : data-sci, ml-eng
- [[Régression quantile]] — domaines : data-sci, ml-eng
- [[Régularisation]] — domaines : data-sci, ml-eng
- [[SVM]] — domaines : data-sci, ml-eng
- [[Systèmes de recommandation]] — domaines : data-sci, ml-eng
- [[Types de données et choix de modèle]] — domaines : data-sci, ml-eng

### Briques
- [[River]] — ML en ligne / streaming en Python — apprentissage incrémental échantillon par échantillon (learn_one/predict_one) couvrant classification, régression, clustering, détection d'anomalies et de dérive ; issu de la fusion creme + scikit-multiflow.
- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
<!-- AUTO:END -->

## Notes
