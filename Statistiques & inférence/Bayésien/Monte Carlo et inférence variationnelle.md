---
role: notion
nom: Monte Carlo et inférence variationnelle
alias: [Monte Carlo et inférence variationnelle, Monte Carlo, méthodes de Monte Carlo, inférence variationnelle, variational inference, VI, ELBO, evidence lower bound, champ moyen, mean field, CAVI, ADVI, échantillonnage préférentiel, importance sampling, échantillonnage par rejet, rejection sampling, reparameterization trick, astuce de reparamétrisation, SVI, BBVI, PSIS, Pareto smoothed importance sampling]
categorie: stats/bayesien
domaines: [data-sci]
tags: [monte-carlo, bayesian, probabilistic-programming, statistical-inference]
---

# Monte Carlo et inférence variationnelle

## Aperçu

- Deux familles pour la même tâche : **calculer une espérance ou une loi a posteriori** quand l'intégrale n'a pas de forme fermée. Monte Carlo **simule** la cible ; l'inférence variationnelle (VI) la **remplace** par la meilleure approximation d'une famille choisie, en résolvant un problème d'optimisation.
- [[MCMC]] est un Monte Carlo à échantillons dépendants. Cette page couvre ce qui l'entoure : Monte Carlo simple, échantillonnage préférentiel, rejet, et l'alternative variationnelle.
- Le compromis est connu : la simulation est **asymptotiquement exacte** mais coûteuse ; la VI est **rapide** et passe à l'échelle, mais son erreur est fixée par la famille choisie et ne diminue pas avec le temps de calcul.
- Les concepts d'information (divergence de Kullback-Leibler) sont dans [[KL divergence]] ; la VI par rétropropagation est le moteur d'entraînement des [[Autoencodeurs]] variationnels.

## Concepts clés

### Monte Carlo simple

- Estimer $\mu = \mathbb E[f(X)]$ par la moyenne $\hat\mu_n = \frac1n\sum_i f(X_i)$ sur des tirages indépendants.
- Estimateur **sans biais**, d'erreur quadratique moyenne $\sigma^2/n$, soit une erreur en $O(n^{-1/2})$ (Owen, chap. 2). La [[Loi des grands nombres]] garantit la convergence, le [[Théorème central limite]] donne la loi de l'erreur.
- La dimension $d$ n'apparaît pas dans $\sigma/\sqrt n$ : c'est l'intérêt du Monte Carlo en grande dimension, là où une quadrature classique voit son erreur se dégrader (Owen cite $O(n^{-4/d})$ pour la règle de Simpson).
- Revers : un chiffre décimal de plus coûte **100 fois** plus de tirages.
- Condition : une variance finie. Pour des queues lourdes, l'estimateur converge mal ou pas ; c'est la question des moments finis que l'échantillonnage préférentiel rend visible (voir plus bas).

### Échantillonnage par rejet

- Disposer d'une densité $g$ facile à simuler et d'une constante $c$ avec $f \le c\,g$ ; proposer $y \sim g$ et l'accepter avec probabilité $f(y)/(c\,g(y))$ (Owen, chap. 4).
- Probabilité d'acceptation globale $1/c$ : il faut en moyenne $c$ propositions par tirage retenu. Marche avec des densités non normalisées.
- Impossible si $\sup f/g = \infty$ (Owen, §9.5), cas où l'échantillonnage préférentiel reste utilisable, avec une variance éventuellement élevée.
- Raisonnement propre à cette page, non sourcé : cible $\mathcal N(0, I_d)$ et proposition $\mathcal N(0, \sigma^2 I_d)$ avec $\sigma > 1$ donnent $c = \sigma^d$ ; le coût croît donc **exponentiellement** avec la dimension. À vérifier avant de s'en servir ailleurs.

### Échantillonnage préférentiel

