---
role: notion
nom: Optimisation bayésienne
alias: [Bayesian optimization, BO, Optimisation bayesienne, Optimisation de boîte noire, Black-box optimization, Expected improvement, GP-UCB, SMBO, Sequential model-based optimization, Tree-structured Parzen Estimator]
categorie: ml/hyperopt
domaines: [data-sci, ml-eng]
tags: [hyperparameter-tuning, bayesian, optimization, multi-armed-bandit]
---

# Optimisation bayésienne

## Aperçu

- Méthode pour optimiser une fonction **boîte noire**, **coûteuse** à évaluer et souvent **bruitée** : pas de gradient, quelques centaines d'évaluations au plus. Frazier (2018) la situe là où $f$ coûte cher, sans dérivées, avec un bruit supposé gaussien indépendant d'une évaluation à l'autre, sur un domaine continu de moins de ~20 dimensions.
- Le principe : construire un **modèle de substitution** de $f$ à partir des évaluations déjà faites, puis choisir la prochaine évaluation en maximisant une **fonction d'acquisition** qui arbitre entre explorer les zones incertaines et exploiter les zones prometteuses.
- Cas d'usage dominant en ML : le réglage d'hyperparamètres, où chaque évaluation est un entraînement. [[Optimisation d'hyperparamètres]] pose ce cadre et les stratégies simples (grille, hasard, arrêt précoce) ; cette page détaille le mécanisme bayésien et ses limites.

## Concepts clés

### La boucle
1. Évaluer $f$ en quelques points initiaux (Jones et al. (1998) proposent environ $10d$ points).
2. Ajuster le modèle de substitution à toutes les observations.
3. Maximiser l'acquisition (peu coûteuse à calculer, contrairement à $f$) pour obtenir le point suivant.
4. Évaluer $f$ en ce point, ajouter l'observation, recommencer jusqu'à épuisement du budget.

### Le modèle de substitution
- **Processus gaussien** : donne une moyenne et une **variance** en tout point, donc une mesure de son ignorance (voir [[Gaussian Process]]). Inférence exacte en $O(n^3)$ avec $n$ observations (Shahriari et al., 2016, §III-E).
- Choix du noyau : Snoek, Larochelle et Adams (2012) jugent le noyau gaussien à échelles par dimension trop lisse pour des problèmes réels et retiennent le **Matérn 5/2**. Ils préfèrent aussi intégrer sur les hyperparamètres du noyau (MCMC) plutôt que de les optimiser en un point.
- **Forêts aléatoires** (SMAC, Hutter, Hoos & Leyton-Brown, 2011) : moyenne et variance prédictives prises entre les arbres. Passent bien à l'échelle et gèrent variables catégorielles et conditionnelles ; en contrepartie, ce sont de « très mauvais extrapolateurs » et la variance est trop confiante loin des données (Shahriari et al., §III-E.3).
- **TPE** (Bergstra, Bardenet, Bengio & Kégl, 2011) : au lieu de modéliser $p(y \mid x)$, modélise $p(x \mid y)$ par deux densités, $\ell(x)$ pour les configurations dont le score est meilleur qu'un quantile $y^*$ des observations, $g(x)$ pour les autres. L'amélioration espérée croît avec $\ell(x)/g(x)$ ; le candidat retenu maximise ce rapport. Le coût est linéaire en nombre d'observations et de variables.

### Les fonctions d'acquisition
- **Amélioration espérée (EI)** : l'espérance du gain par rapport au meilleur point observé. Popularisée par Jones et al. (1998) pour l'optimisation globale de fonctions coûteuses ; c'est le choix de Snoek et al. (2012), qui la jugent mieux comportée que la probabilité d'amélioration et, contrairement à GP-UCB, sans paramètre propre à régler.
- **Probabilité d'amélioration (PI)** : probabilité de dépasser le meilleur point. Plus agressive : Shahriari et al. la disent portée à exploiter fortement quand la cible est inconnue.
- **UCB** (GP-UCB, Srinivas, Krause, Kakade & Seeger, 2010) : moyenne + $\kappa \times$ écart-type — l'optimisme face à l'incertitude. Le paramètre $\kappa$ règle explicitement l'exploration.
- **Échantillonnage de Thompson** : tirer une réalisation du substitut et jouer son maximum ; la randomisation sert de mécanisme d'exploration, et le coût d'un lot croît linéairement avec sa taille (TuRBO, Eriksson et al., 2019).
- Pour les définitions de l'UCB et de Thompson dans le cadre des bandits à bras discrets, voir [[Multi-armed bandits]].

### Compromis exploration-exploitation
- L'EI est croissante en l'écart-type du substitut et décroissante en la moyenne (en minimisation) : un point est attirant parce qu'il est probablement bon ou parce qu'il est mal connu (Jones et al., §4.1 ; Frazier, §4.1).
- Dans une région éloignée des données, un modèle global en haute dimension donne une incertitude postérieure partout élevée : les acquisitions « myopes » surexplorent alors et n'exploitent pas les zones prometteuses (Eriksson et al., 2019, §1).

### Optimisation par lots et parallélisme
- Quand plusieurs évaluations tournent en parallèle, on ne peut plus attendre la précédente. Stratégies : « Constant Liar » ou « Kriging believer » (imputer une valeur aux évaluations en cours), ou intégrer sur les résultats possibles (Snoek et al., 2012, §3.3 ; Shahriari et al., §V-E). L'EI multipoint (Frazier, §5) est la formulation exacte, plus coûteuse.
- Même si le nombre d'évaluations nécessaires ne baisse pas, le gain porte sur le temps réel (Shahriari et al., §V-E).

### Variables catégorielles et conditionnelles
- Un GP n'est pas immédiatement adapté aux espaces conditionnels — une variable n'existe que si une autre a telle valeur. Les forêts aléatoires et TPE y sont « naturellement » adaptés (Shahriari et al., §V-C).
- La documentation Optuna le confirme dans son tableau de samplers : TPE et recherche aléatoire gèrent catégorielles et conditionnelles sans réserve, `GPSampler` est signalé comme travaillant de façon inefficace sur l'espace conditionnel.

### Lien avec les bandits
- Srinivas et al. (2010) formalisent le problème comme un bandit où la fonction est tirée d'un GP ; le régret cumulé de GP-UCB est sous-linéaire, borné via le gain d'information maximal $\gamma_T$ (lien entre optimisation par GP et plan d'expériences). Pour un noyau gaussien, $\gamma_T = O((\log T)^{d+1})$.
- **Hyperband** (Li et al., 2018) prend le problème par l'autre bout : un bandit « à exploration pure, infini, non stochastique » qui alloue adaptativement des ressources à des configurations **tirées au hasard**, sans modèle. [[Optimisation d'hyperparamètres]] décrit l'arrêt précoce qui en découle.

## Les maths, simplement

- Modèle : $f \sim \mathcal{GP}(\mu, k)$ ; après $n$ observations, en $x$ : moyenne $\mu_n(x)$ et écart-type $\sigma_n(x)$.
- EI, en minimisation avec $f_{\min}$ le meilleur point observé et $u = (f_{\min} - \mu_n(x))/\sigma_n(x)$ (Jones et al., 1998, éq. 14-15) : $\mathrm{EI}(x) = (f_{\min} - \mu_n(x))\,\Phi(u) + \sigma_n(x)\,\varphi(u)$, avec $\Phi$ et $\varphi$ la fonction de répartition et la densité de la loi normale. Jones et al. notent que c'est $\sigma$, et non $\sigma^2$, qui apparaît.
- UCB (en maximisation) : $x_t = \arg\max_x \; \mu_{t-1}(x) + \beta_t^{1/2}\,\sigma_{t-1}(x)$ (Srinivas et al., 2010, éq. 6).
- TPE : $p(x \mid y) = \ell(x)$ si $y < y^*$, $g(x)$ si $y \ge y^*$ ; on maximise $\ell(x)/g(x)$.

## En pratique

- **Où ça paie** : peu d'hyperparamètres continus, entraînements chers, budget de quelques dizaines à quelques centaines d'essais. Hors de ce régime, voir les limites plus bas.
- **Optuna** : le sampler par défaut est `TPESampler`. Le tableau de la documentation indique, pour TPE, une complexité $O(dn\log n)$ et un budget recommandé de 100 à 1000 essais ; pour `GPSampler`, $O(n^3)$ et un budget « jusqu'à 500 ». Pour le deep learning, la doc cite une table qui conseille TPE avec peu de ressources parallèles, et GP-EI si l'espace est de faible dimension et continu. Voir [[Optuna]].
- **Autres moteurs** : [[Hyperopt]] implémente TPE ; [[Ray Tune]] enveloppe ces moteurs et ajoute le cluster ; BoTorch (Balandat et al., 2020) est la bibliothèque de référence pour les GP et les acquisitions modernes (lue en partie seulement).
- **Pitfall numérique** : l'EI et ses gradients valent exactement zéro en virgule flottante sur de larges zones quand $n$ et $d$ croissent, ce qui bloque l'optimiseur de l'acquisition. Ament et al. (NeurIPS 2023) la reformulent en log (LogEI) ; Jones et al. notaient déjà que l'EI est très multimodale.
- **Le bruit n'est pas toujours homoscédastique** : sur 108 tâches Bayesmark, Cowen-Rivers et al. (HEBO, JAIR 2022) trouvent que 66 % au moins sont hétéroscédastiques, et proposent de transformer entrées et sorties (Box-Cox, Yeo-Johnson). Lu par un sous-agent, non revérifié.
- **Toujours comparer à une recherche aléatoire** à budget égal, avec échelles log pour les paramètres d'échelle : c'est la base de comparaison naturelle (Bergstra & Bengio, 2012, §6).
- Un modèle bayésien n'évite pas le sur-apprentissage de la validation : Li et al. (2018, §4.2.1) observent sur 117 jeux OpenML que les méthodes bayésiennes surpassent Hyperband et la recherche aléatoire en erreur de test mais montrent des signes de sur-ajustement à l'ensemble de validation.

## Limites et débats

- **La dimension.** Quatre sources, quatre énoncés : Frazier (2018) limite le domaine d'usage à moins de 20 dimensions ; Wang et al. (REMBO) parlent d'un point de bascule autour de 15 à 20 dimensions ; Santoni et al. (2024) rapportent que la performance se dégrade au-delà de 15 variables ; Li et al. (Hyperband, §2.1) écrivent qu'en haute dimension, l'optimisation bayésienne standard se comporte comme la recherche aléatoire.
- **Mais le seuil est contesté.** Hvarfner, Hellsten et Nardi (ICML 2024) soutiennent qu'une modification simple — une loi a priori sur l'échelle de longueur qui croît avec la dimension — permet à l'optimisation bayésienne standard de dépasser des algorithmes spécialisés sur des problèmes réels jusqu'à 6 392 dimensions ; leur conclusion est que l'obstacle n'est pas la dimension mais la complexité supposée de l'objectif, tout en reconnaissant que des algorithmes taillés pour une structure réelle restent justifiés. Santoni et al. (BBOB, sans bruit, jusqu'à 60 dimensions) trouvent l'inverse pour la version standard : à 40 dimensions, elle n'est jamais compétitive à 200 évaluations, et seul TuRBO continue de progresser. **Ces deux résultats ne portent pas sur les mêmes problèmes** (réels continus avec a priori modifiés contre fonctions synthétiques avec les réglages par défaut) ; l'hypothèse que la version standard de Santoni et al. utilise les a priori que Hvarfner et al. mettent en cause est une inférence de cette page, non une affirmation de l'un des articles.
- **Les méthodes locales.** TuRBO (Eriksson et al., NeurIPS 2019) ajuste des modèles locaux dans des régions de confiance, et les alloue par une logique de bandit. Un travail récent (Doumont et al., arXiv:2512.00170, nov. 2025, révisé avril 2026 ; résumé lu seulement) rapporte que la régression linéaire bayésienne, ou un GP à noyau linéaire, égale l'état de l'art sur des espaces de 60 à 6 000 dimensions, ce que les auteurs prennent comme signe qu'on « ne comprend toujours pas » le sujet.
- **La recherche aléatoire résiste, selon le régime.** Bergstra et Bengio (2012) : à budget égal sur 32 dimensions de réseaux, la recherche aléatoire atteint une performance statistiquement égale sur 4 jeux sur 7 à une recherche manuelle plus grille, et supérieure sur 1 ; elle est efficace parce que seuls quelques hyperparamètres comptent vraiment. Li et al. (Hyperband) : la recherche aléatoire avec deux fois le budget (« random 2× ») est compétitive avec SMAC et TPE par défaut sur plusieurs tâches et surpasse les méthodes bayésiennes sur la tâche de noyaux (§4.3). Turner et al. (NeurIPS 2020 Black-Box Optimization Challenge) concluent à l'inverse que l'optimisation assistée par modèle bat la recherche aléatoire : 61 équipes sur 65 la battent, et les 20 premières utilisent un substitut.
- **Ces trois résultats ne se contredisent pas franchement.** Turner et al. portent sur environ 128 évaluations par lots de 8 et de petites tâches de ML (2 à 9 hyperparamètres d'après HEBO) ; Hyperband sur l'arrêt précoce et des défauts de packages ; Bergstra et Bengio sur une dimension effective faible. Le régime décide, et les réglages par défaut des baselines pèsent (dans Turner et al., hyperopt marque 82,4 contre 88,9 pour TuRBO).
- **Origine de l'EI.** Frazier la dit proposée par Močkus (1975) et popularisée par Jones et al. ; Jones et al. la datent d'« au moins 1978 » (Močkus, Tiesis, Žilinskas) ; Shahriari et al. citent la référence de 1978. Les travaux de Močkus n'ont pas pu être ouverts : la divergence est laissée telle quelle.
- **Garanties.** Les bornes de régret de GP-UCB supposent des hypothèses de régularité sur les trajectoires (bornes de dérivées valables pour le noyau gaussien et Matérn $\nu > 2$, violées par le noyau d'Ornstein-Uhlenbeck) et un modèle à hyperparamètres fixés ; Shahriari et al. notent qu'aucune borne n'existe pour un traitement entièrement bayésien des hyperparamètres.
- **Travaux récents** (résumés lus seulement) : OptunaHub (arXiv:2510.02798, oct. 2025) pour partager des algorithmes de boîte noire. Aucune étude 2025-2026 comparant frontalement optimisation bayésienne et recherche aléatoire pour le réglage d'hyperparamètres n'a été trouvée ; les résultats les plus récents sur la résistance de la recherche aléatoire restent ceux de Hyperband (2018).

## Approches voisines & alternatives

- [[Optimisation d'hyperparamètres]] — le cadre : grille, hasard, arrêt précoce, validation croisée imbriquée.
- [[Gaussian Process]] — le substitut de référence ; le noyau y fixe la lissité supposée de la fonction.
- [[Multi-armed bandits]] — UCB, Thompson et regret en bras discrets ; l'optimisation bayésienne en est le cas à bras continus, et Hyperband en est une variante sans modèle.
- [[Méthodes à noyau]] — le noyau d'un GP est celui de la KRR ; le coût cubique vient du même endroit.
- [[Optuna]], [[Hyperopt]], [[Ray Tune]] — les moteurs d'exécution.
- [[Comparatif - Optimisation d'hyperparamètres]] — les trois bibliothèques côte à côte.
- [[Convexity]] et [[Gradient descent]] — l'autre monde : minimiser une fonction connue et dérivable ; ici, pas de gradient.
- [[Optimisation sous contrainte]] — quand la boîte noire est aussi contrainte ; hors périmètre de cette page.
- [[Inférence bayésienne]] — le cadre dont le modèle de substitution hérite.

## Pour aller plus loin

- Jones, Schonlau, Welch (1998) — *Efficient Global Optimization of Expensive Black-Box Functions*, Journal of Global Optimization 13 : 455-492. https://www.stat.ubc.ca/~will/docs/JonSchWel1998_global_optimization.pdf
- Snoek, Larochelle, Adams (2012) — *Practical Bayesian Optimization of Machine Learning Algorithms*, NeurIPS. https://arxiv.org/abs/1206.2944
- Bergstra, Bardenet, Bengio, Kégl (2011) — *Algorithms for Hyper-Parameter Optimization*, NIPS 24 (TPE). https://proceedings.nips.cc/paper_files/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf
- Bergstra, Bengio (2012) — *Random Search for Hyper-Parameter Optimization*, JMLR 13 : 281-305. https://jmlr.csail.mit.edu/papers/volume13/bergstra12a/bergstra12a.pdf
- Shahriari, Swersky, Wang, Adams, de Freitas (2016) — *Taking the Human Out of the Loop: A Review of Bayesian Optimization*, Proceedings of the IEEE 104(1). https://www.cs.princeton.edu/~rpa/pubs/shahriari2016loop.pdf
- Hutter, Hoos, Leyton-Brown (2011) — *Sequential Model-Based Optimization for General Algorithm Configuration* (SMAC), LION 5. https://www.cs.ubc.ca/~hutter/papers/11-LION5-SMAC.pdf
- Srinivas, Krause, Kakade, Seeger (2010) — *Gaussian Process Optimization in the Bandit Setting* (version longue : IEEE Trans. Inf. Theory). https://arxiv.org/abs/0912.3995
- Frazier (2018) — *A Tutorial on Bayesian Optimization*. https://arxiv.org/abs/1807.02811
- Eriksson, Pearce, Gardner, Turner, Poloczek (2019) — *Scalable Global Optimization via Local Bayesian Optimization* (TuRBO), NeurIPS. https://arxiv.org/abs/1910.01739
- Wang, Hutter, Zoghi, Matheson, de Freitas — *Bayesian Optimization in a Billion Dimensions via Random Embeddings* (REMBO ; version IJCAI 2013 sous le titre « …in high dimensions via random embeddings »). https://arxiv.org/abs/1301.1942
- Hvarfner, Hellsten, Nardi (2024) — *Vanilla Bayesian Optimization Performs Great in High Dimensions*, ICML. https://arxiv.org/abs/2402.02229
- Santoni, Raponi, De Leone, Doerr (2024) — *Comparison of High-Dimensional Bayesian Optimization Algorithms on BBOB*. https://arxiv.org/abs/2303.00890
- Turner et al. (2021) — *Bayesian Optimization is Superior to Random Search for Machine Learning Hyperparameter Tuning: Analysis of the Black-Box Optimization Challenge 2020*. https://arxiv.org/abs/2104.10201
- Li, Jamieson, DeSalvo, Rostamizadeh, Talwalkar (2018) — *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*, JMLR 18 : 1-52. https://arxiv.org/abs/1603.06560
- Ament, Daulton, Eriksson, Balandat, Bakshy (2023) — *Unexpected Improvements to Expected Improvement for Bayesian Optimization*, NeurIPS. https://arxiv.org/abs/2310.20708
- Documentation Optuna — *Efficient Optimization Algorithms* (https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html) et *Samplers* (https://optuna.readthedocs.io/en/stable/reference/samplers/index.html).
- **Non ouverts** : Močkus (1975), Močkus, Tiesis, Žilinskas (1978) — références données d'après Jones, Shahriari et Frazier ; la version ICML 2010 de GP-UCB ; l'article IJCAI de REMBO (Wang et al., 2013, lu sous sa version journal). Les résumés seuls : Doumont et al. (2025), OptunaHub, BoTorch (lecture partielle).
