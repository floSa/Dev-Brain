---
role: notion
nom: De la prévision probabiliste à la quantité commandée
alias: [prescriptive analytics (stock), estimate-then-optimize, predict-then-optimize, decision-focused learning, big data newsvendor, prévision probabiliste et décision]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [inventory, newsvendor, forecasting, calibration, optimization]
---

# De la prévision probabiliste à la quantité commandée

## Aperçu

- Une prévision ponctuelle répond à « combien en moyenne ? ». Une quantité à commander répond à « combien, pour que le risque de rupture reste à tel niveau ? ». La seconde est un **quantile** de la demande, au niveau du fractile critique du [[Modèle du vendeur de journaux (newsvendor)]].
- Cette page est la couture entre [[Séries temporelles]] (prévoir) et la recherche opérationnelle (décider). Elle ne reprend ni les métriques ([[Forecasting metrics]]) ni le calcul du stock de sécurité ([[Stock de sécurité et taux de service]]).
- Quatre pièges : demander au modèle la mauvaise statistique, **sommer des quantiles de périodes**, croire un quantile natif calibré, évaluer sur MAPE ou RMSE plutôt que sur le coût de la décision.
- Les chiffres « simulés » ci-dessous viennent d'un script exécuté (numpy, graine fixée, 10⁶ à 2·10⁶ tirages) ; ils illustrent un mécanisme, ils ne mesurent aucun jeu de données réel.

## Concepts clés

### Pourquoi la moyenne ne suffit pas

- Avec un coût unitaire de rupture $c_u$ et de surstock $c_o$, la quantité minimisant le coût espéré est le quantile d'ordre $\tau = c_u/(c_u+c_o)$ de la demande. La moyenne n'est optimale que si $\tau = 0{,}5$ **et** la loi symétrique.
- Simulation : demande lognormale (moyenne 100, coefficient de variation ≈ 0,42), $c_u = 4$, $c_o = 1$, donc $\tau = 0{,}8$. Commander la moyenne (100) coûte **79,3** par période en moyenne ; commander le quantile 0,8 (129,3) coûte **64,7**. Surcoût de la moyenne : 22,5 %.
- Un modèle excellent sur le point reste donc muet sur la décision : la dispersion autour du point est ce qui fixe la quantité.

### Les sorties probabilistes et ce qu'elles permettent

- **Grille de quantiles par pas** : directe pour une période isolée. Ne permet **pas** de sommer sur plusieurs périodes (voir plus bas). Chronos-Bolt génère des quantiles multi-pas directement ; le rapport technique de Chronos-2 décrit une sortie $H \times D \times |Q|$ avec 21 quantiles (0,01 à 0,99) ; rien dans les passages lus ne décrit une loi jointe sur les pas.
- **Échantillons de trajectoires** : le plus souple. Somme, maximum, coût d'une politique de stock simulée : tout se calcule sur les trajectoires. La qualité tient à la dépendance temporelle réellement modélisée. La doc de [[darts]] dit que `predict(num_samples=…)` renvoie des échantillons de Monte-Carlo « décrivant la loi jointe sur le temps et les composantes » ; si le modèle produit des pas indépendants, cette phrase ne vaut plus (non vérifié par modèle). La première génération de [[Chronos]] obtient ses prévisions probabilistes en échantillonnant plusieurs trajectoires futures (README).
- **Loi paramétrique** (lognormale, binomiale négative…) : un quantile à tout niveau, une ligne de code. Exacte et additive seulement dans des cas fermés (somme de Poisson indépendants = Poisson ; voir [[Processus de Poisson]]) ; la surdispersion et la corrélation sortent de ce cadre.
- **Ensemble ou borne conforme** : une borne haute à couverture annoncée, sans hypothèse de loi ([[Prédiction conforme]]). Suffit pour **une** quantité ; ne donne pas la loi, donc pas de coût simulé ni de somme.

### Le piège central : la demande sur le délai est une somme

