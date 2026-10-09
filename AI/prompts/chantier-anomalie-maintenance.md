---
nom: chantier-anomalie-maintenance
created: 2026-10-02
modified: 2026-10-02
tags: [meta, backlog]
---

# Chantier — anomalies, maintenance prédictive, agents de code, stocks et plannings

Plan unique du chantier, vingt-trois lots numérotés de 1 à 23. Chaque conversation reçoit un numéro de lot et lit **sa** section ici, rien d'autre pour le plan.
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

15. **Gratuit d'abord, déployable sur site (règle de floSa, corrigée le 2026-10-07).** On cherche des solutions **non payantes** et utilisables **sur site** (on-prem, auto-hébergées). On privilégie le **libre et commercialisable** (`open-source`). Mais floSa n'a pas d'usage commercial : une solution dont le code est visible ou dont l'usage commercial est limité (`source-available`, `open-core`, licence « non commercial ») est **acceptée** si elle est gratuite pour lui. Un outil fermé mais gratuit et utile en local (LM Studio, Obsidian) est accepté aussi : la première phrase de la fiche le dit. **Pas de page** pour : un service payant ; un service cloud seulement, sans version sur site ; un logiciel fermé et payant. Une licence **introuvable ou non vérifiée** (pas de fichier LICENSE) : pas de page. `licence_type:` est toujours la valeur vérifiée à la source. Si le doute est réel, demande. Là où une section de lot dit « libre seulement », lis cette règle.
16. **Mentions.** Un service payant, cloud seulement ou fermé peut être cité en **texte simple**, sans lien `[[...]]` et sans page, quand c'est utile (un client l'utilise, il a fermé, il sert de comparaison). Jamais en brique.

17. **Nature affichée (règle de floSa, 2026-10-07).** La première phrase de chaque brique dit ce que c'est, en mots simples : agent, skill, jeu de skills, serveur MCP, outil en ligne de commande, application à héberger, plugin, bibliothèque, format. Les alternatives payantes (Jira, Linear, Notion…) se citent en texte simple dans la section Alternatives, sans page.

## Vagues

| Vague | Conversations | Dépend de |
|---|---|---|
| 1 | Lot 1 | — |
| 2 | Lots 2, 3, 4 (en parallèle) | Lot 1 clos et poussé |
| 3 | Lot 5 | Lot 4 |
| 4 | Lot 6 | Lots 2, 3, 4, 5 |
| 5 | Lots 7, 8 (en parallèle) | Lots 1 à 6 clos |
| 6 | Lot 9 (seul) | Lots 1 à 8 clos |
| 7 | Lots 10, 11, 14 (en parallèle) | Lot 9 clos et poussé |
| 8 | Lots 12, 16 (en parallèle) | Lot 11 clos (pour le 12) ; lot 10 clos (pour le 16) |
| 9 | Lot 13 | Lot 12 |
| 10 | Lot 15 | Lots 12, 13, 16 clos |
| 11 | Lot 17 (seul) | Lots 1 à 16 clos |
| 12 | Lots 18, 19, 20, 21, 22 (en parallèle) | Lot 17 clos et poussé |
| 13 | Lot 23 | Lot 19 clos |
| 14 | Lots 24, 25 (en parallèle) | Lots 1 à 23 clos et poussés |
| 15 | Lot 27 | Skill `planifier-projet` réécrit et poussé |

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

## Lot 9 — Retrait des solutions propriétaires (vague 6)

