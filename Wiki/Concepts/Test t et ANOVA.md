---
galaxie: wiki
type: concept
nom: Test t et ANOVA
alias: [t-test, ANOVA, test de Student, comparaison de moyennes]
categorie: concept/stats
domaines: [data-sci]
tags: [hypothesis-testing, parametric-test, effect-size]
---

# Test t et ANOVA

## Aperçu

- Tests paramétriques de comparaison de moyennes : test t pour 2 groupes, ANOVA pour 3 groupes ou plus.
- Reposent sur la normalité (approchée) et, souvent, l'égalité des variances.

## Concepts clés

### Test t
- Une moyenne vs référence (t à un échantillon), deux groupes indépendants (Student / Welch), ou paires (t apparié).
- Welch ne suppose pas l'égalité des variances → défaut raisonnable pour deux groupes.

### ANOVA (analyse de la variance)
- Généralise le test t à 3+ groupes en comparant variance inter-groupes et intra-groupes.
- Un F significatif dit « au moins un groupe diffère », pas lequel.

### Tests post-hoc
- Après une ANOVA significative, comparaisons par paires (Tukey HSD) avec contrôle de la multiplicité.

### Hypothèses
- Normalité des résidus, homoscédasticité, indépendance. Violées → tests sur les rangs.

### Taille d'effet
- Cohen's d (test t), η² ou f (ANOVA) : l'ampleur, indépendante de $n$.

## Les maths, simplement

- Statistique t (deux groupes) : $t = \dfrac{\bar{x}_1 - \bar{x}_2}{SE_{\text{diff}}}$ — écart des moyennes rapporté à son erreur standard.
- F de l'ANOVA : $F = \dfrac{\text{variance inter-groupes}}{\text{variance intra-groupes}}$ — grand F ⇒ groupes plus dispersés entre eux qu'en interne.
- Taille d'effet (Cohen's d) : $d = \dfrac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}$ — écart en nombre d'écarts-types.
- Pour 2 groupes, $F = t^2$ : l'ANOVA est l'extension naturelle du test t.

## En pratique

- 2 groupes → t de Welch ; 3+ → ANOVA puis post-hoc Tukey.
- Vérifier la normalité (QQ-plot) et les variances (Levene) ; sinon Mann-Whitney / Kruskal-Wallis.
- Toujours accompagner la p-value d'une taille d'effet + IC sur la différence (cf. [[Intervalles de confiance]]).
- Mesures répétées (même sujet) → t apparié ou ANOVA à mesures répétées, pas la version indépendante.

## Approches voisines & alternatives

- [[MANOVA et tests multivariés]] — l'extension à **plusieurs réponses** corrélées (vecteur de moyennes).
- [[Tests non paramétriques]] — Mann-Whitney (↔ t), Kruskal-Wallis (↔ ANOVA) quand la normalité tombe.
- [[Test du khi-deux]] — équivalent pour des variables catégorielles (pas des moyennes).
- [[Correction des tests multiples]] — indispensable pour les comparaisons post-hoc.
- [[Analyse de puissance]] — dimensionner pour détecter un $d$ donné.
- [[Tests d'hypothèse]] — cadre général.

## Pour aller plus loin

- Outils : `scipy.stats` (`ttest_ind`, `f_oneway`), `statsmodels` (`anova_lm`), `pingouin`.