- La quantité à commander couvre un horizon de protection : délai $L$, ou $L + R$ en revue périodique (voir [[Politiques de réapprovisionnement (s,S) et (R,Q)]]). La demande utile est $S = \sum_{i=1}^{L} D_{t+i}$, somme de périodes **corrélées** ([[Autocorrelation]]).
- Le quantile n'est pas additif : $Q_\tau(S) \ne \sum_i Q_\tau(D_{t+i})$ en général. Argument gaussien : $Q_\tau(S) = \sum \mu_i + z_\tau \sqrt{\mathbf 1^\top \Sigma \mathbf 1}$, tandis que la somme des quantiles vaut $\sum \mu_i + z_\tau \sum \sigma_i$. Or $\sqrt{\mathbf 1^\top \Sigma \mathbf 1} \le \sum \sigma_i$ (Cauchy-Schwarz), avec égalité seulement si les périodes sont parfaitement corrélées. Pour $\tau > 0{,}5$, la somme des quantiles **sur-commande**. Hors gaussien, cet argument ne donne plus le sens de l'écart.
- Contre-exemple exécuté : $L = 4$, périodes gaussiennes de moyenne 100 et d'écart-type 20, corrélation $0{,}5^{|i-j|}$, $\tau = 0{,}95$ ($c_u = 19$, $c_o = 1$), $10^6$ trajectoires.

| Construction de la quantité | Quantité | $P(S \le q)$ obtenue | Coût moyen |
|---|---|---|---|
| Somme des quantiles 0,95 de période | 531,6 | 0,989 | 135,9 |
| Trajectoires tirées **indépendamment** par pas | 465,8 | 0,874 | 137,5 |
| Trajectoires **jointes** (ou loi de la somme) | 494,2 | 0,950 | 118,4 |

- Deux erreurs de signes opposés : sommer les quantiles suppose la corrélation parfaite (sur-stock), échantillonner pas par pas ignore la corrélation (sous-stock, ici 0,874 au lieu de 0,95). L'écart-type de la somme vaut 57,4 simulé, contre $20\sqrt 4 = 40$ sous indépendance.
- Remèdes : trajectoires jointes, loi agrégée, ou **prévoir directement la demande cumulée** sur $L$ (cible = la somme ; à distinguer de la stratégie directe par horizon décrite dans [[Forecasting framing]]). Les garanties de couverture par pas n'impliquent pas la couverture de la somme ; calibrer sur la somme observée.

### Les pertes adaptées : pinball et CRPS

