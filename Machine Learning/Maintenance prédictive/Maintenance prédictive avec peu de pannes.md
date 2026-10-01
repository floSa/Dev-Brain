---
role: notion
nom: Maintenance prédictive avec peu de pannes
alias: [PdM avec peu de pannes, Pannes rares, Peu de données de défaillance, Few failure data]
categorie: ml/maintenance
domaines: [data-sci, ml-eng, mlops]
tags: [predictive-maintenance, class-imbalance, anomaly-detection, transfer-learning, synthetic-data]
---

# Maintenance prédictive avec peu de pannes

## Aperçu

- Le vrai problème industriel de la maintenance prédictive n'est pas le choix du réseau : **il y a presque toujours très peu de pannes à apprendre**. Un équipement bien entretenu casse rarement, on le remplace avant, et une machine neuve n'a pas d'historique. Les jeux de benchmark (C-MAPSS) cachent le problème en offrant des centaines de trajectoires menées jusqu'à la panne.
- Cette page classe les parades (apprendre le normal seul, transférer, simuler, ajouter de la physique) et dit ce que chacune ne remplace pas. Les revues citées sont lues en texte ou en résumé seul : c'est précisé dans *Pour aller plus loin*.

## Concepts clés

### Le problème : pannes rares, classes déséquilibrées

