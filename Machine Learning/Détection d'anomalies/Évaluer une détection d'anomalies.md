---
role: notion
nom: Évaluer une détection d'anomalies
alias: [Évaluation de la détection d'anomalies, Point-adjust, Métriques d'anomalies, VUS-PR, AU-PRO]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, model-evaluation, class-imbalance]
---

# Évaluer une détection d'anomalies

## Aperçu

- L'évaluation est l'endroit où ce domaine se trompe le plus : l'anomalie est rare, ses étiquettes sont incertaines, et les métriques usuelles se laissent flatter. Plusieurs métriques publiées ont été montrées trompeuses — en particulier le *point-adjust* sur les séries temporelles.
- Quatre pièges reviennent : choisir une métrique qui récompense le hasard, comparer sur des jeux trop faciles, régler le seuil sur ce qu'on évalue, juger un défaut visuel par un score de pixel que les grandes régions dominent.

## Concepts clés

### AUROC contre AUPR en classe rare

- Saito et Rehmsmeier (PLOS ONE, 2015) concluent que la courbe précision-rappel renseigne mieux que la courbe ROC sur des données déséquilibrées : la ROC repose sur une interprétation « intuitive mais fausse » de la spécificité, alors que la précision mesure la part de vrais positifs parmi les prédictions positives.
- Ruff et al. (2021) disent la même chose pour l'anomalie : l'AUC peut donner des scores trop optimistes sur un jeu de test très déséquilibré, l'AUPRC est alors plus informative. Contrepartie notée par les mêmes auteurs : la valeur d'un détecteur aléatoire à l'AUPRC égale la **fraction d'anomalies**, donc l'AUPRC se compare mal d'un jeu à l'autre. Ils recommandent de rapporter les deux.
- Cadre général : [[ROC-AUC & courbe PR]], [[Imbalanced classification]].

### Le point-adjust et son biais

- **Définition** (Kim et al., AAAI 2022) : dès que le score dépasse le seuil au moins une fois à l'intérieur d'un segment d'anomalie réel, **tous** les points du segment comptent comme détectés. Le *point-adjust* ne peut qu'augmenter les vrais positifs et réduire les faux négatifs ; les faux positifs ne bougent pas.
- **Résultat** : les auteurs montrent que même un score **aléatoire** peut devenir une méthode de l'état de l'art sous cette métrique. Sur la plupart des jeux, le F1 ajusté d'un score aléatoire dépasse nettement celui des méthodes existantes ; l'exception est SMD, dont les segments sont courts (longueur moyenne 90), où il plafonne vers 0,8. L'effet dépend donc de la **longueur des segments**.
- **Sans point-adjust**, un modèle non entraîné (l'entrée brute prise comme score, ou un autoencodeur LSTM à poids aléatoires) égale ou bat la plupart des méthodes publiées dans leur comparaison ; une seule les dépasse sur tous les jeux.
- Alternative proposée : PA%K, qui n'applique l'ajustement que si la fraction de points détectés du segment dépasse $K$. Et la recommandation d'AUROC ou d'AUPR plutôt que d'un F1 à seuil.

### Métriques par événement

Une anomalie de série est un **segment**, pas un point. Compter par point favorise les longs segments ; compter par événement fait de « avoir trouvé l'événement » l'unité.

- **Affiliation** (Huet, Navarro, Rossi, KDD 2022) : métrique fondée sur une affiliation entre vérité terrain et prédictions, qui mesure des relations temporelles, sans paramètre, normalisée contre un détecteur aléatoire, évaluée événement par événement. Les auteurs montrent que sous les métriques par événement antérieures, un algorithme adverse atteint une précision et un rappel élevés sur presque n'importe quel jeu. (La formule exacte n'a pas été relue dans cette page.)
- **Désaccord** : sur les dix scénarios synthétiques de TSB-AD (Liu et Paparrizos, 2024), l'Affiliation-F ne distingue presque pas les cas entre eux — ce qui nuance son usage comme seule métrique.

### VUS : une surface plutôt qu'un seuil

- Paparrizos et al. (PVLDB, 2022) ajoutent une zone tampon autour des bornes d'anomalie, de largeur variable (par défaut, jusqu'à la moitié de la période de chaque côté). Pour chaque largeur, on calcule des courbes ROC et PR ; elles forment une surface, et le volume en dessous donne **VUS-ROC** et **VUS-PR**, indépendants du seuil et de la largeur de tampon.
- **Désaccord** : Paparrizos et al. promeuvent les quatre mesures de la famille ; TSB-AD (dont Paparrizos est coauteur) retient **VUS-PR** seule, et juge que l'AUC-ROC (qui peut atteindre 0,97 malgré deux faux négatifs) comme le VUS-ROC attribuent des scores élevés à des prédictions aléatoires.

