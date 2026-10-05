---
role: notion
nom: Quantité économique de commande et tailles de lot
alias: [EOQ, economic order quantity, formule de Wilson, formule de Harris, EPQ, lot sizing, tailles de lot, Wagner-Whitin, Silver-Meal, lot-for-lot]
categorie: math/recherche-operationnelle
domaines: [data-sci]
tags: [inventory, optimization, dynamic-programming, combinatorial-optimization]
---

# Quantité économique de commande et tailles de lot

## Aperçu

- Question posée : **combien** commander (ou lancer en fabrication) à chaque fois, quand chaque lancement coûte un montant fixe et que tout stock détenu coûte aussi ?
- Deux régimes. **Demande constante** : la quantité économique de commande (EOQ, *economic order quantity*) donne une formule fermée, $Q^* = \sqrt{2DK/h}$. **Demande variable dans le temps** : plus de formule, un problème de dimensionnement de lot (*lot sizing*), résolu exactement par programmation dynamique (Wagner-Whitin) ou par heuristiques.
- Ce que l'EOQ ne dit pas : **quand** commander, ni de combien se protéger contre l'aléa. La demande y est connue. Ces deux questions relèvent de [[Politiques de réapprovisionnement (s,S) et (R,Q)]] et de [[Stock de sécurité et taux de service]].
- Limite de cette page : le MRP (calcul des besoins) et l'ordonnancement ne sont pas traités ; le dimensionnement de lot n'en est qu'une étape.

## Concepts clés

### Le compromis lancement / possession

- Notations : $D$ demande par unité de temps (par an), $K$ coût fixe par lancement (commande, ou changement de série), $h$ coût de possession d'**une unité pendant une unité de temps**, $Q$ taille de lot.
- Plus $Q$ est grand, moins il y a de lancements ($D/Q$ par an) mais plus le stock moyen ($Q/2$) est élevé. Harris (1913) le formule ainsi : l'intérêt du capital immobilisé fixe une limite maximale à la quantité fabriquée d'un coup, les coûts de mise en route en fixent le minimum.
- Le coût d'achat $cD$ ne dépend pas de $Q$ tant que le prix est constant : il sort de l'optimisation. $h$ n'est pas qu'un taux de capital : y entrent aussi stockage, assurance, obsolescence. Dans l'exemple de remises du cours IE375 (Erkip, Bilkent), $h$ vaut 20 % du prix ; c'est un choix d'exemple, pas une convention.

### D'où vient la formule (attributions)

- Harris, « How many parts to make at once », *Factory, The Magazine of Management*, février 1913 : première apparition de la formule en racine carrée. Erlenkotter (1990) établit que l'article est resté inaperçu des décennies et a été redécouvert en 1988, et que la version de 1915 (chapitre de la *Library of Factory Management*) a été mal référencée à partir de 1931.
- **Wilson** (*Harvard Business Review*, 1934) en publie une version sans citer ses prédécesseurs ; d'où « formule de Wilson » chez Morse (1958) et Wagner (1980). Beaucoup d'Européens parlent de « formule de Camp » (Camp, 1922 ; Eilon, 1962), et Alford (1934) attribue à Camp la première formule. Ces trois noms désignent la même formule ; seul Harris date de 1913.
- **EPQ** (cadence de production finie) : attribué à Taft (1918, *Iron Age*) par la page Wikipedia consacrée ; l'article de Taft n'a pas été lu.

### Hypothèses, et ce qui casse quand elles tombent

- **Demande constante et connue** : si elle varie dans le temps, passer aux tailles de lot dynamiques (plus bas). Si elle est aléatoire, la formule ne protège de rien (voir les politiques $(R,Q)$ et $(s,S)$). Une demande par à-coups ([[Intermittent demand]]) viole l'idée d'un flux continu.
- **Réapprovisionnement instantané ou à délai constant** : avec un délai $L$ constant, la quantité reste $Q^*$ ; seul le moment de commande se décale (commander quand la position de stock vaut $DL$). Un délai aléatoire sort du cadre.
- **Coût linéaire** : $K$ fixe, $h$ proportionnel au stock, prix constant. Des remises, un coût de lancement dépendant de la séquence ou des contraintes de palette/conteneur cassent la formule fermée.
- **Un seul article, sans capacité commune** : plusieurs articles sur une même machine imposent un calendrier. Appliquer la formule article par article provoque des « interférences » (la machine devrait fabriquer deux articles à la fois) ; le problème d'ordonnancement cyclique de lots (ELSP) est NP-difficile même dans une version très restreinte (Hsu, 1983).

