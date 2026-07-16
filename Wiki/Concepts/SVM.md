---
galaxie: wiki
type: concept
nom: SVM
alias: [Support Vector Machine, Machine à vecteurs de support, Séparateur à vaste marge, SVC, SVR, Astuce du noyau, Kernel trick]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, classification, regression]
---

# SVM

## Aperçu

- Modèle supervisé qui sépare deux classes par l'hyperplan **le plus éloigné possible des points des deux camps** : on ne cherche pas n'importe quelle frontière valide, on cherche celle qui laisse la plus large marge de sécurité.
- Seuls les points situés sur la marge — les **vecteurs de support** — définissent la frontière. Les autres peuvent disparaître sans rien changer. C'est ce qui rend le modèle économe et robuste à petit $n$.

## Concepts clés

### La marge
- Parmi une infinité d'hyperplans séparant deux classes, celui qui maximise la distance aux points les plus proches généralise le mieux : il est le moins susceptible de basculer si un nouveau point arrive.
- Cette distance est la **marge**. Les points qui la touchent sont les vecteurs de support ; ils sont typiquement une petite fraction du jeu.

### Marge souple — le paramètre `C`
- Des données réelles ne sont jamais parfaitement séparables. On autorise des violations, pénalisées par `C`.
- `C` **grand** → on tolère peu d'erreurs, la marge se rétrécit et épouse les données : variance élevée, surapprentissage. `C` **petit** → on accepte des erreurs, la marge s'élargit et se lisse : biais élevé. C'est le curseur [[Compromis biais-variance|biais-variance]] du modèle.

### L'astuce du noyau
- Des données non séparables par une droite peuvent le devenir dans un espace de plus grande dimension. Plutôt que d'y projeter explicitement (coûteux, parfois infini), on remarque que l'algorithme n'a **jamais besoin des coordonnées** — seulement des produits scalaires entre points.
- Un **noyau** $K(x, x')$ calcule directement ce produit scalaire dans l'espace cible, sans jamais s'y rendre. C'est l'astuce : la puissance d'une dimension infinie au prix d'un calcul entre deux points.

### Les noyaux usuels
- **Linéaire** — pas de projection. Le défaut sur texte et sur $d \gg n$, où les données sont déjà séparables.
- **RBF (gaussien)** — le plus courant. Frontières souples et locales, contrôlées par `gamma`.
- **Polynomial** — interactions d'ordre `degree` ; plus rare, plus instable à régler.

### Le paramètre `gamma` (noyau RBF)
- `gamma` fixe la **portée d'influence d'un point**. Grand `gamma` → influence très locale, la frontière se contorsionne autour de chaque point (surapprentissage). Petit `gamma` → influence large, la frontière se rapproche d'une droite (sous-apprentissage).
- `C` et `gamma` interagissent fortement : ils se règlent **ensemble**, en grille, jamais l'un après l'autre.

### Régression — SVR
- Même principe retourné : au lieu d'écarter les points de la frontière, on cherche un tube de largeur `epsilon` qui **contient** un maximum de points. Les erreurs à l'intérieur du tube ne coûtent rien ; seuls les points hors tube sont pénalisés.

## Les maths, simplement

- Problème à marge souple : $\min_{w, b} \; \frac{1}{2}\lVert w \rVert^2 + C \sum_{i=1}^{n} \xi_i$ sous contrainte $y_i(w^\top x_i + b) \ge 1 - \xi_i$, avec $\xi_i \ge 0$ les violations tolérées. Minimiser $\lVert w \rVert^2$ **est** maximiser la marge : celle-ci vaut $2 / \lVert w \rVert$.
- La formulation duale ne fait intervenir que des produits scalaires $x_i^\top x_j$ — d'où la substitution $x_i^\top x_j \to K(x_i, x_j)$, qui est toute l'astuce du noyau.
- Noyau RBF : $K(x, x') = \exp\big(-\gamma \lVert x - x' \rVert^2\big)$. La similarité décroît exponentiellement avec la distance ; $\gamma$ règle la vitesse de cette décroissance. Il correspond à un espace de projection de **dimension infinie**.
- La perte sous-jacente est la *hinge loss* $\max(0, 1 - y \hat{f}(x))$ : nulle dès qu'un point est du bon côté avec une marge suffisante. C'est pourquoi les points bien classés et éloignés n'influencent pas le modèle.

## En pratique

- **Standardiser est obligatoire, pas optionnel.** Le noyau repose sur $\lVert x - x' \rVert$ : une variable de grande amplitude écrase toutes les autres et le modèle devient absurde. C'est l'erreur n°1 sur les SVM ([[Mise à l'échelle]]).
- **Complexité entre $O(n^2)$ et $O(n^3)$** : au-delà de ~100 000 observations, un SVM à noyau devient impraticable. Passer à `LinearSVC` / `SGDClassifier`, ou à un [[Gradient Boosting (GBDT)|GBDT]].
- Le terrain où il brille : **$d \gg n$** (texte, génomique, spectres) et petits jeux propres. La marge maximale y contrôle naturellement la variance là où les arbres surapprennent.
- Régler `C` et `gamma` **conjointement**, en grille logarithmique (`C` et `gamma` ∈ $\{10^{-3} … 10^{3}\}$), par [[Validation croisée|validation croisée]] ([[Optimisation d'hyperparamètres]]).
- **Pas de probabilités natives.** `probability=True` lance en interne une calibration de Platt par CV — coûteuse et parfois médiocre. Si les probabilités comptent, préférer une [[Régression logistique]], ou calibrer explicitement ([[Calibration]]).
- Multiclasse par décomposition seulement (*one-vs-rest* / *one-vs-one*) : ce n'est pas natif, et le coût grimpe avec le nombre de classes.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.svm]] — `SVC` (noyau), `LinearSVC` (linéaire, passe à l'échelle), `SVR`. Toujours dans un `Pipeline` avec `StandardScaler`.

## Approches voisines & alternatives

- [[Régression logistique]] — même frontière linéaire, mais probabilités natives et calibrées ; à préférer quand on a besoin de scores interprétables.
- [[k-NN]] — l'autre modèle à distance : local et sans apprentissage, là où le SVM est global et optimisé.
- [[Gradient Boosting (GBDT)]] — le concurrent qui gagne sur tabulaire dès que $n$ est grand et les données sales.
- [[Random Forest]] — plus robuste sans réglage, mais moins bon en très grande dimension.
- [[Régularisation]] — le terme $\lVert w \rVert^2$ du SVM **est** une pénalité L2 ; `C` en est l'inverse de $\lambda$.
- [[Classification]] — le chapeau de la tâche.
- [[Types de données et choix de modèle]] — quand le SVM est le bon choix.

## Pour aller plus loin

- Cortes & Vapnik (1995) — *Support-Vector Networks* : l'article fondateur de la marge souple.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 12.
- Documentation scikit-learn — *Support Vector Machines* : les pièges d'échelle et de complexité y sont explicites.
