---
role: notion
nom: OEE et rendement global
alias: [OEE, TRS, TRG, TRE, TEEP, Rendement global, Overall Equipment Effectiveness, Taux de rendement synthétique, Six grandes pertes]
categorie: data/industrie
domaines: [data-eng, infra-ops]
tags: [iiot, timeseries, statistical-process-control, data-quality]
---

# OEE et rendement global

## Aperçu

- L'**OEE** (*overall equipment effectiveness*, en France **TRS**, taux de rendement synthétique) mesure la part du temps prévu pour produire qui a servi à fabriquer des pièces bonnes, à la cadence idéale. Il s'écrit comme le produit de trois facteurs : **disponibilité × performance × qualité**.
- C'est un indicateur de **rendement d'équipement**, pas de fiabilité. Son facteur « disponibilité » compte tout arrêt, quelle qu'en soit la cause (panne, changement de série, attente de matière) ; la disponibilité de [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] ne compte que l'incapacité à fonctionner. Les deux ne se comparent pas.
- Calculé depuis des **états machine** et des **compteurs de pièces**, il est un cas d'école de la donnée d'atelier : tout se joue dans les définitions du temps et dans la qualité des horodatages ([[Données industrielles]]).

## Concepts clés

### Les trois facteurs et le temps de référence

- **Disponibilité** : temps de marche divisé par temps planifié de production. **Performance** : production réelle divisée par la production qu'aurait donnée la cadence idéale pendant la marche. **Qualité** : pièces bonnes du premier coup divisées par pièces produites (*first-pass yield*).
- **Le piège du dénominateur.** « Temps planifié » n'est pas une grandeur unique. Trois lectures coexistent dans les sources : le temps total programmé (tout le temps de présence, OEE le plus bas), le temps planifié de production (pauses et arrêts programmés retirés, usage le plus courant selon un site de vendeur), le temps requis (changements de série et arrêts réglementaires retirés aussi, OEE le plus flatteur). Deux sites de vendeurs ne traitent pas les arrêts planifiés de la même façon : Vorne compte les changements de série planifiés comme des arrêts qui font baisser la disponibilité ; TeepTrak retire du temps planifié les arrêts programmés (maintenance préventive, réunion de relève) et ne retire les changements de série que dans le « temps requis ». Une valeur d'OEE ne se lit qu'avec son dénominateur.
- **Où le temps planifié est connu.** La spécification *OPC UA for Machine Tools, Part 1* (OPC Foundation) note que le temps planifié et la cadence idéale viennent d'ordinaire d'un MES ou d'un ERP, et non de la machine : l'OEE n'est pas calculable depuis la seule machine.

### Les six grandes pertes

- Attribuées à Nakajima et au TPM (*total productive maintenance*), elles rangent chaque perte sous un facteur : **disponibilité** : pannes, réglages et changements de série ; **performance** : micro-arrêts (*idling and minor stops*) et vitesse réduite ; **qualité** : rebuts de production et pertes de démarrage (rendement réduit). Source : sites de vendeurs ; le livre de Nakajima (*Introduction to TPM*, Productivity Press, 1988) n'a pas pu être ouvert, la liste est donc de seconde main. Wikipédia en donne une version simplifiée (pannes et attentes ; vitesse réduite et micro-arrêts ; rebut et reprise).
- L'intérêt est de **nommer la perte**. Une valeur d'OEE seule ne dit pas où agir ; les pertes classées en minutes le disent.

### TEEP, TRS, TRG, TRE : mêmes lettres, autres dénominateurs

