---
role: brique
nom: Jeux de données PHM
alias: [Datasets PHM, Benchmarks de maintenance prédictive, Jeux de données de pronostic]
pitch: "Annuaire commenté de huit jeux de référence pour la maintenance prédictive — turboréacteurs simulés (C-MAPSS), roulements (CWRU, PRONOSTIA/FEMTO, IMS, XJTU-SY, Paderborn), batteries (NASA PCoE) et sons de machines (MIMII) — avec, pour chacun, la licence des données, le mode d'accès et ce qu'elle permet en usage commercial. Rien à installer ; un seul jeu interdit l'usage commercial par une licence écrite, mais la plupart n'en portent aucune."
categorie: ml/maintenance
famille: annuaire
domaines: [data-sci, mlops]
licence_type: 
os: 
langage: 
alternatives: []
complements: []
tags: [benchmark, predictive-maintenance, rul]
url_docs: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
url_repo: 
---

# Jeux de données PHM

<!-- AUTO:BANDEAU:START -->
> Annuaire commenté de huit jeux de référence pour la maintenance prédictive — turboréacteurs simulés (C-MAPSS), roulements (CWRU, PRONOSTIA/FEMTO, IMS, XJTU-SY, Paderborn), batteries (NASA PCoE) et sons de machines (MIMII) — avec, pour chacun, la licence des données, le mode d'accès et ce qu'elle permet en usage commercial. Rien à installer ; un seul jeu interdit l'usage commercial par une licence écrite, mais la plupart n'en portent aucune.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Annuaire | — | rien à exécuter | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Nature de cette page, à lire en premier** : ce n'est ni un logiciel ni un service, mais un annuaire de jeux de données. Rien ne s'installe, il n'y a pas de version à suivre, et les huit entrées n'ont **pas de licence commune** : la rubrique « licence » de la fiche, vide, dit précisément cela. Chaque jeu se lit avec sa propre licence, relevée à la source le 2026-10-02. « PHM » vient de *Prognostics and Health Management*, le nom de la communauté et de la conférence qui ont lancé plusieurs de ces jeux.

Ce qu'ils servent à faire : comparer des méthodes de pronostic (durée de vie résiduelle, cf. [[Maintenance prédictive et RUL]]) ou de diagnostic de défauts sur un terrain commun. Ce qu'ils ne servent **pas** à faire : prouver qu'un modèle tiendra sur les machines d'une usine. Quatre avertissements de fond :

- **C-MAPSS est une simulation.** Son article décrit la méthode : des surfaces de réponse de tous les capteurs sont générées par un modèle thermodynamique du moteur, une perte de débit et d'efficacité à taux exponentiel est imposée à partir d'un point de dégradation initial tiré au hasard, et la panne est atteinte quand un indice de santé (le minimum de plusieurs marges de fonctionnement) tombe à zéro. La loi de dégradation est donc celle du générateur, pas celle d'un parc réel : un bon score mesure en partie la capacité à retrouver la loi qui a produit les données. Les auteurs de N-CMAPSS, qui relient la dégradation à l'historique d'usage et utilisent des vols réels enregistrés, justifient leur jeu par le fait que « les grands jeux représentatifs de pannes jusqu'à la rupture manquent souvent dans les applications réelles » ; il reste un jeu simulé.
- **Les défauts de CWRU sont posés à la main.** Les défauts de la bague intérieure, des billes et de la bague extérieure sont introduits par électroérosion (diamètres de 0,007 à 0,040 pouce) sur un moteur dont la vitesse ne varie que de 1720 à 1797 tr/min. Smith et Randall notent dans leur étude que, malgré son statut de référence, le jeu n'avait aucun étalon reconnu pour juger les méthodes, d'où la nécessité de l'examiner de près et de le catégoriser. Paderborn sépare les deux familles (12 roulements à dommage artificiel, 14 à dommage réel issu d'essais de vie accélérés), et Lessmeier et al. observent qu'un entraînement sur dommages artificiels ou sur dommages réels donne des exactitudes différentes.
- **Les effectifs de FEMTO sont minuscules.** Le défi PHM 2012 fournit 6 roulements pour l'apprentissage et demande la RUL de 11 autres, dont les mesures sont tronquées ; les auteurs écrivent que l'ensemble d'apprentissage est « assez petit » alors que les durées de vie s'étalent de 1 h à 7 h. Ils ajoutent que les signatures de fréquence théoriques ne marchent pas sur ces données. Avec 11 roulements de test, l'écart de score entre deux méthodes tient à quelques roulements (conséquence arithmétique, pas un chiffre des auteurs).
- **Le biais de partitionnement fausse les scores.** Hendriks et al. (2022) ont montré que le découpage usuel de CWRU souffre d'une fuite de données ; c'est Rosa et al. (2024) qui le rappellent, en citant aussi Abburi et al. (2023), et ils parlent de résultats « trop optimistes ». Knap et al. (2026), sur CWRU et Paderborn, relient ce gonflement à un découpage au niveau de la **fenêtre** plutôt qu'au niveau de l'**enregistrement** et imposent une séparation par enregistrement. Un score de diagnostic publié sur ces jeux se lit en demandant comment les fenêtres ont été réparties.

