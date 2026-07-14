---
galaxie: dev
type: service
nom: ydata-profiling
alias: [pandas-profiling, ydata profiling]
pitch: "Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/sweetviz|sweetviz]]", "[[Dev/Services/missingno|missingno]]"]
remplace_par: []
status: actif
tags: [eda, data-quality, dataframe]
url_docs: https://docs.profiling.ydata.ai/
url_repo: https://github.com/ydataai/ydata-profiling
---

# ydata-profiling

## Pourquoi

Outil de référence de l'[[EDA automatisée & profiling|EDA automatisée]] : `ProfileReport(df)` génère en une ligne un rapport HTML exhaustif d'un jeu de données. Par variable (type inféré, distribution, quantiles, taux de manquants, cardinalité, valeurs fréquentes) et entre variables (corrélations Pearson/Spearman/Cramér's V, interactions, doublons), plus une section d'**alertes** automatiques (constantes, forte cardinalité, fort taux de manquants, corrélations suspectes). Ex-`pandas-profiling`, renommé pour refléter le support **Spark** (depuis la v4).

## Quand l'utiliser

- Première passe d'EDA juste après le chargement, avant tout nettoyage — un portrait complet sans écrire de code.
- Produire un rapport partageable (HTML auto-porté) pour un revue de qualité de données.
- Comparer deux jeux (`compare()`) ou profiler un DataFrame **Spark** sur du volume.
- Repérer d'un coup d'œil constantes, quasi-identifiants, manquants structurés, corrélations cible suspectes ([[Data leakage]]).

## Quand NE PAS l'utiliser

- Rapport centré sur une **cible** ou comparaison train/test plus lisible → [[Dev/Services/sweetviz|sweetviz]].
- Diagnostic ciblé des seules **valeurs manquantes** (matrice, dendrogramme de nullité) → [[Dev/Services/missingno|missingno]].
- Très gros jeu en pandas : les corrélations et interactions en $O(p^2)$ rendent le rapport interminable — échantillonner ou désactiver ces calculs (mode `minimal`).

## Déploiement & coût

- Bibliothèque Python (`uv add ydata-profiling`), gratuite (MIT). Rien à héberger.
- Single-node sur pandas ; backend **Spark** pour le distribué (sous-ensemble de métriques).
- Sortie : HTML autonome, ou widget dans un [[Notebooks-as-code|notebook]].

## Pièges

- Coûteux sur larges jeux : passer en `minimal=True` ou échantillonner, sinon corrélations/interactions explosent.
- L'ancien paquet `pandas-profiling` est gelé — installer `ydata-profiling` (import `from ydata_profiling import ProfileReport`).
- Rapport générique : un **point de départ**, il n'oriente pas les questions métier ni ne remplace une viz ciblée.

## Alternatives

- [[Dev/Services/sweetviz|sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[Dev/Services/missingno|missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.

## Liens

- Concept : [[EDA automatisée & profiling]] — la notion que cet outil incarne.
- [[Dev/Patterns/Comparatif - Outils EDA - profiling|Comparatif — Outils EDA / profiling]]
- Doc : https://docs.profiling.ydata.ai/