- Idée : tirer sous une loi $q$ facile et **repondérer** pour corriger : $\mu = \mathbb E_q[f(X)\,p(X)/q(X)]$, de poids $w = p/q$. Il faut $q > 0$ partout où $p > 0$.
- Quand $p$ n'est connue qu'à une constante près (le cas d'un a posteriori), on utilise l'estimateur **auto-normalisé** :
  $$\hat\mu_q = \frac{\sum_i f(X_i)\,w_u(X_i)}{\sum_i w_u(X_i)}, \qquad w_u = p_u / q_u,\ X_i \sim q.$$
  Les constantes inconnues se simplifient, au prix d'un léger biais.
- **Taille d'échantillon effective** : $n_e = \dfrac{(\sum_i w_i)^2}{\sum_i w_i^2}$ (Owen, éq. 9.13, attribuée à Kong 1992). Elle chute quand quelques poids dominent.
- **Piège de la grande dimension.** Owen (ex. 9.3) montre que, pour $p = \mathcal N(0, I)$ et $q = \mathcal N(0, \sigma^2 I)$, une faible différence de variance suffit à produire un rapport de poids extrême quand $d$ est grand. Vehtari et al. (JMLR 2024) notent que l'échantillonnage préférentiel peut échouer même lorsque les rapports ont une variance finie, et illustrent l'effondrement de l'ESS avec $D$ de 1 à 1024.
- **PSIS** (Pareto smoothed importance sampling, Vehtari, Simpson, Gelman, Yao, Gabry) : ajuster une loi de Pareto généralisée à la queue des plus grands poids, les remplacer par les statistiques d'ordre attendues, et lire la forme de la queue $\hat k$ comme diagnostic. Seuil d'alerte $\hat k > \min(1 - 1/\log_{10} S, 0{,}7)$, soit 0,7 dès $S > 2000$ tirages.
- Interprétation de $\hat k < 0{,}7$ (même article) : l'échantillon est indiscernable de celui d'une loi ayant plus de $1/0{,}7 \approx 1{,}4$ moments fractionnaires finis. Autour de $0{,}7$, il faut environ dix fois plus de tirages pour diviser l'erreur par deux.

### Quand MCMC échoue ou devient trop lent

- **Volume de données** : chaque pas exige la vraisemblance de tout le jeu de données. La VI stochastique opère sur des sous-échantillons ; Blei et al. citent un cas à un milliard de documents.
- **Exploration de nombreux modèles** : un a posteriori variationnel s'obtient en quelques minutes là où un MCMC prend des heures. Yao et al. (2018) rapportent, sur une régression à 7129 variables et 72 observations avec a priori « horseshoe », quelques minutes pour ADVI et plusieurs heures pour NUTS.
- **Géométries difficiles** : l'entonnoir des modèles hiérarchiques, les modes multiples (permutations d'étiquettes dans un mélange). La VI n'y est pas automatiquement meilleure : voir la section sur les diagnostics, où ce même exemple de régression sort avec $\hat k = 9{,}8$ (mode manqué).
- **Avant l'une ou l'autre**, regarder s'il faut vraiment approcher : [[A priori conjugués]] donnent l'a posteriori exact, et [[Estimation MAP]] un point à moindre coût.

### Inférence variationnelle : le principe

- Choisir une famille $\mathcal Q$ de lois faciles et chercher $q^* = \arg\min_{q \in \mathcal Q} \mathrm{KL}\big(q(z) \,\|\, p(z \mid x)\big)$. La divergence est prise **dans ce sens** (Blei, Kucukelbir, McAuliffe, éq. 1).
- Cette KL n'est pas calculable (elle contient l'évidence $p(x)$). On maximise à la place la **borne inférieure de l'évidence**, l'**ELBO** :
  $$\mathrm{ELBO}(q) = \mathbb E_q[\log p(z, x)] - \mathbb E_q[\log q(z)] = \mathbb E_q[\log p(x \mid z)] - \mathrm{KL}\big(q(z)\,\|\,p(z)\big).$$
- Identité : $\log p(x) = \mathrm{KL}\big(q \,\|\, p(z \mid x)\big) + \mathrm{ELBO}(q)$. Maximiser l'ELBO revient donc à minimiser la KL, et l'ELBO borne $\log p(x)$ par le bas.
- La seconde forme se lit : **ajuster les données** (terme de vraisemblance) tout en **restant proche de l'a priori** (terme de KL).

### Champ moyen et CAVI

- **Champ moyen** : $q(z) = \prod_j q_j(z_j)$, les facteurs étant indépendants.
- **CAVI** (coordinate ascent VI) : mettre à jour un facteur à la fois, $q_j^*(z_j) \propto \exp\{\mathbb E_{-j}[\log p(z_j \mid z_{-j}, x)]\}$ (Blei et al., éq. 17). Chaque pas fait monter l'ELBO.
- L'ELBO est **non convexe** : CAVI converge vers un optimum local qui dépend de l'initialisation.
- **Conséquence connue** : le champ moyen **sous-estime la variance** de l'a posteriori, par construction de l'objectif (Blei et al., §1 ; Wang et Titterington 2005, cités). Pour une gaussienne bidimensionnelle corrélée, les variances marginales du champ moyen sont plus petites que les vraies. Les auteurs précisent que ce n'est pas toujours gênant pour la prédiction.

