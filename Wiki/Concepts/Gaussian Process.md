---
galaxie: wiki
type: concept
nom: Gaussian Process
alias: [GP, Processus gaussien, Régression par processus gaussien, GaussianProcessRegressor, Krigeage, Kriging]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, regression, bayesian, non-parametric]
---

# Gaussian Process

## Aperçu

- Modèle bayésien non paramétrique qui ne cherche pas *une* fonction, mais définit une **distribution sur les fonctions** : à chaque prédiction il rend une moyenne **et** un écart-type — l'incertitude est native, pas bricolée après coup.
- Sa propriété décisive : il **sait qu'il ne sait pas**. Loin des points observés, l'incertitude prédite s'élargit d'elle-même. C'est ce qui en fait le moteur de l'[[Optimisation d'hyperparamètres|optimisation bayésienne]] : pour explorer intelligemment, il faut savoir où l'on est ignorant.

## Concepts clés

### Une distribution sur les fonctions
- Définition : un processus gaussien est un ensemble de variables aléatoires dont **toute** collection finie suit une loi normale multivariée. Autrement dit, tirer une fonction au hasard revient à tirer un vecteur gaussien.
- Le prior est décrit par une fonction de moyenne (souvent nulle) et une fonction de **covariance** — le noyau. Observer des points *conditionne* cette distribution : le posterior passe exactement par les observations et s'évase entre elles.

### Le noyau **est** le modèle
- C'est toute la modélisation. Le noyau encode l'hypothèse « deux entrées proches donnent des sorties proches », et sa forme dicte ce que le GP peut représenter.
- **RBF** : fonctions infiniment lisses — l'hypothèse par défaut, souvent trop optimiste. **Matérn** : rugosité réglable via $\nu$ ($\nu = 3/2$ ou $5/2$ en pratique), plus réaliste sur données physiques. **Périodique** : saisonnalité. **Linéaire** : tendance.
- Les noyaux **s'additionnent et se multiplient** : `RBF + Périodique` modélise « tendance lisse + cycle ». C'est une grammaire, et c'est là que se joue le métier.

### Le fléau : $O(n^3)$
- L'inférence exige d'inverser une matrice $n \times n$ : $O(n^3)$ en temps, $O(n^2)$ en mémoire. **La limite structurelle du modèle.**
- En pratique : confortable jusqu'à ~2 000 points, pénible vers 10 000, impossible au-delà sans approximation (méthodes à points d'induction, GP sparses).
- C'est la raison pour laquelle un GP ne remplacera jamais un [[Gradient Boosting (GBDT)|GBDT]] sur un jeu tabulaire ordinaire — et pourquoi sa niche est le **petit $n$ coûteux**.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `kernel` | Le prior sur les fonctions | **Le vrai choix de modélisation.** Tout se joue ici |
| `length_scale` (du noyau) | Distance sur laquelle la fonction varie | ↓ = fonction nerveuse, surapprentissage ; ↑ = fonction plate |
| `alpha` | Bruit ajouté à la diagonale | ↑ = tolère du bruit d'observation ; sert aussi de garde-fou numérique |
| `nu` (Matérn) | Rugosité | 1/2 = très rugueux (Ornstein-Uhlenbeck), ∞ = RBF lisse |
| `n_restarts_optimizer` | Redémarrages de l'optimisation | ↑ = évite les optima locaux de la vraisemblance. **À monter, le défaut 0 est un piège** |
| `normalize_y` | Centre-réduit la cible | `True` si la cible n'est pas centrée — le prior de moyenne nulle sinon fausse tout |

- Particularité agréable : les hyperparamètres du noyau **s'apprennent** en maximisant la vraisemblance marginale, pas par [[Validation croisée|CV]]. Le modèle règle sa propre complexité.

## Les maths, simplement

- Prior : $f \sim \mathcal{GP}\big(m(x), \, k(x, x')\big)$ — une moyenne et un noyau suffisent à tout définir.
- Noyau RBF : $k(x, x') = \sigma^2 \exp\left(-\dfrac{\lVert x - x' \rVert^2}{2 \ell^2}\right)$, où $\ell$ est la *length-scale*. Deux points distants de bien plus que $\ell$ sont considérés indépendants.
- Prédiction (posterior), le cœur du modèle : $\mu_* = K_*^\top (K + \sigma_n^2 I)^{-1} y$ et $\sigma_*^2 = k_{**} - K_*^\top (K + \sigma_n^2 I)^{-1} K_*$.
  - La **moyenne** $\mu_*$ est une combinaison linéaire des observations, pondérée par la similarité au point à prédire — un [[k-NN]] pondéré, en somme.
  - La **variance** $\sigma_*^2$ ne dépend **pas de $y$**, seulement de *où* sont les points. D'où le fait que l'incertitude s'élargisse mécaniquement loin des observations : c'est de la géométrie, pas de la statistique sur les valeurs.
- L'inversion de $(K + \sigma_n^2 I)$, matrice $n \times n$, est le $O(n^3)$.
- Vraisemblance marginale : $\log p(y \mid X) = -\frac{1}{2} y^\top (K + \sigma_n^2 I)^{-1} y - \frac{1}{2}\log|K + \sigma_n^2 I| - \frac{n}{2}\log 2\pi$. Le premier terme récompense l'ajustement, le second **pénalise la complexité** — un rasoir d'Ockham automatique.

## En pratique

- **La niche : petit $n$, évaluations coûteuses, incertitude nécessaire.** Optimisation bayésienne d'hyperparamètres, plans d'expériences, calibration de simulateurs, géostatistique (où on l'appelle **krigeage**, son nom d'origine minière).
- **Standardiser entrées et sortie** : les *length-scales* sont des distances, donc sensibles aux échelles ; et le prior de moyenne nulle rend `normalize_y=True` presque obligatoire ([[Mise à l'échelle]]).
- **Le choix du noyau prime sur tout le reste.** Le défaut RBF suppose une fonction infiniment lisse — hypothèse rarement vraie sur données réelles. **Matérn 5/2 est un meilleur défaut** dans la plupart des cas.
- **Monter `n_restarts_optimizer`** (5 à 10) : la vraisemblance marginale a des optima locaux, et le défaut à 0 laisse le modèle sur son point de départ. Piège classique.
- **Se dégrade en grande dimension** : au-delà de ~20 variables, les distances se concentrent et le noyau perd son pouvoir discriminant — même mal que [[k-NN]].
- **Ne pas confondre avec [[Gaussian Mixture Models (GMM)]]** : le nom se ressemble, tout le reste diffère. GP = régression supervisée sur des fonctions ; GMM = clustering non supervisé par mélange de lois.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.gaussian_process]] (`GaussianProcessRegressor`, `GaussianProcessClassifier`, catalogue de noyaux composables) ; [[Dev/Services/Optuna|Optuna]] et [[Dev/Services/Hyperopt|Hyperopt]] l'emploient sous le capot pour l'optimisation bayésienne ; [[Dev/Services/PyMC|PyMC]] et [[Dev/Services/Stan|Stan]] pour une modélisation bayésienne complète.

## Approches voisines & alternatives

- [[Optimisation d'hyperparamètres]] — son débouché principal : le GP est le modèle de substitution de l'optimisation bayésienne.
- [[Inférence bayésienne]] — le cadre général : prior sur les fonctions, posterior après observation.
- [[k-NN]] — la moyenne d'un GP est un voisinage pondéré par le noyau ; même parenté, même faiblesse en grande dimension.
- [[SVM]] — l'autre méthode à noyau, mais fréquentiste et sans incertitude.
- [[Régression]] — le chapeau de la tâche.
- [[Régression quantile]] — l'autre façon d'obtenir de l'incertitude, sans hypothèse gaussienne ni coût cubique.
- [[Gradient Boosting (GBDT)]] — ce qu'on utilise dès que $n$ dépasse quelques milliers.
- [[Bootstrap]] — l'alternative non paramétrique pour quantifier l'incertitude d'un modèle quelconque.
- [[Mouvement brownien]] — un processus gaussien particulier, vu côté probabilités.

## Pour aller plus loin

- Rasmussen & Williams (2006) — *Gaussian Processes for Machine Learning* : la référence, disponible librement en ligne.
- Duvenaud — *The Kernel Cookbook* : comment lire, composer et choisir un noyau. Le complément indispensable.
- Documentation scikit-learn — *Gaussian Processes*, et l'exemple *GPR with noise-level estimation*.