- La perte **pinball** au niveau $\tau$ : $L_\tau(y, q) = (\mathbb 1\{y < q\} - \tau)(q - y)$. Gneiting (2011) la présente comme fonction de score strictement cohérente pour le quantile d'ordre $\tau$ (loi à moment d'ordre 1 fini) ; Gneiting et Raftery (2007, théorème 6) montrent que la classe de scores de cette forme est propre pour la prévision d'un quantile.
- Lien avec le coût : $C(q) = (c_u + c_o)\,\mathbb E[L_\tau(D, q)]$ avec $\tau = c_u/(c_u+c_o)$. Minimiser la pinball au niveau $\tau$, c'est minimiser le coût du vendeur de journaux. Vérifié en simulation (égalité numérique) ; Bertsimas et Kallus (2020) notent la même identité entre perte de la [[Régression quantile]] et coût du newsvendor.
- Le **CRPS** note la loi entière : $\mathrm{CRPS}(F,y) = \int (F(x) - \mathbb 1\{x \ge y\})^2 dx = 2\int_0^1 L_p(F^{-1}(p), y)\,dp$ (Gneiting et Raftery, éq. 20, à un signe d'orientation près ; la seconde forme est attribuée à Gneiting et Ranjan 2011 dans Berrisch et Ziel). Contrôle numérique, lognormale précédente, $y = 120$ : 16,11 par l'intégrale de pinball, 16,09 par $\mathbb E|X-y| - \tfrac12 \mathbb E|X-X'|$.
- Choix : une pinball au niveau $\tau$ du SKU note exactement la décision ; le CRPS moyenne tous les niveaux, utile pour comparer des lois sans connaître les coûts. **Limite** : l'équivalence pinball = coût suppose des coûts linéaires. Coût fixe de commande, quantité minimale, plafond de capacité : la décision n'est plus un quantile et l'évaluation passe par simulation.

### Évaluer par la décision

- Gneiting (2011) : un score ne vaut que pour la statistique qu'il élicite. Le RMSE élicite la moyenne (le MAE, la médiane) ; aucun des deux n'élicite le quantile 0,8 qui est commandé. Un modèle classé premier sur ces mesures ne l'est pas forcément sur le coût de la quantité commandée.
- Protocole : [[Walk-forward CV]]. À chaque origine, produire la quantité avec les seules données passées, observer la demande, calculer le **coût réalisé** (rupture + surstock) et le niveau de service atteint ; comparer à une référence (moyenne + stock de sécurité par formule, ou naïve saisonnière). Rapporter le niveau de service obtenu **face à la cible**, avec une incertitude (par exemple [[Bootstrap]] sur les origines).
- Les [[Forecasting metrics]] restent utiles pour diagnostiquer un modèle ; elles ne remplacent pas le coût réalisé pour choisir.
- Limite : un backtest suppose que la demande observée ne dépend pas de la quantité commandée (voir censure plus bas).

### Calibration des quantiles

- Un quantile natif d'un modèle n'est pas un quantile calibré. Si la couverture empirique du « quantile 0,8 » vaut 0,72, la quantité est biaisée dans un sens qui coûte.
- Simulation : un modèle sous-estime la dispersion (14 au lieu de 20). Quantile 0,8 du modèle : 111,8, couverture réelle **0,722**, coût 28,9. Quantile vrai : 116,8, coût 27,96. Recalage par split conformal sur 2 000 résidus signés : 117,3, couverture 0,807, coût 27,97. La moyenne seule (100) coûte 39,85.
- Surcoût de 3,4 % pour une couverture à 0,72 dans ce seul scénario ; l'effet dépend de l'asymétrie des coûts et de l'écart de couverture, non explorés ici.
- [[Calibration]] et [[Prédiction conforme]] : le split conformal corrige sous **échangeabilité**, pas pour une série dérivante ; ACI ne garantit que la fréquence de couverture à long terme. Sur une série, recalibrer sur une fenêtre récente et **surveiller la couverture en ligne**.
- Cao (2024, résumé lu) propose un quantile critique « conformalisé » pour un newsvendor à variables explicatives, avec une garantie indépendante de l'exactitude du modèle sous-jacent.

### Estimer puis optimiser, ou apprendre la quantité

- **Estimer puis optimiser (ETO)** : prévoir la loi, puis dériver la quantité. **Approches intégrées / prescriptives** : apprendre directement la quantité (ou le modèle) pour minimiser le coût de décision.
- **Ban et Rudin (2019)**, newsvendor à $p$ variables explicatives. Montrent que l'ERM (équivalent à une régression quantile en grande dimension) et une méthode à noyaux (KO) donnent des décisions, que **omettre** les variables rend les décisions inconsistantes, et des bornes à taille finie. Sur l'effectif d'urgence d'un hôpital britannique : −23 % (ERM) et −24 % (KO) de coût hors échantillon face à la référence, KO trois ordres de grandeur plus rapide. Limites : un seul produit ; un seul jeu de données ; Elmachtoub et Grigas jugent « pas clair » comment étendre l'approche en présence de contraintes.
- **Bertsimas et Kallus (2020)**, problème conditionnel $\min_z \mathbb E[c(z;Y)\mid X=x]$. Prescriptions à base de poids (plus proches voisins, arbres, noyaux) asymptotiquement optimales sous conditions peu fortes, y compris données non i.i.d. et **censurées**. Cas d'un distributeur de médias : coefficient de prescriptivité $P$ à 88 %. Limites relevées par les auteurs : l'ERM sur une classe de décisions n'a pas la même garantie asymptotique universelle et gère mal les contraintes ; noyaux et voisins se dégradent avec la dimension.
- **Elmachtoub et Grigas (2022)**, Smart « Predict, then Optimize ». Perte SPO mesurant l'erreur de décision, substitut convexe SPO+ **cohérent** avec elle ; les moindres carrés le sont aussi. SPO+ domine surtout quand le modèle est **mal spécifié** (plus courts chemins, portefeuille). Limites des auteurs : objectif linéaire ; paramètres incertains dans les contraintes et objectifs non linéaires laissés en perspective. Écrit comme LP, le newsvendor place la demande dans les contraintes : cas que les auteurs laissent en perspective (déduction de cette page, le papier ne traite pas le newsvendor).
- **Le désaccord, tel que lu.** Elmachtoub, Lam, Zhang et Zhao (2023) : l'intégré gagne quand le modèle est mal spécifié ; l'ETO le domine **asymptotiquement** (au sens de la dominance stochastique du regret) quand le modèle contient la vérité et que les données suffisent. Hu, Kallus et Mao (2022) : pour l'optimisation linéaire contextuelle, le plug-in atteint des vitesses de regret **plus rapides** que les méthodes intégrées, sous une hypothèse limitant la quasi-dégénérescence duale des instances. Aucune source lue ne désigne un gagnant général : l'issue dépend de la spécification du modèle, du volume de données et de la structure du problème.

### Cas particuliers

- **Demande intermittente** : [[Intermittent demand]] fournit une moyenne (taille / intervalle) ; un quantile exige une loi de la demande, et la somme sur $L$ se traite, comme ci-dessus, par trajectoires ou loi agrégée.
- **Hiérarchie** : les moyennes sont cohérentes par linéarité, pas les quantiles : le quantile du total n'est pas la somme des quantiles des feuilles ([[Hierarchical forecasting]]). Panagiotelis et al. (2023) étendent la réconciliation du point aux prévisions probabilistes.
- **Demande censurée** : les ventes valent $\min(D, \text{stock})$, pas la demande. Simulation : politique passée = médiane (92,3) ; moyenne des ventes 80,6 contre 100 pour la demande ; quantile 0,8 des ventes **92,3**, plafonné par le stock, contre 129,3. Entraîner sur les ventes ne permet donc jamais de relever la quantité. Bertsimas et Kallus (§6.2) corrigent la censure à droite lorsque le seuil (stock disponible) est observé.

## Les maths, simplement

- Coût : $C(q) = c_u\,\mathbb E[(D-q)^+] + c_o\,\mathbb E[(q-D)^+]$ ; $C'(q) = (c_u+c_o)F(q) - c_u = 0 \Rightarrow F(q^\*) = \tau$.
- Pinball : $L_\tau(y,q) = (\mathbb 1\{y<q\}-\tau)(q-y)$ ; $C(q) = (c_u+c_o)\,\mathbb E[L_\tau(D,q)]$.
- Somme de $L$ périodes de covariance $\Sigma$ : $\mathrm{Var}(S) = \mathbf 1^\top \Sigma \mathbf 1 \le (\sum_i \sigma_i)^2$.
- Quantité depuis des trajectoires jointes `paths` (matrice $n_{\text{traj}} \times L$) :

```python
S = paths.sum(axis=1)           # demande cumulée sur L périodes, trajectoire par trajectoire
q = np.quantile(S, tau)         # tau = c_u / (c_u + c_o)
cout = np.mean(cu*np.maximum(S - q, 0) + co*np.maximum(q - S, 0))
```

## En pratique

- Vérifier la **chaîne** : statistique produite (point, quantile, trajectoires) → agrégation sur $L$ → recalage → quantité. Une rupture à l'une des étapes invalide les suivantes.
- Un intervalle central de niveau $\ell$ a pour borne haute le quantile $(1+\ell)/2$ **s'il est à queues égales** (à vérifier par modèle) : `level=90` correspond à $\tau = 0{,}95$.
- Mesurer, par famille de SKU, la **couverture empirique** des quantiles en backtest, puis recaler. Comparer toujours au coût réalisé d'une référence simple.
- Outils (licences relevées sur GitHub le 2026-10-04) :
  - [[Chronos]] (Apache-2.0) : Chronos original en échantillons de trajectoires ; Chronos-Bolt en quantiles directs multi-pas ; Chronos-2 via `predict_df(..., quantile_levels=[...])`.
  - [[statsforecast]] (Apache-2.0) : `predict(h, level=[...])` pour les intervalles ; `ConformalIntervals(n_windows, h, method)` avec au moins 2 fenêtres ; méthodes `conformal_distribution` et `conformal_error`.
  - [[darts]] (Apache-2.0) : `num_samples` pour des échantillons ; la vraisemblance `QuantileRegression` entraîne avec la perte pinball ; des modèles conformes existent.
  - Pour les fondations : [[Foundation models pour séries temporelles]]. Une sortie « probabiliste native » ne dispense pas de mesurer la couverture.

### Travaux récents

- Lan, Liao, Elmachtoub, Kroer, Lam, Zhang (arXiv 2510.18215, octobre 2025 ; résumé lu) : sous une mauvaise spécification **locale**, il existe un compromis biais-variance entre SAA, ETO et IEO, dont l'équilibre dépend du degré de mauvaise spécification. Il nuance la lecture binaire « bien ou mal spécifié » du désaccord ci-dessus.

## Approches voisines & alternatives

- [[Modèle du vendeur de journaux (newsvendor)]] — la décision elle-même, avec son fractile critique.
- [[Stock de sécurité et taux de service]] — la même quantité vue comme « moyenne + marge », par formule gaussienne sur le délai.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — la politique qui consomme la demande sur $L$ (ou $L+R$).
- [[Régression quantile]] — le modèle qui apprend directement un quantile conditionnel.
- [[Bootstrap]] / [[Monte Carlo et inférence variationnelle]] — fabriquer des trajectoires ou des incertitudes de backtest.
- [[Reinforcement learning]] — apprendre la politique de réapprovisionnement complète, sans passer par une loi de la demande.

## Pour aller plus loin

- Ban & Rudin (2019), *The Big Data Newsvendor: Practical Insights from Machine Learning*, Operations Research 67(1), 90-108 : <https://doi.org/10.1287/opre.2018.1757> (résumé lu sur les dépôts institutionnels LBS et Imperial ; texte intégral non lu).
- Bertsimas & Kallus (2020), *From Predictive to Prescriptive Analytics*, Management Science 66(3), 1025-1044 : <https://doi.org/10.1287/mnsc.2018.3253> ; <https://arxiv.org/abs/1402.5481>.
- Elmachtoub & Grigas (2022), *Smart "Predict, then Optimize"*, Management Science 68(1), 9-26 : <https://doi.org/10.1287/mnsc.2020.3922> ; <https://arxiv.org/abs/1710.08005>.
- Hu, Kallus & Mao (2022), *Fast Rates for Contextual Linear Optimization*, Management Science 68(6), 4236-4245 : <https://doi.org/10.1287/mnsc.2022.4383> ; <https://arxiv.org/abs/2011.03030> (résumé lu).
- Elmachtoub, Lam, Zhang & Zhao (2023), *Estimate-Then-Optimize versus Integrated-Estimation-Optimization versus Sample Average Approximation: A Stochastic Dominance Perspective* : <https://arxiv.org/abs/2304.06833> (résumé lu) ; Lan et al. (2025) : <https://arxiv.org/abs/2510.18215> (résumé lu).
- Cao (2024), *A Conformal Approach to Feature-based Newsvendor under Model Misspecification* : <https://arxiv.org/abs/2412.13159> (résumé lu).
- Gneiting (2011), *Making and Evaluating Point Forecasts*, JASA 106(494), 746-762 : <https://arxiv.org/abs/0912.0902>.
- Gneiting & Raftery (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation*, JASA 102(477), 359-378 : <https://doi.org/10.1198/016214506000001437>.
- Gneiting & Ranjan (2011), *Comparing Density Forecasts Using Threshold- and Quantile-Weighted Scoring Rules*, JBES 29(3), 411-422 : <https://doi.org/10.1198/jbes.2010.08110> (métadonnées vues ; l'identité CRPS lue dans Berrisch & Ziel, *CRPS Learning*, <https://arxiv.org/abs/2102.00968>, éq. 8).
- Panagiotelis, Gamakumara, Athanasopoulos & Hyndman (2023), *Probabilistic forecast reconciliation: Properties, evaluation and score optimisation*, EJOR 306(2), 693-706 : <https://doi.org/10.1016/j.ejor.2022.07.040> (métadonnées et résumé de dépôt vus).
- Ansari et al. (2025), *Chronos-2: From Univariate to Universal Forecasting* : <https://arxiv.org/abs/2510.15821> ; README de <https://github.com/amazon-science/chronos-forecasting> ; guide « Probabilistic forecasts » de <https://github.com/unit8co/darts> ; classe `ConformalIntervals` du code de <https://github.com/Nixtla/statsforecast>.
- Connexions brain : [[Walk-forward CV]], [[Calibration]], [[Prédiction conforme]], [[Intermittent demand]], [[Hierarchical forecasting]].
