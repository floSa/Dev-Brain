---
nom: chantier-anomalie-maintenance
created: 2026-10-02
modified: 2026-10-02
tags: [meta, backlog]
---

# Chantier — détection d'anomalies et maintenance prédictive

Plan unique du chantier, huit lots numérotés de 1 à 8. Chaque conversation reçoit un numéro de lot et lit **sa** section ici, rien d'autre pour le plan.
Cases cochées par la conversation qui termine son lot, sur **sa** ligne seulement.

## Objectif

Deux sections neuves dans l'arbre : `ml/anomalie` (dossier « Détection d'anomalies ») et
`ml/maintenance` (dossier « Maintenance prédictive »). Environ 55 pages. Profil visé : floSa,
on-prem industriel, ESN.

## Ce qui existe déjà (ne pas recréer, les citer)

- Anomalie tabulaire : PyOD, Isolation Forest, Local Outlier Factor, One-Class SVM, Détection d'outliers uni/multivariée, Comparatif - Détection d'anomalies.
- Série temporelle : Time series anomaly detection, STUMPY, Maintenance prédictive et RUL, Foundation models pour séries temporelles, Chronos, darts, River.
- Autour : Autoencodeurs, Data drift, Evidently, NannyML, lifelines, Imbalanced classification, ROC-AUC & courbe PR, Calibration, Ondelettes, Transformée de Fourier, STFT et spectrogramme, scipy.signal, OpenVINO, ONNX Runtime, TensorRT, InfluxDB, TimescaleDB, Grafana.
- Chaîne industrielle (`Data & pipelines/Données industrielles`) : asyncua, EMQX, Mosquitto, Node-RED, open62541, Telegraf, « Protocoles de l'atelier - MQTT, OPC UA et Modbus », Comparatif - Brokers MQTT.

## Règles communes (valent pour tous les lots)

1. **Mode brain.** Skill `enrichir-brain` pour toute page. Clôture par `cloturer-brain`.
2. **Commits petits.** Un commit par page, ou par petit groupe de pages liées. Jamais de gros commit.
3. **Push régulier**, comme le prescrit `cloturer-brain` (alias SSH perso). Jamais en HTTPS.
4. **Identité git** : la config locale du dépôt (gmail). Commit nu. `--no-verify` interdit.
5. **Aucun co-auteur.** Aucun trailer `Co-Authored-By`. Aucune mention de Claude ni d'IA dans un message de commit.
6. **Frugalité.** Commence par `AI/index/carte.md`, puis le fichier `AI/index/carte/<Domaine>.md` voulu. Interdit : charger en entier `brain-index.json`, `brain-index.md`, `liens.md`. Utilise `AI/scripts/query_index.py` pour tester l'existence d'un nom.
7. **Vérifier l'amont de chaque brique** avant d'écrire : licence, dernière version, dernier push, dépôt archivé, URL de doc. Ne devine jamais une licence, une maturité ou une date. Un fait non vérifié se demande ou s'omet.
8. **Nom unique** dans tout le vault, à la casse près, avant de créer une page.
9. **Pages `role: notion` existantes** : ne les modifie pas. Propose le changement dans ta synthèse. Exception : le lot 1 (voir plus bas).
10. **Chaque lot ajoute les liens dans les deux sens**, vers les pages existantes citées plus haut, par la procédure de `enrichir-brain`.
11. **Si ça sort de ton périmètre**, ou si un domaine tombe en D14 (arbre de `taxonomie.md`) : demande, n'invente pas.
12. **Contexte.** Vise 250 000 jetons au plus. Si tu approches, arrête-toi sur un commit propre et liste dans la synthèse les pages restantes.
13. **Parallèle.** Les lots d'une même vague tournent en parallèle dans des worktrees séparés. Si `origin/main` a bougé à la clôture, suis `cloturer-brain` : fusion dans la branche de travail, régénération des fichiers générés, jamais de fusion à la main d'un fichier généré.
14. **Fin de lot** : coche ta ligne dans « Suivi », puis termine ta réponse par une ligne vide, `SYNTHÈSE DE TÂCHES`, ta synthèse, puis `FIN DE TÂCHES`. La synthèse dit : pages créées, pages à décider, faits non vérifiés, ce qui reste.

