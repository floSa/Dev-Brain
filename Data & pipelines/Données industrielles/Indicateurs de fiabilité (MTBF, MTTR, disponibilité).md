---
role: notion
nom: Indicateurs de fiabilité (MTBF, MTTR, disponibilité)
alias: [MTBF, MTTR, MTTF, Disponibilité, Taux de panne, Taux de défaillance, Disponibilité inhérente, Mean time between failures]
categorie: data/industrie
domaines: [data-sci, mlops]
tags: [predictive-maintenance, survival-analysis, markov]
---

# Indicateurs de fiabilité (MTBF, MTTR, disponibilité)

## Aperçu

- Trois chiffres résument ce qu'une flotte de machines a fait subir à l'exploitation : le **temps moyen entre pannes** (MTBF), le **temps moyen de remise en état** (MTTR) et la **disponibilité**, part du temps où la machine est en état de servir. Ce sont des **moyennes**, calculées sur l'historique, et ils ne disent rien de l'état d'une machine précise aujourd'hui (pour cela : [[Indicateurs de santé]] et [[Maintenance prédictive et RUL]]).
- Leurs formules tiennent en une ligne, leurs **définitions** non : selon la norme, la GMAO ou le fournisseur, « panne », « temps de réparation » et même « MTBF » ne désignent pas la même durée. Cette page pose les définitions, les hypothèses derrière la formule classique $A=\mathrm{MTBF}/(\mathrm{MTBF}+\mathrm{MTTR})$, et ce qu'on peut réellement calculer depuis une GMAO.
- L'indicateur de rendement d'une ligne, qui porte le mot « disponibilité » dans un autre sens, est traité dans [[OEE et rendement global]].

## Concepts clés

### Réparable ou non : deux familles de mesures

