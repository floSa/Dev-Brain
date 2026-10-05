---
role: notion
nom: Anomalies multivariées par apprentissage profond
alias: [Deep learning pour anomalies multivariées, USAD, TranAD, Anomaly Transformer, LSTM-AE, TimesNet]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, timeseries, deep-learning, transformers, benchmark]
---

# Anomalies multivariées par apprentissage profond

## Aperçu

- La famille entière tient en une recette : entraîner un réseau sur des fenêtres supposées **normales** de plusieurs capteurs, lui faire reconstruire (ou prévoir) la fenêtre suivante, et lire l'**erreur** comme score d'anomalie. LSTM-AE, USAD, TranAD, Anomaly Transformer et TimesNet ne diffèrent que par l'architecture, la perte d'entraînement et la façon de combiner l'erreur.
- Les articles fondateurs annoncent tous un gain sur leurs prédécesseurs. Les évaluations indépendantes ne le retrouvent pas : sur des protocoles propres, des méthodes simples (erreur de reconstruction d'une ACP, un petit CNN ou LSTM prédictif) font aussi bien, et les architectures les plus sophistiquées (Anomaly Transformer, TimesNet, TranAD) arrivent derrière.
- Deux raisons s'additionnent : les jeux publics sont faciles ou défectueux, et la plupart des chiffres d'origine reposent sur un seuil optimisé et sur le *point-adjust* (voir [[Évaluer une détection d'anomalies]]). Cette page ne recopie pas ce biais ; elle dit **où** chaque méthode l'a utilisé.

## Concepts clés

### Le schéma commun

- Une fenêtre $W\in\mathbb{R}^{w\times m}$ (longueur $w$, $m$ variables) entre dans le réseau, qui rend $\hat W$. Le score d'un instant est une norme de $W-\hat W$ ; un seuil le transforme en alerte ([[Score et seuil d'alerte]]).
- Hypothèse implicite : le réseau n'a vu que du normal, donc il reconstruit mal l'anormal. Les [[Autoencodeurs]] montrent la limite (un modèle assez large reconstruit aussi bien les anomalies) ; USAD et TranAD sont des réponses à ce problème.
- Atout propre à cette famille : l'erreur existe **par variable**, donc elle localise. TranAD en tire une mesure de diagnostic (HitRate, NDCG) et déclare un instant anormal dès qu'une de ses $m$ dimensions dépasse son seuil.

### LSTM-AE (Malhotra et al., 2016)

- Premier de la liste, et le plus ancien : un encodeur-décodeur LSTM entraîné à reconstruire des séquences normales (*EncDec-AD*). L'article est présenté à l'ICML 2016 Anomaly Detection Workshop.
- Le score n'est pas l'erreur brute : les vecteurs d'erreur d'un jeu de validation normal sont ajustés par une loi gaussienne (maximum de vraisemblance), et le score d'un point est sa distance de Mahalanobis à cette loi. Le seuil $\tau$ n'est appris que « quand assez de séquences anormales sont disponibles », en maximisant un $F_\beta$ avec $\beta<1$. Une fenêtre contenant un motif anormal est étiquetée anormale en entier.
- Jeux : consommation électrique, navette spatiale, ECG, plus deux jeux de moteurs réels. $F_\beta$ rapporté entre 0,65 (ECG) et 0,83 (moteur non prédictible).

### USAD (Audibert et al., KDD 2020)

- Un encodeur $E$ partagé et deux décodeurs $D_1$, $D_2$ forment deux autoencodeurs $AE_1=D_1\circ E$ et $AE_2=D_2\circ E$. Entraînement en deux phases : d'abord chacun reconstruit $W$ ; puis $AE_1$ cherche à tromper $AE_2$, qui apprend à distinguer $W$ de la reconstruction d'$AE_1$. L'effet recherché est d'**amplifier** l'erreur quand l'entrée contient une anomalie.
- Score : $A(\hat W)=\alpha\|\hat W-AE_1(\hat W)\|^2+\beta\|\hat W-AE_2(AE_1(\hat W))\|^2$ avec $\alpha+\beta=1$ ; les auteurs présentent ce couple comme le réglage de sensibilité à l'inférence, avec un seul modèle entraîné.
- Revendications : meilleur $F_1$ sur SWaT, MSL, SMAP et WADI, deuxième sur SMD (SWaT et WADI sont rapportés avec et sans *point-adjust*) ; gain moyen de 0,096 sur OmniAnomaly ; temps d'entraînement divisé en moyenne par 547 face à OmniAnomaly (GPU GTX 1080 Ti). Sur des données internes d'Orange, $F_1=0{,}69$ sans *point-adjust* (précision 0,74, rappel 0,64). Détail instructif : avec *point-adjust*, c'est l'Isolation Forest, sans aucune mémoire temporelle, qui obtient le meilleur $F_1$ sur WADI, ce que les auteurs attribuent à la nature de l'ajustement.
- **Protocole** (lu dans l'article) : « les seuils possibles sont testés et on rapporte celui du meilleur $F_1$ » ; le *point-adjust* est appliqué sur SMD, SMAP et MSL pour rester comparable à OmniAnomaly. C'est donc un seuil oracle.
- Robustesse au bruit d'entraînement : du bruit gaussien injecté dans jusqu'à 5 % des points d'entraînement ne change presque rien, la précision baisse à partir de 10 %. Ce n'est pas de la contamination par de vraies anomalies.

### TranAD (Tuli, Casale, Jennings, VLDB 2022)

- Encodeur transformeur qui reçoit la fenêtre $W$ et le contexte complet $C$ jusqu'à l'instant courant, deux décodeurs, et une « auto-conditionnement » en deux passes : la première passe, avec un score de focalisation nul, donne $O_1$ ; l'écart $\|O_1-W\|^2$ sert de **score de focalisation** pour la seconde passe, qui donne $\hat O_2$. Entraînement adversarial façon USAD, plus du méta-apprentissage MAML pour les petits jeux.
- Score : $s=\tfrac12\|O_1-\hat W\|^2+\tfrac12\|\hat O_2-\hat W\|^2$, seuil par POT (*peak over threshold*, repris d'OmniAnomaly ; voir [[Score et seuil d'alerte]]). Fenêtre de 10.
- Revendications : $F_1$ en hausse jusqu'à 17 %, temps d'entraînement réduit jusqu'à 99 % — par rapport à d'autres modèles profonds. Jeux listés : NAB, UCR, MBA, SMAP, MSL, SWaT, WADI, SMD, MSDS (le résumé de l'article en annonce six, le texte sept).
- Les auteurs écrivent partager les réserves de Wu et Keogh sur la qualité des jeux, mais s'en servir pour la comparabilité. Le texte de l'article ne décrit pas de *point-adjust*.

### Anomaly Transformer (Xu, Wu, Wang, Long, ICLR 2022)

- Observation de départ : les anomalies étant rares, un point anormal peine à s'associer à l'ensemble de la série et concentre son attention sur ses voisins immédiats. D'où un critère, la **discordance d'association** (*association discrepancy*).
- Chaque bloc a deux branches : une association *a priori* (noyau gaussien d'échelle $\sigma$ apprise, centré sur la position) et une association de série (l'attention softmax habituelle). La discordance est la divergence de Kullback-Leibler symétrisée entre les deux. Entraînement *minimax* : une phase la minimise côté a priori, l'autre la maximise côté série sous contrainte de reconstruction.
- Score : $\mathrm{Softmax}(-\mathrm{AssDis})\odot\|X_i-\hat X_i\|_2^2$ — la discordance pondère l'erreur de reconstruction.
- Revendications : état de l'art sur six jeux (SMD, MSL, SMAP, SWaT, PSM, NeurIPS-TS).
- **Protocole** (lu dans l'article) : fenêtre de 100 non recouvrante ; seuil $\delta$ tel qu'une proportion $r$ des données de validation soit étiquetée anormale ($r=0{,}1\,\%$ pour SWaT, $0{,}5\,\%$ pour SMD, $1\,\%$ ailleurs) ; stratégie d'ajustement par segment, justifiée par l'idée qu'un point détecté « fait remarquer le segment entier ». C'est le *point-adjust*.

### TimesNet (Wu, Hu, Liu et al., ICLR 2023)

- Modèle généraliste (prévision, imputation, classification, détection d'anomalies). Idée : repérer les périodes dominantes par FFT, replier la série 1D en tenseurs 2D qui exposent ensemble les variations intra-période et inter-période, et y appliquer des convolutions 2D (blocs de type Inception).
- Pour l'anomalie : reconstruction, erreur comme critère, prétraitement repris d'Anomaly Transformer (fenêtre de 100) ; cinq jeux (SMD, MSL, SMAP, SWaT, PSM). $F_1$ moyen annoncé : 86,34 % pour la variante ResNeXt, contre 76,88 % pour le transformeur canonique.
- Le texte de l'article ne mentionne pas d'ajustement. Le code de la *Time-Series-Library* (`exp/exp_anomaly_detection.py`, branche `main`, lu le 2026-10-02) l'applique pourtant — appel à `adjustment(gt, pred)` — et fixe le seuil comme un percentile des énergies d'entraînement **et de test** réunies, à partir d'un `anomaly_ratio` donné d'avance. Ce qui est annoncé suppose donc de connaître la proportion d'anomalies du test.

## Ce que disent les évaluations indépendantes

- **Audibert et al.** (*Pattern Recognition*, 2022) — les auteurs d'USAD eux-mêmes comparent seize approches classiques, d'apprentissage et profondes : « aucune famille ne surpasse les autres ». Ils recommandent d'inclure les trois familles dans tout banc d'essai.
- **Wagner et al., TimeSeAD** (TMLR, 2023) — 28 méthodes profondes, jeux multivariés réanalysés. Conclusion : aucune méthode ne domine, les approches récentes peinent à égaler les anciennes ; sur SMD, LSTM-AE reste régulièrement forte ; les méthodes qui réussissent sur SMD échouent souvent sur Exathlon, et inversement. Les trois problèmes cités (jeux défectueux, métriques ponctuelles, protocoles incohérents) créent « une illusion de progrès ».
- **Sarfraz et al.**, *Quo Vadis, Unsupervised Time Series Anomaly Detection ?* (ICML 2024, position) — l'erreur de reconstruction d'une ACP, sans réseau, bat les modèles profonds. $F_1$ ponctuel sur SWaT : ACP 0,833 ; TranAD 0,799 ; USAD 0,772 ; Anomaly Transformer 0,765. Avec *point-adjust*, Anomaly Transformer monte à 0,941 sur SWaT, mais une prédiction **aléatoire** atteint 0,963 (contre 0,218 sans). Les auteurs rangent explicitement l'article d'Anomaly Transformer parmi les travaux dont le résultat repose sur cet ajustement, et montrent que des modèles de pointe se laissent distiller en modèles linéaires de performance comparable.
- **TSB-AD** (Liu et Paparrizos, NeurIPS 2024 Datasets & Benchmarks) — protocole curé, VUS-PR, hyperparamètres réglés (fenêtres, taux d'apprentissage). Scores moyens de VUS-PR :

| Méthode | Série univariée (TSB-AD-U) | Multivariée (TSB-AD-M) |
|---|---|---|
| Sub-PCA / PCA | 0,42 (1er) | 0,31 |
| CNN (prédictif) | 0,34 | 0,31 |
| OmniAnomaly | 0,29 | 0,31 |
| LSTMAD (prédictif) | 0,33 | 0,31 |
| USAD | 0,36 | 0,30 |
| TimesNet | 0,26 | 0,19 |
| TranAD | 0,26 | 0,18 |
| Anomaly Transformer | 0,12 | 0,12 |

- Lecture de TSB-AD : en multivarié, les réseaux **simples** (CNN, LSTM, OmniAnomaly, USAD) sont à égalité avec l'ACP à deux décimales ; les transformeurs sont nettement derrière, Anomaly Transformer étant dernier du tableau dans les deux cas. Les auteurs concluent que des architectures simples comme CNN et LSTM font généralement mieux que les conceptions complexes, et que les réseaux « montrent plus de promesse » en multivarié qu'en univarié. **Désaccord interne** : la figure 7 place CNN, OmniAnomaly et l'ACP aux rangs 1 à 3, le texte dit CNN et OmniAnomaly deuxième et troisième.
- Désaccord entre sources sur la portée : TSB-AD y voit une place réservée aux réseaux en multivarié (les scénarios complexes demanderaient une capacité de modélisation que les méthodes statistiques n'ont pas) ; Sarfraz et al. concluent qu'on ne justifie pas leur complexité sur les jeux actuels. Les deux s'accordent sur un point : le transformeur sophistiqué ne paie pas.

## Limites connues

### Des jeux faciles ou défectueux

- Wu et Keogh (IEEE TKDE) reprochent aux jeux historiques (Yahoo, NAB, SMAP/MSL, SMD) d'être triviaux, mal étiquetés ou trop denses en anomalies ; le détail est dans [[Jeux de données d'anomalies]].
- TimeSeAD analyse SWaT, WADI, SMAP et MSL : hors WADI, plus de 10 % d'anomalies dans le test, ce qui n'est plus « rare » ; biais de position des anomalies dans SMAP (vers la seconde moitié) ; anomalies très longues dans SWaT ; changement de distribution entre le début et la fin du test. Un modèle qui lit le contexte normal d'une fenêtre est désavantagé par les longues anomalies.
- Sarfraz et al. relèvent en outre des versions différentes du même jeu (WADI-127 contre WADI-112, avec un sous-ensemble de capteurs) comparées comme si elles étaient identiques.

### Des étiquettes qui décident du score

- L'étiquette d'un segment fixe ses bornes ; un décalage de quelques pas change le score des mesures ponctuelles. TSB-AD montre la sensibilité aux décalages de chaque mesure, et que VUS-PR y résiste le mieux. TSB-AD reconnaît lui-même que la vérification manuelle repose sur un nombre limité de relecteurs expérimentés.
- Les méthodes de cette famille sont entraînées sur du « normal » ; le jeu d'entraînement doit donc être un historique vérifié sans défaut, ce qui est une étiquette de plus à obtenir ([[Types d'anomalies et régimes de supervision]]).

