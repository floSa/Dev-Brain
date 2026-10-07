---
role: notion
nom: Valeurs de Shapley
alias: [Shapley, Shapley value, Shapley values, valeur de Shapley, attribution de Shapley, partage équitable]
categorie: ml/interpretabilite
domaines: [data-sci, ml-eng]
tags: [explainability, game-theory]
---

# Valeurs de Shapley

## Aperçu

- Une valeur de Shapley répond à la question : **dans la décision d'un modèle, combien chaque variable a-t-elle pesé ?** La réponse est un **partage équitable** de l'écart entre la prédiction d'un cas et la prédiction moyenne, calculé comme on partage un gain entre joueurs d'une équipe.
- L'idée vient de la théorie des jeux coopératifs (Shapley, 1953) : le gain de l'équipe est réparti selon la **contribution marginale moyenne** de chaque joueur, sur tous les ordres d'arrivée possibles. Ici, les joueurs sont les variables et le gain est la sortie du modèle.
- Exemple d'usine : un modèle donne un score de risque de panne de 0,80 à un moteur, contre 0,10 en moyenne. Les valeurs de Shapley répartissent ces 0,70 points entre la température, la vibration et le courant.
- Cette page explique le principe. L'usage outillé est dans [[SHAP]], le cadre d'ensemble dans [[Explicabilité des modèles]].

## Concepts clés

### Le jeu : des variables qui rejoignent l'équipe une à une

- Une **coalition** est un sous-ensemble de variables « connues ». Sa valeur $v(S)$ est la sortie attendue du modèle quand seules les variables de $S$ ont la valeur du cas expliqué, les autres restant inconnues (moyennées).
- La contribution d'une variable $i$ est le gain qu'elle apporte en **rejoignant** une coalition : $v(S\cup\{i\})-v(S)$. Elle dépend de ceux qui sont déjà là, donc on la moyenne sur **tous les ordres d'arrivée**.

### Pourquoi « équitable » : quatre propriétés

Shapley (1953) montre que, si l'on exige quatre propriétés, il n'existe qu'une seule répartition :

- **Efficacité** : les parts somment à l'écart total, prédiction du cas moins prédiction moyenne.
- **Symétrie** : deux variables qui jouent le même rôle reçoivent la même part.
- **Variable nulle** : une variable qui n'apporte jamais rien reçoit zéro.
- **Additivité** : pour un modèle somme de deux modèles, la part est la somme des parts.

### Le piège : « $v(S)$ » n'est pas unique

- Il faut décider comment **cacher** les variables hors de $S$. Deux choix courants : les tirer **indépendamment** (valeur dite marginale ou interventionnelle) ou les tirer **conditionnellement** aux variables connues (valeur conditionnelle). Les deux donnent des parts différentes.
- Sundararajan et Najmi (2019) montrent que « les valeurs de Shapley » désignent en pratique **plusieurs méthodes** qui peuvent diverger, jusqu'à créditer une variable que le modèle n'utilise pas. Toute explication par Shapley doit dire **quel $v$** elle emploie.

## Les maths, simplement

- Valeur de Shapley de la variable $i$, avec $F$ l'ensemble des variables : $\phi_i=\sum_{S\subseteq F\setminus\{i\}}\dfrac{|S|!\,(|F|-|S|-1)!}{|F|!}\,\big[v(S\cup\{i\})-v(S)\big]$. Le poids est la part des ordres d'arrivée où $S$ précède exactement $i$.
- Efficacité : $\sum_i\phi_i=v(F)-v(\varnothing)$.
- **Coût** : $2^{|F|}$ coalitions. Avec 3 variables c'est 8 ; avec 40 capteurs, plus d'un millier de milliards. D'où les approximations : échantillonnage de permutations, KernelSHAP, et TreeSHAP, qui exploite la structure des arbres (voir [[SHAP]]). Les articles à l'origine de SHAP rattachent à ce cadre six méthodes d'explication existantes (Lundberg et Lee, 2017).
- **Exemple complet** (valeurs inventées pour l'exemple, calcul de cette page). Moyenne du score : $v(\varnothing)=0{,}10$. Température $T$, vibration $V$, courant $C$.

| Coalition connue | $v$ |
|---|---|
| $\{T\}$ / $\{V\}$ / $\{C\}$ | 0,20 / 0,40 / 0,12 |
| $\{T,V\}$ / $\{T,C\}$ / $\{V,C\}$ | 0,70 / 0,25 / 0,45 |
| $\{T,V,C\}$ | 0,80 |

  Moyenne des gains marginaux sur les 6 ordres d'arrivée : $\phi_T\approx0{,}222$, $\phi_V\approx0{,}422$, $\phi_C\approx0{,}057$. Somme : $0{,}70=0{,}80-0{,}10$. La vibration pèse le plus, mais la température compte beaucoup plus qu'un regard isolé ne le suggère : seule, elle ajoute 0,10, avec la vibration déjà là elle ajoute 0,30.

## En pratique

- **Un outil, pas un calcul à la main** : [[SHAP]] (TreeSHAP exact pour les arbres de [[XGBoost]] ou [[LightGBM]]), [[Captum]] pour les réseaux.
- **Local puis global.** Chaque part explique un cas ; la moyenne des valeurs absolues sur beaucoup de cas donne une importance globale.
- **Capteurs corrélés : la part se répartit entre eux.** Deux capteurs jumeaux reçoivent chacun une partie ; regrouper les capteurs redondants avant d'attribuer. Le sujet est traité pour la détection d'anomalies dans [[Expliquer une anomalie (contribution des capteurs)]].
- **Ce n'est pas une cause.** Les parts décrivent **le modèle**, pas la machine. Une part élevée pour la température ne dit pas que chauffer la machine provoque la panne ; Kumar et al. (2020) détaillent les problèmes mathématiques et d'usage quand on lit ces valeurs comme une importance de variable, et pointent le besoin d'un raisonnement causal.
- **Une explication a un coût de calcul** : en exploitation, expliquer seulement les alertes plutôt que tous les points.

## Approches voisines & alternatives

- [[SHAP]] — la bibliothèque de référence qui calcule ces valeurs.
- [[Explicabilité des modèles]] — le cadre : Shapley, LIME, importance par permutation, locales ou globales.
- [[LIME]] — approximation locale par un modèle simple, sans garantie d'équité des parts.
- [[Attribution par gradient]] — pour les réseaux, utiliser la dérivabilité au lieu de perturber (Integrated Gradients).
- [[Expliquer une anomalie (contribution des capteurs)]] — Shapley appliqué au score d'un détecteur d'anomalies.
- [[Inférence causale]] — le cadre à employer quand la question est « que se passe-t-il si on agit ? ».

## Pour aller plus loin

- Shapley (1953), *A value for n-person games*, in Kuhn et Tucker (éd.), *Contributions to the Theory of Games II*, Princeton University Press, 307-317 (référence confirmée par recherche, texte non relu).
- Lundberg, Lee (2017), *A Unified Approach to Interpreting Model Predictions*, NeurIPS 2017 : https://arxiv.org/abs/1705.07874 (page de résumé lue)
- Sundararajan, Najmi (2019), *The many Shapley values for model explanation*, arXiv : https://arxiv.org/abs/1908.08474 (page de résumé lue)
- Kumar, Venkatasubramanian, Scheidegger, Friedler (2020), *Problems with Shapley-value-based explanations as feature importance measures*, ICML 2020 : https://arxiv.org/abs/2002.11097 (page de résumé lue)
