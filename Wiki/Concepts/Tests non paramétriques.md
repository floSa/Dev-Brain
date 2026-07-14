---
galaxie: wiki
type: concept
nom: Tests non paramétriques
alias: [non-parametric, non-parametric tests, Wilcoxon, Mann-Whitney, Kruskal-Wallis]
categorie: concept/stats
domaines: [data-sci]
tags: [non-parametric, hypothesis-testing]
---

# Tests non paramétriques

## Aperçu

- Tests qui ne supposent pas de forme de distribution (notamment pas de normalité).
- Travaillent souvent sur les rangs plutôt que sur les valeurs → robustes aux outliers et aux petits échantillons.

## Concepts clés

### Wilcoxon (signé, apparié)
- Compare deux mesures appariées (avant / après) — équivalent non paramétrique du t apparié.

### Mann-Whitney U (Wilcoxon rang-somme)
- Deux groupes indépendants — équivalent non paramétrique du test t.

### Kruskal-Wallis
- 3+ groupes indépendants — équivalent non paramétrique de l'ANOVA.

### Travail sur les rangs
- Remplacer les valeurs par leur rang neutralise la forme de la distribution et les valeurs extrêmes.

### Compromis
- Plus robustes, mais un peu moins puissants que les tests paramétriques quand la normalité tient vraiment.

## Les maths, simplement

- Principe : ordonner les données, remplacer chaque valeur par son rang, tester sur les sommes de rangs.
- Mann-Whitney : $U = R_1 - \dfrac{n_1(n_1+1)}{2}$ — $R_1$ = somme des rangs du groupe 1.
- Sous H0, les rangs se répartissent au hasard entre groupes → distribution de référence connue.
- Taille d'effet : corrélation de rangs $r = Z/\sqrt{N}$, ou la statistique de concordance.

## En pratique

- Choisir quand : normalité rejetée, outliers marqués, échelle ordinale, petit $n$.
- Correspondances : 2 appariés → Wilcoxon ; 2 indépendants → Mann-Whitney ; 3+ → Kruskal-Wallis (+ post-hoc Dunn).
- On teste une médiane / distribution, pas une moyenne : interpréter en conséquence.
- Le [[Bootstrap]] et les tests par permutation sont une autre voie distribution-free, plus flexible.

## Approches voisines & alternatives

- [[Test t et ANOVA]] — les équivalents paramétriques (Mann-Whitney ↔ t, Kruskal-Wallis ↔ ANOVA).
- [[Test du khi-deux]] — autre famille distribution-free, pour des catégories.
- [[Bootstrap]] — rééchantillonnage comme alternative sans hypothèse de loi.
- [[Tests d'hypothèse]] — cadre général.

## Pour aller plus loin

- Outils : `scipy.stats` (`wilcoxon`, `mannwhitneyu`, `kruskal`), `pingouin`, `scikit-posthocs` (Dunn).
