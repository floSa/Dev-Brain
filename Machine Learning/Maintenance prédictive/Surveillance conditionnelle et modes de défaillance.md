---
role: notion
nom: Surveillance conditionnelle et modes de défaillance
alias: [CBM, Condition-based maintenance, Courbe P-F, Intervalle P-F, AMDEC, FMEA]
categorie: ml/maintenance
domaines: [data-sci, infra-ops]
tags: [predictive-maintenance, condition-monitoring]
---

# Surveillance conditionnelle et modes de défaillance

## Aperçu

- La **surveillance conditionnelle** mesure l'état d'un équipement ; la **maintenance conditionnelle** (CBM) déclenche l'intervention sur cet état et non sur le calendrier. Avant tout modèle, trois questions amont : quel **mode de défaillance** surveiller, de combien de temps on dispose entre le signe avant-coureur et la panne, quelle norme cadre la mesure.
- Cette page fixe ce vocabulaire et ses hypothèses. Le pronostic chiffré (RUL) est dans [[Maintenance prédictive et RUL]] ; le dossier est présenté par [[Maintenance prédictive]].

## Concepts clés

### Stratégies de maintenance

- **Correctif** (après la panne), **préventif systématique** (au calendrier ou au nombre de cycles), **conditionnel** (sur l'état mesuré), **prédictif** (sur l'état projeté dans le futur). La notion [[Maintenance prédictive et RUL]] les range déjà ; ce brain emploie « conditionnel » et « prédictif » presque comme synonymes.
- Les sources ne tracent pas la frontière au même endroit. Le guide O&M du DOE/PNNL (PNNL-19634, 2010) définit le prédictif comme le fait de fonder le besoin de maintenance sur la condition réelle de la machine plutôt que sur un calendrier prédéfini, donc ce que d'autres appellent conditionnel. La norme de terminologie EN 13306:2018 existe ; ses définitions exactes sont **non vérifiées** (norme payante, texte non lu).
- Le calendrier ne vaut que s'il existe une usure. Nowlan et Heap (United Airlines, 1978) sont la source de la maintenance centrée sur la fiabilité (RCM). D'après un résumé secondaire, 4 % des éléments étudiés suivaient la courbe en baignoire et 89 % n'avaient aucune zone d'usure ; ces pourcentages sont **non vérifiés dans le rapport** (PDF non ouvert).

### CBM : acquérir, traiter, décider

