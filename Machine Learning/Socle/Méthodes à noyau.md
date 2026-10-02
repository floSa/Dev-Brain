---
role: notion
nom: Méthodes à noyau
alias: [Kernel methods, Méthodes à noyaux, Fonction noyau, Kernel ridge regression, Régression ridge à noyau, KRR, Random Fourier Features, Nyström, RKHS, Neural Tangent Kernel, NTK]
categorie: ml/socle
domaines: [data-sci, ml-eng]
tags: [supervised, non-parametric, regression, classification]
---

# Méthodes à noyau

## Aperçu

- Famille d'algorithmes qui n'ont jamais besoin des coordonnées des points, seulement d'une **mesure de similarité** $k(x, x')$ entre deux points : le noyau. Le modèle devient une somme de similarités à des points d'entraînement.
- Le noyau permet de travailler dans un espace de features très grand, voire de dimension infinie, **sans jamais le construire**. Le prix est déplacé : le coût ne dépend plus de la dimension des features mais du **nombre d'observations** $n$.
- La page [[SVM]] détaille l'astuce du noyau sur la classification à marge ; [[Gaussian Process]] détaille le noyau comme covariance. Ce qui suit est ce que ces deux modèles ont en commun, et ce qu'ils coûtent.

## Concepts clés

### Du noyau à l'espace de features
- Un noyau **défini positif** équivaut à un produit scalaire dans un espace de fonctions : $k(x, x') = \langle \Phi(x), \Phi(x') \rangle$ avec $\Phi(x) = k(\cdot, x)$. Cet espace est un **RKHS** (espace de Hilbert à noyau reproduisant), où $\langle k(\cdot, x), f \rangle = f(x)$ (Schölkopf, Herbrich & Smola, 2001, §1.2).
- L'astuce est ancienne. Aizerman, Braverman et Rozonoer (1964) construisent une fonction séparante comme somme de fonctions $K(x, x^k)$ centrées sur les points d'entraînement, dans un « espace redressant » où elle devient linéaire — c'est la méthode des *fonctions potentielles*. Selon Hofmann, Schölkopf et Smola (2008, §2.3.3), ils s'en servaient dans une preuve de convergence du perceptron, et Boser, Guyon et Vapnik (1992) sont les premiers à en tirer un algorithme d'estimation non linéaire (le SVM).