### Ce que disent les benchmarks

- **TSB-AD** (NeurIPS 2024 Datasets & Benchmarks) : 1 070 séries tirées de 40 jeux, 40 algorithmes. Conclusion du résumé : les architectures simples et les méthodes statistiques donnent souvent de meilleurs résultats. En univariée, Sub-PCA domine (VUS-PR moyen 0,42) ; seuls deux réseaux de neurones (USAD, CNN) et un modèle de fondation (MOMENT) figurent dans les douze premiers. Les modèles de fondation excellent sur les anomalies ponctuelles et peinent sur les séquences.
- **Schmidl, Wenig, Papenbrock** (PVLDB, 2022) : 71 algorithmes réimplémentés sur 976 jeux de séries. « Chaque famille peut être efficace et il n'y a pas de gagnant net » ; l'apprentissage profond n'est pas (encore) compétitif malgré son coût de calcul, et des méthodes simples font presque aussi bien. Les auteurs écartent volontairement les seuils et retiennent trois mesures indépendantes du seuil (AUC-ROC, AUC-PR, AUC-PTRT).
- Détail utile : TSB-AD règle les hyperparamètres sur 15 % de chaque jeu, et évalue sur le reste. C'est l'inverse d'un réglage sur le test.

### Images : AUROC pixel et AU-PRO

- L'AUROC **image** dit si une image est défectueuse ; l'AUROC **pixel** et l'**AU-PRO** disent où.
- **PRO** (Bergmann et al., *Uninformed Students*, CVPR 2020) : pour chaque composante connexe de la vérité terrain, on calcule le recouvrement relatif avec la zone prédite binarisée, et l'on fait croître le seuil jusqu'à un taux de faux positifs par pixel de 30 %. L'aire sous cette courbe, normalisée à 1, est l'**AU-PRO**. La métrique donne le **même poids aux régions de tailles différentes**, là où une mesure par pixel comme la ROC laisse une grande région bien segmentée compenser beaucoup de petites ratées.
- **MVTec AD 2** (Heckler-Kram et al., 2025) : la ROC par pixel est dominée par les grandes anomalies et surestime la qualité de localisation ; l'intégration du PRO passe de 0,30 à 0,05 de taux de faux positifs. Sur MVTec AD et VisA, la performance en AU-PRO de segmentation est saturée, les modèles se séparant de moins d'un point ; sur MVTec AD 2, les méthodes de l'état de l'art restent sous 60 % d'AU-PRO moyen (résumé de l'article). Voir [[Jeux de données d'anomalies]] et [[Métriques vision]].

### Fuite de labels

- **Seuil réglé sur le test.** Kim et al. relèvent que les méthodes publiées règlent le seuil après avoir regardé le jeu de test, ou prennent le seuil optimal qui maximise le F1 : le résultat dépend alors fortement du choix du seuil. À noter que leur propre protocole prend lui aussi le meilleur seuil : un F1 « à seuil oracle » **n'est pas** une performance déployable.
- **Hyperparamètres réglés sur des anomalies de test.** Lee et al. (2018) reprochent à une méthode concurrente d'être réglée sur des jeux de validation d'échantillons OOD, « ce qui est souvent impossible » en pratique ; leur propre méthode se règle avec les seuls échantillons normaux. Même exigence pour l'anomalie : si les anomalies de réglage et de test se recouvrent, le chiffre est optimiste ([[Data leakage]]).
- **Étiquettes dérivées du score.** Un jeu étiqueté a posteriori en regardant les sorties d'un détecteur favorise ce détecteur.

## Les maths, simplement

- Précision $P=\dfrac{TP}{TP+FP}$, rappel $R=\dfrac{TP}{TP+FN}$, $F_1=\dfrac{2PR}{P+R}$. En classe rare, $FP$ pèse lourd dans $P$ même quand le taux de fausses alertes est petit : voir l'erreur du taux de base dans [[Score et seuil d'alerte]].
- **Point-adjust.** Soit $S_m$ un segment d'anomalie réel. Si $\exists\, t\in S_m,\ s_t>\delta$, alors $\hat y_t=1$ pour **tout** $t\in S_m$. Un score aléatoire, tiré assez de fois dans un long segment, franchit $\delta$ presque sûrement : le segment entier est « détecté ».
- **PRO.** Avec $C_k$ les composantes connexes de la vérité terrain et $P$ la zone prédite : $\mathrm{PRO}=\dfrac1K\sum_k \dfrac{|P\cap C_k|}{|C_k|}$, tracé contre le taux de faux positifs, intégré jusqu'à une limite $f_{\max}$ (0,30 d'usage, 0,05 pour MVTec AD 2) et normalisé par $f_{\max}$.
- **Référence aléatoire de l'AUPR** : égale à la fraction $\pi$ d'anomalies ; un AUPR de 0,3 est excellent pour $\pi=0{,}01$, médiocre pour $\pi=0{,}2$.