### Un seuil qui n'est pas celui du terrain

- Meilleur $F_1$ sur tous les seuils (USAD), proportion d'anomalies connue d'avance (Anomaly Transformer, TimesNet) : aucun de ces seuils n'existe en exploitation. Voir [[Évaluer une détection d'anomalies]] pour l'effet sur les chiffres.

### Un coût qui ne se justifie pas toujours

- Les gains de temps annoncés (USAD, TranAD) sont mesurés contre d'autres modèles profonds, pas contre une ACP. TSB-AD mesure l'ordre inverse sur l'ensemble du banc : méthodes statistiques les plus rapides, puis réseaux, avec CNN et LSTM à la fois efficaces et rapides.
- Réglage : la taille de fenêtre pèse. USAD trouve son optimum à $K=10$ sur SWaT en testant 5 à 100, avec l'argument qu'une fenêtre courte détecte vite et une longue détecte les anomalies longues mais noie les courtes. TSB-AD règle fenêtres et taux d'apprentissage sur grille.
- Réentraînement sur dérive : le modèle suppose un normal stable ; un changement de régime est signalé comme anomalie ([[Data drift]], [[Détection de ruptures]]).

## Les maths, simplement

- **Score par reconstruction.** $s_t=\|x_t-\hat x_t\|_2^2$, moyenné sur les fenêtres qui contiennent $t$ ; ou par dimension $s_{t,i}=(x_{t,i}-\hat x_{t,i})^2$ pour localiser.
- **LSTM-AE.** Avec $e^{(i)}$ le vecteur d'erreur du point $i$, $\mu$ et $\Sigma$ estimés sur des séquences normales de validation : $a^{(i)}=(e^{(i)}-\mu)^{\top}\Sigma^{-1}(e^{(i)}-\mu)$. Un point est anormal si $a^{(i)}>\tau$.
- **USAD.** Deux phases, avec $n$ le numéro d'époque : $\mathcal L_{AE_1}=\tfrac1n\|W-AE_1(W)\|^2+(1-\tfrac1n)\|W-AE_2(AE_1(W))\|^2$ et $\mathcal L_{AE_2}=\tfrac1n\|W-AE_2(W)\|^2-(1-\tfrac1n)\|W-AE_2(AE_1(W))\|^2$. Le poids passe progressivement de la reconstruction à l'adversaire.
- **Anomaly Transformer.** Prior $P_{ij}\propto\frac{1}{\sqrt{2\pi}\sigma_i}\exp\!\big(-\tfrac{|j-i|^2}{2\sigma_i^2}\big)$ renormalisé par ligne ; discordance $\mathrm{AssDis}=\mathrm{KL}(P\|S)+\mathrm{KL}(S\|P)$ ; une anomalie, collée à ses voisins, a une série $S$ proche du prior $P$ donc une discordance faible, et $\mathrm{Softmax}(-\mathrm{AssDis})$ lui donne un poids fort.
- **Référence ACP** (Sarfraz et al.). Avec $U$ les $F'$ premiers vecteurs propres des données d'entraînement centrées : $\tilde X=\hat XU^\top U$, erreur $E=\hat X-\tilde X$. Équivalent à un autoencodeur **linéaire** entraîné à l'erreur quadratique, d'où son intérêt comme plancher : tout réseau doit le battre pour justifier sa complexité.

