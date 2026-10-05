---
role: notion
nom: Jumeau numérique et modèles hybrides
alias: [Jumeau numérique, Digital twin, Modèle hybride, Modèles hybrides physique-données]
categorie: ml/maintenance
domaines: [data-sci, ml-eng]
tags: [digital-twin, predictive-maintenance, rul]
---

# Jumeau numérique et modèles hybrides

## Aperçu

- Un **jumeau numérique** est, sobrement, un modèle d'un équipement réel **tenu à jour par les mesures de cet équipement**, et qui sert à une décision. Ce qui le distingue d'une simulation de conception est la boucle : mesurer, recaler le modèle, estimer l'état, prévoir, décider.
- Un **modèle hybride** combine une structure physique connue et des données qui comblent ce que la physique ne dit pas. C'est le plus souvent ce qu'on met derrière le mot « jumeau » en maintenance prédictive.

## Concepts clés

### Définitions, et ce qu'elles ne tranchent pas

- **ISO 23247-1:2021** : *Automation systems and integration — Digital twin framework for manufacturing — Part 1: Overview and general principles* (édition 1, octobre 2021, ISO/TC 184/SC 4). Objet : aperçu et principes généraux d'un cadre de jumeau numérique pour la fabrication, avec termes, définitions et exigences. Le cadre ne prescrit ni format de données ni protocole. La définition de « jumeau numérique », telle que citée **de seconde main** (thèse de Tola, arXiv:2401.02227), est : « une représentation numérique adaptée à l'usage d'un élément de fabrication observable, avec synchronisation entre l'élément et sa représentation » (traduction libre). La page ISO lue ne reproduit pas la définition : **texte de la norme non vérifié**.
- **Définition NASA (2012)**, citée par Kunzer et al. : simulation multiphysique et multi-échelle d'un véhicule qui utilise les meilleurs modèles physiques, les mesures de capteurs et l'historique de flotte pour refléter la vie de son jumeau réel, et en prévoir la santé et le RUL. Le concept est né dans la maintenance d'actifs complexes.
- **Kritzinger et al. (2018)** classent par le degré d'automatisation du flux de données : *digital model* (manuel dans les deux sens), *digital shadow* (automatique de l'objet vers le modèle seulement), *digital twin* (automatique dans les deux sens). Leur constat : la littérature sur le jumeau au sens strict est rare, celle sur le modèle et l'ombre est plus abondante. Un tableau de bord alimenté par des capteurs est donc une **ombre**, pas un jumeau.
- **Kunzer, Berges, Dubrawski (2022)** exigent sept éléments au minimum : actif physique, jumeau numérique, instrumentation, analyse, fil numérique (la liaison), données en direct, information actionnable. Sans actif physique, c'est une simulation classique ; sans analyse, le jumeau ne fait que refléter l'état courant. **Jones et al. (2020)** ont dégagé 13 caractéristiques de 92 publications.
- **Désaccord à conserver.** L'ISO parle de synchronisation sans en fixer le sens ; Kritzinger exige un flux automatique bidirectionnel. Abdelrahman et al. (2025, plus de 15 000 publications, bâtiment) concluent que le consensus terminologique est hors d'atteinte et que les traits supposés (simulation, IA, temps réel, échange bidirectionnel) ne sont pas encore mûrs dans leur domaine. Wright et Davidson (2020) jugent que l'absence de distinction entre modèle et jumeau menace la crédibilité du sujet.

### Ce qu'un jumeau fait réellement en maintenance

- **Estimer l'état** non mesuré (usure, longueur de fissure, capacité) à partir des mesures : filtre de Kalman ou variante ([[Modèles de Markov cachés et filtre de Kalman]]).
- **Détecter** par les résidus : Isermann décrit la détection de défauts par modèle comme la génération, à partir des entrées $U$ et sorties $Y$ mesurées, de résidus, d'estimées de paramètres ou d'estimées d'état, comparés à leur valeur normale pour produire des symptômes. Ses trois familles sont l'estimation de paramètres, les équations de parité et les observateurs d'état.
- **Prévoir** : propager l'état estimé jusqu'au seuil de défaillance donne le RUL ([[Maintenance prédictive et RUL]]).
- **Tester des scénarios** : l'effet d'un changement de charge sur la durée de vie, hors des données vues.

### Filtre de Kalman, résidus et modèles de dégradation