### Les noyaux usuels
- **Linéaire** : $k(x, x') = \langle x, x' \rangle$. Retombe sur le modèle linéaire, dans sa forme duale.
- **Polynomial** : $(\langle x, x' \rangle + c)^p$ avec $c \ge 0$. Calcule implicitement tous les monômes jusqu'au degré $p$ (Hofmann et al., 2008, §2.2.4).
- **RBF (gaussien)** : $\exp(-\gamma \lVert x - x' \rVert^2)$. Strictement défini positif ; son espace de features est de dimension infinie.
- Les noyaux se **combinent** : somme et produit de noyaux restent des noyaux. La grammaire de composition est détaillée côté [[Gaussian Process]], où elle est le cœur de la modélisation.

### Le théorème de représentation
- Énoncé pour la perte quadratique par Kimeldorf et Wahba (1971), d'après Rasmussen et Williams (2006, §6.2). Généralisé par Schölkopf, Herbrich et Smola (2001, théorème 1) : pour un coût **quelconque** $c$ et une pénalité $g(\lVert f \rVert)$ **strictement croissante**, tout minimiseur de $c\big((x_i, y_i, f(x_i))_{i \le n}\big) + g(\lVert f \rVert)$ s'écrit $f(\cdot) = \sum_{i=1}^n \alpha_i \, k(\cdot, x_i)$.
- Conséquence : un problème posé dans un espace de dimension infinie se réduit à **$n$ coefficients** $\alpha_i$. C'est ce qui rend l'astuce utilisable, et ce qui fixe le coût plus bas : le modèle contient autant de termes que de points.
- La stricte monotonie de $g$ est nécessaire. Sans elle, il existe encore une solution de cette forme, mais plus toutes les solutions (Schölkopf et al., 2001).

### Les modèles
- **SVM / SVR** : perte charnière ou $\varepsilon$-insensible, solution creuse (seuls les vecteurs de support portent un $\alpha_i \neq 0$). Voir [[SVM]].
- **Régression ridge à noyau (KRR)** : perte quadratique, $\hat{\alpha} = (K + \lambda n I)^{-1} y$ (Rudi, Camoriano & Rosasco, 2015, éq. 3-4), résolue en forme fermée.
- La documentation scikit-learn compare les deux : `KernelRidge` ajuste plus vite sous ~1 000 échantillons mais donne un modèle **non creux** (prédiction plus lente), `SVR` ajuste plus lentement et prédit plus vite grâce à la parcimonie.
- **Processus gaussien** : la moyenne prédictive $\bar{f}_* = k_*^\top (K + \sigma_n^2 I)^{-1} y$ est **exactement** celle de la KRR (Rasmussen & Williams, 2006, éq. 2.25) ; le GP y ajoute une variance prédictive. Le noyau y joue le rôle de covariance.

### Ce que le noyau fait à la complexité
- La **matrice de Gram** $K = (k(x_i, x_j))_{ij}$ est $n \times n$ : mémoire $O(n^2)$ pour toute méthode exacte (Rudi et al., 2015).
- Résoudre $(K + \sigma^2 I)^{-1}$ par Cholesky coûte $n^3/6$ opérations (Rasmussen & Williams, 2006, algo. 2.1). Au-delà de $n \approx 10\,000$, stocker la matrice et résoudre le système deviennent prohibitifs sur un poste de travail (Rasmussen & Williams, chap. 8).
- À la prédiction, $f(x) = \sum_i \alpha_i k(x_i, x)$ coûte $O(nd)$ et oblige à **garder les données** (Rahimi & Recht, 2007, §1). Le SVM atténue cela par parcimonie, pas la KRR.
- Le noyau échange donc une dimension d'espace contre une dimension d'échantillon : avantageux quand $d \gg n$, pénalisant quand $n$ explose.

### Approximer le noyau
Deux familles, qui remplacent le noyau par des features **explicites** de dimension modérée, pour réutiliser un modèle linéaire.

- **Random Fourier Features** (Rahimi & Recht, 2007). Pour un noyau invariant par translation, le théorème de Bochner donne $k(x - y) = \mathbb{E}_{\omega \sim p}[e^{j\omega^\top (x - y)}]$ avec $p$ une mesure positive. On tire $D$ fréquences $\omega_i$ et on pose $z(x) = \sqrt{1/D}\,[\cos(\omega_i^\top x), \sin(\omega_i^\top x)]_i$, de sorte que $z(x)^\top z(y) \approx k(x - y)$. Sur un compact, l'erreur uniforme est $\le \varepsilon$ avec forte probabilité dès que $D = \Omega\big((d/\varepsilon^2) \log(\sigma_p \,\mathrm{diam}/\varepsilon)\big)$. L'évaluation coûte alors $O(D + d)$ au lieu de $O(nd)$.
- **Nyström** (Williams & Seeger, 2001). On choisit $m$ points et on pose $\tilde{K} = K_{n,m} K_{m,m}^{-1} K_{m,n}$ ; exacte si $K$ est de rang $m$. Coût $O(m^2 n)$ (contre $n^3$), et $O(p^2 n)$ pour la régression GP avec la formule de Woodbury.
- La documentation scikit-learn expose les deux : `RBFSampler` (features de Fourier, « Random Kitchen Sinks ») est moins précis que `Nystroem` à `n_components` égal mais moins cher, donc utilisable avec plus de composantes ; leur combinaison avec un `SGDClassifier` rend l'apprentissage non linéaire possible sur de grands jeux.

### Noyau, GP et réseaux infiniment larges
- À l'initialisation, un réseau de largeur infinie est un **processus gaussien** (Jacot, Gabriel & Hongler, 2018, prop. 1). Pendant l'entraînement par descente de gradient, la fonction suit le gradient dans l'espace des fonctions pour un nouveau noyau, le **Neural Tangent Kernel** (NTK) ; dans la limite de largeur infinie, ce noyau converge vers un noyau déterministe qui **reste constant** pendant l'entraînement (théorèmes 1 et 2).
- Dans ce régime, entraîner le réseau revient à une régression à noyau. C'est le lien exact entre ce sujet et l'[[Apprentissage profond]].

## Les maths, simplement

- Problème général dans le RKHS $\mathcal{H}$ : $\min_{f \in \mathcal{H}} \; \frac{1}{n}\sum_{i=1}^n \ell\big(y_i, f(x_i)\big) + \lambda \lVert f \rVert_{\mathcal{H}}^2$. La pénalité $\lVert f \rVert^2_{\mathcal{H}}$ est la même idée que la [[Régularisation|régularisation L2]], appliquée aux fonctions plutôt qu'aux coefficients.
- Théorème de représentation : $\hat{f}(x) = \sum_{i=1}^n \alpha_i\, k(x_i, x)$. Les $\alpha_i$ se trouvent par un problème à $n$ inconnues.
- KRR : $\alpha = (K + \lambda n I)^{-1} y$. Le terme $\lambda n I$ conditionne la matrice : sans lui, un noyau très lisse donne une matrice de Gram presque singulière (raisonnement de la page, sans source lue).
- Un noyau est défini positif si toute matrice de Gram est symétrique semi-définie positive ; c'est cette condition, pas la forme de la formule, qui le rend légitime.

## En pratique

- **Standardiser les features** avant tout noyau à distance (RBF) : $\lVert x - x' \rVert$ est dominé par la variable de plus grande amplitude ([[Mise à l'échelle]]).
- **Le noyau et sa largeur sont les vrais hyperparamètres.** `gamma` du RBF, `degree` du polynomial, $\lambda$ ou `C` : à régler ensemble par [[Validation croisée]], voir [[Optimisation d'hyperparamètres]].
- **Repères de taille** (raisonnement de la page, sans source primaire lue pour les seuils exacts) : jusqu'à quelques milliers de points, la méthode exacte est praticable ; vers $10^4$, la matrice de Gram devient le goulot ; au-delà, Nyström ou features de Fourier + modèle linéaire, ou un autre modèle comme un [[Gradient Boosting (GBDT)|GBDT]] sur données en colonnes.
- **Nyström, désaccord entre sources.** Williams et Seeger (2001) concluent qu'un $m \ll n$ suffit sans perte notable sur leurs expériences ; Rasmussen et Williams (2006, §8.3.2) déconseillent la méthode pour de petits $m$ (qualité pauvre, variance prédictive pouvant devenir négative) et lui préfèrent une autre approximation de GP. À lire comme deux contextes différents, pas comme une contradiction résolue.
- **Garanties pour Nyström** : Rudi, Camoriano et Rosasco (2015) montrent qu'à un niveau de sous-échantillonnage bien choisi, il atteint les taux optimaux de la KRR exacte, sous des hypothèses de régularité ; le sous-échantillonnage joue alors le rôle de régularisation. Pour passer à très grande échelle, FALKON (Rudi, Carratino & Rosasco, 2017) annonce $O(n)$ mémoire et $O(n\sqrt{n})$ temps (résumé de l'article seulement, non lu en détail).
- Outils : [[Scikit-Learn]] — `SVC`, `SVR`, `KernelRidge`, `GaussianProcessRegressor`, et dans `sklearn.kernel_approximation` `Nystroem`, `RBFSampler`, `PolynomialCountSketch`.
- Limite structurelle, côté usage : le noyau fixe la représentation avant de voir les données. Un réseau apprend ses features ; le noyau les suppose.

## Limites et débats

- **NTK et apprentissage de features.** Chizat, Oyallon et Bach (2019) montrent que le « lazy training » — où le modèle reste équivalent à sa linéarisation, donc à un apprentissage par noyau — dépend d'un choix de mise à l'échelle. Sur des CNN de vision entraînés dans ce régime, la performance **se dégrade** : il est peu probable, écrivent-ils, que le lazy training soit ce qui explique les succès des réseaux sur les tâches difficiles en grande dimension.
- **Quand un réseau bat un noyau.** Ghorbani, Mei, Misiakiewicz et Montanari (2020) : si les covariables sont presque isotropes, les méthodes RKHS souffrent de la malédiction de la dimension, tandis qu'un réseau peut y échapper en apprenant la meilleure représentation de basse dimension. Les auteurs *font l'hypothèse* d'une telle structure en classification d'images (résumé lu seulement).
- **Interpolation et généralisation.** Belkin, Ma et Mandal (2018) observent que des noyaux interpolants (erreur d'entraînement nulle) généralisent bien, y compris avec des étiquettes bruitées, et prouvent que la norme RKHS d'un interpolant croît presque exponentiellement avec $n$ : les bornes de généralisation classiques fondées sur la norme ne disent alors rien de non trivial. Le sujet rejoint [[Double descente et généralisation des grands modèles]].
- **Travaux récents** (résumés lus uniquement, non vérifiés dans le corps) : St-Arnaud, Carvalho et Farnadi (arXiv:2511.07272, nov. 2025, révisé juin 2026) reviennent sur le NTK en largeur et profondeur grandes ; Li et al. (arXiv:2412.18756, révisé juillet 2026) passent en revue la théorie NTK et ses limites (noyau fixe) et proposent un modèle de séquence gaussienne à features adaptatives. Aucun travail récent propre aux SVM à noyau ou à la KRR n'a été trouvé.

## Approches voisines & alternatives

- [[SVM]] — le modèle à noyau le plus connu : marge, parcimonie, perte charnière.
- [[Gaussian Process]] — même algèbre que la KRR, avec une variance prédictive ; le noyau y est la covariance.
- [[Régularisation]] — la pénalité $\lVert f \rVert^2_{\mathcal{H}}$ est une L2 sur les fonctions ; $\lambda$ en est le poids.
- [[One-Class SVM]] — la même astuce appliquée à la détection de nouveauté.
- [[k-NN]] — l'autre famille de modèles « à similarité » : local et sans apprentissage, là où le noyau est global et régularisé.
- [[Perceptron et MLP]] — le réseau apprend ses features au lieu de les fixer par un noyau ; le NTK est le pont entre les deux.
- [[Attention linéaire]] — remplace le poids d'attention $\exp(q_i^\top k_j)$ par un noyau factorisable $\varphi(q_i)^\top \varphi(k_j)$ : la même idée de features explicites qui évite la matrice $n \times n$.
- [[Gradient Boosting (GBDT)]] — l'alternative dominante sur données en colonnes dès que $n$ est grand.
- [[Scikit-Learn]] — l'implémentation de référence des modèles et des approximations.

## Pour aller plus loin

- Aizerman, Braverman, Rozonoer (1964) — *Theoretical foundations of the potential function method in pattern recognition learning*, Automation and Remote Control 25 : 821-837. Lu en partie (pages 918-921 de l'original russe) : https://www.mathnet.ru/php/getFT.phtml?jrnid=at&paperid=11677&what=fullt&option_lang=eng
- Boser, Guyon, Vapnik (1992) — *A training algorithm for optimal margin classifiers*, COLT, pp. 144-152. https://mlanthology.org/colt/1992/boser1992colt-training/
- Schölkopf, Herbrich, Smola (2001) — *A Generalized Representer Theorem*, COLT. https://alex.smola.org/papers/2001/SchHerSmo01.pdf
- Schölkopf, Smola (2002) — *Learning with Kernels*, MIT Press. **Non ouvert** : cité comme référence de la matière, aucun passage n'en est repris ici.
- Rahimi, Recht (2007) — *Random Features for Large-Scale Kernel Machines*, NIPS 2007. https://papers.nips.cc/paper_files/paper/2007/file/013a006f03dbc5392effeb8f18fda755-Paper.pdf
- Williams, Seeger (2001) — *Using the Nyström Method to Speed Up Kernel Machines*, NIPS 13. https://infoscience.epfl.ch/record/161322/files/nystroem.pdf
- Rudi, Camoriano, Rosasco (2015) — *Less is More: Nyström Computational Regularization*, NIPS. https://papers.neurips.cc/paper_files/paper/2015/file/03e0704b5690a2dee1861dc3ad3316c9-Paper.pdf
- Jacot, Gabriel, Hongler (2018) — *Neural Tangent Kernel: Convergence and Generalization in Neural Networks*, NeurIPS. https://arxiv.org/abs/1806.07572
- Chizat, Oyallon, Bach (2019) — *On Lazy Training in Differentiable Programming*, NeurIPS. https://arxiv.org/abs/1812.07956
- Belkin, Ma, Mandal (2018) — *To understand deep learning we need to understand kernel learning*. https://arxiv.org/abs/1802.01396
- Ghorbani, Mei, Misiakiewicz, Montanari (2020) — *When Do Neural Networks Outperform Kernel Methods?* https://arxiv.org/abs/2006.13409
- Hofmann, Schölkopf, Smola (2008) — *Kernel methods in machine learning*, Annals of Statistics 36(3) : 1171-1220 (synthèse). https://arxiv.org/abs/math/0701907
- Rasmussen, Williams (2006) — *Gaussian Processes for Machine Learning*, MIT Press. https://gaussianprocess.org/gpml/
- Documentation scikit-learn — *Kernel Approximation* et *Kernel ridge regression*. https://scikit-learn.org/stable/modules/kernel_approximation.html
