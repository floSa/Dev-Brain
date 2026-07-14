---
galaxie: wiki
type: concept
nom: Correction des tests multiples
alias: [multiple testing, multiple comparisons, Bonferroni, FDR]
categorie: concept/stats
domaines: [data-sci]
tags: [hypothesis-testing, multiple-testing, p-value]
---

# Correction des tests multiples

## Aperçu

- Lancer beaucoup de tests gonfle mécaniquement les faux positifs : il faut ajuster les p-values (ou le seuil) pour le contrôler.
- Deux philosophies : contrôler le risque d'au moins un faux positif (FWER), ou la part de faux positifs parmi les rejets (FDR).

## Concepts clés

### Le problème
- À α = 5 %, 20 tests indépendants sous H0 → en moyenne 1 « significatif » par pur hasard.

### FWER (family-wise error rate)
- Proba d'au moins un faux positif sur toute la famille. Contrôle strict.
- Bonferroni : seuil = α / m. Simple, conservateur.
- Holm : version séquentielle, uniformément plus puissante que Bonferroni.

### FDR (false discovery rate)
- Proportion attendue de faux positifs parmi les résultats déclarés positifs.
- Benjamini-Hochberg : moins conservateur, adapté au criblage (génomique, A/B massif).

### Choix
- Peu de tests, faux positif coûteux → FWER. Beaucoup de tests exploratoires → FDR.

## Les maths, simplement

- Famille de $m$ tests. Sans correction : $P(\ge 1 \text{ faux positif}) = 1-(1-\alpha)^m \to 1$ quand $m$ grandit.
- Bonferroni : rejeter si $p_i \le \alpha/m$ (équivaut à $p_i^{adj} = m\,p_i$).
- Benjamini-Hochberg : p-values triées $p_{(1)}\le\dots\le p_{(m)}$ ; plus grand $k$ tel que $p_{(k)} \le \dfrac{k}{m}\,\alpha$ ; rejeter les $k$ premières.
- FWER ≥ FDR : contrôler le FWER est plus exigeant.

## En pratique

- Compter **tous** les tests réellement effectués (y compris ceux non rapportés).
- Post-hoc d'ANOVA, comparaisons de modèles, A/B multi-variantes : correction obligatoire.
- BH (FDR) par défaut en exploration à grande échelle ; Holm si l'on veut le FWER sans le conservatisme de Bonferroni.
- La correction réduit la puissance → en tenir compte dès le dimensionnement.

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — la brique répétée ici.
- [[Test t et ANOVA]] — les post-hoc sont le cas typique de multiplicité.
- [[Analyse de puissance]] — la correction abaisse la puissance, à anticiper.
- [[Sequential testing]] — même problème décalé dans le temps (peeking) : la multiplicité y est sur les regards répétés.

## Pour aller plus loin

- Outils : `statsmodels.stats.multitest` (`multipletests` : `bonferroni`, `holm`, `fdr_bh`).
