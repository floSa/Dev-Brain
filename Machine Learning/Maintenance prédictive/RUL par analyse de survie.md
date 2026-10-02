---
role: notion
nom: RUL par analyse de survie
alias: [RUL par survie, Survie et RUL, Weibull et RUL]
categorie: ml/maintenance
domaines: [data-sci, mlops]
tags: [rul, predictive-maintenance, survival-analysis, regression]
---

# RUL par analyse de survie

## Aperçu

- Au lieu de prédire **un nombre** de cycles restants, modéliser la **loi** de la durée de vie $T$ de l'équipement, puis en déduire le RUL à l'âge $t$ comme la durée restante sachant que l'unité a survécu jusque-là. Le RUL devient une distribution, pas une valeur ponctuelle.
- Le gain décisif est la **censure** : une unité encore en service, ou retirée avant la panne, compte quand même. La régression sur le RUL ne sait pas l'utiliser.
- La mécanique générale (Kaplan-Meier, risque, Cox) est dans [[Analyse de survie]] et la bibliothèque dans [[lifelines]] ; cette page ne les réécrit pas. Elle traite ce que la maintenance y ajoute : le Weibull comme loi de panne, les capteurs comme covariables, et le piège des covariables qui changent au cours du temps.

## Concepts clés

### La censure, en maintenance