- **TEEP** (*total effective equipment performance*) rapporte la même production utile aux heures **calendaires**, non aux heures planifiées (Wikipédia).
- **NF E60-182** (AFNOR, mai 2002, *Systèmes de production — indicateurs de performance — TRS, TRG, TRE*, titre lu au catalogue AFNOR) définit trois taux. D'après des pages de vendeurs, ils partagent le numérateur « temps utile » et diffèrent par le dénominateur : **TRS** sur le temps requis, **TRG** sur le temps d'ouverture de l'atelier, **TRE** sur le temps total (année entière). Le TRS correspond à l'OEE, le TRE au TEEP ; **le TRG n'est pas un synonyme d'OEE**. Le texte de la norme n'a pas été lu.
- **ISO 22400-2:2014** (*Automation systems and integration — KPIs for manufacturing operations management — Part 2: definitions and descriptions*, janvier 2014, titre lu au catalogue AFNOR) fixe formules, éléments et comportement temporel d'un ensemble de KPI choisis. D'après des pages de vendeurs, qui les attribuent à la norme, et l'annexe OPC UA citée plus haut (qui ne la nomme pas) : OEE $=$ disponibilité $\times$ **efficacité** $\times$ taux de qualité, avec disponibilité $=\mathrm{APT}/\mathrm{PBT}$, efficacité $=\mathrm{PRI}\times\mathrm{PQ}/\mathrm{APT}$ et qualité $=\mathrm{GQ}/\mathrm{PQ}$. « Efficacité » y joue le rôle de la performance de Nakajima. **Désaccord de libellé** : la spécification OPC UA lit PQ comme « *planned* quantity », les pages de vendeurs comme quantité produite ; seule la seconde lecture est cohérente avec la formule. Texte de la norme non lu.

### Ce que la critique reproche à l'OEE

