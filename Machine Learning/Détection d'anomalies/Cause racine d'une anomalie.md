---
role: notion
nom: Cause racine d'une anomalie
alias: [RCA, Analyse de cause racine, Root cause analysis, Cause racine, Propagation de panne, Root cause localization]
categorie: ml/anomalie
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection, causal-inference, condition-monitoring, timeseries]
---

# Cause racine d'une anomalie

## Aperçu

- Détecter dit **que** quelque chose s'écarte. Localiser (cf. [[Expliquer une anomalie (contribution des capteurs)]]) dit **où** l'écart se voit. La cause racine dit **ce qui a changé en premier** et pourquoi : une vanne qui fuit, un filtre qui se colmate, une consigne modifiée.
- Un détecteur entraîné sur du normal voit des **symptômes**. Dans un procédé couplé, un défaut local se propage : le capteur qui dévie le plus n'est pas forcément celui qui a causé le reste.
- État de l'art, dit sans détour : les méthodes existent, mais **peu sont validées sur des usines réelles**. Les benchmarks sont surtout logiciels (micro-services), simulés (procédé de Tennessee Eastman) ou des bancs d'essai avec défauts injectés. Une liste de candidats classés est le bon livrable ; un verdict ne l'est pas.

## Concepts clés

### Trois niveaux : détecter, localiser, remonter à la cause