- Un équipement **non réparable** (ou remplacé à la première panne) n'a qu'une durée de vie $T$ : on parle de **MTTF** (*mean time to failure*), espérance de $T$. Un équipement **réparable** enchaîne marche, panne, remise en état, marche : on parle de MTBF, de taux d'occurrence des pannes et de disponibilité.
- La norme IEC 61703:2016 (aperçu lu : champ d'application et sommaire) range les équipements en trois classes : non réparables ; réparables à temps de remise en état nul (modèle : processus de renouvellement simple) ; réparables à temps de remise en état non nul (processus de renouvellement **alterné**). C'est ce dernier cadre qui porte la disponibilité.
- Le guide NIST (chap. 8) définit séparément le **taux de panne** $h(t)$ d'une population non réparable (« le taux auquel les survivants tombent de la falaise ») et le **taux d'occurrence des pannes** (ROCOF, $m(t)$, dérivée du nombre espéré de pannes cumulées) d'un système réparable. Ce sont deux objets distincts ; les pages lues ne l'énoncent pas en toutes lettres, et le vocabulaire courant les confond sous « taux de panne ».

### Les durées : ce que « MTBF » et « MTTR » recouvrent

- **MTBF.** Le vocabulaire IEC 60050-192 définit la moyenne des temps de **bon fonctionnement** entre pannes (*mean operating time between failures*, [192-05-13]) ; IEC 61703 définit à part, au point 3.3, un « mean time between failures » qui n'est pas le même terme (le sommaire cite même une figure « time between failures versus operating time between failures »). Le texte de 3.3 n'est pas dans l'aperçu : la différence exacte (durée de marche seule, ou marche plus remise en état) n'est **pas vérifiée** ici.
- **Désaccord entre sources.** Wikipédia (Availability) écrit $A=\mathrm{MTTF}/(\mathrm{MTTF}+\mathrm{MTTR})=\mathrm{MTTF}/\mathrm{MTBF}$, donc un MTBF qui **inclut** la remise en état (de début de panne à début de panne). La forme $\mathrm{MTBF}/(\mathrm{MTBF}+\mathrm{MTTR})$, usuelle en maintenance, suppose un MTBF qui **exclut** la remise en état. Les deux formules ne donnent le même $A$ que si on lit « MTBF » comme la même durée. Toujours écrire quelle durée est comptée.
- **MTTR.** IEC 61703 liste cinq durées distinctes : durée moyenne de réparation [192-07-21], de maintenance corrective active [07-22], **de remise en état** (*mean time to restoration*, [07-23]), délai administratif moyen [07-26] et délai logistique moyen [07-27]. « MTTR » peut viser l'une ou l'autre. (Un résumé de recherche de l'entrée IEV donne « mean time to repair » comme synonyme déconseillé de *mean time to restoration* ; la page Electropedia n'a pas pu être ouverte, accès refusé : non vérifié.)
- **Norme de vocabulaire de la maintenance** : EN 13306:2017 (*Maintenance. Terminologie de la maintenance*, champ d'application lu sur la page du catalogue BSI). Les définitions elles-mêmes n'ont pas été lues : cette page ne les cite pas.

### Trois disponibilités

| Disponibilité | Temps d'arrêt compté | Temps de marche |
|---|---|---|
| **Inhérente** $A_i$ | maintenance corrective seule (le MTTR) | MTBF |
| **Atteinte** $A_a$ | corrective **et** préventive | temps moyen entre maintenances (MTBM) |
| **Opérationnelle** $A_o$ | corrective, préventive, **délai logistique et délai administratif** | MTBM |

- Source : note « Availability » du NASA KSC (T. Adams, 2016) ; Wikipédia donne les mêmes trois types. L'inhérente est la seule qui se déduit des lois de panne et de réparation, donc la seule utilisable en conception ; l'opérationnelle dépend aussi des pièces de rechange et des équipes, hors du bureau d'études.
- Une GMAO mesure, dans le meilleur cas, la disponibilité **opérationnelle** : l'attente de pièce y est comprise. Comparer ce chiffre à la valeur inhérente d'une fiche constructeur compare deux grandeurs différentes.
- IEC 61703 distingue en outre la disponibilité **instantanée** [192-08-01], **moyenne** [08-05] et **asymptotique** [08-07] : à l'instant $t$, sur un intervalle, ou en régime établi. La valeur d'une fiche est presque toujours l'asymptotique.

### Loi de panne : exponentielle, Weibull, baignoire

- Le guide NIST rappelle que l'exponentielle est la **seule** loi à taux de panne constant, avec MTTF $=1/\lambda$. Le Weibull la généralise : forme $\beta<1$, taux décroissant (jeunesse), $\beta=1$ exponentielle, $\beta>1$ taux croissant (usure). Le cas $\beta>1$ est celui de [[RUL par analyse de survie]] et de [[Politique de maintenance et coût]].
- **La baignoire** (NIST) : une période de défaillances précoces à taux décroissant, une période intrinsèque à taux à peu près constant, puis l'usure. NIST dit que la plupart des systèmes passent le plus clair de leur vie dans la partie plate, et fonde là l'usage du modèle exponentiel pour estimer un MTBF.
- **La baignoire n'est pas universelle.** Nowlan et Heap (*Reliability-Centered Maintenance*, rapport AD-A066579, United Airlines, 1978) ont classé des composants en six profils d'évolution du risque. D'après un éditorial de *Tribology & Lubrication Technology* (STLE, février 2018), 89 à 92 % des défaillances relèveraient de profils sans lien avec l'âge, et la baignoire n'en serait qu'un ; le rapport lui-même n'a **pas** pu être ouvert (accès refusé), les pourcentages sont donc de seconde main.

## Les maths, simplement

- **Risque et survie** (NIST 8.1.2.3), pour une unité non réparable de durée de vie $T$ : $h(t)=\dfrac{f(t)}{R(t)}$ et $R(t)=\exp\!\Big(-\displaystyle\int_0^t h(u)\,du\Big)$, avec $R(t)=P(T>t)$ la fiabilité et $f$ la densité. Voir [[Analyse de survie]].
- **Exponentielle** : $R(t)=e^{-\lambda t}$, MTTF $=1/\lambda$. À $t=\mathrm{MTTF}$ : $R=e^{-1}\approx 36{,}8\ \%$, la médiane vaut $\ln 2/\lambda\approx 0{,}69\ \mathrm{MTTF}$. **Un MTBF de 10 000 h ne promet pas 10 000 h de service** : 63 % des unités sont déjà tombées en panne à cette date. Hypothèse : taux constant, donc aucun vieillissement.
- **Weibull** : $R(t)=\exp\!\big(-(t/\eta)^{\beta}\big)$, $h(t)=\dfrac{\beta}{\eta}\Big(\dfrac{t}{\eta}\Big)^{\beta-1}$, MTTF $=\eta\,\Gamma(1+1/\beta)$ (calcul classique, non repris d'une page lue). L'échelle $\eta$ est le quantile à 63,2 % de pannes quel que soit $\beta$ (NIST) ; le MTTF n'est égal à $\eta$ que pour $\beta=1$. Notations : NIST écrit $\alpha,\gamma$, lifelines $\lambda,\rho$ ([[RUL par analyse de survie]]).
- **Estimer un MTBF à taux constant** (NIST 8.4.5.1) : $\widehat{\mathrm{MTBF}}=T/r$ et $\hat\lambda=r/T$, avec $T$ le **temps de fonctionnement cumulé de toutes les unités** (pannées ou non) et $r$ le nombre de pannes. C'est l'estimateur du [[Maximum de vraisemblance]] avec ou sans censure ; NIST donne des bornes exactes pour une observation à durée fixée (formule non reprise ici, cf. [[Intervalles de confiance]]). Avec $r=0$, l'estimateur n'est pas défini : seule une borne inférieure existe.
- **Plusieurs machines** : le taux agrégé est $\hat\lambda=\sum_i r_i/\sum_i T_i$, **pas** la moyenne des $T_i/r_i$ : une machine sans panne ($r_i=0$) rend la seconde indéfinie, et une machine observée peu de temps pèse autant qu'une autre.
- **Modes de défaillance en série** : NIST définit un modèle à risques concurrents où une unité tombe par le premier mode qui survient. Si les modes sont indépendants à taux constants $\lambda_k$, le taux global est $\sum_k\lambda_k$ (calcul direct). Un MTBF « équipement » mélange donc des modes de nature différente ([[Surveillance conditionnelle et modes de défaillance]]).
- **Disponibilité asymptotique** : avec $\mathrm{MUT}$ la durée moyenne de marche et $\mathrm{MDT}$ la durée moyenne d'arrêt, $A_\infty=\dfrac{\mathrm{MUT}}{\mathrm{MUT}+\mathrm{MDT}}$ (résultat classique du renouvellement alterné ; IEC 61703 en traite les mesures, mean up time [08-09] et mean down time [08-10]). Cas particulier de la formule usuelle : MUT $=$ MTBF et MDT $=$ MTTR.
- **Marche et arrêt exponentiels** (taux de panne $\lambda$, taux de remise en état $\mu$) : c'est une [[Chaînes de Markov]] à deux états, d'où $A_\infty=\dfrac{\mu}{\lambda+\mu}=\dfrac{\mathrm{MTBF}}{\mathrm{MTBF}+\mathrm{MTTR}}$ et $A(t)=\dfrac{\mu}{\lambda+\mu}+\dfrac{\lambda}{\lambda+\mu}e^{-(\lambda+\mu)t}$ si la machine est en marche en $t=0$. Hypothèses : durées de marche et d'arrêt indépendantes et exponentielles, remise en état « comme neuf ». Si $\lambda\,\mathrm{MTTR}\ll1$, l'indisponibilité vaut environ $\lambda\,\mathrm{MTTR}$.
- **Système réparable** (NIST 8.1.7) : si les pannes forment un [[Processus de Poisson]] homogène, $M(t)=\lambda t$, le ROCOF est constant et égal à $\lambda$, et $1/\lambda$ est le MTBF. Si le taux dérive, le modèle en loi de puissance $m(t)=a\,b\,t^{b-1}$ (Duane, AMSAA) couvre $b>1$ (système qui se dégrade) et $b<1$ (qui s'améliore) ; $b=1$ redonne le cas homogène.

## En pratique

- **MTBF n'est pas une durée de vie.** Un MTBF élevé avec un risque croissant ($\beta>1$) est compatible avec une usure rapide passé un certain âge. Le MTBF ne fournit ni date de remplacement ni RUL.
- **Quatre décisions de définition à écrire avant de calculer**, car elles changent le résultat de plusieurs dizaines de pour cent (raisonnement, non vérifié sur un jeu réel) :
  - *Qu'est-ce qu'une panne* : perte de l'aptitude à remplir la fonction requise (formulation usuelle). Dans une GMAO, un ordre de travail « correctif » recouvre aussi un réglage, un micro-arrêt ou une intervention sans arrêt de production. La norme ISO 14224:2016 (pétrole, gaz, pétrochimie ; catalogue ISO lu, texte non lu) existe précisément pour fixer modes de défaillance, causes et durées d'arrêt dans les données de maintenance.
  - *Quelle durée d'arrêt* : début de panne ou date de la demande d'intervention ? fin de réparation ou remise en production ? L'attente de pièce est-elle comprise (cf. le tableau des disponibilités) ?
  - *Quel temps de marche* : heures calendaires, heures de fonctionnement du compteur, cycles ou pièces. Le catalogue SEMI E10 liste des moyennes par cycle (MCBF) à côté du MTBF. Le MTBF calendaire et le MTBF en heures de marche diffèrent du rapport entre les deux temps : pour une machine arrêtée la nuit et le week-end, un facteur 2 ou 3 (exemple d'illustration, pas une mesure).
  - *Quelle population* : même modèle, même régime de charge. Un taux agrégé sur des machines hétérogènes ne décrit aucune d'elles.
- **Censure.** Le dernier intervalle (depuis la dernière panne jusqu'à la fin de la fenêtre d'observation) est un temps de marche **sans panne** : il compte dans $T$. L'omettre sous-estime le MTBF. Une unité retirée avant la panne se traite de même ([[RUL par analyse de survie]], [[lifelines]]).
- **Remplacement préventif = censure possiblement informative** : retirer une pièce parce qu'elle montre des signes d'usure biaise l'estimation de sa loi de panne (point déjà posé dans [[RUL par analyse de survie]], non vérifié dans une source).
- **Peu de pannes, peu d'information.** L'incertitude relative d'un MTBF à taux constant dépend surtout du nombre de pannes $r$, non de la durée cumulée $T$ (résultat classique de l'exponentielle). Avec cinq pannes, l'intervalle est large ; donner l'intervalle, pas le point ([[Intervalles de confiance]], [[Bootstrap]], [[Maintenance prédictive avec peu de pannes]]).
- **Weibull sur un système réparable.** Ajuster un Weibull aux temps entre pannes successives suppose une remise « comme neuf » à chaque réparation, donc des durées indépendantes et de même loi. Un système qui se dégrade viole l'hypothèse ; c'est le cas du ROCOF croissant ci-dessus.
- **Moyenne contre prévision.** Un MTBF de flotte sert à dimensionner stocks et astreintes ; il ne sert pas à décider d'intervenir sur une machine précise, où la condition mesurée l'emporte ([[Surveillance conditionnelle et modes de défaillance]]).
- **Où sont les données.** Les états et horodatages viennent du terrain ([[Données industrielles]], [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]]) ; les pannes, des ordres de travail. La jointure entre les deux est le point faible : horloges non alignées, pannes saisies après coup. Contrôles de cohérence : [[Contrats de données & qualité]].

## Approches voisines & alternatives

- [[OEE et rendement global]] — l'indicateur de rendement d'une ligne ; son facteur « disponibilité » n'est pas celui-ci.
- [[Analyse de survie]] — estimer la loi de la durée de vie avec censure, sans supposer le taux constant.
- [[RUL par analyse de survie]] — le Weibull comme loi de panne, et la durée de vie restante qui en découle.
- [[lifelines]] — la bibliothèque Python pour Kaplan-Meier, Weibull et Cox.
- [[Processus de Poisson]] — le comptage de pannes à taux constant (modèle homogène du système réparable).
- [[Chaînes de Markov]] — le modèle à deux états marche / arrêt de la disponibilité.
- [[Maximum de vraisemblance]] — l'estimateur $T/r$ en est un cas.
- [[Politique de maintenance et coût]] — comment la loi de panne et le coût fixent une date de remplacement.
- [[Surveillance conditionnelle et modes de défaillance]] — décomposer par mode plutôt que par équipement.
- [[Maintenance prédictive et RUL]] — passer de la moyenne de flotte à la prévision par machine.
- [[Maintenance prédictive avec peu de pannes]] — quand les pannes observées sont trop rares pour estimer une loi.
- [[Indicateurs de santé]] — l'état d'une machine, par opposition à la moyenne d'une flotte.

## Pour aller plus loin

- NIST/SEMATECH, *e-Handbook of Statistical Methods*, chap. 8 « Assessing Product Reliability » (date de l'édition non lue sur les pages). Sections lues : 8.1.2.3 (taux de panne) https://www.itl.nist.gov/div898/handbook/apr/section1/apr123.htm ; 8.1.2.4 (baignoire) https://www.itl.nist.gov/div898/handbook/apr/section1/apr124.htm ; 8.1.2.5 (ROCOF) https://www.itl.nist.gov/div898/handbook/apr/section1/apr125.htm ; 8.1.6.1 (exponentielle) https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm ; 8.1.6.2 (Weibull) https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm ; 8.1.7.1-8.1.7.2 (HPP, loi de puissance) https://www.itl.nist.gov/div898/handbook/apr/section1/apr171.htm ; 8.4.5.1 (estimer un MTBF) https://itl.nist.gov/div898/handbook/apr/section4/apr451.htm
- IEC 61703:2016 (éd. 2.0, août 2016), *Mathematical expressions for reliability, availability, maintainability and maintenance support terms* — aperçu (champ d'application, sommaire, définitions 3.1-3.2) : https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec61703%7Bed2.0%7Db.pdf
- Adams (2016), *Availability*, note de fiabilité du NASA Kennedy Space Center (fichier 160727) : https://extapps.ksc.nasa.gov/Reliability/Documents/160727.1_Availability_What_is_it.pdf
- EN 13306:2017, *Maintenance. Maintenance terminology* (page du catalogue BSI, texte non lu) : https://knowledge.bsigroup.com/products/maintenance-maintenance-terminology
- ISO 14224:2016, *Petroleum, petrochemical and natural gas industries — Collection and exchange of reliability and maintenance data for equipment* (page du catalogue SIS, texte non lu) : https://www.sis.se/en/produkter/petroleum-and-related-technologies/equipment-for-petroleum-and-natural-gas-industries/general/iso142242016
- SEMI E10-0422, *Specification for Definition and Measurement of Equipment Reliability, Availability, and Maintainability (RAM) and Utilization* (page du catalogue SEMI, texte non lu) : https://store-us.semi.org/products/e01000-semi-e10-specification-for-definition-and-measurement-of-equipment-reliability-availability-and-maintainability-ram-and-utilization
- Wikipédia, *Availability*, pour la formule $A=\mathrm{MTTF}/\mathrm{MTBF}$ et les trois types, à titre d'orientation : https://en.wikipedia.org/wiki/Availability
