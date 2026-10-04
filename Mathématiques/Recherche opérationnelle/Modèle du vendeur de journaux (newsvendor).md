---
role: notion
nom: Modèle du vendeur de journaux (newsvendor)
alias: [newsvendor, newsboy, vendeur de journaux, critical fractile, critical ratio, ratio critique, fractile critique]
categorie: math/recherche-operationnelle
domaines: [data-sci]
tags: [inventory, newsvendor, optimization, probability]
---

# Modèle du vendeur de journaux (newsvendor)

## Aperçu

- Une quantité à commander **une seule fois**, avant de connaître la demande. Trop commandé : un reste invendu à perte. Pas assez : une vente manquée.
- La réponse optimale n'est **ni la moyenne ni la médiane de la demande** : c'est un **quantile** de sa loi, dont le niveau est fixé par le rapport des deux coûts d'erreur. Le modèle est la brique élémentaire de toute la théorie des stocks sous incertitude.
- Il traite une période, une loi de demande connue, aucun coût fixe de commande. Les politiques à plusieurs périodes (stock de sécurité, point de commande) en sont l'extension, voir [[Stock de sécurité et taux de service]]. Comment obtenir la loi à partir d'un modèle de prévision : [[De la prévision probabiliste à la quantité commandée]].

## Concepts clés

### Le problème à une période

- $D$ : demande de la période, aléatoire, de fonction de répartition $F$ supposée connue. $Q$ : quantité commandée avant d'observer $D$.
- $p$ : prix de vente, $c$ : coût d'achat unitaire, $s$ : valeur de récupération d'une unité invendue (négative s'il faut payer pour s'en défaire), avec $s < c < p$.
- **Coût de rupture** (underage) : $C_u = p - c$, la marge perdue par unité demandée mais non livrée. **Coût de surstock** (overage) : $C_o = c - s$, la perte par unité invendue.
- Tout coût proportionnel supplémentaire s'ajoute au coût qu'il aggrave : une pénalité de rupture ou de réputation grossit $C_u$, un coût de stockage ou de mise au rebut grossit $C_o$. La dérivation est inchangée.

### Le fractile critique

$$Q^* = F^{-1}(\beta), \qquad \beta = \frac{C_u}{C_u + C_o} = \frac{p - c}{p - s}.$$