- **Détection** : un score et un seuil ([[Score et seuil d'alerte]]).
- **Localisation** : une contribution par capteur. Elle explique le détecteur, pas le procédé.
- **Cause racine** : l'élément dont la modification, seule, suffit à produire les écarts observés. C'est une question **causale** : « que se serait-il passé sans ce changement ? ». Corrélation et classement par amplitude n'y répondent pas.
- Le lien avec la page 1 : Orchard et al. (NeurIPS 2025) montrent que, graphe inconnu, retenir comme causes les variables au score d'anomalie marginal le plus élevé est justifié sous leurs hypothèses (une cause unique, graphe en polyarbre). L'attribution par capteur est donc un point de départ défendable, mais seulement sous ces hypothèses.

### RCA industrielle classique

- **Les 5 pourquoi** : remonter une chaîne de « pourquoi ? ». Technique attribuée à Sakichi Toyoda, décrite par Taiichi Ohno (Toyota). Critiques recensées (d'après Wikipédia, qui cite un document de Toyota de 2003 non ouvert) : l'enquêteur s'arrête au symptôme, ne peut pas trouver une cause qu'il ne connaît pas, deux enquêteurs aboutissent à deux chaînes, et la méthode isole une cause unique là où plusieurs interviennent.
- **Diagramme d'Ishikawa** (arête de poisson) : classer les causes candidates par familles, popularisé dans les années 1960 par Kaoru Ishikawa. En fabrication, les « 5 M » : main-d'œuvre, machine, matière, méthode, mesure (d'après Wikipédia).
- **AMDEC** : énumérer les modes de défaillance d'un équipement avec leurs effets et, si possible, leurs causes, avant l'incident. Voir [[Surveillance conditionnelle et modes de défaillance]].
- Ces méthodes reposent sur la connaissance de l'équipe. Elles ne s'opposent pas aux méthodes ci-dessous : l'AMDEC et le schéma de procédé sont la **connaissance a priori** qui manque aux algorithmes (lecture de cette page).

### RCA algorithmique : corrélation, précédence, causalité

- **Corrélation.** Deux capteurs bougent ensemble parce que l'un pilote l'autre, ou parce qu'une cause commune les pilote tous deux. La corrélation ne dit pas lequel.
- **Précédence temporelle.** Une cause précède ses effets, donc le premier capteur à dévier est un bon candidat. Piège (lecture, non sourcée) : une boucle de régulation fermée répartit et retarde l'écart, et l'ordre d'apparition peut s'en trouver brouillé.
- **Causalité de Granger.** $X$ « cause au sens de Granger » $Y$ si les valeurs passées de $X$ améliorent la prévision de $Y$ au-delà de ses propres valeurs passées (Granger, 1969, d'après Wikipédia). Limites rapportées : ne tient pas compte des confondants latents, ne capte pas les effets instantanés ni non linéaires, exige la stationnarité ou des différences. AERCA (ICLR 2025) formule les deux premières : pas de confondant caché, pas d'effet instantané.
- **PCMCI** (Runge et al., *Science Advances*, 2019) : une sélection de conditions (PC1) puis un test d'indépendance conditionnelle « momentané » (MCI). Il vise deux difficultés : la perte de puissance quand on conditionne sur tout le passé en grande dimension, et le contrôle des faux positifs sous forte autocorrélation. Hypothèses : suffisance causale (causes communes observées), condition de Markov causale, stationnarité, fidélité, liens retardés seulement (les liens simultanés restent non orientés). Cadre général : [[Découverte causale]].
- **Entropie de transfert.** Pendant sans modèle linéaire de l'idée de Granger, fondée sur l'[[Mutual information]] conditionnelle. Chen et al. (*Sensors*, 2025) proposent une variante à décalage spécifique (LSTE) qui désigne l'instrument qui dévie en premier et le délai de propagation vers les points en aval. Testée sur un système simulé, le procédé de Tennessee Eastman (perturbations IDV5 et IDV8), un montage de laboratoire et un haut-fourneau en exploitation. Limites des auteurs : coût de calcul, hypothèse d'une perturbation unique, non-stationnarité et bruit à haute fréquence non résolus.

### L'anomalie comme intervention sur un mécanisme

- Cadre commun des travaux récents : le procédé est un **modèle causal structurel** $x_j := f_j(\mathrm{pa}_j, n_j)$. Une anomalie est une **intervention** qui change un mécanisme ou un bruit exogène. La cause racine est le nœud intervenu.
- **Budhathoki, Minorics, Blöbaum, Janzing** (ICML 2022) : avec le graphe et le modèle fonctionnel connus, ils définissent un **score d'anomalie conditionnel** (la valeur d'une variable est-elle surprenante *sachant ses parents* ?) et répartissent par valeurs de Shapley la contribution des ancêtres à l'anomalie d'une cible.
- **Orchard, Okati, Garrido Mejia, Blöbaum, Janzing** (NeurIPS 2025) : un seul échantillon post-intervention, une seule cause, un graphe en polyarbre ; l'algorithme de parcours n'exige que des scores marginaux, sans seuil arbitraire. Évalué sur données synthétiques, PetShop, Sock-shop v2 et des jeux semi-synthétiques ; le simple classement par score « fonctionne souvent bien », les méthodes de parcours et contre-factuelle faisant mieux. Les auteurs qualifient le polyarbre d'hypothèse structurelle forte.
- **AERCA** (Han, Absar, Zhang, Yuan, ICLR 2025) : un autoencodeur apprend la causalité de Granger et la loi normale des variables exogènes ; les causes sont les variables exogènes qui s'en écartent. Testé sur quatre jeux synthétiques, SWaT et MSDS. Sur SWaT, les performances de toutes les méthodes baissent ; les auteurs invoquent des hypothèses violées (indépendance, confondants cachés, effets instantanés).
- **Travaux 2026**, résumés seuls lus : Khosravinia et al. restreignent un transformeur de prévision aux parents issus d'une découverte causale ; Tao et al. (MATERO-RCA) traitent les anomalies **contextuelles** industrielles, dont la réponse dépend des commandes et des états de marche, par trajectoires contre-factuelles, sur données simulées et industrielles réelles.

### RCA en micro-services (AIOps) : l'idée est transposable, les benchmarks ne le sont pas

- Une panne logicielle se propage d'un service à l'autre selon un **graphe de dépendances** que les traces distribuées révèlent ([[Métriques, logs et traces]], [[OpenTelemetry]]). Le problème est formellement voisin de celui d'une usine : un graphe, des métriques, une cause à désigner.
- **RCAEval** (Pham et al.) : trois jeux, 735 cas de panne, quinze méthodes de référence reproductibles. **PetShop** (Hardt et al., CLeaR 2024) : latence, requêtes et disponibilité à pas de 5 minutes, 68 problèmes de performance injectés.
- Pham, Ha, Zhang (ASE 2024) comparent neuf méthodes de découverte causale et vingt et une méthodes de RCA : « aucune méthode ne domine dans toutes les situations », et les performances sur jeux synthétiques ne reflètent pas fidèlement celles sur systèmes réels.
- **Pas de garantie de transfert** : un service logiciel redémarre, se duplique et s'injecte à volonté ; un procédé a de l'inertie, des délais de transport, des boucles de régulation et des capteurs à cadences différentes (lecture, non sourcée). Les méthodes se transposent, leurs scores non.

### Propagation dans un procédé : le graphe de procédé

- Un procédé industriel porte un graphe **connu à la conception** : flux de matière et d'énergie, régulations, instrumentation (schéma de procédé, P&ID). Ce graphe donne les **directions** que la découverte causale peine à retrouver, et restreint la liste des candidats (lecture de cette page).
- **causRCA** (Mehling, Pieper, Lüke, Fraunhofer IWU, 2025) : un tour vertical à commande numérique, 170 enregistrements de fonctionnement normal pris par OPC UA en production réelle, 100 scénarios de défaut (fuites de vanne, filtres colmatés) produits par un jumeau numérique couplé à un automate réel, et un graphe causal de 92 nœuds et 104 arêtes **validé par des experts**. Licence Apache 2.0. Données de marche réelles, défauts simulés : un compromis, pas un jeu de pannes réelles. Les auteurs le présentent comme comblant le manque de jeux réels pour évaluer ensemble découverte causale et RCA (résumé vu via recherche). Voir [[Jumeau numérique et modèles hybrides]].
- Tennessee Eastman reste le banc d'essai de simulation le plus cité dans les travaux lus ici (LSTE) ; il est simulé de bout en bout.
- Vuković et Thalmann (2022) concluent, d'après le résumé, que dans la fabrication on ne connaît encore que des applications expérimentales et dispersées de la découverte causale (page de l'éditeur non accessible, texte non lu).

## Les maths, simplement

- **Granger.** Modèle $y_t=\sum_{k=1}^{p}a_k\,y_{t-k}+\sum_{k=1}^{p}b_k\,x_{t-k}+\varepsilon_t$. $X$ cause $Y$ au sens de Granger si l'hypothèse nulle $b_1=\dots=b_p=0$ est rejetée (test de Fisher). Hypothèses : pas de confondant latent, pas d'effet instantané, stationnarité, linéarité.
- **Entropie de transfert.** $\mathrm{TE}_{X\to Y}=I\big(Y_t\,;\,X^{(k)}_{t-1}\,\big|\,Y^{(l)}_{t-1}\big)$ : l'information sur $Y_t$ que le passé de $X$ apporte en plus du passé de $Y$. Elle vaut zéro si $X$ n'apporte rien.
- **Propagation linéaire** (calcul de cette page). Pour $x=Bx+n$, soit $x=(I-B)^{-1}n$. Un décalage $\delta$ du bruit du nœud $j$ déplace $x$ de $\delta\,(I-B)^{-1}e_j$ : **tous les descendants de $j$** dévient en marginal. Seul $j$ dévie encore une fois qu'on **conditionne sur ses parents**.
- **Score conditionnel.** $r_j=\dfrac{x_j-\hat f_j(\mathrm{pa}_j)}{\hat\sigma_j}$, avec $\hat f_j$ ajusté sur du normal. Candidats cause : les $j$ où $|r_j|$ est grand malgré des parents « normaux ». C'est la logique du score conditionnel de Budhathoki et al. Elle exige un **graphe correct** : un parent oublié ou une cause commune non mesurée fausse $r_j$.
- **Rappel top-$K$.** Avec $\mathrm{GT}$ les causes étiquetées : $R@K=\dfrac{|\mathrm{top}_K\cap \mathrm{GT}|}{|\mathrm{GT}|}$ (définition usuelle).

## En pratique

- **Partir de la connaissance, pas des données.** Le schéma de procédé et l'AMDEC donnent le graphe et les modes plausibles ; l'algorithme **classe** les candidats dans cet ensemble. Ils servent aussi de test d'adéquation : une cause algorithmique absente de l'AMDEC mérite une relecture, pas un acquiescement.
- **Regrouper les alertes en événement** avant l'analyse, puis chercher le **premier** instant de déviation : la fenêtre d'analyse se cale sur lui, pas sur le pic du score. [[Détection de ruptures]] aide à dater cet instant.
- **Prévoir des variables de contexte** : consignes, commandes, état de marche. Tao et al. (MATERO-RCA) rappellent que la réponse dépend de ces variables ; les omettre fabrique des causes cachées et des liens faux.
- **Ne livrer qu'un classement avec ses hypothèses** : « cause unique, graphe de procédé v3, fenêtre de 40 minutes ». Un opérateur doit pouvoir contester l'hypothèse, pas seulement le résultat.
- **Valider par défauts injectés** (banc d'essai, jumeau numérique, causRCA) avant de croire un score sur du réel. Les historiques de pannes menées à terme sont rares ([[Maintenance prédictive avec peu de pannes]]), donc l'évaluation en vrai est mince presque partout.
- **Consigner les cas confirmés** : chaque panne dont la cause est établie devient une ligne de vérité terrain pour mesurer le rappel top-$K$ à venir. Le seul jeu de test qui compte est le sien.
- **Pièges** : prendre le premier capteur à dévier pour la cause quand une boucle de régulation masque l'ordre ; confondre un défaut de capteur (dérive, blocage) avec un défaut de procédé ; supposer une cause unique quand deux défauts coïncident (LSTE et la plupart des méthodes de parcours le supposent) ; conclure à partir d'un graphe appris sur un historique contaminé par des défauts ([[Types d'anomalies et régimes de supervision]]).

## Approches voisines & alternatives

- [[Expliquer une anomalie (contribution des capteurs)]] — l'étape d'avant : le classement par capteur, base de la cause racine.
- [[Découverte causale]] — retrouver le graphe à partir des données : PC, FCI, LiNGAM, NOTEARS, avec leurs hypothèses d'identifiabilité.
- [[Inférence causale]] — estimer l'effet d'une intervention une fois le graphe posé ; cadre des contre-factuels.
- [[Modèles graphiques probabilistes]] — le formalisme du graphe et de l'indépendance conditionnelle.
- [[Mutual information]] — la brique de l'entropie de transfert.
- [[Surveillance conditionnelle et modes de défaillance]] — l'AMDEC, la courbe P-F et le vocabulaire de la défaillance.
- [[Diagnostic de défauts de roulements]] — le diagnostic quand le mode de défaillance est déjà connu et mesurable.
- [[Maintenance prédictive et RUL]] et [[Politique de maintenance et coût]] — ce que la cause change à la décision d'intervenir.
- [[Jumeau numérique et modèles hybrides]] — simuler les défauts pour disposer d'une vérité terrain.
- [[Métriques, logs et traces]] — la télémétrie des services, terrain de la RCA logicielle.
- [[Time series anomaly detection]], [[Évaluer une détection d'anomalies]] — la détection qui déclenche l'analyse et sa mesure.
- [[Graph Neural Networks]] — apprendre sur le graphe de dépendances.

## Pour aller plus loin

- Orchard, Okati, Garrido Mejia, Blöbaum, Janzing (NeurIPS 2025), *Root Cause Analysis of Outliers with Missing Structural Knowledge*. arXiv : https://arxiv.org/abs/2406.05014
- Budhathoki, Minorics, Blöbaum, Janzing (ICML 2022), *Causal structure-based root cause analysis of outliers*. arXiv : https://arxiv.org/abs/1912.02724 (la première version arXiv porte un autre ordre d'auteurs).
- Han, Absar, Zhang, Yuan (ICLR 2025), *Root Cause Analysis of Anomalies in Multivariate Time Series through Granger Causal Discovery* : https://proceedings.iclr.cc/paper_files/paper/2025/file/6fde96479648d71e4fd9724374bf76eb-Paper-Conference.pdf
- Runge, Nowack, Kretschmer, Flaxman, Sejdinovic (2019), *Detecting and quantifying causal associations in large nonlinear time series datasets*, Science Advances 5(11). arXiv : https://arxiv.org/abs/1702.07007 (le titre arXiv omet « and quantifying »).
- Chen, Liang, Wang, Yao, Su, Liu (2025), *Lag-Specific Transfer Entropy for Root Cause Diagnosis and Delay Estimation in Industrial Sensor Networks*, Sensors : https://pmc.ncbi.nlm.nih.gov/articles/PMC12251659/
- Mehling, Pieper, Lüke (2025), *causRCA: Real-World Dataset for Causal Discovery and Root Cause Analysis in Machinery*, Zenodo : https://zenodo.org/records/15876410 (description lue ; article associé non ouvert, accès refusé).
- Pham, Zhang, Ha, Salim, Zhang (2024), *RCAEval: A Benchmark for Root Cause Analysis of Microservice Systems with Telemetry Data*. arXiv : https://arxiv.org/abs/2412.17015
- Pham, Ha, Zhang (2024), *Root Cause Analysis for Microservice System based on Causal Inference: How Far Are We?*, ASE 2024. arXiv : https://arxiv.org/abs/2408.13729
- Hardt, Orchard, Blöbaum, Kasiviswanathan, Kirschbaum (2024), *The PetShop Dataset: Finding Causes of Performance Issues across Microservices*, CLeaR 2024. arXiv : https://arxiv.org/abs/2311.04806
- Vuković, Thalmann (2022), *Causal Discovery in Manufacturing: A Structured Literature Review*, Journal of Manufacturing and Materials Processing 6(1):10. DOI : https://doi.org/10.3390/jmmp6010010 (non ouvert, accès refusé ; résumé vu via recherche).
- Khosravinia, Gama, Veloso (2026), *Causally-Constrained Probabilistic Forecasting for Time-Series Anomaly Detection*. arXiv : https://arxiv.org/abs/2604.17998 (résumé lu seulement).
- Tao, Huang, Xiao (2026), *MATERO-RCA: Mode-Aware Trajectory-Level Energy-Based Root-Set Optimization for Industrial Root Cause Analysis*. arXiv : https://arxiv.org/abs/2607.29092 (résumé lu seulement).
- Granger (1969), *Investigating Causal Relations by Econometric Models and Cross-spectral Methods*, Econometrica 37(3):424-438 (non ouvert ; référence reprise de Wikipédia).
- Ohno (1988), *Toyota Production System: Beyond Large-Scale Production* ; Toyota Motor Corporation (2003), *The "Thinking" Production System* (non ouverts ; références reprises de Wikipédia : https://en.wikipedia.org/wiki/Five_whys).
