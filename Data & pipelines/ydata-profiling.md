---
role: brique
nom: ydata-profiling
alias: [pandas-profiling, ydata profiling]
pitch: "Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark."
categorie: data/eda
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[sweetviz]]", "[[missingno]]"]
complements: []
tags: [eda, data-quality, dataframe]
url_docs: https://docs.profiling.ydata.ai/
url_repo: https://github.com/ydataai/ydata-profiling
---

# ydata-profiling

<!-- AUTO:BANDEAU:START -->
> Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Profileur **exhaustif** : `ProfileReport(df)` génère en une ligne un rapport HTML complet
d'un jeu de données. Par variable — type inféré, distribution, quantiles, taux de manquants,
cardinalité, valeurs fréquentes — et entre variables — corrélations Pearson, Spearman et
Cramér's V, interactions, doublons — plus une section d'**alertes** automatiques :
constantes, forte cardinalité, manquants massifs, corrélations suspectes avec la cible. Le
prix de cette exhaustivité est en $O(p^2)$ : corrélations et interactions rendent le rapport
interminable sur un jeu large. Ex-`pandas-profiling`, renommé quand la v4 a ajouté le backend
Spark.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Première passe d'EDA juste après le chargement, avant tout nettoyage — un portrait complet sans écrire de code | Jeu large en pandas : les corrélations et interactions en $O(p^2)$ explosent — passer `minimal=True` ou échantillonner |
| Produire un rapport partageable, HTML auto-porté, pour une revue de qualité de données | L'ancien paquet `pandas-profiling` est gelé : installer `ydata-profiling` et importer `from ydata_profiling import ProfileReport` |
| Comparer deux jeux (`compare()`) ou profiler un DataFrame Spark sur du volume | Rapport générique : un point de départ, qui n'oriente pas les questions métier et ne remplace pas une viz ciblée |
| Repérer d'un coup d'œil constantes, quasi-identifiants, manquants structurés, corrélations suspectes avec la cible ([[Data leakage]]) | |

## Mise en œuvre

- Installation — `uv add ydata-profiling`
- Point d'entrée — import Python, `ProfileReport(df)` ; `compare()` pour deux jeux
- Prérequis — un DataFrame pandas, ou un DataFrame Spark pour le backend distribué (sous-ensemble de métriques)
- Exécution — single-node sur pandas, distribué via Spark ; sortie HTML autonome ou widget dans un notebook
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.

## Ressources

- Documentation — https://docs.profiling.ydata.ai/
- Dépôt — https://github.com/ydataai/ydata-profiling

## Voir aussi

- [[EDA automatisée & profiling]] — la notion du dossier, que cet outil incarne
- [[Comparatif - Outils EDA - profiling]] — ce qui départage les trois profileurs du dossier