- $\beta$ est le **ratio critique**. C'est aussi la probabilité de **ne pas rompre** : $\mathbb P(D \le Q^*) = \beta$, donc $\mathbb P(D > Q^*) = C_o/(C_u + C_o)$.
- Marge forte ou récupération élevée : $\beta > 1/2$, commander **au-dessus** de la médiane (livres, mode, d'après la classification de Schweitzer et Cachon : « produit à forte marge » quand $\beta \ge 1/2$). Marge faible et récupération nulle : $\beta < 1/2$, commander **en dessous**.
- Si $c \ge p$, la formule donne un $\beta \le 0$ : la quantité optimale est zéro.

### Pourquoi un quantile et non la moyenne

- Le coût de l'erreur est asymétrique : manquer une unité ne coûte pas ce que coûte une unité en trop. Le minimiseur d'une perte asymétrique est un quantile, pas une moyenne.
- Le coût s'écrit exactement comme une **perte pinball** de niveau $\beta$, à un facteur près (voir *Les maths, simplement*). Un modèle entraîné à minimiser une erreur quadratique estime la moyenne : il répond à une autre question que celle de la commande.
- La moyenne n'est optimale que si $\beta = 1/2$, c'est-à-dire $C_u = C_o$, et alors la médiane aussi (loi symétrique).
- Mesure sur l'exemple chiffré plus bas : commander la moyenne coûte environ **25 %** de plus que $Q^*$.
- Voir [[Régression quantile]] : la perte pinball y est la perte d'apprentissage.

### Trois lois, trois formes fermées

- **Normale** $\mathcal N(\mu, \sigma^2)$ : $Q^* = \mu + z_\beta\,\sigma$, avec $z_\beta = \Phi^{-1}(\beta)$. Le terme $z_\beta\,\sigma$ est la marge au-dessus de la moyenne (le « stock de sécurité » de la période). Le coût moyen minimal vaut $(C_u + C_o)\,\sigma\,\varphi(z_\beta)$, où $\varphi$ est la densité normale centrée réduite.
- **Exponentielle** de taux $\lambda$ : $F(Q) = 1 - e^{-\lambda Q}$, d'où $Q^* = \frac{1}{\lambda}\ln\frac{C_u + C_o}{C_o}$. Loi à queue plus épaisse que la normale : $Q^*$ dépasse vite plusieurs fois la moyenne $1/\lambda$ quand $\beta$ approche 1.
- **Discrète** : $Q^*$ est le **plus petit** entier tel que $F(Q) \ge \beta$. Si $F(Q) = \beta$ exactement, toute quantité entre ce $Q$ et le suivant est optimale. Exemple de l'expérience de Schweitzer et Cachon : demande uniforme sur $\{1,\dots,300\}$, $p = 12$, $s = 0$ ; $c = 3$ donne $\beta = 0{,}75$ et $Q^* = 225$, $c = 9$ donne $\beta = 0{,}25$ et $Q^* = 75$ (retrouvé ici par recherche exhaustive).

### Origine historique

- Une note du CWI sur 125 ans de gestion des stocks attribue à Edgeworth (1888, *The mathematical theory of banking*, J. Royal Statistical Society) la première publication du problème, dans le contexte des réserves de caisse d'une banque. Seule la référence a été vue dans cette note, l'article d'Edgeworth n'a pas été lu.
- Arrow, Harris et Marschak (1951, *Econometrica* 19(3), 250-272) donnent le traitement moderne : un modèle statique où la demande a une loi connue, et un modèle dynamique. Leur coût de rupture est une pénalité $A + B(x - S)$ (partie fixe plus partie proportionnelle). **Le fractile critique n'y est qu'un cas particulier** : sans partie fixe ($A = 0$) et sans rabais de quantité, la condition d'optimalité (3.8) devient $1 - F(S^*) = (c + b_0)/(B + a)$, soit la formule ci-dessus, où $B + a$ (utilité d'une unité livrée plus pénalité par unité manquante) joue le rôle de $p$, $c + b_0$ celui de $c$, et $s = 0$. Avec une partie fixe, la condition porte sur la **densité** $f(S^*)$, pas sur un quantile.
- Les mêmes auteurs signalent que des travaux antérieurs fixaient la probabilité de rupture à une valeur imposée plutôt que de la déduire des coûts, et regrettent de ne pas avoir connu les travaux de Massé. La formule du fractile a donc des antécédents, et le texte de 1951 la présente comme une conséquence d'un modèle de coûts plus général.

### Extensions