## En pratique

- **Commencer par le plancher.** erreur de reconstruction d'une ACP sur les capteurs, norme L2, distance au plus proche voisin dans l'historique normal. Ces références battent plusieurs réseaux publiés sur SWaT (Sarfraz et al.) ; [[PyOD]] rassemble d'autres détecteurs classiques à comparer. Si le plancher résout le problème, le reste est du coût.
- **Si le plancher échoue, monter par paliers** : un CNN ou un LSTM prédictif (rapides et au niveau de l'ACP dans TSB-AD) avant les architectures à attention. Ne pas garder un transformeur qu'un LSTM égale.
- **Évaluer sans *point-adjust*** et sans seuil oracle : VUS-PR plus une mesure par événement, seuil fixé sur une période normale vérifiée ([[Évaluer une détection d'anomalies]]). Réexécuter le dépôt d'un article avec ses réglages n'est pas le reproduire : le code de la *Time-Series-Library* applique l'ajustement d'office.
- **Valider sur des données du procédé**, avec des défauts étiquetés par quelqu'un qui connaît la machine ; les jeux publics classent mal ([[Jeux de données d'anomalies]]).
- **Exploiter la localisation** : l'erreur par variable désigne les capteurs en cause, utile à la maintenance. Elle reste une piste de diagnostic, pas une cause.
- **Prévoir le cycle de vie** : fenêtre à caler, historique normal à entretenir, réentraînement quand le régime change. Détail de l'exploitation dans [[Détection d'anomalies en ligne]] et [[Maintenance prédictive et RUL]].
- **Bibliothèques** : [[DeepOD]] propose notamment TimesNet et Anomaly Transformer (son README liste ces deux modèles et fournit une fonction d'ajustement, à ne pas employer comme seule métrique) ; [[TSB-AD]] fournit le protocole et les modèles du banc d'essai.

## Approches voisines & alternatives

- [[Time series anomaly detection]] — la notion de départ : résidus de prévision, [[STUMPY]] (profil matriciel), [[Détection d'outliers multivariée]] sur fenêtres. Trois alternatives qui n'exigent aucun entraînement profond.
- [[Autoencodeurs]] — le socle de la reconstruction, avec sa limite : un modèle trop expressif reconstruit aussi l'anomalie.
- [[Évaluer une détection d'anomalies]] — où le *point-adjust* de Kim et al. (AAAI 2022) est décrit ; les chiffres de cette page doivent se lire à travers elle.
- [[Expliquer une anomalie (contribution des capteurs)]] — de l'alerte au classement des capteurs en cause.
- [[Anomalie acoustique]] — les mêmes familles de modèles appliquées au son de machine.
- [[Jeux de données d'anomalies]] — les terrains d'essai et leurs défauts.
- [[Foundation models et anomalies de séries]] — la voie sans entraînement par série : prévoir avec un modèle pré-entraîné, lire le résidu.
- [[Détection d'anomalies en ligne]] — ce qui change quand les fenêtres arrivent au fil de l'eau et que le normal dérive.
- [[Détection de ruptures]] — un changement de régime durable est une rupture, pas une anomalie, et fait exploser le score d'un modèle réglé sur l'ancien normal.
- [[Contrôle statistique de procédé (SPC)]] — le cadre statistique de la surveillance multivariée d'un procédé, qui reste la référence en usine ; l'erreur de reconstruction d'une ACP en est une forme proche.
- [[Types d'anomalies et régimes de supervision]] — ce qu'on suppose de l'entraînement : normal pur, ou contaminé.
- [[Détection hors distribution (OOD)]] — même idée appliquée aux entrées d'un modèle déployé.
- [[Transformer architectures]] et [[Self-attention]] — le socle d'Anomaly Transformer et de TranAD.
- [[LSTM et réseaux récurrents]] — le socle de LSTM-AE et des détecteurs prédictifs : cellule, portes, limites face à l'attention.

## Pour aller plus loin

- Malhotra, Ramakrishnan, Anand, Vig, Agarwal, Shroff (2016), *LSTM-based Encoder-Decoder for Multi-sensor Anomaly Detection*, ICML 2016 Anomaly Detection Workshop. arXiv : https://arxiv.org/abs/1607.00148
- Audibert, Michiardi, Guyard, Marti, Zuluaga (2020), *USAD : UnSupervised Anomaly Detection on Multivariate Time Series*, KDD 2020. DOI : https://doi.org/10.1145/3394486.3403392
- Tuli, Casale, Jennings (2022), *TranAD : Deep Transformer Networks for Anomaly Detection in Multivariate Time Series Data*, VLDB 2022. arXiv : https://arxiv.org/abs/2201.07284
- Xu, Wu, Wang, Long (2022), *Anomaly Transformer : Time Series Anomaly Detection with Association Discrepancy*, ICLR 2022. arXiv : https://arxiv.org/abs/2110.02642
- Wu, Hu, Liu, Zhou, Wang, Long (2023), *TimesNet : Temporal 2D-Variation Modeling for General Time Series Analysis*, ICLR 2023. arXiv : https://arxiv.org/abs/2210.02186 — code : https://github.com/thuml/Time-Series-Library
- Audibert, Michiardi, Guyard, Marti, Zuluaga (2022), *Do Deep Neural Networks Contribute to Multivariate Time Series Anomaly Detection ?*, Pattern Recognition 132. arXiv : https://arxiv.org/abs/2204.01637
- Wagner, Michels, Schulz, Nair, Rudolph, Kloft (2023), *TimeSeAD : Benchmarking Deep Multivariate Time-Series Anomaly Detection*, TMLR. https://ml.cs.rptu.de/publications/2023/TimeSeAD.pdf
- Sarfraz, Chen, Layer, Peng, Koulakis (2024), *Position : Quo Vadis, Unsupervised Time Series Anomaly Detection ?*, ICML 2024. arXiv : https://arxiv.org/abs/2405.02678
- Liu, Paparrizos (2024), *The Elephant in the Room : Towards A Reliable Time-Series Anomaly Detection Benchmark*, NeurIPS 2024 Datasets & Benchmarks : https://proceedings.neurips.cc/paper_files/paper/2024/file/c3f3c690b7a99fba16d0efd35cb83b2c-Paper-Datasets_and_Benchmarks_Track.pdf — dépôt : https://github.com/TheDatumOrg/TSB-AD
- Wu, Keogh (2021), *Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress*, IEEE TKDE. arXiv : https://arxiv.org/abs/2009.13807
- Kim, Choi, Choi, Lee, Yoon (2022), *Towards a Rigorous Evaluation of Time-series Anomaly Detection*, AAAI 2022. arXiv : https://arxiv.org/abs/2109.05257