- **Il mélange le jugement sur la machine et sur son environnement.** De Ron et Rooda (IEEE TSM, 2005) notent que l'OEE inclut des états indépendants de l'équipement (par exemple le manque de pièces en entrée) et lui opposent une efficacité $E$ calculée sur les seuls états dépendants de l'équipement, indépendante du taux d'utilisation. Leur version de 2006 (IJPR) ajoute que l'OEE ne rend pas bien l'effet des arrêts et des reprises.
- **Théorie et pratique divergent.** Muchiri et Pintelon (IJPR, 2008) décrivent la dérive de l'OEE vers TEEP, PEE, OFE, OPE et OAE, discutent deux applications industrielles et proposent un cadre de classement des pertes.
- **Un agrégat masque.** Un OEE à 73 % peut venir de $0{,}9\times0{,}9\times0{,}9$ comme de $1{,}0\times0{,}73\times1{,}0$ : l'action n'est pas la même.
- **L'objectif « 85 % classe mondiale ».** Le chiffre vient d'objectifs par facteur : $0{,}90\times0{,}95\times0{,}999\approx0{,}854$ (arithmétique). Sa paternité est attribuée à Nakajima par des sites de vendeurs ; source primaire non lue. Vorne précise que ces chiffres valent pour un lieu (le Japon), une époque (les années 1970) et une industrie (l'automobile), et recommande de fixer l'objectif sur sa propre progression ; Wikipédia range « 85 % » parmi les mythes. À titre de point de comparaison, Ljungberg (1998) trouve un OEE d'environ 55 % sur une vingtaine de cas, avec des pertes de **performance** dominantes. Aucun de ces chiffres ne vaut norme pour un procédé donné.

## Les maths, simplement

- **Notations.** $T_{plan}$ : temps planifié de production ; $T_{run}$ : temps de marche ; $c$ : temps de cycle idéal ; $N$ : nombre de pièces produites ; $N_g$ : nombre de pièces bonnes. Disponibilité $A=T_{run}/T_{plan}$ ; performance $P=cN/T_{run}$ ; qualité $Q=N_g/N$.
- **Le produit se simplifie** : $\mathrm{OEE}=A\,P\,Q=\dfrac{c\,N_g}{T_{plan}}$ : le temps passé à fabriquer des pièces bonnes à la cadence idéale, sur le temps planifié (le « temps utile » de la norme française). Hypothèses : un seul produit ; avec plusieurs, $cN$ devient $\sum_k c_kN_k$ (cadence $c_k$ de chaque produit) ; une pièce reprise ne compte pas comme bonne.
- **Les pertes s'additionnent, les facteurs se multiplient.** En temps : $L_A=T_{plan}-T_{run}$, $L_P=T_{run}-cN$, $L_Q=c\,(N-N_g)$, et $T_{plan}-c N_g=L_A+L_P+L_Q$, soit $\mathrm{OEE}=1-(L_A+L_P+L_Q)/T_{plan}$. Classer $L_A, L_P, L_Q$ en minutes dit ce qui coûte le plus ; les facteurs, eux, se comparent mal d'un trait à l'autre.
- **TEEP** : avec $T_{cal}$ le temps calendaire, $\mathrm{TEEP}=\mathrm{OEE}\times T_{plan}/T_{cal}=cN_g/T_{cal}$. Le rapport $T_{plan}/T_{cal}$ est un taux de charge. Comme $T_{requis}\le T_{ouverture}\le T_{total}$, on a toujours TRE $\le$ TRG $\le$ TRS pour un même numérateur.
- **Agréger plusieurs machines ou périodes** : $\mathrm{OEE}_{agr}=\sum_i c_iN_{g,i}\big/\sum_i T_{plan,i}$, un rapport de sommes, pas la moyenne des OEE. Exemple : 10 h à 50 % et 2 h à 100 % donnent $(5+2)/12\approx58\ \%$, non 75 %.
- **Comparer à la fiabilité.** Ici $A=T_{run}/T_{plan}$ compte comme perdu tout temps où la machine ne produit pas ; en fiabilité, $A=\mathrm{MTBF}/(\mathrm{MTBF}+\mathrm{MTTR})$ ne compte que l'arrêt dû à une panne ou à une maintenance. Une machine à l'arrêt faute de matière est **disponible** au sens de la fiabilité (la définition IEC de la disponibilité vise l'aptitude à fonctionner, d'après un résumé de recherche de l'entrée IEV non ouverte) et **perd** de l'OEE.

## En pratique

- **Calculer depuis les états et les compteurs.**
  1. *Le temps de référence* : le calendrier des équipes et les arrêts programmés (MES ou ERP) donnent $T_{plan}$, fenêtre par fenêtre.
  2. *Les états* : la séquence des états machine (marche, arrêt, réglage, attente, arrêt programmé, hors tension) avec début et fin. Le modèle SEMI E10 (semi-conducteurs ; titre et métriques lus au catalogue SEMI, texte non lu) sépare six états : temps non planifié, arrêt non programmé, arrêt programmé, ingénierie, attente (*standby*) et productif (d'après des résumés de recherche). Un tel découpage sert de modèle de correspondance.
  3. *Les compteurs* : pièces produites et rebuts, cumulés par l'automate. Les pièces bonnes sont la différence, avec le délai propre au contrôle qualité (un rebut peut être connu après coup).
  4. *La cadence idéale* par référence produit, tenue à jour dans le MES.
  5. *Le calcul* : durées des états par fenêtre ($T_{run}$), incrément du compteur par fenêtre ($N$), puis agrégation par rapport de sommes.
- **Les pièges de la donnée** (raisonnement, non vérifié sur un site) : compteur remis à zéro au redémarrage de l'automate ou qui boucle ; états qui ne s'enchaînent pas (deux « marche » consécutifs, trou entre deux états) ; changement de référence au milieu d'une fenêtre ; horloges non alignées entre automate et collecteur. L'horodatage à la source (OPC UA, Sparkplug) est décrit dans [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] ; sans lui, l'horodatage est celui du collecteur.
- **Micro-arrêts.** Une machine en état « marche » qui bégaie ne déclenche aucun arrêt : la perte tombe dans la performance. Vorne ne suit que les arrêts assez longs pour mériter une raison ; le seuil est une convention à écrire.
- **Une performance au-dessus de 100 %** signale une cadence idéale trop basse ou un compteur faux, pas une machine exceptionnelle. Un vendeur (TeepTrak) note qu'une cadence « réelle soutenable » prise comme référence masque les pertes de vitesse. Test de cohérence à automatiser : [[Contrats de données & qualité]].
- **Ne pas comparer l'OEE de machines différentes** sans mêmes définitions, même mix produit et même rôle dans la ligne. Il sert à suivre **une** machine ou **une** ligne dans le temps. Wikipédia ajoute qu'il ne mesure pas la performance des opérateurs.
- **Lire la série, pas le point.** Un OEE quotidien oscille ; distinguer bruit et changement relève de [[Contrôle statistique de procédé (SPC)]] (recommandation, non issue d'une source lue) et de [[Détection de ruptures]]. Des travaux récents traitent la prévision à court terme de l'OEE (Anapa, Güzel, Yozgatlıgil, arXiv 2025, contenu non évalué ici).
- **Chaîne d'outils du dossier** : collecte par [[Telegraf]] ou [[Node-RED]], stockage dans [[InfluxDB]] ou [[TimescaleDB]] ([[Séries temporelles]]), durées d'état par fenêtres sur les événements de changement d'état, affichage par [[Grafana]].
- **Lien avec la maintenance** : la part de $L_A$ due aux pannes se lit avec les indicateurs de [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] ; les décisions d'intervention relèvent de [[Politique de maintenance et coût]] et de [[Maintenance prédictive et RUL]].

## Approches voisines & alternatives

- [[Indicateurs de fiabilité (MTBF, MTTR, disponibilité)]] — la disponibilité au sens de la fiabilité, et pourquoi elle diffère du facteur de l'OEE.
- [[Politique de maintenance et coût]] — décider quand intervenir, une fois les pertes de disponibilité chiffrées.
- [[Maintenance prédictive et RUL]] — réduire la part des pannes dans la perte de disponibilité.
- [[Surveillance conditionnelle et modes de défaillance]] — les modes de défaillance derrière « pannes » dans les six pertes.
- [[Contrôle statistique de procédé (SPC)]] — surveiller la stabilité d'un indicateur contre ses limites naturelles ; côté qualité, la maîtrise du procédé agit sur le facteur $Q$.
- [[Détection de ruptures]] — repérer un changement de niveau de l'OEE.
- [[Données industrielles]] et [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — d'où viennent états, compteurs et horodatages.
- [[Contrats de données & qualité]] — contrôler la cohérence des états et des compteurs.

## Pour aller plus loin

- De Ron, Rooda (2005), *Equipment Effectiveness: OEE Revisited*, IEEE Transactions on Semiconductor Manufacturing 18(1):190-196. DOI : https://doi.org/10.1109/TSM.2004.836657 (métadonnées et résumé lus)
- De Ron, Rooda (2006), *OEE and equipment effectiveness: an evaluation*, International Journal of Production Research 44(23):4987-5003. DOI : https://doi.org/10.1080/00207540600573402 (métadonnées et résumé lus)
- Muchiri, Pintelon (2008), *Performance measurement using overall equipment effectiveness (OEE): literature review and practical application discussion*, International Journal of Production Research 46(13):3517-3535. DOI : https://doi.org/10.1080/00207540601142645 (métadonnées et résumé lus)
- Ljungberg (1998), *Measurement of overall equipment effectiveness as a basis for TPM activities*, International Journal of Operations & Production Management 18(5):495-507. DOI : https://doi.org/10.1108/01443579810206334 (métadonnées et résumé lus)
- Nakajima (1988), *Introduction to TPM: Total Productive Maintenance*, Productivity Press, ISBN 0915299232 (notice bibliographique lue, livre non ouvert).
- OPC Foundation, *OPC UA for Machine Tools — Part 1: Machine Monitoring and Job Management*, annexe C.2.4 « Calculation of the OEE » : https://reference.opcfoundation.org/MachineTool/v101/docs/C.2.4
- AFNOR, *NF E60-182* (mai 2002), notice du catalogue : https://www.boutique.afnor.org/en-gb/standard/nf-e60182/manufacturing-systems-performance-indications-overall-equipment-effectivene/fa120534/513
- AFNOR, *ISO 22400-2:2014*, notice du catalogue : https://www.boutique.afnor.org/en-gb/standard/iso-2240022014/automation-systems-and-integration-key-performance-indicators-kpis-for-manu/xs123365/120048
- Vorne, *Calculating OEE* (https://www.oee.com/calculating-oee/) et *World-Class OEE* (https://www.oee.com/world-class-oee/) : pages d'un éditeur de logiciel d'OEE, à lire comme source de vendeur.
- Anapa, Güzel, Yozgatlıgil (2025), *Robust Short-Term OEE Forecasting in Industry 4.0 via Topological Data Analysis*, arXiv:2507.02890 : https://arxiv.org/abs/2507.02890
- Wikipédia, *Overall equipment effectiveness*, pour s'orienter : https://en.wikipedia.org/wiki/Overall_equipment_effectiveness