- **Plusieurs produits, une contrainte commune** (budget d'achat $B$ : $\sum_i c_i Q_i \le B$). Le lagrangien donne, pour chaque produit, $F_i(Q_i) = \dfrac{C_{u,i} - \lambda c_i}{C_{u,i} + C_{o,i}}$ : le multiplicateur $\lambda \ge 0$ **abaisse le fractile** de chaque produit en proportion de son coût unitaire. $\lambda$ se trouve par dichotomie jusqu'à saturer la contrainte. Dérivé et vérifié numériquement ici (deux produits normaux, budget 450 : $\lambda \approx 1{,}15$, solution identique à celle d'un optimiseur sous contrainte). Voir [[Optimisation sous contrainte]].
- **Prix endogène** : quand le prix fait partie de la décision et que la loi de $D$ en dépend, $\beta$ dépend de $p$ et le problème devient conjoint (quantité et prix). Voir Petruzzi et Dada (1999), seul le résumé a été lu.
- **Demande censurée** : voir *En pratique*.
- **Aversion au risque** : un décideur averse au risque commande **moins** que $Q^*$, un décideur preneur de risque plus (Eeckhoudt, Gollier, Schlesinger, 1995, rapporté par Schweitzer et Cachon ; l'article n'a pas été lu). $Q^*$ ne maximise que l'espérance du profit.
- Panorama de ces variantes : Qin, Wang, Vakharia, Chen, Seref (2011), revue dans *EJOR*, résumé seul lu.

### Le biais comportemental : pull-to-center

- Schweitzer et Cachon (2000) font passer des décideurs par un jeu de newsvendor à loi connue. Résultat : **trop peu commandé pour les produits à forte marge, trop pour ceux à faible marge**. Les commandes se placent entre la moyenne de la demande et $Q^*$.
- Chiffres du premier essai (33 sujets, demande uniforme 1-300, moyenne 150) : commande moyenne de 176,68 pour $Q^* = 225$, et de 134,06 pour $Q^* = 75$. Dans les deux cas, plus de la moitié de l'écart entre $Q^*$ et la moyenne est effacée (calcul d'après ces moyennes).
- Les auteurs écartent l'aversion au risque, la théorie des perspectives et l'aversion au gaspillage ou à la rupture. Deux explications restent compatibles avec les données : la volonté de réduire l'erreur d'inventaire *ex post*, ou l'ancrage sur la moyenne avec ajustement insuffisant. Retour d'expérience et formation n'ont pas réduit l'erreur.
- L'expression « pull-to-center » n'apparaît pas dans l'article de 2000 (recherche textuelle sur le PDF) ; elle vient de la littérature suivante. Yang et Cai (2022) la reprennent et testent trois causes (ancrage sur la moyenne, poursuite de la demande précédente, surconfiance) sur un échantillon chinois.
- Conséquence pratique : une quantité décidée à la main, sans calcul du fractile, est biaisée vers la moyenne dans un sens prévisible.

## Les maths, simplement

- Coût moyen de la commande $Q$ :
  $$G(Q) = C_u\,\mathbb E[(D - Q)^+] + C_o\,\mathbb E[(Q - D)^+], \qquad x^+ = \max(x, 0).$$
- Une unité de plus est **vendue** avec la probabilité $1 - F(Q)$ (gain : on évite $C_u$) ou **invendue** avec la probabilité $F(Q)$ (coût : $C_o$). D'où
  $$G'(Q) = C_o\,F(Q) - C_u\,\bigl(1 - F(Q)\bigr) = (C_u + C_o)\,F(Q) - C_u.$$
- $G'$ croît avec $Q$ : $G$ est convexe, le minimum est unique et vérifie $G'(Q^*) = 0$, soit $F(Q^*) = C_u/(C_u + C_o)$.
- Lien avec la perte pinball $\rho_\beta(u) = u\,(\beta - \mathbb 1_{u < 0})$, pour l'erreur $u = D - Q$ :
  $$C_u\,(D - Q)^+ + C_o\,(Q - D)^+ = (C_u + C_o)\;\rho_\beta(D - Q).$$
  Vérification : si $D > Q$, $(C_u + C_o)\,\beta\,(D - Q) = C_u\,(D - Q)$ ; si $D < Q$, $(C_u + C_o)(1 - \beta)(Q - D) = C_o\,(Q - D)$.
- Contrôle numérique de la formule normale (2 millions de tirages) :

```python
import numpy as np
from scipy import stats
Cu, Co, mu, sigma = 9.0, 3.0, 100, 20          # beta = 0.75
rng = np.random.default_rng(0); D = rng.normal(mu, sigma, 2_000_000)
cost = lambda Q: np.mean(Cu*np.maximum(D-Q, 0) + Co*np.maximum(Q-D, 0))
Q_star = mu + sigma*stats.norm.ppf(Cu/(Cu+Co))
print(round(Q_star, 2), round(cost(Q_star), 2), round(cost(mu), 2))   # 113.49 76.25 95.77
```

- Lecture : $Q^* = 113{,}49$ ; le coût simulé 76,25 colle à la valeur théorique $(C_u + C_o)\sigma\varphi(z_\beta) = 76{,}27$ ; commander la moyenne (100) coûte 95,77, soit environ 25 % de plus. Autour de $Q^*$, le coût est plat à l'ordre un : $\pm 5$ unités ajoutent environ 3 %, $\pm 10$ unités entre 11 et 14 % (calcul analytique, mêmes paramètres). Se tromper de $\beta$ coûte plus cher que se tromper de quelques unités : prendre $\beta = 0{,}5$ à la place de $0{,}75$ ajoute 25 %.
- Même contrôle pour les autres lois : sur la loi uniforme discrète, la recherche exhaustive donne 225 et 75. Sur l'exponentielle (moyenne 100, $\beta = 0{,}75$), la formule donne 138,63 et la minimisation par simulation 138,35 (bruit d'échantillonnage).

