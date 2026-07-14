---
galaxie: wiki
type: concept
nom: Newton & quasi-Newton
alias: [Newton, Méthode de Newton, Newton-Raphson, quasi-Newton, BFGS, L-BFGS, IRLS]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, second-order]
---

# Newton & quasi-Newton

## Aperçu

- Méthodes du **second ordre** : elles utilisent la courbure (la hessienne) en plus du gradient, $\theta \leftarrow \theta - H^{-1}\nabla f$, ce qui donne une convergence **quadratique** près de l'optimum.
- Beaucoup moins d'itérations que la [[Gradient descent]], mais chaque itération est coûteuse — d'où les variantes quasi-Newton qui approchent $H$.

## Concepts clés

### Pas de Newton
- $\theta_{t+1} = \theta_t - [\nabla^2 f(\theta_t)]^{-1}\,\nabla f(\theta_t)$ : on minimise l'approximation quadratique locale de $f$.
- Invariant à l'échelle des variables (pas de $\eta$ à régler), contrairement à la descente de gradient.

### Coût et limites
- Hessienne : $O(n^2)$ en mémoire, $O(n^3)$ pour l'inversion → impraticable en grande dimension.
- Si $H$ n'est pas définie positive (près d'un [[Loss landscape and saddle points|point-selle]]), le pas peut **remonter** → Newton non fiable hors voisinage convexe.

### Quasi-Newton
- **BFGS** : reconstruit une approximation de $H^{-1}$ à partir des gradients successifs.
- **L-BFGS** : version à mémoire limitée, adaptée aux problèmes à beaucoup de paramètres.
- **IRLS** : Newton appliqué à la log-vraisemblance = moindres carrés repondérés itératifs ([[Régression logistique]], [[GLM]]).

## Les maths, simplement

- Développement de Taylor au 2nd ordre : $f(\theta+\Delta)\approx f+\nabla f^\top\Delta+\tfrac12\Delta^\top H\Delta$ ; annuler la dérivée donne $\Delta=-H^{-1}\nabla f$.
- La hessienne « redresse » la géométrie : Newton voit un problème mal conditionné comme une cuvette ronde, là où la descente de gradient zigzague (cf. [[Convexity]]).

## En pratique

- Idéal : objectifs lisses, convexes, de dimension petite à moyenne (régression logistique, [[GLM]] via IRLS).
- `LogisticRegression` de scikit-learn utilise **L-BFGS** par défaut.
- À éviter sur les réseaux profonds : hessienne trop grande et surface non convexe → on préfère le premier ordre + optimiseurs adaptatifs.
- Outils : `scipy.optimize.minimize(method="BFGS" / "L-BFGS-B" / "Newton-CG")`.

## Approches voisines & alternatives

- [[Gradient descent]] — premier ordre : itérations bon marché, plus nombreuses.
- [[Convexity]] — Newton brille sur les fonctions convexes lisses.
- [[Loss landscape and saddle points]] — la courbure (signe des valeurs propres de $H$) y classe les points critiques.
- [[Régression logistique]] — résolue par IRLS, c'est-à-dire Newton sur la vraisemblance.
- [[Maximum de vraisemblance]] — Newton-Raphson est la méthode classique de maximisation.

## Pour aller plus loin

- Nocedal & Wright — *Numerical Optimization* (BFGS, L-BFGS, régions de confiance).
- Méthodes de région de confiance : alternative robuste quand $H$ n'est pas définie positive.
