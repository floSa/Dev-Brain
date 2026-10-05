---
role: notion
nom: Politiques de réapprovisionnement (s,S) et (R,Q)
alias: ["(s,S)", "(R,Q)", "(s,Q)", "(R,S)", "(R,s,S)", "(T,S)", base-stock, order-up-to, point de commande, reorder point, min-max, réapprovisionnement périodique, réapprovisionnement continu, position de stock, inventory position, revue continue, revue périodique, politique de stock]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [inventory, optimization, dynamic-programming, markov-decision-process]
---

# Politiques de réapprovisionnement (s,S) et (R,Q)

## Aperçu

- Une politique de réapprovisionnement est une **règle de décision** : à partir de l'état du stock, elle dit **quand** commander et **combien**. Elle se réduit à deux ou trois paramètres (point de commande, quantité ou niveau cible) qu'il faut ensuite calibrer.
- Elle prolonge le [[Modèle du vendeur de journaux (newsvendor)|vendeur de journaux]] (une période, pas de coût fixe) à un horizon répété, avec un délai et, souvent, un coût fixe de commande. Le point de commande contient un [[Stock de sécurité et taux de service|stock de sécurité]] ; la quantité de lot vient de la [[Quantité économique de commande et tailles de lot|quantité économique de commande]].
- Cette page traite **un seul article**, un seul site. Le multi-échelon et le multi-article ne sont pas couverts (voir Limites).
- Les indicateurs qui mesurent le résultat (rotation, rupture) sont dans [[Indicateurs de stock (rotation, couverture, rupture)]].

## Concepts clés

### Notations : le piège

Les lettres changent d'un auteur à l'autre, et **$R$ désigne deux choses opposées**.

- Cours de Caplice (MIT, 2006), qui s'appuie sur le manuel « SPP » de Silver, Pyke, Peterson : $s$ = point de commande, $S$ = niveau cible, $Q$ = quantité, **$R$ = période de revue**. Politiques $(s,Q)$, $(s,S)$, $(R,S)$, $(R,s,S)$.
- Axsäter : $R$ = **point de commande**, d'où $(R,Q)$. Seul le résumé d'un article de 2003 a été vu (« $(R, nQ)$ policy with time-varying reorder points ») ; le manuel n'a pas été lu.
- Zheng et Federgruen (1991) : $(s,S)$, et $(r,Q)$ avec $r$ = niveau de commande.
- Zipkin : notation non vérifiée.

Dans cette page : $s$ = point de commande (= le $R$ de $(R,Q)$, le $r$ de Zheng-Federgruen), $S$ = niveau cible, $Q$ = lot fixe, $T$ = période de revue (= le $R$ de Caplice), $L$ = délai. Règle de lecture : un $R$ suivi de $Q$ est un point de commande ; un $R$ suivi de $S$ est un intervalle de revue. La page [[Stock de sécurité et taux de service]] note $R$ le point de commande, comme $(R,Q)$.

### La position de stock

- **Position de stock** $IP$ = en stock + en commande − dus (Caplice ajoute « − engagé »).
- Elle se compare au point de commande, **pas le stock physique** : une commande en route est du stock à venir. Comparer le stock physique à $s$ re-déclencherait une commande à chaque période du délai, tant que la première n'est pas arrivée.
- En régime permanent, stock net $=$ $IP$ $-$ demande sur le délai $D(L)$, les deux étant indépendants (Zheng et Federgruen, éq. 13, qui citent Sahin 1979 et Zipkin 1986). La politique pilote donc $IP$ ; le stock physique en découle, décalé de $L$.

### Les politiques

| Politique | Revue | Quand | Combien | Autres notations |
|---|---|---|---|---|
| $(s,Q)$ | continue | $IP \le s$ | $Q$ fixe | $(R,Q)$, $(r,Q)$, « deux bacs » |
| $(s,S)$ | continue | $IP \le s$ | $S - IP$ | min-max |
| $(T,S)$ | périodique | toutes les $T$ | $S - IP$ | $(R,S)$ de Caplice, order-up-to, base-stock |
| $(T,s,S)$ | périodique | toutes les $T$ si $IP \le s$ | $S - IP$ | $(R,s,S)$ |

