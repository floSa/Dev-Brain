---
role: notion
nom: Apprentissage semi-supervisé
alias: [Semi-supervised learning, SSL, apprentissage semi supervisé, peu d'étiquettes, données non étiquetées, auto-apprentissage, self-training, pseudo-étiquettes, pseudo-labels, pseudo-labeling, régularisation par cohérence, consistency regularization, Mean Teacher, FixMatch, propagation de labels, label propagation, label spreading, hypothèse de cluster, hypothèse de la variété, apprentissage transductif]
categorie: ml/socle
domaines: [data-sci, ml-eng]
tags: [supervised, unsupervised]
---

# Apprentissage semi-supervisé

## Aperçu

- Situation : **quelques exemples étiquetés**, **beaucoup d'exemples bruts**. L'apprentissage semi-supervisé (SSL) fait servir les deux dans un même entraînement : les étiquettes fixent la tâche, les données brutes renseignent sur la forme de la distribution des entrées.
- Le non-étiqueté n'aide que si la **connaissance de $p(x)$ renseigne sur $p(y\mid x)$** (Chapelle, Schölkopf, Zien, 2006, chap. 1). Sinon il n'apporte rien, et il peut dégrader la prédiction en la « guidant mal ». Tout le sujet tient dans cette condition, et dans les **hypothèses** qui la rendent vraie.
- À distinguer de l'[[Apprentissage auto-supervisé en vision|auto-supervisé]] : il n'y a là **aucune** étiquette, la tâche d'entraînement est fabriquée à partir des données ; ici les étiquettes existent mais sont rares, et on s'en sert.
- Les méthodes profondes de 2017-2020 (Mean Teacher, FixMatch) ont donné des chiffres spectaculaires avec 40 à 4 000 étiquettes sur CIFAR-10. Leurs critiques (Oliver et al., 2018) et les travaux de 2025 sur les modèles de fondation relativisent l'intérêt pratique : un modèle pré-entraîné suivi d'un fine-tuning avec peu d'étiquettes rivalise souvent.

## Concepts clés

### Les trois hypothèses
Chapelle, Schölkopf et Zien (2006, §1.2) les énoncent, et chaque méthode en choisit une :
- **Lissage semi-supervisé** (*smoothness*) : si deux points proches sont dans une région de **haute densité**, leurs sorties sont proches.
- **Cluster** : des points d'un même cluster ont probablement la même classe. Elle équivaut à la **séparation par basse densité** : la frontière de décision passe dans une région peu peuplée. Elle n'implique pas qu'une classe forme un seul cluster compact.
- **Variété** (*manifold*) : les données de grande dimension sont à peu près sur une variété de petite dimension. Cela évite la malédiction de la dimension et justifie les distances le long de la variété.
- **Quand elles échouent** : si les classes se recouvrent dans une région dense, ou si le non-étiqueté vient d'une autre distribution que l'étiqueté, la frontière est repoussée au mauvais endroit. Le chapitre 1 renvoie au chapitre 4 (Cozman et Cohen) sur la dégradation de performance des classifieurs génératifs ; ce chapitre n'a pas été lu ici.

### Inductif ou transductif
- Un algorithme **inductif** apprend une fonction définie sur tout l'espace d'entrée ; un algorithme **transductif** prédit seulement les étiquettes des points de test fournis.
- Le livre de 2006 insiste : la **transduction n'est pas le SSL**. Certains algorithmes SSL sont transductifs (propagation de labels), d'autres inductifs (Mean Teacher, FixMatch). Il ajoute que le benchmark du chapitre 21 ne montre pas d'avantage systématique de la transduction.

### Auto-apprentissage et pseudo-étiquettes
- **Principe** : entraîner sur les exemples étiquetés, prédire les non étiquetés, **ajouter les prédictions les plus sûres** comme étiquettes, recommencer. C'est la plus ancienne idée du domaine (Scudder 1965, Fralick 1967, Agrawala 1970, cités par le livre).
- **Limite lue dans le livre** : avec une minimisation du risque empirique et une perte 0-1, les données non étiquetées n'ont **aucun effet** ; avec une méthode à marge, la frontière est repoussée des points non étiquetés ; autrement, on ne sait pas quelle hypothèse l'algorithme met en œuvre.
- **Biais de confirmation** : le modèle apprend de ses propres erreurs. Tarvainen et Valpola (2017) nomment le risque.
- **Seuil de confiance** : ne retenir qu'une pseudo-étiquette dont la probabilité dépasse un seuil. La fiabilité du seuil dépend de la [[Calibration|calibration]] du modèle ; la documentation de scikit-learn le dit en une ligne pour son `SelfTrainingClassifier`.
- La version profonde est **Pseudo-Label** (Lee, 2013). L'article n'a pas pu être ouvert ; il est décrit ici d'après FixMatch, qui le présente comme un argmax avec seuil, lié à la minimisation d'entropie.

### Cohérence : Mean Teacher
- **Idée** : le modèle doit prédire la même chose sur **deux versions bruitées** de la même entrée. Aucune étiquette n'est nécessaire pour mesurer ce désaccord, donc on le mesure sur les données non étiquetées.
- **Mean Teacher** (Tarvainen et Valpola, NeurIPS 2017) : le « professeur » a pour poids la **moyenne exponentielle** des poids de l'étudiant. La perte de cohérence est l'erreur quadratique entre les prédictions de l'étudiant et du professeur. $\alpha = 0{,}99$ pendant la montée en charge, $0{,}999$ ensuite ; le poids de la cohérence monte de zéro sur les 80 premières époques.
- **Ce que le papier annonce** : 4,35 % d'erreur sur SVHN avec 250 étiquettes (contre un Temporal Ensembling entraîné avec 1 000), 12,31 % sur CIFAR-10 à 4 000 étiquettes avec un réseau convolutif à 13 couches (6,28 % avec un ResNet).
- **Limites écrites dans le papier** : le Π-model continue de progresser plus longtemps sur SVHN à 500 étiquettes ; VAT fait mieux à 1 000 étiquettes sur SVHN et à 4 000 sur CIFAR-10.

### FixMatch : cohérence et seuil
- **Procédé** (Sohn et al., NeurIPS 2020) : une vue **faiblement** augmentée produit la pseudo-étiquette (argmax) ; elle n'est gardée que si la confiance dépasse $\tau$ ; le modèle est entraîné à la prédire à partir d'une vue **fortement** augmentée (RandAugment ou CTAugment). Perte totale : $\ell_s + \lambda_u\,\ell_u$.
- **Réglages** : $\tau = 0{,}95$, $\lambda_u = 1$, $\mu = 7$ (rapport non étiqueté sur étiqueté dans un lot), lot de 64 étiquetés ; les mêmes pour tous les jeux sauf ImageNet. Le seuil règle un compromis qualité / quantité des pseudo-étiquettes : $0{,}95$ donne l'erreur la plus basse, un seuil trop bas coûte plus de 1,5 point.
- **Résultats annoncés** : 94,93 % de précision sur CIFAR-10 avec 250 étiquettes, 88,61 % avec 40 (quatre par classe). Tableau 2, erreur sur CIFAR-10 : $13{,}81 \pm 3{,}37$ (40 étiquettes, RandAugment), $5{,}07 \pm 0{,}65$ (250), $4{,}26 \pm 0{,}05$ (4 000).
- **Variance** : à quatre étiquettes par classe, l'écart-type vaut 3,35 point ; avec **une** étiquette par classe, la précision varie de 48,58 % à 85,32 % selon le tirage des étiquettes, médiane 64,28 %. Le résultat dépend de *quels* exemples sont étiquetés (voir [[Active learning]]).

### Propagation de labels
- **Principe** : construire un **graphe de similarité** sur tous les points, étiquetés ou non, et faire **diffuser** les étiquettes le long des arêtes. L'hypothèse mise en œuvre est celle de cohérence locale et globale : des voisins, et des points d'une même structure, partagent l'étiquette.
- **Version de Zhou et al.** (*Learning with Local and Global Consistency*, NIPS 2003) : matrice d'affinité gaussienne $W$ à diagonale nulle, $S = D^{-1/2} W D^{-1/2}$, itération $F^{(t+1)} = \alpha S F^{(t)} + (1-\alpha) Y$ avec $\alpha \in (0,1)$, qui converge vers $F^* = (1-\alpha)(I-\alpha S)^{-1} Y$.
- **Dans scikit-learn** : `LabelPropagation` (verrouillage **dur** des étiquettes connues, $\alpha = 0$) et `LabelSpreading` (verrouillage relâché) ; les points non étiquetés portent la valeur `-1` dans `y`.
- C'est un algorithme **transductif** : ajouter un point exige de recalculer ou d'étendre le graphe.

## Critiques : ce que les benchmarks cachaient

- **Oliver, Odena, Raffel, Cubuk, Goodfellow (NeurIPS 2018, *Realistic evaluation of deep semi-supervised learning algorithms*)** : après une réimplémentation unifiée, 1 000 essais d'optimisation d'hyperparamètres pour la baseline comme pour chaque méthode, trois constats : les **baselines supervisées sont sous-déclarées** ; les méthodes diffèrent par leur sensibilité à la quantité d'étiquettes et de non-étiqueté ; la performance peut **chuter nettement quand le non-étiqueté contient des classes absentes de l'étiqueté**.
- **Baselines** : les deux papiers qui précèdent rapportent des baselines différant jusqu'à 15 % pour le même modèle. Sur CIFAR-10 à 4 000 étiquettes, leur supervisé donne $20{,}26 \pm 0{,}38$ % d'erreur ; Mean Teacher $15{,}87 \pm 0{,}28$ ; Pseudo-Label $17{,}78 \pm 0{,}57$ ; VAT avec minimisation d'entropie $13{,}13 \pm 0{,}39$. Un Shake-Shake bien régularisé **sans** non-étiqueté fait 13,4 %, proche du meilleur SSL.
- **Transfert** : un pré-entraînement sur ImageNet en 32×32 suivi d'un fine-tuning sur 4 000 étiquettes de CIFAR-10 donne 12,09 %, mieux que tout SSL de leur étude.
- **Validation** : la validation de SVHN fait environ 7 000 exemples, plus de sept fois les 1 000 étiquettes d'entraînement ; régler sur une telle validation n'est pas réaliste.
- **Désaccord laissé tel quel sur Mean Teacher** : 12,31 % à 4 000 étiquettes dans son papier (réseau à 13 couches), 15,87 % chez Oliver et al., 9,19 % dans le tableau de FixMatch (WRN-28-2, même code pour toutes les méthodes). Architectures, réglages et validation diffèrent ; les chiffres d'un papier à l'autre ne se comparent pas.

## Depuis les modèles de fondation (2025-2026)

- **Zhang, Mai, Nguyen, Chao (NeurIPS 2025, arXiv 2503.09707)** : sur six jeux du benchmark VTAB, où des modèles de vision figés sont faibles, le **fine-tuning étiqueté seul** avec adaptation paramétriquement économe atteint ou dépasse FixMatch, FlexMatch et SoftMatch. Les auteurs rapprochent leur conclusion de celle d'Oliver et al. (2018). Ils proposent V-PET : un **ensemble de pseudo-étiquettes** issues de plusieurs adaptations et de plusieurs backbones (CLIP, DINOv2), sans filtrage par seuil.
- **Lv, Zhu, Wei, Li, Guo (arXiv 2505.13317, v4 du 26 octobre 2025, préprint en relecture)** : thèse que le SSL a rencontré son Waterloo face aux modèles pré-entraînés. Nuances écrites dans le texte : sur CIFAR en 32×32, FixMatch bat CLIP en zero-shot (un biais d'adaptation) ; sur STL-10 (96×96), CLIP en zero-shot dépasse les meilleurs SSL ; sur ImageNet, des modèles vision-langage dépassent 73 % avec 2 % d'étiquettes, quand FixMatch en utilise environ 10 % et reste derrière. Texte lu partiellement.
- **Les deux travaux ne tranchent pas pareil** : le premier garde un rôle aux pseudo-étiquettes (en ensemble), le second voit le SSL classique battu hors petite résolution. Désaccord laissé tel quel.
- **Résumés seulement (non vérifiés au texte)** : CoVar (Liu, He, Liu, arXiv 2601.11670, 2026) soutient que la confiance maximale seule échoue sous sur-confiance et déséquilibre de classes, et propose de lui adjoindre la variance résiduelle des classes non cibles, sans seuil à régler.

## Les maths, simplement

- Objectif général : une perte supervisée sur les $n_l$ exemples étiquetés, plus une perte non supervisée pondérée sur les $n_u$ exemples bruts :
  $$\mathcal{L} = \frac{1}{n_l}\sum_{i=1}^{n_l} \ell_s\big(f(x_i), y_i\big) + \lambda\,\frac{1}{n_u}\sum_{j=1}^{n_u} \ell_u(x_j)$$
- Mean Teacher : poids du professeur $\theta'_t = \alpha\,\theta'_{t-1} + (1-\alpha)\,\theta_t$ ; cohérence $\ell_u = \mathbb{E}\,\lVert f(x;\theta,\eta) - f(x;\theta',\eta')\rVert^2$, où $\eta$ et $\eta'$ sont deux bruits indépendants.
- FixMatch : $\ell_u = \frac{1}{\mu B}\sum_b \mathbb{1}\big[\max q_b \ge \tau\big]\; H\big(\arg\max q_b,\; p(y \mid \mathcal{A}(u_b))\big)$, où $q_b$ est la prédiction sur la vue faible, $\mathcal{A}$ l'augmentation forte et $H$ l'entropie croisée.
- Propagation de labels : $F^* = (1-\alpha)(I-\alpha S)^{-1} Y$ ; $\alpha$ proche de 1 laisse l'information voyager loin, $\alpha$ proche de 0 colle aux étiquettes initiales.

## En pratique

- **D'abord une baseline supervisée sérieusement réglée** : c'est la première leçon d'Oliver et al. Un gain de SSL mesuré contre une baseline sous-réglée ne prouve rien.
- **Un modèle pré-entraîné existe pour la modalité ?** L'ajuster avec peu d'étiquettes (voir [[Transfer learning vision]], [[Méta-apprentissage et few-shot learning]]) avant tout SSL. C'est l'enseignement de Zhang et al. et de Lv et al.
- **Le non-étiqueté doit venir de la même distribution** que l'étiqueté : des classes absentes de l'étiqueté peuvent faire **pire** que ne pas utiliser de non-étiqueté (Oliver et al.).
- **Valider honnêtement** : une validation de taille comparable à l'étiqueté, les étiquettes tirées du même pool que le non-étiqueté, et jamais de fuite des exemples de validation vers les pseudo-étiquettes (voir [[Data leakage]]).
- **Étiqueter peu mais bien** : si l'annotation est possible à petite échelle, choisir *quoi* étiqueter pèse autant que la méthode ([[Active learning]], [[Annotation de données]]).
- **Classes déséquilibrées** : CoVar (résumé lu seulement) relève que la confiance maximale seule échoue sous déséquilibre de classes ; voir [[Imbalanced classification]].
- **Outils** : [[Scikit-Learn]] fournit `SelfTrainingClassifier`, `LabelPropagation` et `LabelSpreading` (documentation de la version 1.9.1) ; les méthodes profondes s'écrivent dans un framework d'entraînement comme [[PyTorch]].

## Approches voisines & alternatives

- [[Apprentissage supervisé]] — le cas où toutes les étiquettes existent ; c'est la baseline à battre.
- [[Apprentissage non supervisé]] — aucune étiquette ; le SSL en emprunte les hypothèses (cluster, variété).
- [[Apprentissage auto-supervisé en vision]] — pré-entraîner sans étiquette sur la tâche, puis ajuster avec peu d'étiquettes ; alternative directe quand beaucoup de données brutes existent.
- [[Apprentissage contrastif]] — la perte qui construit les représentations de l'auto-supervisé.
- [[Active learning]] — choisir les exemples à étiqueter, au lieu de tirer parti de ceux qu'on n'étiquette pas ; les deux se combinent.
- [[Annotation de données]] — produire les étiquettes : coût, accord entre annotateurs, pré-annotation.
- [[Méta-apprentissage et few-shot learning]] et [[Transfer learning vision]] — le chemin « modèle pré-entraîné » qui rivalise avec le SSL quand les étiquettes sont rares.
- [[Distillation]] — la cohérence entre un professeur et un étudiant en est proche ; ici le professeur est la moyenne exponentielle de l'étudiant.
- [[Synthetic data generation]] — fabriquer des exemples au lieu d'exploiter des exemples bruts.
- [[Calibration]] et [[Imbalanced classification]] — conditions de fiabilité d'un seuil de pseudo-étiquette.
- [[Régularisation]] — la perte de cohérence agit comme une régularisation : elle pénalise une sortie instable au bruit.
- [[Scikit-Learn]] — `semi_supervised` : auto-apprentissage et propagation de labels.

## Pour aller plus loin

- Chapelle, Schölkopf & Zien (éd.) (2006) — [*Semi-Supervised Learning*](https://www.molgen.mpg.de/3659531/MITPress--SemiSupervised-Learning.pdf), MIT Press (volume collectif ; seul le chapitre 1 a été lu).
- Tarvainen & Valpola (2017) — [*Mean teachers are better role models*](https://arxiv.org/abs/1703.01780), NeurIPS 2017.
- Sohn et al. (2020) — [*FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence*](https://arxiv.org/abs/2001.07685), NeurIPS 2020.
- Oliver, Odena, Raffel, Cubuk & Goodfellow (2018) — [*Realistic Evaluation of Deep Semi-Supervised Learning Algorithms*](https://arxiv.org/abs/1804.09170), NeurIPS 2018.
- Zhou, Bousquet, Lal, Weston & Schölkopf (2003) — [*Learning with Local and Global Consistency*](https://proceedings.neurips.cc/paper/2003/file/87682805257e619d49b8e0dfdc14affa-Paper.pdf), NIPS 2003.
- Zhang, Mai, Nguyen & Chao (2025) — [*Revisiting semi-supervised learning in the era of foundation models*](https://arxiv.org/abs/2503.09707), NeurIPS 2025 ; Lv, Zhu, Wei, Li & Guo (2025) — [*Unlabeled Data vs. Pre-trained Knowledge*](https://arxiv.org/abs/2505.13317).
- Documentation scikit-learn — [*1.14 Semi-supervised learning*](https://scikit-learn.org/stable/modules/semi_supervised.html).
- Non ouvert : Lee (2013), *Pseudo-Label*, atelier ICML ; Zhu & Ghahramani (2002), propagation de labels.
