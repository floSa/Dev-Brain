---
role: notion
nom: Indicateurs de santé
alias: [Health indicator, Health index, Indice de santé, Indicateur de santé]
categorie: ml/maintenance
domaines: [data-sci, mlops]
tags: [predictive-maintenance, rul, condition-monitoring, dimensionality-reduction, multivariate, feature-engineering]
---

# Indicateurs de santé

## Aperçu

- Un **indicateur de santé** (HI, *health indicator*) résume en une courbe, par machine et dans le temps, l'état d'un équipement. Il se place entre les mesures brutes et le pronostic : c'est lui que l'on seuille ou que l'on extrapole pour obtenir un RUL.
- [[Maintenance prédictive et RUL]] le pose en une phrase (fusion de capteurs, PCA, agrégats) et traite surtout la cible RUL. Cette page approfondit trois points laissés de côté : **comment fusionner** les capteurs (PCA, distance de Mahalanobis), **comment juger** un indicateur (monotonie, tendance, pronosticabilité), **comment poser le seuil de panne** et où il casse.
- Lei et al. (2018) découpent la chaîne de pronostic en quatre étapes : acquisition des données, construction de l'indicateur, division en stades de santé, prédiction du RUL. L'indicateur est donc un maillon, pas une fin.

## Concepts clés

### Partir d'une grandeur ou en fusionner plusieurs

