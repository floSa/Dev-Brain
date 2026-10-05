---
role: notion
nom: Contrôle statistique de procédé (SPC)
alias: [SPC, Statistical process control, Maîtrise statistique des procédés, Cartes de contrôle, Control charts, Carte de Shewhart, Cartes EWMA, Capabilité de procédé, Cpk, Western Electric, Average run length]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [statistical-process-control, anomaly-detection, timeseries]
---

# Contrôle statistique de procédé (SPC)

## Aperçu

- Le SPC surveille un procédé **dans le temps** avec des **cartes de contrôle** : une statistique est tracée point par point autour d'une ligne centrale, entre des limites haute et basse. Selon le manuel du NIST, le procédé est jugé sous contrôle quand tous les points sont dans les limites et qu'aucun motif systématique n'apparaît ; il est hors contrôle dès qu'un point sort des limites ou que les points suivent un motif non aléatoire.
- **Rangement.** La page est en `ml/anomalie` et non en `stats/*` parce que son sujet est l'**écart au normal d'un procédé suivi dans le temps et la décision d'alerte** qui en découle (règle D-R10 de la taxonomie), et non l'estimation d'un paramètre ni le test d'une hypothèse, même si une carte se lit comme une suite de tests.
- Deux questions à ne pas mélanger : le procédé est-il **stable** (cartes de contrôle) et est-il **conforme** aux spécifications (indices de capabilité $C_p$, $C_{pk}$) ? Le manuel du NIST précise que la capabilité compare la sortie d'un procédé **sous contrôle** aux limites de spécification : sans stabilité, l'indice ne veut rien dire.
- Les cartes sont les ancêtres de la détection d'anomalies sur série temporelle : le CUSUM et l'EWMA y servent encore de références, et le seuil à $3\sigma$ de [[Détection d'outliers univariée]] en est le cas sans ordre temporel.

## Concepts clés

### Carte de Shewhart et limites à $3\sigma$

- Modèle général : pour une statistique d'échantillon $w$ de moyenne $\mu_w$ et d'écart-type $\sigma_w$, ligne centrale $\mu_w$, limites $\mu_w\pm k\sigma_w$. Avec $k=3$ on parle de carte à $3\sigma$, « un standard accepté dans l'industrie » d'après le NIST.
- Pour des données normales, les limites à $3\sigma$ équivalent à des limites de probabilité 0,001 de chaque côté. Quand la loi est asymétrique, le risque réel monte : le NIST cite le passage de 0,001 à 0,009 dans certains cas d'une loi de Poisson.
- **$\bar X$ et $R$** (sous-groupes de taille $n$) : limites de $\bar X$ à $\bar{\bar x}\pm A_2\bar R$ ; carte $R$ entre $D_3\bar R$ et $D_4\bar R$, avec $A_2=3/(d_2\sqrt n)$, $D_3=1-3d_3/d_2$, $D_4=1+3d_3/d_2$ ($d_2$ et $d_3$ tabulés en fonction de $n$). Variante $\bar X$ et $S$ avec la constante $c_4$.
- **Mesures individuelles (I-MR)**, quand il n'y a pas de sous-groupe (un capteur, une mesure par pas) : étendue mobile $MR_i=|x_i-x_{i-1}|$, et limites $\bar x\pm 3\,\overline{MR}/1{,}128$ ; $1{,}128$ est $d_2$ pour $n=2$. Variante avec l'écart-type : $\bar x\pm 3s/c_4$. Les paramètres sont estimés sur des **échantillons préliminaires**.
- Les pages du NIST lues ne mentionnent pas l'autocorrélation. Voir plus bas : c'est l'hypothèse qui casse en premier sur des données de capteurs.

### Le CUSUM : accumuler les petits écarts

- Somme cumulée de Page (1954), à sens unique : $S_{hi}$ accumule $x_i-\hat\mu_0-k$ et reste à zéro tant que la somme est négative ; $S_{lo}$ fait de même pour la baisse. Le procédé est hors contrôle quand l'une dépasse $h$.
- Réglage (NIST) : $k=\delta\sigma_x/2$ pour un décalage visé $\delta$ ; règle empirique $k$ = la moitié du décalage (0,5 en unités d'écart-type) et $h$ autour de 4 ou 5.
- Le NIST juge le CUSUM plus efficace pour des décalages de moyenne de **$2\sigma$ ou moins**.
- Le même mécanisme sert à la détection de ruptures et de dérive : [[Détection de ruptures]].

### La carte EWMA : une mémoire qui s'estompe

- $\mathrm{EWMA}_t=\lambda Y_t+(1-\lambda)\,\mathrm{EWMA}_{t-1}$ avec $0<\lambda\le 1$ et $\mathrm{EWMA}_0$ la moyenne historique. Limites $\mathrm{EWMA}_0\pm k\,s_{\mathrm{ewma}}$, avec $s^2_{\mathrm{ewma}}=\dfrac{\lambda}{2-\lambda}s^2$ et $k$ typiquement égal à 3.
- Le NIST donne $\lambda$ entre 0,2 et 0,3 comme valeur usuelle, renvoie aux tables de Lucas et Saccucci (1990) pour le choix de $\lambda$ et des limites, et note que la carte « peut être rendue sensible à une dérive petite ou graduelle » là où une carte de Shewhart ne réagit qu'à un point isolé.

### Règles supplémentaires : Western Electric et Nelson

Une carte de Shewhart seule ne voit que le point hors limites. Des règles de séquences augmentent la sensibilité aux petits décalages, et le nombre de fausses alertes.

- **Western Electric** (*Statistical Quality Control Handbook*, 1956), quatre règles :
  1. un point au-delà de $3\sigma$ ;
  2. deux points sur trois consécutifs au-delà de $2\sigma$, du même côté ;
  3. quatre points sur cinq consécutifs au-delà de $1\sigma$, du même côté ;
  4. huit points consécutifs du même côté de la ligne centrale.
- **Nelson** (Journal of Quality Technology, 1984) en liste huit. Telles que les rapportent deux sources secondaires : un point au-delà de $3\sigma$ ; **neuf** points du même côté ; six points en tendance ; quatorze points qui alternent haut-bas ; deux points sur trois au-delà de $2\sigma$ ; quatre sur cinq au-delà de $1\sigma$ ; quinze points consécutifs dans $\pm 1\sigma$ ; huit points consécutifs hors de $\pm 1\sigma$ des deux côtés.
- **Désaccords entre sources.** Western Electric dit **huit** points du même côté, Nelson **neuf**. Pour la règle « deux sur trois », Wikipédia écrit « deux ou trois sur trois », l'autre source « 2 sur 3 ». **Les sources primaires (le manuel de 1956, l'article de Nelson) n'ont pas été relues** : à vérifier avant de coder ces règles.
- Taux de fausses alertes : un point seul hors de $3\sigma$ se déclenche par hasard une fois sur 370 en moyenne ; en cumulant les quatre règles de Western Electric, une fois sur 91,75 environ (Champ et Woodall, *Technometrics*, 1987, d'après Wikipédia ; l'article en donne le calcul exact par chaîne de Markov). Plus on applique de règles, plus les fausses alertes montent.

### ARL : la longueur moyenne d'un run

- ARL (*average run length*) : nombre moyen d'échantillons (ou de sous-groupes) tracés avant un signal. Sous contrôle, on la veut **grande** ($\mathrm{ARL}_0$ : fausses alertes) ; après un décalage, **petite** ($\mathrm{ARL}_1$ : délai de détection).
- Carte $\bar X$ à $3\sigma$ sans changement : $\mathrm{ARL}\approx 371$, soit $p=0{,}0027$ par point.
- Tableau du NIST pour un décalage de moyenne (en $\sigma$), CUSUM avec $k=0{,}5$ contre Shewhart :

| Décalage | CUSUM $h=4$ | CUSUM $h=5$ | Shewhart |
|---|---|---|---|
| 0 | 336 | 930 | 371 |
| 0,5 | 26,6 | 30,0 | 155,22 |
| 1,0 | 8,38 | 10,4 | 44,0 |
| 1,5 | 4,75 | 5,75 | 14,97 |
| 2,0 | 3,34 | 4,01 | 6,30 |

  Lecture du NIST : « Shewhart supérieur pour les grands décalages, CUSUM plus rapide pour les petits ». À $h=5$, le CUSUM a en outre un $\mathrm{ARL}_0$ de 930 : moins de fausses alertes que Shewhart **et** plus de réactivité sur un décalage de $1\sigma$.
- L'ARL se compte en **échantillons**, pas en minutes. À une mesure par seconde, un $\mathrm{ARL}_0$ de 370 fait une fausse alerte toutes les six minutes environ ($370\ \text{s}\approx 6{,}2$ min, calcul de cette page).

### Capabilité : $C_p$ et $C_{pk}$

- $C_p=\dfrac{USL-LSL}{6\sigma}$ compare la **largeur** de la tolérance à la dispersion du procédé ; il ignore le **centrage**.
- $C_{pk}=\min\!\Big[\dfrac{USL-\mu}{3\sigma},\dfrac{\mu-LSL}{3\sigma}\Big]$ prend le côté le plus proche d'une limite. Centré, $C_{pk}=C_p$ ; décentré, $C_{pk}<C_p$.
- Hypothèses du NIST : données normales, procédé sous contrôle, au moins 50 valeurs **indépendantes** (100 recommandées) pour une étude de capabilité. Valeur souhaitée de $C_{pk}$ : au moins 1,0 selon le NIST ; d'autres secteurs exigent plus, et ce seuil n'est pas fixé par les sources lues ici.
- Exemple chiffré (valeurs inventées pour la page) : $LSL=9{,}4$, $USL=10{,}6$, $\sigma=0{,}1$, moyenne $10{,}3$. Alors $C_p=2{,}0$ mais $C_{pk}=(10{,}6-10{,}3)/0{,}3=1{,}0$ ; sous normalité, environ 0,135 % de la production dépasse $USL$, soit 1 350 ppm. Un $C_p$ de 2 seul ne dit rien de ce décentrage.

## Les limites sous autocorrélation

Les cartes de Shewhart, CUSUM et EWMA supposent des observations **indépendantes**. Un capteur échantillonné vite ne les donne presque jamais ([[Autocorrelation]]).

### Ce que les sources disent

- Thaga et Yadavalli (2007), en résumé de la littérature : une autocorrélation **positive** biaise négativement l'estimateur de l'écart-type, d'où des limites « beaucoup plus serrées que souhaité » et un taux de fausses alertes bien supérieur au taux annoncé.
- Deux familles de réponses. (a) Garder les cartes sur les observations, en corrigeant limites et estimation des paramètres (VanBrackle et Reynolds 1997 ; Lu et Reynolds 1999) : adapté quand l'autocorrélation est **faible**. (b) **Ajuster un modèle de série temporelle**, prévoir chaque observation à partir des précédentes, et tracer les **résidus** sur une carte classique (Alwan et Roberts 1988 ; Montgomery et Mastrangelo 1991 ; Wardell, Moskowitz et Plante 1994 ; Lu et Reynolds 1999) : si le modèle ajusté est le vrai et les paramètres exacts, les résidus sont indépendants et de même loi normale sous contrôle. Yashchin recommande de tracer les données brutes quand l'autocorrélation est faible et une transformation en résidus quand elle est élevée.
- Alwan et Roberts (1988) appellent cette carte « carte de cause spéciale » (SCC) : résidus du modèle sur une carte de contrôle, valeurs ajustées tracées à part pour les effets systématiques. La page n'a lu que ce résumé, pas l'article.
- **Le coût de l'approche par résidus** : si l'autocorrélation est positive, un décalage de la moyenne du procédé n'est transmis aux résidus que **pour une fraction**, et la carte le détecte lentement. Les cartes de résidus fonctionnent mieux quand l'autocorrélation est **forte** ; quand elle est faible, la prévision est difficile et ces cartes sont peu efficaces (Thaga et Yadavalli).
- **Désaccord.** Dans la documentation SAS, trois positions : Wheeler (1991) juge qu'il n'y a pas lieu de trop s'inquiéter de l'effet de l'autocorrélation sur la carte, sauf au-delà d'environ 0,80 ; l'automatique (APC) voit l'autocorrélation comme un phénomène à **exploiter** par réglage continu du procédé ; Alwan et Roberts préconisent le filtrage par modèle puis la carte sur les résidus (Shewhart, EWMA ou CUSUM).

### Un calcul à reproduire

Pour un AR(1) stationnaire de coefficient $\phi$, $\mathrm{Var}(x_t-x_{t-1})=2\sigma_x^2(1-\phi)$. L'estimateur $\overline{MR}/1{,}128$ des cartes I-MR vise donc $\sigma_x\sqrt{1-\phi}$ au lieu de $\sigma_x$ (déduit de la formule ; la simulation ci-dessous confirme). Simulation de cette page (200 000 points gaussiens AR(1), limites $\bar x\pm 3\,\overline{MR}/1{,}128$, un seul point hors limites comme règle) :

| $\phi$ | $\hat\sigma/\sigma_x$ | fausses alertes par point | ARL approchée |
|---|---|---|---|
| 0 | 1,00 | 0,0027 | 365 |
| 0,3 | 0,84 | 0,0118 | 85 |
| 0,5 | 0,71 | 0,0338 | 30 |
| 0,7 | 0,55 | 0,1007 | 10 |
| 0,9 | 0,32 | 0,3412 | 3 |

La documentation SAS ne dit pas quel estimateur de $\sigma$ suppose Wheeler, et ce tableau ne le contredit ni ne le confirme pour tous les estimateurs. Avec **l'étendue mobile**, estimateur standard des mesures individuelles, le taux d'alerte par point est déjà multiplié par 4 à $\phi=0{,}3$ et par 12 à $\phi=0{,}5$ ; avec l'écart-type global, les limites ne se resserrent pas de cette façon (non simulé ici).

Côté résidus, un saut $\delta$ de la moyenne d'un AR(1) donne un premier résidu égal à $\delta$, puis un résidu qui décroît vers $(1-\phi)\delta$ (cohérent avec Thaga et Yadavalli). Rapporté à l'écart-type des résidus $\sigma_\varepsilon=\sigma_x\sqrt{1-\phi^2}$, un saut de $1\,\sigma_x$ finit par peser $\sqrt{(1-\phi)/(1+\phi)}$ : environ $0{,}42\,\sigma_\varepsilon$ pour $\phi=0{,}7$.

## Les maths, simplement

- Carte de Shewhart : $UCL=\mu_w+k\sigma_w$, $LCL=\mu_w-k\sigma_w$, $k=3$.
- Faux positif d'un point à $3\sigma$ sous normalité : $p=2\,(1-\Phi(3))\approx 0{,}0027$ ; $\mathrm{ARL}_0=1/p\approx 370$ (371 dans le manuel du NIST).
- Cartes à plusieurs variables : $m$ cartes indépendantes à $\mathrm{ARL}_0=370$ déclenchent en moyenne $m/370$ fausses alertes par instant (calcul de cette page, sous indépendance). Le manuel du NIST traite des cartes multivariées (Hotelling, composantes principales, EWMA multivarié), non relues ici.
- CUSUM : $S_{hi}(i)=\max(0,\,S_{hi}(i-1)+x_i-\hat\mu_0-k)$ ; $k=\delta\sigma_x/2$ ; $h=dk$ avec $d=\dfrac{2}{\delta^2}\ln\dfrac{1-\beta}{\alpha}$ d'après le NIST.
- EWMA : $z_t=\lambda x_t+(1-\lambda)z_{t-1}$, variance asymptotique $\dfrac{\lambda}{2-\lambda}\sigma^2$.
- Capabilité : $C_p=\dfrac{USL-LSL}{6\sigma}$ ; $C_{pk}=\min\big(C_{pu},C_{pl}\big)$.

## En pratique

- **Un capteur rapide n'est pas un procédé en sous-groupes.** Pour un flux de mesures individuelles : I-MR en vérifiant [[Autocorrelation]] d'abord ; si elle est forte, tracer les résidus d'un modèle de prévision ([[Forecasting framing]], [[ARIMA SARIMA]]) et recalibrer les limites sur ces résidus. C'est le « score par résidu standardisé » de [[Time series anomaly detection]], avec un cadre plus ancien et un vocabulaire de fausses alertes déjà installé.
- **Le modèle de résidu a son propre défaut** : un modèle qui s'adapte trop vite absorbe la dérive qu'on veut voir (risque propre au filtrage, non mesuré ici) ; un modèle figé accumule des fausses alertes dès que le régime change ([[Stationarity]]). Revoir le modèle à intervalle fixé.
- **Choisir la carte selon le décalage visé.** Grands sauts : Shewhart. Petites dérives de moyenne : CUSUM ou EWMA (NIST). Un changement de variance demande une carte de dispersion ($R$, $S$, MR) ou une carte « Max », qui surveille moyenne et dispersion ensemble (Thaga et Yadavalli, cités plus bas).
- **Chiffrer le budget d'alertes avant de poser les limites** : $\mathrm{ARL}_0$ visé $\times$ période d'échantillonnage = temps moyen entre fausses alertes. Régler ensuite $k$, $h$, $\lambda$ pour garder un $\mathrm{ARL}_1$ acceptable sur le décalage qui compte en maintenance ([[Maintenance prédictive et RUL]]).
- **Du signal à l'alerte** : une carte rend une décision binaire déjà seuillée. Le choix du seuil, le coût d'une fausse alerte contre un défaut manqué et la fatigue d'alerte sont traités dans [[Score et seuil d'alerte]] ; l'ARL en est la traduction pour un procédé échantillonné. Une alerte de carte dit que le procédé est hors contrôle, pas pourquoi : ce n'est pas un diagnostic de panne.
- **Ne pas cumuler les règles par réflexe.** Chaque règle ajoutée abaisse l'ARL sous contrôle : choisir un jeu de règles et en mesurer le taux d'alerte sur une période propre.
- **Normes.** Des normes ISO existent sur les cartes de contrôle et la capabilité ; aucune n'a été lue pour cette page et aucun numéro n'est donné ici.

