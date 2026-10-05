---
role: notion
nom: Stock de sécurité et taux de service
alias: [safety stock, service level, taux de service, fill rate, taux de remplissage, cycle service level, stock tampon]
categorie: math/recherche-operationnelle
domaines: [data-sci]
tags: [inventory, probability, forecasting, statistical-inference]
---

# Stock de sécurité et taux de service

## Aperçu

- Le **stock de sécurité** (SS) est la quantité tenue **au-dessus** de la demande attendue pendant le délai de réapprovisionnement, pour absorber ce que la prévision n'a pas vu : l'aléa de la demande et, le cas échéant, celui du délai.
- Il se fixe à partir d'un **objectif de service**. Deux objectifs portent le même mot « taux de service » et ne mesurent pas la même chose : la **probabilité de ne pas tomber en rupture** pendant un cycle, et la **part de la demande servie depuis le stock**. Les confondre est l'erreur la plus fréquente.
- Le calcul courant s'écrit $SS = z\,\sigma$. Le point qui décide de sa justesse n'est pas $z$ mais $\sigma$ : c'est l'écart-type de l'**erreur de prévision** sur le délai, pas celui de la demande brute.
- Le stock de sécurité est le coussin du point de commande d'une politique [[Politiques de réapprovisionnement (s,S) et (R,Q)|(s,S) ou (R,Q)]]. Sur une seule période, le même quantile est le fractile critique du [[Modèle du vendeur de journaux (newsvendor)|vendeur de journaux]].
- Les indicateurs qui *constatent* le service après coup (rotation, couverture, taux de rupture) sont dans [[Indicateurs de stock (rotation, couverture, rupture)]].

## Concepts clés

### Ce que le stock de sécurité couvre

- Point de commande : $R = \hat\mu_{LT} + SS$, où $\hat\mu_{LT}$ est la demande **prévue** sur le délai. Le stock de sécurité n'est que l'écart de précaution.
- Pendant le délai, le risque est de commander trop tard par rapport à ce qui arrive. Pas d'aléa, pas de stock de sécurité : si la prévision était exacte, $SS = 0$.
- Il couvre deux sources : la demande qui s'écarte de la prévision, et un délai fournisseur qui varie.

### Taux de service cyclique (« type 1 », $\alpha$)