- Jardine, Lin et Banjevic (2006) décrivent la CBM en trois étapes : acquisition des données, traitement, décision de maintenance. Le diagnostic et le pronostic en sont les deux piliers (d'après le résumé de la revue).
- Isermann définit un **défaut** (*fault*) comme un écart non permis d'une propriété caractéristique par rapport au comportement acceptable : un état qui peut mener à un dysfonctionnement ou à une défaillance. Il distingue les défauts **brusques**, **naissants** (dérive lente) et **intermittents**. Seul le défaut naissant offre une fenêtre à la CBM.
- Isermann note aussi que la supervision classique par valeurs limites est simple et fiable, mais ne réagit qu'après un changement déjà grand et ne permet pas de diagnostic fin.

### Mode de défaillance et AMDEC

- Un **mode de défaillance** est la manière dont un élément cesse de remplir sa fonction. L'**AMDEC** (FMEA) l'énumère, avec ses effets locaux et globaux et, si possible, ses causes. La CEI 60812:2018 (édition 3, août 2018) explique comment l'AMDE, y compris sa variante **AMDEC** (FMECA, avec criticité), est planifiée, réalisée, documentée et maintenue. Elle s'applique au matériel, aux logiciels et aux processus, y compris l'action humaine.
- **Indice de criticité** : en usage français, $C = F \times D \times G$ (fréquence, détection, gravité). Côté anglophone, le **RPN** (*risk priority number*) vaut $S \times O \times D$ (*severity*, *occurrence*, *detection*). Les trois échelles sont ordinales, souvent graduées de 1 à 10 (usage courant, non imposé par ce qui a été lu).
- **Critiques du produit.** Des praticiens relèvent que les doublons sont fréquents, que la gravité élevée doit être traitée quelle que soit la valeur du RPN, et que l'échelle de détection est jugée difficile à appliquer (Carlson, Accendo Reliability, 2018). La CEI 60812:2018 elle-même prévoit d'autres modes de calcul du RPN et une méthode par matrice de criticité. Pour l'automobile, le manuel AIAG-VDA (2019) remplace le RPN par des tables d'*Action Priority* (S, O, D donnent une priorité haute, moyenne ou basse) : **d'après des synthèses secondaires, manuel non consulté**.
- **Lien avec la maintenance conditionnelle.** La colonne « détection » de l'AMDEC pose la question qui intéresse ici : existe-t-il un précurseur mesurable pour ce mode ? Un mode sans précurseur (rupture brutale) n'est pas justiciable de la CBM. Un mode avec précurseur (écaillage de roulement et vibrations) se traite par [[Analyse vibratoire]], [[Indicateurs de santé]] et [[Diagnostic de défauts de roulements]].

### Courbe P-F

- **P** (*potential failure*) : condition identifiable qui indique qu'une défaillance fonctionnelle est imminente. **F** (*functional failure*) : l'élément ne tient plus le niveau de performance requis. L'**intervalle P-F** est le temps entre les deux. Définitions reprises de synthèses secondaires de Nowlan et Heap ; le rapport (DTIC AD-A066579) n'a pas pu être ouvert, seule sa page de description l'a été : elle cite l'inspection pour détecter les défaillances potentielles parmi ses quatre familles de tâches.
- **Ce que la courbe suppose** :
  1. Le mode a un précurseur détectable avant F.
  2. L'intervalle est stable, ou au moins connu comme distribution. Christer et Waller (1984) modélisent le même objet sous le nom de *delay time*, mais **aléatoire** ; l'intervalle P-F de la RCM est pris comme constant.
  3. **P dépend de la technique de détection**, pas seulement de la physique : une méthode plus sensible avance P et allonge l'intervalle (synthèse Reliable Media, 2024). Un intervalle P-F est donc propre à un couple mode de défaillance et technique.
  4. Une courbe par mode de défaillance, non par machine.
  5. (Lecture, non sourcée.) La dégradation est supposée monotone et lisse ; sur le terrain, elle est bruitée et peut régresser après une intervention (regraissage).
- L'intervalle P-F est un artefact de modélisation, pas une mesure. Le chiffrer exige des historiques de pannes menées à terme, justement rares ([[Maintenance prédictive avec peu de pannes]]).

## Les maths, simplement

- **Période d'inspection.** Avec un intervalle P-F déterministe $I$ et un délai de réaction $m$ (commander, planifier, arrêter), une inspection de période $T$ voit tout défaut au plus tard $T$ après son apparition. Il faut donc $T + m \le I$. La règle pratique « inspecter à la moitié de l'intervalle » ($T = I/2$) est une heuristique de praticiens (Reliable Media, 2024), qui laisse $I/2$ pour réagir.
- **Si le délai est aléatoire** ($H$ de fonction de répartition $F_H$), un défaut apparu au hasard dans un cycle devient panne avant l'inspection suivante avec la probabilité $\dfrac1T\int_0^T F_H(s)\,ds$ (raisonnement : l'apparition est uniforme dans le cycle ; inspection supposée parfaite). Pour $H \equiv I$, ce terme vaut $0$ si $T \le I$ et $1 - I/T$ sinon. Pour un $H$ dispersé, $T = I/2$ ne donne plus zéro : la règle de la moitié ne vaut que pour un intervalle déterministe.
- **Criticité** : $C = F \times D \times G$ ou $\mathrm{RPN} = S \times O \times D$. Un produit de rangs n'est pas une mesure de risque : $(S,O,D) = (10,1,1)$ et $(2,5,1)$ donnent le même RPN de 10 pour des risques sans commune mesure.

## En pratique

