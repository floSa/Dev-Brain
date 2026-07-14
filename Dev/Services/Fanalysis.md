---
galaxie: dev
type: service
nom: Fanalysis
alias: [fanalysis]
pitch: "Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: experimental
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Prince|Prince]]"]
remplace_par: []
status: actif
tags: [dimensionality-reduction, factor-analysis, unsupervised]
url_docs: 
url_repo: https://github.com/OlivierGarciaDev/fanalysis
---

# Fanalysis

## Pourquoi

Module d'**analyse factorielle descriptive** (PCA, CA, MCA) centré sur les **aides à l'interprétation** dans l'esprit du package R FactoMineR : contributions, cos², valeurs-tests, graphiques d'éboulis et plans factoriels prêts à lire. Double usage : exploration descriptive *et* étape de réduction dans un pipeline scikit-learn. Validé en comparant ses sorties à celles de FactoMineR.

## Quand l'utiliser

- Reproduire en Python le confort d'interprétation de FactoMineR sur PCA / CA / MCA (tableaux d'aides, valeurs-tests).
- Enseignement et analyse exploratoire descriptive où la lecture des axes prime.

## Quand NE PAS l'utiliser

- Famille complète (FAMD, MFA, GPA), maintenance active et API sklearn moderne → [[Dev/Services/Prince|Prince]] (recommandé par défaut).
- Code de production : projet **peu maintenu** (v0.0.1, poignée de commits, pas de release récente).
- Données mixtes ou groupes de variables → [[Dev/Services/Prince|Prince]].

## Déploiement & coût

- Bibliothèque Python (`pip install fanalysis`), au-dessus de NumPy/pandas/matplotlib.
- Single-node ; calcul en mémoire.
- Open-source (licence affichée de façon incohérente : README BSD-3-Clause, classifieurs PyPI MIT) — gratuit dans les deux cas.

## Pièges

- **Faible maintenance** : version 0.0.1, très peu de commits, pas de mise à jour récente → risque de friction avec des versions récentes de NumPy/pandas.
- Périmètre limité à PCA/CA/MCA (pas de FAMD/MFA).
- Licence ambiguë entre README et PyPI — vérifier avant tout usage contraint.

## Alternatives

- [[Dev/Services/Prince|Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.

## Liens

- Concepts implémentés : [[Wiki/Concepts/PCA|PCA]], [[Wiki/Concepts/MCA|MCA]], [[Wiki/Concepts/CA|CA]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- [[Dev/Patterns/Comparatif - Réduction de dimension]] — analyse factorielle vs PCA / manifold.
- Doc : https://github.com/OlivierGarciaDev/fanalysis