### VI par rétropropagation

- **Stochastic VI** (Hoffman et al. 2013, cité par Blei et al.) : gradient naturel et optimisation stochastique sur des sous-échantillons.
- **Estimateur par score** (REINFORCE) : $\nabla_\phi \mathbb E_{q_\phi}[f(z)] = \mathbb E_{q_\phi}[f(z)\,\nabla_\phi \log q_\phi(z)]$. Général, mais Kingma et Welling le jugent de variance très élevée et impraticable tel quel ; Black Box VI (Ranganath, Gerrish, Blei) en est la déclinaison à variance contrôlée (résumé seul lu).
- **Reparamétrisation** (Kingma et Welling, 2014) : écrire $z = g_\phi(\epsilon, x)$ avec $\epsilon \sim p(\epsilon)$ indépendant de $\phi$. Alors
  $$\nabla_\phi \mathbb E_{q_\phi}[f(z)] = \mathbb E_{p(\epsilon)}\big[\nabla_\phi f(g_\phi(\epsilon, x))\big],$$
  un gradient qui traverse l'échantillonnage et se calcule par rétropropagation. Cas gaussien : $z = \mu + \sigma \odot \epsilon$. Limite : suppose une variable continue reparamétrisable.
- **VI amortie** : au lieu d'un $q$ par point, un réseau d'inférence $q_\phi(z \mid x)$ valable pour tout $x$. C'est le **VAE** (voir [[Autoencodeurs]]) : une même ELBO sert de fonction de perte.
- **ADVI** (Kucukelbir, Tran, Ranganath, Gelman, Blei, JMLR 2017) automatise le tout pour tout modèle différentiable en quatre temps :
  1. transformer les paramètres vers un **espace non contraint**, $\zeta = T(\theta)$, avec le jacobien de la transformation ;
  2. poser une gaussienne : **champ moyen** (covariance diagonale) ou **rang plein** ;
  3. standardiser par une transformation elliptique pour obtenir un gradient reparamétré, l'entropie gaussienne étant analytique ;
  4. monter le gradient de l'ELBO, par ascension stochastique à pas adaptatif ; un seul échantillon par pas suffit en pratique.
- Les auteurs notent que le champ moyen sous-estime les variances marginales, que le rang plein suit mieux, et que la précision de la moyenne domine la précision prédictive.

### Diagnostiquer une approximation variationnelle

- **L'ELBO ne dit pas si l'approximation est bonne.** Sa constante est inconnue et change avec la reparamétrisation ; comparer deux ELBO n'a pas de sens, et un ELBO plus haut peut accompagner un ajustement moins bon (Yao et al. 2018, §1 et §4.2).
- **$\hat k$ de PSIS** appliqué au rapport $r_s = p(\theta_s, y) / q(\theta_s)$, $\theta_s \sim q$ (Yao et al. 2018) : si $q$ est proche de la cible, les poids sont proches de 1.
  - $\hat k < 0{,}5$ : $q$ proche de la vérité, le théorème central limite s'applique à l'estimateur repondéré ;
  - $0{,}5 \le \hat k \le 0{,}7$ : $q$ imparfaite mais utile ;
  - $\hat k > 0{,}7$ : fiabilité perdue ; reparamétrer, itérer plus, ou passer à MCMC.
  Lien avec les divergences de Rényi : pour $k > 0{,}5$, $\chi^2(p \| q) = \infty$ ; pour $k > 1$, $\mathrm{KL}(p \| q) = \infty$.
- Exemple « huit écoles » : l'entonnoir entre $\mu$ et $\log\tau$ n'est pas capté par une gaussienne ($\hat k = 1{,}00$ en paramétrisation centrée) ; la version non centrée donne $\hat k = 0{,}64$.
- **VSBC** (variational simulation-based calibration) : tirer $\theta^{(0)}_j$ de l'a priori, simuler un jeu de données, ajuster $q_j$, et vérifier que les probabilités $\Pr_{\theta \sim q_j}(\theta_i < \theta^{(0)}_{ij})$ sont symétriques autour de 0,5. Une asymétrie à droite ou à gauche trahit un biais positif ou négatif. Il évalue la performance **moyenne** du point central sur le modèle, pas sur un jeu de données précis ; il suppose le modèle bien spécifié.
- **Sensibilité à l'arrêt** : Yao et al. montrent qu'élargir la tolérance relative de l'ELBO de $10^{-5}$ à $0{,}01$ (défaut d'ADVI) fait passer $\hat k$ à 4,4 ; une « fausse convergence ».
- Limite des deux diagnostics : $\hat k$ ne voit pas les modes que $q$ n'a pas visités (Yao et al., §5).
- Côté MCMC, les diagnostics sont ceux de [[MCMC]] : $\hat R$, ESS, divergences, via [[ArviZ]].