### Variantes à demande constante

- **EPQ** : le lot est produit à la cadence $P > D$ pendant qu'il est consommé. Stock maximal $Q(1-D/P)$, d'où $Q^* = \sqrt{\dfrac{2DK}{h(1-D/P)}}$. Si $P \to \infty$, on retrouve l'EOQ.
- **Rupture autorisée (*backorder*)** : coût $b$ par unité en rupture et par unité de temps, rupture maximale $S$ en fin de cycle. $Q^* = \sqrt{\dfrac{2DK}{h}}\sqrt{\dfrac{h+b}{b}}$, $S^* = Q^*\dfrac{h}{h+b}$ (formules du cours de Bilkent, redérivées et vérifiées). Le coût optimal est inférieur à celui de l'EOQ sans rupture ; si $b\to\infty$, retour à l'EOQ. Hypothèse lourde : la demande manquée est **reportée**, pas perdue.
- **Remises par paliers** : prix $c$ dépendant de $Q$ (remise sur toutes les unités ou incrémentale). Le coût n'est plus convexe d'un seul tenant : on calcule l'EOQ par palier, on garde les réalisables, puis on compare avec les bornes de paliers (procédure du cours de Bilkent pour les remises sur toutes les unités).

### Tailles de lot dynamiques (demande $d_t$ variable)

- Données : demandes connues $d_1,\dots,d_T$, coût de lancement $K$ par période où l'on lance, coût $h$ par unité détenue d'une période à la suivante.
- **Wagner-Whitin** (Wagner et Whitin, 1958, *Management Science* 5) : optimum exact sur l'horizon fini. Propriété clé : on ne lance que si le stock est nul (*zero-inventory ordering*) ; un lot couvre donc les demandes de périodes consécutives, et le problème est un plus court chemin. Algorithme original en $O(T^2)$ ; Wagelmans, van Hoesel et Kolen (1992) donnent $O(T\log T)$, et $O(T)$ dans le cas Wagner-Whitin (coûts positifs).
- **Lot-for-lot** : un lot par période, de la taille de la demande. Aucun stock, mais $K$ payé à chaque période. Sans lancement coûteux, c'est optimal ; sinon, au pire un coût $T$ fois l'optimum (van den Heuvel et Wagelmans, 2007, avec leur définition : un lancement à chaque période).
- **Lot à période fixe** (*periodic order quantity*, POQ) : un lot couvre $n$ périodes, $n$ étant l'EOQ ramenée à une durée de couverture. Simple, mais aveugle aux variations de la demande.
- **Silver-Meal** (Silver et Meal, 1973) : on étend le lot période par période tant que le coût moyen **par période** décroît ; on s'arrête à la première hausse. Méthode « gloutonne » qui ne regarde pas au-delà de la première hausse.
- Heuristiques et exactitude : l'algorithme exact est souvent jugé difficile à comprendre, et en horizon glissant des heuristiques peuvent faire mieux que Wagner-Whitin (van den Heuvel et Wagelmans, 2007, citant Stadtler, 2000). Ils montrent aussi qu'aucune heuristique « en ligne » (qui décide sans voir la demande future) n'a un rapport au pire cas inférieur à 2.

### Avec une capacité : NP-difficile

- Si la production par période est plafonnée par $C_t$ (**capacitated lot sizing**), le problème change de classe : Florian, Lenstra et Rinnooy Kan (1980) montrent que certaines variantes sont NP-difficiles ; Bitran et Yanasse (1982) montrent que des classes spéciales le sont, et que deux articles à lancements indépendants le restent dans des conditions où le cas à un article est facile.
- À un article avec coûts de production linéaires par morceaux, Shaw et Wagelmans (1995) le décrivent comme NP-difficile mais soluble en temps **pseudo-polynomial** par programmation dynamique.
- Pratique : on le pose en programme en nombres entiers mixtes ([[Programmation linéaire en nombres entiers (MIP)]]) et on le traite avec les outils de [[Optimisation combinatoire]]. Trigeiro, Thomas et McClain (1989) traitent le cas avec temps de lancement par relaxation lagrangienne et programmation dynamique, plus une heuristique de lissage.

