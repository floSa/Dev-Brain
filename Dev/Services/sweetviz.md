---
galaxie: dev
type: service
nom: sweetviz
alias: [Sweetviz]
pitch: "EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes)."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/ydata-profiling|ydata-profiling]]", "[[Dev/Services/missingno|missingno]]"]
remplace_par: []
status: actif
tags: [eda, statistical-viz, dataframe]
url_docs: https://pypi.org/project/sweetviz/
url_repo: https://github.com/fbdesignpro/sweetviz
---

# sweetviz

## Pourquoi

Bibliothèque d'[[EDA automatisée & profiling|EDA automatisée]] orientée **visuel et comparaison**. En une ligne, `sweetviz.analyze(df)` produit un rapport HTML auto-porté à forte densité graphique. Sa différence : il est construit autour d'une **variable cible** (comment chaque feature se comporte selon la cible) et de la **comparaison de deux jeux** — train vs test (`compare`), ou deux sous-groupes d'un même jeu (`compare_intra`, séparés par une condition booléenne).

## Quand l'utiliser

- Analyser comment les features se rapportent à une **cible** (classification ou régression).
- Comparer **train vs test** pour détecter un décalage de distribution avant modélisation.
- Comparer deux sous-populations (hommes/femmes, avant/après) d'un même jeu.
- Obtenir un rapport visuel partageable, plus « lisible d'un coup d'œil » qu'un dump exhaustif.

## Quand NE PAS l'utiliser

- Rapport de **profiling exhaustif** (toutes les statistiques, alertes qualité, support Spark) → [[Dev/Services/ydata-profiling|ydata-profiling]].
- Diagnostic ciblé des seules **valeurs manquantes** → [[Dev/Services/missingno|missingno]].
- Très haute dimension (centaines de colonnes) : le rapport devient lourd ; désactiver l'analyse par paires (`pairwise_analysis="off"`).

## Déploiement & coût

- Bibliothèque Python (`uv add sweetviz`), gratuite (MIT). Rien à héberger.
- Single-node, en mémoire (pandas). Sortie HTML autonome ou rendu dans un [[Notebooks-as-code|notebook]].
- S'appuie sur matplotlib pour les graphiques pré-rendus intégrés au HTML.

## Pièges

- Préciser le **type de la cible** (`FeatureConfig` / `target_feat`) : une cible mal typée fausse l'analyse d'association.
- `pairwise_analysis` est coûteux en haute dimension — le passer à `"off"` au-delà de quelques dizaines de colonnes.
- Pensé pour des jeux **tabulaires de taille raisonnable** ; pas un outil de qualité de données industriel.

## Alternatives

- [[Dev/Services/ydata-profiling|ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
- [[Dev/Services/missingno|missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.

## Liens

- Concept : [[EDA automatisée & profiling]] — la notion que cet outil incarne.
- [[Dev/Patterns/Comparatif - Outils EDA - profiling|Comparatif — Outils EDA / profiling]]
- Doc : https://github.com/fbdesignpro/sweetviz
