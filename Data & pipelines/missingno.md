---
role: brique
nom: missingno
alias: [missing-no]
pitch: "Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas."
categorie: data/eda
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[ydata-profiling]]", "[[sweetviz]]"]
complements: []
tags: [missing-data, eda, static-viz]
url_docs: https://github.com/ResidentMario/missingno
url_repo: https://github.com/ResidentMario/missingno
---

# missingno

<!-- AUTO:BANDEAU:START -->
> Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont ancien · 2023-02-26 |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils dédiée à un seul problème : voir **où** et **comment** une donnée manque.
Quatre vues sur un DataFrame pandas — `matrix`, matrice de nullité dense qui fait ressortir
les motifs ligne à ligne ; `bar`, complétude par colonne ; `heatmap`, corrélation de nullité,
c'est-à-dire « quand cette colonne manque, une autre manque-t-elle aussi ? » ; `dendrogram`,
qui regroupe hiérarchiquement les colonnes par co-occurrence de manquants. C'est ce qui
sépare un manque aléatoire d'un manque **structuré**, et donc ce qui oriente le diagnostic
du mécanisme. L'outil décrit la nullité ; il ne la traite pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Inspecter visuellement où et comment une donnée manque, juste après le chargement | La `matrix` **échantillonne** au-delà d'un certain nombre de lignes : un motif partiel ne se lit pas comme exhaustif |
| Distinguer un manque aléatoire d'un manque structuré — colonnes qui manquent ensemble, piste MAR/MNAR | Une heatmap de nullité vide signifie le plus souvent des colonnes toujours pleines ou toujours vides — corrélation indéfinie, pas absence de motif |
| Décider d'une stratégie d'imputation sur la base de la structure observée | Très grand nombre de lignes ou de colonnes : la vue devient illisible, filtrer ou agréger en amont |
| Compléter un rapport de profiling par une lecture ciblée de la nullité | En mode maintenance : corrections acceptées, peu de nouvelles fonctionnalités à attendre — le périmètre est stable et suffisant |

## Mise en œuvre

- Installation — `uv add missingno`
- Point d'entrée — import Python, quatre fonctions sur un DataFrame pandas : `matrix`, `bar`, `heatmap`, `dendrogram`
- Prérequis — un DataFrame pandas ; matplotlib pour le rendu
- Exécution — CPU, single-node, en mémoire ; sortie graphique statique (PNG, SVG) ou rendu dans un notebook
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
- [[sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).

## Ressources

- Documentation — https://github.com/ResidentMario/missingno
- Dépôt — https://github.com/ResidentMario/missingno

## Voir aussi

- [[Mécanismes de données manquantes]] — le diagnostic que ces quatre vues instruisent
- [[Imputation des valeurs manquantes]] — la suite, une fois la structure comprise
- [[Comparatif - Outils EDA - profiling]] — ce qui départage les trois profileurs du dossier