| Jeu | Modalité · contenu · taille | Licence des données | Usage commercial | Accès |
|---|---|---|---|---|
| **C-MAPSS** (NASA, Saxena et al., PHM 2008) | Turboréacteurs **simulés** ; quatre sous-jeux FD001 à FD004 (un ou six régimes, un ou deux modes de panne), 100, 260, 100 et 249 trajectoires d'apprentissage (comptées dans les fichiers), 26 colonnes (3 réglages, capteurs bruités) ; archive de 12,4 Mo | **Non écrite** : la fiche data.nasa.gov dit « licence non spécifiée », accès public ; citation demandée par le dépôt PCoE, utilisation « à ses propres risques » | Non établi | Téléchargement direct (NASA open data ou dépôt PCoE), sans formulaire |
| **PRONOSTIA / FEMTO** (FEMTO-ST, défi IEEE PHM 2012) | Roulements en vieillissement accéléré ; 17 roulements en trois régimes (1800 tr/min 4000 N, 1650 tr/min 4200 N, 1500 tr/min 5000 N) : 6 d'apprentissage, 11 de test ; vibration 25,6 kHz, température 10 Hz ; taille non relevée | **Non écrite** (le miroir GitHub le dit expressément ; citation de l'article PRONOSTIA demandée) | Non établi | Miroir GitHub tiers et dépôt PCoE (jeu n° 10) ; le site d'origine femto-st.fr répond 404 (non ouvert, 2026-10-02) |
| **CWRU** (Case Western Reserve University) | Roulements sains et défauts posés par électroérosion ; moteur 2 ch, 0 à 3 ch, 1720 à 1797 tr/min ; accéléromètres côté entraînement, côté ventilateur et base ; fichiers Matlab à 12 kHz et 48 kHz ; taille non relevée | **Non écrite** : ni licence, ni conditions, ni citation sur la page | Non établi | Page web, liens de téléchargement directs, aucun compte mentionné |
| **IMS** (NASA / Université de Cincinnati, Lee et al., 2007) | Roulements en essai jusqu'à la rupture, dégradation naturelle ; archive PCoE de 1,08 Go | Le catalogue data.gov porte « U.S. Government Works », domaine public ; la page PCoE exige une citation et décline toute responsabilité | Permis d'après le catalogue ; à rapprocher de la mention PCoE, que le texte ne tranche pas | Téléchargement direct (dépôt PCoE) ; le lien data.nasa.gov/docs/legacy/IMS.zip n'a pas répondu en 15 s le 2026-10-02 (non vérifié) |
| **XJTU-SY** (Xi'an Jiaotong et Sumyoung, Wang et al., 2020) | 15 roulements menés jusqu'à la rupture, 5 par régime (2100 tr/min 12 kN, 2250 tr/min 11 kN, 2400 tr/min 10 kN) ; deux accéléromètres à 25,6 kHz, 32 768 points (1,28 s) enregistrés chaque minute ; CSV ; taille non relevée | **Non écrite** : la page dit que les jeux sont publics et que chacun peut s'en servir pour valider des algorithmes de pronostic ; citation de Wang et al. demandée | Non établi | Six miroirs (site personnel, Google Drive, Dropbox, MediaFire, MEGA, Baidu) |
| **Batteries NASA** (PCoE, Saha et Goebel, 2007) | Piles Li-ion 18650 cyclées en charge, décharge et impédance à températures variées, jusqu'à 30 % de perte de capacité (2 Ah à 1,4 Ah) ; archive PCoE de 210 Mo (description tirée de la page DASHlink, correspondance avec l'archive non vérifiée) ; le nombre de piles n'est pas écrit sur les pages ouvertes | **Non écrite** : « N/A » sur la page DASHlink, aucune licence dans le catalogue, accès public | Non établi | Téléchargement direct (dépôt PCoE, jeu n° 5) |
| **Paderborn** (KAt-DataCenter, Lessmeier et al., PHME 2016) | 32 roulements 6203 : 6 sains, 12 à dommage artificiel, 14 à dommage réel (essais de vie accélérés) ; courant moteur et vibration, quatre conditions de fonctionnement ; fichiers `.mat` ; taille non relevée | **CC BY-NC 4.0** | **Non** ; usage commercial sur demande à l'auteur | Téléchargement depuis le site de la chaire, sans formulaire relevé |
| **MIMII** (Hitachi, Purohit et al., 2019) | **Sons** de quatre machines (vannes, pompes, ventilateurs, glissières), quatre modèles chacune, de 5 000 à 10 000 s de son normal par modèle et environ 1 000 s de son anormal ; réseau de 8 microphones à 16 kHz, bruit d'usine à −6, 0 et 6 dB ; 12 archives, 100,2 Go | **CC BY-SA 4.0** | **Permis**, avec attribution et partage à l'identique | Libre sur Zenodo |