- **Ordre de travail.** Fonctions et criticité de l'équipement (AMDEC), puis modes à précurseur détectable, puis mesure et fréquence d'échantillonnage, puis estimation de l'intervalle P-F (ou du délai) sur l'historique, puis période d'inspection ou seuil d'alerte ([[Score et seuil d'alerte]]).
- **ISO 17359:2018** : *Condition monitoring and diagnostics of machines — General guidelines* (édition 3, confirmée en 2023, ISO/TC 108/SC 5). Objet : lignes directrices sur les procédures générales à considérer pour mettre en place un programme de surveillance conditionnelle des machines, avec renvoi aux normes associées ; applicable à toutes les machines.
- **ISO 20816-1:2016** : *Mechanical vibration — Measurement and evaluation of machine vibration — Part 1: General guidelines* (édition 1, novembre 2016). Objet : conditions et procédures générales de mesure et d'évaluation des vibrations sur les parties tournantes, non tournantes et non alternatives de machines complètes ; critères en amplitude et en variation, pour la surveillance en exploitation et la réception. Remplace l'ISO 10816-1:1995. Au 2026-10-02, la page ISO la donne « en cours de révision », l'édition 2 étant au stade FDIS (vote ouvert le 2026-08-11) : la citer avec cette réserve.
- **ISO 20816-3:2022** (machines industrielles de plus de 15 kW, de 120 à 30 000 tr/min) précise qu'elle **ne fournit pas d'évaluation diagnostique** de l'état d'un engrenage ou d'un roulement : un niveau global de vibration dit s'il faut s'inquiéter, pas ce qui est cassé. Les quatre zones d'évaluation A à D (machine neuve, acceptable, insatisfaisante pour un service continu, susceptible de provoquer des dommages) viennent d'une synthèse non officielle : **valeurs limites non vérifiées, donc non reprises ici**.
- ISO 13379-1:2025 (interprétation des données et techniques de diagnostic) existe aussi ; seul son titre et son objet général ont été lus.
- **Pièges** : prendre un seuil de norme pour un seuil de pronostic ; confondre le niveau d'alarme et le délai de réaction $m$ ; reprendre l'intervalle P-F d'un autre site ou d'une autre technique.

## Approches voisines & alternatives

- [[Maintenance prédictive et RUL]] — la grandeur pronostique (RUL) ; la surveillance conditionnelle la précède.
- [[Politique de maintenance et coût]] — transformer l'état ou le RUL en décision et en coût.
- [[Indicateurs de santé]] — résumer les capteurs en une grandeur qui suit la dégradation.
- [[Analyse vibratoire]] et [[Diagnostic de défauts de roulements]] — le précurseur le plus courant sur machine tournante.
- [[Time series anomaly detection]] et [[Types d'anomalies et régimes de supervision]] — la détection d'écart sans connaissance du mode.
- [[Analyse de survie]] — la durée jusqu'à la panne avec censure ; [[RUL par analyse de survie]] en est la déclinaison maintenance.
- [[Jumeau numérique et modèles hybrides]] — la surveillance appuyée sur un modèle du mécanisme.
- [[Amazon Monitron]] — une offre de surveillance conditionnelle livrée de bout en bout (capteurs, passerelle, analyse dans le cloud) ; fermée aux nouveaux clients depuis le 2024-10-31.

## Pour aller plus loin

- Nowlan, Heap (1978), *Reliability-Centered Maintenance*, rapport DoD / United Airlines, AD-A066579 : https://apps.dtic.mil/sti/pdfs/ADA066579.pdf (non ouvert ; page de description : https://everyspec.com/DoD/DOD-General/AD-A066579_18228/)
- Jardine, Lin, Banjevic (2006), *A review on machinery diagnostics and prognostics implementing condition-based maintenance*, Mechanical Systems and Signal Processing 20(7):1483-1510. DOI : https://doi.org/10.1016/j.ymssp.2005.09.012
- Christer, Waller (1984), *Delay time models of industrial inspection maintenance problems*, JORS 35(5):401-406. DOI : https://doi.org/10.1057/jors.1984.80
- Isermann (2004), *Model-based fault detection and diagnosis — status and applications*, IFAC Proceedings Volumes 37(6):49-60 (version lue). DOI : https://doi.org/10.1016/S1474-6670(17)32149-3
- IEC 60812:2018, *Failure modes and effects analysis (FMEA and FMECA)* : https://webstore.iec.ch/publication/26359
- ISO 17359:2018 : https://www.iso.org/standard/71194.html ; ISO 20816-1:2016 : https://www.iso.org/standard/63180.html ; ISO 20816-3:2022 : https://www.iso.org/standard/78311.html
- Sullivan, Pugh, Melendez, Hunt (2010), *Operations & Maintenance Best Practices Guide, Release 3.0*, PNNL-19634 : https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-19634.pdf
- Carlson (2018), *Understanding RPN: limitations, problems, solutions*, Accendo Reliability : https://accendoreliability.com/understanding-rpn-limitations-problems-solutions/
