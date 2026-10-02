---
role: notion
nom: Foundation models et anomalies de séries
alias: [Détection d'anomalies zero-shot, Résidus de prévision zero-shot, TSFM pour anomalies, MOMENT, TimesFM]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, timeseries, foundation-model, forecasting, zero-shot, benchmark]
---

# Foundation models et anomalies de séries

## Aperçu

- Deux manières de détecter une anomalie avec un modèle de fondation pour séries temporelles, sans entraîner quoi que ce soit sur la série cible : **prévoir** avec un modèle pré-entraîné (Chronos, TimesFM, Lag-Llama) et lire l'écart entre prévision et mesure, ou **reconstruire** avec un modèle à masquage (MOMENT) et lire l'erreur de reconstruction. Dans les deux cas le score est un résidu.
- Le seul banc d'essai qui les compare sérieusement aux méthodes classiques est TSB-AD (NeurIPS 2024). Résultat : ces modèles sont **bons sur les anomalies ponctuelles, faibles sur les séquences**, MOMENT dans les douze premiers, TimesFM, Chronos et Lag-Llama en milieu de tableau, les plus lents de tous, et exposés à la contamination du pré-entraînement. Aucun n'apparaît dans son classement multivarié.
- Le « normal » est celui du corpus de pré-entraînement, pas celui de la machine. Ce qui se gagne en absence d'entraînement se paie en absence de contexte : arrêt programmé, changement de consigne ou de régime sont des surprises pour le modèle.

## Concepts clés

### Le résidu comme score

- Un prévisionniste à poids figés $\theta$ reçoit le passé récent et prédit la valeur suivante ; l'anomalie est ce que le passé ne prévoyait pas. C'est l'« approche par résidus » de [[Time series anomaly detection]], avec un modèle de prévision qu'on n'a pas eu à ajuster.
- TSB-AD les implémente ainsi pour Lag-Llama, Chronos et TimesFM : prévision comparée à la valeur réelle sur un contexte glissant, **erreur quadratique moyenne** comme score « pour garantir l'équité ». Les modèles probabilistes ([[Chronos]], Lag-Llama) fournissent des quantiles, mais le banc d'essai ne s'en sert pas.
- La qualité de prévision, mesurée par les [[Forecasting metrics]] (MASE, sMAPE), n'est pas la qualité de détection. Les sources lues ne relient pas les deux ; ne pas supposer qu'un meilleur prévisionniste donne un meilleur détecteur.

### Les modèles

- **Chronos** (Ansari et al., 2024) — met à l'échelle puis quantifie les valeurs en un vocabulaire fixe et entraîne des modèles de langue de la famille T5 (20 M à 710 M de paramètres) par entropie croisée ; testé sur 42 jeux, compétitif sans ajustement sur des jeux hors entraînement. Fiche : [[Chronos]].
- **TimesFM** (Das, Kong, Sen, Zhou, 2023-2024) — modèle à attention de type décodeur sur des *patches*, pré-entraîné sur un grand corpus ; annoncé proche des méthodes supervisées en zero-shot sur plusieurs jeux publics.
- **Lag-Llama** (Rasul et al., 2023) — transformeur décodeur, prévision probabiliste **univariée**, retards (*lags*) comme covariables.
- **Moirai** (Woo et al., ICML 2024) — encodeur « any-variate », pré-entraîné sur LOTSA (plus de 27 milliards d'observations, neuf domaines). Absent de TSB-AD.
- **MOMENT** (Goswami et al., ICML 2024) — encodeur type T5 (trois tailles calquées sur T5 Small, Base et Large) pré-entraîné par **reconstruction de patches masqués** sur la *Time Series Pile*. Entrée univariée de 512 pas ; les séries multivariées sont traitées **canal par canal**, donc sans relation entre capteurs.
- Panorama et usages du prévisionnel : [[Foundation models pour séries temporelles]].

### MOMENT dans son propre article

- Protocole : 44 séries de l'archive d'anomalies UCR, fenêtre de 512, erreur quadratique entre observation et reconstruction comme critère, en zero-shot ou par sonde linéaire ; mesures : F1 « ajusté au meilleur seuil » et VUS-ROC.
- F1 ajusté moyen : MOMENT zero-shot 0,585 ; avec sonde linéaire 0,628 ; k plus proches voisins 0,554 ; TimesNet 0,537 ; Anomaly Transformer 0,492 ; GPT4TS 0,424. Le k-NN fait légèrement mieux en VUS-ROC. Les auteurs écrivent que, selon les tâches, des méthodes statistiques ou peu profondes (dont le k-NN pour l'anomalie) battent de nombreux modèles profonds.
- Le seuil est explicitement hors périmètre (« estimer de bons seuils est un problème ouvert »), et le « meilleur seuil » est un seuil oracle ([[Évaluer une détection d'anomalies]]).

### Ce que dit TSB-AD

- Protocole : 1 070 séries, 40 jeux, 40 détecteurs, VUS-PR comme mesure de référence, hyperparamètres réglés. Chronos, TimesFM et Lag-Llama sont évalués en zero-shot ; MOMENT en zero-shot et en version ajustée (sur les premiers segments de chaque série) ; OFA (un GPT adapté) en ajustement. Les modèles de fondation ne sont évalués **qu'en univarié** (TSB-AD-U).
- Scores moyens sur TSB-AD-U (extraits du tableau 5 de l'annexe) :

| Méthode | VUS-PR | F1 standard | F1 avec *point-adjust* |
|---|---|---|---|
| Sub-PCA (statistique, 1er) | 0,42 | 0,42 | 0,56 |
| MOMENT ajusté | 0,39 | 0,35 | 0,65 |
| MOMENT zero-shot | 0,38 | 0,35 | 0,61 |
| TimesFM | 0,30 | 0,34 | 0,84 |
| Chronos | 0,27 | 0,32 | 0,83 |
| Lag-Llama | 0,27 | 0,30 | 0,77 |
| OFA | 0,24 | 0,22 | 0,67 |

- **Ponctuel contre séquence.** Sur les séries à anomalies ponctuelles, TimesFM est premier et Chronos troisième ; sur les anomalies de séquence, les méthodes statistiques dominent (Sub-KNN, POLY). Explication des auteurs : le modèle ne prédit qu'une valeur à la fois avec un contexte limité ; face à une longue anomalie, ce contexte est lui-même anormal, la prévision suit le régime anormal et le score devient bruité. MOMENT commence à se distinguer quand les anomalies sont multiples.
- **Le *point-adjust* masque l'écart.** TimesFM atteint 0,84 de F1 ajusté pour 0,34 en F1 standard, Chronos 0,83 pour 0,32 : un score bruité gagne à l'ajustement (le biais est décrit dans [[Évaluer une détection d'anomalies]]). TSB-AD le cite comme l'une des causes de « l'illusion de progrès » pour ces modèles.
- **Les LLM adaptés déçoivent** : OFA est en queue de peloton, TSB-AD parle de résultats « insatisfaisants » pour cette voie.
- **Ajustement contre zero-shot** : le test par paires de TSB-AD (Wilcoxon) donne l'avantage à MOMENT ajusté, bien que les moyennes de VUS-PR ne diffèrent que de 0,01 ; l'ajustement réduit l'intérêt du « sans entraînement ».
- **Contamination.** Le pré-entraînement de MOMENT contient des jeux d'anomalies. Sur le sous-ensemble que MOMENT a réservé à son évaluation (MOMENT-Eval), le VUS-PR de MOMENT passe, d'après la figure 15 (valeurs lues dans le texte extrait du PDF), de 0,39 à 0,14 pour la version ajustée et de 0,38 à 0,12 pour le zero-shot, alors que les méthodes statistiques ne souffrent pas de ce phénomène. Les auteurs concluent à « un problème critique de contamination des données » et à de la prudence au déploiement.
- **Coût.** Les modèles de fondation sont les plus lents du banc, en raison de leur taille ; les méthodes statistiques sont les plus rapides, suivies des réseaux, et CNN et LSTM allient efficacité et vitesse.

### Pistes plus récentes : les plongements

- Au lieu du résidu, utiliser l'**encodeur** du modèle comme extracteur de caractéristiques, puis un détecteur classique ou léger dessus. *THEMIS* (atelier AI4TS d'IJCAI 2025) applique LOF et une décomposition spectrale aux plongements de l'encodeur de Chronos ; *ChronosAD* (arXiv, mai 2026, accepté à INDIN 2026) ajoute un bloc BiLSTM-attention sur ces plongements et annonce +4,72 % d'AUC et +6,60 % d'AP sur 11 benchmarks. **Résumés lus seulement** ; THEMIS évalue sur MSL, SMAP et SWaT, des jeux jugés défectueux par TimeSeAD et Sarfraz et al. ([[Anomalies multivariées par apprentissage profond]]).

## Les maths, simplement

- **Score par prévision.** $\hat y_t=f_\theta(y_{t-L:t-1})$ avec $\theta$ figé, $L$ la longueur du contexte ; $s_t=(y_t-\hat y_t)^2$. Variante standardisée : $s_t=|y_t-\hat y_t|/\hat\sigma$, avec $\hat\sigma$ estimé sur une période normale vérifiée.
- **Score par reconstruction (MOMENT).** La fenêtre de 512 pas est découpée en *patches* ; le modèle, entraîné à reconstruire des patches masqués, rend $\hat x$ ; $s_t=(x_t-\hat x_t)^2$.
- **Variante par intervalle** (non évaluée dans les sources lues) : un modèle probabilistique donne des quantiles $q_\alpha$ et $q_{1-\alpha}$ ; un point hors de $[q_\alpha,q_{1-\alpha}]$ est signalé. Le seuil devient un niveau de risque $\alpha$ plutôt qu'une valeur à caler, à condition que les quantiles soient calibrés sur la série visée.
- **Pourquoi la longue anomalie échappe.** Si l'anomalie dure plus que le contexte $L$, tout $y_{t-L:t-1}$ est déjà anormal ; $f_\theta$ extrapole ce régime, le résidu $y_t-\hat y_t$ reste petit, et seul l'instant d'entrée dans l'anomalie produit un pic.

## En pratique

- **Quand y penser** : parc de séries hétérogènes sans historique propre à chacune, démarrage à froid, besoin d'un détecteur de pics ponctuels sans pipeline d'entraînement. Rien d'autre dans les sources lues ne justifie de les préférer.
- **Quand les écarter** : anomalies de séquence ou de régime (usure lente, dérive, oscillation durable) ; relations entre capteurs à surveiller ; budget de calcul serré. Dans ces cas Sub-PCA, k-NN, [[STUMPY]] ou une ACP multivariée font aussi bien, plus vite ([[Anomalies multivariées par apprentissage profond]]).
- **Évaluer sur ses données.** Deux garde-fous : une mesure sans *point-adjust* (VUS-PR, événements) et des données **postérieures au pré-entraînement ou privées**, faute de quoi la contamination gonfle le chiffre. Les séries d'un procédé industriel sont à ce titre un terrain plus sûr que les jeux publics, qui peuvent figurer dans le corpus.
- **Fixer le seuil sur les résidus d'une période normale** : quantile ou POT ([[Score et seuil d'alerte]]), série par série, car l'échelle du résidu varie. Aucune des sources lues ne livre de seuil prêt à l'emploi.
- **Absence de contexte machine.** Aucun de ces modèles ne sait qu'une pompe vient de démarrer : un changement de régime légitime produit un pic de résidu. Le traiter en amont (segmenter par état de marche) ou en aval ([[Détection de ruptures]]).
- **Multivarié.** MOMENT traite les canaux séparément et Lag-Llama est univarié ; pour des relations entre capteurs, voir [[Anomalies multivariées par apprentissage profond]]. Les modèles multivariés natifs (Moirai, Chronos-2 selon [[Foundation models pour séries temporelles]]) n'ont pas été évalués pour l'anomalie dans les sources lues.
- **Exploitation on-prem.** Les poids de Chronos sont publiés sous Apache-2.0 (voir la fiche) et s'exécutent localement ; [[darts]] sait envelopper un modèle de prévision pour la détection d'anomalies et intégrer Chronos comme modèle. Le coût réel est celui du GPU d'inférence, à chaque pas de la fenêtre glissante : cela se compte dès qu'on surveille des milliers de capteurs en continu ([[Détection d'anomalies en ligne]]).

## Approches voisines & alternatives

- [[Time series anomaly detection]] — la notion mère : résidus, profil matriciel, isolation.
- [[Anomalies multivariées par apprentissage profond]] — l'autre branche du neuronal : modèles entraînés par série, sur des fenêtres multivariées.
- [[Foundation models pour séries temporelles]] — le panorama des modèles et leur évaluation en prévision (GIFT-Eval, fuite de pré-entraînement).
- [[Chronos]] et [[darts]] — la brique de prévision et la bibliothèque qui peut l'envelopper.
- [[Forecasting metrics]] — les métriques de la prévision ; pas celles de la détection.
- [[Évaluer une détection d'anomalies]] — VUS-PR, *point-adjust* (Kim et al., AAAI 2022), seuil oracle.
- [[Jeux de données d'anomalies]] — TSB-AD et ses prédécesseurs, avec leurs défauts.
- [[Score et seuil d'alerte]] — comment passer d'un résidu à une décision.
- [[Détection d'anomalies en ligne]] — le flux continu où le coût d'inférence se paie.
- [[Détection de ruptures]] — pour les changements de régime que le résidu confond avec des anomalies.
- [[Contrôle statistique de procédé (SPC)]] — une carte de contrôle appliquée aux résidus d'un modèle de prévision classique se rapproche de la même idée, sans modèle de fondation.
- [[Types d'anomalies et régimes de supervision]] — ponctuelle, contextuelle, collective : la typologie qui explique la frontière ponctuel contre séquence.

## Pour aller plus loin

- Liu, Paparrizos (2024), *The Elephant in the Room : Towards A Reliable Time-Series Anomaly Detection Benchmark*, NeurIPS 2024 Datasets & Benchmarks : https://proceedings.neurips.cc/paper_files/paper/2024/file/c3f3c690b7a99fba16d0efd35cb83b2c-Paper-Datasets_and_Benchmarks_Track.pdf — dépôt : https://github.com/TheDatumOrg/TSB-AD
- Goswami, Szafer, Choudhry, Cai, Li, Dubrawski (2024), *MOMENT : A Family of Open Time-series Foundation Models*, ICML 2024. arXiv : https://arxiv.org/abs/2402.03885
- Ansari et al. (2024), *Chronos : Learning the Language of Time Series*. arXiv : https://arxiv.org/abs/2403.07815
- Das, Kong, Sen, Zhou (2023, révisé en 2024), *A Decoder-Only Foundation Model for Time-Series Forecasting*. arXiv : https://arxiv.org/abs/2310.10688
- Rasul et al. (2023), *Lag-Llama : Foundation Models for Time Series Forecasting*. arXiv : https://arxiv.org/abs/2310.08278
- Woo et al. (2024), *Unified Training of Universal Time Series Forecasting Transformers* (Moirai), ICML 2024. arXiv : https://arxiv.org/abs/2402.02592
- Sarfraz et al. (2024), *Position : Quo Vadis, Unsupervised Time Series Anomaly Detection ?*, ICML 2024. arXiv : https://arxiv.org/abs/2405.02678
- Wagner et al. (2023), *TimeSeAD : Benchmarking Deep Multivariate Time-Series Anomaly Detection*, TMLR : https://ml.cs.rptu.de/publications/2023/TimeSeAD.pdf
- Lorik et al. (2025), *THEMIS : Unlocking Pretrained Knowledge with Foundation Model Embeddings for Anomaly Detection in Time Series*. arXiv : https://arxiv.org/abs/2510.03911
- Khan et al. (2026), *ChronosAD : Leveraging Time Series Foundation Models for Accurate Anomaly Detection*. arXiv : https://arxiv.org/abs/2606.01300
- Kim, Choi, Choi, Lee, Yoon (2022), *Towards a Rigorous Evaluation of Time-series Anomaly Detection*, AAAI 2022. arXiv : https://arxiv.org/abs/2109.05257