## En pratique

- **Le point d'entrée est le ratio, pas la prévision** : $C_u$ et $C_o$ se lisent dans la comptabilité (marge, valeur de reprise, coût de destruction). Un ratio mal estimé coûte plus qu'une loi de demande approximative (voir le chiffre ci-dessus).
- **La loi $F$ n'est jamais connue** : elle s'estime sur l'historique, et le quantile à $\beta$ élevé repose sur la queue de la loi, la partie la moins bien observée. Un quantile prévu doit être contrôlé comme tel : fréquence de ruptures observée contre $1 - \beta$ attendu, voir [[Calibration]] et [[Forecasting metrics]] (perte pinball, couverture).
- **Garantie sans hypothèse de loi** : une borne supérieure issue de [[Prédiction conforme]] vise la condition $\mathbb P(D \le Q) \ge \beta$ avec une garantie à taille finie (si la demande est échangeable). Elle garantit le **taux de service**, pas le coût optimal, et ne tient pas sous tendance ou saisonnalité non traitée.
- **Demande intermittente ou en grande partie nulle** : la loi a une masse en zéro, le cas discret s'applique, pas le normal. Voir [[Intermittent demand]].
- **Demande censurée par les ruptures** : quand un article tombe en rupture, seule la demande **vendue** $\min(D, Q)$ est observée. Utiliser les ventes comme demande sous-estime la demande et donc $Q^*$, ce qui provoque encore plus de ruptures.
  - Ding, Puterman, Bisi (2002) : paramètres de la loi inconnus, ruptures non observées : la quantité optimale en présence de censure est plus élevée que celle d'une politique bayésienne myope (qui ignore la valeur de l'information).
  - Huh, Levi, Rusmevichientong, Orlin (2011) : une politique adaptative non paramétrique fondée sur l'estimateur de Kaplan-Meier ; convergence presque sûre démontrée pour une demande discrète.
  - Lugosi, Markakis, Neu (2017, prépublication) : sans aucune hypothèse probabiliste sur la demande, le coût de la censure est négligeable sur le critère du regret (écart au meilleur choix fixe a posteriori).
- **Demande dépendante de la quantité** (effet de présentation en rayon, clients perdus durablement après une rupture) : hors modèle de base. Une partie passe dans $C_u$ (pénalité de réputation), le reste demande un autre modèle.
- **Plusieurs périodes, commandes répétées, stock restant** : le modèle ne s'applique plus tel quel ; voir [[Stock de sécurité et taux de service]].

### Travaux récents

- Kumar, Mouchtaki (arXiv 2602.16842, février 2026), *What is the Value of Censored Data? An Exact Analysis for the Data-driven Newsvendor* (résumé lu seul) : calcul exact du pire regret de politiques classiques avec demande censurée. Les ventes traitées comme demande dégradent fortement la performance quand les données censurées s'accumulent ; avec l'estimateur de Kaplan-Meier, un peu d'exploration ciblée à des niveaux de stock élevés améliore nettement les garanties.

