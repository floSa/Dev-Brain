---
role: notion
nom: Détection de ruptures
alias: [Change point detection, Changepoint detection, Détection de points de rupture, Segmentation de séries temporelles, CUSUM, PELT, BOCPD]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [change-point, anomaly-detection, timeseries]
---

# Détection de ruptures

## Aperçu

- Une **rupture** est un instant où les propriétés statistiques d'un signal changent (moyenne, variance, corrélation, loi complète) et **restent** changées. Détecter des ruptures, c'est découper la série en régimes homogènes ou lever une alerte dès que le régime vient de changer.
- Deux régimes d'usage, selon Truong, Oudre et Vayatis (2020) : **hors ligne** (tous les échantillons sont reçus, on segmente après coup) et **en ligne** (détecter le changement dès qu'il survient). Les mêmes auteurs notent que la seconde tâche est souvent appelée détection d'événement ou d'anomalie, et la première segmentation du signal.
- La page traite le cadre commun (coût, recherche, pénalité), quatre algorithmes (CUSUM, segmentation binaire, programmation dynamique avec PELT, BOCPD), la distinction avec l'anomalie et la dérive, et l'évaluation avec une marge de tolérance.

## Concepts clés

### Le cadre : coût, recherche, contrainte

Truong et al. décrivent toute méthode par trois éléments.

- **Le coût** $c(\cdot)$ mesure l'homogénéité d'un segment : faible si le segment ne contient pas de rupture, élevé sinon. Son choix fixe le **type de changement** détectable.
- **La recherche** résout le problème d'optimisation discret, de façon exacte ou approchée.
- **La contrainte** sur le nombre de ruptures : soit $K$ est connu, soit une pénalité arbitre entre ajustement et complexité.

Coûts décrits dans la revue, tous définis sur un segment $y_{a..b}$ :