## Vagues

| Vague | Conversations | Dépend de |
|---|---|---|
| 1 | Lot 1 | — |
| 2 | Lots 2, 3, 4 (en parallèle) | Lot 1 clos et poussé |
| 3 | Lot 5 | Lot 4 |
| 4 | Lot 6 | Lots 2, 3, 4, 5 |
| 5 | Lots 7, 8 (en parallèle) | Lots 1 à 6 clos |

## Faits vérifiés le 2026-10-02 (à reconfirmer à la source avant d'écrire)

- anomalib : dépôt `open-edge-platform/anomalib`, Apache-2.0, v2.6.x, poussé le jour même, export OpenVINO.
- patchcore-inspection (`amazon-science`) : Apache-2.0, dernier push 2024-07.
- Dinomaly (`guojiajeremy/Dinomaly`) : CVPR 2025, Apache-2.0, 99,6 % d'AUROC image sur MVTec AD.
- AnomalyCLIP (`zqhang/AnomalyCLIP`) : ICLR 2024, MIT.
- MVTec AD est saturé. MVTec AD 2 : meilleurs résultats sous 60 % d'AU-PRO.
- TSB-AD (NeurIPS 2024) : 1070 séries, 40 jeux, 40 algorithmes. Métrique de référence : VUS-PR. Les méthodes simples ou statistiques battent souvent le deep learning.
- Azure AI Anomaly Detector : retiré le 2026-10-01. AWS Lookout for Equipment : fermeture le 2026-10-07.
- Merlion (`salesforce/Merlion`) : archivé. Kats (`facebookresearch/Kats`), aeon, DeepOD, Orion, ruptures, sktime, tsfresh : actifs ou récents (dates à relire).
- scikit-survival : licence **GPL-3.0**. À signaler dans la fiche (usage ESN).
- Introuvables à l'adresse supposée : ADTK, ceruleo. Cherche la bonne adresse, sinon omets.

## Lot 1 — Ouverture et socle (vague 1)

**Accord explicite de floSa** : tu peux changer la ligne `categorie:` des 7 notions listées ci-dessous, par `git mv` + édition de cette seule ligne. Aucune autre ligne de ces notions ne change.

1. Ouvre `ml/anomalie` et `ml/maintenance` par la procédure « nouvelle valeur de catégorie » de `enrichir-brain` (brain.yml, `taxonomie.md`, `tags.md`, même commit que les pages). Libellés de dossier : « Détection d'anomalies » et « Maintenance prédictive ». Écris deux règles de départage : anomalie contre non-supervisé, maintenance contre séries-temporelles.
2. Déplace vers `ml/anomalie` : les notions Détection d'outliers multivariée, Détection d'outliers univariée, Isolation Forest, Local Outlier Factor, One-Class SVM, Time series anomaly detection ; les briques PyOD et STUMPY ; Comparatif - Détection d'anomalies (`.md` et `.base`). Déplace vers `ml/maintenance` : la notion Maintenance prédictive et RUL. Un commit par groupe lié.
3. Pose les tags dont les lots suivants ont besoin, si absents de `tags.md` : `predictive-maintenance`, `rul`, `condition-monitoring`, `vibration-analysis`, `change-point`, `statistical-process-control`, `out-of-distribution`, `thresholding`, `industrial-inspection`, `digital-twin`, `edge-ml`, `zero-shot`, `normalizing-flow`. Ne recrée pas un tag proche d'un existant.
4. Aligne `git.identite.email` de `brain.yml` sur l'adresse gmail de la config locale du dépôt. Vérifie qu'aucun hook ne compare ce champ à autre chose. En cas de doute, demande.
5. Corrige `Home.md` : sous-domaines et comptes, si l'audit le signale.
6. Écris les 5 pages du socle (`ml/anomalie`) :
   - **Types d'anomalies et régimes de supervision** (notion) : ponctuelle, contextuelle, collective ; supervisé, semi-supervisé, non supervisé ; outlier, novelty, OOD ; hypothèse « normal propre » ; contamination.
   - **Score et seuil d'alerte** (notion) : du score à la décision, quantile, valeurs extrêmes (POT), conformal, taux de fausses alertes, fatigue d'alerte.
   - **Évaluer une détection d'anomalies** (notion) : AUROC contre AUPR en classe rare, point-adjust et son biais, métriques par événement, affiliation, VUS-PR, AUROC pixel et AU-PRO, fuite de labels.
   - **Détection hors distribution (OOD)** (notion) : confiance softmax, énergie, Mahalanobis, kNN sur embeddings ; frontière avec Data drift.
   - **Jeux de données d'anomalies** (brique, `famille: annuaire`) : MVTec AD, MVTec AD 2, VisA, Real-IAD, NAB, SMD, SMAP/MSL, SWaT, TSB-AD, ADBench, ODDS. Licence de chaque jeu à vérifier (usage commercial ?).

