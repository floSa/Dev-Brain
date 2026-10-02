---
role: notion
nom: Méta-apprentissage et few-shot learning
alias: [Méta-apprentissage, meta-learning, learning to learn, apprendre à apprendre, few-shot learning, apprentissage à partir de peu d'exemples, one-shot learning, MAML, Reptile, réseaux prototypiques, prototypical networks, matching networks, apprentissage en contexte, in-context learning, épisodes, N-way K-shot]
categorie: ml/apprentissage-profond
domaines: [ml-eng, ai-eng]
tags: [transfer-learning, deep-learning, llm]
---

# Méta-apprentissage et few-shot learning

## Aperçu

- Le **few-shot learning** pose un problème : apprendre une nouvelle tâche (souvent une classification à $N$ classes) à partir de **$K$ exemples par classe**, avec $K$ de l'ordre de 1 à 5. Le **méta-apprentissage** (« apprendre à apprendre ») est une famille de réponses : entraîner un modèle **sur une distribution de tâches**, pour qu'il s'adapte vite à une tâche nouvelle.
- Trois méthodes classiques : **MAML** (Finn et al., 2017, apprendre une initialisation qu'un ou quelques pas de gradient suffisent à adapter), les **réseaux prototypiques** (Snell et al., 2017) et les **matching networks** (Vinyals et al., 2016), qui classent par distance dans un espace d'embedding appris.
- Le sujet a changé de nature avec les grands modèles de langage : Brown et al. (2020) décrivent l'**apprentissage en contexte** de GPT-3 comme une forme de méta-apprentissage dont le pré-entraînement est la boucle externe. Les critiques (2019-2020) ont montré, de leur côté, qu'un simple bon embedding pré-entraîné rivalise avec les méthodes dédiées.

## Concepts clés

### Épisodes : s'entraîner comme on sera testé
- Un **épisode** est une mini-tâche : un **support** ($N$ classes, $K$ exemples chacune) et une **requête** à classer. On entraîne sur des milliers d'épisodes tirés de classes d'entraînement, on teste sur des épisodes de classes **jamais vues**.
- Principe de Vinyals et al. (2016) : les conditions d'entraînement doivent refléter celles du test (« test and train conditions must match »). C'est ce qui justifie l'entraînement par épisodes, et le protocole $N$-way $K$-shot.
- Snell et al. relèvent que choisir un nombre de classes ($N$) plus élevé à l'entraînement qu'au test donne l'avantage, et que le nombre d'exemples ($K$) gagne à rester le même.

### MAML : une initialisation qui s'adapte vite
- **Boucle interne** : un ou quelques pas de gradient sur le support d'une tâche, qui donnent des paramètres adaptés $\theta'$. **Boucle externe** : une descente de gradient sur $\theta$, avec la perte de la requête évaluée **en $\theta'$**. L'algorithme est « agnostique au modèle » : tout modèle entraîné par descente de gradient convient.
- Le méta-gradient **traverse** le pas de gradient : il demande des dérivées secondes (produits hessienne-vecteur, voir [[Rétropropagation et différentiation automatique]]). Finn et al. testent une **version premier ordre** qui les omet.
- **Les sources divergent sur ce que le premier ordre coûte.** Finn et al. : sur miniImageNet, la version premier ordre est « presque identique » (1-shot, 5 classes : 48,07 contre 48,70 ; 5-shot : 63,15 contre 63,11) pour environ 33 % de calcul en moins. Nichol et al. (2018) jugent que MAML, le premier ordre et Reptile ont des performances « très similaires » ; pourtant leur tableau Omniglot, où le premier ordre vient du code de Finn avec les mêmes hyperparamètres, donne 95,8 % pour MAML et **89,4 % pour le premier ordre** en 20 classes, 1-shot. L'équivalence dépend donc du jeu et du réglage.
- **Reptile** (Nichol et al., 2018) : après $k$ pas de SGD sur une tâche, déplacer $\theta$ vers les paramètres obtenus, $\theta \leftarrow \theta + \epsilon(\phi - \theta)$. Pas de dérivée seconde. Leur analyse de Taylor montre que MAML, sa version premier ordre et Reptile contiennent les mêmes termes (apprentissage joint, et maximisation du produit scalaire entre gradients de lots différents), dans des proportions différentes.

### Réseaux prototypiques et matching networks : méta-apprendre une distance
- **Réseaux prototypiques** : le prototype d'une classe est la **moyenne des embeddings** de ses exemples de support ; on classe par softmax sur les distances aux prototypes. Justification des auteurs : pour une divergence de Bregman régulière, la moyenne est le meilleur représentant d'un groupe ; la distance euclidienne au carré fait nettement mieux que le cosinus.
- **Matching networks** : un classifieur par attention sur le support, avec des embeddings qui tiennent compte de tout le support (*full context embeddings*).
- Dans les deux cas, ce qui est méta-appris est un **espace d'embedding** ; la tâche nouvelle se résout **sans mise à jour de poids**, par comparaison. Les pertes par paires et triplets de [[Metric learning & ré-identification]] et les pertes de [[Apprentissage contrastif]] sont de la même famille.

### Apprentissage en contexte : le méta-apprentissage des grands modèles
- Brown et al. (2020, GPT-3, 175 milliards de paramètres) : l'**apprentissage en contexte** consiste à mettre $K$ démonstrations dans le prompt, **sans aucune mise à jour de gradient** ; $K$ va jusqu'à ce que la fenêtre de contexte le permette (2048 jetons ; « typiquement 10 à 100 »). Zero-shot = instruction seule ; one-shot = une démonstration ; few-shot = plusieurs.
- Le papier emploie le mot : l'apprentissage en contexte est « la boucle interne » d'une structure interne/externe, le pré-entraînement non supervisé étant la boucle externe. Mais les auteurs écrivent aussi qu'ils ignorent si le modèle **apprend la tâche** à l'inférence ou **reconnaît** une tâche vue à l'entraînement : ils y voient un spectre, variable selon la tâche.
- Résultats few-shot de GPT-3 (zero / one / few) : TriviaQA 64,3 / 68,0 / 71,2 % ; LAMBADA 76,2 / 72,5 / 86,4 %.

### Apprentissage en contexte : apprentissage ou reconnaissance ?
- **Du côté « reconnaissance »** : Min et al. (2022) montrent que remplacer les étiquettes des démonstrations par des étiquettes aléatoires **ne dégrade que marginalement** les performances sur plusieurs tâches de classification et de choix multiple, avec 12 modèles dont GPT-3. Ce qui compte : l'espace des étiquettes, la distribution des entrées, le format.
- **Du côté « apprentissage »** : Garg et al. (2022) entraînent de zéro un Transformer (12 couches, 8 têtes) à apprendre **en contexte** des fonctions (linéaires, parcimonieuses, réseaux à 2 couches, arbres de profondeur 4), avec une performance comparable aux moindres carrés pour le linéaire ; ils parlent d'une instance de méta-apprentissage. Von Oswald et al. (2023) **construisent** explicitement les poids d'une couche d'auto-attention **linéaire** dont la mise à jour est identique à un pas de descente de gradient sur une perte quadratique ; des Transformers à attention linéaire entraînés sur de la régression convergent vers cette construction ou s'en approchent. Limite écrite : une couche softmax seule n'y arrive pas. Akyürek et al. (2023) : un Transformer peut implémenter descente de gradient et régression ridge, et ses prédictions passent de l'un à l'autre selon la profondeur et le bruit.
- **Les deux familles ne testent pas les mêmes objets** (classification de langage naturel avec un modèle pré-entraîné contre régression synthétique avec entraînement de zéro) ; aucune des sources lues ne les réconcilie. Désaccord laissé tel quel.

### Méta-entraîner un modèle de langage
- Ici le méta-apprentissage **survit**, sous forme d'un entraînement multi-tâches à lire des démonstrations. **MetaICL** (Min et al., 2022) : 142 jeux de données, 52 tâches cibles, base GPT-2 Large (770 M) ; il égale ou bat GPT-J, huit fois plus gros, et approche parfois le fine-tuning complet ; la diversité des tâches d'entraînement est déterminante. Chen et al. (2022, *in-context tuning*) : méta-entraîner un modèle à prédire l'étiquette à partir d'exemples en contexte ; ils annoncent un gain sur MAML premier ordre et sur l'apprentissage en contexte brut.

## Critiques : ce qu'un bon embedding suffit à faire

- **Chen et al. (2019, ICLR)** : une base line à classifieur par distance (*Baseline++*) rivalise avec les méthodes de méta-apprentissage ; l'écart entre méthodes se réduit à mesure que le backbone devient profond. Sur miniImageNet 5 classes, backbone Conv-4, 1-shot / 5-shot : Baseline++ 48,24 / 66,43 ; ProtoNet 44,42 / 64,24 ; MAML 46,47 / 62,71 ; MatchingNet 48,14 / 63,48.
- **Tian et al. (2020)** : un embedding **supervisé** pré-entraîné sur toutes les classes d'entraînement, suivi d'une régression logistique, bat l'état de l'art d'alors (ResNet-12 : 62,02 / 79,64 ; avec auto-distillation : 64,82 / 82,14).
- **Raghu et al. (2020, ICLR)** : l'efficacité de MAML vient surtout de la **réutilisation de caractéristiques** (*feature reuse*), pas d'une adaptation rapide. Geler le corps du réseau change à peine la précision ; ANIL, qui n'adapte que la **tête**, égale MAML (46,7 contre 46,9) avec un entraînement 1,7 fois plus rapide par itération et une inférence 4,1 fois plus rapide ; une variante sans boucle interne (NIL) fait 48,0.
- **Hospedales et al. (2021)**, une revue : taxonomie en méta-représentation, méta-objectif et méta-optimiseur, sur une formulation à deux niveaux.

### Ce qui a survécu, ce qui a été dépassé
- **Dépassé** (d'après Chen, Tian, Raghu) : l'idée qu'une boucle de méta-optimisation est nécessaire pour la classification en peu d'exemples. Un backbone bien pré-entraîné et un classifieur simple rivalisent ; c'est la même logique que le [[Transfer learning vision|transfert]].
- **Survit** : le protocole d'évaluation en épisodes ($N$-way $K$-shot), la classification par prototype ou par distance dans un espace d'embedding appris, et le méta-entraînement multi-tâches d'un modèle de langage (MetaICL).
- **Déplacé** : l'adaptation à partir de $K$ exemples se fait désormais, pour un grand modèle de langage, **dans le prompt**, sans mise à jour de poids. Travaux récents, lus par leur résumé seulement : Dragutinović, Saxe et Singh (2025) analysent des Transformers softmax comme faisant de la descente de gradient dans un espace de caractéristiques noyau, avec un taux d'apprentissage adaptatif au contexte ; Ghosh et al. (2026) comparent fine-tuning et apprentissage en contexte (le fine-tuning est meilleur en distribution, les deux sont équivalents hors distribution, l'apprentissage en contexte plus sensible à la taille du modèle).

## Les maths, simplement

- MAML, pour une tâche $\mathcal{T}_i$ de perte $\mathcal{L}_i$ et un pas interne $\alpha$ :
  $$\theta_i' = \theta - \alpha\,\nabla_\theta \mathcal{L}_i(\theta), \qquad \min_\theta \sum_i \mathcal{L}_i(\theta_i')$$
- Le gradient externe contient $\partial\theta_i'/\partial\theta = I - \alpha\,\nabla^2_\theta\mathcal{L}_i(\theta)$ : c'est la dérivée seconde. La version **premier ordre** le remplace par $I$.
- Prototype de la classe $k$ : $c_k = \frac{1}{|S_k|}\sum_{x_i \in S_k} f_\phi(x_i)$ ; probabilité $p(y=k \mid x) \propto \exp\!\big(-d(f_\phi(x), c_k)\big)$.
- Apprentissage en contexte : $p(y \mid x,\ (x_1, y_1), \dots, (x_K, y_K))$ avec **$\theta$ figé** ; seul le contexte change.

## En pratique

- **Peu d'exemples, une modalité bien couverte par un modèle pré-entraîné** : partir d'un encodeur pré-entraîné et poser une tête simple (logistique, prototypes) avant d'envisager le méta-apprentissage. C'est l'enseignement de Chen et de Tian.
- **Texte** : [[SetFit]] fait du few-shot sans prompt par fine-tuning contrastif d'un sentence-transformer ; ou quelques démonstrations dans le prompt d'un grand modèle de langage ([[Prompt engineering]]).
- **Évaluer** : tirer des épisodes de classes **absentes** de l'entraînement, rapporter la moyenne et l'intervalle de confiance sur de nombreux épisodes (les tableaux des articles cités donnent des moyennes avec un intervalle de confiance).
- **Méta-apprentissage à deux niveaux** : coût en mémoire et en temps de la boucle interne (dérivées secondes) ; Reptile ou le premier ordre allègent, au prix d'écarts qui dépendent du jeu de données.
- Les démonstrations en contexte ne portent pas toutes la même information : s'attendre à ce que le **format** et la **distribution des entrées** comptent autant que la justesse des étiquettes (Min et al.).

## Approches voisines & alternatives

- [[Transfer learning vision]] — le concurrent qui a rattrapé le méta-apprentissage en classification few-shot.
- [[Metric learning & ré-identification]] — apprendre un espace où la distance reflète la similarité ; les réseaux prototypiques en sont un cas.
- [[Apprentissage contrastif]] — mêmes pertes pour construire l'espace d'embedding sur lequel on classe ensuite par prototype.
- [[Rétropropagation et différentiation automatique]] — MAML différencie à travers une mise à jour de gradient : le second ordre en usage.
- [[Gradient descent]] — la boucle interne de MAML est un pas de descente.
- [[Prompt engineering]] et [[Chain-of-Thought]] — l'apprentissage en contexte côté pratique, exemples dans le prompt.
- [[Transformer architectures]] et [[Self-attention]] — les mécanismes dont l'apprentissage en contexte est étudié (équivalence avec un pas de descente pour l'attention linéaire).
- [[Distillation]] — l'auto-distillation ajoute 2 à 3 points chez Tian et al.
- [[Régularisation]] — avec peu de données, un biais inductif simple (distance, prototype) est la contrainte qui compte (Snell et al.).
- [[SetFit]] — few-shot sur texte par fine-tuning contrastif.
- [[sentence-transformers]] — l'encodeur qui sert d'embedding pour ces approches côté texte.
- [[PyTorch]] et [[JAX]] — `backward(create_graph=True)` d'un côté, `grad` appliqué à sa propre sortie de l'autre : les deux permettent de différencier à travers une mise à jour de gradient.

## Pour aller plus loin

- Finn, Abbeel & Levine (2017) — [*Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks*](https://arxiv.org/abs/1703.03400), ICML 2017.
- Nichol, Achiam & Schulman (2018) — [*On First-Order Meta-Learning Algorithms*](https://arxiv.org/abs/1803.02999) (rapport OpenAI).
- Snell, Swersky & Zemel (2017) — [*Prototypical Networks for Few-shot Learning*](https://arxiv.org/abs/1703.05175) ; Vinyals et al. (2016) — [*Matching Networks for One Shot Learning*](https://arxiv.org/abs/1606.04080).
- Brown et al. (2020) — [*Language Models are Few-Shot Learners*](https://arxiv.org/abs/2005.14165).
- Chen, Liu, Kira, Wang & Huang (2019) — [*A Closer Look at Few-shot Classification*](https://arxiv.org/abs/1904.04232), ICLR 2019 ; Tian et al. (2020) — [*Rethinking Few-Shot Image Classification: a Good Embedding Is All You Need?*](https://arxiv.org/abs/2003.11539) ; Raghu et al. (2020) — [*Rapid Learning or Feature Reuse?*](https://arxiv.org/abs/1909.09157), ICLR 2020.
- Hospedales, Antoniou, Micaelli & Storkey (2021) — [*Meta-Learning in Neural Networks: A Survey*](https://arxiv.org/abs/2004.05439).
- Garg, Tsipras, Liang & Valiant (2022) — [*What Can Transformers Learn In-Context?*](https://arxiv.org/abs/2208.01066) ; von Oswald et al. (2023) — [*Transformers learn in-context by gradient descent*](https://arxiv.org/abs/2212.07677), ICML 2023 ; Akyürek et al. (2023) — [*What learning algorithm is in-context learning?*](https://arxiv.org/abs/2211.15661), ICLR 2023.
- Min et al. (2022) — [*Rethinking the Role of Demonstrations*](https://arxiv.org/abs/2202.12837) ; Min et al. (2022) — [*MetaICL*](https://arxiv.org/abs/2110.15943) ; Chen et al. (2022) — [*Meta-learning via Language Model In-context Tuning*](https://arxiv.org/abs/2110.07814).
