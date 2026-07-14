---
galaxie: wiki
type: concept
nom: Test du khi-deux
alias: [chi-squared, chi-square, khi2, test d'indépendance]
categorie: concept/stats
domaines: [data-sci]
tags: [hypothesis-testing, p-value]
---

# Test du khi-deux

## Aperçu

- Famille de tests sur données catégorielles : compare des effectifs observés à des effectifs attendus.
- Deux usages courants : indépendance (table de contingence) et adéquation (goodness-of-fit).

## Concepts clés

### Test d'indépendance
- Deux variables catégorielles sont-elles liées ? (ex. groupe × conversion).
- Sur une table de contingence ; H0 = indépendance.

### Test d'adéquation
- Une distribution observée colle-t-elle à une distribution théorique attendue ?

### Effectifs attendus
- Sous H0, effectif = (total ligne × total colonne) / total général.
- Approximation valable si les attendus sont assez grands (règle ≥ 5).

### Petits effectifs
- Attendus < 5 → test exact de Fisher (table 2×2) plutôt que khi-deux.

### Taille d'effet
- Cramér's V (ou φ pour 2×2) : force de l'association.

## Les maths, simplement

- Statistique : $\chi^2 = \sum_i \dfrac{(O_i - E_i)^2}{E_i}$ — somme des écarts relatifs au carré entre observé $O$ et attendu $E$.
- Degrés de liberté (indépendance) : $(r-1)(c-1)$, pour $r$ lignes et $c$ colonnes.
- Grand $\chi^2$ ⇒ observé loin de l'attendu ⇒ petite p-value.
- Cramér's V : $V = \sqrt{\dfrac{\chi^2}{n\,(k-1)}}$, $k=\min(r,c)$ — entre 0 (nul) et 1 (fort).

## En pratique

- Données = comptages (pas des proportions déjà calculées ni des moyennes).
- Vérifier la règle des attendus ≥ 5 ; sinon Fisher exact ou regrouper des modalités.
- Significatif = « association existe » ; rapporter Cramér's V pour l'ampleur.
- Données appariées (avant/après sur les mêmes sujets) → test de McNemar, pas le khi-deux d'indépendance.

## Approches voisines & alternatives

- [[Test t et ANOVA]] — l'équivalent pour des moyennes (données numériques).
- [[Tests non paramétriques]] — même esprit distribution-free, sur des rangs.
- [[Analyse de puissance]] — dimensionner une table de contingence (effet w).
- [[Tests d'hypothèse]] — cadre général.
- Test exact de Fisher — alternative exacte sur petits effectifs.

## Pour aller plus loin

- Outils : `scipy.stats` (`chi2_contingency`, `chisquare`, `fisher_exact`).
