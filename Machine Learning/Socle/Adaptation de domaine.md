---
role: notion
nom: Adaptation de domaine
alias: [Domain adaptation, adaptation de domaine non supervisée, UDA, unsupervised domain adaptation, domain shift, décalage de domaine, covariate shift, décalage de covariables, importance weighting, pondération par importance, DANN, adaptation au test, test-time adaptation, TTA, généralisation de domaine, domain generalization, transfert entre machines]
categorie: ml/socle
domaines: [data-sci, ml-eng, mlops]
tags: [domain-adaptation, transfer-learning, data-drift, predictive-maintenance]
---

# Adaptation de domaine

## Aperçu

- Situation : un modèle est appris sur un **domaine source** (des étiquettes, une distribution) et doit servir sur un **domaine cible** dont la distribution est **différente**. L'adaptation de domaine cherche à compenser cet écart, avec peu ou pas d'étiquettes côté cible.
- Dans l'industrie, le « domaine » est une machine, une ligne, un site, un capteur de remplacement, un régime d'exploitation. Le cas typique : des pannes en abondance sur une flotte voisine ou en simulation, presque aucune sur la machine à surveiller.
- Trois situations selon ce qu'on a côté cible : **non supervisée** (aucune étiquette), **semi-supervisée** (quelques-unes), **supervisée** (assez pour affiner). Variante : l'**adaptation au test**, qui ajuste le modèle sur les données cibles au moment de l'inférence sans revoir la source.
- À ne pas confondre : [[Data drift]] **mesure** l'écart entre deux lots, l'adaptation le **compense** ; [[Détection hors distribution (OOD)]] repère un exemple que le modèle ne connaît pas, l'adaptation tente de le lui faire connaître ; [[Transfer learning vision]] réutilise des features pré-entraînées pour une nouvelle **tâche**, ici la tâche reste la même et c'est la **distribution** qui change.
- **Rangement.** Arbre D1→D14 : aucun grand modèle de langage requis (D1 non) ; un modèle d'apprentissage est entraîné (D2 oui) → `ml/*`. Dans `ml/*`, c'est un **régime d'apprentissage** qui ne suppose rien de la nature des données (ni des images, ni des colonnes, ni une séquence) : `ml/socle`, comme [[Apprentissage semi-supervisé]] et [[Apprentissage fédéré]]. `ml/monitoring` est écarté (il observe un modèle déployé, il ne le corrige pas : le sujet ici est le geste d'apprentissage) ; `ml/vision` aussi, bien que [[Transfer learning vision]] y soit rangé.

## Concepts clés

### Quel décalage ?

Kouw et Loog (arXiv 1812.11806, *An introduction to domain adaptation and transfer learning*) distinguent trois cas, et le bon outil dépend du cas :

- **Décalage de covariables** (*covariate shift*) : $p(x)$ change, $p(y\mid x)$ non. Un autre capteur, un autre régime de charge, une autre température : les mêmes causes donnent les mêmes effets, mais on les observe ailleurs.
- **Décalage des étiquettes** (*prior shift*) : les fréquences des classes changent. Une machine neuve tombe moins en panne que celle d'une flotte usée : $p(y)$ diffère.
- **Décalage de concept** : $p(y\mid x)$ change. Une même signature vibratoire n'annonce pas la même panne sur deux machines. Aucune méthode sans étiquette cible ne le corrige en général.

Entre machines, les trois coexistent. Savoir lequel domine décide du reste.

### Pondérer par importance (covariate shift pur)