- **Base-stock** : niveau cible seul, sans seuil. C'est le cas sans coût fixe : pour $K=0$ la politique $(y^*-1,\, y^*)$ est optimale (Zheng et Federgruen). Avec revue continue et demandes unitaires, chaque vente déclenche un réapprovisionnement d'une unité.
- **$(s,S)$ et $(s,Q)$ coïncident** quand les commandes sont passées exactement au point de commande, c'est-à-dire pour des demandes unitaires en revue continue : $Q = S - s$ (Zheng et Federgruen). Sinon la position peut **plonger sous $s$** avant d'être vue (dépassement) : les paramètres exacts de $(s,S)$ sont alors plus compliqués à établir (Caplice : « more complicated due to undershoots »).
- Règle du pouce de Caplice, **convention de cours**, pas résultat : articles A en $(s,S)$ ou $(R,s,S)$, articles B en $(s,Q)$ ou $(R,S)$, articles C à la main ou $(R,S)$. Voir [[Classification ABC-XYZ]].
- Revue continue : coût d'équipement ou de transactions, mais, d'après Caplice, même service avec moins de stock de sécurité. Revue périodique : commandes coordonnées, charge prévisible.

## Les maths, simplement

### Calibrer les paramètres

- **$(s,Q)$** : $s = \mu_L + SS$, avec $\mu_L$ la demande prévue sur le délai et $SS = k\sigma_L$ en loi normale ($k$ fixé par le taux de service visé, voir [[Stock de sécurité et taux de service]]). $Q$ par la formule de Wilson, $Q^* = \sqrt{2KD/h}$ ($K$ coût fixe, $D$ demande par unité de temps, $h$ coût de détention par unité et par unité de temps). Contrôle sur l'exemple de Caplice : $K=50$, $D=13\,000$, $h = 25$ donnent 228. Pour les articles A, Caplice calcule $k$ et $Q$ **ensemble**, car ils interagissent.
- **$(T,S)$** : substitution de Caplice $s \to S$, $Q \to D\cdot T$, $L \to T+L$. $S = \mu_{T+L} + k\,\sigma_{T+L}$ : l'article est protégé sur **tout l'intervalle** entre deux arrivées, pas sur le seul délai. Exemple de ses diapositives : 13 000 unités/an, $L$ = 2 semaines, $T$ = 8 semaines, taux de remplissage 95 % : $\mu_{T+L} = 2\,500$, $\sigma_{T+L} = 577$, $k \approx 0{,}58$, $S \approx 2\,835$ (2 837 sans arrondir $k$, recalculé ici).
- **Version coût, ventes reportées** : $S$ est un **fractile du vendeur de journaux** de la demande sur l'horizon de protection, $S = F^{-1}\!\big(b/(b+h)\big)$, $b$ le coût de rupture par unité et par période, $h$ le coût de détention. Xie et al. (2026) le citent comme formule du fractile critique de Snyder et Shen (2019), pour une demande i.i.d. Contrôle ici : voir la simulation (0,9-quantile d'une loi de Poisson de moyenne 20 = 26, et la grille retrouve $S=26$).
- **$(s,S)$** : pas de formule fermée simple. Départ raisonnable : $s$ du $(s,Q)$, $S = s + Q^*$, puis recherche locale ou algorithme exact (ci-dessous). Le coût d'une paire $(s,S)$ n'est en général **pas quasi-convexe** et peut avoir plusieurs optima locaux (Zheng et Federgruen) : une descente de gradient naïve est risquée.
- Demande faible : la loi normale est tenue pour correcte si $\mu_L \ge 10$ (règle de Caplice) ; en deçà, Poisson (voir [[Processus de Poisson]]) ou loi adaptée ([[Intermittent demand]]).