- $c_{L2}$, l'erreur quadratique autour de la moyenne du segment : détecte un **saut de moyenne** (modèle gaussien à variance fixe, le plus ancien et le plus étudié).
- $c_\Sigma$, une vraisemblance gaussienne avec moyenne et covariance empiriques : détecte un changement des deux premiers moments.
- $c_{\text{Poisson}}$ : changement du taux d'une série de comptages.
- Des coûts non paramétriques (rang, noyau) quand aucune loi n'est supposée. La revue note que, dans l'approche par fenêtres, utiliser $c_{L2}$, $c_{\text{i.i.d.}}$ ou $c_{\text{noyau}}$ revient respectivement à un test t de Student, un test du rapport de vraisemblance généralisé et un test MMD à noyau : on hérite de la littérature des tests ([[Tests d'hypothèse]]).

### CUSUM : la somme cumulée de Page

- Plus ancien détecteur en ligne de la page. Il accumule les écarts à une moyenne de référence $\hat\mu_0$ moins une tolérance $k$, en s'arrêtant à zéro, et signale quand la somme dépasse un seuil $h$ (formules plus bas). Le manuel du NIST donne comme règle empirique $k$ égal à la moitié du décalage $\delta$ qu'on veut détecter (0,5 en unités d'écart-type) et $h$ autour de 4 ou 5.
- Il demande une **moyenne de référence** (connue ou estimée en régime sous contrôle) et se règle pour un décalage précis. Il est plus rapide que la carte de Shewhart pour les petits décalages, moins pour les grands : le détail chiffré est dans [[Contrôle statistique de procédé (SPC)]], où il est traité comme carte de contrôle.
- Le détecteur `PageHinkley` de [[River]] est présenté dans sa documentation comme l'implémentation du « CUSUM control chart » avec facteur d'oubli ; il sert à la détection de dérive dans un flux.

### Programmation dynamique et PELT

- **Opt** (programmation dynamique, $K$ connu) trouve la segmentation optimale en $O(KT^2)$ d'après Truong et al. Une variante sans $K$ (Optimal Partitioning, Jackson et al. 2005) est exacte en $O(n^2)$ d'après Killick et al.
- **PELT** (*Pruned Exact Linear Time*, Killick, Fearnhead, Eckley, JASA 2012) ajoute à cette récursion une règle d'élagage qui retire les instants candidats qui ne pourront plus jamais être la dernière rupture. Le résultat reste **exact** pour une pénalité linéaire $\beta|\mathcal T|$.
- **Condition de validité de l'élagage** : il existe une constante $K$ telle que l'ajout d'une rupture ne fait pas monter le coût de plus de $K$ ; l'article note que presque tous les coûts usuels la satisfont ($K=0$ pour moins une log-vraisemblance, $K$ égal à la pénalité pour une log-vraisemblance pénalisée).
- **Coût de calcul** : « linéaire sous des conditions faibles ». La condition qui compte est que le nombre de ruptures croisse **proportionnellement** à $n$. Truong et al. le résument en supposant des longueurs de régimes tirées uniformément. Killick et al. montrent par simulation que, si le nombre de ruptures croît plus lentement (racine carrée de $n$, ou nombre fixe), le coût n'est plus linéaire, tout en restant bien en dessous de l'Optimal Partitioning. **Pire cas : $O(n^2)$**, quand rien n'est élagué.
- Par rapport à la segmentation binaire, Killick et al. rapportent une précision supérieure à coût similaire quand le nombre de ruptures croît linéairement.

### Segmentation binaire

- Gloutonne : on trouve la rupture qui abaisse le plus la somme des coûts, on coupe le signal en deux, on recommence sur chaque morceau jusqu'à un critère d'arrêt.
- Coût de calcul $O(T\log T)$ (Truong et al.) ; Killick et al. la qualifient de méthode **approchée** la plus répandue.
- Contrepartie : chaque estimation dépend des précédentes et ne vient pas de segments homogènes. Truong et al. notent que les ruptures **proches** sont détectées de façon imprécise.
- Deux autres méthodes approchées de la revue. La **fenêtre glissante** (*Win*) mesure l'écart $d=c(y_{a..b})-c(y_{a..t})-c(y_{t..b})$ entre la fenêtre de gauche et celle de droite, puis cherche les pics de la courbe d'écart ; elle est linéaire en nombre d'échantillons et simple, avec une demi-largeur de fenêtre à régler. L'**ascendante** (*bottom-up*) part de nombreux petits segments et fusionne ceux dont l'écart est le plus faible, jusqu'à $K$ ruptures ; elle est aussi linéaire.

### BOCPD : une loi sur la longueur du run

- Adams et MacKay (2007) : algorithme bayésien en ligne qui calcule, à chaque pas, la **loi a posteriori de la durée écoulée depuis la dernière rupture** (*run length* $r_t$) par passage de messages. Les paramètres avant et après la rupture sont supposés indépendants.
- Il demande : un modèle prédictif pour les données d'un run (famille exponentielle pour une récursion exacte), et un *a priori* sur l'intervalle entre ruptures, résumé par la **fonction de hasard** $H(\tau)$. Si l'intervalle suit une loi géométrique d'échelle $\lambda$, le hasard est constant, $H=1/\lambda$.
- Le coût par pas est linéaire en nombre d'observations déjà vues. En écartant la queue de probabilité de la loi (masse totale sous un seuil, par exemple $10^{-4}$), le coût moyen devient de l'ordre de l'espérance de $r$, mais le pire cas reste linéaire.
- La sortie n'est **pas une alarme** : c'est une loi. La décision (un seuil, un mode) reste à fixer.

### Choisir la pénalité

- Pénalité linéaire (ou $\ell_0$) : $\mathrm{pen}(\mathcal T)=\beta|\mathcal T|$. Truong et al. la qualifient de choix le plus courant ; elle généralise BIC et AIC. Un $\beta$ faible produit beaucoup de régimes, y compris du bruit ; un $\beta$ élevé ne garde que les ruptures les plus fortes, voire aucune.
- Pénalités BIC de la revue : $\mathrm{pen}_{\text{BIC}}(\mathcal T)=\frac p2 \log T\,|\mathcal T|$ pour $p$ paramètres par segment, et $\sigma^2\log T\,|\mathcal T|$ pour un signal gaussien à variance $\sigma^2$ et moyenne constante par morceaux (tel qu'imprimé dans l'article). Dans ce cas, $\beta$ **suit la variance du bruit**.
- Sans modèle supposé, la revue cite la validation croisée, l'heuristique de pente, et des méthodes supervisées qui règlent $\beta$ sur des signaux annotés.
- Le choix de $\beta$ reste le point le plus fragile en pratique : il est lié à l'amplitude des changements qu'on veut voir.

### Rupture, anomalie, dérive

La distinction ci-dessous est celle de cette page, appuyée sur les sources citées là où elles existent.

- **Anomalie** (au sens de [[Types d'anomalies et régimes de supervision]]) : un point, un contexte ou un motif s'écarte d'un normal qui, lui, ne change pas. Après l'événement, le signal revient au normal. Un détecteur d'anomalies se règle sur ce normal.
- **Rupture** : le normal lui-même change et ne revient pas. Après la rupture, un détecteur d'anomalies réglé sur l'ancien normal signale presque tout, jusqu'à ce qu'on le ré-entraîne ; c'est la raison de l'existence de [[Détection d'anomalies en ligne]]. Un faux positif de rupture et une anomalie persistante (un segment collectif long) se distinguent mal : tout dépend de la durée et du modèle de coût.
- **Dérive** d'un modèle ([[Data drift]]) : un écart entre la distribution des entrées en production et celle de l'entraînement, jugé du point de vue de la performance du modèle. La page [[Data drift]] range la rupture parmi les formes de dérive (« soudain »). Même outillage statistique, mais **référence différente** : pour une rupture, le régime précédent ; pour la dérive, le jeu d'entraînement.
- Une dégradation lente de machine n'est ni une anomalie ponctuelle ni une rupture franche : la détection d'un changement de pente rejoint [[Maintenance prédictive et RUL]].

### Évaluer des ruptures

Les métriques de [[Évaluer une détection d'anomalies]] ne s'appliquent pas telles quelles : une rupture est un **instant**, et les erreurs de position comptent. Truong et al. proposent :

- **Précision / rappel avec marge** $M>0$ : une rupture vraie est détectée si une estimée tombe à moins de $M$ échantillons. Précision = part des estimées qui sont vraies, rappel = part des vraies retrouvées. Les deux sont bien définies si $M$ est plus petit que l'écart minimal entre deux vraies ruptures. La sur-segmentation envoie la précision vers 0 et le rappel vers 1, la sous-segmentation fait l'inverse.
- **Hausdorff** : la pire erreur de position entre les deux ensembles de ruptures, en nombre d'échantillons ; il pénalise sur- et sous-segmentation.
- **Indice de Rand** : proportion de paires d'indices rangées de la même façon (même segment ou segments différents) par la vérité terrain et l'estimation ; borné entre 0 et 1.
- En ligne, ajouter le **délai de détection** et le nombre de fausses alertes par durée, comme pour [[Score et seuil d'alerte]]. Ces deux grandeurs figurent dans l'ARL de [[Contrôle statistique de procédé (SPC)]].

## Les maths, simplement

- Objectif : $V(\mathcal T,y)=\sum_{k=0}^{K} c\big(y_{t_k..t_{k+1}}\big)$. Problème 1 ($K$ connu) : $\min_{|\mathcal T|=K}V$. Problème 2 ($K$ inconnu) : $\min_{\mathcal T}\ V(\mathcal T)+\mathrm{pen}(\mathcal T)$.
- Saut de moyenne : $c_{L2}(y_{a..b})=\sum_{t=a+1}^{b}\lVert y_t-\bar y_{a..b}\rVert_2^2$.
- **Élagage de PELT** (Killick et al., théorème 3.1) : s'il existe $K$ tel que $C(y_{(t+1):s})+C(y_{(s+1):T})+K\le C(y_{(t+1):T})$ pour tout $t<s<T$, alors, si $F(t)+C(y_{(t+1):s})+K\ge F(s)$, l'instant $t$ ne peut plus être la dernière rupture avant un $T>s$. Ici $F(t)$ est le coût pénalisé optimal du début à $t$.
- **CUSUM bilatéral** (NIST) : $S_{hi}(i)=\max\big(0,S_{hi}(i-1)+x_i-\hat\mu_0-k\big)$ et $S_{lo}(i)=\max\big(0,S_{lo}(i-1)+\hat\mu_0-k-x_i\big)$ ; signal quand l'une dépasse $h$.
- **BOCPD** : a priori sur le run, $P(r_t\mid r_{t-1})=H(r_{t-1}+1)$ si $r_t=0$, $1-H(r_{t-1}+1)$ si $r_t=r_{t-1}+1$, et 0 sinon ; avec $H(\tau)=\dfrac{P_{\text{gap}}(g=\tau)}{\sum_{t\ge\tau}P_{\text{gap}}(g=t)}$. La récursion combine cet a priori et la prédictive $P(x_t\mid r_{t-1},x^{(r)}_t)$ calculée sur les seules données du run en cours.
- **Conséquence (se déduit des deux lignes précédentes, l'article ne l'écrit pas)** : avec un hasard constant, la masse « rupture » et la masse « le run continue » partagent le même facteur prédictif, donc $P(r_t=0\mid x_{1:t})=H$ quelle que soit la donnée. Le signal d'une rupture se lit dans le **reste de la loi** de $r_t$ (le mode qui retombe vers zéro), pas dans $P(r_t=0)$.
- **Marge** : $\mathrm{Tp}=\{t^*\in\mathcal T^*\mid\exists\hat t\in\hat{\mathcal T},\ |\hat t-t^*|<M\}$ ; $\mathrm{Prec}=|\mathrm{Tp}|/\hat K$, $\mathrm{Rec}=|\mathrm{Tp}|/K^*$.
- Hausdorff : $\max\Big\{\max_{\hat t}\min_{t^*}|\hat t-t^*|,\ \max_{t^*}\min_{\hat t}|\hat t-t^*|\Big\}$.

## En pratique

- **Décider d'abord hors ligne ou en ligne.** Segmenter un historique pour en extraire des régimes (puis des *features* par régime) est du hors ligne : PELT avec un coût adapté. Alerter sur le flux d'une machine est du en ligne : CUSUM ou carte EWMA si le décalage visé est connu ([[Contrôle statistique de procédé (SPC)]]), BOCPD si l'on préfère une loi à une alarme.
- **Le coût encode ce qu'on cherche.** $c_{L2}$ ne voit que des sauts de moyenne : un changement de variance (usure qui augmente le bruit d'un capteur) lui échappe. Un coût qui regarde moyenne et covariance ($c_\Sigma$) ou un coût non paramétrique couvre plus, avec plus de calcul.
- **Régler la pénalité en balayant** $\beta$ et en traçant le nombre de ruptures en fonction de $\beta$ : un palier large est un signe de stabilité (usage courant, pas une garantie des sources lues). Standardiser le signal avant de comparer des $\beta$ entre séries, puisque la pénalité BIC suit la variance du bruit.
- **Retirer le déterministe d'abord.** Les coûts de la revue supposent des segments homogènes ; une saisonnalité forte ou une tendance non retirée ([[Stationarity]], [[Autocorrelation]]) risque de produire des ruptures fantômes avec un coût de moyenne. C'est une conséquence du modèle de coût, non vérifiée sur un jeu dans cette page.
- **Fixer $M$ à partir de l'exploitation**, pas de la méthode : le délai acceptable d'une alerte, converti en échantillons. Rappeler qu'il doit rester plus petit que l'écart minimal entre deux vraies ruptures.
- **Ne pas confondre alarme et rupture.** Une alarme de CUSUM dit « le niveau a quitté la référence », pas où est la rupture. Pour la dater, relancer une méthode hors ligne sur la fenêtre autour de l'alarme.
- **Étiqueter les ruptures coûte cher** : les jeux publics sont rares, l'évaluation sur un procédé réel passe par un expert qui date les changements de régime ([[Jeux de données d'anomalies]]).
- Brique dédiée : [[ruptures]], la bibliothèque Python publiée avec la revue de Truong et al. Pour le CUSUM et BOCPD côté code, [[Kats]] (page d'accueil de sa documentation, relue le 2026-10-02 : détection de saisonnalités, outliers, points de rupture et changements de tendance ; les détecteurs précis sont décrits dans la fiche de la brique).

## Approches voisines & alternatives

- [[Contrôle statistique de procédé (SPC)]] — le CUSUM et l'EWMA y sont des cartes de contrôle, avec leurs ARL ; la rupture y est un « décalage ».
- [[Détection d'anomalies en ligne]] — le détecteur qui doit survivre à la rupture, avec ses fenêtres d'oubli et ses détecteurs de dérive.
- [[Time series anomaly detection]] — le cas général, ruptures comprises.
- [[Data drift]] — la dérive d'un modèle en production, vue du côté de la performance.
- [[Sequential testing]] — l'arrêt optimal d'un test à mesure que les données arrivent, proche du CUSUM par l'accumulation d'un rapport de vraisemblance (rapprochement de cette page, non sourcé).
- [[Inférence bayésienne]] et [[Modèles de Markov cachés et filtre de Kalman]] — la famille bayésienne que Truong et al. écartent de leur revue ; BOCPD en relève, comme les HMM.
- [[Maximum de vraisemblance]] — d'où dérive le coût $c_{\text{i.i.d.}}$.
- [[Maintenance prédictive et RUL]] — le changement de pente d'un indicateur de santé comme amorce de dégradation.
- [[Types d'anomalies et régimes de supervision]] — l'anomalie collective, la plus proche d'une rupture transitoire.
- [[Évaluer une détection d'anomalies]] — les métriques par événement, applicables à la détection de ruptures avec adaptation.

## Pour aller plus loin

- Truong, Oudre, Vayatis (2020), *Selective review of offline change point detection methods*, Signal Processing 167. arXiv : https://arxiv.org/abs/1801.00718
- Killick, Fearnhead, Eckley (2012), *Optimal detection of changepoints with a linear computational cost*, JASA 107(500). arXiv : https://arxiv.org/abs/1101.1438
- Adams, MacKay (2007), *Bayesian Online Changepoint Detection*. arXiv : https://arxiv.org/abs/0710.3742
- Page (1954), *Continuous inspection schemes*, Biometrika 41(1/2), 100-115 — origine du CUSUM ; non relu, cité par Truong et al. et par la documentation de River.
- NIST/SEMATECH e-Handbook of Statistical Methods, §6.3.2.3, *CUSUM Control Charts* : https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc323.htm
- Documentation de River, `drift.PageHinkley` : https://riverml.xyz/latest/api/drift/PageHinkley/
