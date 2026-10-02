---
role: notion
nom: Modèles de Markov cachés et filtre de Kalman
alias: [HMM, hidden Markov model, modèle de Markov caché, Kalman filter, filtre de Kalman, state-space model, modèle à espace d'états, modèle d'état latent, Baum-Welch, Viterbi, forward-backward, EKF, UKF, extended Kalman filter, unscented Kalman filter, particle filter, filtre particulaire, RTS smoother, lisseur de Kalman, HSMM, linear Gaussian state-space model, LGSSM]
categorie: stats/probabilite
domaines: [data-sci]
tags: [stochastic-process, markov, forecasting]
---

# Modèles de Markov cachés et filtre de Kalman

## Aperçu

- Deux modèles pour la même situation : un **état qu'on ne voit pas** évolue dans le temps, et on n'en observe que des **mesures bruitées**. Le but est de reconstituer l'état, de prédire ou d'apprendre le modèle.
- **HMM** : l'état est **discret** (régime, phonème, mode de panne). **Filtre de Kalman** : l'état est **continu**, la dynamique linéaire et les bruits gaussiens (position et vitesse d'un mobile, niveau d'une série).
- Les deux sont des cas d'un même cadre, le **modèle à espace d'états** : un processus de Markov caché plus une loi d'observation (Doucet et Johansen le nomment *general state space hidden Markov model*).
- Filtrer, c'est calculer la loi de l'état **maintenant** sachant les mesures passées ; lisser, c'est la calculer avec **aussi** les mesures futures.

## Concepts clés

### Modèle à espace d'états

