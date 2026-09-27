---
role: notion
nom: Active learning
alias: [Apprentissage actif, active learning, apprentissage actif profond, deep active learning, échantillonnage par incertitude, uncertainty sampling, query by committee, requête par comité, pool-based sampling, sélection d'exemples à étiqueter, core-set, BADGE, BALD, TypiClust, démarrage à froid en apprentissage actif, oracle d'annotation]
categorie: ml/annotation
domaines: [data-sci, ml-eng]
tags: [annotation, human-in-the-loop, supervised]
---

# Active learning

## Aperçu

- L'**active learning** (apprentissage actif) laisse l'algorithme **choisir les exemples à faire étiqueter** par un oracle, en général un annotateur, plutôt que d'étiqueter au hasard. Il vise la meilleure précision pour un **budget d'étiquettes** donné (Settles, 2009). [[Annotation de données]] en donne la définition et le piège principal (un jeu construit par incertitude n'est pas représentatif) ; cette page porte les **stratégies**, la version profonde et les **critiques**.
- Le choix se fait à partir de ce que le modèle sait déjà : où il hésite, où ses modèles voisins se contredisent, quelles zones de l'espace ne sont pas couvertes.
- Le sujet est en tension. Settles note que la majorité des résultats publiés montrent une réduction du nombre d'étiquettes, et admet un **biais de publication**. En apprentissage profond, plusieurs études de reproduction trouvent un gain **faible, instable ou nul** face à un tirage aléatoire bien réglé. Désaccord laissé tel quel (section *Critiques*).
- Différence avec l'[[Apprentissage semi-supervisé]] : le semi-supervisé **exploite** les exemples qu'on n'étiquette pas ; l'active learning **choisit** ceux qu'on étiquette. Les deux se combinent.

## Concepts clés

### Trois scénarios (Settles, §2)
- **Synthèse de requêtes** (*membership query synthesis*) : le modèle fabrique un exemple et le soumet à l'oracle.
- **Échantillonnage en flux** (*stream-based selective sampling*) : les exemples arrivent un par un, le modèle décide d'en demander l'étiquette ou non.
- **Échantillonnage sur un lot** (*pool-based*) : un grand lot d'exemples bruts existe, le modèle les classe selon un critère et demande les meilleurs. C'est la situation de qui possède un lot de données non étiquetées.

### Stratégies par incertitude
- **Idée** : demander l'étiquette de l'exemple où le modèle est le moins sûr. Trois mesures : **étiquette la moins sûre** (probabilité de la classe prédite la plus basse), **marge** (écart entre les deux classes les plus probables), **entropie** de la distribution prédite (Settles, §3.1).
- **Piège** : les méthodes simples peuvent interroger des **valeurs aberrantes** (§3). Karamcheti et al. (plus bas) en donnent un cas : des exemples que le modèle n'apprend pas.
- **En profondeur** : Ren et al. (2021) notent que le softmax est **trop confiant**, ce qui fausse l'incertitude (voir [[Calibration]]). Gal, Islam et Ghahramani (ICML 2017) estiment l'incertitude par **dropout de Monte-Carlo** et acquièrent par **BALD** (information mutuelle entre la prédiction et les poids). Sur MNIST, le nombre d'images à acquérir pour atteindre 5 % d'erreur : BALD 335, variation ratios 295, entropie maximale 355, écart-type moyen 695, tirage aléatoire 835 (Table 1) ; pour 10 % d'erreur : 145, 120, 165, 230 et 255.

### Stratégies par comité
- **Query-by-committee** (Settles, §3.2) : plusieurs modèles entraînés sur les mêmes étiquettes ; on demande l'exemple sur lequel ils **divergent** le plus. Le désaccord remplace la probabilité comme mesure de doute.
- Autres critères de Settles : changement attendu du modèle (§3.3), réduction attendue de l'erreur (§3.4), réduction de variance (§3.5), méthodes **pondérées par la densité** (§3.6), qui évitent les aberrations en favorisant les zones peuplées.

### Diversité et sélection par lots
- **Pourquoi** : en profondeur, on annote **par lots** (réentraîner pour chaque étiquette est impraticable). Demander les k exemples les plus incertains revient à demander k variantes du même exemple.
- **Core-set** (Sener et Savarese, ICLR 2018) : choisir un sous-ensemble qui **représente la géométrie** de l'ensemble des données, avec une borne. Les auteurs écrivent que de nombreuses heuristiques de la littérature « ne sont pas efficaces » sur des CNN en mode lot, et que dans leurs expériences le tirage aléatoire bat l'incertitude bayésienne en lot, qu'ils attribuent à la corrélation entre les étiquettes demandées.
- **BADGE** (Ash et al., ICLR 2020) : échantillonner des points « disparates et de grande magnitude » dans l'espace des **gradients de la dernière couche** calculés avec l'étiquette prédite. La norme du gradient mesure l'incertitude, sa direction la diversité. Les auteurs affirment que les méthodes purement incertitude ou purement diversité sont irrégulières selon l'architecture, la taille de lot et le jeu de données, et que BADGE se comporte « aussi bien ou mieux » de façon constante ; aucun chiffre absolu n'a été relevé.
- **Taxonomie** de Ren et al. (2021, *ACM Computing Surveys* 54(9), 2022) : lot, incertitude et hybrides, bayésien profond, densité, conception automatisée. Le survey reconnaît lui-même que le tirage aléatoire est une **base solide** et que les résultats divergent d'une étude à l'autre.

### La boucle d'annotation et son coût
- **Boucle** : entraîner sur l'existant, évaluer le lot non étiqueté, demander un lot de requêtes, annoter, réentraîner, jusqu'au budget ou à un plateau.
- **Coût d'étiquetage variable** (Settles, §6.3) : réduire le **nombre** d'instances étiquetées ne garantit **pas** de baisser le **coût total**. Presque toute la littérature suppose un coût fixe et connu d'avance pour chaque annotation ; le coût réel varie.
- Le comptage du coût (temps, accord entre annotateurs, relecture) relève d'[[Annotation de données]].

### Biais d'échantillonnage
- Le jeu d'entraînement construit par un apprenant actif est **lié à la classe de modèle** qui a posé les requêtes : il suit une distribution biaisée, pas tirée de façon i.i.d. (Settles, §4.1).
- **Réutilisation** : le jeu peut-il servir à un autre modèle ? Settles (§6.6) rapporte deux avis opposés : Lewis et Catlett l'ont montré, Baldridge et Osborne ont constaté le contraire. Lowell, Lipton et Wallace (EMNLP 2019) trouvent qu'un modèle successeur entraîné sur un jeu acquis activement **ne bat pas systématiquement** un jeu i.i.d. Désaccord laissé tel quel.

### Démarrage à froid
- **Le problème** : l'incertitude d'un modèle presque sans étiquettes ne vaut rien. Hacohen, Dekel et Weinshall (ICML 2022) rappellent que les stratégies profondes exigent un grand jeu initial étiqueté, et qu'à petit budget le tirage aléatoire bat la plupart d'entre elles.
- **Leur théorie** : un comportement de type transition de phase. À **petit** budget, demander des exemples **typiques** ; à grand budget, des exemples **difficiles**, non représentatifs. **TypiClust** : pré-entraînement auto-supervisé, regroupement, choix d'un exemple typique par groupe. Avec 10 exemples ainsi choisis sur CIFAR-10 et une méthode semi-supervisée, 93,2 % de précision, soit 39,4 points de plus qu'une sélection aléatoire (abstract).
- **Contre-point** : Gupte et al. (TMLR, arXiv 2401.14555, 2024) avec DINOv2 ViT-g14 sur CIFAR100, Food101, ImageNet-100 et DomainNet : l'échantillonnage par incertitude est compétitif avec TypiClust dès la deuxième itération, et ils ne voient « aucune preuve d'une transition de phase ». Lu en extraits seulement. Le désaccord porte sur le point de départ : une représentation de fondation change le démarrage à froid.

## Critiques : l'efficacité réelle en apprentissage profond

- **Mittal, Tatarchenko, Çiçek, Brox (2019, arXiv 1912.05361, *Parting with illusions about deep active learning*)** : l'évaluation courante est jugée insuffisante. Sur CIFAR-10 **sans** augmentation, la meilleure méthode gagne 3,2 points sur le tirage aléatoire ; **avec** augmentation, toutes les méthodes sont dans une plage de 0,4 point. Sur CIFAR-100, 1,4 point sans augmentation. Couplées à du semi-supervisé, elles progressent beaucoup, sans guère faire mieux que l'aléatoire. À petit budget, certaines font **pire** que l'aléatoire.
- **Munjal, Hayat, Hayat, Sourati, Khan (CVPR 2022, *Towards robust and reproducible active learning using neural networks*)** : à conditions identiques, les méthodes d'incertitude, de diversité et de comité donnent un gain **incohérent** sur l'aléatoire ; avec une forte régularisation, marginal ou nul ; aucune méthode ne domine. Ils citent un écart d'environ 13 % entre deux articles pour le résultat de l'aléatoire à 20 % d'étiquettes sur CIFAR-10.
- **Beck, Sivasubramanian, Dani, Ramakrishnan, Iyer (2021, arXiv 2106.15324)** : à l'inverse, l'active learning est **2 à 4 fois** plus économe en étiquettes qu'un tirage aléatoire **avec** augmentation de données ; mais, avec augmentation, BADGE n'a plus de gain constant sur l'échantillonnage par incertitude simple. Venue (atelier ICML 2021) non confirmée.
- **Karamcheti, Krishna, Fei-Fei, Manning (ACL-IJCNLP 2021, VQA)** : huit méthodes, cinq modèles, quatre jeux : peu ou pas d'amélioration face à l'aléatoire, parfois pire. Cause identifiée : des **valeurs aberrantes collectives** (questions sur du texte dans les images, connaissances externes) que l'active learning préfère acquérir et que les modèles n'apprennent pas ; les retirer du lot augmente nettement l'efficacité.
- **Lowell, Lipton, Wallace (EMNLP 2019, *Practical obstacles to deploying active learning*)** : bénéfices non fiables entre modèles et tâches, rapport coût / gain « modeste et irrégulier ».
- **Lüth, Bungert, Klein, Jaeger (NeurIPS 2023)** : cinq pièges d'évaluation, un benchmark à grande échelle ; lu par son résumé seulement.
- **Les chiffres divergent selon le protocole** (pool, hyperparamètres, régularisation, augmentation) : Beck contre Mittal et Munjal en est la preuve. Désaccord laissé tel quel ; la leçon commune est qu'un résultat n'a de sens que contre un tirage aléatoire **réglé de la même façon**.
- **Critiques anciennes** (citées par Settles, §4.1) : Schein et Ungar (2007) montrent que l'active learning peut demander **plus** d'étiquettes que l'apprentissage passif ; Guo et Schuurmans (2008) trouvent que les stratégies standard appliquées en lot de façon myope sont souvent « bien pires » que l'échantillonnage aléatoire.

## Depuis 2025 : modèles de fondation et LLM comme annotateurs

- **Romberg, Schröder, Gonsior, Tomanek, Olsson (EACL 2026, arXiv 2503.09701, v4 du 2 février 2026)** : enquête auprès de praticiens du traitement du langage. Les obstacles persistent : complexité de mise en place, réduction de coût incertaine, outillage ; les auteurs notent qu'ils étaient déjà décrits il y a plus de quinze ans. Premier dépôt en mars 2025.
- **Résumés seulement (non vérifiés au texte)** : Zhang, Li, Zhang, Zhu (ICML 2026, arXiv 2606.07630) emploient des a priori de modèles de fondation face au déséquilibre de classes et annoncent plus de 50 % d'économie d'annotation face à la meilleure baseline active ; Qi et al. (arXiv 2601.15773, 2026) agrègent plusieurs LLM comme annotateurs dans la boucle et annoncent une performance comparable à l'annotation humaine ; Bayer, Lutz, Reuter (TACL 14, 2026, *ActiveLLM*) font choisir les exemples par un LLM en démarrage à froid.
- Aucun benchmark vérifié de la période sur ce dernier point : à lire comme des annonces.

## Les maths, simplement

- Score d'incertitude de l'exemple $x$, avec $\hat{y}$ la classe la plus probable et $\hat{y}'$ la deuxième :
  $$s_{\text{LC}}(x) = 1 - P(\hat{y}\mid x), \qquad s_{\text{marge}}(x) = P(\hat{y}\mid x) - P(\hat{y}'\mid x), \qquad s_{\text{ent}}(x) = -\sum_k P(y_k\mid x)\log P(y_k\mid x)$$
  On demande l'étiquette du plus fort $s_{\text{LC}}$ ou $s_{\text{ent}}$, du plus faible $s_{\text{marge}}$.
- **BALD** : $\mathbb{I}[y;\omega \mid x,\mathcal{D}] = \mathbb{H}[y \mid x,\mathcal{D}] - \mathbb{E}_{\omega}\,\mathbb{H}[y \mid x,\omega]$ : le désaccord entre tirages de poids, donc l'incertitude **épistémique** et non le bruit des données.
- **Core-set** : choisir $k$ centres minimisant la distance maximale d'un point au centre le plus proche (problème des $k$-centres, résolu par un algorithme glouton).
- **BADGE** : vecteur de gradient $g_x = \partial \ell(f(x), \hat{y}) / \partial \theta_{\text{sortie}}$ ; échantillonnage de type k-means++ sur ces vecteurs.

## En pratique

- **Toujours comparer à un tirage aléatoire, au même budget, avec les mêmes réglages et la même augmentation** : c'est la leçon commune de Mittal, Munjal et Beck. Sans cette comparaison, le gain n'est pas établi.
- **Avant la première requête** : un lot initial tiré au hasard, ou choisi par typicité (Hacohen) à partir d'un embedding pré-entraîné ([[Apprentissage auto-supervisé en vision]]). Ne pas se fier à l'incertitude d'un modèle presque sans étiquettes.
- **Annoter par lots**, et diversifier le lot (core-set, BADGE) au lieu de prendre les $k$ plus incertains.
- **Inspecter les exemples les plus incertains** avant de les envoyer : ce sont souvent des aberrations ou des cas ambigus que les annotateurs n'étiquetteront pas de façon fiable (Karamcheti et al.).
- **Garder un jeu de test tiré au hasard, à part** : le jeu acquis activement ne sert pas à évaluer (voir [[Annotation de données]] et [[Data leakage]]).
- **Les outils** : [[Label Studio]] réserve la boucle active **automatique** à l'édition Enterprise ; la Community se limite à trier les tâches à la main et à relire des prédictions. La documentation de [[CVAT]] lue pour sa fiche ne décrit pas de boucle active.
- **Classes déséquilibrées** : le lot de requêtes peut sur-représenter la classe rare ou l'ignorer ; voir [[Imbalanced classification]].

## Approches voisines & alternatives

- [[Annotation de données]] — la notion qui cadre l'étiquetage : tâches, guides, accord entre annotateurs, coût, pré-annotation.
- [[Apprentissage semi-supervisé]] — exploiter les exemples non étiquetés au lieu de choisir ceux qu'on étiquette ; complémentaire.
- [[Apprentissage auto-supervisé en vision]] — fournit l'embedding du démarrage à froid.
- [[Calibration]] — une incertitude fiable est la condition des stratégies par incertitude.
- [[Imbalanced classification]] — la classe rare et le biais d'échantillonnage.
- [[Data leakage]] — éviter que le jeu de requêtes contamine l'évaluation.
- [[Synthetic data generation]] — fabriquer des exemples au lieu de les faire étiqueter.
- [[Apprentissage supervisé]] — le régime dont l'active learning réduit le coût d'étiquetage.
- [[Label Studio]] — plateforme d'annotation : active learning automatique en Enterprise, tri manuel en Community.
- [[CVAT]] — annotation pour la vision ; pré-annotation par modèle, sans boucle active décrite dans sa fiche.

## Pour aller plus loin

- Settles (2009) — [*Active Learning Literature Survey*](https://burrsettles.com/pub/settles.activelearning.pdf), rapport technique 1648, Université du Wisconsin-Madison (version lue mise à jour le 26 janvier 2010).
- Ren et al. (2021) — [*A Survey of Deep Active Learning*](https://arxiv.org/abs/2009.00236), ACM Computing Surveys 54(9), 2022.
- Gal, Islam & Ghahramani (2017) — [*Deep Bayesian Active Learning with Image Data*](https://arxiv.org/abs/1703.02910), ICML 2017 ; Sener & Savarese (2018) — [*Active Learning for Convolutional Neural Networks: A Core-Set Approach*](https://arxiv.org/abs/1708.00489), ICLR 2018 ; Ash et al. (2020) — [*Deep Batch Active Learning by Diverse, Uncertain Gradient Lower Bounds*](https://arxiv.org/abs/1906.03671), ICLR 2020.
- Hacohen, Dekel & Weinshall (2022) — [*Active Learning on a Budget: Opposite Strategies Suit High and Low Budgets*](https://arxiv.org/abs/2202.02794), ICML 2022 ; Gupte et al. (2024) — [*Revisiting Active Learning in the Era of Vision Foundation Models*](https://arxiv.org/abs/2401.14555), TMLR.
- Critiques : Mittal et al. (2019) — [*Parting with Illusions about Deep Active Learning*](https://arxiv.org/abs/1912.05361) ; Munjal et al. (2022) — [*Towards Robust and Reproducible Active Learning Using Neural Networks*](https://arxiv.org/abs/2002.09564), CVPR 2022 ; Beck et al. (2021) — [*Effective Evaluation of Deep Active Learning on Image Classification Tasks*](https://arxiv.org/abs/2106.15324) ; Karamcheti et al. (2021) — [*Mind Your Outliers!*](https://arxiv.org/abs/2107.02331), ACL-IJCNLP 2021 ; Lowell, Lipton & Wallace (2019) — [*Practical Obstacles to Deploying Active Learning*](https://aclanthology.org/D19-1003/), EMNLP 2019 ; Lüth et al. (2023) — [*Navigating the Pitfalls of Active Learning Evaluation*](https://arxiv.org/abs/2301.10625), NeurIPS 2023 (résumé seulement).
- Romberg et al. (2026) — [*Reassessing Active Learning Adoption in Contemporary NLP: A Community Survey*](https://arxiv.org/abs/2503.09701), EACL 2026.
