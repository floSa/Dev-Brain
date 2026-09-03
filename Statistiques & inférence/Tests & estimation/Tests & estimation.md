---
role: hub
nom: Tests & estimation
alias: [inférence fréquentiste, tests statistiques]
pitch: Ce qu'un échantillon déjà collecté permet de conclure — une décision binaire, une fourchette, ou un paramètre estimé.
domaines: [data-sci]
tags: [statistical-inference, hypothesis-testing, confidence-interval, p-value, non-parametric, parametric-test, effect-size, maximum-likelihood, resampling, survival-analysis]
---

# Tests & estimation

> Ce qu'un échantillon déjà collecté permet de conclure — une décision binaire, une fourchette, ou un paramètre estimé.

## Ce qu'il faut comprendre

- **Ce dossier suppose la donnée déjà là.** Concevoir la collecte — randomiser, réduire la variance, décider quand arrêter — est un autre sujet, resté au niveau du domaine avec [[A-B testing]], [[CUPED]], [[Sequential testing]] et [[Multi-armed bandits]]. Ici, l'échantillon est un fait ; la seule question est ce qu'on a le droit d'en dire.
- **Un test et un intervalle répondent à la même question, avec deux sorties différentes.** [[Tests d'hypothèse]] rend un oui/non ; [[Intervalles de confiance]] rend une ampleur assortie de son incertitude, et contient le test — si la valeur nulle est hors de l'intervalle, le test rejette. L'intervalle dit tout ce que dit le test, plus l'ordre de grandeur ; préférer le test seul est presque toujours une perte d'information.
- **Le choix du test se fait sur la nature des données, pas sur le confort.** Deux ou plusieurs moyennes sur données à peu près normales → [[Test t et ANOVA]] ; plusieurs réponses simultanées → [[MANOVA et tests multivariés]] ; des effectifs par catégorie → [[Test du khi-deux]] ; pas d'hypothèse de distribution tenable → [[Tests non paramétriques]], qui travaillent sur les rangs et se paient en puissance.
- **Une p-value seule ne décide rien.** Elle dépend de $n$ autant que de l'effet : avec assez de lignes, tout devient significatif. La taille d'effet est ce qui rend le résultat lisible, et [[Analyse de puissance]] est ce qui aurait dû être fait **avant** — c'est elle qui donne le $n$ nécessaire pour détecter un effet donné, et elle explique après coup autant les résultats manqués que les significativités creuses.
- **Multiplier les tests fabrique des faux positifs mécaniquement**, et c'est le piège le plus fréquent dès qu'un tableau de bord compare vingt métriques : [[Correction des tests multiples]]. Deux philosophies à ne pas confondre — contrôler le risque d'au moins un faux positif (FWER, conservateur) ou la part de faux positifs parmi les rejets (FDR, adapté au criblage).
- **Quand la formule manque, le rééchantillonnage la remplace.** [[Bootstrap]] donne un intervalle pour une statistique dont personne ne connaît la loi d'échantillonnage — médiane, ratio, quantile, métrique métier composite. C'est souvent la réponse la plus courte à « quelle est l'incertitude de ce chiffre ? ».
- **Deux familles de données ont leur traitement propre**, et un test ordinaire y ment. [[Analyse de survie]] ([[lifelines]]) parce que la **censure** — l'événement pas encore survenu à la fin de l'étude — n'est ni une absence d'événement ni une ligne à jeter. [[Maximum de vraisemblance]] parce que c'est le principe d'estimation qui sous-tend la régression, les GLM et une grande partie du reste : le connaître évite de traiter chaque modèle comme une boîte à part.

## Choisir

- Une loi, un test brut, une brique dans son propre code → [[scipy.stats]].
- Un modèle et sa table de résultats, façon R → [[statsmodels]].
- Quelques tests à lire vite, tailles d'effet incluses → [[pingouin]].
- Un temps jusqu'à un événement, avec des observations censurées → [[lifelines]].
- Une incertitude sans formule analytique → [[Bootstrap]], à la main sur `scipy`.
- Une distribution a posteriori plutôt qu'une p-value → [[Bayésien]], pas ce dossier.

<!-- AUTO:START -->
### Notions
- [[Analyse de puissance]] — domaines : data-sci
- [[Analyse de survie]] — domaines : data-sci
- [[Bootstrap]] — domaines : data-sci
- [[Correction des tests multiples]] — domaines : data-sci
- [[Intervalles de confiance]] — domaines : data-sci
- [[MANOVA et tests multivariés]] — domaines : data-sci
- [[Maximum de vraisemblance]] — domaines : data-sci
- [[Test du khi-deux]] — domaines : data-sci
- [[Test t et ANOVA]] — domaines : data-sci
- [[Tests d'hypothèse]] — domaines : data-sci
- [[Tests non paramétriques]] — domaines : data-sci

### Briques
- [[lifelines]] — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.
- [[pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- [[scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
<!-- AUTO:END -->
