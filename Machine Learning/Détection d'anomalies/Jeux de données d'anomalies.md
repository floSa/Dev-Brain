---
role: brique
nom: Jeux de données d'anomalies
alias: [Datasets d'anomalies, Benchmarks d'anomalies]
pitch: "Annuaire commenté de onze jeux de référence pour la détection d'anomalies — images industrielles (MVTec AD, MVTec AD 2, VisA, Real-IAD), séries temporelles (NAB, SMD, SMAP/MSL, SWaT, TSB-AD) et tabulaire (ADBench, ODDS) — avec, pour chacun, la licence des données et ce qu'elle permet en usage commercial. Rien à installer ; plusieurs jeux sont réservés à la recherche."
categorie: ml/anomalie
famille: annuaire
domaines: [data-sci, ml-eng]
licence_type: 
os: 
langage: 
alternatives: []
complements: []
tags: [anomaly-detection, benchmark]
url_docs: https://thedatumorg.github.io/TSB-AD/
url_repo: https://github.com/TheDatumOrg/TSB-AD
---

# Jeux de données d'anomalies

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

**Nature de cette page, à lire en premier** : ce n'est ni un logiciel ni un service, mais un annuaire de jeux de données. Rien ne s'installe, il n'y a pas de version à suivre, et les onze entrées n'ont **pas de licence commune** : la rubrique « licence » de la fiche, vide, dit précisément cela. Chaque jeu se lit avec sa propre licence, relevée à la source le 2026-10-02.

Ce qu'ils servent à faire : comparer des méthodes publiées sur un terrain commun. Ce qu'ils ne servent **pas** à faire : prouver qu'un détecteur marchera sur les données d'une usine. Deux avertissements de fond :

- **Saturation côté images.** L'article de MVTec AD 2 écrit que MVTec AD et VisA saturent en AU-PRO de segmentation, des modèles très différents s'y séparant de moins d'un point ; Real-IAD annonce « plus de 99 % d'AUROC » sur les jeux existants. D'où MVTec AD 2, où les méthodes de l'état de l'art restent, d'après son résumé, **sous 60 % d'AU-PRO moyen**.
- **Défauts côté séries.** Wu et Keogh (IEEE TKDE) reprochent à quatre jeux populaires — Yahoo, NAB, SMAP/MSL et SMD — d'être trop faciles (beaucoup de séries se résolvent par une ligne de code), parfois mal étiquetés, ou trop denses en anomalies, au point de rendre les comparaisons peu fiables. TSB-AD est né du même constat.

| Jeu | Modalité · contenu | Licence des données | Usage commercial | Accès |
|---|---|---|---|---|
| **MVTec AD** (Bergmann et al., CVPR 2019) | Images ; 15 catégories, plus de 70 types de défauts, environ 5 400 images ; étiquettes image et masque pixel | CC BY-NC-SA 4.0 | Non | Formulaire sur la page |
| **MVTec AD 2** (Heckler-Kram et al., 2025) | Images ; 8 scénarios, plus de 8 000 images ; test privé évalué par un serveur public ; pixel | CC BY-NC-SA 4.0 | Non ; la page renvoie à MVTec pour un usage commercial | Formulaire ; serveur d'évaluation |
| **VisA** (Zou et al., ECCV 2022) | Images ; 12 objets, 10 821 images dont 1 200 anormales ; image et pixel | **CC BY 4.0** (code Apache-2.0) | Permis, avec attribution | Libre, archive publique |
| **Real-IAD** (Wang et al., CVPR 2024) | Images ; 30 objets, multi-vues, 150 000 images, 8 types de défauts | CC BY-NC-SA 4.0 d'après la carte Hugging Face (« à des fins de recherche ») | Non | Demande sur Hugging Face, approuvée automatiquement |
| **NAB** (Numenta) | Séries univariées ; 58 fichiers, réels et artificiels ; fenêtres d'anomalie | Dépôt sous MIT ; **aucune licence propre aux données** n'est écrite | Non établi | Libre, dans le dépôt |
| **SMD** (OmniAnomaly) | Séries multivariées ; 28 machines, 38 dimensions, 5 semaines ; points | Dépôt sous MIT ; licence des données non écrite | Non établi | Libre, dans le dépôt |
| **SMAP/MSL** (NASA, Hundman et al., KDD 2018) | Séries multivariées ; 82 canaux (55 + 27), 105 séquences d'anomalies | Code Apache-2.0 ; **licence des données non écrite** | Non établi | Kaggle (clé API) |
| **SWaT** (iTrust, SUTD) | Séries multivariées d'une station de traitement d'eau ; 51 capteurs et actionneurs, 41 attaques sur 11 jours dans la version A1 | Pas de licence type : conditions d'usage iTrust ; **partage du jeu interdit** | Non tranché par le texte | Formulaire, adresse institutionnelle exigée |
| **TSB-AD** (Liu et Paparrizos, NeurIPS 2024) | Séries univariées et multivariées ; 1 070 séries tirées de 40 jeux ; VUS-PR en métrique de référence | Apache-2.0 **sur la curation seulement** ; les jeux sources gardent leurs licences, hétérogènes | Selon le jeu source | Libre |
| **ADBench** (Han et al., NeurIPS 2022) | Tabulaire ; 57 jeux dont 47 réels, 30 algorithmes comparés | Dépôt sous BSD-2-Clause ; chaque jeu garde sa licence d'origine, non vérifiée jeu par jeu | Selon le jeu | Libre |
| **ODDS** (Stony Brook, Rayana, depuis 2016) | Tabulaire, collection de jeux d'outliers avec vérité terrain | **Non vérifiée** : le site n'a pas pu être ouvert le 2026-10-02 (échec de la négociation TLS) | Non vérifié | Non vérifié |