**Accord explicite de floSa** : tu peux supprimer les pages listées ci-dessous par `git rm` (l'historique est conservé), et remplacer par du texte simple les liens qui y mènent, dans les notions comme ailleurs. Aucune autre modification de texte dans les notions.

Pages à supprimer, un commit chacune :
- les 7 briques propriétaires du chantier : **Seeq**, **Siemens Insights Hub**, **AVEVA PI System**, **Cognite Data Fusion**, **Amazon Lookout for Equipment**, **Amazon Monitron**, **Azure AI Anomaly Detector** ;
- le **Comparatif - Offres de maintenance prédictive** (`.md` et `.base`), dont tous les membres disparaissent.

Procédure (suis la procédure « mode mise à jour » de `enrichir-brain`, section suppression) :
1. Pour chaque page, liste ses consommateurs avec `grep -rl` sur son nom et ses alias : corps de pages, `alternatives:` et `complements:` des briques, sections « Ce qui départage » et vues `.base` des comparatifs (Bases temporelles, BI auto-hébergée, Détection d'anomalies en séries temporelles, etc.), corps de hubs, `Home.md`, `CLAUDE.md`, `AI/index/fraicheur.json`, patterns et règles.
2. Dans le corps d'une page : remplace `[[Nom]]` ou `[[Nom|texte]]` par le texte simple, sans lien. Dans le frontmatter : retire l'entrée. Dans un comparatif : retire le paragraphe du membre disparu ; si le comparatif descend sous 2 membres, signale-le et propose, ne supprime pas.
3. **Garde les mentions utiles** : ajoute dans le corps du hub « Maintenance prédictive » un paragraphe « Hors périmètre du brain (propriétaires ou payants) » qui cite en texte simple Seeq, Siemens Insights Hub, AVEVA PI System, Cognite Data Fusion, et « Services fermés » : Amazon Lookout for Equipment (2026-10-07), Amazon Monitron, Azure AI Anomaly Detector (2026-10-01).
4. Supprime les entrées de ces pages dans `AI/index/fraicheur.json` par la voie prévue (`sonder_amont.py --recalculer`) ; sinon, dis-le.
5. Regénère, recompte `Home.md` et `CLAUDE.md`, valide. Le compte d'avertissements ne doit pas dépasser 158. `audit_inventaire.py` doit sortir conforme.
6. Fais ensuite un balayage : `grep -rn` des sept noms. Il ne doit rester que du texte simple, aucun `[[...]]`.
7. Ne touche à aucune autre brique, même propriétaire : si tu en trouves (`licence_type` différent de `open-source`), liste-les dans ta synthèse, sans rien faire.

## Lot 10 — Agents de code libres (vague 7)

Domaine `llm/agent-de-code`. Applique la règle 15 : **licence libre seulement**. floSa exclut Claude Code, Codex CLI et Gemini CLI.

- Candidates, à vérifier chacune à la source : **OpenCode** (le nom a été porté par plusieurs projets : dis lequel est lequel, lequel est archivé, lequel est devenu Crush), **Goose**, **Crush**, **Kilo Code**, **Roo Code**. Cherche aussi un ou deux autres agents de code libres actifs que le brain n'a pas (Qwen Code, par exemple) et propose-les sans les créer.
- Pour chaque candidate : licence exacte (fichier LICENSE), version et date de la dernière release, archivage, fournisseurs de modèles pris en charge, usage avec un modèle local (Ollama, vLLM), mode d'exécution (terminal, extension, application). Une candidate non libre (source-available, licence FSL, offre payante au cœur du produit) n'obtient **pas** de page : dis-le dans ta synthèse.
- Une brique par candidate retenue, puis mets à jour **Comparatif - Assistants de code IA** (`.md` et `.base`), et le hub « Agents de code ». Cite Aider, Cline, Continue, OpenHands, pi, Hermes Agent, OpenClaw.

## Lot 11 — Ouverture de la recherche opérationnelle, et gestion de stock (vague 7)

1. **Ouvre le sous-domaine** qui accueillera stocks et plannings, par la procédure « nouvelle valeur de catégorie » de `enrichir-brain`. Derive-le par l'arbre D1→D14 ; hypothèse de départ : `math/recherche-operationnelle` (dossier « Recherche opérationnelle »), distinct de `math/optimisation` (les méthodes de résolution). Écris la règle de départage. S'il vaut mieux ranger dans `math/optimisation`, justifie-le. Ne déplace aucune page existante sans demander.
2. Écris 7 notions : **Modèle du vendeur de journaux (newsvendor)**, **Quantité économique de commande et tailles de lot**, **Stock de sécurité et taux de service**, **Politiques de réapprovisionnement (s,S) et (R,Q)**, **Classification ABC/XYZ**, **De la prévision probabiliste à la quantité commandée**, **Indicateurs de stock (rotation, couverture, rupture)**.
3. Cite, sans les modifier : Intermittent demand, Hierarchical forecasting, Forecasting framing, Forecasting metrics, Prédiction conforme, Optimisation combinatoire.
4. Tags manquants à créer, un commit : `inventory`, `supply-chain`, `newsvendor`, s'ils n'existent pas.

## Lot 12 — Planification et ordonnancement (vague 8, après le lot 11)

Sous-domaine ouvert par le lot 11. Six notions : **S&OP et plan directeur de production**, **MRP et calcul des besoins**, **Ordonnancement d'atelier (job-shop, flow-shop)**, **Plannings de personnel (rostering)**, **Tournées de véhicules (VRP)**, **Programmation par contraintes**. Cite Programmation linéaire en nombres entiers (MIP), Optimisation combinatoire, Optimisation sous contrainte, les notions du lot 11. Tags manquants : `scheduling`, `constraint-programming`, `vehicle-routing`, `logistics`, s'ils n'existent pas. N'utilise pas `supply-chain`, qui désigne la chaîne d'approvisionnement logicielle.

## Lot 13 — Solveurs libres, simulation et pattern (vague 9, après le lot 12)

Règle 15 : libres seulement.
- Lis d'abord la page existante **Comparatif - Solveurs d'optimisation** et ses membres (PuLP, etc.) : complète-la, ne la double pas.
- Briques candidates, à vérifier à la source : **OR-Tools** (CP-SAT), **HiGHS**, **Pyomo**, **CVXPY**, **SimPy**, **Timefold Solver**, plus **PyVRP** et **HGS-CVRP** (MIT, vus sur leurs dépôts par le lot 12, tournées de véhicules). Le lot 12 a rangé la notion « Programmation par contraintes » en `math/optimisation` et les cinq autres en `math/recherche-operationnelle` : applique la même règle D-R12 aux briques (solveur = méthode de résolution, donc `math/optimisation`) et justifie chaque rangement. Exclus de page : toute brique `open-core` ou à édition payante, dont Gurobi et CPLEX, qui se citent en texte simple seulement.
- **Pattern - Prévoir puis optimiser** : demande, stock, plan. Il cite des briques et notions réelles du brain.
- Met à jour les hubs et le comparatif des solveurs.

## Lot 14 — Fiabilité et exploitation de la maintenance (vague 7)

Domaine `ml/maintenance` quand le sujet est un modèle ; dérive sinon.
- Notions : **Indicateurs de fiabilité (MTBF, MTTR, disponibilité)**, **OEE et rendement global**, **Cause racine d'une anomalie**, **Expliquer une anomalie (contribution des capteurs)**, **Santé de batterie (SOH et RUL)**, **Anomalie acoustique**.
- Briques candidates, libres seulement, à vérifier : une **GMAO / CMMS libre** (Atlas CMMS, openMAINT, par exemple ; Odoo est open-core : pas de page), **PyBaMM** pour les batteries. Cherche d'autres outils libres actifs ; une candidate non libre n'a pas de page.
- Cite les notions existantes : Maintenance prédictive et RUL, Surveillance conditionnelle et modes de défaillance, Politique de maintenance et coût, Types d'anomalies et régimes de supervision, Explicabilité des modèles, SHAP.

## Lot 15 — Câblage final des lots 10 à 14 (vague 10, après les lots 12, 13 et 16)

**Accord de floSa** : liens seulement (aucun texte réécrit), un commit par groupe de 5 fichiers au plus regroupés par sous-dossier. Lis d'abord le frontmatter de chaque page : ne lien que si le renvoi est naturel, deux liens au plus par page.

1. Depuis les notions et briques existantes vers les notions du lot 14 : Indicateurs de fiabilité (MTBF, MTTR, disponibilité), OEE et rendement global, Santé de batterie (SOH et RUL), Anomalie acoustique, Expliquer une anomalie (contribution des capteurs), Cause racine d'une anomalie. Pages candidates : Politique de maintenance et coût, RUL par analyse de survie, Protocoles de l'atelier - MQTT, OPC UA et Modbus, Jumeau numérique et modèles hybrides, Indicateurs de santé, Analyse vibratoire, Contrôle statistique de procédé (SPC), Découverte causale, Surveillance conditionnelle et modes de défaillance, Anomalies multivariées par apprentissage profond, Jeux de données d'anomalies.
2. Depuis les notions existantes vers les notions de stock (lot 11) et de planification (lot 12) : Intermittent demand, Hierarchical forecasting, Forecasting framing, Prédiction conforme, Optimisation combinatoire, Programmation linéaire en nombres entiers (MIP), Optimisation sous contrainte, et la brique PuLP. Vers les briques du lot 13 : le hub Optimisation et la brique PuLP. Depuis les notions du lot 11 (Quantité économique de commande, Stock de sécurité, Politiques (s,S) et (R,Q)) vers les notions du lot 12. Depuis la brique PuLP vers Programmation par contraintes.
3. Le retrait de l'alias « recherche opérationnelle » du hub Optimisation (fait par le lot 11) est confirmé par floSa.
4. **À proposer seulement, ne pas faire** : Chronos et « Foundation models pour séries temporelles » parlent d'intervalles « sans calibration » alors que les docs lues ne garantissent aucune couverture ; « Forecasting metrics » pourrait dire que la perte pinball vaut le coût du vendeur de journaux à un facteur près ; ajouts à « Jeux de données PHM » (DCASE, MIMII DUE, jeux de batterie Oxford, CALCE, MIT-Stanford-Toyota) ; pAUC et moyenne harmonique de DCASE dans « Évaluer une détection d'anomalies » ; tag `battery` ; PyBOP ; BatteryML, archivé, à citer sans fiche ; notions voisines manquantes (lois de durée de vie de Weibull, processus de renouvellement, théorie des contraintes, analyse multivariée de procédé T² et SPE, distance de Mahalanobis, valeurs de Shapley, causalité de Granger).

## Lot 16 — Agents de code libres, suite (vague 8)

Domaine `llm/agent-de-code`. Règle 15 : libre seulement. Le lot 10 a laissé ces candidats.
- **Qwen Code** (Apache-2.0, actif d'après le lot 10) et **Zoo Code** (fork de Roo Code, Apache-2.0, actif) : vérifie chacun à la source (licence, dernière release, archivage, fournisseurs de modèles, usage local).
- **Kilo Code** : dépôt MIT, mais le lot 10 n'a pas pu confirmer l'usage avec ses propres clés ni un modèle local. Vérifie dans la documentation : si la clé propre et le modèle local sont possibles et que rien de payant n'est au cœur du produit, crée la page ; sinon, cite-le en texte simple.
- Exclus : Crush (licence FSL), Roo Code (extension fermée, dépôt archivé), Kimi CLI (archivé), Plandex (dernier push en 2025-10 : mentionne-le en texte simple s'il est utile). Claude Code, Codex CLI et Gemini CLI restent exclus par floSa.
- Mets à jour **Comparatif - Assistants de code IA** (`.md`, la vue `.base` est filtrée par catégorie) et le hub « Agents de code ».

## Lot 17 — Gestion de projet : ouverture et méthodes (vague 11)

floSa veut une section « Gestion de projet » : outils, **skills précis** et **méthodes** (les méthodes sont des notions) pour aider le développement et le cycle de vie d'un projet, avec ou sans agent. Libre seulement (règles 15 et 16). Pas de remplissage : une page doit servir.

1. **Vocabulaire.** Derive par l'arbre D1→D14 et ouvre au plus **deux** valeurs de catégorie par la procédure « nouvelle valeur » de `enrichir-brain`. Hypothèse : `devtools/projet` (dossier « Gestion de projet »). Écris la règle de départage. Les lots suivants utilisent ces valeurs. Ne déplace aucune page existante.
2. **Notions à écrire** (14). Chacune : courte, claire, directe, un schéma Mermaid quand il aide (Obsidian le rend). Cite les briques du brain concernées.
   - **Cycle de vie d'un projet assisté par agent** : cadrer, spécifier, planifier, implémenter, vérifier, documenter, livrer ; ce que l'agent fait bien, mal, et où l'humain décide.
   - **Développement piloté par la spécification** : la spécification avant le code ; plan, tâches ; limites et coût.
   - **PRD et user stories** : contenu minimal, critères d'acceptation.
   - **Backlog, Kanban, Scrum et Shape Up** : version légère en solo et avec agents. Parallèle avec Jira : ce que Jira apporte en entreprise, en texte simple, sans page Jira.
   - **ADR et design docs** : décisions d'architecture et RFC ; format MADR ; où les ranger. Cite en texte simple log4brains et adr-tools.
   - **Modèle C4** : quatre niveaux ; outils en texte simple : Structurizr, D2, PlantUML, Kroki ; liens vers Mermaid, Excalidraw, draw.io, GitDiagram.
   - **Documentation : Diátaxis et docs-as-code** : les quatre types de pages, la doc dans le dépôt.
   - **Fichiers de contexte pour agents** : AGENTS.md, CLAUDE.md, règles, skills ; taille, pièges. Cherche d'abord une notion existante (context engineering, Agent Skills) : cite-la au lieu de la doubler.
   - **Revue, tests et « terminé » avec un agent** : définition de terminé, tests d'abord, revue de ce que l'agent a écrit.
   - **La boucle de Ralph** : un agent relancé en boucle contre un plan, contexte neuf à chaque tour ; quand ça marche, quand ça dérive.
   - **Branches courtes et worktrees pour agents** : isoler le travail de chaque agent.
   - **Commits conventionnels, versions et changelog** : Conventional Commits, SemVer, Keep a Changelog.
   - **Mesurer un projet : DORA, coût des agents, temps passé** : quoi mesurer, avec quoi (les briques viennent au lot 22).
   - **Vibe coding contre ingénierie agentique** : limites, quand reprendre la main.
3. **Citer, sans les modifier** : BMAD, Spec Kit, Graphify, i-have-adhd, GitDiagram, Mermaid, Excalidraw, draw.io, Obsidian, Forgejo, GitLab CE, pytest, Hypothesis, testcontainers, pre-commit, ai-memory, swarm-forge, t3code, Agent patterns.
4. Hub du dossier : corps écrit à la main, avec un « Choisir » qui renvoie aussi vers les briques déjà rangées ailleurs (BMAD, Spec Kit, Graphify, i-have-adhd en `llm/agent-de-code`).
5. Tags à créer, un commit : `project-management`, `spec-driven`, `adr`, `documentation`, `skills`, s'ils n'existent pas.

## Lot 18 — BMAD en détail, et la spécification d'abord (vague 12)

**BMAD est l'outil que floSa veut le mieux comprendre.** Il veut des pages claires et directes, avec **des schémas** (Mermaid), qui passent en revue tout ce qu'on peut faire avec.

1. **Lis d'abord la documentation officielle actuelle** (https://docs.bmad-method.org et le dépôt `bmad-code-org/BMAD-METHOD`, licence MIT, marque déposée par BMad Code LLC). Ne t'appuie pas sur la fiche existante : elle peut être périmée. Le README décrit aujourd'hui une boucle Clarify, Plan, Build & Verify, Learn & Adjust, un « skill hub » `bmad`, des commandes `bmad setup`, `bmad status`, `bmad-build`, et des modules : BMad Method, BMad Builder, Creative Intelligence Suite, Test Architect, BMad Loop, Game Dev Studio. Vérifie tout, et décris ce qui existe vraiment : agents ou rôles, workflows, artefacts produits.
2. **Notion « BMAD : la méthode »** : le principe, les phases, les rôles, les artefacts, l'adaptation de la profondeur de planification, quand BMAD convient et quand il est trop lourd. Au moins deux schémas Mermaid : la boucle de livraison, et qui produit quoi. Parallèle avec Scrum et avec le cycle du lot 17.
3. **Notion « BMAD : tour complet des skills »** : chaque module, chaque agent ou skill, chaque commande, ce qu'on en tire, dans quel ordre on les utilise, un exemple de session de bout en bout. Un tableau « je veux faire X, j'utilise Y ». Installation (skills CLI, plugin) et outils compatibles.
4. **Accord de floSa** : tu peux corriger la fiche brique **BMAD** si elle contredit la documentation officielle actuelle, et y ajouter les liens vers les deux notions. Liste les corrections dans ta synthèse. Ne touche à aucune autre brique.
5. **OpenSpec** (brique, `Fission-AI/OpenSpec`, MIT) : spécification dans le dépôt, suivi des changements. Cite Spec Kit et BMAD en comparaison, en texte simple ou par lien.
6. Agent OS (`buildermethods/agent-os`, MIT) : texte simple, pas de page. Kiro (AWS) et Task Master (clause Commons Clause) : texte simple.

## Lot 19 — Skills précis pour le cycle de vie (vague 12)

floSa veut des **skills précis, qui font une chose précise** : pas de méta-collection. Une brique par jeu de skills (`famille` à dériver : un skill s'exécute dans un agent hôte), qui **liste chaque skill avec ce qu'il fait et à quelle étape on le lance**. Dépôts vérifiés le 2026-10-07 ; relis la licence de chaque dépôt avant d'écrire.

- **Superpowers** (`obra/superpowers`, MIT) : brainstorming (explorer le besoin avant de coder), writing-plans, executing-plans, subagent-driven-development, dispatching-parallel-agents, test-driven-development, systematic-debugging, requesting-code-review, receiving-code-review, verification-before-completion (preuves avant d'annoncer « terminé »), using-git-worktrees, finishing-a-development-branch, writing-skills.
- **Ponytail** (`DietrichGebert/ponytail`, MIT) : ponytail (la solution la plus simple qui marche), ponytail-review (revue de sur-ingénierie sur un diff), ponytail-audit (même chose sur tout le dépôt), ponytail-debt (registre des raccourcis laissés), ponytail-gain (tableau de mesure), ponytail-help. Les chiffres de gain annoncés (54 % de code en moins) sont ceux du projet : cite-les comme tels.
- **agent-skills** (`addyosmani/agent-skills`, MIT) : idea-refine, interview-me, spec-driven-development, planning-and-task-breakdown, incremental-implementation, test-driven-development, code-review-and-quality, code-simplification, debugging-and-error-recovery, git-workflow-and-versioning, documentation-and-adrs, ci-cd-and-automation, shipping-and-launch, context-engineering, doubt-driven-development, source-driven-development, constraint-driven-development, security-and-hardening, deprecation-and-migration, api-and-interface-design, browser-testing-with-devtools, observability-and-instrumentation, performance-optimization, frontend-ui-engineering.
- **skills de Matt Pocock** (`mattpocock/skills`, MIT) : code-review, diagnosing-bugs, domain-modeling, grill-with-docs, implement, implement-spec, improve-codebase-architecture, prototype, research, retro, pr, grill-me, handoff, writing-for-agents, setup-pre-commit, git-guardrails (blocage des commandes git dangereuses). Ignore les dossiers `deprecated` et `in-progress`.
- **pm-skills** (`phuryn/pm-skills`, MIT) : skills de gestion de produit : create-prd, user-stories, job-stories, sprint-plan, retro, pre-mortem, release-notes, prioritization-frameworks, outcome-roadmap, test-scenarios, stakeholder-map, interview-script, opportunity-solution-tree, identify-assumptions, prioritize-features.
- **Notion « Quel skill pour quelle étape »** : le tableau qui réunit tout : étape du cycle de vie, besoin, skill précis, jeu qui le porte. C'est la page qu'on ouvre pour choisir. Ajoute-y, en une ligne chacun et si la licence le permet, quatre skills d'Anthropic (`anthropics/skills`) : skill-creator (créer et mesurer un skill), mcp-builder (construire un serveur MCP), webapp-testing (tester une application web avec Playwright), doc-coauthoring (rédiger une spec ou un document de décision). Vérifie la licence **skill par skill** (beaucoup indiquent « terms in LICENSE.txt ») : sans licence libre confirmée, cite-les en texte simple, sans lien d'installation.
- Pas de page pour : everything-claude-code, wshobson/agents, awesome-copilot (trop larges). Texte simple dans la notion.
- Cite Agent Skills, AGENTS.md, i-have-adhd, BMAD, Spec Kit et les notions du lot 17.

## Lot 20 — Outils autour de l'agent : contexte, parallèle, revue, livraison (vague 12)

Libre seulement. Chaque fiche commence par dire ce que c'est (règle 17). Vérifie l'amont de chaque dépôt.

- **Contexte** : Context7 (`upstash/context7`, MIT, serveur MCP : documentation à jour des bibliothèques), Repomix (`yamadashy/repomix`, MIT, outil en ligne de commande : empaquette un dépôt pour une IA), DeepWiki-Open (`AsyncFuncAI/deepwiki-open`, MIT, application à héberger : wiki généré d'un dépôt), Serena (`oraios/serena`, licence à lire dans le dépôt, serveur MCP : compréhension du code par symbole). Gitingest, claude-mem et ai-memory : texte simple ou lien.
- **Agents en parallèle** : Vibe Kanban (`BloopAI/vibe-kanban`, Apache-2.0, application locale : un tableau Kanban où chaque carte lance un agent dans sa branche). Claude Squad, Ruflo, Crystal : texte simple dans la notion du lot 17.
- **Revue** : PR-Agent (`qodo-ai/pr-agent`, MIT, revue automatique de pull requests, auto-hébergeable). Kodus et Lefthook : texte simple.
- **Livraison** : Commitizen (`commitizen-tools/commitizen`, MIT, Python), git-cliff (`orhun/git-cliff`, Apache-2.0), release-please (`googleapis/release-please`, Apache-2.0), just (`casey/just`, CC0), mise (`jdx/mise`, MIT). Task et python-semantic-release : texte simple.
- **Comparatif - Versions et changelog** (`.md` + `.base`) : Commitizen, git-cliff, release-please.

## Lot 21 — Documenter et dessiner l'architecture (vague 12)

Libre seulement. Valeur de catégorie ouverte au lot 17 pour la documentation, sinon `devtools/projet`.

- **Documentation** (briques) : MkDocs (`mkdocs/mkdocs`, BSD-2 ; dernier push en 2025-10 : dis si le projet ralentit), mkdocstrings (`mkdocstrings/mkdocstrings`, ISC : documentation d'API Python depuis les docstrings), Sphinx, Docusaurus (MIT), Zensical (`zensical/zensical`, MIT, successeur de Material for MkDocs qui est en maintenance : vérifie). VitePress, Starlight, mdBook et pdoc : texte simple dans le comparatif.
- **Comparatif - Générateurs de documentation** (`.md` + `.base`).
- **Dessin d'architecture** : LikeC4 (`likec4/likec4`, MIT, modèle C4 en code) en brique. D2, PlantUML, Structurizr, Kroki, Diagrams : texte simple dans la notion C4 du lot 17.
- Cite : Diátaxis, C4, ADR (lot 17), Mermaid, Excalidraw, draw.io, GitDiagram, Graphify, Obsidian.

## Lot 22 — Suivi de projet auto-hébergé et mesure (vague 12)

Libre seulement. **Pas de page pour OpenProject ni Plane** (floSa : on oublie OpenProject) : texte simple. Parallèle avec Jira en texte simple, sans page Jira : ce que Jira fait en entreprise et ce que les outils libres couvrent.

- **Suivi** : Redmine (GPL, `redmine/redmine`) et Kanboard (MIT, `kanboard/kanboard`) en briques. Vikunja, Wekan, Huly, Leantime, Taiga, Focalboard : texte simple.
- **Comparatif - Suivi de projet auto-hébergé** (`.md` + `.base`) : Redmine, Kanboard ; méthode supportée, poids, état d'entretien.
- **Mesure** : ccusage (`ryoppippi/ccusage`, licence à lire : coût et jetons des sessions d'agent), ActivityWatch (`ActivityWatch/activitywatch`, MPL-2.0 : suivi du temps automatique, local), Kimai (`kimai/kimai`, AGPL-3.0 : suivi du temps facturable). Apache DevLake et Claude-Code-Usage-Monitor : texte simple dans la notion « Mesurer un projet ».
- Cite : Backlog.md, Beads (texte simple si pas de page), Forgejo, GitLab CE, Obsidian, les notions du lot 17.

## Lot 23 — Annuaires et standards, à part (vague 13, après le lot 19)

floSa veut les annuaires et les standards **à part des outils**, jamais mêlés à eux.

- Propose d'abord, dans ta synthèse intermédiaire ou ta première question, l'endroit : un dossier ou sous-domaine séparé nommé « Annuaires et standards », hors des hubs d'outils. Sans réponse, crée-le (`famille: annuaire` ou `specification`).
- Candidats, à vérifier : **AGENTS.md** (`agentsmd/agents.md`, MIT, format), **Agent Skills** (spécification SKILL.md, agentskills.io : une notion « Agent Skills » existe déjà en `llm/agents`, cite-la au lieu de la doubler), **awesome-claude-code** (`hesreallyhim/awesome-claude-code`, licence à lire), **awesome-claude-skills** (`ComposioHQ/awesome-claude-skills`, pas de licence détectée), **anthropics/skills** (dépôt officiel de skills, licences variables). Une page par annuaire, sans description des outils qu'il liste.
- Aucune page ne doit se faire passer pour un outil.

## Lot 24 — Outils manquants (vague 14)

Règle 15 corrigée (gratuit d'abord, déployable sur site). Vérifie la licence de chaque dépôt **à la source** (`gh api repos/<dépôt> --jq .license` puis le fichier LICENSE) avant d'écrire. Licence introuvable ou outil abandonné : pas de page, dis-le dans ta synthèse. Pour chaque outil, la **première phrase** dit ce que c'est en mots simples (règle 17).

Une page par outil, rangée avec ses voisins de même sujet (regarde la carte et l'index, ne devine pas) :

- **Tâches et spécifications** : Backlog.md (`MrLesk/Backlog.md`, tâches en fichiers Markdown dans le dépôt), Beads (`gastownhall/beads`, MIT, suivi de tâches pour agents, dans git), Agent OS (`buildermethods/agent-os`, MIT : tu écris une fois tes règles de code, nommage, structure, tests, dans des fichiers ; l'outil les donne à l'agent à chaque tâche pour qu'il code comme toi ; donne un exemple concret dans la fiche). floSa veut garder ces outils de gestion de projet à portée : relie-les à OpenSpec, Fichiers de contexte pour agents, Backlog, Kanban, Scrum et Shape Up.
- **Plusieurs agents** : Claude Squad (`smtg-ai/claude-squad`, AGPL-3.0, plusieurs agents dans tmux). Mets-le près de Vibe Kanban.
- **Contexte** : Gitingest (`coderamp-labs/gitingest`, dépôt GitHub en un seul fichier pour l'IA). Près de Repomix.
- **Qualité et versions** : Lefthook (`evilmartians/lefthook`, hooks git rapides, près de pre-commit), python-semantic-release (`python-semantic-release/python-semantic-release`, versions et publication PyPI depuis les commits, près de release-please), Task (`go-task/task`, lanceur de commandes en YAML, près de just).
- **Diagrammes écrits en texte** : D2 (`d2lang/d2`, MPL-2.0), PlantUML (`plantuml/plantuml`, LGPL-3.0), Kroki (`yuzutech/kroki`, MIT), près de LikeC4 et Mermaid.
- **Décisions** : MADR (`adr/madr`, l'API ne détecte pas de licence : lis le fichier LICENSE, modèle de fiche pour les décisions d'architecture), à relier à la notion « ADR et design docs ».
- **Suivi** : Vikunja (`go-vikunja/vikunja`, listes de tâches auto-hébergées) et Wekan (`wekan/wekan`, Kanban à la Trello), près de Redmine et Kanboard ; Claude-Code-Usage-Monitor (`Maciek-roboblog/Claude-Code-Usage-Monitor`, coût des sessions en temps réel) et Apache DevLake (`apache/devlake`, tableaux de bord de livraison DORA), près de ccusage.
- **Annuaire** : awesome-claude-code (`hesreallyhim/awesome-claude-code`, licence CC BY-NC-ND 4.0 : usage non commercial, donc accepté depuis la règle 15 corrigée) avec `devtools/annuaire-standard`. Dis dans la première phrase que c'est un annuaire et que la licence interdit l'usage commercial. **Pas de page** pour awesome-claude-skills (aucun fichier de licence).

Mets à jour les comparatifs existants de ces dossiers au lieu d'en créer : Diagrammes, Suivi de projet auto-hébergé, Versions et changelog, Générateurs de documentation, et le comparatif des lanceurs de commandes s'il existe. Aucune nouvelle notion : relie les fiches aux notions existantes (lien seul dans la notion, c'est autorisé). Si le sous-domaine « Annuaires et standards » atteint 5 pages, le dossier apparaît seul : fais la promotion proprement (`cloturer-brain`). Recompte les chiffres de `Home.md` et `CLAUDE.md` avec `audit_inventaire.py`.

## Lot 25 — Notions voisines et pages fermées déjà au brain (vague 14)

**Partie A — cinq notions** (`role: notion`, gabarit `Templates/Concept-Wiki.md`, schéma Mermaid si ça aide). Cherche d'abord dans l'index : si une notion couvre déjà le sujet, ne la double pas, ajoute un lien. Explique chaque notion en mots simples, avec un exemple d'usine ou de capteur.

- **Weibull** : la loi qui décrit la durée de vie d'une machine avant panne (taux de panne qui monte, baisse ou reste plat).
- **Shapley** : ce qui a pesé dans la décision d'un modèle, calculé comme un partage équitable entre les variables. Relie à SHAP si la brique existe.
- **Mahalanobis** : la distance qui dit si un point est bizarre en tenant compte des corrélations entre capteurs. Relie à la détection d'anomalies.
- **Granger** : le test pour savoir si une série aide à prédire une autre. Dis sa limite : ce n'est pas une preuve de cause.
- **T² et SPE** : les deux indicateurs classiques de surveillance d'un procédé industriel, à partir d'une ACP. Relie à la maintenance prédictive et au contrôle statistique de procédé.

**Partie B — Neptune.** floSa donne son accord pour retirer la page **seulement si** tu confirmes à une source officielle que le service hébergé est arrêté. Si oui : `git rm` de la page, puis chaque `[[Neptune]]` devient du texte simple « Neptune (service arrêté en mars 2026) », y compris dans les comparatifs (page et `.base`), les `alternatives:` et les hubs. Régénère, valide. Si non confirmé : ne supprime rien et dis-le.

**Partie C — les 31 autres pages fermées ou payantes** (floSa les **garde toutes**, par connaissance : AWS S3, SageMaker, Cloudflare R2, Vertex AI, Azure ML, Snowflake, Databricks, Pinecone, Modal, OpenRouter, Cohere Rerank, LlamaParse, LangSmith, Zapier, gumloop, Figma, DataRobot, Alteryx, Comet, Weights & Biases, Postman, GitHub Actions, DataGrip, SQL Server, Dataiku, LM Studio, LM Studio Bionic, Obsidian, TensorRT, Page to Markdown, Superwhisper). floSa autorise ici, pour ces 31 briques seulement, de modifier la **première phrase** et la ligne `alternatives:` / `## Alternatives`, rien d'autre. Pour chacune, la première phrase dit : ce que c'est, et si c'est payant, cloud seulement, ou gratuit en local. Ajoute, si elle existe au brain, l'alternative libre ou sur site (exemple : Zapier renvoie vers n8n). La page ne dit jamais « n'utilise pas » : elle dit ce que c'est, et que rien n'empêche de l'utiliser. Vérifie aussi que LM Studio et LM Studio Bionic se renvoient l'un à l'autre. Pour les pages `open-core` et `source-available` (une soixantaine), ne modifie rien : liste seulement dans ta synthèse celles dont la première phrase ne dit pas la nature.

## Lot 27 — Kits de bonnes pratiques de démarrage (vague 15)

Le skill `planifier-projet` (réécrit le 2026-10-09) initialise un projet avec ses règles écrites. Il les lit dans `Rules/` par `python3 .claude/skills/planifier-projet/scripts/candidats.py regles --mot <sujet>`, puis copie une ligne par règle `MUST` dans l'`AGENTS.md` du nouveau projet (dix lignes au plus). Ce lot écrit les règles qui manquent.

Règles déjà présentes, à lire d'abord et à ne pas doubler : « Toolchain Python », « Structure de projet », « Qualité stricte », « Config typée », « Packaging démo ». Ajoute, ou étends si une page couvre déjà le sujet :

- **Tests** : niveau essentiel (pytest, un test de bout en bout) et niveau strict (CI, seuil de couverture). Lien vers pytest, Hypothesis.
- **Commits et versions** : commits conventionnels, contrôles avant commit (pre-commit ou Lefthook), versions automatiques (Commitizen, python-semantic-release ou release-please). Lien vers les fiches du lot 20 et 24.
- **Git et identité** : identité locale du dépôt, aucun co-auteur, petits commits, **contrôle mécanique** (hook commit-msg et pre-commit) plutôt que consigne seule. Retour d'expérience du DevBrain : une consigne écrite a laissé passer cinq commits avec la mauvaise adresse. Le script `scripts/garde_fous.sh` du skill en est l'implémentation.
- **Docker** : image minimale, utilisateur non root, `.dockerignore`, vérification de santé, aucun secret dans l'image.
- **Documentation de projet** : `README.md` pour qui arrive, `docs/` (cadrage, décisions, spécification), `AGENTS.md` court, décisions au format MADR, repères Diátaxis.
- **Projet assisté par agent** : spécification avant le code, vérification avant de rendre la main, branches courtes et worktrees, ce qui va dans `AGENTS.md` et ce qui va ailleurs. S'appuie sur les notions du lot 17.
- **Secrets et configuration** : fichier `.env` jamais commité, modèle d'exemple, validation au démarrage. Étends « Config typée » si elle couvre déjà l'essentiel.

Contraintes de forme :

- `role: rule`, gabarit `Templates/Rule.md`. Frontmatter complet, avec des `tags:` qui nomment le sujet et le langage (python, docker, tests, git, docs) : c'est par eux que le skill retrouve la règle.
- Sections `MUST`, `SHOULD`, `NICE-TO-HAVE`. Chaque `MUST` est **une phrase courte, à l'impératif**, qui se recopie telle quelle dans `AGENTS.md`. Pas plus de six `MUST` par règle.
- Ajoute une section `## Pour AGENTS.md` : trois à cinq lignes prêtes à copier. Vérifie d'abord que le validateur accepte la section ; sinon, mets ces lignes dans les `MUST`.
- Outils cités : gratuits et déployables sur site (règle 15). Liens nus `[[...]]` vers les briques du brain.
- Mets à jour le hub `Rules` par la régénération habituelle. Ne touche pas aux règles existantes, sauf pour y ajouter un lien.
- Recompte `Home.md` et `CLAUDE.md` avec `audit_inventaire.py`.

## Suivi

- [x] Lot 1 — ouverture et socle
- [x] Lot 2 — anomalie visuelle
- [x] Lot 3 — séries temporelles
- [x] Lot 4 — maintenance, concepts
- [x] Lot 5 — maintenance, outils et offres
- [x] Lot 6 — patterns, rules, bord d'usine
- [x] Lot 7 — notions transverses (LSTM, adaptation de domaine, prédiction conforme)
- [x] Lot 8 — correctif BrainKit, fichiers orphelins de la carte
- [x] Lot 9 — retrait des solutions propriétaires
- [x] Lot 10 — agents de code libres
- [x] Lot 11 — recherche opérationnelle et gestion de stock
- [x] Lot 12 — planification et ordonnancement
- [x] Lot 13 — solveurs libres, simulation, pattern
- [x] Lot 14 — fiabilité et exploitation
- [x] Lot 15 — câblage final des lots 10 à 14
- [x] Lot 16 — agents de code libres, suite
- [x] Lot 17 — gestion de projet : ouverture et méthodes
- [x] Lot 18 — BMAD en détail et spécification d'abord
- [x] Lot 19 — skills précis pour le cycle de vie
- [x] Lot 20 — outils autour de l'agent
- [x] Lot 21 — documenter et dessiner l'architecture
- [x] Lot 22 — suivi de projet auto-hébergé et mesure
- [x] Lot 23 — annuaires et standards, à part
- [x] Lot 24 — outils manquants
- [x] Lot 25 — notions voisines et pages fermées déjà au brain
- [x] Lot 27 — kits de bonnes pratiques de démarrage