- Probabilité qu'**aucune rupture** ne survienne pendant un cycle de réapprovisionnement : $\alpha = \mathbb P(D_{LT} \le R)$. L'anglais dit *cycle service level* (CSL).
- Il compte les **cycles** sans rupture, pas les **unités** manquantes. Une rupture d'une unité et une rupture de mille pèsent pareil.
- Avec une demande normale, $SS = z_\alpha\,\sigma_{LT}$ où $z_\alpha = \Phi^{-1}(\alpha)$, $\Phi$ étant la fonction de répartition de la loi normale centrée réduite. Définition reprise par la page [Wikipedia *Safety stock*](https://en.wikipedia.org/wiki/Safety_stock) (source secondaire).

### Taux de remplissage (« type 2 », $\beta$, *fill rate*)

- Part de la **demande servie immédiatement** depuis le stock : $\beta = 1 - \dfrac{\text{demande non servie}}{\text{demande totale}}$. Rossi, Kilic et Tarim (2011) rappellent la forme « un moins l'espérance du rapport rupture totale / demande totale sur l'horizon ».
- C'est ce que la plupart des clients ressentent : une rupture courte et rare passe, une rupture massive non.
- Le même $z$ donne des $\beta$ très différents selon la taille de lot $Q$ : un lot grand sur $\sigma_{LT}$ expose peu de cycles à la rupture (voir plus bas).
- Les deux cibles ne se convertissent pas sans la **taille de lot** et la **loi de la demande** : un « 95 % » sans le nom de l'indicateur n'est pas une spécification.

### $\sigma$ : l'erreur de prévision, pas la demande brute

- Le stock de sécurité couvre ce que la prévision **n'explique pas**. La variance de la demande brute contient aussi la tendance, la saisonnalité et les promotions que la prévision prédit déjà : l'employer **surstocke** hors saison et ne couvre rien de plus en pic.
- Le $\sigma$ à employer est celui de l'**erreur de prévision cumulée sur le délai**, mesurée **hors échantillon** et à l'horizon du délai (voir [[Walk-forward CV]]). Sur un horizon d'un pas, la RMSE de [[Forecasting metrics]] en est l'estimation, biais inclus ; sous normalité, $\sigma \approx 1{,}25 \times \mathrm{MAE}$ (identité $\mathbb E|X| = \sigma\sqrt{2/\pi}$).
- Silver, Pyke et Thomas (4e éd., 2017) et Axsäter (3e éd., 2015) sont les manuels de référence du sujet ; seules leurs métadonnées ont été vues, pas le texte.
- Prak, Teunter et Syntetos (EJOR 256(2), 2017) montrent que **multiplier la variance de l'erreur à un pas par $L$** est faux : les erreurs sur les périodes d'un même délai sont **positivement corrélées**, même sans autocorrélation de la demande, car elles partagent le même estimateur de la moyenne. D'après leur résumé, les stocks de sécurité obtenus peuvent être jusqu'à 30 % trop bas et les taux de service jusqu'à 10 % sous la cible. Le PDF de l'article n'a pas pu être ouvert : les expressions ci-dessous sont **redérivées ici**, non lues.

### Ce qui casse la normale

- **Demande intermittente** : beaucoup de zéros, quelques pics. Lead time demand sans cloche. Voir [[Intermittent demand]]. Persson et al. (WSC 2017) comparent simulation et calcul théorique sur trois produits à demande intermittente et concluent que la simulation fixe mieux le stock de sécurité (un cas, trois produits).
- **Faible volume** : une loi discrète ($\text{Poisson}$, voir [[Processus de Poisson]]) se lit directement : $R$ est le plus petit entier avec $\mathbb P(D_{LT} \le R) \ge \alpha$, sans $z$.
- **Queues lourdes** : le quantile à 99,9 % d'une loi à queue lourde n'a rien à voir avec $z\sigma$. Voir [[Théorie des valeurs extrêmes]].
- Pauly (2025) note que la normale s'emploie surtout quand la demande est élevée, avec un coefficient de variation $\le 0{,}5$ d'après la plupart des ressources spécialisées (donnée de seconde main) ; la normale donne sinon une probabilité de demande négative.

## Les maths, simplement

- Notations : $d$ demande moyenne par période, $\sigma_d$ son écart-type, $L$ délai moyen en périodes, $s_L$ l'écart-type du délai, $D_{LT}$ la demande cumulée sur le délai.
- **Demande et délai aléatoires, indépendants, périodes indépendantes, demande normale** (Wikipedia, *Safety stock*) :
  $$\sigma_{LT} = \sqrt{L\,\sigma_d^2 + d^2\,s_L^2}, \qquad SS = z\,\sigma_{LT}.$$
  Le premier terme vient de la somme de $L$ demandes indépendantes, le second de la variabilité du nombre de périodes sommées. Un contrôle par simulation (délai de 3, 5 ou 7 périodes, $\sigma_d = 5$, $d = 20$) retrouve la variance de la formule à moins de 0,2 %.
- **Perte normale** : pour $Z \sim \mathcal N(0,1)$, $G(z) = \mathbb E[(Z - z)^+] = \varphi(z) - z\,(1 - \Phi(z))$, où $\varphi$ est la densité normale réduite. Le manque attendu par cycle, avec $R = \mu_{LT} + z\sigma_{LT}$, vaut $\sigma_{LT}\,G(z)$ (vérifié par Monte-Carlo, 4 millions de tirages, à 0,2 % près).
- **Fill rate** pour une politique $(R,Q)$ à rupture différée, un seul ordre en cours :
  $$\beta = 1 - \frac{\sigma_{LT}\,G(z)}{Q} \quad\Longleftrightarrow\quad G(z) = \frac{(1-\beta)\,Q}{\sigma_{LT}}.$$
  La seconde forme, trouvée aussi dans Wikipedia, donne $z$ par inversion numérique de $G$ (décroissante, donc bijective).
- Pour un taux cyclique $\alpha$ : $z = \Phi^{-1}(\alpha)$, $G(z)$ résultant. Valeurs calculées ici : $\alpha = 0{,}90 \to z = 1{,}282$, $G = 0{,}0473$ ; $0{,}95 \to 1{,}645$, $0{,}0209$ ; $0{,}99 \to 2{,}326$, $0{,}0034$.
- **Même $z$, deux services** : à $\alpha = 95\,\%$ ($z = 1{,}645$), le fill rate vaut $97{,}9\,\%$ si $Q = \sigma_{LT}$, $99{,}5\,\%$ si $Q = 4\sigma_{LT}$. Inversement, viser $\beta = 95\,\%$ avec $Q = \sigma_{LT}$ demande $z = 1{,}256$ seulement ; avec $Q = 4\sigma_{LT}$, $z = 0{,}49$. Pour $\beta = 90\,\%$ et $Q = 4\sigma_{LT}$, $z$ tombe à environ $0$ (calculs ici).
- **Variance de l'erreur sur le délai, demande de moyenne constante, délai constant** : si la prévision est la moyenne des $N$ dernières périodes, de variance $\sigma^2$ par période, l'erreur sur $L$ périodes vaut $\sum_{i=1}^{L}\varepsilon_i + L(\mu - \hat\mu)$, d'où
  $$\mathrm{Var} = L\,\sigma^2 + L^2\,\mathrm{Var}(\hat\mu) = \sigma^2\left(L + \frac{L^2}{N}\right),$$
  contre $L\,\sigma_{e1}^2 = \sigma^2(L + L/N)$ si l'on prolonge la variance de l'erreur à un pas ($\sigma_{e1}^2 = \sigma^2(1 + 1/N)$). Pour $N = 10$, $L = 4$ : $5{,}6\,\sigma^2$ contre $4{,}4\,\sigma^2$, soit un stock de sécurité environ 11 % trop bas ; simulation à 200 000 tirages en accord avec $5{,}6$. Avec un lissage exponentiel de paramètre $a$, $\mathrm{Var}(\hat\mu) = \sigma^2\,a/(2-a)$ remplace $\sigma^2/N$ (résultat classique sur le lissage exponentiel, non relu dans Prak et al.).
- **Forme du coût** : $SS = z_\alpha\sigma_{LT}$ est **linéaire en $\sigma_{LT}$** et **convexe en $\alpha$** (sa pente en $\alpha$ est $\sigma_{LT}/\varphi(z)$, croissante pour $\alpha > 0{,}5$). Rapports calculés : de 95 % à 99 %, $z$ passe de $1{,}645$ à $2{,}326$ (+41 %) ; de 99 % à 99,9 %, à $3{,}090$ (+33 %). Chaque neuf de plus coûte donc de plus en plus cher en stock.

```python
from scipy.stats import norm
from scipy.optimize import brentq
G = lambda z: norm.pdf(z) - z * norm.sf(z)          # perte normale
z_fill = lambda beta, Q, sig: brentq(lambda z: G(z) - (1 - beta) * Q / sig, -5, 10)
z_fill(0.95, 1.0, 1.0)   # 1.256 : fill rate 95 % quand Q = sigma_LT
```

## En pratique

- **Écrire l'indicateur** : « CSL 95 % » ou « fill rate 98 % », jamais « taux de service 95 % » seul. Les deux se pilotent différemment et ne se comparent pas.
- **Mesurer $\sigma$ sur l'erreur de la prévision réellement employée**, à l'horizon du délai, hors échantillon, puis la **réévaluer** : un changement de modèle ou de saison change le stock de sécurité. Voir [[Forecasting metrics]] et [[Walk-forward CV]].
- **Sans loi normale** : prendre directement le **quantile empirique** des erreurs de prévision cumulées sur le délai. [[Calibration]] et [[Prédiction conforme]] en donnent le cadre : pour une prévision à un côté, le quantile des erreurs signées de calibration est le score conforme, avec la garantie à taille finie de l'échangeabilité. Pour obtenir directement la loi de la demande sur le délai sans hypothèse de forme, voir [[De la prévision probabiliste à la quantité commandée]].
- **Poisson, ordre de grandeur** (calcul ici) : à moyenne 6 sur le délai, le quantile 95 % vaut 10 pour Poisson et 10,03 pour la normale ; à moyenne 1, 3 contre 2,64 ; à 99 % et moyenne 1, 4 contre 3,33. La normale sous-couvre à faible volume.
- **Le délai aussi varie** : sa variabilité pèse par $d^2 s_L^2$, d'autant plus que la demande moyenne $d$ est forte. Mesurer $s_L$ sur les livraisons réelles, pas sur le délai promis.
- **Rythme de réapprovisionnement** : avec une revue périodique de période $R$, la commande passée à une revue n'arrive qu'après $R + L$ : la protection porte sur $R + L$, pas sur $L$ (voir [[Politiques de réapprovisionnement (s,S) et (R,Q)]]).
- **Limites des formules** : périodes indépendantes, loi stationnaire, délai indépendant de la demande, rupture différée. Les ruptures avec ventes perdues et la demande qui dépend du stock disponible sortent du cadre.
- **Définitions du fill rate** : le $\beta$ « par cycle » de Tempelmeier diffère, d'après Rossi, Kilic et Tarim (2011), de la définition sur l'horizon complet, et peut conduire à des politiques sous-optimales. Un logiciel qui annonce un « fill rate » ne dit pas toujours lequel.

### Travaux récents

Prépublication de juillet 2026, lue au niveau du résumé : Fernández-Palacios, Ceballos, Muñoz-Ocaña, arXiv 2607.19835. Quand les erreurs de prévision historiques changent de loi, un indice (LOWDII) mesure l'influence de chaque erreur sur l'incertitude employée pour le stock de sécurité. Sur un environnement simulé, les auteurs rapportent le maintien du niveau de service avec 5,1 à 22,6 % de stock moyen en moins par rapport aux méthodes comparées. Résultat de simulation d'une seule équipe ; non reproduit.

## Approches voisines & alternatives

- [[Modèle du vendeur de journaux (newsvendor)]] — le même quantile $F^{-1}$ de la demande, mais sur une période et avec un coût de rupture explicite : le service n'est plus imposé, il se déduit des coûts.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — la politique dont le point de commande contient ce stock de sécurité.
- [[De la prévision probabiliste à la quantité commandée]] — passer de la prévision à la décision sans loi normale.
- [[Indicateurs de stock (rotation, couverture, rupture)]] — mesurer le service réalisé, après coup.
- [[Intermittent demand]] — prévoir quand la demande est creuse ; la normale n'y tient pas.
- [[Théorie des valeurs extrêmes]] — quantiles très élevés d'une queue lourde.
- [[Processus de Poisson]] — demande rare à loi connue, lecture directe du quantile.
- [[Forecasting metrics]], [[Calibration]], [[Prédiction conforme]] — mesurer l'erreur, vérifier qu'elle est bien calibrée, la borner sans loi supposée.
- [[MRP et calcul des besoins]] — où le stock de sécurité entre dans le calcul des besoins.
- [[S&OP et plan directeur de production]] — les stocks tampons d'un plan agrégé, dimensionnés avec ce stock de sécurité.

## Pour aller plus loin

- Prak, Teunter, Syntetos (2017), *On the calculation of safety stocks when demand is forecasted*, EJOR 256(2), 454-461 : <https://doi.org/10.1016/j.ejor.2016.06.035> (titre, auteurs, année vérifiés par Crossref ; résumé lu sur le portail de l'Université de Groningue ; texte non lu).
- Silver, Pyke, Thomas (2017), *Inventory and Production Management in Supply Chains*, 4e éd., CRC Press : <https://www.routledge.com/Inventory-and-Production-Management-in-Supply-Chains/Silver-Pyke-Thomas/p/book/9781466558618> — seules les métadonnées ont été vues.
- Axsäter (2015), *Inventory Control*, 3e éd., Springer : <https://doi.org/10.1007/978-3-319-15729-0> — titre, auteur et année vérifiés par Crossref ; texte non lu.
- Rossi, Kilic, Tarim (2011), *A note on Tempelmeier's β-service measure under non-stationary stochastic demand* : <https://arxiv.org/abs/1103.1286>
- Pauly (2025), *Loss Functions for Inventory Control* : <https://arxiv.org/abs/2502.05212> (version de janvier 2025 lue ; l'entrée arXiv indique une révision postérieure).
- Persson, Axelsson, Edlund, Lanshed, Lindström, Persson (2017), *Using Simulation to Determine the Safety Stock Level for Intermittent Demand*, Winter Simulation Conference : <https://informs-sim.org/wsc17papers/includes/files/318.pdf>
- Fernández-Palacios, Ceballos, Muñoz-Ocaña (2026), arXiv 2607.19835 : <https://arxiv.org/abs/2607.19835> (résumé lu).
- Connexions brain : [[Politiques de réapprovisionnement (s,S) et (R,Q)]], [[Modèle du vendeur de journaux (newsvendor)]], [[Intermittent demand]], [[Forecasting metrics]], [[Prédiction conforme]].
