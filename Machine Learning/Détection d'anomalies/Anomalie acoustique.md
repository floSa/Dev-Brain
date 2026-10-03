---
role: notion
nom: Anomalie acoustique
alias: [Anomalous sound detection, ASD, détection d'anomalie sonore, anomalie audio, DCASE, DCASE tâche 2, son anormal de machine]
categorie: ml/anomalie
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection, unsupervised, signal-processing, spectrogram, audio-classification, self-supervised, condition-monitoring]
---

# Anomalie acoustique

## Aperçu

- Décider qu'une machine (pompe, ventilateur, convoyeur, vanne) sonne anormalement, à partir d'un microphone et **sans exemple d'anomalie à l'entraînement**. Le jargon anglais est *anomalous sound detection* (ASD). L'entrée est un extrait audio de quelques secondes, la sortie un score d'anomalie, puis une décision par seuil. Le régime est celui de [[Types d'anomalies et régimes de supervision]] : du normal seulement.
- Le banc d'essai de fait est la **tâche 2 du défi DCASE**, reconduite chaque année depuis 2020 avec un protocole qui change : changement de domaine (2021), domaine caché (2022), machines jamais vues (*first-shot*, 2023 à 2025), bruit et deux microphones (2026). Les scores d'une édition ne se comparent pas à ceux d'une autre.

## Concepts clés

### Le problème

- Un score $A_\theta(x)$ grand quand l'extrait $x$ paraît anormal ; décision « anomalie » si $A_\theta(x)>\varphi$ (Koizumi et al., 2020). La difficulté posée par les auteurs : comment détecter des anomalies sans exemple d'anomalie ?
- **Les anomalies des jeux sont provoquées.** MIMII liste contamination, fuite, balourd et dommage de glissière ; ToyADMOS endommage volontairement des machines miniatures. Un score sur ces jeux ne dit rien sur la rareté ni sur la variété des défauts réels.

### Les jeux

- **ToyADMOS** (Koizumi et al., WASPAA 2019) : machines miniatures, trois sous-jeux de plus de 180 h de son normal chacun, plus de 4 000 sons anormaux, 4 microphones, 48 kHz.
- **MIMII** (Purohit et al., 2019, Hitachi) : vannes, pompes, ventilateurs, glissières ; 8 microphones, 16 kHz ; bruit d'usine à −6, 0 et 6 dB ; 5 000 à 10 000 s de son normal par modèle et environ 1 000 s d'anormal ; CC BY-SA 4.0. **MIMII DUE** (Tanabe et al., 2021) : cinq types de machines dans deux contextes, pour étudier le changement de domaine. **ToyADMOS2** (Harada et al., 2021) : plus de 27 000 sons normaux et 8 000 anormaux, avec modèles, vitesses et microphones variés.
- Licences : le jeu de développement de DCASE 2020 reprend MIMII sous CC BY-NC-SA 4.0 ([[Jeux de données PHM]]). Annuaire voisin côté détection : [[Jeux de données d'anomalies]].

### Les éditions de la tâche 2

- **2020** : première édition formelle, ToyADMOS et MIMII (toy-car, toy-conveyor, ventilateur, pompe, glissière, vanne), 117 soumissions de 40 équipes. Le classement moyenne les rangs par type de machine, d'où la pénalité d'une équipe faible sur un seul type. Le système de référence, un autoencodeur, finit 33e.
- **2021** : *domain shift* sur MIMII DUE, 75 soumissions de 26 équipes. Définition de Kawaguchi et al. : les caractéristiques acoustiques de l'apprentissage et du test diffèrent (environnement, variantes de produit, saison). Deux stratégies gagnantes : ensembles mêlant exposition aux valeurs aberrantes et modélisation du normal ; modélisation du normal sur des descripteurs issus d'une tâche d'identification de machine.
- **2022** : généralisation de domaine, 81 soumissions. L'étiquette de domaine disparaît au test et un **seuil unique** doit servir tous les domaines (Dohi et al.). Stratégies dominantes : mélange de domaines, classification de domaine.
- **2023** : *first-shot*, 86 soumissions de 23 équipes. Un seul sous-ensemble (section) par type de machine, et des types **différents** entre développement et évaluation, sans réglage d'hyperparamètres propre à la machine. Facteurs de succès cités : rééchantillonnage contre le déséquilibre entre domaines, échantillons synthétiques, plusieurs modèles pré-entraînés pour les plongements.
- **2024** : nouveaux types de machines en entraînement supplémentaire ; l'information d'attribut (vitesse, modèle, bruit) est **cachée** pour certains types. Modèles pré-entraînés autorisés (VGGish, PANNs, OpenL3, BEATs) et AudioSet ; les jeux des éditions précédentes sont interdits. L'article de description lu ne contient pas encore l'analyse des résultats.
- **2025** : données **supplémentaires** facultatives (machine seule, bruit seul), 119 soumissions de 35 équipes. Constat de Nishida et al. : affiner un modèle pré-entraîné, geler un réseau pré-entraîné avec normalisation des scores, ou entraîner un petit modèle à partir de zéro peuvent tous être compétitifs. Un AUC élevé en développement ne garantit pas un AUC élevé en évaluation.
- **2026** : *noise-aware*. Deux voies d'enregistrement, l'une près de la machine, l'autre plus loin ; cinq types sont des enregistrements à deux voies **émulés** par convolution de réponses impulsionnelles. 51 équipes, 168 soumissions ; l'équipe MERL se classe première avec un apprentissage auto-supervisé conscient du bruit (NA-SSL). Son rapport donne 66,20 % de score officiel dans le résumé et 70,24 % dans la page de classement : écart non élucidé.

### Les approches

- **Autoencodeur sur log-mel** : référence des éditions. Spectrogramme log-mel de 128 filtres, 5 trames concaténées (640 dimensions), score = erreur de reconstruction ; une variante utilise une distance de Mahalanobis choisie entre les domaines (description 2024). Voir [[Autoencodeurs]], [[STFT et spectrogramme]], [[librosa]].
- **Classification auto-supervisée** : le réseau apprend à reconnaître l'identifiant de la machine, les autres identifiants jouant le rôle d'anomalies (Koizumi et al., 2020). Giri et al. (DCASE 2020 *workshop*) y ajoutent MobileNetV2 ou ResNet-50, une perte à marge angulaire, des mélanges et déformations de spectrogrammes, et un ensemble avec un autoencodeur masqué ; équipe gagnante. Limite relevée : si les identifiants sonnent presque pareil, la frontière est difficile et les fausses alertes montent (toy-conveyor). Wilkinghoff (ICASSP 2024) retire le besoin de métadonnées avec *Feature Exchange* et annonce l'état de l'art sur DCASE 2023.
- **Densité par flux normalisants** : Dohi et al. (ICASSP 2021) notent que la vraisemblance exacte peut échouer en détection hors distribution, parce qu'elle dépend de la régularité des données ; ils entraînent le flux à donner une vraisemblance plus basse aux machines du même type, et gagnent 4,6 % d'AUC (MAF) et 5,8 % (Glow) sur DCASE 2020. Voir [[Détection hors distribution (OOD)]].
- **Plus proche voisin sur plongements pré-entraînés** : GenRep (Saengthong, Shinozaki, 2024), sans réglage fin ni étiquette de cible, avec une banque mémoire enrichie (*MemMixup*) et une normalisation par domaine ; score officiel de 73,79 % sur l'évaluation DCASE 2023, au-dessus de la meilleure approche à exposition aux aberrants. Voir [[k-NN]].
- **Exposition aux aberrants** : traiter les sons des autres machines comme une classe anormale (Primus, cité par Koizumi et al.).

## Les maths, simplement

- **AUC** : $\mathrm{AUC}=\dfrac{1}{N^-N^+}\sum_{i=1}^{N^-}\sum_{j=1}^{N^+}H\big(A_\theta(x_j^+)-A_\theta(x_i^-)\big)$, $N^-$ extraits normaux, $N^+$ anormaux de test, $H$ la fonction marche. C'est la probabilité qu'une anomalie reçoive un score plus haut qu'un normal, hors égalités.
- **pAUC** : $\mathrm{pAUC}=\dfrac{1}{\lfloor pN^-\rfloor N^+}\sum_{i=1}^{\lfloor pN^-\rfloor}\sum_{j=1}^{N^+}H\big(A_\theta(x_j^+)-A_\theta(x_i^-)\big)$ avec $p=0{,}1$ et les normaux triés par score décroissant : seuls les 10 % de normaux les plus suspects comptent, c'est-à-dire un taux de fausses alertes d'au plus 0,1. Motif des auteurs : un système qui alerte trop n'est plus cru ; il faut un bon taux de détection à faible taux de fausses alertes.
- **Score officiel** : moyenne **harmonique** de tous les AUC et pAUC, sur types de machines, sections et domaines. Hypothèse : chaque terme est positif. La moyenne harmonique est dominée par les petites valeurs : une machine proche de 0,5 tire tout le score vers le bas, d'où l'intérêt d'être correct partout.
- **Reconstruction** : $A_\theta(x)=\dfrac1D\sum_{d=1}^{D}(x_d-\hat x_d)^2$, $D$ la dimension de l'entrée, $\hat x$ la sortie de l'autoencodeur. Variante : $(x-\hat x)^{\top}\Sigma^{-1}(x-\hat x)$, $\Sigma$ une covariance estimée à la fin de l'entraînement.
- **Seuil du système de référence** (2026) : loi gamma ajustée sur les scores d'apprentissage, seuil au 90e centile. Aucune garantie de taux de fausses alertes en exploitation : c'est une règle de départ.
- **Changement de domaine** : $p_{\text{test}}(x)\neq p_{\text{train}}(x)$. En 2024-2026, chaque section du développement compte 990 extraits normaux du domaine source pour 10 du domaine cible : le cas visé est celui où le domaine cible est presque absent.

## En pratique

- **Bruit d'usine.** MIMII mélange le bruit à −6, 0 et 6 dB ; la tâche 2026 ajoute une voie « bruit ». Jombo et Zhang (2023) notent que le signal acoustique est sensible au bruit de fond et aux changements de régime de la machine. Fixer le microphone et noter sa position et sa référence : un déplacement ou un changement de modèle peut jouer comme un changement de domaine (la page de la tâche 2024 cite vitesse, charge, bruit et position du microphone parmi les causes).
- **Seuil par machine.** Les scores ne sont pas comparables d'une machine à l'autre, et l'AUC ne dit rien du seuil. Le défi demande des décisions binaires, mais classe sur AUC et pAUC. En usine : un seuil par machine, calé sur un échantillon normal propre, puis revu ([[Score et seuil d'alerte]]).
- **Valider sans anomalies réelles.** Les anomalies des jeux sont posées ; en site, elles manquent. Prévoir des défauts provoqués ou rejoués, et lire [[Évaluer une détection d'anomalies]] sur les biais des métriques.
- **Dev n'est pas éval.** Les éditions 2023 à 2025 changent les types de machines entre développement et évaluation, et l'analyse 2025 souligne l'écart. Une architecture réglée sur les sept types de développement ne garantit rien sur une machine nouvelle.
- **Données d'entraînement propres.** Le normal doit l'être réellement : machine en régime, sans autre machine dominante. Les enregistrements « machine seule » et « bruit seul » de 2025 vont dans ce sens ; ils servent en augmentation, en classifieurs auxiliaires, en apprentissage contrastif ou en débruitage.
- **Fuite.** Découper par enregistrement et par machine, jamais par fenêtre d'un même enregistrement ([[Data leakage]]) : deux fenêtres voisines sont presque identiques.
- **Licences.** MIMII est en CC BY-SA 4.0, mais la copie de DCASE 2020 est non commerciale ; DCASE 2026 interdit de réutiliser les jeux de la tâche 2 des éditions 2020 à 2025 dans le défi.
- **Acoustique et vibration.** Un microphone ne touche pas la machine, s'installe vite et à bas coût (Jombo et Zhang) ; un accéléromètre est collé à la machine, plus robuste au bruit, mais demande plus de points de mesure. Sur des roulements, Tandon et Nakra (1992) trouvent que l'émission acoustique (haute fréquence, par contact) et l'enveloppe d'accélération détectent mieux les défauts que la pression acoustique audible. Le micro seul est donc un capteur de premier niveau, non un substitut. Voir [[Analyse vibratoire]] et [[Diagnostic de défauts de roulements]].

## Approches voisines & alternatives

- [[Types d'anomalies et régimes de supervision]] — pourquoi « du normal seulement » est le régime par défaut.
- [[Score et seuil d'alerte]] — transformer le score en décision.
- [[Évaluer une détection d'anomalies]] — métriques et biais, dont les mesures à faible taux de fausses alertes.
- [[Analyse vibratoire]] — le capteur de contact, ses descripteurs et ses limites.
- [[Détection hors distribution (OOD)]] — le cadre général de l'écart au normal, avec ses pièges de vraisemblance.
- [[Anomalies multivariées par apprentissage profond]] — les mêmes familles de modèles sur des séries de capteurs.
- [[Autoencodeurs]] — le modèle de référence des éditions.
- [[STFT et spectrogramme]] — l'entrée de presque tous les systèmes, en échelle log-mel.
- [[librosa]] — extraction de spectrogrammes en Python.
- [[Adaptation de domaine]] — passer d'une machine, d'un site ou d'un micro à l'autre.
- [[Jeux de données PHM]] et [[Jeux de données d'anomalies]] — où trouver MIMII, et sous quelle licence.
- [[Surveillance conditionnelle et modes de défaillance]] — où l'acoustique se place dans la détection précoce.
- [[Détection d'anomalies]] — le dossier.

## Pour aller plus loin

- Koizumi et al. (2020), *Description and discussion on DCASE2020 challenge task2: unsupervised anomalous sound detection for machine condition monitoring*, arXiv : https://arxiv.org/abs/2006.05822
- Kawaguchi et al. (2021), *Description and discussion on DCASE 2021 challenge task 2: unsupervised anomalous sound detection for machine condition monitoring under domain shifted conditions*, arXiv : https://arxiv.org/abs/2106.04492
- Dohi et al. (2022), *Description and discussion on DCASE 2022 challenge task 2: unsupervised anomalous sound detection for machine condition monitoring applying domain generalization techniques*, arXiv : https://arxiv.org/abs/2206.05876
- Dohi et al. (2023), *Description and discussion on DCASE 2023 challenge task 2: first-shot unsupervised anomalous sound detection for machine condition monitoring*, arXiv : https://arxiv.org/abs/2305.07828
- Nishida et al. (2024), *Description and discussion on DCASE 2024 challenge task 2: first-shot unsupervised anomalous sound detection for machine condition monitoring*, arXiv : https://arxiv.org/abs/2406.07250 ; page de la tâche : https://dcase.community/challenge2024/task-first-shot-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring
- Nishida et al. (2025), *Description and discussion on DCASE 2025 challenge task 2: first-shot unsupervised anomalous sound detection for machine condition monitoring*, arXiv : https://arxiv.org/abs/2506.10097
- DCASE 2026, tâche 2, *Noise-aware unsupervised anomalous sound detection for machine condition monitoring* : https://dcase.community/challenge2026/task-first-shot-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring ; Fujimura et al. (2026), *The MERL systems for DCASE 2026 challenge task 2* : https://merl.com/publications/TR2026-100
- Purohit et al. (2019), *MIMII dataset: sound dataset for malfunctioning industrial machine investigation and inspection*, arXiv : https://arxiv.org/abs/1909.09347 ; données : https://zenodo.org/records/3384388
- Koizumi et al. (2019), *ToyADMOS: a dataset of miniature-machine operating sounds for anomalous sound detection*, arXiv : https://arxiv.org/abs/1908.03299
- Tanabe et al. (2021), *MIMII DUE*, arXiv : https://arxiv.org/abs/2105.02702 ; Harada et al. (2021), *ToyADMOS2*, arXiv : https://arxiv.org/abs/2106.02369
- Giri et al. (2020), *Self-supervised classification for detecting anomalous sounds*, DCASE Workshop : https://dcase.community/documents/workshop2020/proceedings/DCASE2020Workshop_Giri_65.pdf
- Dohi et al. (2021), *Flow-based self-supervised density estimation for anomalous sound detection*, ICASSP, arXiv : https://arxiv.org/abs/2103.08801
- Wilkinghoff (2024), *Self-supervised learning for anomalous sound detection*, ICASSP, arXiv : https://arxiv.org/abs/2312.09578
- Saengthong, Shinozaki (2024), *Deep generic representations for domain-generalized anomalous sound detection*, arXiv : https://arxiv.org/abs/2409.05035
- Jombo, Zhang (2023), *Acoustic-based machine condition monitoring - methods and challenges*, Eng 4(1). DOI : https://doi.org/10.3390/eng4010004
- Tandon, Nakra (1992), *Comparison of vibration and acoustic measurement techniques for the condition monitoring of rolling element bearings*, Tribology International 25(3):205-212 : https://repository.ias.ac.in/24220
