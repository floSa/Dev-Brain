---
role: notion
nom: Modèles graphiques probabilistes
alias: [Modèles graphiques probabilistes, modèles graphiques, probabilistic graphical models, PGM, réseaux bayésiens, réseau bayésien, Bayesian network, Bayes net, belief network, champs de Markov, champ de Markov, Markov random field, MRF, réseau de Markov, modèle graphique orienté, modèle graphique non orienté, d-séparation, d-separation, élimination de variables, variable elimination, arbre de jonction, junction tree, propagation de croyances, belief propagation, loopy belief propagation, pgmpy]
categorie: stats/bayesien
domaines: [data-sci]
tags: [bayesian, probability, markov, statistical-inference]
---

# Modèles graphiques probabilistes

## Aperçu

- Représenter une **loi de probabilité jointe** sur plusieurs variables par un **graphe** : les nœuds sont les variables, l'absence d'arête dit une **indépendance conditionnelle**.
- Deux familles : les **réseaux bayésiens** (graphe orienté acyclique, DAG) et les **champs de Markov** (graphe non orienté). Les deux factorisent la loi jointe en morceaux locaux ; ce qui change est la forme des morceaux.
- Intérêt : une loi jointe sur $N$ variables à $K$ états demande $O(K^N)$ paramètres sans structure, contre $O(N K^{N_P+1})$ avec un DAG dont chaque nœud a au plus $N_P$ parents (Murphy, *Probabilistic Machine Learning: Advanced Topics*, §4.2). Le graphe est ce qui rend le calcul et l'estimation possibles.
- Un réseau bayésien n'a **rien d'intrinsèquement bayésien** : c'est une manière de définir une loi, qui peut s'estimer par n'importe quelle méthode (Murphy, §4.2). Le sens de « bayésien » est ici historique, pas méthodologique ; la page [[Inférence bayésienne]] traite de l'autre sens, celui des paramètres variables aléatoires.
- Ce que cette page ne répète pas : la lecture causale des flèches ([[Inférence causale]], [[Découverte causale]]), le cas séquentiel ([[Modèles de Markov cachés et filtre de Kalman]], un modèle graphique particulier à structure en chaîne), les algorithmes d'échantillonnage ([[MCMC]], [[Monte Carlo et inférence variationnelle]]).

## Concepts clés

### Factorisation d'une loi jointe

- **Réseau bayésien** : en numérotant les nœuds dans un ordre topologique, la loi se factorise en probabilités conditionnelles locales (Murphy, éq. 4.2) :
  $$p(x_{1:N}) = \prod_{i=1}^{N} p\big(x_i \mid x_{\mathrm{pa}(i)}\big),$$
  où $\mathrm{pa}(i)$ désigne les parents de $i$ dans le graphe. Chaque facteur est une table (variables discrètes) ou une loi paramétrique.
- **Champ de Markov** : la loi s'écrit comme un produit de **fonctions de potentiel** sur les cliques, normalisé :
  $$p(x) = \frac{1}{Z} \prod_{c \in \mathcal C} \psi_c(x_c), \qquad Z = \sum_x \prod_{c} \psi_c(x_c).$$
  C'est le théorème de **Hammersley–Clifford**, énoncé pour une loi strictement positive $p > 0$. Murphy note que le théorème « n'a jamais été publié » et renvoie à Koller et Friedman pour une preuve, non lue ici.
- Les potentiels ne sont pas des probabilités : seule la constante de normalisation $Z$ (la fonction de partition) donne une loi. Son calcul est souvent le point dur.
- Un **graphe de facteurs** est une représentation commune aux deux familles, utilisée par les algorithmes de passage de messages.

### Indépendance conditionnelle et d-séparation

- Dans un DAG, l'indépendance se lit par la **d-séparation**. Un chemin non orienté entre $s$ et $t$ est bloqué par un ensemble $C$ si (Murphy, §4.2.4.1) :
  - il contient une **chaîne** $s \to m \to t$ (ou le sens inverse) avec $m \in C$ ;
  - ou une **fourche** $s \leftarrow m \to t$ avec $m \in C$ ;
  - ou un **collisionneur** $s \to m \leftarrow t$ avec $m \notin C$ et aucun descendant de $m$ dans $C$.