## Les maths, simplement

- **Coût variable annuel** : $TC(Q) = \dfrac{KD}{Q} + \dfrac{hQ}{2}$. Dérivée nulle : $-KD/Q^2 + h/2 = 0$, d'où
  $$Q^* = \sqrt{\frac{2DK}{h}}, \qquad TC^* = \sqrt{2DKh}.$$
  À l'optimum, coût de lancement et coût de possession sont **égaux** (chacun $TC^*/2$). Durée du cycle : $T^* = Q^*/D$.
- **Surcoût exact d'un lot $Q$ quelconque.** Comme $KD/Q = \frac{TC^*}{2}\frac{Q^*}{Q}$ et $hQ/2 = \frac{TC^*}{2}\frac{Q}{Q^*}$ :
  $$\frac{TC(Q)}{TC^*} = \frac12\left(\frac{Q}{Q^*} + \frac{Q^*}{Q}\right), \qquad \frac{TC(Q)}{TC^*} - 1 = \frac{(Q-Q^*)^2}{2\,Q\,Q^*}.$$
  Avec $Q = (1+\varepsilon)Q^*$ : surcoût relatif $\dfrac{\varepsilon^2}{2(1+\varepsilon)} \approx \dfrac{\varepsilon^2}{2}$. L'erreur est du **second ordre** : l'optimum est plat.
- Lecture numérique (formule vérifiée par calcul) : $\varepsilon=+10\,\%$ donne $+0{,}46\,\%$ ; $-10\,\%$ donne $+0{,}56\,\%$ ; $+20\,\%$ donne $+1{,}67\,\%$ ; $-20\,\%$ donne $+2{,}5\,\%$ ; doubler ou diviser par deux $Q$ donne $+25\,\%$. Le surcoût est symétrique en rapport ($Q/Q^*$ et $Q^*/Q$ coûtent pareil), pas en pourcentage : **sous-commander coûte plus que sur-commander** de la même fraction.
- Corollaire : $Q^*$ varie en racine de $K/h$. Se tromper d'un facteur 4 sur $K$ (ou $h$) fait se tromper d'un facteur 2 sur $Q$, soit $+25\,\%$ de coût variable. Dobson (1988, résumé seul lu) étudie directement la sensibilité aux erreurs d'estimation des paramètres et établit des bornes serrées ; sa conclusion est que cette sensibilité croît comme la racine quatrième de l'incertitude.
- Même formule, autre usage : la restriction à des cycles en puissances de 2 d'une période de base ne coûte au pire que $\frac12(\sqrt2+1/\sqrt2) \approx 1{,}0607$, soit les « 6 % » annoncés par le cours de Bilkent.
- **Exemple à la main.** $D = 12\,000$ unités/an, $K = 50$ €, prix 12 €, taux de possession 20 % donc $h = 2{,}4$ €/unité/an.
  - $Q^* = \sqrt{2\cdot12\,000\cdot50/2{,}4} = \sqrt{500\,000} \approx 707$ ; $TC^* = \sqrt{2\cdot12\,000\cdot50\cdot2{,}4} \approx 1\,697$ €/an ; environ 17 commandes par an, un cycle de 21,5 jours.
  - Lot de 1 000 (palette) : $TC = 50\cdot12/1+2{,}4\cdot500 = 600+1\,200 = 1\,800$ €, soit $+6{,}1\,\%$ pour un lot **41 % trop grand**. Lot de 500 : 1 800 € aussi.
  - EPQ avec $P = 24\,000$ : $Q^* = 1\,000$, coût $1\,200$ € (facteur $\sqrt{1-D/P}=\sqrt{0{,}5}$). Rupture autorisée avec $b = h$ : $Q^* = 1\,000$, $S^* = 500$, coût $1\,200$ €.
  - Remises (exemple de Bilkent : $D=600$, $K=8$, prix 0,30 / 0,29 / 0,28 € à partir de 0 / 500 / 1 000, $h$ = 20 % du prix) : seul l'EOQ à 0,30 € (400) est réalisable ; coût annuel, achats compris : 204,0 € ; au palier 500 : **198,1 €** ; au palier 1 000 : 200,8 €. Optimum : 500 à 0,29 €.