- Le filtre compare à chaque pas la mesure $y_k$ à sa prévision $H\hat x_k^-$ ; l'écart est l'**innovation** $\nu_k$, de covariance $S_k$. Une innovation trop grande devant $S_k$ signale un écart au modèle : défaut, ou modèle périmé (raisonnement, non appuyé par une source lue). C'est le résidu du paragraphe précédent.
- **Modèles de dégradation.** Physiques : loi de Paris pour la fissuration en fatigue, $da/dN = C(\Delta K)^m$ ($a$ longueur de fissure, $N$ nombre de cycles, $\Delta K$ amplitude du facteur d'intensité de contrainte, $C$ et $m$ coefficients du matériau obtenus par essais ; Paris et Erdogan, 1963). Stochastiques : processus gamma (van Noortwijk, 2009, pour son usage en maintenance), processus de Wiener ([[Mouvement brownien]]).
- Le coefficient $C$ et l'exposant $m$ se **recalent en ligne** en les ajoutant à l'état du filtre (état augmenté) : un geste hybride classique (raisonnement, non appuyé par une source lue). Le filtre linéaire n'y suffit pas dès que la loi est non linéaire : EKF, UKF ou filtre particulaire.

### Modèles hybrides

- Willard et al. (ACM Computing Surveys, 2022) proposent une taxonomie des méthodes qui intègrent la connaissance scientifique à l'apprentissage. Kunzer et al. retiennent trois stratégies pour la maintenance : réseaux informés par la physique, modèles d'ordre réduit, données simulées pour compléter de petits jeux.
- **Revue de 2026.** Braun, Raible et Huber (arXiv:2608.10047, 212 études, août 2026) classent les approches en biais d'observation, d'induction, d'apprentissage et hybrides. Ils rapportent que les études montrent un gain constant sur les références, avec une littérature concentrée sur les batteries lithium-ion et les roulements, et demandent des bancs d'essai comparant les stratégies d'intégration : il n'y en a donc pas encore. (Lecture : des auteurs qui choisissent leurs références, dans une littérature qui publie surtout des succès, rendent ce gain constant moins probant qu'il n'y paraît.)
- **PINN, en une phrase critique.** Un réseau dont la perte pénalise le résidu d'une équation aux dérivées partielles (Raissi, Perdikaris, Karniadakis, 2019) peut échouer sur des problèmes à peine plus complexes (Krishnapriyan et al., NeurIPS 2021, pour des raisons d'optimisation) et n'a pas battu les éléments finis en temps et en précision dans l'étude de Grossmann et al. (2024) : utile pour un problème inverse ou une équation partielle connue, pas pour remplacer un solveur sur un problème bien posé.

## Les maths, simplement

- **Espace d'états** : $x_k = f(x_{k-1}) + w_k$ (dégradation), $y_k = h(x_k) + v_k$ (mesure), avec $w_k$ et $v_k$ des bruits. Innovation : $\nu_k = y_k - h(\hat x_k^-)$.
- **RUL comme premier passage** : $\mathrm{RUL}_k = \inf\{t \ge 0 : x_{k+t} \ge x_{\mathrm{crit}}\}$ ; l'estimée de $x_k$ et de sa vitesse d'usure donne une loi de RUL, non un nombre.
- **PINN** : $\mathcal L = \mathcal L_{\text{données}} + \lambda\,\mathcal L_{\text{EDP}}$ (plus les conditions initiales et aux limites), $\lambda$ étant un réglage.

## En pratique

- **Quand l'hybride vaut la peine.** Kunzer et al. : il excelle quand il existe un peu de données (échantillons rares, capteurs bruités ou épars) et un peu de physique (conditions aux limites manquantes, interactions connues), sans que l'un ou l'autre suffise. Avec beaucoup de pannes menées à terme et sans physique, un modèle appris suffit ([[RUL par apprentissage profond]]) ; avec une bonne physique et peu de données, le modèle physique recalé ; avec ni l'un ni l'autre, rien.
- **Le coût de la physique pure.** Kunzer et al. citent une simulation de propagation de fissure à 5,5 millions de degrés de liberté qui demande environ 4 jours de calcul : loin de la décision en temps quasi réel. D'où les modèles d'ordre réduit, et les jumeaux « implicites » appris sur les données (Xiong et al., cités par eux), que leurs auteurs justifient par le coût d'un modèle physique par composant.
- **Commencer petit** : un filtre de Kalman sur un [[Indicateurs de santé|indicateur de santé]] avec un seuil, avant tout modèle multiphysique. Sans décision à éclairer, pas de jumeau.
- **Cahier des charges** : écrire la synchronisation (fréquence, sens, latence) et la décision visée, pas le mot « jumeau ».

## Limites

