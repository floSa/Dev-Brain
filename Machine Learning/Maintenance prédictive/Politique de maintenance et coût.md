---
role: notion
nom: Politique de maintenance et coût
alias: [Politique de maintenance, Maintenance conditionnelle à seuil, Politique d'âge, Politique de bloc, Coût de maintenance]
categorie: ml/maintenance
domaines: [data-sci, mlops]
tags: [predictive-maintenance, rul, thresholding, optimization]
---

# Politique de maintenance et coût

## Aperçu

- Un score ou un RUL n'est pas une décision. Une **politique de maintenance** associe ce qu'on observe (âge, état, prévision) à une action (attendre, inspecter, remplacer), et se juge à son **coût moyen à long terme** (ou à sa disponibilité).
- Le seuil d'alerte d'un détecteur est traité dans [[Score et seuil d'alerte]] et n'est pas repris ici. Cette page prend la suite : la structure des coûts autour d'une décision, les politiques classiques avec lesquelles tout modèle appris doit être comparé, et ce que les sources disent du coût réel de la maintenance prédictive.

## Concepts clés

### Les coûts en jeu

- $c_p$ : remplacement **préventif**, planifié. $c_f$ : remplacement **sur panne** (arrêt non planifié, dégâts induits, pièce en urgence). Les notations $c_{FA}$ (fausse alerte) et $c_M$ (panne manquée) de [[Score et seuil d'alerte]] s'y rattachent par convention : $c_{FA}\approx c_p$ plus la vie résiduelle jetée ; $c_M\approx c_f-c_p$, le surcoût d'une panne subie par rapport à l'intervention qu'on aurait faite.
- Koops (PHME 2018) écrit le coût moyen sur les quatre issues d'une prédiction, plus un **coût fixe $C_0$** : développement, mise en œuvre et maintenance de la solution prédictive. Le gain net est l'écart entre le coût de référence (sans prédiction) et le coût minimal. Deux conclusions de l'article : le point de fonctionnement optimal est une **décision d'entreprise** et il dépend de la **fréquence du mode** (mode rare, seuil strict, car presque toutes les alertes sont fausses) ; tous les cas ne sont pas rentables.
- Les conséquences de sûreté ne se convertissent pas en euros. La RCM de Nowlan et Heap vise d'abord les conséquences des défaillances (d'après un résumé secondaire, rapport non ouvert).

### Politiques classiques, sans capteur

- **Politique d'âge** : remplacer à la panne ou à l'âge $T$, selon ce qui arrive en premier. **Politique de bloc** : remplacer à dates fixes $T, 2T, \dots$ quel que soit l'âge, et à chaque panne. Variante : réparation minimale entre deux dates.
- Barlow et Hunter (1960), *Optimum preventive maintenance policies*, est un article ancien sur le sujet (titre vérifié, texte non ouvert). Wang (2002) dresse un état de l'art des politiques pour systèmes qui se dégradent : remplacement, réparation imparfaite, maintenance de groupe, approches conditionnelles à inspection périodique.
- Elles servent de **référence** : un modèle appris n'a de valeur que s'il bat la politique d'âge optimale calculée avec les mêmes coûts.

### Maintenance conditionnelle à seuil

- On inspecte tous les $\Delta$ ; si le niveau de dégradation dépasse un **seuil préventif** $L$, on remplace avant la panne ; au-delà du seuil de défaillance, on remplace sur panne. Les deux leviers sont $L$ et $\Delta$.
- Dieulle, Bérenguer, Grall et Roussignol (EJOR, 2003) la traitent pour une dégradation en **processus gamma** : le critère est le coût moyen par unité de temps, rapport du coût espéré d'un cycle de renouvellement à sa durée espérée, et leurs essais numériques montrent que des valeurs précises du seuil critique et de la fonction de planification minimisent le coût. Van Noortwijk (RESS, 2009) recense les modèles d'inspection et de maintenance sous dégradation gamma.
- Les revues : Alaswad et Xiang (RESS, 2017) classent les modèles de CBM par type de dégradation (états discrets, continus, modèle à risques proportionnels) et par critère d'optimisation, fréquence d'inspection, degré de maintenance et méthode de résolution, avec le multi-composants ; de Jonge et Scarf (EJOR, 2020) couvrent plus de 200 articles parus de 2001 à 2018. Les résumés lus décrivent des **modèles** ; aucun ne présente de bilan d'exploitation.

### Du RUL à la décision

- **Règle à un pas** : remplacer dès que $P(\text{panne avant la prochaine occasion})\ge c_p/c_f$. Elle ignore la vie résiduelle perdue et pousse à agir trop tôt ; c'est un point de départ, pas une politique optimale.
- **Prévision asymétrique** : le score PHM08 de [[Maintenance prédictive et RUL]] pénalise plus l'erreur tardive que la précoce. Il classe des algorithmes sur un jeu, avec des constantes fixées par le défi et non par un site ; il ne dit pas ce que coûte une erreur dans une usine. Dès que $c_p$ et $c_f$ sont connus, évaluer directement le coût.
- **Décision séquentielle** : [[Markov Decision Process]] et [[Apprentissage par renforcement]]. Xu et Zhang (*Complex & Intelligent Systems*, 2025) entraînent un agent QR-DQN à choisir entre ne rien faire, réparer et remplacer sur C-MAPSS, avec un RUL probabiliste. Les coûts y sont des unités choisies par les auteurs (remplacement 6,0 plus pénalité de vie perdue, réparation 3,0, panne −80) : la politique n'est valable que pour cette échelle.

### Le coût réel : ce que disent les sources

- **Le guide O&M du DOE/PNNL** (PNNL-19634, Release 3.0, août 2010) donne 8 à 12 % d'économie par rapport à un préventif seul, puis, dans le même paragraphe, des « enquêtes indépendantes » : retour sur investissement ×10, coûts de maintenance −25 à −30 %, pannes −70 à −75 %, arrêts −35 à −45 %, production +20 à +25 %. **Aucune référence n'est donnée dans ce passage**, et les deux fourchettes (8-12 % et 25-30 %) ne portent pas sur une base explicite. À ne pas citer comme des mesures.
- Le même guide liste les coûts : outillage souvent supérieur à 50 000 $ (valeur 2010), formation du personnel, engagement de la direction, et un gain « pas immédiatement visible » pour elle.
- **Preuve économique rare.** La revue de Wahab et al. (PeerJ Computer Science, 2024) sur maintenance prédictive et jumeaux numériques fournit peu d'analyse coût-bénéfice directe. Yu et Law (arXiv, 2020) partent du constat que l'adoption reste limitée faute de justification économique, et chiffrent un cas, une installation de traitement d'eau, par simulation de Monte-Carlo : un exemple, non une généralité.
- **Sur le papier, la fusion données + physique pèse.** Dans l'exemple d'un moteur d'avion, avec des coûts tirés de la littérature, Koops annonce jusqu'à 63 % de gain supplémentaire pour le modèle fusionné ; hypothèses de coût non vérifiées sur site.

## Les maths, simplement

- **Optimum sur une courbe ROC** (Metz, 1978, cité par Koops). Avec $p$ la fréquence du mode, le coût moyen est $C = C_0 + p\,[\,\mathrm{TPR}\,C_{TP} + (1-\mathrm{TPR})\,C_{FN}\,] + (1-p)\,[\,\mathrm{FPR}\,C_{FP} + (1-\mathrm{FPR})\,C_{TN}\,]$. L'optimum est où la pente de la courbe vaut $\dfrac{dTPR}{dFPR}=\dfrac{(1-p)(C_{FP}-C_{TN})}{p\,(C_{FN}-C_{TP})}$ (dérivation directe, $C_{TN}=0$ en général). Un $p$ petit rend la pente grande : seuil strict.
- **Politique d'âge** (renouvellement-récompense) : $g(T)=\dfrac{c_p\,R(T)+c_f\,F(T)}{\int_0^T R(t)\,dt}$, avec $F$ la loi de durée de vie et $R=1-F$.
- **Politique de bloc** : $g(T)=\dfrac{c_p+c_f\,M(T)}{T}$, $M(T)$ le nombre espéré de pannes sur $[0,T]$. Avec réparation minimale et un risque de Weibull (forme $\beta$, échelle $\eta$), $M(T)=(T/\eta)^\beta$ et $T^\ast=\eta\left[\dfrac{c_p}{(\beta-1)\,c_f}\right]^{1/\beta}$. **Si $\beta\le 1$, aucun optimum fini** : le risque ne croît pas, remplacer plus tôt ne rapporte rien.
- **Quantile optimal.** Sous une perte linéaire asymétrique ($c_e$ par unité de temps de prévision trop précoce, $c_l$ par unité de retard), la meilleure prévision ponctuelle du RUL est le quantile de niveau $c_e/(c_e+c_l)$ de sa loi. Si le retard coûte deux fois plus, c'est le tiers inférieur : prévoir tôt. Voir [[Régression quantile]].

## En pratique

- **Chiffrer d'abord $c_p$ et $c_f$**, avec arrêt, pièce et délai d'approvisionnement ; puis refaire le calcul pour plusieurs rapports $c_f/c_p$, car il est rarement connu à un facteur 2 près. Un modèle dont l'intérêt disparaît dans cette fourchette ne vaut pas le déploiement.
- **Toujours une référence d'âge** : coût de la politique d'âge optimale avec les mêmes coûts. Si le modèle appris ne la bat pas, l'usure n'est pas lisible dans les capteurs ([[Maintenance prédictive avec peu de pannes]]).
- **Évaluer en coût**, pas en exactitude : [[Évaluer une détection d'anomalies]]. Calibrer les probabilités avant de les comparer à $c_p/c_f$ ([[Calibration]]).
- **Compter $C_0$.** Capteurs, intégration, réentraînement, astreinte : le gain par alerte doit les couvrir.
- **Piège** : régler le seuil sur les coûts d'un jeu public (C-MAPSS) et le croire transposable à un site.

## Approches voisines & alternatives

- [[Surveillance conditionnelle et modes de défaillance]] — l'intervalle P-F borne le délai disponible pour agir.
- [[Maintenance prédictive et RUL]] — la prévision du RUL et son score asymétrique.
- [[RUL par analyse de survie]] — la loi de durée de vie $F$ des politiques d'âge, estimée avec censure.
- [[Analyse de survie]] et [[Processus de Poisson]] — durées de vie et comptage des pannes.
- [[Prédiction conforme]] — intervalles sur le RUL avec garantie de couverture.
- [[Régression quantile]] — viser le quantile que les coûts dictent.
- [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] — la loi de panne moyenne d'un parc, point de départ des politiques d'âge.
- [[OEE et rendement global]] — la perte de disponibilité que la politique cherche à réduire.
- [[Markov Decision Process]] — le cadre des décisions séquentielles.

## Pour aller plus loin

- Alaswad, Xiang (2017), *A review on condition-based maintenance optimization models for stochastically deteriorating system*, RESS 157:54-63. DOI : https://doi.org/10.1016/j.ress.2016.08.009
- de Jonge, Scarf (2020), *A review on maintenance optimization*, EJOR 285(3):805-824. DOI : https://doi.org/10.1016/j.ejor.2019.09.047
- Dieulle, Bérenguer, Grall, Roussignol (2003), *Sequential condition-based maintenance scheduling for a deteriorating system*, EJOR 150(2):451-461. DOI : https://doi.org/10.1016/S0377-2217(02)00593-3
- Wang (2002), *A survey of maintenance policies of deteriorating systems*, EJOR 139(3):469-489. DOI : https://doi.org/10.1016/S0377-2217(01)00197-7
- Barlow, Hunter (1960), *Optimum preventive maintenance policies*, Operations Research 8(1):90-100. DOI : https://doi.org/10.1287/opre.8.1.90
- van Noortwijk (2009), *A survey of the application of gamma processes in maintenance*, RESS 94(1):2-21. DOI : https://doi.org/10.1016/j.ress.2007.03.019
- Koops (2018), *ROC-based business case analysis for predictive maintenance — applications in aircraft engine monitoring*, PHME 2018 : https://www.bauhaus-luftfahrt.net/fileadmin/user_upload/Publikationen/2018_Koops_Business_Case_Analysis_Predictive_Maintenance_PHME.pdf
- Sullivan, Pugh, Melendez, Hunt (2010), *O&M Best Practices Guide, Release 3.0*, PNNL-19634 : https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-19634.pdf
- Xu, Zhang (2025), *Predictive maintenance optimization for industrial equipment via reliable prognosis and risk-aware reinforcement learning*, Complex & Intelligent Systems : https://pmc.ncbi.nlm.nih.gov/articles/PMC12605408/
- Wahab et al. (2024), *Systematic review of predictive maintenance and digital twin technologies challenges, opportunities, and best practices*, PeerJ Computer Science : https://pmc.ncbi.nlm.nih.gov/articles/PMC11057655/
- Yu, Law (2020), *An economic perspective on predictive maintenance of filtration units*, arXiv:2008.11070 : https://arxiv.org/abs/2008.11070
