---
role: notion
nom: Détection hors distribution (OOD)
alias: [OOD, Out-of-distribution detection, Détection OOD, Entrée hors distribution]
categorie: ml/anomalie
domaines: [ml-eng, mlops, data-sci]
tags: [out-of-distribution, anomaly-detection, model-monitoring]
---

# Détection hors distribution (OOD)

## Aperçu

- Un modèle entraîné répond toujours, même à une entrée qui ne ressemble à rien de ce qu'il a vu. La détection OOD (*out-of-distribution*) pose la question **exemple par exemple** : cette entrée relève-t-elle de ce que le modèle sait traiter ? Si non, ne pas faire confiance à sa prédiction, voire refuser de répondre.
- C'est de la détection d'anomalies appliquée à l'entrée d'un modèle supervisé, souvent un classifieur : l'anomalie n'est pas un défaut de la machine mais une pièce, une classe ou un capteur que le modèle n'a jamais rencontrés.

## Concepts clés

### Le problème, et sa place dans la famille

- Yang et al. rangent la détection d'anomalies, de nouveauté, l'*open-set recognition*, l'OOD et celle des outliers comme cas particuliers d'un même cadre ; l'OOD y est définie comme la détection d'échantillons issus d'une distribution différente de celle de l'entraînement (cf. [[Types d'anomalies et régimes de supervision]]).
- Ce qui distingue l'OOD des autres cas : il existe un **modèle déjà entraîné** (un réseau de neurones de classification), et le détecteur se branche sur ce que ce modèle expose — ses logits, ses embeddings. Les méthodes qui suivent sont presque toutes *post-hoc* : elles ne réentraînent rien.

### Confiance softmax (le point de départ)

- Hendrycks et Gimpel (ICLR 2017) : les exemples bien classés tendent à avoir une probabilité softmax maximale plus grande que les exemples mal classés ou hors distribution. Cette probabilité maximale est donc un score, et c'est la **référence** à battre. Validé en vision, en traitement de texte et en reconnaissance vocale.
- Limite : un réseau peut attribuer une confiance très élevée à une entrée sans rapport. Nguyen, Yosinski et Clune (CVPR 2015) obtiennent des images méconnaissables classées avec une confiance voisine de 99,99 %. Lee et al. (2018) parlent de postérieurs « très trop confiants » pour les échantillons anormaux.

### Énergie

- Liu, Wang, Owens et Li (NeurIPS 2020) : le score d'énergie est $E(x;f)=-T\log\sum_i e^{f_i(x)/T}$, soit moins $T$ fois le *logsumexp* des logits. Il n'est pas probabiliste et se calcule à coût quasi nul ; on détecte quand $-E(x;f)$ dépasse un seuil $\tau$.
- Lien avec le softmax : le logarithme de la probabilité maximale est l'énergie des logits décalés de leur maximum. L'article annonce une baisse de 18,03 points du FPR95 par rapport au softmax sur CIFAR-10 avec un WideResNet.

### Distance de Mahalanobis

- Lee, Lee, Lee et Shin (NeurIPS 2018) : modéliser les caractéristiques des couches du réseau par des gaussiennes conditionnelles à la classe, puis calculer un score fondé sur la distance de Mahalanobis. Applicable à tout classifieur softmax pré-entraîné.
- Avantage souligné par les auteurs : les hyperparamètres se règlent avec les seuls échantillons *in-distribution* (les poids par couche sont appris par régression logistique sur des échantillons de validation).

### kNN sur les embeddings

- Sun, Ming, Zhu et Li (ICML 2022) : prendre l'embedding $z=\phi(x)/\lVert\phi(x)\rVert_2$ normalisé, et mesurer la distance au **$k$-ième plus proche voisin** parmi les embeddings d'entraînement. Le seuil se choisit pour qu'environ 95 % des données in-distribution passent, sans donnée OOD.
- La **normalisation est critique** : les auteurs la disent responsable d'une amélioration de 61,05 % du FPR95 par rapport au cas non normalisé. Le $k$ optimal dépend de la taille du jeu de référence : environ 1 000 avec tout le jeu d'entraînement, environ 10 avec 1 % de celui-ci.
- Coût : garder en mémoire les embeddings d'entraînement et chercher les voisins ([[k-NN]], [[embeddings]]).

### Ce que dit le benchmark OpenOOD

- OpenOOD v1.5 (Zhang et al., 2023, publié dans *Journal of Data-centric Machine Learning Research*, 2024) : **il n'y a pas de gagnant unique**, le classement change d'un jeu à l'autre. Les méthodes d'entraînement (RotPred, LogitNorm) font mieux que les méthodes post-hoc sur CIFAR-10 et CIFAR-100 ; sur ImageNet-200 et ImageNet-1K, elles ne les battent pas, et un post-processeur appliqué à un modèle entraîné en entropie croisée standard donne les meilleurs résultats en *near-OOD* comme en *far-OOD*. Les augmentations de données aident. La détection « pleine gamme » (décalages sémantiques et de covariables à la fois) reste difficile pour toutes les approches.
- La v1 (Yang et al., NeurIPS 2022 Datasets & Benchmarks) compare plus de 30 méthodes.

### Les modèles génératifs ne règlent pas la question

- Nalisnick et al. (ICLR 2019) : la densité apprise par des modèles à flux, des VAE et des PixelCNN ne distingue pas des images d'objets courants (CIFAR-10) de chiffres de maisons (SVHN) — la vraisemblance est même plus élevée sur SVHN. Une vraisemblance élevée n'est donc pas un certificat d'appartenance au normal.

### La frontière avec la dérive de données

- Le billet de l'équipe d'Evidently (2021, mis à jour en 2025) trace la ligne pour les *outliers* : la dérive regarde les distributions « globales » de tout le jeu de données ; chercher des outliers, c'est repérer des objets individuels « inhabituels » ; les deux peuvent exister indépendamment — un jeu entier peut dériver sans outlier, un outlier peut apparaître sans dérive. Le billet parle d'outliers, pas d'OOD : le rapprochement est celui de cette page.
- **Règle de lecture** : [[Data drift]] juge un **lot** contre une référence (« la distribution de la semaine a-t-elle bougé ? ») ; la détection OOD juge **un exemple** (« cette image-ci est-elle traitable ? »). Une dérive croissante se traduit en général par plus d'exemples OOD, mais l'un n'implique pas l'autre. Les outils de dérive ([[Evidently]], [[NannyML]]) comparent des colonnes ou des « chunks » de données à une référence ; ils ne signalent pas des points isolés.

## Les maths, simplement

- **Score softmax maximal** : $s_{\mathrm{MSP}}(x)=\max_c\ \mathrm{softmax}(f(x))_c$ ; rejeter si $s_{\mathrm{MSP}}(x)<\tau$.
- **Énergie** : $s_{\mathrm{E}}(x)=T\log\sum_i e^{f_i(x)/T}=-E(x;f)$ ; rejeter si $s_{\mathrm{E}}(x)<\tau$.
- **Mahalanobis** (forme de base, sans les ajouts de l'article) : $M(x)=\min_c\,(\phi(x)-\mu_c)^\top\Sigma^{-1}(\phi(x)-\mu_c)$, où $\mu_c$ est la moyenne des caractéristiques de la classe $c$ et $\Sigma$ une covariance estimée sur l'entraînement ; rejeter si $M(x)>\tau$.
- **kNN** : $s_{\mathrm{kNN}}(x)=-\lVert z-z_{(k)}\rVert_2$, avec $z_{(k)}$ le $k$-ième plus proche embedding normalisé de l'entraînement ; rejeter si $s_{\mathrm{kNN}}(x)<\tau$.
- Dans tous les cas, $\tau$ se choisit pour une fraction cible de données *in-distribution* conservées (95 % est l'usage de l'article kNN) : voir [[Score et seuil d'alerte]].

## En pratique

- **Commencer par le softmax et l'énergie** : ils ne coûtent rien et servent de ligne de base. Passer à Mahalanobis ou au kNN si la base ne suffit pas, avec un coût de stockage et de recherche.
- **Ne pas régler sur des OOD de test.** Régler un seuil ou un hyperparamètre sur les mêmes exemples OOD que ceux qui servent à évaluer est la fuite de labels classique du domaine ([[Évaluer une détection d'anomalies]]). Conserver un jeu OOD de réglage séparé de celui de test.
- **Définir ce qu'est « hors »** avant de mesurer : une classe nouvelle (décalage sémantique), un changement de capteur ou d'éclairage (décalage de covariables), une pièce de la bonne classe mais défectueuse (anomalie). Les trois ne sont pas détectés par les mêmes méthodes.
- **Brancher la réponse à une action** : refuser la prédiction, envoyer à un opérateur, journaliser pour l'étiquetage ultérieur. Un score OOD sans action associée n'est qu'un chiffre de plus.
- Un détecteur OOD qui se déclenche en masse dans la durée annonce plutôt une dérive de la distribution d'entrée : le [[Monitoring de modèles]] prend alors le relais.

## Approches voisines & alternatives

- [[Data drift]] — la même famille de questions, posée sur un lot et non sur un exemple.
- [[Monitoring de modèles]] — où les deux se rejoignent en exploitation.
- [[Evidently]], [[NannyML]] — outils de surveillance de dérive ; non conçus pour juger un exemple isolé.
- [[Calibration]] — une meilleure calibration sur les données connues ne dit pas ce que vaut une entrée inconnue : ce n'est pas un détecteur OOD.
- [[Autoencodeurs]] — la reconstruction comme score d'anomalie, sans classifieur.
- [[k-NN]] et [[embeddings]] — les briques du score kNN.
- [[Détection d'outliers multivariée]] — la version statique, sans réseau de neurones.
- [[Isolation Forest]], [[One-Class SVM]] — des détecteurs qu'on peut brancher sur des embeddings.
- [[Prédiction conforme]] — des garanties de couverture qui supposent l'échangeabilité, donc précisément pas un décalage de distribution.
- [[Score et seuil d'alerte]] — fixer le seuil $\tau$.
- [[Types d'anomalies et régimes de supervision]] — le vocabulaire et ses désaccords.

## Pour aller plus loin

- Hendrycks, Gimpel (2017), *A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks*, ICLR 2017. arXiv : https://arxiv.org/abs/1610.02136
- Liu, Wang, Owens, Li (2020), *Energy-based Out-of-distribution Detection*, NeurIPS 2020. arXiv : https://arxiv.org/abs/2010.03759
- Lee, Lee, Lee, Shin (2018), *A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks*, NeurIPS 2018. arXiv : https://arxiv.org/abs/1807.03888
- Sun, Ming, Zhu, Li (2022), *Out-of-Distribution Detection with Deep Nearest Neighbors*, ICML 2022. arXiv : https://arxiv.org/abs/2204.06507
- Yang et al. (2022), *OpenOOD*, NeurIPS 2022 Datasets & Benchmarks. arXiv : https://arxiv.org/abs/2210.07242 ; Zhang et al. (2023), *OpenOOD v1.5*. arXiv : https://arxiv.org/abs/2306.09301
- Nguyen, Yosinski, Clune (2015), *Deep Neural Networks are Easily Fooled*, CVPR 2015. arXiv : https://arxiv.org/abs/1412.1897
- Nalisnick et al. (2019), *Do Deep Generative Models Know What They Don't Know?*, ICLR 2019. arXiv : https://arxiv.org/abs/1810.09136
- Yang, Zhou, Li, Liu, *Generalized Out-of-Distribution Detection: A Survey*. arXiv : https://arxiv.org/abs/2110.11334
- Dral, Samuylova (Evidently), *What is the difference between outlier detection and data drift detection?* : https://www.evidentlyai.com/blog/ml-monitoring-drift-detection-vs-outlier-detection
