---
galaxie: dev
type: service
nom: pingouin
alias: []
pitch: "Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/scipy.stats|scipy.stats]]", "[[Dev/Services/statsmodels|statsmodels]]"]
remplace_par: []
status: actif
tags: [hypothesis-testing, effect-size, statistical-power, non-parametric, parametric-test]
url_docs: https://pingouin-stats.org/
url_repo: https://github.com/raphaelvallat/pingouin
---

# pingouin

## Pourquoi

Bibliothèque de tests statistiques pensée pour la **lisibilité** : chaque test renvoie un DataFrame pandas prêt à publier, avec p-value **mais aussi taille d'effet, intervalle de confiance et puissance** — ce que scipy.stats laisse à calculer à part. Couvre t-tests, ANOVA (y compris à mesures répétées et mixtes) avec post-hoc et corrections, corrélations (dont robustes/partielles), tests non paramétriques, et une `pingouin.power_*` pour le dimensionnement. Écrite au-dessus de pandas/NumPy/SciPy.

## Quand l'utiliser

- Analyse statistique « classique » (recherche, expérimentation) où l'on veut p-value + taille d'effet + puissance d'un seul appel.
- ANOVA à mesures répétées / mixtes avec tests post-hoc et correction de la multiplicité intégrés.
- Calcul de puissance et de taille d'échantillon (`power_ttest`, `power_anova`…).

## Quand NE PAS l'utiliser

- Catalogue exhaustif de lois et de tests, ou dépendance minimale → [[Dev/Services/scipy.stats|scipy.stats]].
- Modèles de régression / séries temporelles avec diagnostics complets → [[Dev/Services/statsmodels|statsmodels]].
- Contrainte de licence permissive : pingouin est en **GPL-3.0** (copyleft) — à vérifier avant intégration dans un produit fermé.

## Déploiement & coût

- Bibliothèque Python (`uv add pingouin`), maintenue par Raphael Vallat.
- Single-node ; calcul en mémoire sur pandas.
- GPL-3.0 (copyleft), gratuit — attention à la contamination de licence en distribution.

## Pièges

- **GPL-3.0** : licence plus contraignante que le BSD de scipy/statsmodels.
- Performances pensées pour des jeux de taille recherche, pas pour du massif.
- Surcouche de SciPy : pour un cas très spécifique, le test sous-jacent reste dans scipy.stats.

## Alternatives

- [[Dev/Services/scipy.stats|scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[Dev/Services/statsmodels|statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.

## Liens

- Concepts implémentés : [[Wiki/Concepts/Test t et ANOVA|Test t et ANOVA]], [[Wiki/Concepts/Tests non paramétriques|Tests non paramétriques]], [[Wiki/Concepts/Analyse de puissance|Analyse de puissance]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://pingouin-stats.org/