## Les maths, simplement

- Erreur Monte Carlo : $\mathrm{RMSE}(\hat\mu_n) = \sigma / \sqrt n$.
- Préférentiel auto-normalisé : $\hat\mu_q = \sum_i \tilde w_i f(X_i)$ avec $\tilde w_i = w_i / \sum_j w_j$ et $\mathrm{ESS} = 1 / \sum_i \tilde w_i^2$.
- Densité préférentielle optimale pour l'estimateur auto-normalisé : $q \propto |f - \mu|\,p$ ; pour l'estimateur non normalisé : $q \propto |f|\,p$ (Owen, §9.2). Elle dépend de $\mu$, qu'on ne connaît pas : un guide de conception, pas une recette.
- ELBO : $\log p(x) - \mathrm{KL}(q \,\|\, p(z\mid x))$. Sens de la KL : $\mathrm{KL}(q\|p)$ pénalise un $q$ qui met de la masse là où $p$ n'en a pas, et tolère un $q$ qui néglige un mode de $p$. D'où les approximations **trop étroites** et le risque de manquer un mode (raisonnement standard, non tiré d'une source lue ici).
- Gradient reparamétré avec $z = \mu + \sigma\epsilon$ : $\partial_\mu f(z) = f'(z)$ et $\partial_\sigma f(z) = f'(z)\,\epsilon$.

## En pratique

- **Choisir** : un modèle de taille moyenne dont l'incertitude compte → MCMC (NUTS) via [[PyMC]] ou [[Stan]] ; un gros jeu de données, une exploration rapide, ou un a posteriori amorti → VI, à valider par $\hat k$ ou par comparaison avec un MCMC de référence sur un sous-échantillon.
- **Outils** (versions relevées sur PyPI/GitHub le 2026-10-02) :
  - [[PyMC]] 6.3.2 (2026-09-08) : `pymc.fit(n=10000, method='advi')` ; méthodes `'advi'`, `'fullrank_advi'`, `'svgd'`, `'asvgd'` ; retourne une `Approximation`.
  - [[Stan]] / CmdStan 2.40.0 (2026-09-16) : `variational` avec `algorithm=meanfield|fullrank`, `iter=10000`, `tol_rel_obj=0.01` par défaut ; **Pathfinder** en alternative.
  - NumPyro 0.22.0 (2026-09-18) : `SVI(model, guide, optim, loss)`, auto-guides (`AutoNormal`, `AutoMultivariateNormal`, `AutoIAFNormal`…) ; `Trace_ELBO` ne gère que les variables à échantillonneur reparamétré.
- **Désaccord à noter dans la documentation de Stan** : le guide CmdStan classe ADVI comme algorithme expérimental (« may be unstable or buggy »), alors que la page ADVI du manuel de référence lue ne porte pas cet avertissement. Le manuel présente Pathfinder comme meilleur qu'ADVI sur la plupart des modèles de PosteriorDB, tout en notant qu'il demande davantage de tests.
- **Pathfinder** (Zhang, Carpenter, Gelman, Vehtari, arXiv:2108.03782, résumé seul lu) : qualité meilleure qu'ADVI et comparable à de courtes chaînes HMC, avec un à deux ordres de grandeur d'évaluations en moins.
- **Habitude saine** : ne jamais conclure sur un a posteriori variationnel sans $\hat k$ ou un contrôle croisé, et regarder les **variances marginales** (sous-estimées) avant les moyennes.
- **Seuil de convergence** : abaisser `tol_rel_obj` et vérifier que $\hat k$ ne change pas ; le défaut (0,01) a produit une fausse convergence dans l'exemple de Yao et al.

### Travaux récents

Prépublications des 12 derniers mois, lues au niveau du résumé :

- Odgers, Riegler, Swaroop, Fortuin — *Gaussian Mean Field Variational Inference can Overestimate Predictive Variance* (arXiv 2606.25745, juin 2026) : le champ moyen sous-estime la variance des paramètres, mais peut sur-estimer la variance prédictive dans les directions où les données se concentrent.
- Liu et Li — *Bend to Mend: Toward Trustworthy Variational Bayes with Valid Uncertainty Quantification* (arXiv 2512.22655, décembre 2025) : recalibrage des intervalles de crédibilité variationnels, en spécifiant volontairement mal la vraisemblance pour obtenir une couverture fréquentiste valide.
- Yin et Jiao — *Using Variational Inference to Improve the Efficiency of MCMC Algorithms* (arXiv 2606.29205, juin 2026) : une transformation issue d'une VI gaussienne pour préconditionner HMC.
- Parra-Aldana et Sosa — VI pour modèles linéaires hiérarchiques (arXiv 2512.12857, décembre 2025) : les méthodes variationnelles y déforment la dépendance a posteriori et rendent WAIC et DIC instables.

Ces quatre références n'ont pas été lues au-delà de leur résumé. Aucune synthèse récente sur les méthodes de Monte Carlo séquentielles n'a été retrouvée dans cette recherche : le sujet n'est pas couvert ici.

## Approches voisines & alternatives

- [[MCMC]] — la simulation par chaîne de Markov ; exact à la limite, c'est la référence contre laquelle se juge la VI.
- [[KL divergence]] — la mesure que minimise la VI, dans le sens $\mathrm{KL}(q\|p)$.
- [[Autoencodeurs]] — le VAE est une VI amortie entraînée par rétropropagation.
- [[Inférence bayésienne]] — le cadre : l'a posteriori que les deux familles approchent.
- [[A priori conjugués]] — a posteriori exact, sans simulation ni optimisation, quand le couple le permet.
- [[Estimation MAP]] — un point au lieu d'une loi ; le moins cher, au prix de toute l'incertitude.
- [[Loi des grands nombres]] et [[Théorème central limite]] — ce qui justifie l'estimateur Monte Carlo et mesure son erreur.
- [[Prédiction conforme]] — une garantie de couverture sur les prédictions sans hypothèse sur l'a posteriori. Rapprochement propre à cette page, sans source lue : une approximation variationnelle suspecte n'invalide pas cette garantie, qui ne dépend pas du modèle.
- [[PyMC]], [[Stan]], [[ArviZ]] — les moteurs et le diagnostic.

## Pour aller plus loin

- Metropolis, Rosenbluth, Rosenbluth, Teller, Teller (1953), *Equation of State Calculations by Fast Computing Machines*, J. Chem. Phys. 21(6):1087–1092 : <https://doi.org/10.1063/1.1699114> — métadonnées vues, texte non lu.
- Hastings (1970), *Monte Carlo sampling methods using Markov chains and their applications*, Biometrika 57(1):97–109 : <https://doi.org/10.1093/biomet/57.1.97> — résumé vu, texte non lu.
- Owen, *Monte Carlo theory, methods and examples* (livre en ligne, chap. 2, 4 et 9 lus) : <https://artowen.su.domains/mc/>
- Blei, Kucukelbir, McAuliffe (2017), *Variational Inference: A Review for Statisticians*, JASA 112(518):859–877 : <https://arxiv.org/abs/1601.00670>
- Kingma et Welling (2014), *Auto-Encoding Variational Bayes*, ICLR : <https://arxiv.org/abs/1312.6114> — la mention « ICLR 2014 » vient d'un dépôt institutionnel, la page arXiv ne donne pas de venue.
- Kucukelbir, Tran, Ranganath, Gelman, Blei (2017), *Automatic Differentiation Variational Inference*, JMLR 18(14) : <https://arxiv.org/abs/1603.00788>
- Yao, Vehtari, Simpson, Gelman (2018), *Yes, but Did It Work?: Evaluating Variational Inference*, ICML, PMLR 80:5581–5590 : <https://arxiv.org/abs/1802.02538>
- Vehtari, Simpson, Gelman, Yao, Gabry (2024), *Pareto Smoothed Importance Sampling*, JMLR 25(72) : <https://arxiv.org/abs/1507.02646>
- Ranganath, Gerrish, Blei, *Black Box Variational Inference* : <https://arxiv.org/abs/1401.0118> (résumé seul).
- Documentation : [PyMC `pm.fit`](https://www.pymc.io/projects/docs/en/stable/api/generated/pymc.fit.html), manuel Stan et guide CmdStan sur ADVI et Pathfinder, [NumPyro SVI](https://num.pyro.ai/en/stable/svi.html).
- Connexions brain : [[MCMC]], [[KL divergence]], [[Autoencodeurs]], [[Inférence bayésienne]], [[PyMC]], [[Stan]], [[ArviZ]].