- Un HI peut être **une seule caractéristique** déjà informative (par exemple RMS ou kurtosis d'un signal de vibration, voir [[Analyse vibratoire]]) ou une **fusion** de plusieurs capteurs et caractéristiques. La fusion paie quand aucune grandeur seule ne suit l'usure sur toutes les machines.
- Avant toute fusion : mettre à l'échelle ([[Mise à l'échelle]]) avec des statistiques calculées sur une période **saine** de référence, et séparer les régimes de marche ([[Types d'anomalies et régimes de supervision]]).

### Fusion par PCA

- On ajuste une [[PCA]] sur la période saine de la machine, on projette la série entière, et on lit deux statistiques : $T^2$, la distance dans le sous-espace retenu, et $Q$ (aussi appelée SPE), l'erreur de reconstruction hors de ce sous-espace.
- $T^2$ attrape un déplacement le long des directions déjà connues de variation ; $Q$ attrape l'apparition d'une structure nouvelle, que le modèle sain ne sait pas décrire. Les limites de contrôle de $Q$ viennent de Jackson et Mudholkar (1979).
- Variante : la première composante comme HI. Elle est simple, mais son **signe est arbitraire** et elle ne suit la dégradation que si celle-ci porte la plus grande variance. À contrôler, pas à supposer.

### Distance de Mahalanobis

- Estimer moyenne $\mu_0$ et covariance $\Sigma_0$ sur le régime sain, puis mesurer l'écart de chaque observation : une distance **sans unité**, qui tient compte des corrélations entre capteurs. L'équipe du CALCE (Université du Maryland) l'a employée pour la détection de défaut, l'isolation, la détection de dégradation et le pronostic sur des systèmes électroniques (Kumar, thèse sous la direction de Pecht, 2009).
- Sous l'hypothèse gaussienne, le carré de la distance suit une loi du $\chi^2$ à $p$ degrés de liberté : cela donne un seuil d'**anomalie** par quantile (déjà vu dans [[Détection d'outliers multivariée]]).
- Piège : si des capteurs sont presque colinéaires, $\Sigma_0$ est mal conditionnée et son inverse amplifie le bruit. Réduire d'abord les dimensions (c'est alors $T^2$ de la PCA), ou régulariser la covariance. Une référence « saine » qui contient déjà un début de dérive fausse la distance entière.

### Juger un indicateur : trois critères et trois définitions

Coble et Hines (PHM 2009) ont formalisé trois qualités d'un paramètre de pronostic, sur un ensemble de $M$ machines suivies jusqu'à la panne ; $x_j$ est la série de la machine $j$ et $N_j$ sa longueur.

- **Monotonie** : le HI va-t-il dans un seul sens, sachant qu'une machine ne se « répare » pas d'elle-même ? Version de Coble et Hines, par machine : $\left|\dfrac{\#(\Delta x>0)}{n-1}-\dfrac{\#(\Delta x<0)}{n-1}\right|$, puis moyenne sur la population. MathWorks reprend cette forme (signe des différences) et propose une variante par corrélation de rangs de Spearman. Les auteurs notent que l'hypothèse tombe pour les batteries, qui peuvent se régénérer à l'arrêt, et qu'il faut **lisser** avant de dériver.
- **Pronosticabilité** : les valeurs finales (à la panne) sont-elles groupées ? $\exp\!\Big(-\dfrac{\operatorname{std}_j\,x_j(N_j)}{\operatorname{mean}_j\,|x_j(1)-x_j(N_j)|}\Big)$. Plus l'écart-type des valeurs de fin est faible devant l'amplitude parcourue, plus un seuil unique a un sens.
- **Tendance** (*trendability*) : les machines suivent-elles la même forme ? C'est ici que les définitions divergent.
  - Coble et Hines (2009) : $1-\operatorname{std}(t_i)$, avec $t_i$ la fraction de dérivées premières positives plus celle des dérivées secondes positives de la machine $i$ ; ils précisent que cette forme est « particulièrement sensible au bruit ».
  - MathWorks : $\min_{j,k}|\operatorname{corr}(x_j,x_k)|$, la plus faible corrélation entre deux machines.
  - Sun et al. (2025) : la corrélation de Pearson, **au sein d'une machine**, entre le HI et le temps de fonctionnement ; ils ajoutent une **robustesse** $\frac1K\sum_k \exp\!\big(-|y_k-y_k^{tr}|/y_k\big)$ où $y^{tr}$ est une version lissée du HI.
- Conséquence : un « score de tendance de 0,9 » n'a de sens qu'avec sa définition. Les formules de Lei et al. (2018) pour ces critères n'ont pas été relues dans l'article ; elles ne sont pas reprises ici.

### Seuil de panne

- Deux seuils à ne pas confondre (Li et Gryllias, PHM 2024) : le seuil d'**anomalie**, qui dit quand la dégradation commence (voir [[Score et seuil d'alerte]]), et le seuil de **panne**, valeur du HI à laquelle on déclare la fin de vie et que l'on atteint par extrapolation pour obtenir le RUL.
- **Fixe ou dynamique.** Un seuil fixe suppose que, pour un type de roulement, la valeur du HI à la panne est la même ; il demande beaucoup de mesures de fin de vie. Un seuil dynamique se règle sur l'historique de chaque machine (Li et Gryllias, travail de doctorat présenté comme perspective). Pour des systèmes aux caractéristiques variables, Bender, Schinke et Sextro (2019) jugent les seuils fixes insuffisants et comparent des seuils adaptatifs dans un filtre particulaire.

## Les maths, simplement

- Mahalanobis : $d_M(x)=\sqrt{(x-\mu_0)^\top\Sigma_0^{-1}(x-\mu_0)}$ (`scipy.spatial.distance.mahalanobis` attend l'**inverse** de la covariance, pas la covariance).
- PCA à $k$ composantes retenues, scores $t_j$ et valeurs propres $\lambda_j$ calculés sur le sain : $T^2=\sum_{j\le k} t_j^2/\lambda_j$ et $Q=\|x-\hat x\|^2=\sum_{j>k} t_j^2$ (en gardant toutes les composantes, $T^2$ redevient le carré de la distance de Mahalanobis).
- Sketch essayé sur des données synthétiques (dérive de deux capteurs sur six, référence = les 200 premiers points) :

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
sc = StandardScaler().fit(X_sain); Z = sc.transform(X)
pca = PCA(n_components=2).fit(sc.transform(X_sain))
T = pca.transform(Z)
T2 = (T**2 / pca.explained_variance_).sum(axis=1)
Q  = ((Z - pca.inverse_transform(T))**2).sum(axis=1)
```

## En pratique

- **Calibrer sur du sain, par machine** : la référence est la période de début de vie de la machine concernée, pas la moyenne du parc. Elle doit rester hors de la fenêtre qu'on évalue.
- **Les critères ne se calculent pas sur le test.** Choisir le HI (ou ses poids) en maximisant monotonie et pronosticabilité sur les machines qu'on évalue ensuite, c'est de la fuite ([[Data leakage]]) : les critères regardent la fin de vie. Choisir sur un groupe de machines, évaluer sur un autre.
- **Optimiser le HI sur ces critères le rend lisse, pas juste.** Coble et Hines optimisent justement leur somme par algorithme génétique. Un HI monotone peut avoir perdu l'information utile ; vérifier qu'il bouge bien avec les défauts connus ([[Diagnostic de défauts de roulements]]).
- **Seuil de panne issu de peu d'unités** : si le seuil se règle sur les seules machines allées jusqu'à la panne, les machines encore en service (censurées) sont ignorées et la valeur de fin est biaisée. Le cadre de survie traite la censure : [[RUL par analyse de survie]].
- **Un seuil se juge à son coût**, pas à son erreur de RUL seule : [[Politique de maintenance et coût]].
- **Peu de pannes, peu de machines** : toutes ces statistiques sont des moyennes sur $M$ unités ; avec $M$ petit elles sont fragiles. Voir [[Maintenance prédictive avec peu de pannes]].
- **Dérive des capteurs ou de la référence** : [[Data drift]]. Une recalibration change l'échelle du HI et rompt la comparabilité dans le temps.
- Pour la validation temporelle : [[Walk-forward CV]] et découpage par machine.

## Approches voisines & alternatives

- [[Maintenance prédictive et RUL]] — le cadre, la cible RUL, les scores de pronostic.
- [[PCA]] et [[Détection d'outliers multivariée]] — les deux briques statistiques de la fusion.
- [[Autoencodeurs]] — HI appris : l'erreur de reconstruction joue le rôle de $Q$. Travaux récents : Sun et al. (2025, autoencodeur à connexions résiduelles et bloc de prédiction interne, jeux PHM 2012 et HIT-B), Choo et al. (arXiv 2603.10430, mars 2026, adaptation de domaine) et Thil et al. (arXiv 2511.21208, nov. 2025, groupes de capteurs) ; résumés de l'API arXiv, articles non relus.
- [[Time series feature engineering]] — les caractéristiques candidates.
- [[RUL par apprentissage profond]] — contourne le HI en prédisant le RUL de bout en bout.
- [[Surveillance conditionnelle et modes de défaillance]] — quels capteurs pour quel mode de défaillance.
- [[Jeux de données PHM]] — où essayer ces critères.

## Pour aller plus loin

- Coble & Hines (2009), *Identifying Optimal Prognostic Parameters from Data: A Genetic Algorithms Approach*, Annual Conference of the PHM Society 1(1). https://papers.phmsociety.org/index.php/phmconf/article/view/1404
- Lei, Li, Guo, Li, Yan, Lin (2018), *Machinery health prognostics: A systematic review from data acquisition to RUL prediction*, MSSP 104, 799-834. DOI : https://doi.org/10.1016/j.ymssp.2017.11.016
- Sun, Yin, Zheng, Dong (2025), *An Unsupervised Framework for Dynamic Health Indicator Construction and Its Application in Rolling Bearing Prognostics*, arXiv:2506.05438. https://arxiv.org/abs/2506.05438
- Jackson & Mudholkar (1979), *Control Procedures for Residuals Associated With Principal Component Analysis*, Technometrics 21(3), 341-349. DOI : https://doi.org/10.1080/00401706.1979.10489779
- Kumar (2009), *Development of Diagnostic and Prognostic Methodologies for Electronic Systems Based on Mahalanobis Distance*, thèse, Université du Maryland. https://drum.lib.umd.edu/items/5ceee970-c9c8-4cba-9e6c-fe88e00b53d2
- Li & Gryllias (2024), *Remaining Useful Life Prognostics of Rolling Element Bearings Based on State Estimation Techniques*, PHM Society. https://papers.phmsociety.org/index.php/phmconf/article/download/4179/phmc_24_4179
- Bender, Schinke, Sextro (2019), *Remaining useful lifetime prediction based on adaptive failure thresholds*, ESREL 2019, 1262-1269. https://ris.uni-paderborn.de/record/13460
- MathWorks, [monotonicity](https://www.mathworks.com/help/predmaint/ref/monotonicity.html), [prognosability](https://www.mathworks.com/help/predmaint/ref/prognosability.html), [trendability](https://www.mathworks.com/help/predmaint/ref/trendability.html) ; SciPy, [mahalanobis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.mahalanobis.html).