- Sur C-MAPSS, tous les moteurs d'entraînement vont jusqu'à la panne (la dernière ligne de chaque trajectoire est l'état défaillant, Babu et al. 2016), alors que les moteurs de test sont arrêtés au hasard **avant** la panne et leur RUL vrai est fourni (Zhang et al. 2022). Le jeu de test est donc, par construction, à **censure à droite**, le RUL vrai n'y servant que d'étiquette d'évaluation.
- En exploitation, c'est la règle : la plupart des moteurs sont retirés du service avant la défaillance (Wang et al. 2025). La régression sur une cible RUL exige une panne observée par ligne : on jette les unités censurées, ou on les étiquette comme si la fin du suivi était une panne. [[Analyse de survie]] dit pourquoi les deux biaisent.
- **Point à justifier** (raisonnement, non vérifié dans une source ce jour) : la censure standard suppose qu'elle ne dépend pas de l'état de l'unité. Un remplacement préventif décidé *parce que* la machine donne des signes de fatigue la viole.
- Noot, Martin et Birmele (IJPHM 2025) reprochent aux approches profondes d'ignorer la censure, adaptent un Transformer et un LSTM pour la prendre en compte et rapportent un résultat compétitif à faible taux de censure, plus efficace à fort taux de censure si le jeu est assez grand. Voir aussi [[RUL par apprentissage profond]].

### Weibull : une loi de panne à deux paramètres

- Dans lifelines, `WeibullFitter` a pour survie $S(t)=\exp\!\big(-(t/\lambda)^{\rho}\big)$ et pour risque $h(t)=\dfrac{\rho}{\lambda}\Big(\dfrac{t}{\lambda}\Big)^{\rho-1}$. $\lambda$ (`lambda_`) est l'**échelle** : le temps où 63,2 % de la population est défaillante. $\rho$ (`rho_`) est la **forme**.
- **Forme et risque** (lecture directe de la formule) : $\rho<1$, risque **décroissant** (défauts de jeunesse : ce qui a survécu au rodage a moins de risque de casser) ; $\rho=1$, risque **constant** (loi exponentielle, sans mémoire : l'âge ne dit rien, le RUL est le même à tout âge) ; $\rho>1$, risque **croissant** (usure, le cas visé par la maintenance prédictive).
- **RUL conditionnel à l'âge** : $P(\mathrm{RUL}>r\mid T>t)=S(t+r)/S(t)$. Pour un Weibull, la médiane est $r_{1/2}(t)=\lambda\big((t/\lambda)^{\rho}+\ln 2\big)^{1/\rho}-t$. Avec $\rho>1$, elle décroît quand $t$ augmente.
- **Limite** : un Weibull sur l'âge seul ne voit pas la condition de la machine. Deux pompes du même âge ont le même RUL, qu'elles vibrent ou non. D'où les covariables.

### Cox et AFT : l'effet des covariables

- **Cox** (`CoxPHFitter`) : le risque est $h(t\mid x)=h_0(t)\exp\big((x-\bar x)'\beta\big)$ dans la documentation de lifelines. Le risque de base $h_0$ est estimé par la méthode de Breslow par défaut, ou par splines ou constantes par morceaux. On lit des *hazard ratios*. Hypothèse des risques proportionnels à vérifier ; la stratification gère une variable catégorielle qui la viole (documentation de lifelines).
- **AFT** (*accelerated failure time*, `WeibullAFTFitter`) : $\lambda(x)=\exp(\beta_0+\beta_1x_1+\dots)$ et $S(t;x)=\exp\!\big(-(t/\lambda(x))^{\rho}\big)$. Les covariables **étirent ou compriment le temps** : un coefficient se lit comme un facteur multiplicatif sur la durée de vie, pas comme un rapport de risque. Le paramètre $\rho$ peut lui-même dépendre de covariables (`model_ancillary=True`).
- Autres lois AFT de la même documentation : `LogNormalAFTFitter`, `LogLogisticAFTFitter`, et `GeneralizedGammaRegressionFitter`, qui généralise les précédentes. Le choix Cox contre AFT : Cox laisse libre la forme du risque de base ; AFT la fixe mais se lit directement en durée, plus commode pour un RUL.

### Covariables dépendantes du temps : le point dur

- Un capteur n'est pas une covariable fixe : c'est une trajectoire $x(t)$. Le cadre naturel est le modèle de Cox à covariables variant dans le temps, `CoxTimeVaryingFitter` dans lifelines, qui veut un format **long** (une ligne par intervalle, avec `start`, `stop`, `event` et un identifiant).
- **Le piège**, dit en toutes lettres par la documentation de lifelines : pour prédire il faudrait connaître les valeurs futures des covariables, mais si on les connaissait, on saurait déjà si l'unité est encore en vie. On peut donc estimer l'effet du niveau actuel d'un capteur sur le risque, **pas** en déduire une loi de RUL sans modèle de l'évolution des capteurs. La documentation précise que les méthodes de prédiction existent avec des réserves sur leur sens.
- **Trois sorties** vues dans la littérature :
  - le **modèle joint** (trajectoire de capteurs et temps de panne estimés ensemble) : Aghaee Dabaghan Fard et al. (arXiv, 2025, révisé en 2026) combinent Cox, processus gaussiens multi-sorties convolués et loi multinomiale pour prédire RUL **et** mode de défaillance, testé sur des jeux de moteurs d'avion ;
  - le **réseau qui sort les paramètres de la loi** : WTTE-RNN (Martinsson, thèse de master, Chalmers, 2017) fait sortir par un réseau récurrent les paramètres d'un Weibull ; il gère censure à droite et covariables variant dans le temps, testé sur données synthétiques et sur des données de moteurs d'avion ;
  - le **risque en temps discret** : Yang et al. (arXiv, 2026) associent une représentation longitudinale des capteurs à un objectif de risque en temps discret, appris de façon fédérée, sur C-MAPSS.
- Un indicateur de santé ([[Indicateurs de santé]]) réduit les capteurs à une trajectoire unique, ce qui allège le modèle joint.

## Les maths, simplement

- **Vraisemblance avec censure** : pour l'unité $i$ de durée observée $t_i$ et d'indicateur $\delta_i$ (1 si panne, 0 si censurée), $L=\prod_i f(t_i)^{\delta_i}\,S(t_i)^{1-\delta_i}$. Une panne contribue par sa densité, une unité censurée par la probabilité d'avoir survécu au moins jusque-là. C'est la logique de l'ajustement dans lifelines ([[Maximum de vraisemblance]]) ; WTTE-RNN, d'après les résumés consultés, entraîne son réseau avec une vraisemblance adaptée à la censure.
- **Lien survie / risque** : $S(t)=\exp\!\big(-\int_0^t h(u)\,du\big)$, donc $H(t)=(t/\lambda)^{\rho}$ pour un Weibull.
- **RUL** : $S(t+r)/S(t)$ ; une fois la loi estimée, un **intervalle** sur le RUL se lit sur ses quantiles, sans méthode supplémentaire. La garantie de couverture de [[Prédiction conforme]] est d'une autre nature (sans hypothèse de loi).

## En pratique

- **Régression sur RUL contre survie**

| | Régression sur le RUL | Analyse de survie |
|---|---|---|
| Cible | un RUL par ligne, donc une panne observée | durée + indicateur de panne |
| Unités censurées | jetées ou mal étiquetées | utilisées jusqu'à leur date de censure |
| Sortie | une valeur ponctuelle | une loi, donc des quantiles |
| Capteurs variables | fenêtre glissante, naturel | difficile, cf. ci-dessus |
| Hypothèse | aucune sur la loi | forme de loi (Weibull) ou risques proportionnels (Cox) |
| Peu de pannes | peu de lignes étiquetées | peu d'événements : la loi est mal estimée aussi |

- **Encoder correctement le couple** (durée, indicateur) : `event_observed` dans les fitters univariés de lifelines. L'oubli de la censure est l'erreur n°1.
- **Commencer par `KaplanMeierFitter` et `WeibullFitter`** sur la flotte, regarder $\rho$ : si $\rho\approx1$, l'âge est inutile et seule la condition informe.
- **Évaluer sur des métriques de survie**, pas le RMSE sur le RUL des seules unités en panne : une évaluation sur les seules pannes ignore justement les censurées. scikit-survival, mentionnée plus bas, propose justement des outils d'évaluation sous censure (JMLR 2020).
- **Séparer par unité** à l'évaluation, comme pour le profond ([[Data leakage]], [[Walk-forward CV]]).
- **Autre bibliothèque** : scikit-survival (Pölsterl, JMLR 21(212), 2020) apporte la survie « machine learning » — Cox pénalisé, forêts de survie aléatoires, SVM de survie — compatible scikit-learn. Elle n'a pas de fiche dans le brain à ce jour.

## Approches voisines & alternatives

- [[Analyse de survie]] — la notion mère : censure, Kaplan-Meier, Cox.
- [[lifelines]] — la brique : `WeibullFitter`, `WeibullAFTFitter`, `CoxPHFitter`, `CoxTimeVaryingFitter`.
- [[RUL par apprentissage profond]] — la régression par réseaux, et la prise en compte de la censure par Noot et al.
- [[Maintenance prédictive et RUL]] — le cadre du pronostic.
- [[Indicateurs de santé]] — un indice qui résume les capteurs en une seule covariable.
- [[Politique de maintenance et coût]] — une loi de durée de vie nourrit directement le coût d'un remplacement.
- [[Modèles de Markov cachés et filtre de Kalman]] — modéliser l'état de santé comme latent, autre route vers la covariable dynamique.
- [[Maintenance prédictive]] — le dossier.

## Pour aller plus loin

- Documentation lifelines — `WeibullFitter` : https://lifelines.readthedocs.io/en/latest/fitters/univariate/WeibullFitter.html ; `WeibullAFTFitter` : https://lifelines.readthedocs.io/en/latest/fitters/regression/WeibullAFTFitter.html ; `CoxPHFitter` : https://lifelines.readthedocs.io/en/latest/fitters/regression/CoxPHFitter.html ; covariables variant dans le temps : https://lifelines.readthedocs.io/en/latest/Time%20varying%20survival%20regression.html
- Martinsson (2017), *WTTE-RNN: Weibull Time To Event Recurrent Neural Network*, thèse de master, Chalmers : https://odr.chalmers.se/items/a48cefc9-f542-4280-ba0d-c0a8f5106b9d
- Noot, Martin, Birmele (2025), *LSTM and Transformers based methods for Remaining Useful Life Prediction considering Censored Data*, IJPHM 16(2). DOI : https://doi.org/10.36001/ijphm.2025.v16i2.4260
- Aghaee Dabaghan Fard, Kim, Deep, Lee, *Bayesian Joint Model of Multi-Sensor and Failure Event Data for Multi-Mode Failure Prediction*, arXiv : https://arxiv.org/abs/2506.17036
- Yang, Weller, Fernando, Livneh, Wen (2026), *Collaborative System Failure Prognostics via Federated Longitudinal-Survival Modeling*, arXiv : https://arxiv.org/abs/2607.26038
- Pölsterl (2020), *scikit-survival: A Library for Time-to-Event Analysis Built on Top of scikit-learn*, JMLR 21(212) : https://jmlr.org/beta/papers/v21/20-729.html
- Babu, Zhao, Li (2016), *Deep Convolutional Neural Network Based Regression Approach for Estimation of Remaining Useful Life*, DASFAA. DOI : https://doi.org/10.1007/978-3-319-32025-0_14
- Wang et al. (2025), *Deep Domain Adaptation for Turbofan Engine Remaining Useful Life Prediction*, arXiv : https://arxiv.org/abs/2510.03604