Trois jeux appellent une lecture plus fine :

- **NAB** : TSB-AD classe les données de NAB comme « GPL », ce qui contredit le MIT du dépôt. La seule affirmation tenable est que la licence des données n'est pas écrite.
- **Real-IAD** : le pied de page du site du projet parle de CC BY-SA 4.0, mais il vise le **site**, pas les données ; la carte du jeu sur Hugging Face dit CC BY-NC-SA 4.0. C'est cette dernière qui est retenue.
- **MVTec AD** : le code d'évaluation est un téléchargement distinct, sa licence n'est pas écrite sur la page.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer une méthode à l'état de l'art publié, sur un terrain que le lecteur d'un article connaît | Valider un détecteur pour un procédé réel : aucun jeu public ne reproduit ses défauts, son capteur ni son taux de base |
| Choisir un jeu de test **d'images** pour un prototype : MVTec AD pour la comparaison historique, MVTec AD 2 pour un terrain non saturé, VisA ou Real-IAD pour plus d'objets | Livrer un modèle entraîné sur MVTec AD, MVTec AD 2 ou Real-IAD à un client : licence non commerciale |
| Évaluer sur des **séries** avec un protocole sérieux : TSB-AD et sa métrique VUS-PR | Faire confiance à NAB, SMD ou SMAP/MSL pour classer des méthodes : Wu et Keogh les jugent trop faciles ou mal étiquetés |
| Comparer des détecteurs **tabulaires** sur une grille large : ADBench | Redistribuer SWaT : ses conditions d'usage l'interdisent |
| | Compter sur ODDS sans avoir ouvert sa page : licence non vérifiée ici |

## Mise en œuvre

- Installation — aucune ; chaque jeu se télécharge depuis sa page ou son dépôt (liens ci-dessous)
- Point d'entrée — le tableau de la section *Définition*
- Prérequis — un formulaire pour MVTec AD, MVTec AD 2 et SWaT ; un compte Hugging Face pour Real-IAD ; une clé API Kaggle pour SMAP/MSL
- Exécution — rien à exécuter ; compter plusieurs dizaines de gigaoctets pour Real-IAD (environ 53 Go pour la variante 1024 px, environ 507 Go pour les données brutes)
- Coût — gratuit à l'accès ; le coût est dans la licence (usage commercial interdit pour trois des onze, non établi ou non tranché pour plusieurs autres)

## Écosystème

### Alternatives

<!-- Aucune : un annuaire de jeux n'a pas d'équivalent fiché dans le brain. -->

## Ressources

- Documentation — MVTec AD : https://www.mvtec.com/company/research/datasets/mvtec-ad
- Papier — MVTec AD (CVPR 2019) : https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html
- Documentation — MVTec AD 2 : https://www.mvtec.com/company/research/datasets/mvtec-ad-2 (serveur d'évaluation : https://benchmark.mvtec.com/)
- Papier — MVTec AD 2 : https://arxiv.org/abs/2503.21622
- Dépôt — VisA : https://github.com/amazon-science/spot-diff
- Papier — VisA (ECCV 2022) : https://arxiv.org/abs/2207.14315
- Documentation — Real-IAD : https://realiad4ad.github.io/Real-IAD/ (données : https://huggingface.co/datasets/Real-IAD/Real-IAD)
- Papier — Real-IAD (CVPR 2024) : https://arxiv.org/abs/2403.12580
- Dépôt — NAB : https://github.com/numenta/NAB
- Dépôt — SMD : https://github.com/NetManAIOps/OmniAnomaly
- Dépôt — SMAP/MSL : https://github.com/khundman/telemanom
- Documentation — SWaT : https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/ (conditions d'usage : https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)
- Dépôt — TSB-AD : https://github.com/TheDatumOrg/TSB-AD (page du projet : https://thedatumorg.github.io/TSB-AD/)
- Dépôt — ADBench : https://github.com/Minqi824/ADBench
- Papier — ADBench (NeurIPS 2022) : https://arxiv.org/abs/2206.09426
- Documentation — ODDS : https://odds.cs.stonybrook.edu/ (page non ouverte le 2026-10-02)
- Papier — Wu et Keogh, critique des jeux de séries : https://arxiv.org/abs/2009.13807

## Voir aussi

- [[Détection d'anomalies]] — le hub du domaine
- [[Évaluer une détection d'anomalies]] — les métriques à employer sur ces jeux, et leurs biais
- [[Types d'anomalies et régimes de supervision]] — ce que chaque jeu suppose du « normal » de son entraînement
- [[Time series anomaly detection]] — la notion pour les jeux de séries