## Lot 2 — Anomalie visuelle (vague 2)

Neuf pages, `ml/anomalie`.

- **Détection d'anomalies visuelle** (notion) : contrôle qualité, apprentissage sur le « bon » seul, sortie image + carte pixel, pourquoi pas un classifieur supervisé, saturation de MVTec AD.
- **Anomalie visuelle par banque de mémoire** (notion) : SPADE, PaDiM, PatchCore ; features pré-entraînées, coreset, plus proche voisin ; coût mémoire et latence.
- **Anomalie visuelle par reconstruction, distillation et flux** (notion) : DRAEM, RD4AD, STFPM, EfficientAD, UniAD, Dinomaly, FastFlow, CFlow.
- **Anomalie visuelle zero-shot et few-shot** (notion) : WinCLIP, AnomalyCLIP, AnomalyDINO, modèles vision-langage ; limites.
- **anomalib**, **patchcore-inspection**, **Dinomaly**, **AnomalyCLIP** (briques) : famille à dériver par l'arbre F1→F9 (poids contre code). Lien vers OpenVINO.
- **Comparatif - Détection d'anomalies visuelles** (`.md` + `.base`) : ce qui départage les quatre.
- Citer : Vision par ordinateur, Segmentation, Transfer learning vision, Modèles de fondation vision, Autoencodeurs, Métriques vision.

## Lot 3 — Séries temporelles : méthodes et outils (vague 2)

Quinze pages, `ml/anomalie`.

- **Anomalies multivariées par apprentissage profond** (notion) : LSTM-AE, USAD, TranAD, Anomaly Transformer, TimesNet ; ce que dit TSB-AD ; le point-adjust.
- **Détection de ruptures** (notion) : CUSUM, PELT, segmentation binaire, BOCPD ; rupture contre anomalie contre dérive.
- **Contrôle statistique de procédé (SPC)** (notion) : Shewhart, EWMA, CUSUM, règles de Western Electric, Cp/Cpk ; limites sous autocorrélation. Domaine à dériver (`ml/anomalie` ou `stats/*`) et à justifier.
- **Détection d'anomalies en ligne** (notion) : Half-Space Trees, RRCF, seuils adaptatifs ; lien River, Stream processing.
- **Foundation models et anomalies de séries** (notion) : résidus de prévision zero-shot, MOMENT, Chronos, TimesFM ; résultats de TSB-AD.
- Briques : **ruptures**, **aeon**, **DeepOD**, **TSB-AD**, **Orion**, **Kats**, **Merlion** (archivé), **time-series-anomaly-detector** (Microsoft), **Azure AI Anomaly Detector** (retiré le 2026-10-01 ; `famille: saas`, maturité en conséquence).
- **Comparatif - Détection d'anomalies en séries temporelles** (`.md` + `.base`).
- Citer : STUMPY, darts, River, Time series anomaly detection (sans la modifier), Forecasting metrics.

## Lot 4 — Maintenance prédictive : concepts (vague 2)

