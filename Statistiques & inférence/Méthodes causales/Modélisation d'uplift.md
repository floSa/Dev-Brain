---
role: notion
nom: Modélisation d'uplift
alias: [uplift modeling, uplift, modélisation de l'uplift, effet incrémental, CATE, conditional average treatment effect, effet de traitement hétérogène, heterogeneous treatment effects, HTE, meta-learner, S-learner, T-learner, X-learner, R-learner, DR-learner, causal tree, arbre causal, causal forest, forêt causale, courbe de Qini, Qini, AUUC, ciblage marketing]
categorie: stats/causal
domaines: [data-sci]
tags: [causal-inference, experimentation, regression]
---

# Modélisation d'uplift

## Aperçu

- Estimer, pour **chaque individu**, l'effet **incrémental** d'une action (une offre, un message, un traitement) : ce qui change *à cause* de l'action, pas ce qui arrive aux personnes qui la reçoivent.
- Autre nom de l'**effet de traitement conditionnel** (CATE) : l'effet moyen de l'action sur les individus qui ont les mêmes caractéristiques $x$. Gutierrez et Gérardy (2017) le disent tel quel : modéliser l'uplift revient à estimer un CATE.
- Sert à **cibler** : n'agir que sur ceux dont l'effet est positif, et épargner ceux qui auraient acheté de toute façon ou que l'action fait fuir.
- Un modèle de réponse classique (« qui achète ? ») ne répond pas à cette question : il ne regarde pas le groupe témoin. Radcliffe et Surry (2011) le soulignent : l'uplift est un phénomène de second ordre, l'écart est souvent petit devant l'effet principal.

## Concepts clés

### Effet moyen, effet conditionnel, effet individuel

- **ATE** : un effet moyen sur toute la population — ce que produit un [[A-B testing|test A/B]] simple.
- **CATE** $\tau(x)$ : l'effet moyen **sachant** les covariables. C'est l'objet de l'uplift.
- **Effet individuel** $Y_i(1) - Y_i(0)$ : jamais observé, on ne voit qu'un seul des deux résultats potentiels. Künzel et al. (2019) montrent qu'on peut construire des mécanismes aux lois observées identiques mais aux effets individuels différents. Seul le CATE est estimable, et il est aussi le meilleur estimateur de l'effet individuel au sens de l'erreur quadratique.

### Hypothèses d'identification

- **Ignorabilité** : $(Y(0), Y(1)) \perp W \mid X$ — une fois $X$ fixé, l'affectation est « comme aléatoire ». Posée à l'identique par Künzel et al., Athey et Imbens, Nie et Wager.
- **Chevauchement** (overlap) : $0 < e_{\min} < e(x) < e_{\max} < 1$ — chaque profil a une chance de recevoir chacun des deux traitements.
- Dans un **essai randomisé** (cas normal du marketing selon Gutierrez et Gérardy), ces deux conditions tiennent par construction. Hors essai, elles se supposent, pas se vérifient : voir [[Inférence causale]].

### Méta-apprenants (Künzel et al., 2019)

Ils emploient n'importe quel modèle de régression comme brique.

- **S-learner** : un seul modèle $\hat\mu(x, w)$, le traitement est une variable parmi d'autres ; $\hat\tau(x) = \hat\mu(x,1) - \hat\mu(x,0)$. Le traitement n'a aucun rôle spécial : un modèle pénalisé peut l'ignorer, d'où un biais vers 0.
- **T-learner** : deux modèles, un par bras ; $\hat\tau = \hat\mu_1 - \hat\mu_0$. Ne mutualise pas les données : pénalisant si l'effet est simple, utile si les deux réponses n'ont rien en commun.
- **X-learner** : comme le T-learner, puis impute l'effet de chaque individu avec le modèle de l'autre bras, régresse ces effets imputés sur $X$ et combine les deux résultats avec un poids (le score de propension convient). Les auteurs le disent adapté quand un bras est beaucoup plus grand que l'autre ; il n'est « jamais le pire » en simulation, mais pas le meilleur partout.
- **R-learner** (Nie et Wager) : s'appuie sur la décomposition de Robinson et un apprentissage en deux étapes avec validation croisée. Propriété « quasi-oracle » **démontrée pour un cas** (régression à noyau pénalisée), pas pour tout apprenant de base.
- **DR-learner** (Kennedy) : régresse sur $X$ un pseudo-résultat doublement robuste ; l'erreur dépend d'un produit des erreurs sur la propension et sur les réponses.

### Arbres et forêts causaux

- **Arbre causal** (Athey et Imbens, 2016) : partitionne l'espace des covariables pour que l'effet soit homogène dans chaque feuille. Un arbre est **honnête** quand l'échantillon qui choisit la partition n'est pas celui qui estime l'effet dans les feuilles — d'où un découpage de l'échantillon en deux.
- **Forêt causale** (Wager et Athey, 2018) : moyenne d'arbres honnêtes ; estimation ponctuellement consistante et asymptotiquement gaussienne, avec un estimateur de variance, sous honnêteté, ignorabilité et chevauchement.
- **Arbres d'uplift** historiques (Radcliffe et Surry, 2011) : arbres dont la coupe maximise l'écart d'uplift entre feuilles, avec un critère de significativité.

### Évaluer un modèle d'uplift

- Pas de vérité terrain individuelle : on ne peut pas calculer l'erreur sur $\tau(x_i)$. On évalue donc le **classement** que produit le modèle.
- **Courbe d'uplift / de gain incrémental** : on trie du meilleur au plus mauvais score, on cumule le gain en comparant traités et témoins. Plus elle s'écarte de la diagonale (ciblage au hasard), mieux le modèle classe.
- **Qini** : aire de cette courbe, par analogie avec le Gini.
- ⚠ **Sous un même nom, des quantités différentes** (désaccord laissé tel quel entre les sources lues) :
  - Radcliffe et Surry : Qini = aire **entre** la courbe et la diagonale.
  - Gutierrez et Gérardy : le coefficient de Qini est l'aire **sous** la courbe de Qini.
  - Yadlowsky et al. (RATE) : le coefficient de Qini est l'aire entre la courbe et la diagonale, cas particulier d'une famille avec le poids $\alpha(u) = u$ ; leur AUTOC prend $\alpha(u) = 1$ et pèse davantage le haut du classement.
  - Dans les bibliothèques, `scikit-uplift` normalise par la courbe parfaite et exige un résultat binaire ; `causalml` distingue `qini_score` (aire entre la courbe et l'aléatoire) et `auuc_score` (aire sous le gain cumulé). Un « AUUC » de l'une n'est pas celui de l'autre.

## Les maths, simplement

- CATE : $\tau(x) = \mathbb E[Y(1) - Y(0) \mid X = x]$ — l'effet moyen sur les individus de profil $x$.
- Décomposition de Robinson : $Y - m(X) = (W - e(X))\,\tau(X) + \varepsilon$, avec $m(x) = \mathbb E[Y \mid X = x]$ et $e(x) = P(W=1 \mid X=x)$. L'effet est le coefficient d'une régression sur le **résidu de traitement** $W - e(X)$ : c'est la base du R-learner.
- Courbe de Qini, version de Gutierrez et Gérardy (attribuée à Radcliffe 2007, non lu ici) : en triant par score décroissant, à une fraction $t$ de la population, $g(t) = Y^T_t - Y^C_t\,\dfrac{N^T_t}{N^C_t}$, où $Y^T_t$ et $Y^C_t$ sont les résultats cumulés chez les traités et les témoins, $N^T_t$ et $N^C_t$ leurs effectifs. Le second terme remet le témoin à l'échelle du groupe traité.
- Courbe TOC (RATE) : $\mathrm{TOC}(u) = \mathbb E[\tau(X) \mid X \text{ dans le premier } u\ \text{du classement}] - \mathbb E[\tau(X)]$ — de combien le haut du classement fait mieux que la moyenne.

## En pratique

- **Commencer par un essai randomisé** : sans lui, ignorabilité et chevauchement sont des paris. Le groupe témoin aléatoire est, pour Radcliffe et Surry, la clé de l'exercice.
- **Taille d'échantillon** : l'uplift est un signal faible. Un témoin souvent dix fois plus petit que le groupe traité, des variances élevées : prévoir plus de données que pour un simple ATE ([[Analyse de puissance]]).
- **Données d'observation** : les méta-apprenants n'ont de sens que si l'ignorabilité tient. Künzel et al. recommandent la plus grande prudence quand le chevauchement est violé ; Athey et Imbens, Wager et Athey exigent l'ignorabilité pour leurs garanties.
- **Fuite de traitement** (raisonnement, non appuyé par une source lue qui en ferait un point dédié) : les hypothèses ci-dessus portent sur des covariables **mesurées avant** le traitement (Sverdrup et al. l'écrivent). Une variable calculée après l'action, ou qui l'encode, fait fuir l'affectation dans les entrées — le modèle « trouve » l'effet sans l'estimer.
- **Choisir le modèle** : aucun critère de sélection n'est meilleur partout (Curth et van der Schaar, 2023) ; les critères « plug-in » favorisent les estimateurs qui leur ressemblent. Comparer plusieurs méta-apprenants avec plusieurs briques de base avant de trancher.
- **Benchmarks** : IHDP et ACIC 2016 ont des propriétés (surfaces de réponse, chevauchement, déséquilibre) qui avantagent certains algorithmes (Curth et van der Schaar, 2021, papier d'atelier).
- **Métriques de rang** : elles ne mesurent que l'ordre, pas la calibration des scores ([[Calibration]]) ; un bon Qini ne dit pas de combien l'effet est surestimé.
- **Intervalles** : Künzel et al. notent qu'aucun intervalle par bootstrap testé n'atteignait la bonne couverture ; la forêt causale fournit en revanche une variance estimée.

### Travaux récents (2026)

Trois prépublications lues, toutes sur l'**évaluation** :

- Yang, Liu, Huang — *Evaluating Uplift Modeling under Structural Biases* (arXiv 2603.20775, KDD 2026) : ciblage et prédiction de l'effet sont deux objectifs distincts ; TARNet est stable face aux biais testés ; les métriques proches de l'ATE classent plus fiablement en présence d'imperfections.
- Li — *UpliftBench* (arXiv 2608.00915, août 2026) : sur IHDP, le Qini non normalisé suit très peu l'exactitude de l'effet (corrélation de rangs moyenne +0,07), l'AUUC mieux ; sur Jobs, les métriques de rang ne conviennent pas à une politique à seuil. Résultats propres à ces jeux : l'auteur précise qu'ils ne se généralisent pas.
- Hadjipantelis et al. — *Significance-First Splitting* (arXiv 2607.03999) : arbre hybride entre arbres d'uplift à critère de significativité et arbres causaux honnêtes.

Ce sont des prépublications d'un seul travail chacune, non répliquées ici.

## Approches voisines & alternatives

- [[Inférence causale]] — le cadre : résultats potentiels, ignorabilité, chevauchement. L'uplift en est le volet « effet conditionnel ».
- [[A-B testing]] — fournit les données idéales (randomisation) ; estime un effet moyen, l'uplift l'éclate par profil.
- [[Multi-armed bandits]] — allocation adaptative de l'action ; l'uplift cible à partir d'un essai fini, le bandit apprend en route.
- [[Diff-in-Diff]] — quasi-expérience pour un effet moyen sans randomisation ; ne produit pas un effet par individu.
- [[CUPED]] — réduit la variance de l'ATE par une covariable de pré-période ; vise l'efficacité de l'estimation, pas l'hétérogénéité.
- [[Calibration]] — vérifie que les probabilités sont fiables ; l'évaluation par Qini n'en dit rien.
- Briques du brain : **sans objet** — aucune bibliothèque d'uplift (CausalML, EconML, scikit-uplift) n'a de fiche ; les modèles de base peuvent venir de scikit-learn.

## Pour aller plus loin

- Rubin (1974), *Estimating causal effects of treatments in randomized and nonrandomized studies*, J. Educational Psychology 66(5) — résumé de notice seulement, texte non lu.
- Künzel, Sekhon, Bickel, Yu (2019), *Metalearners for estimating heterogeneous treatment effects using machine learning*, PNAS ; arXiv : <https://arxiv.org/abs/1706.03461>
- Athey & Imbens (2016), *Recursive partitioning for heterogeneous causal effects*, PNAS 113(27) ; arXiv : <https://arxiv.org/abs/1504.01132>
- Wager & Athey (2018), *Estimation and inference of heterogeneous treatment effects using random forests*, JASA 113(523) ; arXiv : <https://arxiv.org/abs/1510.04342>
- Nie & Wager, *Quasi-oracle estimation of heterogeneous treatment effects* (arXiv <https://arxiv.org/abs/1712.04912>) ; Kennedy, *Towards optimal doubly robust estimation of heterogeneous causal effects* (arXiv <https://arxiv.org/abs/2004.14497>).
- Radcliffe (2007), *Using control groups to target on predicted lift*, Direct Marketing Analytics Journal — non ouvert ; Radcliffe & Surry (2011), *Real-world uplift modelling with significance-based uplift trees*, white paper : <https://stochasticsolutions.com/pdf/sig-based-up-trees.pdf>
- Gutierrez & Gérardy (2017), *Causal inference and uplift modelling: a review of the literature*, PMLR 67 : <http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf>
- Yadlowsky, Fleming, Shah, Brunskill, Wager, *Evaluating treatment prioritization rules via rank-weighted average treatment effects* (RATE) : <https://arxiv.org/abs/2111.07966> ; Sverdrup, Wu, Athey, Wager, *Qini curves for multi-armed treatment rules* : <https://arxiv.org/abs/2306.11979>
- Curth & van der Schaar (2023), *In search of insights, not magic bullets*, ICML : <https://arxiv.org/abs/2302.02923> ; (2021) *Doing great at estimating CATE?* : <https://arxiv.org/abs/2107.13346>
- Outils (pas de fiche dans le brain) : CausalML (Uber), EconML (py-why), scikit-uplift. À la date du relevé, les deux premiers sont maintenus, scikit-uplift n'a plus de version depuis août 2022.
- Connexions brain : [[Inférence causale]], [[A-B testing]], [[Calibration]].
