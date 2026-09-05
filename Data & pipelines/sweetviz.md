---
role: brique
nom: sweetviz
alias: [Sweetviz]
pitch: "EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes)."
categorie: data/eda
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[ydata-profiling]]", "[[missingno]]"]
complements: []
tags: [eda, statistical-viz, dataframe]
url_docs: https://pypi.org/project/sweetviz/
url_repo: https://github.com/fbdesignpro/sweetviz
---

# sweetviz

<!-- AUTO:BANDEAU:START -->
> EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Profileur orienté **visuel et comparaison** : `sweetviz.analyze(df)` produit en une ligne un
rapport HTML auto-porté à forte densité graphique. Ce qui le distingue tient en deux objets —
une **variable cible**, autour de laquelle chaque feature est décrite selon son comportement
vis-à-vis d'elle, et la **comparaison de deux jeux** : `compare` pour train contre test,
`compare_intra` pour deux sous-populations d'un même jeu séparées par une condition
booléenne. C'est le seul du dossier à répondre « la distribution a-t-elle bougé ? ». Les
graphiques sont pré-rendus et intégrés au HTML, ce qui rend le rapport partageable tel quel.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analyser comment les features se rapportent à une cible, en classification ou en régression | La cible doit être typée explicitement (`FeatureConfig`, `target_feat`) : mal typée, elle fausse l'analyse d'association |
| Comparer train et test pour détecter un décalage de distribution avant modélisation | `pairwise_analysis` coûte cher en haute dimension — le passer à `"off"` au-delà de quelques dizaines de colonnes |
| Comparer deux sous-populations d'un même jeu (avant / après, deux segments) | Pensé pour du tabulaire de taille raisonnable, en mémoire : ce n'est pas un outil de qualité de données industriel |
| Obtenir un rapport visuel partageable, lisible d'un coup d'œil | |

## Mise en œuvre

- Installation — `uv add sweetviz`
- Point d'entrée — import Python : `analyze`, `compare`, `compare_intra`
- Prérequis — un DataFrame pandas tenant en mémoire ; matplotlib pour les graphiques pré-rendus
- Exécution — CPU, single-node ; sortie HTML autonome ou rendu dans un notebook
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
- [[missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.

## Ressources

- Documentation — https://pypi.org/project/sweetviz/
- Dépôt — https://github.com/fbdesignpro/sweetviz

## Voir aussi

- [[EDA automatisée & profiling]] — la notion du dossier, que cet outil incarne
- [[Comparatif - Outils EDA - profiling]] — ce qui départage les trois profileurs du dossier