## En pratique

- **Rapporter au moins une métrique indépendante du seuil** (AUPR ou VUS-PR sur des séries) **et** une métrique à seuil fixé avec le seuil choisi sur du normal vérifié, jamais sur le test.
- **Proscrire le point-adjust seul.** S'il figure dans un article qu'on reproduit, le recalculer sans l'ajustement, et comparer à un score aléatoire et à un score trivial (la valeur brute, sa différence).
- **Calculer la référence aléatoire** de chaque métrique sur son propre jeu : sans elle, un chiffre ne veut rien dire.
- **Compter par événement** quand l'exploitation traite des événements : un tableau de bord de maintenance ne lit pas des points. Distinguer le nombre d'événements détectés, le délai de détection et le nombre de fausses alertes par jour.
- **Ne pas conclure d'un jeu public à un procédé réel.** Les jeux publics sont faciles ou saturés ([[Jeux de données d'anomalies]]) ; la seule évaluation qui compte est sur des données du procédé, avec des défauts étiquetés par quelqu'un qui connaît la machine.
- Une anomalie rare impose peu d'événements de test : donner un intervalle d'incertitude (bootstrap) plutôt qu'une valeur ponctuelle.

## Approches voisines & alternatives

- [[ROC-AUC & courbe PR]] — les deux courbes, dans le cas général.
- [[Classification metrics]] — précision, rappel, F-mesure à seuil fixé.
- [[Imbalanced classification]] — la classe rare et ses pièges, dont l'évaluation.
- [[Forecasting metrics]] — le cas voisin pour la prévision ; une détection par résidu hérite de ses pièges.
- [[Métriques vision]] — les métriques de segmentation et de détection en vision.
- [[Data leakage]] — la fuite d'information du train vers l'évaluation, au sens large.
- [[Score et seuil d'alerte]] — comment le seuil est fixé, donc ce que les métriques à seuil mesurent.
- [[Time series anomaly detection]] — la notion qui rencontre le plus ces métriques.
- [[Anomalies multivariées par apprentissage profond]] — le cas SWaT : un score aléatoire atteint 0,963 de F1 ajusté, contre 0,218 sans ajustement (Sarfraz et al., ICML 2024).
- [[Jeux de données d'anomalies]] — les terrains d'essai, et leurs défauts connus.
- [[Types d'anomalies et régimes de supervision]] — ce que le jeu d'évaluation suppose.
- [[Détection hors distribution (OOD)]] — la même évaluation, sur les entrées d'un modèle entraîné.

## Pour aller plus loin

- Kim, Choi, Choi, Lee, Yoon (2022), *Towards a Rigorous Evaluation of Time-series Anomaly Detection*, AAAI 2022. arXiv : https://arxiv.org/abs/2109.05257
- Huet, Navarro, Rossi (2022), *Local Evaluation of Time Series Anomaly Detection Algorithms*, KDD 2022. arXiv : https://arxiv.org/abs/2206.13167
- Paparrizos, Boniol, Palpanas, Tsay, Elmore, Franklin (2022), *Volume Under the Surface*, PVLDB 15(11) : https://www.vldb.org/pvldb/vol15/p2774-paparrizos.pdf
- Liu, Paparrizos (2024), *The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark*, NeurIPS 2024 Datasets & Benchmarks. Dépôt : https://github.com/TheDatumOrg/TSB-AD
- Schmidl, Wenig, Papenbrock (2022), *Anomaly Detection in Time Series: A Comprehensive Evaluation*, PVLDB 15(9) : https://www.vldb.org/pvldb/vol15/p1779-wenig.pdf
- Saito, Rehmsmeier (2015), *The Precision-Recall Plot Is More Informative than the ROC Plot…*, PLOS ONE. DOI : https://doi.org/10.1371/journal.pone.0118432
- Bergmann, Fauser, Sattlegger, Steger (2019), *MVTec AD*, CVPR 2019. Bergmann et al. (2020), *Uninformed Students*, CVPR 2020 (définition de PRO) : https://arxiv.org/abs/1911.02357
- Heckler-Kram et al. (2025), *The MVTec AD 2 Dataset*. arXiv : https://arxiv.org/abs/2503.21622
- Ruff et al. (2021), *A Unifying Review of Deep and Shallow Anomaly Detection*. arXiv : https://arxiv.org/abs/2009.11732
