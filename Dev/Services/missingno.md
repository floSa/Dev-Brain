---
galaxie: dev
type: service
nom: missingno
alias: [missing-no]
pitch: "Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/ydata-profiling|ydata-profiling]]", "[[Dev/Services/sweetviz|sweetviz]]"]
remplace_par: []
status: actif
tags: [missing-data, eda, static-viz]
url_docs: https://github.com/ResidentMario/missingno
url_repo: https://github.com/ResidentMario/missingno
---

# missingno

## Pourquoi

Petite boîte à outils dédiée à **un seul problème** : visualiser les valeurs manquantes. Quatre vues complémentaires sur un DataFrame pandas — `matrix` (matrice de nullité dense, repère visuellement les motifs ligne à ligne), `bar` (complétude par colonne), `heatmap` (corrélation de nullité : quand une colonne manque, une autre manque-t-elle aussi ?) et `dendrogram` (regroupe hiérarchiquement les colonnes par co-occurrence de manquants). L'outil qui donne corps au diagnostic des [[Mécanismes de données manquantes|mécanismes de données manquantes]].

## Quand l'utiliser

- Inspecter visuellement **où** et **comment** une donnée manque, juste après le chargement.
- Distinguer un manque aléatoire d'un manque **structuré** (colonnes qui manquent ensemble → piste MAR/MNAR).
- Décider d'une stratégie d'[[Imputation des valeurs manquantes|imputation]] sur la base de la structure observée.
- Compléter un rapport de profiling par une lecture ciblée de la nullité.

## Quand NE PAS l'utiliser

- Profiling **complet** (distributions, corrélations, alertes qualité) → [[Dev/Services/ydata-profiling|ydata-profiling]].
- Analyse orientée **cible** ou comparaison de jeux → [[Dev/Services/sweetviz|sweetviz]].
- Très grand nombre de lignes/colonnes : la matrice échantillonne et devient illisible — filtrer ou agréger en amont.

## Déploiement & coût

- Bibliothèque Python (`uv add missingno`), gratuite (MIT). Rien à héberger.
- Single-node ; bâtie sur matplotlib, sortie graphique statique (PNG/SVG) ou rendu [[Notebooks-as-code|notebook]].
- En **mode maintenance** : corrections acceptées, peu de nouvelles fonctionnalités attendues — périmètre stable et suffisant.

## Pièges

- La `matrix` **échantillonne** au-delà d'un certain nombre de lignes : ne pas lire un motif partiel comme exhaustif.
- Couvre la nullité, pas son traitement : enchaîner vers [[Imputation des valeurs manquantes]] une fois la structure comprise.
- Une heatmap de nullité vide signifie souvent colonnes toujours pleines ou toujours vides (corrélation indéfinie), pas absence de motif.

## Alternatives

- [[Dev/Services/ydata-profiling|ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
- [[Dev/Services/sweetviz|sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).

## Liens

- Concept : [[Mécanismes de données manquantes]] — le diagnostic que cet outil visualise ; suivi de [[Imputation des valeurs manquantes]].
- [[Dev/Patterns/Comparatif - Outils EDA - profiling|Comparatif — Outils EDA / profiling]]
- Doc : https://github.com/ResidentMario/missingno
