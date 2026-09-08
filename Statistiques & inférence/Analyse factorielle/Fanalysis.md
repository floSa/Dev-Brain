---
role: brique
nom: Fanalysis
alias: [fanalysis]
pitch: "Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince."
categorie: stats/exploratoire
famille: paquet
licence_type: open-source
maturite: deprecated
langage: Python
alternatives: ["[[Prince]]"]
complements: []
tags: [dimensionality-reduction, factor-analysis, unsupervised]
url_docs: 
url_repo: https://github.com/OlivierGarciaDev/fanalysis
---

# Fanalysis

<!-- AUTO:BANDEAU:START -->
> Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | deprecated | amont ancien · 2018-06-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Module d'analyse factorielle descriptive — PCA, CA, MCA — centré sur les **aides à
l'interprétation** dans l'esprit du package R FactoMineR : contributions, cos²,
valeurs-tests, éboulis et plans factoriels prêts à lire. Double usage, exploration
descriptive ou étape de réduction dans un pipeline scikit-learn, et ses sorties ont été
validées contre FactoMineR. Le point qui commande tout le reste est l'état du projet :
**aucun commit depuis le 4 juin 2018**, resté en v0.0.1. Le code fonctionne, mais rien
n'évoluera.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Retrouver en Python le confort d'interprétation de FactoMineR sur PCA, CA et MCA — tableaux d'aides, valeurs-tests | Projet **à l'arrêt en amont** : v0.0.1, aucun commit depuis juin 2018, donc friction probable avec les NumPy et pandas récents |
| Enseignement et analyse exploratoire descriptive, où la lecture des axes prime | Périmètre limité à PCA, CA et MCA : ni FAMD, ni MFA, ni GPA |
| | Licence affichée de façon **incohérente** — BSD-3-Clause au README, MIT aux classifieurs PyPI : à trancher avant tout usage contraint |

## Mise en œuvre

- Installation — `pip install fanalysis` (pas de publication récente sur PyPI)
- Point d'entrée — import Python, estimateurs à API scikit-learn
- Prérequis — NumPy, pandas et matplotlib
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit ; licence ambiguë entre README (BSD-3-Clause) et PyPI (MIT)

## Écosystème

### Alternatives

- [[Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.

## Ressources

- Dépôt — https://github.com/OlivierGarciaDev/fanalysis

## Voir aussi

- [[PCA]] · [[MCA]] · [[CA]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
- [[Comparatif - Réduction de dimension]] — analyse factorielle face à la PCA et aux méthodes manifold