- Si tous les chemins de $A$ à $B$ sont bloqués par $C$, alors $X_A \perp X_B \mid X_C$ (propriété de Markov globale). L'algorithme « Bayes ball » le teste en pratique (Murphy).
- **Le collisionneur fonctionne à l'envers** : deux causes indépendantes deviennent dépendantes quand on conditionne sur leur effet (« explaining away »). C'est la raison pour laquelle les indépendances d'un DAG ne sont pas monotones.
- Les propriétés de Markov **globale, locale et ordonnée** d'un DAG sont équivalentes, et équivalentes à la factorisation (Murphy ; la preuve est renvoyée à Koller et Friedman, non lue). Dans un graphe non orienté, globale, locale et de paire sont équivalentes si $p > 0$ ; la « couverture de Markov » d'un nœud y est l'ensemble de ses voisins.
- **I-carte.** Un graphe $G$ est une I-carte de $p$ si toutes ses indépendances sont vraies dans $p$ ; minimale si aucune arête ne peut être retirée. Le graphe complet est I-carte de toute loi. Une loi **infidèle** possède des indépendances absentes du graphe, notamment à cause de contraintes déterministes.
- **Les deux familles ne représentent pas les mêmes lois** (Murphy, §4.5) : la structure en V $A \to C \leftarrow B$ n'a pas d'équivalent non orienté, le cycle à quatre nœuds n'a pas d'équivalent orienté.
- **Équivalence de Markov** : deux DAG expriment les mêmes indépendances si et seulement s'ils ont les mêmes arêtes (sans orientation) et les mêmes structures en V non couvertes (Verma et Pearl, UAI 1990, théorème 1). Conséquence : la loi observée seule ne permet pas d'orienter toutes les arêtes.

### Inférence exacte