- **Identifiabilité.** Raue et al. (2009) distinguent la non-identifiabilité **structurelle** (paramétrage redondant, aucune mesure n'y change rien) de la **pratique** (données trop rares ou bruitées pour borner un paramètre). Un filtre ajuste toujours quelque chose : si $C$ et $m$ de la loi de Paris ne sont pas identifiables avec les capteurs disponibles, la valeur recalée est un artefact et l'extrapolation du RUL en hérite.
- **Coût de modélisation** : un modèle physique par composant, à tenir à jour après chaque réparation ; un jumeau périmé produit des résidus qui ressemblent à des défauts ([[Data drift]], raisonnement).
- **Limites des données** (Kunzer et al.) : pannes catastrophiques rares ou absentes des enregistrements ; validation croisée trompée par des corrélations parasites ; boîtes noires.
- **Preuve** : Sharma et al. (2020) relèvent des métriques d'évaluation insuffisantes. Un chiffre de gain doit venir d'un site, pas d'une plaquette.

## Approches voisines & alternatives

- [[Modèles de Markov cachés et filtre de Kalman]] — les équations du filtre, EKF, UKF, filtre particulaire.
- [[Indicateurs de santé]] — l'observable que le jumeau recale.
- [[Surveillance conditionnelle et modes de défaillance]] — quel mode modéliser, et quel intervalle P-F attendre.
- [[Politique de maintenance et coût]] — la décision que le jumeau doit éclairer.
- [[Maintenance prédictive avec peu de pannes]] — le régime où la physique compense le manque de données.
- [[RUL par apprentissage profond]] et [[RUL par analyse de survie]] — les voies sans modèle du mécanisme.
- [[Time series anomaly detection]] — détecter l'écart sans modèle physique.
- [[Santé de batterie (SOH et RUL)]] — le cas où le modèle physique de cellule et l'apprentissage se rejoignent.
- [[Cause racine d'une anomalie]] — simuler les défauts pour disposer d'une vérité terrain.
- [[Inférence en bordure - modèles sur du matériel d'atelier]] et [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — le fil numérique côté atelier.

## Pour aller plus loin

- Kunzer, Berges, Dubrawski (2022), *The digital twin landscape at the crossroads of predictive maintenance, machine learning and physics based modeling*, arXiv:2206.10462 : https://arxiv.org/abs/2206.10462
- Kritzinger, Karner, Traar, Henjes, Sihn (2018), *Digital twin in manufacturing: a categorical literature review and classification*, IFAC-PapersOnLine 51(11):1016-1022. DOI : https://doi.org/10.1016/j.ifacol.2018.08.474
- Jones, Snider, Nassehi, Yon, Hicks (2020), *Characterising the digital twin: a systematic literature review*, CIRP JMST 29:36-52. DOI : https://doi.org/10.1016/j.cirpj.2020.02.002
- Wright, Davidson (2020), *How to tell the difference between a model and a digital twin*, Advanced Modeling and Simulation in Engineering Sciences 7, art. 12. DOI : https://doi.org/10.1186/s40323-020-00147-4
- Abdelrahman et al. (2025), *What is a digital twin anyway?*, arXiv:2409.19005 : https://arxiv.org/abs/2409.19005
- Sharma et al. (2020), *Digital twins: state of the art theory and practice, challenges, and open research questions*, arXiv:2011.02833 : https://arxiv.org/abs/2011.02833
- ISO 23247-1:2021 : https://www.iso.org/standard/75066.html
- Isermann (2004), *Model-based fault detection and diagnosis — status and applications*, IFAC Proceedings Volumes 37(6):49-60. DOI : https://doi.org/10.1016/S1474-6670(17)32149-3
- Willard, Jia, Xu, Steinbach, Kumar (2022), *Integrating scientific knowledge with machine learning for engineering and environmental systems*, ACM Computing Surveys 55(4). DOI : https://doi.org/10.1145/3514228
- Raissi, Perdikaris, Karniadakis (2019), *Physics-informed neural networks*, J. Comput. Phys. 378:686-707. DOI : https://doi.org/10.1016/j.jcp.2018.10.045
- Krishnapriyan et al. (2021), *Characterizing possible failure modes in physics-informed neural networks*, arXiv:2109.01050 : https://arxiv.org/abs/2109.01050
- Grossmann, Komorowska, Latz, Schönlieb (2024), *Can physics-informed neural networks beat the finite element method?*, IMA J. Appl. Math., arXiv:2302.04107 : https://arxiv.org/abs/2302.04107
- Raue et al. (2009), *Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood*, Bioinformatics 25(15):1923-1929. DOI : https://doi.org/10.1093/bioinformatics/btp358
- Braun, Raible, Huber (2026), *Physics-informed machine learning in prognostics and health management: a systematic literature review*, arXiv:2608.10047 : https://arxiv.org/abs/2608.10047
