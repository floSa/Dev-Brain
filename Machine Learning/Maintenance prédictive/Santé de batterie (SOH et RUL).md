---
role: notion
nom: Santé de batterie (SOH et RUL)
alias: [SOH, State of Health, état de santé batterie, fin de vie batterie, EOL, Pronostic de batterie, Durée de vie résiduelle d'une batterie]
categorie: ml/maintenance
domaines: [data-sci, ml-eng, mlops]
tags: [predictive-maintenance, rul, digital-twin, timeseries, deep-learning, condition-monitoring]
---

# Santé de batterie (SOH et RUL)

## Aperçu

- Une cellule lithium-ion perd de la capacité et gagne en résistance au fil des cycles et du temps. Le **SOH** (*State of Health*) résume où elle en est ; le **RUL** dit combien de cycles, ou de mois, restent avant un seuil de **fin de vie** (EOL). Le cadre général du RUL est dans [[Maintenance prédictive et RUL]] ; cette page traite ce qui est propre à la batterie : un état interne que rien ne mesure directement, plusieurs mécanismes de dégradation, deux horloges (cycles et calendrier).
- Trois familles d'approches coexistent : modèles **physiques**, modèles **empiriques ou à circuit équivalent** avec filtre de Kalman, modèles **appris**. La limite commune est la donnée : quelques centaines de cellules cyclées en laboratoire, chimies et protocoles différents d'un jeu à l'autre, aucune panne de flotte.

## Concepts clés

### SOC, SOH et fin de vie

- **SOC** (*State of Charge*) : charge restante rapportée à la capacité courante de la cellule. Il varie à chaque cycle. Le **SOH** varie sur des centaines de cycles. Confondre les deux est l'erreur classique : un SOC erroné peut venir d'un SOH périmé (la capacité au dénominateur a baissé).
- **SOH capacitif** : capacité maximale mesurée rapportée à la capacité nominale. **SOH résistif** : résistance interne rapportée à sa valeur initiale, ou à celle de fin de vie. Les deux évoluent différemment : la capacité dit l'autonomie, la résistance dit la puissance disponible.
- **Fin de vie : 80 % de la capacité nominale** est une convention d'usage, non une propriété de la chimie. Severson et al. définissent la durée de vie (*cycle life*) comme le nombre de cycles jusqu'à 80 % de la capacité nominale. Une revue de 2025 (Zhang et al., sur les batteries de seconde vie) écrit que beaucoup de constructeurs et de normes retiennent 80 % pour la mobilité, que certains acceptent 70 %, et que d'autres ajoutent une limite sur la résistance.
- **Le seuil change d'un jeu à l'autre.** Les essais NASA PCoE s'arrêtent à 30 % de perte (2 Ah à 1,4 Ah), soit 70 % de la capacité nominale. Un « RUL » de ce jeu et un « RUL » de Severson ne se comparent donc pas sans recalage de la cible.
- **Origine du 80 %** : non établie ici en source primaire. Un article de blog d'éditeur (Qnovo) l'attribue à l'observation que la perte s'accélère au-delà ; des résumés de recherche l'attribuent à l'industrie du véhicule électrique et à un manuel de l'USABC, sans que le texte ait pu être ouvert. À vérifier avant de citer.

### Deux horloges : cycles et temps calendaire

- **Vieillissement cyclique** : lié à l'énergie débitée, aux courants, à la profondeur de décharge, à la température. **Vieillissement calendaire** : lié au temps et aux conditions de stockage (température, niveau de charge). Li et al. (2023) rappellent que la performance se dégrade « avec le temps et les cycles répétés ».
- **RUL en cycles** : naturel en laboratoire, où le profil est imposé. **RUL en temps calendaire** : ce que demande l'exploitant. Passer de l'un à l'autre suppose un profil d'usage futur (cycles équivalents par mois, température), qui est l'inconnue principale en exploitation.

### Mécanismes de vieillissement

- **SEI** (*solid electrolyte interphase*) : couche qui se forme sur l'électrode négative et consomme du lithium cyclable et du solvant. Sa croissance est le mécanisme le plus courant dans les modèles physiques (Li et al.) ; une loi en racine du temps est reproduite par un processus limité par la diffusion.
- **Dépôt de lithium** (*lithium plating*) : un courant d'interface plus fort l'accélère ; le lithium déposé peut réagir avec l'électrolyte et former de la SEI (Li et al.).
- **Perte de matière active** (fissuration de particules, déformations) : réduit la surface active, ce qui augmente la densité de courant sur le reste et accélère les autres mécanismes (Li et al.).
- **Trois modes observables** dans la littérature de diagnostic : perte d'inventaire de lithium (LLI), perte de matière active à l'électrode négative (LAM_NE) et à la positive (LAM_PE). Edge et al. (2021) recensent cinq mécanismes principaux et treize secondaires, qui se traduisent en cinq modes (d'après le résumé ; texte non ouvert).
- **Genoux** (*knees*) : dégradation rapide et non linéaire. Attia et al. (2022) décrivent des trajectoires dites *snowball*, *hidden* et *threshold* et six voies d'accélération (dépôt de lithium, saturation d'électrode, croissance de résistance, épuisement d'électrolyte et d'additifs, connectivité limitée par percolation, déformation mécanique). Certains mécanismes laissent des signaux « électrochimiquement indétectables ». Une extrapolation linéaire de la capacité rate un genou.
- **Identifiabilité** : Li et al. montrent que plusieurs combinaisons de mécanismes donnent les mêmes courbes de capacité et de résistance ; seul le modèle à cinq mécanismes couplés reproduit aussi les modes de dégradation à toutes les températures. Valider uniquement sur la capacité ne suffit donc pas.

### Trois familles d'approches

**Modèles physiques.**

- Équations de transport et de réaction dans l'électrode. Le **modèle à particule unique** (SPM) ramène chaque électrode à une particule sphérique et résout la diffusion du lithium en son sein ; le modèle **DFN** (Doyle, Fuller, Newman, 1993) ajoute l'électrolyte et la théorie des électrodes poreuses. Des extensions branchent la croissance de SEI, le dépôt de lithium ou la fissuration.
- Cadre libre : [[PyBaMM]] (SPM, DFN et variantes, licence BSD-3 d'après l'article JORS). Le coût est dans l'**identification des paramètres** : Li et al. notent que les modèles à mécanismes couplés dépassent déjà dix paramètres d'ajustement, dont beaucoup ne se mesurent pas, d'où un risque de surajustement.

**Modèles empiriques et circuit équivalent.**

- **Circuit équivalent** : une source de tension à vide dépendant du SOC, une résistance série, un ou deux réseaux RC. Un filtre de Kalman étendu estime en ligne le SOC, la puissance disponible et des paramètres indicatifs du SOH (série de Plett, 2004, *J. Power Sources* 134, résumé lu, texte non ouvert). Voir [[Modèles de Markov cachés et filtre de Kalman]].
- **Lois empiriques** : racine du temps pour la perte calendaire, Arrhenius pour la température (deux régimes selon Li et al.), ajustées sur des courbes de capacité. Rapides, mais valables dans le domaine d'ajustement.

**Modèles appris.**

- **Régression sur courbes** : Severson et al. (*Nature Energy*, 2019) prédisent la durée de vie de 124 cellules LFP/graphite à partir des **100 premiers cycles**, avant toute baisse de capacité visible. Le descripteur central est la variance de $\Delta Q_{100-10}(V)$, différence des courbes de décharge entre les cycles 100 et 10 ; sa corrélation avec la durée de vie, sur échelle log-log, est de −0,93 (figure 2c). Modèle : élastique net sur des descripteurs de domaine, cible $\log$(durée de vie). Voir [[Régularisation]].
- **Optimisation d'essais** : Attia et al. (*Nature*, 2020) combinent un prédicteur précoce et une optimisation bayésienne pour trouver de bons protocoles de charge rapide parmi 224 candidats en 16 jours, contre plus de 500 sans prédiction précoce.
- **Pipelines et réseaux profonds** : Roman et al. (préprint, annoncé pour *Nature Machine Intelligence*) construisent 30 descripteurs sur des segments de courbes de charge de 179 cellules ; leur meilleur modèle atteint 0,45 % d'erreur quadratique moyenne en pourcentage (RMSPE) sur des cellules chargées vite. Le banc d'essai BatteryLife (KDD 2025) compare 18 méthodes et conclut que des modèles populaires en séries temporelles peuvent être inadaptés à la prédiction de durée de vie.
- **Modèles de fondation** : Tan et al. (*Pretrained Battery Transformer*, arXiv 2025, révisé 2026) pré-entraînent sur 13 jeux et annoncent un gain moyen de 24,8 % sur 15 jeux aval ; Chan et al. (arXiv, décembre 2025) adaptent un modèle de fondation de séries temporelles à 20 jeux publics (1 704 cellules). Résultats d'auteurs, non reproduits ici.
- **Hybrides** : physique pour la structure, apprentissage pour le résidu ou pour les paramètres. La revue de Liu et al. (2026) place l'intégration de connaissance de domaine et les approches informées par la physique parmi ses axes. Cadre : [[Jumeau numérique et modèles hybrides]].

### Jeux de données

- **NASA PCoE** (Saha et Goebel, 2007) : cellules 18650 cyclées en charge, décharge et impédance, jusqu'à 30 % de perte de capacité ; le nombre de cellules n'est pas écrit sur la page du catalogue. Licence non écrite. Fiche : [[Jeux de données PHM]].
- **Oxford** (Birkl, Howey, 2017) : 8 cellules pochette Kokam cyclées en 2015-2016, licence ODbL. Profil de conduite urbain et caractérisation périodique (d'après un résumé de recherche de la documentation, non relu).
- **CALCE** (Université du Maryland) : cellules cylindriques, prismatiques et pochette, chimies NMC, LFP et LCO ; citation des articles d'origine demandée, aucune licence explicite sur la page.
- **MIT-Stanford-Toyota** (Severson et al.) : 124 cellules LFP/graphite de même modèle, environ 96 700 cycles, 72 protocoles de charge rapide, enceinte à 30 °C, décharge identique. Les auteurs le disent le plus grand jeu public de cellules nominalement identiques cyclées en conditions contrôlées.
- **Inventaires** : Mauthe et al. (arXiv, mars 2024, révisé 2026) répertorient les jeux publics de dégradation ; BatteryLife agrège des jeux de 8 formats, 59 systèmes chimiques et 421 protocoles.

## Les maths, simplement

- **SOH capacitif** : $\mathrm{SOH}_C(k)=\dfrac{Q_{\max}(k)}{Q_{\mathrm{nom}}}$, avec $Q_{\max}(k)$ la capacité mesurée au cycle $k$ à courant et température de référence, $Q_{\mathrm{nom}}$ la capacité nominale. **SOH résistif** : $\mathrm{SOH}_R(k)=\dfrac{R_{\mathrm{EOL}}-R(k)}{R_{\mathrm{EOL}}-R_0}$ (une définition parmi d'autres).
- **Fin de vie et RUL en cycles** : $k_{\mathrm{EOL}}=\min\{k:\ \mathrm{SOH}_C(k)\le s\}$ avec $s$ le seuil (0,8 par convention), puis $\mathrm{RUL}(k)=k_{\mathrm{EOL}}-k$. Le choix de $s$ est une décision, non une mesure.
- **Comptage de coulombs** : $\mathrm{SOC}(t)=\mathrm{SOC}(t_0)+\dfrac{1}{Q_{\max}}\int_{t_0}^{t}\eta\,i(\tau)\,d\tau$, $i$ le courant (positif en charge), $\eta$ le rendement coulombien. Hypothèse : $Q_{\max}$ et $\eta$ connus ; l'erreur de courant s'intègre sans borne, d'où le recalage par le filtre.
- **Circuit équivalent à un réseau RC** : $V(t)=\mathrm{OCV}(\mathrm{SOC})-R_0\,i-V_1$, $\dot V_1=-\dfrac{V_1}{R_1C_1}+\dfrac{i}{C_1}$. Le filtre de Kalman étendu linéarise $\mathrm{OCV}(\cdot)$ autour de l'état estimé ; il suppose des bruits gaussiens et un modèle assez fidèle. Des paramètres lents ($R_0$, $Q_{\max}$) peuvent s'ajouter à l'état, ce qui fait du SOH un sous-produit de l'estimation.
- **Particule unique** : dans une particule de rayon $R_p$, $\dfrac{\partial c}{\partial t}=\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\!\left(D\,r^2\,\dfrac{\partial c}{\partial r}\right)$, $c$ la concentration de lithium solide, $D$ la diffusivité ; le courant impose le flux en $r=R_p$. Hypothèse du SPM : l'électrolyte ne limite pas, toutes les particules d'une électrode se comportent pareil.
- **SEI limitée par la diffusion** : l'épaisseur croît comme $L_{\mathrm{SEI}}(t)\propto\sqrt{t}$ (hypothèse de Li et al., un seul paramètre libre), ce qui reproduit la dépendance en racine du temps de la littérature. Le modèle ne dépend pas du SOC, limite relevée par les mêmes auteurs.
- **Régression de Severson** : $\log y_i=\mathbf w^{\top}\mathbf x_i+b$, avec $y_i$ la durée de vie, $\mathbf x_i$ les descripteurs (min, moyenne, variance de $\Delta Q_{100-10}(V)$, résistance, température), et un élastique net : $\min_{\mathbf w}\ \lVert\log\mathbf y-X\mathbf w\rVert^2+\lambda\big(\alpha\lVert\mathbf w\rVert_1+\tfrac{1-\alpha}{2}\lVert\mathbf w\rVert_2^2\big)$. Erreur moyenne en pourcentage : $\dfrac{100}{n}\sum_i\dfrac{|y_i-\hat y_i|}{y_i}$.

## En pratique

- **Découper par cellule, jamais par cycle.** Deux cycles voisins d'une cellule sont presque identiques : les répartir entre apprentissage et test fuit ([[Data leakage]]). Maher et Yerken (ICRERA 2025) passent de $R^2$ jusqu'à 0,9999 avec un découpage aléatoire à environ 0,91 avec une validation par groupe de cellules. Le et Nguyen (arXiv, juillet 2026), sur le jeu NASA avec une validation « une batterie laissée de côté », rapportent un écart de 119 % de performance avec une validation croisée à 5 plis. Chez Severson, un jeu secondaire de 40 cellules a été produit **après** le développement des modèles : protocole à imiter.
- **Fixer la cible avant de comparer** : seuil (70 ou 80 %), capacité mesurée à quel courant, à quelle température, cycles ou temps. Les erreurs de Severson se lisent sur un jeu à décharge imposée.
- **Lire les chiffres d'origine en entier.** Severson annonce 9,1 % d'erreur sur 100 cycles ; le tableau 1 donne, selon le modèle et le jeu de test, de 7,5 % (modèle complet, une cellule atypique exclue) à 14,7 %, avec un RMSE de 91 à 214 cycles. Le chiffre de 9,1 % ne se retrouve pas dans ce tableau tel que lu ; écart non élucidé. Le modèle naïf (durée de vie moyenne de l'entraînement) fait 30 et 36 %.
- **Du labo à la flotte.** Les descripteurs de Severson exigent des décharges complètes à courant constant (4 C), une température imposée et une seule chimie. En exploitation, charges partielles, températures et courants variables : ces courbes n'existent pas telles quelles (raisonnement, non sourcé ici). Deux textes de 2025-2026 posent la généralisation entre chimies, formats et conditions comme un problème ouvert : la revue de Liu et al. (approches conventionnelles limitées en généralisation entre domaines) et Chan et al. (hétérogénéité qui rend un modèle unique difficile).
- **Pas de panne réelle.** L'EOL à 80 % est un seuil de capacité, pas une défaillance. Le RUL à 80 % ne dit rien du risque de sûreté ; le dépôt de lithium est cité comme risque d'incendie par la source de blog, non vérifiée.
- **Entre fabricants.** Sours et al. (préprint, octobre 2024, révisé mai 2025) combinent courbes tension-capacité et résistance continue précoce, et prédisent le nombre de cycles à l'EOL de fabricants jamais vus avec une erreur absolue moyenne de 150 cycles. Piste, pas garantie.
- **Incertitude et décision.** Un RUL sans intervalle ne se décide pas : [[Prédiction conforme]], [[Calibration]]. Le passage au remplacement, à la seconde vie ou à la garantie relève de [[Politique de maintenance et coût]].
- **Critiques à garder en tête.** Li et al. : valider sur la capacité seule est insuffisant. Liu et al. (revue 2026, arXiv 2608.26111, numéro et date de dépôt affichée qui ne concordent pas, non élucidé) retiennent comme défis l'accès aux données, la validation, la confiance et le déploiement.

## Approches voisines & alternatives

- [[PyBaMM]] — simulation physique de cellule (SPM, DFN), jumeau numérique de batterie une fois recalé.
- [[Jumeau numérique et modèles hybrides]] — fusionner modèle physique et données.
- [[Indicateurs de santé]] — construire un indicateur monotone avant de prédire.
- [[RUL par apprentissage profond]] — réseaux de séquence et leurs pièges, vus sur turboréacteurs.
- [[RUL par analyse de survie]] — loi de durée de vie avec censure, utile quand peu de cellules vont à la fin de vie.
- [[Maintenance prédictive avec peu de pannes]] — transfert et simulation quand les trajectoires manquent.
- [[Jeux de données PHM]] — les batteries NASA PCoE et leurs limites de licence.
- [[Politique de maintenance et coût]] — du RUL à la décision.
- [[Time series feature engineering]] — la voie par descripteurs, sans réseau.
- [[Adaptation de domaine]] — passer d'une chimie ou d'un protocole à l'autre.
- [[Maintenance prédictive]] — le dossier.

## Pour aller plus loin

- Severson et al. (2019), *Data-driven prediction of battery cycle life before capacity degradation*, Nature Energy 4(5):383-391. DOI : https://doi.org/10.1038/s41560-019-0356-8 ; données : https://data.matr.io/1
- Attia et al. (2020), *Closed-loop optimization of fast-charging protocols for batteries with machine learning*, Nature 578(7795):397-402. DOI : https://doi.org/10.1038/s41586-020-1994-5
- Attia et al. (2022), *"Knees" in lithium-ion battery aging trajectories*, arXiv : https://arxiv.org/abs/2201.02891 (publication en revue : non vérifiée)
- Li, Kirkaldy, Oehler, Marinescu, Offer, O'Kane (2023), *Lithium-ion battery degradation: using degradation mode analysis to validate lifetime prediction modelling*, arXiv : https://arxiv.org/abs/2311.05482
- Edge et al. (2021), *Lithium ion battery degradation: what you need to know*, Phys. Chem. Chem. Phys. 23:8200-8221 (résumé lu, texte non ouvert) : https://pubs.rsc.org/en/content/articlelanding/2021/cp/d1cp00359c
- Sulzer, Marquis, Timms, Robinson, Chapman (2021), *Python Battery Mathematical Modelling (PyBaMM)*, J. Open Research Software. DOI : https://doi.org/10.5334/jors.309
- Doyle, Fuller, Newman (1993), *Modeling of galvanostatic charge and discharge of the lithium/polymer/insertion cell*, J. Electrochem. Soc. 140(6):1526-1533. DOI : https://doi.org/10.1149/1.2221597
- Plett (2004), *Extended Kalman filtering for battery management systems of LiPB-based HEV battery packs*, J. Power Sources 134(2), parties 1 à 3. DOI (partie 1) : https://doi.org/10.1016/j.jpowsour.2004.02.031
- Roman, Saxena, Robu, Pecht, Flynn (2021), *Machine learning pipeline for battery state of health estimation*, arXiv : https://arxiv.org/abs/2102.00837
- Tan et al. (2025), *BatteryLife: a comprehensive dataset and benchmark for battery life prediction*, KDD 2025, arXiv : https://arxiv.org/abs/2502.18807
- Tan, Hong, Li, Huang, Zhang (2025-2026), *Pretrained Battery Transformer*, arXiv : https://arxiv.org/abs/2512.16334
- Chan et al. (2025), *Universal battery degradation forecasting driven by foundation model across diverse chemistries and conditions*, arXiv : https://arxiv.org/abs/2601.00862
- Sours et al. (2024), *Early-cycle internal impedance enables ML-based battery cycle life predictions across manufacturers*, arXiv : https://arxiv.org/abs/2410.05326
- Maher, Yerken (2025), *Comprehensive machine learning for lithium-ion battery state-of-health estimation using group-wise cross-validation*, ICRERA 2025. DOI : https://doi.org/10.1109/ICRERA66237.2025.11283788
- Le, Nguyen (2026), *Charging phase health indicators for battery state-of-health estimation*, arXiv : https://arxiv.org/abs/2607.23482
- Liu et al. (2026), *Large models for battery prognostics and health management: a review and future roadmap*, arXiv : https://arxiv.org/abs/2608.26111
- Zhang, Guo, Ge, Mahon, Shen (2025), *Experimental methods, health indicators, and diagnostic strategies for retired lithium-ion batteries: a comprehensive review*, arXiv : https://arxiv.org/abs/2512.01294
- Mauthe, Braun, Raible, Zeiler, Huber (2024), *Overview of publicly available degradation data sets for tasks within prognostics and health management*, arXiv : https://arxiv.org/abs/2403.13694
- Oxford Battery Degradation Dataset 1 (Howey, Birkl, 2017). DOI : https://doi.org/10.5287/bodleian:KO2kdmYGg ; CALCE : https://calce.umd.edu/battery-data ; NASA : https://catalog.data.gov/dataset/li-ion-battery-aging-datasets