- **Wagner-Whitin** : $F(0)=0$ et $F(j)=\min_{0\le i<j}\Big[F(i)+K+h\sum_{t=i+1}^{j}(t-i-1)\,d_t\Big]$ ($F(j)$ : coût optimal des $j$ premières périodes ; un lot lancé en période $i+1$ couvre les périodes $i+1$ à $j$). Un plus court chemin sur $T+1$ nœuds.
- **Exemple** ($K=100$, $h=1$, $d=[10,40,60,20,10,80,90,30]$) : Wagner-Whitin lance en périodes 1, 3, 6, 7 pour **510** (140 + 140 + 100 + 130). Silver-Meal lance en 1, 3, 6 pour **530** : à la période 6 le coût moyen par période (100, 95, 83,3) ne remonte jamais, donc la méthode étire le lot sur 6-8 alors que lancer à nouveau en 7 économise 20. Lot-for-lot : 800 ; lot à période fixe de 2 périodes (EOQ ramenée à la durée : $\sqrt{2\cdot42{,}5\cdot100}/42{,}5 \approx 2{,}2$) : 570. Valeurs recalculées par énumération complète.
- **Capacité** : $\min\sum_t (K y_t + h I_t)$ sous $I_{t-1}+x_t-d_t=I_t$, $0\le x_t\le C_t\,y_t$, $y_t\in\{0,1\}$, $I_t\ge0$. Formulation classique, non reprise d'une source ouverte ici ; la variable binaire $y_t$ porte la difficulté.

## En pratique

- **Estimer $K$ et $h$ honnêtement** : $K$ est un coût **marginal** (temps de préparation, frais de transport fixes), pas la masse salariale du service achats. Platitude de l'optimum : une approximation grossière suffit, mais un $K$ ou un $h$ faux d'un ordre de grandeur donne un $Q$ faux d'un facteur $\sqrt{10}\approx3{,}2$.
- **Arrondir sans scrupule** : conditionnement, palette, multiple de camion ou de série ; l'arrondi coûte peu tant que $Q/Q^*$ reste dans $[0{,}7;\,1{,}4]$ (surcoût inférieur à $6{,}5\,\%$ d'après la formule ci-dessus).
- **Découpler taille et sécurité** : $Q$ vient de ce modèle ; la protection contre l'aléa et le moment de commande se règlent à part ([[Stock de sécurité et taux de service]], [[Politiques de réapprovisionnement (s,S) et (R,Q)]]). Une demande prévue se traduit en quantité commandée par [[De la prévision probabiliste à la quantité commandée]].
- **Demande variable** : comparer sur l'historique le coût de l'EOQ, du lot à période fixe et de Wagner-Whitin plutôt que de choisir à l'intuition (l'exemple ci-dessus montre 570 contre 510). En horizon glissant, l'optimum à horizon fini n'est pas forcément le meilleur plan (van den Heuvel et Wagelmans, 2007, cité plus haut).
- **Mesurer le résultat** : [[Indicateurs de stock (rotation, couverture, rupture)]].

```python
def wagner_whitin(d, K, h):
    T = len(d)
    F = [0.0] + [float("inf")] * T          # F[j] : coût optimal des j premières périodes
    for j in range(1, T + 1):
        for i in range(j):                  # un lot lancé en période i couvre i..j-1
            F[j] = min(F[j], F[i] + K + h * sum((t - i) * d[t] for t in range(i, j)))
    return F[T]                             # 510.0 sur l'exemple ci-dessus
```

## Approches voisines & alternatives

- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — le cadre stochastique : $Q$ de $(R,Q)$ joue le rôle d'une taille de commande, le point de commande répond au *quand*.
- [[Stock de sécurité et taux de service]] — la marge face à l'aléa de demande et de délai, que l'EOQ ignore.
- [[Modèle du vendeur de journaux (newsvendor)]] — une seule période, demande aléatoire : la quantité vient d'un quantile, pas d'un compromis lancement/possession.
- [[Programmation linéaire en nombres entiers (MIP)]] et [[Optimisation combinatoire]] — pour le dimensionnement capacitaire, les remises complexes, les plusieurs articles.
- [[Optimisation sous contrainte]] — cadre général quand le problème n'a plus de formule fermée.
- [[MRP et calcul des besoins]] — l'étape qui transforme une taille de lot en ordres de fabrication.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — le calendrier que plusieurs articles sur une même machine imposent.