- **Question** : calculer une marginale ou une loi conditionnelle $p(x_Q \mid x_E)$ sachant une observation $x_E$.
- **Élimination de variables.** Sommer les variables inutiles l'une après l'autre en regroupant les facteurs où elles figurent. Le coût dépend de l'**ordre d'élimination** : $O(K^{w_\pi + 1})$ pour une largeur induite $w_\pi$ de l'ordre $\pi$ (Murphy, §9.5.2).
- La **largeur d'arbre** est la plus petite largeur induite possible. Trouver l'ordre optimal est NP-complet (Yannakakis 1981 ; Arnborg, Corneil, Proskurowski 1987, cités par Murphy, non lus) ; l'heuristique gloutonne *min-fill* est courante.
- **Arbre de jonction** (Lauritzen et Spiegelhalter, 1988) : construire un arbre de cliques du graphe triangulé, puis y faire circuler des messages de façon à obtenir **toutes** les marginales en deux passes, au lieu de relancer une élimination par requête (Murphy, §9.6).
- Pour une chaîne ou un arbre, l'inférence est linéaire ; un graphe dense a une largeur d'arbre de l'ordre de $N$ et le coût devient exponentiel.
- **Difficulté générale** : l'inférence exacte dans un réseau discret est NP-difficile, et #P-difficile pour le calcul exact d'une marginale (Murphy cite Dagum et Luby 1993 et Roth 1996). Désaccord d'attribution : la littérature courante cite Cooper (1990, *The computational complexity of probabilistic inference using Bayesian belief networks*) pour la NP-difficulté ; Murphy cite Dagum et Luby, dont le titre porte sur l'**approximation**. Les deux articles n'ont été vus que par leurs métadonnées et par des sources secondaires.
- Dagum et Luby montrent en outre que **approcher** une probabilité à précision relative donnée est lui aussi NP-difficile en général, sans algorithme aléatoire polynomial sauf si NP $\subseteq$ RP ; un algorithme polynomial existe quand les probabilités conditionnelles ne sont pas extrêmes (d'après une page de cours de Princeton, source secondaire).

### Inférence approchée

- Quand la largeur d'arbre est trop grande, trois voies :
  - **propagation de croyances à boucles** (*loopy belief propagation*) : appliquer les messages de l'arbre à un graphe qui a des cycles. Aucune garantie de convergence ; si elle converge, les marginales sont approchées. Dans le cas gaussien, les moyennes sont exactes et les variances trop confiantes (Murphy, §9.4). Murphy, Weiss et Jordan (UAI 1999) rapportent une bonne convergence sur plusieurs réseaux, mais des croyances oscillantes sans lien visible avec les vraies a posteriori sur le réseau diagnostique QMR ;
  - **échantillonnage** : [[MCMC]], Gibbs, échantillonnage préférentiel — voir [[Monte Carlo et inférence variationnelle]] ;
  - **inférence variationnelle**, dont la propagation de croyances est un cas particulier de point fixe (Wainwright et Jordan 2008, vu par ses métadonnées seulement).
- Aucun résultat ne dit laquelle des trois est la meilleure : cela dépend du graphe.

### Apprentissage des paramètres

- **Données complètes** : la vraisemblance et l'a priori se factorisent par nœud, donc l'estimation se fait **nœud par nœud** (Murphy, §4.2.7) :
  $$p(\theta, D) = \prod_i p(\theta_i)\, p(D_i \mid \theta_i).$$
  Le [[Maximum de vraisemblance]] revient à compter des fréquences pour des tables de probabilités discrètes ; une estimation bayésienne avec un a priori de Dirichlet ajoute des pseudo-comptes (voir [[A priori conjugués]]).
- **Données manquantes ou variables latentes** : la factorisation disparaît ; on passe par l'algorithme **EM** (Dempster, Laird, Rubin, 1977, vu par ses métadonnées) ou par l'inférence bayésienne complète.
- Heckerman, Geiger et Chickering (1995) construisent l'a priori sur les paramètres à partir d'un **réseau a priori** et d'une **taille d'échantillon équivalente** $N'$, sous une hypothèse d'équivalence de vraisemblance.

### Apprentissage de structure

- **Par score** : définir un score de graphe et chercher le graphe qui le maximise. Scores courants : BIC, K2, BD / BDe (Cooper et Herskovits ; Heckerman et al.). La métrique BD s'écrit (Chickering 1996, éq. 12.1) :
  $$p(D, B_S) = p(B_S) \prod_{i=1}^{n}\prod_{j=1}^{q_i} \frac{\Gamma(N'_{ij})}{\Gamma(N'_{ij} + N_{ij})} \prod_{k=1}^{r_i} \frac{\Gamma(N'_{ijk} + N_{ijk})}{\Gamma(N'_{ijk})},$$
  où $r_i$ est le nombre d'états du nœud $i$ et $q_i$ le nombre de configurations de ses parents.
- **BIC**, tel qu'il est codé dans pgmpy 1.1.2 : log-vraisemblance moins $\tfrac{\log N}{2} \, q_i (r_i - 1)$ par nœud.
- **Par contraintes** : l'algorithme **PC** teste des indépendances conditionnelles et en déduit le graphe, à l'équivalence de Markov près. Kalisch et Bühlmann (JMLR 2007) en prouvent la cohérence en grande dimension sous une hypothèse de parcimonie (résumé seul lu).
- **Hybrides** : MMHC dans pgmpy, par exemple.
- **Recherche gloutonne** : *hill climbing* sur les graphes ; GES (Chickering 2002, JMLR 3) opère sur les classes d'équivalence et identifie asymptotiquement une carte parfaite si elle existe (résumé seul lu).
- **Le problème est NP-difficile** : Chickering (1996) démontre que chercher la structure de meilleur score est NP-difficile pour tout nombre maximal de parents $K > 1$, par réduction depuis un problème d'ensemble d'arcs de retour. Pour $K = 1$ le problème est polynomial. Heckerman et al. (1995) en tirent des heuristiques (recherche locale, locale itérée, recuit simulé).

## Les maths, simplement

- Réseau bayésien : $p(x) = \prod_i p(x_i \mid x_{\mathrm{pa}(i)})$. Chaque variable ne dépend que de ses parents ; le reste de la loi s'en déduit.
- Champ de Markov : $p(x) = \tfrac1Z \prod_c \psi_c(x_c)$. Chaque clique contribue un facteur ; $Z$ garantit que la somme vaut 1.
- Coût de l'élimination : $\sum_{c} K^{|c|}$ sur les cliques du graphe induit, soit $O(K^{w+1})$ avec $w$ la largeur induite.
- Équivalence de Markov : mêmes squelette et mêmes V non couvertes. Orientation d'une arête qui n'est dans aucune V : indéterminée sans hypothèse supplémentaire.

## En pratique

- **Quand un modèle graphique est le bon choix** : peu de variables nommées et interprétables, de la connaissance d'expert à encoder, des données incomplètes, un besoin de répondre à des questions conditionnelles variées (diagnostic, tableaux de bord de risque). Il perd quand le nombre de variables est grand et que les relations sont continues, non linéaires et sans structure à intégrer.
- **Écrire la structure à la main d'abord** : l'apprentissage de structure est instable et mal identifiable. Un graphe appris sert d'hypothèse à discuter, pas de vérité.
- **Valider la structure par un autre moyen** que le score : stabilité par rééchantillonnage, ou jugement d'expert.
- **Ne pas lire les flèches comme des causes** sans hypothèses supplémentaires : voir [[Inférence causale]].

### En Python

- **pgmpy** (version 1.1.2, 2026-04-30, licence MIT, Python ≥ 3.10 et < 3.15, relevé sur PyPI le 2026-10-02) :
  - modèles : `DiscreteBayesianNetwork`, `DiscreteMarkovNetwork`, `FactorGraph`, `JunctionTree`, `DynamicBayesianNetwork`, `LinearGaussianBayesianNetwork`, `NaiveBayes` (API lue ; les anciens noms `BayesianNetwork` et `MarkovNetwork` sont des alias dépréciés) ;
  - inférence exacte : `VariableElimination` (`query(variables, evidence=None, elimination_order="greedy", …)`, ordres `MinFill`, `MinNeighbors`, `MinWeight`, `WeightedMinFill`), `BeliefPropagation` (par arbre de jonction) ; la variante par passage de messages `BeliefPropagationWithMessagePassing` n'accepte que les graphes **sans boucle** ;
  - approximation : `ApproxInference`, `BayesianModelSampling`, `GibbsSampling` ; aucune propagation de croyances à boucles générique n'a été vue dans la liste des classes ;
  - estimation de paramètres : `MaximumLikelihoodEstimator`, `BayesianEstimator` (a priori `dirichlet`, `BDeu` par défaut, `K2`), `ExpectationMaximization` ;
  - structure : `PC` (variantes `orig`, `stable`, `parallel`), `HillClimbSearch` (scores `k2`, `bdeu`, `bds`, `bic-d`, `aic-d` et leurs variantes gaussiennes), `GES`, `TreeSearch`, `MmhcEstimator`.
  - **Limites relevées** : les scores discrets exigent des variables discrètes (BIC lève une `ValueError` sur des variables continues) ; les valeurs manquantes se codent en `numpy.nan`. Aucune mesure de performance n'a été faite. Pas de brique pgmpy dans le brain.
- **scikit-learn** : `sklearn.covariance.GraphicalLasso` estime une **matrice de précision parcimonieuse** par pénalité $\ell_1$, ce qui revient à apprendre un champ de Markov gaussien (la structure se lit dans les zéros de la précision) ; scikit-learn n'a pas de réseau bayésien général (non vérifié exhaustivement). Voir [[Scikit-Learn]].
- **Programmation probabiliste** : [[PyMC]] et NumPyro expriment un modèle bayésien comme un graphe de variables aléatoires, mais leur documentation sur ce point n'a pas été lue pour cette page.

### Travaux récents

Prépublications des 12 derniers mois, lues au niveau du résumé :

- Zhang, Zhang, Kordjamshidi, Cui — *Bayesian Network Structure Discovery Using Large Language Models* (arXiv 2511.00574, nov. 2025 ; TMLR) : PromptBN produit un DAG complet à partir des seuls noms et métadonnées des variables, ReActBN le raffine avec des scores sur les données ; les auteurs annoncent de meilleurs résultats quand les données sont rares ou absentes.
- Harviainen, Parviainen, Sharma — *Learning Bayesian and Markov Networks with an Unreliable Oracle* (arXiv 2603.09563, mars 2026) : avec un oracle d'indépendance conditionnelle qui se trompe, un réseau bayésien ne tolère **aucune** erreur pour une identification garantie, même à largeur d'arbre bornée ; un champ de Markov en tolère sous une condition de chemins disjoints.
- Ramazi, Kalantari — *Structure Learning for Unfaithful Distributions: The Minimal Dependence Faithfulness* (UAI 2026, PMLR 337) : MD-PC pour les violations de fidélité de type XOR, que PC ne détecte pas.

Aucun article récent sur l'inférence exacte et la largeur d'arbre n'a été retrouvé dans cette recherche : les résultats renvoyaient à des travaux de 2015–2019.

## Approches voisines & alternatives

- [[Inférence bayésienne]] — pose le cadre de l'a posteriori ; un réseau bayésien en est un support de calcul, pas un synonyme.
- [[Découverte causale]] — apprend un graphe à partir des données, avec une lecture causale que ces algorithmes de structure ne garantissent pas ; PC y est le point de contact.
- [[Inférence causale]] — la lecture causale d'un DAG et le calcul des interventions.
- [[Modèles de Markov cachés et filtre de Kalman]] — modèles graphiques à structure en chaîne, avec leurs algorithmes dédiés (avant-arrière, Viterbi, Kalman).
- [[MCMC]] — l'échantillonnage de Gibbs est l'inférence approchée naturelle d'un modèle graphique.
- [[Monte Carlo et inférence variationnelle]] — l'inférence approchée quand la largeur d'arbre est trop grande ; la propagation de croyances est un cas particulier de méthode variationnelle.
- [[Chaînes de Markov]] — le cas d'un graphe linéaire.
- [[Maximum de vraisemblance]] — l'estimation des paramètres, nœud par nœud, avec données complètes.
- [[A priori conjugués]] — l'a priori de Dirichlet des tables de probabilités conditionnelles.
- [[Scikit-Learn]] — `GraphicalLasso` pour un champ de Markov gaussien.
- [[PyMC]] — pour exprimer un modèle bayésien sous forme de programme.

## Pour aller plus loin

- Pearl (1988), *Probabilistic Reasoning in Intelligent Systems*, Morgan Kaufmann — livre non lu ; seule la table des matières a été vue sur une fiche de bibliothèque (réseaux bayésiens et de Markov, propagation par réseau, apprentissage de structure).
- Koller et Friedman (2009), *Probabilistic Graphical Models: Principles and Techniques*, MIT Press — livre non lu ; cité par Murphy et par la documentation de pgmpy. L'année (2009 ou 2010) varie selon les catalogues consultés.
- Lauritzen et Spiegelhalter (1988), *Local computations with probabilities on graphical structures and their application to expert systems*, JRSS B 50(2) : <https://doi.org/10.1111/j.2517-6161.1988.tb01721.x> — métadonnées seules, le scan n'a pas pu être lu.
- Murphy (2023), *Probabilistic Machine Learning: Advanced Topics*, MIT Press : <https://probml.github.io/pml-book/book2.html> — lu en version de travail (chap. 4, 9 et §30.3) ; les numéros de section viennent du PDF de travail, pas de l'édition imprimée.
- Cooper (1990), *The computational complexity of probabilistic inference using Bayesian belief networks*, Artificial Intelligence 42(2-3) : <https://doi.org/10.1016/0004-3702(90)90060-D> — métadonnées seules.
- Chickering (1996), *Learning Bayesian Networks is NP-Complete* : <https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/lns96.pdf> — lu.
- Heckerman, Geiger, Chickering (1995), *Learning Bayesian Networks: The Combination of Knowledge and Statistical Data*, Machine Learning 20(3) : <https://geiger.net.technion.ac.il/files/2016/08/heckerman1995learning.pdf> — lu.
- Verma et Pearl (1990), UAI, *Equivalence and Synthesis of Causal Models* (la page arXiv porte le titre « On the Equivalence of Causal Models ») : <https://arxiv.org/abs/1304.1108> — lu.
- Murphy, Weiss, Jordan (1999), *Loopy Belief Propagation for Approximate Inference: An Empirical Study* : <https://arxiv.org/abs/1301.6725> — résumé seul.
- Kalisch et Bühlmann (2007), *Estimating High-Dimensional DAGs with the PC-Algorithm*, JMLR 8 : <https://jmlr.org/papers/v8/kalisch07a.html> — résumé seul. Chickering (2002), *Optimal Structure Identification With Greedy Search*, JMLR 3 : <https://jmlr.org/papers/v3/chickering02b.html> — résumé seul.
- Uhler, Raskutti, Bühlmann, Yu (2013), *Geometry of the Faithfulness Assumption in Causal Inference*, Ann. Statist. 41(2) : <https://arxiv.org/abs/1207.0547> — résumé seul : l'ensemble des lois qui ne sont pas « fortement fidèles » est, selon le résumé, de mesure non nulle et « étonnamment grande », ce qui limite PC en présence d'erreur d'échantillonnage.
- Reisach, Seiler, Weichwald (2021), *Beware of the Simulated DAG! Causal Discovery Benchmarks May Be Easy To Game*, NeurIPS : <https://arxiv.org/abs/2102.13647> — résumé seul : la variance marginale croît souvent le long de l'ordre causal dans les DAG simulés, et des algorithmes qui l'exploitent échouent après standardisation des données.
- Wainwright et Jordan (2008), *Graphical Models, Exponential Families, and Variational Inference*, Found. Trends ML 1(1-2) — métadonnées seules.
- Documentation : [pgmpy](https://github.com/pgmpy/pgmpy) (dépôt, API et code lus).
- Connexions brain : [[Inférence bayésienne]], [[Découverte causale]], [[Modèles de Markov cachés et filtre de Kalman]], [[MCMC]], [[PyMC]], [[Scikit-Learn]].

### Points ouverts

- Aucun énoncé de Pearl 1988, de Koller et Friedman ni de Lauritzen et Spiegelhalter n'a été lu à la source : ce qui s'en réclame passe par Murphy, pgmpy et Chickering.
- La forme BDeu comme cas particulier $N'_{ijk} = N'/(r_i q_i)$, le BIC de Schwarz (1978) et l'algorithme PC exact (Spirtes, Glymour, Scheines) n'ont pas été confirmés dans une source ouverte.
- Aucune source ouverte ne compare modèles graphiques et réseaux profonds : toute affirmation sur leurs mérites respectifs serait une opinion.