## Approches voisines & alternatives

- [[Régression quantile]] — apprend directement le quantile $\beta$ de la demande conditionnelle ; la perte pinball est le coût du newsvendor.
- [[Prédiction conforme]] — borne supérieure à couverture garantie ; équivalent probabiliste du fractile.
- [[Intermittent demand]] — demande en grande partie nulle, où la loi n'est pas normale.
- [[Forecasting metrics]] — évaluer un quantile prévu (pinball, couverture) plutôt qu'une erreur de moyenne.
- [[Calibration]] — vérifier que le quantile affiché couvre bien la fréquence annoncée.
- [[Stock de sécurité et taux de service]] — le cas multi-périodes avec délai d'approvisionnement.
- [[De la prévision probabiliste à la quantité commandée]] — la suite pratique : de la prévision à la quantité.
- [[Optimisation sous contrainte]] — la contrainte commune de plusieurs produits.

## Pour aller plus loin

- Schweitzer, Cachon (2000), *Decision Bias in the Newsvendor Problem with a Known Demand Distribution: Experimental Evidence*, Management Science 46(3), 404-420 : <https://doi.org/10.1287/mnsc.46.3.404.12070> (PDF consulté sur <https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Cachon_schweitzer_ms.pdf>)
- Arrow, Harris, Marschak (1951), *Optimal Inventory Policy*, Econometrica 19(3), 250-272 : <https://doi.org/10.2307/1906813>
- Edgeworth (1888), *The Mathematical Theory of Banking*, Journal of the Royal Statistical Society 51, 113-127 : référence relevée dans la note du CWI *125 years of inventory management, 100 years of EOQ and 40 years of vLm* (<https://www.cwi.nl/documents/199620/100_jaar_voorraadbeheersing_v3_ENG.pdf>), article non lu.
- Yang, Cai (2022), *Revisiting the Causes of the Pull-to-Centre Effect: Evidence From China*, Frontiers in Psychology 12 : <https://doi.org/10.3389/fpsyg.2021.754626> (page consultée)
- Ding, Puterman, Bisi (2002), *The Censored Newsvendor and the Optimal Acquisition of Information*, Operations Research 50(3), 517-527 : <https://doi.org/10.1287/opre.50.3.517.7752> (résumé seul)
- Huh, Levi, Rusmevichientong, Orlin (2011), *Adaptive Data-Driven Inventory Control with Censored Demand Based on Kaplan-Meier Estimator*, Operations Research 59(4), 929-941 : <https://doi.org/10.1287/opre.1100.0906> (résumé seul)
- Lugosi, Markakis, Neu (2017), *On the Hardness of Inventory Management with Censored Demand Data* : <https://arxiv.org/abs/1710.05739>
- Kumar, Mouchtaki (2026), *What is the Value of Censored Data? An Exact Analysis for the Data-driven Newsvendor* : <https://arxiv.org/abs/2602.16842>
- Petruzzi, Dada (1999), *Pricing and the Newsvendor Problem: A Review with Extensions*, Operations Research 47(2), 183-194 : <https://doi.org/10.1287/opre.47.2.183> (résumé seul)
- Qin, Wang, Vakharia, Chen, Seref (2011), *The newsvendor problem: Review and directions for future research*, EJOR 213(2), 361-374 : <https://doi.org/10.1016/j.ejor.2010.11.024> (résumé seul)
- Eeckhoudt, Gollier, Schlesinger (1995), *The Risk-Averse (and Prudent) Newsboy*, Management Science 41(5), 786-794 : <https://doi.org/10.1287/mnsc.41.5.786> (métadonnées seules)
- Connexions brain : [[Régression quantile]], [[Prédiction conforme]], [[Intermittent demand]], [[Forecasting metrics]], [[Stock de sécurité et taux de service]], [[De la prévision probabiliste à la quantité commandée]].
