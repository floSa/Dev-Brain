---
galaxie: wiki
type: concept
nom: Attribution par gradient
alias: [Saliency, Saliency map, Carte de saillance, Integrated Gradients, IntegratedGradients, SmoothGrad, InputxGradient, Grad-CAM, GradientShap, Attribution methods]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [explainability, deep-learning]
---

# Attribution par gradient

## Aperçu

- Famille de méthodes qui répond à « quelle partie de l'entrée a pesé sur cette sortie ? » en exploitant le fait qu'un réseau est **dérivable** : le gradient de la sortie par rapport à l'entrée dit, localement, ce qui la ferait bouger.
- C'est le pendant **par gradient** des méthodes par perturbation ([[Explicabilité des modèles|SHAP, LIME]]) : au lieu de perturber l'entrée des milliers de fois, on rétropropage **une fois**. Beaucoup plus rapide, mais réservé aux modèles dérivables et à boîte ouverte.

## Concepts clés

### L'intuition, et sa naïveté
- **Saliency** (Simonyan, 2013), la version brute : $\partial y / \partial x$. Grand gradient = pixel/token important.
- Trois défauts immédiats. Le gradient est **local** — il ne dit que ce qui se passe à un cheveu de l'entrée. Il est **bruité** — deux entrées voisines donnent des cartes très différentes. Et il **sature** : si un neurone ReLU est déjà à fond, son gradient est nul alors que la feature est décisive.

### Le problème de saturation
- Le cas d'école : un modèle détecte « chat » avec une confiance de 0,99. Le gradient au point observé est ≈ 0 — pas parce que rien ne compte, mais parce que le modèle est déjà au plafond et que rien ne peut plus le faire bouger.
- Toute la famille cherche à contourner ça. C'est ce qui distingue les méthodes entre elles.

### Integrated Gradients — la réponse principale
- L'idée : ne pas regarder le gradient **au point**, mais l'**accumuler le long d'un chemin** entre une baseline (l'absence de signal : image noire, tokens de padding) et l'entrée réelle.
- On traverse ainsi la zone où le modèle n'était pas encore saturé, et l'on capte la contribution réelle. Coût : 20 à 300 passes au lieu d'une — toujours bien moins que les méthodes par perturbation.
- Sa force est axiomatique : c'est **la seule** méthode de chemin qui satisfait simultanément *sensibilité* et *invariance d'implémentation*, et ses attributions **somment exactement** à $f(x) - f(\text{baseline})$ (complétude).

### Le choix de la baseline est un choix de modèle
- Point sous-estimé : Integrated Gradients répond toujours à « important **par rapport à quoi ?** ». Une image noire comme baseline rend les pixels noirs invisibles par construction.
- Il n'existe pas de baseline neutre. C'est une hypothèse de l'analyste, à assumer et à documenter.

### SmoothGrad — contre le bruit
- Bruiter l'entrée $n$ fois, moyenner les cartes obtenues. Le gradient est bruité localement ; la moyenne sur un voisinage le stabilise. Se combine avec les autres (SmoothGrad + IG).
- Variantes : **VarGrad** et **SquareGrad** agrègent la variance ou le carré plutôt que la moyenne.

### La famille, et ce que chacune corrige

| Méthode | Le geste | Ce qu'elle corrige | Coût |
|---|---|---|---|
| **Saliency** | $\partial y/\partial x$ | — (la baseline naïve) | 1 passe |
| **InputxGradient** | $x \odot \partial y/\partial x$ | Pondère par l'amplitude du signal | 1 passe |
| **Integrated Gradients** | Gradients cumulés sur un chemin | **La saturation** | 20-300 passes |
| **SmoothGrad** | Moyenne sur entrées bruitées | **Le bruit** des cartes | $n$ passes |
| **GradientShap** | IG + baselines échantillonnées | Saturation + arbitraire de la baseline | $n$ passes |
| **Grad-CAM** | Gradients au niveau d'une couche conv | Cartes lisibles pour la vision ([[CNN]]) | 1 passe |

## Les maths, simplement