- Les revues disent la même chose. Azari et al. (IEEE Access, 2023) : manque de données d'entraînement, **surtout défectueuses**, calcul, décalage de distribution. Schwarz et al. (*Artificial Intelligence Review*, 2024) : la plupart des données viennent du fonctionnement normal, d'où des jeux déséquilibrés où il est « très difficile, voire impossible » d'entraîner un modèle fiable. Wang et al. (2025) : peu de données jusqu'à la panne en pratique, la plupart des moteurs étant retirés avant la défaillance.
- **Un cas chiffré** (Hakami, *Scientific Reports*, 2024) : le jeu de production IMPROVE (Kaggle) compte **8 expériences jusqu'à la panne**, soit 228 416 observations saines pour 8 observations de panne, environ $3{,}5\times10^{-5}$ de positifs.
- **L'horizon de panne** : étiqueter « panne » les $H$ derniers instants avant la panne (Susto et al., d'après Hakami). Avec $H=720$ et 8 pannes, les positifs passent de 8 à 5 760, environ 2,5 % des observations (calcul sur ces chiffres). Mais les 8 pannes restent 8 : les positifs sont des copies corrélées d'un même événement.
- Les outils usuels du déséquilibre s'appliquent ([[Imbalanced classification]]). Le point propre à la maintenance : **le taux de base commande l'utilité du détecteur** ([[Score et seuil d'alerte]], erreur du taux de base).

### Apprendre le normal, sans pannes

- Le fonctionnement normal abonde. Le régime semi-supervisé de [[Types d'anomalies et régimes de supervision]] l'apprend et signale l'écart : [[Time series anomaly detection]], [[Autoencodeurs]], [[Détection d'outliers multivariée]], [[Détection hors distribution (OOD)]].
- **Ce que cela donne** : « la machine ne se comporte plus comme d'habitude », sans étiquette de panne. Nunes, Santos et Rocha (CIRP JMST, 2023, résumé seul) relient la détection d'anomalies au pronostic : elle retire les données erronées et repère des événements utiles au pronostic.
- **Ce que cela ne donne pas** : ni le temps restant, ni le mode de défaillance. Un écart n'est pas une panne : un changement de régime de marche ([[Data drift]]) le provoque aussi. Fixer le seuil ([[Score et seuil d'alerte]]) et évaluer ([[Évaluer une détection d'anomalies]]) demandent quelques pannes réelles.

### Transférer d'une machine à une autre

- **Idée** : entraîner là où il y a des pannes (flotte voisine, simulation, la *source*), puis adapter à la machine où il y en a peu (la *cible*). Azari et al. (2023, résumé seul) en font la revue systématique pour la maintenance prédictive. Le brain n'a pas de page sur l'apprentissage par transfert hors vision ni sur l'adaptation de domaine ; voisines : [[Transfer learning vision]], [[Méta-apprentissage et few-shot learning]].
- **Adaptation de domaine** (*domain adaptation*) : aligner les distributions source et cible sans étiquettes de panne côté cible. Wang et al. (2025) décrivent le schéma général comme l'équilibre entre une perte de prédiction sur la source et une perte d'adaptation.
- **Ce que mesure un benchmark** : Wang et al. comparent huit méthodes sur C-MAPSS en transférant d'un sous-jeu à l'autre (12 paires), même extracteur pour toutes, cinq exécutions, hyperparamètres choisis sur le risque source pour ne pas fuiter la cible. RMSE moyen (tableau III) : source seule **36,41** ; DDC 22,89 ; ConsDANN 22,06 ; ADARUL 22,59 ; CADA 21,90. Mais HoMM (40,95) fait **pire** que la source seule, et sur F1 vers F2 la source seule (17,20) bat CADA (22,95). Les auteurs notent que la source seule bat parfois l'état de l'art.
- **Flotte hétérogène** : Wang et al. citent les écarts entre compagnies, moteurs et conditions comme source de décalage ; Nunes et al. notent que les approches de pronostic sont le plus souvent propres à une pièce ou un équipement. La confidentialité bloque le partage de données entre acteurs : l'[[Apprentissage fédéré]] est la piste citée (Wang et al. ; Yang et al. 2026, sur C-MAPSS).

### Simuler et synthétiser

- **Revue** : Nieminen et al. (*J. Intelligent Manufacturing*, 2026, résumé seul) couvrent 86 articles depuis 2020. Quatre familles : augmentation de données, modèles génératifs, simulations physiques et approches hybrides, transformations de caractéristiques. Conclusion : les modèles **hybrides et informés par la physique** sont les plus utiles en domaine critique ; cadre proposé en cinq phases (SD-PdM).
- **GAN** : Hakami génère des trajectoires synthétiques « semblables » aux 8 réelles, puis entraîne LSTM et classifieurs : ANN à 88,98 % d'exactitude pour $H=720$. Voir [[GANs]], [[Synthetic data generation]]. Schwarz et al. jugent les modèles génératifs les plus prometteurs et placent la validation de la **plausibilité** du synthétique parmi les problèmes ouverts.
- **Jumeau numérique** : simuler la machine par un modèle physique pour produire les pannes que l'exploitation n'a pas fournies. Dong et al. (*Heliyon*, 2023, résumé seul) en font la revue, limites et défis compris. Détail : [[Jumeau numérique et modèles hybrides]].
- C-MAPSS est lui-même une simulation : un modèle qui y réussit a appris le simulateur ([[RUL par apprentissage profond]]).

### Fusionner un modèle physique

- Fassi et al. (*IEEE Trans. Power Electronics*, 2024, résumé seul) opposent, pour les convertisseurs de puissance, modèles à base de physique, données seules et apprentissage **informé par la physique**, proposé contre les limites de données, de cohérence physique et de généralisation.
- Forme générique (non propre à cette revue) : $y=f_{\text{phys}}(x;\theta)+g_{\text{ML}}(x)$, le réseau n'apprenant que l'écart au modèle. Voir [[Jumeau numérique et modèles hybrides]], [[Modèles de Markov cachés et filtre de Kalman]].

### Peu d'étiquettes côté cible : modèles pré-entraînés

- Fu et al. (arXiv, 2026) affinent un modèle de représentation de séries temporelles pré-entraîné sur de nombreux domaines et annoncent un RUL utile avec **moins de 1 %** des échantillons de la cible (moteurs d'avion, roulements). Annonce des auteurs, non reproduite ici. Cadre : [[Foundation models pour séries temporelles]].

## Les maths, simplement

- **Taux de base** : avec $p$ la proportion de « panne », même un détecteur de sensibilité 1 a une précision d'alerte $p/(p+(1-p)\,\mathrm{FPR})$. À $p=3{,}5\times10^{-5}$, plus de la moitié des alertes ne sont vraies que si $\mathrm{FPR}$ reste sous environ $3{,}5\times10^{-5}$ (même mécanique que dans [[Score et seuil d'alerte]]).
- **Adaptation de domaine** : minimiser $\mathcal L_{\text{source}}+\lambda\,d(P_S,P_T)$, $d$ mesurant l'écart des distributions et $\lambda$ l'équilibre que Wang et al. signalent comme difficile.
- **Pannes effectives** : l'information tient dans le nombre de pannes **indépendantes**, pas d'observations (raisonnement).

## En pratique

- **Compter les pannes indépendantes avant de choisir.** Ordres de grandeur de jugement, non sourcés : moins d'une dizaine, détection d'anomalies sur du normal, règles d'expert, modèle physique, et aucun modèle supervisé validable ; quelques dizaines, survie ([[RUL par analyse de survie]]) ou transfert depuis une flotte voisine.
- **Valider par unité et par panne** ([[Data leakage]]) : les observations d'une même panne sont des quasi-copies. Une validation « une panne laissée de côté » est honnête, mais à variance élevée.
- **Réserver les pannes réelles au test**, jamais à la génération ni au réglage : entraîner sur du synthétique, **tester sur du réel**. Le texte de Hakami lu ici ne décrit pas de jeu de test réel séparé.
- **Mettre le coût dans la décision** : [[Politique de maintenance et coût]]. Les jeux ouverts de pannes réelles sont rares : [[Jeux de données PHM]].

## Ce qui ne remplace pas des pannes réelles

- **Un GAN ne sait que ce qu'on lui montre.** Hakami : il génère des données semblables aux réelles fournies et ne généralise pas à un mode de défaillance jamais vu. Schwarz et al. : la plausibilité du synthétique reste à valider.
- **Un simulateur vaut son modèle.** C-MAPSS impose un taux de dégradation exponentiel de paramètres tirés au hasard (Saxena et al. 2008) ; N-CMAPSS améliore la mission de vol mais reste simulé.
- **Le transfert peut faire pire que rien** : HoMM (40,95) contre la source seule (36,41), et les paires du benchmark viennent d'un **même simulateur**, bien plus proches que deux machines réelles. Basora et al. (2025) ne trouvent aucune méthode d'incertitude robuste hors distribution ; un modèle transféré dans un régime inédit y est (inférence de cette page).
- **Le normal ne dit pas la panne** : détecter un écart n'enseigne ni délai ni cause.
- **Le test manque de puissance** : avec 8 pannes, une exactitude de 89 % ou de 74 % n'a pas d'intervalle utilisable (raisonnement).

## Approches voisines & alternatives

- [[Maintenance prédictive et RUL]] — le cadre du pronostic.
- [[RUL par apprentissage profond]] — ce qui se passe quand les pannes abondent (en simulation).
- [[RUL par analyse de survie]] — exploite les unités censurées.
- [[Jumeau numérique et modèles hybrides]] — simulation et physique.
- [[Politique de maintenance et coût]] — décider malgré l'incertitude.
- [[Maintenance prédictive]] — le dossier.

## Pour aller plus loin

Lus en texte : Hakami (2024) ; Wang et al. (2025), sections défis et benchmark. Lus en **résumé seul** : Azari, Schwarz, Nieminen, Nunes, Fassi, Dong.

- Azari, Flammini, Santini, Caporuscio (2023), *A Systematic Literature Review on Transfer Learning for Predictive Maintenance in Industry 4.0*, IEEE Access 11. DOI : https://doi.org/10.1109/ACCESS.2023.3239784
- Schwarz et al. (2024), *Data augmentation in predictive maintenance applicable to hydrogen combustion engines: a review*, Artificial Intelligence Review 58(1). DOI : https://doi.org/10.1007/s10462-024-11021-9
- Nieminen, Gebreweld, Liuha et al. (2026), *Synthetic Data for Predictive Maintenance: A Systematic Review and Framework for Industry 4.0 Applications*, J. Intelligent Manufacturing. DOI : https://doi.org/10.1007/s10845-026-02795-6
- Nunes, Santos, Rocha (2023), *Challenges in predictive maintenance – A review*, CIRP JMST 40. DOI : https://doi.org/10.1016/j.cirpj.2022.11.004
- Fassi, Heiries, Boutet, Boisseau (2024), *Toward Physics-Informed Machine-Learning-Based Predictive Maintenance for Power Converters—A Review*, IEEE Trans. Power Electronics 39(2). DOI : https://doi.org/10.1109/TPEL.2023.3328438
- Dong, Xia, Zhu, Duan (2023), *Overview of predictive maintenance based on digital twin technology*, Heliyon. DOI : https://doi.org/10.1016/j.heliyon.2023.e14534
- Hakami (2024), *Strategies for overcoming data scarcity, imbalance, and feature selection challenges in machine learning models for predictive maintenance*, Scientific Reports 14, 9645. DOI : https://doi.org/10.1038/s41598-024-59958-9
- Wang et al. (2025), *Deep Domain Adaptation for Turbofan Engine Remaining Useful Life Prediction*, arXiv : https://arxiv.org/abs/2510.03604
- Fu, Hu, Jin, Peng (2026), *PEFT-MuTS*, arXiv : https://arxiv.org/abs/2601.22631
- Basora et al. (2025), RESS 253, 110513. DOI : https://doi.org/10.1016/j.ress.2024.110513
- Yang et al. (2026), *Collaborative System Failure Prognostics via Federated Longitudinal-Survival Modeling*, arXiv : https://arxiv.org/abs/2607.26038