Quatre jeux appellent une lecture plus fine :

- **MIMII et DCASE 2020** : le jeu de développement de la tâche 2 de DCASE 2020 reprend une partie de MIMII mais sous **CC BY-NC-SA 4.0**. La même matière sonore change donc de licence selon la porte par laquelle elle entre ; seule la version Zenodo de MIMII est ouverte à l'usage commercial. MIMII sert à la **détection d'anomalies sonores** (cf. [[Jeux de données d'anomalies]]), pas au pronostic.
- **IMS** : deux textes de NASA se côtoient, le catalogue (domaine public) et la page du dépôt (citation exigée, aucune garantie). Ils ne se contredisent pas formellement ; aucun ne dit si les données données par l'université restent soumises à des conditions propres.
- **C-MAPSS** : le fichier `readme.txt` de l'archive annonce 248 trajectoires d'apprentissage et 249 de test pour FD004 ; les fichiers contiennent l'inverse (249 d'apprentissage, 248 de test), comptées le 2026-10-02. Les trois autres sous-jeux concordent. Le dépôt PCoE liste aussi le défi PHM08 (RUL de test cachée) et « Turbofan Engine Degradation-2 », le jeu N-CMAPSS aux conditions de vol réalistes.
- **FEMTO** : l'hébergeur d'origine est introuvable, le jeu circule par un miroir GitHub tiers et par le dépôt PCoE. Rien ne garantit l'intégrité de la copie : comparer avec l'archive PCoE avant de publier.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer une méthode de RUL à la littérature : C-MAPSS pour la flotte, FEMTO et XJTU-SY pour les roulements en dégradation naturelle accélérée | Valider un modèle de RUL pour un parc réel : C-MAPSS est une simulation, FEMTO tient en 17 roulements |
| Évaluer un diagnostic de défauts de roulements en classification : CWRU, Paderborn (voir [[Diagnostic de défauts de roulements]]) | Annoncer un score CWRU sans avoir séparé les enregistrements entre apprentissage et test : fuite de données |
| Étudier une dégradation sur un composant naturel jusqu'à la rupture : IMS, XJTU-SY | Livrer un produit entraîné sur Paderborn à un client : licence non commerciale |
| Étudier le vieillissement d'une batterie : le jeu NASA, en sachant que le nombre de piles est à relever dans l'archive | Compter sur une licence qui n'est pas écrite : C-MAPSS, FEMTO, CWRU, XJTU-SY et les batteries n'en portent pas |
| Tester une détection d'anomalies sonores, avec une licence qui permet l'usage commercial : MIMII (version Zenodo) | Mesurer un pronostic sur MIMII ou sur CWRU : ni l'un ni l'autre ne porte de trajectoire jusqu'à la panne |

## Mise en œuvre

- Installation — aucune ; chaque jeu se télécharge depuis sa page (liens ci-dessous)
- Point d'entrée — le tableau de la section *Définition*
- Prérequis — aucun compte ni formulaire relevé pour les huit jeux ; MIMII demande de la place disque
- Exécution — rien à exécuter ; archives mesurées par requête HTTP le 2026-10-02 : C-MAPSS 12,4 Mo, batteries 210 Mo, roulements IMS 1,08 Go, MIMII 100,2 Go (CWRU, FEMTO, XJTU-SY et Paderborn : non relevé)
- Coût — gratuit à l'accès ; le coût est dans la licence (usage commercial interdit pour un jeu, permis pour un ou deux, non établi pour la plupart)

## Écosystème

### Alternatives

<!-- Aucune : un annuaire de jeux n'a pas d'équivalent fiché dans le brain. -->

## Ressources

- Documentation — dépôt PCoE de la NASA (C-MAPSS, IMS, batteries, FEMTO, 21 jeux) : https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
- Données — C-MAPSS : https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data
- Papier — C-MAPSS, Saxena et al. (PHM 2008) : https://ntrs.nasa.gov/citations/20090029214
- Papier — N-CMAPSS, Arias Chao et al. (Data, 2021) : https://ntrs.nasa.gov/citations/20210020068
- Dépôt — PRONOSTIA/FEMTO (miroir tiers) : https://github.com/wkzs111/phm-ieee-2012-data-challenge-dataset
- Papier — PRONOSTIA, Nectoux et al. (2012) : https://hal.science/hal-00719503
- Documentation — CWRU : https://engineering.case.edu/bearingdatacenter (fichiers : https://engineering.case.edu/bearingdatacenter/download-data-file)
- Papier — Smith et Randall, étude de référence sur CWRU (MSSP, 2015) : https://doi.org/10.1016/j.ymssp.2015.04.021
- Données — IMS : https://catalog.data.gov/dataset/ims-bearings
- Documentation — XJTU-SY : https://biaowang.tech/xjtu-sy-bearing-datasets/
- Données — batteries NASA : https://catalog.data.gov/dataset/li-ion-battery-aging-datasets (description : https://c3.ndc.nasa.gov/dashlink/resources/133/)
- Documentation — Paderborn : https://mb.uni-paderborn.de/kat/forschung/bearing-datacenter/
- Papier — Lessmeier et al., Paderborn (PHME 2016) : https://papers.phmsociety.org/index.php/phme/article/view/1577
- Données — MIMII : https://zenodo.org/records/3384388 (article : https://arxiv.org/abs/1909.09347)
- Données — DCASE 2020 tâche 2, développement (reprend MIMII) : https://zenodo.org/records/3678171
- Papier — Hendriks et al., fuite de données sur CWRU (MSSP, 2022) : https://doi.org/10.1016/j.ymssp.2021.108732 (page d'éditeur non lue ; énoncé repris du résumé de Rosa et al.)
- Papier — Rosa et al., CWRU en multi-étiquettes (2024) : https://arxiv.org/abs/2407.14625
- Papier — Knap et al., évaluation sans fuite sur CWRU et Paderborn (PHME, 2026) : https://papers.phmsociety.org/index.php/phme/article/view/4924

## Voir aussi

- [[Maintenance prédictive]] — le hub du domaine
- [[Maintenance prédictive et RUL]] — la notion : ce que ces jeux servent à mesurer
- [[Diagnostic de défauts de roulements]] — le diagnostic sur CWRU et Paderborn, et le piège du partitionnement
- [[RUL par apprentissage profond]] — les modèles que l'on entraîne sur C-MAPSS, FEMTO et XJTU-SY
- [[Jeux de données d'anomalies]] — l'annuaire voisin, côté détection (MIMII y a sa place de voisin)
- [[Évaluer une détection d'anomalies]] — les métriques à employer sur MIMII, et leurs biais