## Approches voisines & alternatives

- [[Détection de ruptures]] — le CUSUM comme détecteur de changement de régime, PELT et BOCPD pour localiser la rupture.
- [[Détection d'anomalies en ligne]] — des détecteurs appris sur un flux, sans hypothèse de loi sur le normal.
- [[Détection d'outliers univariée]] — Z-score, IQR, MAD : le seuil à $3\sigma$ sans ordre temporel.
- [[Score et seuil d'alerte]] — du score à l'alerte, choix de coût.
- [[Time series anomaly detection]] — le cas général ; le score par résidu y reprend la carte de résidus.
- [[Autocorrelation]] et [[Stationarity]] — les hypothèses des cartes, et ce qui les brise.
- [[Sequential testing]] — la version « test statistique » de l'arrêt dès qu'une preuve est suffisante.
- [[Tests d'hypothèse]] — chaque point de carte est un test ; la carte répète ce test à chaque instant, d'où l'ARL.
- [[Théorie des valeurs extrêmes]] — les seuils à risque très bas de SPOT (voir [[Score et seuil d'alerte]]) remplacent le $3\sigma$ gaussien par une queue estimée.
- [[Maintenance prédictive et RUL]] — la surveillance d'un indicateur de santé est un usage naturel des cartes (rapprochement de cette page).
- [[OEE et rendement global]] — un indicateur d'atelier qu'on surveille contre ses limites naturelles.

## Pour aller plus loin

- NIST/SEMATECH e-Handbook of Statistical Methods, §6.3, *Univariate and Multivariate Control Charts* : https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc3.htm — pages lues : `pmc31` (https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm), `pmc32` (variables), `pmc321` ($\bar X$, $R$, $S$, ARL), `pmc322` (mesures individuelles), `pmc323` (CUSUM), `pmc3231` (ARL du CUSUM), `pmc324` (EWMA).
- NIST, §6.1.6, indices de capabilité : https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm
- Page (1954), *Continuous inspection schemes*, Biometrika 41(1/2), 100-115 — non relu ; cité par Thaga et Yadavalli et par la documentation de River.
- Alwan, Roberts (1988), *Time-series modeling for statistical process control*, Journal of Business & Economic Statistics 6(1), 87-95 — non relu ; seul un résumé a été retrouvé.
- Thaga, Yadavalli (2007), *Max-EWMA chart for autocorrelated processes*, South African Journal of Industrial Engineering 18(2). PDF : https://sajie.journals.ac.za/pub/article/download/123/119/133
- Documentation SAS, *Autocorrelation in Process Data* (trois positions) : https://support.sas.com/documentation/cdl/en/qcug/66114/HTML/default/qcug_shewhart_sect550.htm
- Western Electric (1956), *Statistical Quality Control Handbook* ; Nelson (1984), *The Shewhart Control Chart — Tests for Special Causes*, Journal of Quality Technology 16(4) (pages 238-239 selon Wikipédia) — non relus ; Wikipédia : https://en.wikipedia.org/wiki/Western_Electric_rules et https://en.wikipedia.org/wiki/Nelson_rules
- Champ, Woodall (1987), *Exact Results for Shewhart Control Charts with Supplementary Runs Rules*, Technometrics 29(4) : https://scholars.georgiasouthern.edu/en/publications/exact-results-for-shewhart-control-charts-with-supplementary-runs-12/ (résumé lu).
- Montgomery, Mastrangelo (1991), *Some statistical process control methods for autocorrelated data*, Journal of Quality Technology 23, 179-193 — non relu ; cité par Thaga et Yadavalli.