- Un **état latent** $x_t$ suit une dynamique de Markov : $x_t$ ne dépend que de $x_{t-1}$.
- Une **observation** $y_t$ dépend seulement de $x_t$ (bruit de mesure).
- Cette double hypothèse (Markov sur l'état, indépendance conditionnelle des mesures) est ce qui rend les calculs **récursifs** : un pas coûte la même chose quelle que soit la longueur de l'historique. Voir [[Chaînes de Markov]] pour la partie « état » seule.

### HMM : les trois problèmes (Rabiner, 1989)

Un HMM est $\lambda = (A, B, \pi)$ : matrice de transition, lois d'émission, loi initiale. Rabiner pose trois problèmes, cadrage qu'il attribue à Jack Ferguson :

1. **Évaluation** : calculer $P(O \mid \lambda)$. Algorithme *forward*.
2. **Décodage** : trouver la séquence d'états la plus probable. Algorithme de **Viterbi**. Rabiner insiste : il n'y a pas de « bonne » séquence, seulement des critères.
3. **Apprentissage** : ajuster $\lambda$ pour maximiser $P(O \mid \lambda)$. Algorithme de **Baum-Welch**.

- **Forward** : coût $O(N^2 T)$ pour $N$ états et $T$ pas, contre un ordre $2TN^T$ pour l'énumération directe. Rabiner donne l'exemple $N=5$, $T=100$ : environ 3 000 opérations contre $10^{72}$.
- **Viterbi** : même structure que le forward, avec un **max** à la place de la **somme**, et des pointeurs pour remonter le chemin.
- **Baum-Welch** : c'est l'algorithme **EM** appliqué au HMM (Rabiner : les équations sont « essentiellement identiques » aux étapes EM). La vraisemblance **croît à chaque itération** ou l'on est sur un point critique.

### Filtre de Kalman

- Modèle **linéaire gaussien** : $x_k = A x_{k-1} + q_{k-1}$, $y_k = H x_k + r_k$, avec bruits gaussiens $q \sim \mathcal N(0, Q)$, $r \sim \mathcal N(0, R)$.
- Le filtre alterne **prédiction** (propager l'état et son incertitude par la dynamique) et **mise à jour** (corriger avec la mesure, d'autant plus que la mesure est fiable).
- Särkkä (2013) : dans ce cas, le filtre est la solution **exacte**, sous forme fermée, de l'équation de filtrage bayésien — la loi de l'état reste gaussienne à chaque pas.
- Kalman (1960) : l'estimée est optimale si les processus sont gaussiens ; sinon elle reste le meilleur estimateur **linéaire** au sens de l'erreur quadratique. Il note lui-même qu'il est difficile de savoir dans quelle mesure un processus physique est gaussien.
- **Lisseur de Rauch-Tung-Striebel** : passe arrière qui corrige les estimations filtrées avec les mesures futures ; l'équivalent du *backward* pour le HMM.

### Extensions non linéaires

- **EKF** (filtre de Kalman étendu) : linéarise dynamique et mesure autour de l'estimée par un développement de Taylor (jacobiennes). Särkkä : les jacobiennes sont « sources d'erreurs et difficiles à déboguer », et le filtre ne convient pas aux non-linéarités marquées. Wan et van der Merwe (2000) signalent que l'erreur de linéarisation peut dégrader l'estimée, voire faire diverger le filtre.
- **UKF** (filtre de Kalman unscented) : propage quelques **points sigma** à travers la fonction non linéaire au lieu de la linéariser ; pas de jacobienne, pas de dérivabilité requise, coût un peu supérieur à l'EKF.
- **Filtre particulaire** (algorithme SIR chez Särkkä) : $N$ échantillons pondérés, rééchantillonnés ; ni linéarité ni gaussianité. Coût plus élevé ; souffre de **dégénérescence** (presque tous les poids tendent vers 0 sans rééchantillonnage) puis d'appauvrissement quand le bruit de dynamique est faible. Doucet et Johansen : tout algorithme SMC qui dépend de trajectoires complètes échoue pour $n$ assez grand à $N$ fini.
- **Désaccord entre sources sur la précision de l'UKF**, laissé tel quel : Wan et van der Merwe écrivent que moyenne et covariance sont captées « précisément jusqu'à l'ordre 3 » du développement de Taylor pour toute non-linéarité ; Särkkä écrit que la moyenne est exacte pour les polynômes jusqu'à l'ordre 3, mais que la **covariance** n'est exacte que jusqu'à l'ordre 1 (comme le filtre à linéarisation statistique). Les deux se concilient si l'on distingue moyenne et covariance, ce que Wan et van der Merwe ne font pas dans leur résumé.

## Les maths, simplement

- HMM, récursion *forward* : $\alpha_t(j) = \Big[\sum_i \alpha_{t-1}(i)\, a_{ij}\Big]\, b_j(o_t)$, et $P(O \mid \lambda) = \sum_j \alpha_T(j)$. La somme sur les états précédents est la source du coût $O(N^2)$ par pas.
- Viterbi : $\delta_t(j) = \big[\max_i \delta_{t-1}(i)\, a_{ij}\big]\, b_j(o_t)$.
- Durée d'un état dans un HMM : $p_i(d) = a_{ii}^{\,d-1}(1 - a_{ii})$ — une loi **géométrique**. Rabiner la juge inadaptée à la plupart des signaux physiques et décrit le HMM à durée variable.
- Kalman, prédiction : $m_k^- = A\, m_{k-1}$, $P_k^- = A P_{k-1} A^\top + Q$.
- Kalman, mise à jour (Särkkä, Thm 4.2) : $v_k = y_k - H m_k^-$, $S_k = H P_k^- H^\top + R$, $K_k = P_k^- H^\top S_k^{-1}$, $m_k = m_k^- + K_k v_k$, $P_k = P_k^- - K_k S_k K_k^\top$. $K_k$ est le **gain** : grand quand la mesure est fiable ($R$ petit), petit sinon.
- La covariance $P_k$ ne dépend **pas** des observations : elle peut être calculée à l'avance.

## En pratique

- **Baum-Welch trouve un maximum local.** Rabiner et Dempster, Laird, Rubin le disent : la vraisemblance monte, mais pas forcément jusqu'à l'optimum global. Lancer plusieurs initialisations aléatoires et garder le meilleur score (le tutoriel de `hmmlearn` le recommande). Pour des émissions en mélange continu, l'initialisation est « essentielle » (Rabiner).
- **Nombre d'états** : pas de règle générale dans les sources lues. Cartella et al. (2015) emploient l'AIC. Un état de trop se paie en optima locaux et en paramètres.
- **Hypothèses fortes** : HMM d'ordre 1 et durées géométriques ; Kalman linéaire et gaussien. Quand elles cassent : HMM semi-markovien (durée libre), EKF / UKF / particulaire, ou modèles appris.
- **Régimes en séries temporelles** : Hamilton (1989) modélise les paramètres d'une autorégression comme issus d'un processus de Markov à états discrets (application au PNB américain). Voir [[Stationarity]] pour la raison d'être des changements de régime.
- **Suivi** : un filtre de Kalman prédit où sera chaque piste (modèle de mouvement, souvent à vitesse constante) ; voir [[Suivi d'objets]].
- **Maintenance prédictive** : Liu et al. (2013) notent qu'un HMM seul sait détecter et diagnostiquer mais pas prédire l'état de santé futur, et le combinent à un autre modèle ; Cartella et al. (2015) emploient un HMM semi-markovien pour prévoir le temps jusqu'à une panne (résumé seulement lu). Aucune revue de littérature n'a pu être ouverte ici.
- **Détection d'anomalies** (raisonnement, non appuyé par une source lue) : un état latent permet de signaler une mesure improbable sachant l'état prédit, c'est-à-dire une innovation $v_k$ trop grande devant $S_k$ ; voir [[Time series anomaly detection]].

### En Python

- `hmmlearn` (0.3.3, 2024-10-31) : `GaussianHMM`, `GMMHMM`, `CategoricalHMM`, `PoissonHMM`… ; README « limited-maintenance mode ».
- `statsmodels` (0.15.0) : le module `tsa.statespace` expose le modèle $y_t = Z_t \alpha_t + d_t + \varepsilon_t$, $\alpha_{t+1} = T_t \alpha_t + c_t + R_t \eta_t$ et s'appuie sur le filtre de Kalman pour la vraisemblance ; `SARIMAX` et `UnobservedComponents` (niveau, tendance, saison, cycle) en dérivent ; `MarkovRegression` implémente le filtre de Hamilton pour les régimes, `MarkovAutoregression` n'a pas de stabilité d'API garantie selon sa doc.
- `filterpy` : dernière version 1.4.5 en 2018, dernier commit en 2022, 86 tickets ouverts — peu maintenu ; compatibilité avec les versions actuelles de numpy non testée ici.
- `pykalman` (0.11.2, 2026-01-31) : Kalman, UKF et EM ; repris en publication depuis 2024.
- `dynamax` (1.0.2, 2026-06-25) : HMM et modèles linéaires gaussiens en JAX, dans un même cadre.
- `pomegranate` (1.1.2) : HMM sur PyTorch ; le README et le code ne s'accordent pas sur la disponibilité de Viterbi, non tranché.

### Travaux récents

Deux prépublications lues au niveau du résumé :

- Brady, Nüsken, Li — *Efficient Learning of Deep State Space Models via Importance Smoothing* (arXiv 2605.21108, ICML 2026) : méthode PVMC, annoncée 10 fois plus rapide que l'approche SMC concurrente la plus rapide.
- Zhang, Ni, Shlezinger, Wang — *Change-Aware Self-Adaptive AI-Aided Kalman Filters With Neural Change Point Detection* (arXiv 2607.13387) : filtre de Kalman assisté par réseau (KalmanNet), adaptation en ligne aux changements de modèle.

Ne pas confondre ces **modèles d'état profonds** avec les « state-space models » à la mode des architectures séquentielles (S4, Mamba, tag `state-space-model` du brain) : même vocabulaire, même idée d'état latent récurrent, mais le filtre n'y est pas bayésien.

## Approches voisines & alternatives

- [[Chaînes de Markov]] — la partie « état » seule, observée directement ; le HMM y ajoute une observation bruitée.
- [[Suivi d'objets]] — l'usage le plus courant du filtre de Kalman en vision : prédiction de la position de chaque piste.
- [[Time series anomaly detection]] — détecter une mesure improbable ; l'innovation du filtre ou la vraisemblance d'un HMM en sont des scores possibles.
- [[MCMC]] — pour les modèles où le filtrage exact est impossible et où l'on veut la loi a posteriori complète sur les paramètres.
- [[Inférence bayésienne]] — le filtre de Kalman est de l'inférence bayésienne récursive, exacte dans le cas linéaire gaussien.
- [[Markov Decision Process]] — chaîne de Markov enrichie d'actions et de récompenses, le cadre du reinforcement learning ; l'état y est observé, contrairement au HMM.
- [[Stationarity]] — un HMM à régimes est une réponse à une série non stationnaire.
- [[statsmodels]] — `tsa.statespace` et régimes de Markov.
- [[pmdarima]] — AutoARIMA qui enveloppe `SARIMAX` de statsmodels, donc ajusté par filtre de Kalman.
- [[darts]] — propose un `KalmanFilter` dans `darts.models.filtering`.
- [[Modèles graphiques probabilistes]] — le HMM en est le cas particulier à structure de chaîne ; la page décrit les graphes généraux.

## Pour aller plus loin

- Rabiner (1989), *A tutorial on hidden Markov models and selected applications in speech recognition*, Proc. IEEE 77(2):257–286 : <https://www.cs.cmu.edu/~cga/behavior/rabiner1.pdf>
- Kalman (1960), *A new approach to linear filtering and prediction problems*, J. Basic Engineering 82(1):35–45 : <https://www.cs.yale.edu/homes/yry/readings/general/Kalman1960.pdf>
- Dempster, Laird, Rubin (1977), *Maximum likelihood from incomplete data via the EM algorithm*, JRSS B 39(1) : <https://cs.brown.edu/courses/csci1820/spring-2022/resources/Dempster_Laird_Rubin_1977.pdf>
- Särkkä (2013), *Bayesian Filtering and Smoothing*, Cambridge UP (version en ligne de l'auteur) : <https://users.aalto.fi/~ssarkka/pub/cup_book_online_20131111.pdf>
- Murphy, *Machine Learning: A Probabilistic Perspective* (MIT Press, 2012), chap. 17 (HMM) et 18 (modèles à espace d'états) ; *Probabilistic Machine Learning: Advanced Topics* (2023), chap. 29 — seules les tables des matières ont été lues.
- Wan & van der Merwe (2000), *The unscented Kalman filter for nonlinear estimation* : <https://groups.seas.harvard.edu/courses/cs281/papers/unscented.pdf> ; Doucet & Johansen, *A tutorial on particle filtering and smoothing: fifteen years later* : <https://www.stats.ox.ac.uk/~doucet/doucet_johansen_tutorialPF2011.pdf>
- Hamilton (1989), Econometrica 57(2):357–384 — résumé seulement ; Baum et al. (1970), Viterbi (1967), Gordon, Salmond, Smith (1993) : non ouverts, cités via Rabiner, Dempster-Laird-Rubin et Särkkä.
- Liu et al. (2013), *A hybrid LSSVR/HMM-based prognostic approach*, Sensors : <https://pmc.ncbi.nlm.nih.gov/articles/PMC3690014/> ; Cartella et al. (2015), *Hidden semi-Markov models for predictive maintenance* : <https://doi.org/10.1155/2015/278120>
- Connexions brain : [[Chaînes de Markov]], [[Suivi d'objets]], [[Time series anomaly detection]], [[statsmodels]], [[pmdarima]], [[darts]].