- Shimodaira (2000) : sous décalage de covariables, l'estimation par maximum de vraisemblance n'est plus cohérente ; **pondérer** chaque terme par $w(x)=p_{\text{cible}}(x)/p_{\text{source}}(x)$ la rétablit.
- Sugiyama, Nakajima, Kashima, von Bünau et Kawanabe (NIPS 2007) estiment ce rapport **directement**, sans estimer les deux densités.
- Limites : le décalage doit être de covariables **pur**, la cible doit être couverte par la source (sinon $w$ n'est pas défini), et un rapport extrême donne une variance énorme : quelques points portent tout l'entraînement.

### La borne qui dit pourquoi ça peut échouer

- Ben-David, Blitzer, Crammer, Kulesza, Pereira et Vaughan (*Machine Learning* 79, 2010, pp. 151-175) bornent l'erreur cible d'un classifieur par son erreur source, plus la divergence entre les deux distributions d'entrée (une quantité estimable sur des échantillons **non étiquetés**), plus un terme $\lambda^*$ : l'erreur d'**une** hypothèse bonne sur les deux domaines.
- Lecture utile : si aucun modèle de la classe ne marche à la fois sur la source et sur la cible, aucune quantité d'alignement ne sauvera le résultat, et $\lambda^*$ ne se lit sur aucune donnée non étiquetée.

### Apprendre des features invariantes

- **DANN** (Ganin et al., *Domain-Adversarial Training of Neural Networks*, arXiv 1505.07818, JMLR 2016) : des features à la fois utiles à la tâche sur la source et **indiscernables** entre source et cible, grâce à une **couche d'inversion de gradient** qui entraîne l'extracteur contre un classifieur de domaine. S'ajoute à un réseau existant sans changer la rétropropagation.
- **Deep CORAL** (Sun et Saenko, arXiv 1607.01719, 2016) : aligne les statistiques d'**ordre deux** (les corrélations) des activations entre domaines, sans adversaire.
- **La limite démontrée.** Zhao, Tachet des Combes, Zhang et Gordon (arXiv 1901.09453, 2019) construisent un contre-exemple : des features invariantes à faible erreur source n'assurent pas une bonne erreur cible quand les distributions **conditionnelles** diffèrent ; et quand les fréquences de classes diffèrent entre domaines, il existe une borne inférieure : l'invariance et la petite erreur conjointe se disputent. Pour la maintenance, où le taux de pannes n'est pas le même d'une machine à l'autre, c'est le cas ordinaire, pas une curiosité.

### S'adapter au moment du test

- **Tent** (Wang, Shelhamer, Liu, Olshausen et Darrell, ICLR 2021, arXiv 2006.10726) : sans toucher à l'entraînement, minimiser l'**entropie** des prédictions sur les lots cibles, en n'ajustant que les statistiques et les paramètres affines de normalisation. Ne demande que le modèle et les données cibles (*source-free*). Évalué sur classification d'images corrompues, chiffres et segmentation.
- **Ce que ça donne en RUL.** Yu, Zhao et Qin (*Eksploatacja i Niezawodność* 29(1), août 2026) étudient l'adaptation au test sur la prévision de durée de vie, C-MAPSS, N-CMAPSS et des squelettes LSTM. Leur résultat : l'adaptation n'aide que si la **source est plus variée en régimes** que la cible ; restreinte aux paramètres de normalisation, toutes les méthodes à gradient donnent des sorties fonctionnellement équivalentes ; une **normalisation par lot adaptative sans gradient** égale ou dépasse les méthodes à gradient dans cinq scénarios sur six. Résultat d'un seul article, résumé lu.

### Généralisation de domaine : quand la cible est inconnue

- Si aucune donnée cible n'est disponible à l'entraînement, on parle de **généralisation de domaine**. Gulrajani et Lopez-Paz (*In Search of Lost Domain Generalization*, arXiv 2007.01434, 2020) introduisent DomainBed et trouvent que, avec une sélection de modèle soignée, la **minimisation du risque empirique** simple fait aussi bien ou mieux que les méthodes spécialisées sur tous les jeux testés. La leçon vaut au-delà de ce cadre : un résultat d'adaptation qui ne dit pas comment le modèle a été choisi n'est pas un résultat.

### Choisir un modèle sans étiquette cible

- C'est le point faible de la littérature. Ragab et al. (AdaTime, arXiv 2203.08321, *ACM TKDD* 2023) évaluent 11 méthodes sur 50 scénarios inter-domaines et 5 jeux de séries temporelles, et relèvent que les travaux antérieurs violaient le principe non supervisé en **sélectionnant le modèle avec des étiquettes cibles**. Autre résultat : des méthodes d'image bien réglées rivalisent avec celles conçues pour les séries.
- Conséquence : séparer les machines **par construction** (une machine cible tenue à l'écart pour de bon), et dire quelle information a servi à choisir les hyperparamètres.

## Les maths, simplement

- **Borne de Ben-David** (classification binaire, classe $\mathcal H$, $\varepsilon$ erreur, $d_{\mathcal H\Delta\mathcal H}$ divergence entre les deux lois d'entrée) :

$$\varepsilon_T(h)\;\le\;\varepsilon_S(h)\;+\;\tfrac12\,d_{\mathcal H\Delta\mathcal H}\!\big(P_X^S,P_X^T\big)\;+\;\lambda^*,\qquad \lambda^*=\min_{h\in\mathcal H}\big(\varepsilon_S(h)+\varepsilon_T(h)\big).$$

- **Pondération** : sous décalage de covariables pur, le risque cible se réécrit en espérance sous la source,
  $R_T(h)=\mathbb E_{(x,y)\sim S}\big[w(x)\,\ell(h(x),y)\big]$ avec $w=p_T/p_S$. D'où l'entraînement pondéré de Shimodaira.
- **DANN** : un extracteur $G_f$, une tête de tâche $G_y$, une tête de domaine $G_d$. On cherche le point-selle de $L_y(G_y\circ G_f)-\lambda\,L_d(G_d\circ G_f)$ : minimiser la perte de tâche, **maximiser** la perte de domaine côté extracteur. La couche d'inversion de gradient réalise cela : identité à l'aller, gradient multiplié par $-\lambda$ au retour.
- **CORAL** : avec $C_S$, $C_T$ les matrices de covariance des activations et $d$ leur dimension, la perte pousse $\lVert C_S-C_T\rVert_F^2/(4d^2)$ vers zéro, en plus de la perte de tâche. (Forme lue dans l'article de 2016 ; non revérifiée ici.)

## En pratique

### Ce qui marche avec peu de pannes

Hiérarchie de rédaction de cette page, **pas un résultat publié** : monter d'un cran seulement quand le précédent ne suffit pas, et toujours garder le cran 0 comme témoin.

0. **Aucune adaptation** (modèle source appliqué tel quel) : le plancher. Une méthode d'adaptation qui ne le bat pas n'a pas sa place.
1. **Normaliser par domaine** : centrer et réduire chaque capteur **par machine**, ou par régime. Le décalage de covariables dû aux étalonnages et aux plages de fonctionnement s'en va largement. Sur FD002 et FD004 de C-MAPSS, la normalisation par condition abaisse le RMSE dans toutes les cellules appariées d'un audit de 1 080 exécutions (préimpression, relevé dans [[RUL par apprentissage profond]]).
2. **Quelques trajectoires cibles** : affiner le modèle source sur ce qu'on possède ([[Fine-tuning]], [[Méta-apprentissage et few-shot learning]]). Ce que vaut une panne côté cible dépasse souvent ce qu'apporte un alignement.
3. **Pondérer** si le décalage est de covariables et que les domaines se recouvrent.
4. **Alignement adversarial ou de corrélations** (DANN, CORAL) en dernier : le plus lourd, le plus fragile, et celui dont la borne de Zhao et al. avertit quand les taux de panne diffèrent.
5. **Adaptation au test** (Tent, normalisation par lot adaptative) quand le modèle est déjà déployé et que la cible dérive, sachant le résultat de Yu et al. sur la variété des régimes.

### Dans la maintenance prédictive

- **LSTM + DANN sur C-MAPSS.** da Costa, Akcay, Zhang et Kaymak (arXiv 1907.07480, *Reliability Engineering & System Safety*) : fenêtre temporelle, [[LSTM et réseaux récurrents|LSTM]] et réseau adversarial de domaine, source étiquetée en RUL et cible sans étiquette, entre conditions d'exploitation et modes de panne différents. Les auteurs rapportent des prédictions plus fiables que sans adaptation.
- **Revue.** Wang, Ragab, Hou, Chen, Wu et Li (arXiv 2510.03604, octobre 2025) classent les méthodes d'adaptation en RUL de turboréacteurs selon trois axes (méthodologie, origine du décalage, problème visé) et en évaluent une sélection. Résumé lu.
- **Alignement des stades de dégradation.** Hou, Ragab, Wu, Kwoh, Li et Chen (TACDA, arXiv 2512.02610, *IEEE Transactions on Automation Science and Engineering* 2025) ajoutent une reconstruction du domaine cible dans l'adaptation adversariale et alignent des stades de dégradation analogues. Les auteurs annoncent de meilleurs résultats que l'état de l'art ; résumé lu, protocole non audité.
- **Réserve de fond** : ces travaux reposent sur C-MAPSS, une simulation (voir [[RUL par apprentissage profond]]). Passer d'un sous-jeu simulé à un autre n'est pas passer d'une flotte à une machine réelle. Le cadre général, les revues et les autres moyens (simulation, synthétique) sont dans [[Maintenance prédictive avec peu de pannes]].

### Pièges

- **Valider sur la cible étiquetée** tout en l'appelant non supervisé : la faute que relève AdaTime.
- **Taux de pannes différent** : le décalage des étiquettes brise l'invariance (Zhao et al.). Ne pas lire une bonne exactitude sur une cible rare en pannes comme une adaptation réussie : voir [[Imbalanced classification]] et [[ROC-AUC & courbe PR]].
- **Sur-aligner** : effacer des différences qui portaient justement le signal de défaut.
- **Alerter sur le décalage au lieu de le traiter** : [[Evidently]] et [[NannyML]] mesurent la dérive en production ; ils ne remplacent pas l'adaptation, ils disent quand elle devient nécessaire.
- **Garantie de couverture** : une enveloppe conforme perd sa garantie sous décalage ; Tibshirani et al. (2019) la rétablissent par pondération si le rapport de vraisemblance est connu, voir [[Prédiction conforme]].

## Approches voisines & alternatives

- [[Transfer learning vision]] — réutiliser des features pré-entraînées pour une autre tâche ; l'adaptation garde la tâche et change la distribution.
- [[Méta-apprentissage et few-shot learning]] — apprendre à apprendre vite à partir de quelques exemples, une voie pour la cible rare.
- [[Fine-tuning]] — le geste le plus simple dès qu'on a quelques étiquettes cibles.
- [[Maintenance prédictive avec peu de pannes]] — le cadre d'usage : transfert entre machines, simulation, synthétique.
- [[Data drift]] — mesurer le décalage au lieu de le compenser ; [[Monitoring de modèle en production]] pour la boucle complète.
- [[Détection hors distribution (OOD)]] — dire qu'un exemple sort du connu, quand l'adaptation n'est pas possible.
- [[Apprentissage semi-supervisé]] — utilise des données non étiquetées de **la même** distribution ; ici elles viennent d'une autre.
- [[Apprentissage fédéré]] — plusieurs domaines (sites) dont les données ne circulent pas ; le décalage entre clients y est le cas courant.
- [[Optimal transport]] — une famille de méthodes d'alignement de distributions, voisine de la divergence de la borne.
- [[Apprentissage contrastif]] et [[Apprentissage auto-supervisé en vision]] — apprendre des features moins dépendantes du domaine sans étiquettes.
- [[Calibration]] — les probabilités se dérèglent sous décalage ; recalibrer sur la cible si quelques étiquettes existent.

## Pour aller plus loin

- Kouw, Loog (2018), *An introduction to domain adaptation and transfer learning* : <https://arxiv.org/abs/1812.11806>
- Ben-David, Blitzer, Crammer, Kulesza, Pereira, Vaughan (2010), *A theory of learning from different domains*, Machine Learning 79 : 151-175 : <https://research.google/pubs/a-theory-of-learning-from-different-domains/>
- Shimodaira (2000), *Improving predictive inference under covariate shift by weighting the log-likelihood function*, Journal of Statistical Planning and Inference 90(2) ; seules les références ont été vues, pas le texte.
- Sugiyama, Nakajima, Kashima, von Bünau, Kawanabe (2007), *Direct Importance Estimation with Model Selection and Its Application to Covariate Shift Adaptation*, NIPS 2007 : <https://proceedings.neurips.cc/paper/2007/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract.html>
- Ganin et al. (2015), *Domain-Adversarial Training of Neural Networks* : <https://arxiv.org/abs/1505.07818>
- Sun, Saenko (2016), *Deep CORAL: Correlation Alignment for Deep Domain Adaptation* : <https://arxiv.org/abs/1607.01719>
- Zhao, Tachet des Combes, Zhang, Gordon (2019), *On Learning Invariant Representation for Domain Adaptation* : <https://arxiv.org/abs/1901.09453>
- Wang et al. (2020), *Tent: Fully Test-time Adaptation by Entropy Minimization*, ICLR 2021 : <https://arxiv.org/abs/2006.10726>
- Gulrajani, Lopez-Paz (2020), *In Search of Lost Domain Generalization* : <https://arxiv.org/abs/2007.01434>
- Ragab et al. (2022), *ADATIME: A Benchmarking Suite for Domain Adaptation on Time Series Data* : <https://arxiv.org/abs/2203.08321>
- da Costa et al. (2019), *Remaining Useful Lifetime Prediction via Deep Domain Adaptation* : <https://arxiv.org/abs/1907.07480>
- Wang et al. (2025), *Deep Domain Adaptation for Turbofan Engine Remaining Useful Life Prediction* : <https://arxiv.org/abs/2510.03604>
- Hou et al. (2025), *Target-specific Adaptation and Consistent Degradation Alignment for Cross-Domain Remaining Useful Life Prediction* : <https://arxiv.org/abs/2512.02610>
- Yu, Zhao, Qin (2026), *Test-Time Adaptation for Cross-Domain Remaining Useful Life Prediction: When Does…*, Eksploatacja i Niezawodność 29(1) : <https://ein.org.pl/Test-Time-Adaptation-for-Cross-Domain-Remaining-Useful-Life-Prediction-When-Does,226057,0,2.html>. Titre complet non relevé.
- Connexions brain : [[Maintenance prédictive avec peu de pannes]], [[RUL par apprentissage profond]], [[LSTM et réseaux récurrents]], [[Jeux de données PHM]].