### Optimalité

- **$(s,S)$ est optimale** avec coût fixe $K$ et coût linéaire. Scarf (1960), d'après Xiang et al. (2017) : sur horizon fini, la fonction de coût $G_t(y)$ (coût de la période plus coût futur espéré, $y$ = niveau après réception) est **$K$-convexe** ; $S_t$ minimise $G_t$, et $s_t < S_t$ vérifie $K + G_t(S_t) = G_t(s_t)$. L'article de Scarf n'a pas été lu.
- Horizon infini : Zheng et Federgruen (1991) rappellent l'optimalité de $(s,S)$ en coût moyen sous ventes reportées (Veinott), et en coût actualisé (Iglehart 1963) ; en revue continue avec délai fixe pour une demande de Poisson composée (Beckmann 1961, Veinott 1966, Stidham 1986), citations de seconde main.
- Conditions de Zheng et Federgruen : demandes i.i.d. entières, coûts stationnaires, ventes reportées, $G$ quasi-convexe (leur $-G$ est unimodale) avec $\lim_{|y|\to\infty} G > \min G + K$. Un délai aléatoire reste couvert s'il est exogène et sans croisement de commandes.
- **Ventes reportées, délai constant** : $IP$ résume tout l'état et une base-stock est optimale (Arrow et Karlin 1958, tels que cités par Gijsbrechts et al.). Ce résumé **disparaît avec les ventes perdues** : l'état est alors le vecteur de toutes les commandes en route, de dimension $L$.
- Systèmes en série : Clark et Scarf (1960) en caractérisent la structure optimale (d'après Gijsbrechts et al., source primaire non lue).
- Calcul : Zheng et Federgruen donnent un algorithme exact dont la complexité vaut 2,4 fois l'évaluation d'**une** politique $(s,S)$.

### Lien MDP

- Équation de Bellman, un article, une période (Xiang et al.) : $C_t(I) = \min_{Q}\{\, f_t(I,Q) + \mathbb E[\,C_{t+1}(I + Q - d_t)\,]\,\}$, avec $f_t$ le coût immédiat (commande $K\mathbf 1_{Q>0} + cQ$, détention, rupture). C'est un [[Chaînes de Markov|processus de décision markovien]] : sous une politique stationnaire, la position de stock est une chaîne de Markov régénérative.
- La politique $(s,S)$ est la **forme de la solution**, pas une hypothèse : la programmation dynamique la retrouve.
- La programmation dynamique devient intractable dès que l'état gonfle (ventes perdues et délai long, multi-échelon).

## En pratique

### Une simulation de dix lignes

Revue quotidienne, délai $L=3$, demande de Poisson de moyenne 5 par jour, $K=50$, $h=1$, $b=9$ par unité et par jour, ventes reportées, 100 000 jours, une seule graine (exécuté avec numpy) :

```python
D = np.random.default_rng(0).poisson(5, 100_000)
def cout(s, S, L=3, K=50, h=1, b=9, physique=False):
    stock, pipe, tot = 12, [0] * L, 0
    for d in D:
        stock += pipe.pop(0)                    # réception
        pos = stock + sum(pipe)                 # position = en stock + en commande - dus
        q = S - pos if (stock if physique else pos) <= s else 0
        pipe.append(q); stock -= d
        tot += K * (q > 0) + h * max(stock, 0) + b * max(-stock, 0)
    return tot / len(D)
```

- Grille $s \in [14,29]$, $S \in [s+5,\ s+43]$ (pas 2) : meilleur point $(18,\,41)$, **24,32 par jour**, 0,196 commande par jour, 9,1 % des jours finissant en rupture.
- Heuristique $s = 20$ (quantile 0,9 de Poisson(15)), $S = s + Q^* \approx 42$ ($Q^* = \sqrt{2\cdot 50\cdot 5/1} \approx 22{,}4$) : 24,71. Même ordre, écart de 1,6 % non testé statistiquement.
- Base-stock seule ($K$ payé presque chaque jour) : $S = 26$, **57,86**. C'est le prix du coût fixe ignoré.
- Même $(18,41)$ déclenché sur le **stock physique** : **37,56**, 0,42 commande par jour au lieu de 0,20. La position de stock n'est pas un détail.

### Choisir et régler

- Coût fixe significatif ou lot imposé par le fournisseur : $(s,S)$ ou $(s,Q)$. Pas de coût fixe : base-stock.
- Revue imposée (tournée camion, calendrier fournisseur) : $(T,S)$ ou $(T,s,S)$ ; la protection porte sur $T+L$.
- Les paramètres ne valent que par la loi de demande sur le délai : l'erreur de prévision est la source d'erreur dominante. Voir [[De la prévision probabiliste à la quantité commandée]].

### Limites

Établies par les sources lues, pas par la page :

- **Un seul article** : toutes les sources lues le sont. Le multi-échelon est un autre problème (Clark-Scarf, Federgruen-Zipkin, d'après Gijsbrechts et al.), « peu d'espoir » d'une structure optimale en réseau divergent (de Kok et al. 2018, cités par eux).
- **Délai constant** (ou aléatoire sans croisement). Xie et al. écrivent qu'une politique calibrée pour un délai déterministe peut échouer si le délai réel est très aléatoire.
- **Demande stationnaire** : Zheng-Federgruen supposent des demandes i.i.d. En non stationnaire, les paramètres dépendent de la période ; Xiang et al. proposent un MILP à $(s_t,S_t)$ avec écarts d'environ 0,3 % à l'optimum, quand Askin (1981) et Bollapragada-Morton (1999) sont à 3,9 % et 4,9 % (mesure de Dural-Selcuk et al. 2016, relayée par Xiang et al.).
- **Ventes reportées ou perdues** : les formules ci-dessus supposent les ventes reportées. Avec ventes perdues, la base-stock est mauvaise sauf pénalité élevée (Zipkin 2008, Huh et al. 2009, d'après Gijsbrechts et al.) ; Caplice note que le taux de remplissage change aussi de formule. Non couvert : le détail des politiques à ventes perdues (capped base-stock de Xin 2019, myope).
- **Demande intermittente** ou à très faible volume : normale fausse, voir plus haut.

### Apprentissage par renforcement profond

- Gijsbrechts et al. (MSOM 2022) appliquent A3C à trois problèmes classiques à ventes perdues, double approvisionnement et multi-échelon, sur des cas où la programmation dynamique est solvable. Ils concluent : A3C **égale** les meilleures heuristiques ou méthodes de programmation dynamique approchée, **sans les battre toutes**. En ventes perdues (Poisson de moyenne 5, $L$ de 2 à 4), A3C fait mieux que la base-stock et la commande constante, mais pas mieux que la politique myope à deux périodes ni la capped base-stock ; en double approvisionnement, A3C reste à moins de 2 % de l'optimum.
- Leurs réserves : réglage initial coûteux (environ 250 jeux d'hyperparamètres évalués), politique en boîte noire, loi de demande **connue** à l'entraînement ; ils recommandent d'étudier les cas non stationnaires, multi-articles, à demande à apprendre.
- Temizöz et al. (EJOR 2025), lu au niveau du résumé : un algorithme d'itération de politique approchée (Deep Controlled Learning) dépasse les heuristiques, dont la capped base-stock, avec un écart à l'optimum d'au plus 0,2 % sur leurs cas. Non confronté à Gijsbrechts : algorithme différent.

### Travaux récents

- Xie, Hao, Liu, Ma, Xin, Cao, Zhang — *DeepStock: Reinforcement Learning with Policy Regularizations for Inventory Management* (arXiv 2603.19621, mars 2026) : **imposer la structure base-stock** à l'agent accélère le réglage et améliore le résultat. Déploiement chez Alibaba (Tmall), sur un modèle à ventes perdues, période de revue et délai fixes. Le pilote de juillet 2024 rapporte −0,83 % de rupture et −9,53 jours de rotation en différence de différences, mais sur 10 % de références que les auteurs disent avoir « cherry-picked » parmi les problématiques. Résultats des auteurs, non reproduits ici.
- Lecture : DeepStock réintroduit la structure base-stock dans l'agent au lieu de la laisser à apprendre.

## Approches voisines & alternatives

- [[Modèle du vendeur de journaux (newsvendor)]] : la brique à une période, dont le fractile donne $S$.
- [[Stock de sécurité et taux de service]] : le coussin du point de commande.
- [[Quantité économique de commande et tailles de lot]] : le $Q$ de $(s,Q)$ et l'écart $S-s$ de $(s,S)$.
- [[Reinforcement learning]] : apprendre la politique directement, utile quand aucune heuristique n'existe ; sinon à comparer à la meilleure base-stock.
- [[Chaînes de Markov]] : cadre de l'évaluation d'une politique donnée.
- [[Optimisation]] : programmation mathématique du dimensionnement (Xiang et al. : MILP pour $(s_t,S_t)$).
- [[Classification ABC-XYZ]] : choisit quelle politique pour quel article.
- [[MRP et calcul des besoins]] — l'autre manière de déclencher les ordres, par les besoins dérivés plutôt que par un point de commande.

## Pour aller plus loin

- Zheng & Federgruen (1991), *Finding optimal (s,S) policies is about as simple as evaluating a single policy*, Operations Research 39(4):654-665, DOI 10.1287/opre.39.4.654 : <https://business.columbia.edu/sites/default/files-efs/pubfiles/4030/federgruen_finding.pdf>
- Xiang, Rossi, Martin-Barragan, Tarim (2017), *Computing non-stationary (s,S) policies using mixed integer linear programming* : <https://arxiv.org/abs/1702.08820>
- Gijsbrechts, Boute, Van Mieghem, Zhang (2022), *Can deep reinforcement learning improve inventory management? Performance on lost sales, dual-sourcing, and multi-echelon problems*, MSOM 24(3):1349-1368, DOI 10.1287/msom.2021.1064 : <https://ideas.repec.org/a/inm/ormsom/v24y2022i3p1349-1368.html> ; version de travail lue : <https://ssrn.com/abstract=3302881>
- Xie, Hao, Liu, Ma, Xin, Cao, Zhang (2026), *DeepStock* : <https://arxiv.org/abs/2603.19621>
- Temizöz, Imdahl, Dijkman, Lamghari-Idrissi, van Jaarsveld (2025), *Deep Controlled Learning for Inventory Control*, EJOR 324(1) : <https://arxiv.org/abs/2011.15122> (résumé seul)
- Caplice (2006), MIT ESD.260J, cours 11 à 13 (notation, $(s,Q)$, $(R,S)$, $(R,s,S)$) : <https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf>, <https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/bc18dd1b2543535a61f826d00a8c6e42_lect12.pdf>, <https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/0f257fe6c8b83a24840d9b1017491950_lect13.pdf>
- Axsäter (2003), *Note: Optimal policies for serial inventory systems under fill rate constraints*, notation $(R,nQ)$ : <https://lup.lub.lu.se/record/636994> (résumé seul)
- Scarf (1960), *The optimality of (S,s) policies in the dynamic inventory problem*, Stanford University Press : seules les citations de seconde main ont été vues. Silver, Pyke, Thomas, *Inventory and Production Management in Supply Chains* (4e éd., CRC Press) : seules les métadonnées ont été vues.
- Connexions brain : [[Modèle du vendeur de journaux (newsvendor)]], [[Stock de sécurité et taux de service]], [[Quantité économique de commande et tailles de lot]], [[De la prévision probabiliste à la quantité commandée]], [[Indicateurs de stock (rotation, couverture, rupture)]], [[Reinforcement learning]], [[Chaînes de Markov]].