## Pour aller plus loin

- Harris (1913), « How many parts to make at once », *Factory, The Magazine of Management* 10(2) ; réimprimé dans *Operations Research* 38(6), 1990, p. 947-950 : <https://doi.org/10.1287/opre.38.6.947> (seul le résumé a été vu).
- Erlenkotter (1990), « Ford Whitman Harris and the Economic Order Quantity Model », *Operations Research* 38(6), 937-946 : <https://doi.org/10.1287/opre.38.6.937> (texte lu) ; et Erlenkotter (2014), « Ford Whitman Harris's economical lot size model », *IJPE* 155 : <https://doi.org/10.1016/j.ijpe.2013.12.008> (texte lu).
- Wilson (1934), « A scientific routine for stock control », *Harvard Business Review* 13, 116-128 — cité par Erlenkotter, non lu.
- Wagner et Whitin (1958), « Dynamic version of the economic lot size model », *Management Science* 5(1), 89-96 : <https://doi.org/10.1287/mnsc.5.1.89> (seules les métadonnées et des descriptions secondaires ont été vues).
- Wagelmans, van Hoesel, Kolen (1992), « Economic lot sizing: an O(n log n) algorithm that runs in linear time in the Wagner-Whitin case », *Operations Research* 40(1-S), S145-S156 : <https://doi.org/10.1287/opre.40.1.S145> (résumé).
- Silver et Meal (1973), *Production and Inventory Management* 14, 64-74 — référence relevée dans la page Wikipedia, non lue.
- van den Heuvel et Wagelmans (2007), « Worst case analysis for a general class of on-line lot-sizing heuristics », rapport Econometric Institute EI 2007-46 : <https://repub.eur.nl/pub/10859/> (texte lu).
- Florian, Lenstra, Rinnooy Kan (1980), « Deterministic production planning: algorithms and complexity », *Management Science* 26(7), 669-679 : <https://doi.org/10.1287/mnsc.26.7.669> (résumé) ; Bitran et Yanasse (1982), *Management Science* 28(10), 1174-1186 : <https://doi.org/10.1287/mnsc.28.10.1174> (résumé) ; Shaw et Wagelmans (1995), rapport Econometric Institute : <https://repub.eur.nl/pub/1353/> (résumé).
- Hsu (1983), « On the general feasibility test of scheduling lot sizes for several products on one machine », *Management Science* 29(1), 93-105 : <https://doi.org/10.1287/mnsc.29.1.93> (résumé).
- Trigeiro, Thomas, McClain (1989), « Capacitated lot sizing with setup times », *Management Science* 35(3), 353-366 : <https://doi.org/10.1287/mnsc.35.3.353> (résumé).
- Dobson (1988), « Sensitivity of the EOQ model to parameter estimates », *Operations Research* 36(4), 570-574 : <https://doi.org/10.1287/opre.36.4.570> (résumé).
- Erkip, cours IE375 (Bilkent, 2020), chapitre 4 partie IV : <https://courses.ie.bilkent.edu.tr/ie102/wp-content/uploads/sites/7/2020/11/Chapter-4-3.pdf> (texte lu : remises, rupture, puissances de 2, lot sizing).
- Enquêtes : Jans et Degraeve (2008), *Int. J. Production Research* 46(6) : <https://doi.org/10.1080/00207540600902262> ; Glock, Grosse, Ries (2014), *IJPE* 155 : <https://doi.org/10.1016/j.ijpe.2013.12.009> (métadonnées et résumés vus).
- Connexions brain : [[Politiques de réapprovisionnement (s,S) et (R,Q)]], [[Stock de sécurité et taux de service]], [[Modèle du vendeur de journaux (newsvendor)]], [[Programmation linéaire en nombres entiers (MIP)]], [[Optimisation combinatoire]].