Dix pages, `ml/maintenance` (sauf l'analyse vibratoire).

- **Surveillance conditionnelle et modes de défaillance** (notion) : CBM, courbe P-F, AMDEC, stratégies correctif / préventif / prédictif ; normes à vérifier (ISO 17359, ISO 20816).
- **Indicateurs de santé** (notion) : fusion de capteurs, PCA, Mahalanobis, monotonie et tendance, seuil de panne.
- **Analyse vibratoire** (notion, `signal/traitement`) : RMS, facteur de crête, kurtosis, FFT, suivi d'ordres, enveloppe (Hilbert), cepstre. Liens vers les pages signal existantes.
- **Diagnostic de défauts de roulements** (notion) : fréquences BPFO / BPFI / BSF / FTF, spectre d'enveloppe, kurtogramme ; biais du jeu CWRU.
- **RUL par apprentissage profond** (notion) : CNN 1D, LSTM, Transformers sur C-MAPSS, étiquette plateau-puis-linéaire, incertitude, score asymétrique.
- **RUL par analyse de survie** (notion) : Weibull, Cox, AFT, censure ; lien lifelines.
- **Maintenance prédictive avec peu de pannes** (notion) : anomalie non supervisée, transfert entre machines, simulation, données synthétiques.
- **Politique de maintenance et coût** (notion) : du score à la décision, seuil qui minimise le coût, asymétrie tôt / tard.
- **Jumeau numérique et modèles hybrides** (notion) : physique + données, filtre de Kalman, résidus ; sans le battage.
- **Jeux de données PHM** (brique, `famille: annuaire`) : C-MAPSS, PRONOSTIA/FEMTO, CWRU, IMS, XJTU-SY, batteries NASA, Paderborn, MIMII. Licences à vérifier.
- **Accord de floSa, en premier geste (avant de créer le hub « Maintenance prédictive »)** : retire de la notion « Maintenance prédictive et RUL » l'alias « Maintenance prédictive », qui porte le nom du hub. Ne change rien d'autre dans cette notion ; propose ses autres ajouts dans ta synthèse. Un commit.

## Lot 5 — Maintenance prédictive : outils et offres (vague 3)

Une dizaine de pages, `ml/maintenance` ou domaine dérivé (lifelines est en `stats/inference` : applique le même arbre et justifie).

- Briques libres : **scikit-survival** (GPL-3.0), **tsfresh**, **sktime**.
- Offres : **Siemens Insights Hub** (ex-MindSphere), **Cognite Data Fusion**, **Seeq**, **AVEVA PI System** (historien, pas un outil ML), **AWS Lookout for Equipment** (fermeture le 2026-10-07), **AWS Monitron** (statut à vérifier). Faits publics seulement, aucun argumentaire commercial. Dis pour chacune si elle s'auto-héberge (axe on-prem).
- **Comparatif - Offres de maintenance prédictive** (`.md` + `.base`) : sur l'auto-hébergement, la licence, l'ouverture des données.
- Cite les notions du lot 4.

## Lot 6 — Patterns, rules et bord d'usine (vague 4)

Six pages.

- **Pattern - Pipeline de maintenance prédictive on-prem** : OPC UA → collecte (Telegraf, Node-RED) → broker MQTT → base de séries → modèle → alerte.
- **Pattern - Inspection visuelle en ligne de production** : caméra → prétraitement → modèle d'anomalie en bord (anomalib, OpenVINO) → décision → retour.
- **Pattern - Détection d'anomalies en deux étages** : règles et SPC d'abord, apprentissage ensuite.
- **Rule - Entraîner sur du normal vérifié**.
- **Rule - Évaluer une anomalie par événement, pas par point**.
- **ML en bord d'usine** (notion) : latence, CPU contre GPU, mise à jour des modèles, air-gap, quantification ; domaine à dériver.
- Les patterns citent les briques réelles du vault, pas de nom inventé.
- **Accord de floSa, câblage final.** Liste complète, issue des synthèses des lots 1 à 5. Ajoute des **liens seulement** (aucun texte réécrit), un commit par groupe de 5 fichiers au plus, regroupés par sous-dossier. Ne réécris rien d'autre dans ces pages.
  1. Notion « Time series anomaly detection » : liens vers Évaluer une détection d'anomalies, Jeux de données d'anomalies, Détection de ruptures, Contrôle statistique de procédé (SPC), Détection d'anomalies en ligne, Anomalies multivariées par apprentissage profond, Foundation models et anomalies de séries. Ajoute aussi des liens vers Insights Hub, Cognite Data Fusion et Amazon Lookout for Equipment si le contexte s'y prête.
  2. Notion « Data drift » : lien vers Détection hors distribution (OOD).
  3. Notion « Apprentissage non supervisé » : la mention des « trois usages » renvoie aussi au dossier Détection d'anomalies.
  4. Briques Evidently et NannyML : lien retour vers Détection hors distribution (OOD).
  5. Vers « Détection d'anomalies visuelle » et ses trois notions de méthode, depuis : Vision par ordinateur, Segmentation, Transfer learning vision, Modèles de fondation vision, Autoencodeurs, Métriques vision, Apprentissage auto-supervisé en vision, Vision Transformers (ViT).
  6. Notion « Foundation models pour séries temporelles » : renvoi vers Foundation models et anomalies de séries. Notions « Stream processing » et « Forecasting metrics » : renvoi vers Détection d'anomalies en ligne.
  7. Notion « Maintenance prédictive et RUL » : en « Approches voisines », liens vers Indicateurs de santé, Diagnostic de défauts de roulements, Politique de maintenance et coût, RUL par apprentissage profond, RUL par analyse de survie, Maintenance prédictive avec peu de pannes ; en « Pour aller plus loin », lien vers Jeux de données PHM ; une puce « Outils » vers scikit-survival, tsfresh, sktime. Ne touche pas à sa mention ISO 13381.
  8. Notion « Score et seuil d'alerte » : renvoi vers Politique de maintenance et coût.
  9. Liens retour vers Analyse vibratoire, en « Approches voisines » : Filtrage numérique, Transformée de Fourier, STFT et spectrogramme, Ondelettes, Traitement du signal, brique scipy.signal.
  10. Notion « RUL par analyse de survie » : remplace la phrase qui dit que scikit-survival n'a pas de fiche par un lien. Notion « Time series feature engineering » : lien vers tsfresh. Notion « Surveillance conditionnelle et modes de défaillance » : lien vers Amazon Monitron. Notion « Politique de maintenance et coût » : lien vers Comparatif - Offres de maintenance prédictive. Notion « Protocoles de l'atelier - MQTT, OPC UA et Modbus » : liens vers Insights Hub et Cognite Data Fusion.
- **Avertissements.** Le compte est passé de 148 à 158 depuis le lot 1 (R8e et R20 sur les briques ajoutées : tsfresh, scikit-survival, Seeq, Amazon Lookout for Equipment, Amazon Monitron, TSB-AD, Jeux de données d'anomalies). Pour chacune, déclare les `alternatives:` ou `complements:` évidents entre briques du même dossier, ou ajuste le filtre de la vue concernée. Sinon, liste-la dans ta synthèse avec le motif. Le compte final ne doit pas dépasser 158.
- **Vérifie** que les filtres `.base` des trois comparatifs de `ml/anomalie` ne se recouvrent pas ; s'ils se recouvrent, propose le correctif sans l'appliquer.
- **À proposer seulement, ne pas faire** (modifient du texte de page existante) : phrase sur le point-adjust de TimesNet (0,963 de F1 ajusté contre 0,218 aléatoire sur SWaT, Sarfraz et al.) dans « Évaluer une détection d'anomalies » ; puce `CoxTimeVaryingFitter` dans lifelines ; ISO 13381 dans « Maintenance prédictive et RUL ; notions à créer plus tard : adaptation de domaine hors vision, LSTM ; tags manquants (`domain-adaptation`, `conformal-prediction`, `uncertainty`, `lstm`).

## Lot 7 — Notions transverses laissées par les lots 1 à 6 (vague 5)

Trois notions, que les pages du chantier appellent sans les trouver. Domaines à dériver par l'arbre D1→D14 et à justifier dans chaque page.

- **LSTM et réseaux récurrents** (notion) : RNN, LSTM, GRU ; cellule et portes, gradient qui s'évanouit, séquences longues contre Transformers et modèles à espace d'états ; usages vus dans le chantier (RUL, anomalies multivariées). Citer : Apprentissage profond, State Space Models, Self-attention, RUL par apprentissage profond, Anomalies multivariées par apprentissage profond.
- **Adaptation de domaine** (notion) : décalage de covariables, entre machines, entre lignes, entre capteurs ; adaptation supervisée, non supervisée, par features invariantes, par ré-étiquetage ; ce qui marche avec peu de pannes. Citer : Transfer learning vision, Maintenance prédictive avec peu de pannes, Data drift, Détection hors distribution (OOD).
- **Prédiction conforme** (notion) : garantie de couverture sans hypothèse de loi, split conformal, intervalles et ensembles de prédiction, application au seuil d'alerte et à l'incertitude du RUL ; limites (échangeabilité, séries temporelles). Citer : Score et seuil d'alerte, RUL par apprentissage profond, Calibration, Forecasting metrics.
- **Tags** : crée `lstm`, `domain-adaptation`, `conformal-prediction`, `uncertainty` s'ils manquent, un commit.
- **Liens retour, liens seulement** : depuis les notions du chantier qui les appellent (RUL par apprentissage profond, Anomalies multivariées par apprentissage profond, Maintenance prédictive avec peu de pannes, Score et seuil d'alerte), vers les trois nouvelles notions. Ne touche à aucune autre page existante.
- Vérifie l'amont et cite des sources pour tout chiffre ; un fait non vérifié se signale.

## Lot 8 — Correctif BrainKit : les fichiers orphelins de la carte (vague 5)

Ce lot ne touche **pas** les pages du brain. Il travaille dans le dépôt BrainKit.

- **Problème.** Quand un fichier de la carte (`AI/index/carte/<Dossier>.md`) se scinde en « - 1 sur 2 », « - 2 sur 2 », l'ancien fichier devient orphelin. `build_carte.py` ne supprime jamais, et son `--check` échoue tant que l'orphelin existe. Deux lots du chantier ont dû faire un `git rm` à la main.
- **Étapes.**
  1. Clone `git@github.com-perso:floSa/BrainKit.git` dans `~/Projets/BrainKit` s'il est absent. Vérifie sa config git locale : même identité (gmail), mêmes règles de commit (petits commits, aucun co-auteur, push régulier).
  2. Lis seulement le générateur de la carte (grep, pas de lecture entière) et ses tests.
  3. Écris d'abord un test qui échoue : un orphelin dans le dossier généré, qui doit être supprimé en écriture, et signalé par `--check` (code 2) sans être supprimé.
  4. Corrige le générateur : en écriture, il supprime les fichiers du dossier généré qu'il ne produit plus. Il ne touche **jamais** un fichier hors de ce dossier ni un fichier qui ne porte pas sa marque « Généré par ». Décide si la suppression est opt-in ; justifie ton choix dans le commit.
  5. Fais passer toute la batterie du kit. Commit et push dans BrainKit.
  6. Reporte à la main les fichiers modifiés dans la copie figée `AI/scripts/brainkit/generer/` du DevBrain, et consigne-le dans `AI/scripts/brainkit/FIGE.md` comme les reports précédents. Vérifie que la copie est identique au kit. Clôture avec `cloturer-brain`.
- Aucune page du brain n'est modifiée. Si tu dois en toucher une, arrête-toi et demande.

## Suivi

- [x] Lot 1 — ouverture et socle
- [x] Lot 2 — anomalie visuelle
- [x] Lot 3 — séries temporelles
- [x] Lot 4 — maintenance, concepts
- [x] Lot 5 — maintenance, outils et offres
- [x] Lot 6 — patterns, rules, bord d'usine
- [x] Lot 7 — notions transverses (LSTM, adaptation de domaine, prédiction conforme)
- [x] Lot 8 — correctif BrainKit, fichiers orphelins de la carte