- Saliency : $A_i(x) = \dfrac{\partial f(x)}{\partial x_i}$ — la dérivée de la sortie par rapport à la $i$-ème composante de l'entrée. Une rétropropagation suffit.
- Integrated Gradients : $\text{IG}_i(x) = (x_i - x'_i) \times \displaystyle\int_{\alpha=0}^{1} \frac{\partial f\big(x' + \alpha(x - x')\big)}{\partial x_i} \, d\alpha$, où $x'$ est la baseline.
  - Lecture : on avance de la baseline vers l'entrée, on relève le gradient à chaque pas, on fait la moyenne, on multiplie par le déplacement total. L'intégrale s'approche par une somme de Riemann sur 20 à 300 pas.
- **Complétude** — la propriété qui fait sa valeur : $\sum_i \text{IG}_i(x) = f(x) - f(x')$. Les attributions se somment exactement à l'écart de prédiction, exactement comme les valeurs de Shapley. Ce n'est pas un hasard : IG est l'analogue continu de Shapley (*Aumann-Shapley*).
- SmoothGrad : $\tilde{A}(x) = \frac{1}{n}\sum_{j=1}^{n} A(x + \epsilon_j)$, avec $\epsilon_j \sim \mathcal{N}(0, \sigma^2)$.

## En pratique

- **Ne jamais utiliser Saliency brut** pour conclure. C'est la baseline pédagogique du domaine, pas un outil. Integrated Gradients est le défaut raisonnable.
- **Toujours expliciter la baseline.** Une attribution IG sans mention de sa baseline est ininterprétable — et le lecteur ne saura pas à quoi il compare.
- **Vérifier la convergence de l'intégrale** : si $\sum_i \text{IG}_i \ne f(x) - f(x')$ à quelques pourcents près, le nombre de pas est insuffisant. Ce contrôle est gratuit et presque toujours oublié.
- **Gradient ≠ perturbation.** Le gradient dit ce qui *ferait bouger* le modèle localement ; SHAP/LIME disent ce qui se passe *si on retire* la feature. Deux questions différentes — les désaccords entre les deux ne sont pas des bugs.
- **Attribution ≠ causalité, et attribution ≠ correction.** Une carte de saillance montre où le modèle regarde, pas s'il a raison. Des travaux ont montré que certaines cartes restent inchangées quand on randomise les poids du modèle — un test de cohérence à faire ([[Explicabilité des modèles]]).
- **Sur du texte**, les attributions par token sont trompeuses quand la tokenisation découpe les mots : agréger au niveau du mot avant de montrer quoi que ce soit ([[Tokenization]]).
- Outils : [[Dev/Services/Captum|Captum]] (la référence PyTorch, toute la famille), [[Dev/Services/interpreto|interpreto]] (côté modèles de langage, gradient **et** perturbation sous une API commune, avec les métriques d'insertion/suppression).

## Approches voisines & alternatives

- [[Explicabilité des modèles]] — le chapeau, et les méthodes par perturbation (SHAP, LIME, permutation) qui répondent à la même question autrement.
- [[Probing]] — l'autre versant : ce que le modèle **encode**, plutôt que ce qui a pesé sur une prédiction.
- [[Interprétabilité mécaniste]] — l'étape d'après : comprendre le **mécanisme**, pas seulement pondérer l'entrée.
- [[Gradient descent]] — le même gradient, employé pour apprendre au lieu d'expliquer.
- [[CNN]] — le terrain d'origine des cartes de saillance (Grad-CAM).
- [[Métriques vision]] — pour évaluer une carte d'attribution face à une vérité terrain de segmentation.
- [[Calibration]] — une attribution sur un modèle mal calibré explique une confiance qui n'a pas de sens.

## Pour aller plus loin

- Simonyan, Vedaldi, Zisserman (2013) — *Deep Inside Convolutional Networks* : les cartes de saillance d'origine.
- Sundararajan, Taly, Yan (2017) — *Axiomatic Attribution for Deep Networks* : Integrated Gradients et ses axiomes.
- Smilkov et al. (2017) — *SmoothGrad: removing noise by adding noise*.
- Adebayo et al. (2018) — *Sanity Checks for Saliency Maps* : la critique salutaire, et les tests de randomisation.
