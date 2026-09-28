---
role: notion
nom: Fusion de modèles
alias: [model merging, merge de modèles, model soups, soupe de modèles, Task Arithmetic, task vectors, TIES-Merging, DARE, SLERP, mergekit, frankenmerge, depth up-scaling, fusion de poids, weight averaging]
categorie: llm/finetuning
domaines: [ai-eng, ml-eng]
tags: [llm, fine-tuning, transfer-learning]
---

# Fusion de modèles

## Aperçu

- **Fusionner** des modèles : combiner les **poids** de plusieurs modèles de même architecture en un seul, sans gradient ni données d'entraînement. Le calcul est une opération sur tenseurs (moyenne, interpolation, somme de différences) ; le coût réel est l'**évaluation** de chaque candidat.
- Ce n'est ni un **ensemble** (un seul modèle tourne à l'inférence, pas N), ni une [[Distillation]] (aucun élève n'est entraîné), ni le simple rabattement d'un adaptateur LoRA dans les poids de base ([[LoRA et QLoRA]]), qui n'en est qu'un cas particulier.
- Usages documentés : moyenner des modèles ajustés avec d'autres hyperparamètres (*model soups*), additionner des compétences ajustées séparément (*task arithmetic*), assembler les experts d'un pipeline de post-entraînement (Command A, Olmo 3), empiler des couches (*depth up-scaling*), ou construire un MoE à partir de modèles denses.

## Concepts clés

### Pourquoi la moyenne de poids peut marcher

- **Même point de départ, même bassin.** Neyshabur, Sedghi, Zhang (NeurIPS 2020) observent qu'un modèle ajusté à partir de poids pré-entraînés reste dans le même bassin du paysage de perte ; Frankle et al. (ICML 2020) montrent que deux copies ajustées à partir d'un point où l'entraînement est devenu stable au bruit de SGD restent linéairement connectées, sans barrière de perte. La fusion de poids hérite de cette condition.
- **Model soups** (Wortsman et al., ICML 2022). Moyenner les poids de modèles ajustés avec des hyperparamètres différents ne coûte, à l'inférence, que le prix d'un modèle. Deux recettes : la soupe **uniforme** (tous les modèles) et la soupe **gloutonne** (modèles triés par précision de validation, ajoutés un à un s'ils améliorent le score). Sur ImageNet avec ViT-G/14 (58 modèles ajustés) : 90,94 % de précision top-1 pour la soupe gloutonne contre 90,78 % pour le meilleur modèle de la recherche d'hyperparamètres ; l'état de l'art précédent était CoAtNet-7 à 90,88 %. La soupe uniforme échoue avec de forts taux d'apprentissage (barrière d'erreur) ; sur le texte (T5), les gains sont faibles.
- **Départs différents.** Git Re-Basin (Ainsworth, Hayase, Srinivasa, ICLR 2023) aligne les unités cachées par des permutations avant de fusionner : connectivité sans barrière entre deux ResNet entraînés indépendamment sur CIFAR-10 ; sur ImageNet (ResNet50), la barrière est réduite de 67 % mais pas annulée. Le travail porte sur la vision ; il n'est pas la pratique des LLM, qui fusionnent des variantes d'un même modèle de base.

### Méthodes pour modèles ajustés

- **Moyenne linéaire.** Moyenne (pondérée) des poids : c'est la soupe. Elle est associative : une fusion linéaire de fusions linéaires est une fusion linéaire unique (Command A).
- **Task arithmetic** (Ilharco et al., ICLR 2023). Le **vecteur de tâche** est la différence entre poids ajustés et poids de base. On l'additionne pour ajouter une compétence, on le **nie** pour en retirer une : sur GPT-2 Large, nier un vecteur ajusté sur du texte toxique fait passer le taux de générations toxiques de 4,8 % à 0,8 % sans dégrader la perplexité sur WikiText-103. Le coefficient d'échelle se choisit sur un jeu de validation. Limite écrite : même architecture et même initialisation.
- **TIES-Merging** (Yadav, Tam, Choshen, Raffel, Bansal, NeurIPS 2023). Trois étapes pour limiter les interférences : (1) *trim* : ne garder que les 20 % de paramètres de plus grande amplitude de chaque vecteur ; (2) *elect sign* : choisir le signe de chaque paramètre par la masse d'amplitude totale ; (3) *disjoint merge* : moyenner seulement les valeurs qui s'accordent avec ce signe. Les conflits de signe subsistent après le trim et croissent avec le nombre de modèles. Limites de l'annexe : initialisation et architecture communes, et retard sur l'entraînement multitâche simultané.
- **DARE** (Yu, Yu, Yu, Huang, Li, ICML 2024). *Drop And REscale* : mettre à zéro chaque delta avec une probabilité $p$ puis multiplier les autres par $1/(1-p)$. Les deltas d'un modèle ajusté seraient très redondants (typiquement inférieurs à 0,002) : 90 %, voire 99 %, peuvent être supprimés. La tolérance croît avec la taille (WizardMath-70B résiste à $p = 0{,}99$, les 7B et 13B non) ; sans le rééchelonnage, la qualité s'effondre ; appliquer l'élagage aux paramètres ajustés plutôt qu'aux deltas est catastrophique. Se combine avec task arithmetic (*dare_linear*) ou TIES (*dare_ties*).
- **SLERP.** Interpolation sphérique entre **deux** modèles ; l'origine est l'interpolation de rotations (Shoemake, 1985, non ouvert : cité par le papier MergeKit). Dans mergekit, SLERP porte sur exactement deux modèles.
- **Autres variantes.** *DELLA* (Deep, Bhardwaj, Poria, 2024 : élagage des deltas selon l'amplitude), *Model Breadcrumbs* (Davari, Belilovsky, ECCV 2024 : masque creux retirant les très grands et les très petits deltas), *Model Stock* (Jang, Yun, Han, ECCV 2024 : moyennage par couche à partir de peu de modèles ajustés), moyenne pondérée par l'information de Fisher (Matena, Raffel, 2021) et RegMean (Jin et al., ICLR 2023). Les trois derniers ne sont lus qu'au résumé.
- **Optimiser la recette** (Akiba, Shing, Tang, Sun, Ha, Sakana AI ; arXiv 2024, *Nature Machine Intelligence* 2025). Une recherche évolutionnaire (CMA-ES) règle les hyperparamètres de DARE-TIES dans l'espace des paramètres et, dans une seconde variante, le chemin des données à travers les couches des modèles sources. Modèle japonais 7B issu de trois sources : 52,0 sur MGSM-JA contre 9,6, 18,4 et 30,0 pour les trois modèles sources ; fusions non optimisées avec les mêmes sources : TIES 4,4, DARE-TIES 35,2, *frankenmerge* 0,0. Limites écrites : héritage des limites des sources, réponses parfois sans cohérence logique.
- **Passthrough, frankenmerge, depth up-scaling.** Empiler des tranches de couches de modèles. SOLAR 10.7B (Kim et al., NAACL 2024 industrie) duplique 32 couches vers 48 (8 couches retirées de chaque copie), puis **réentraîne** : c'est donc de l'empilement plus de l'entraînement, publié sous Apache 2.0.
- **Fusion en MoE.** *Sparse upcycling* (Komatsuzaki et al., ICLR 2023) convertit un checkpoint dense en MoE ; sur T5 et ViT, les modèles dépassent leurs équivalents denses avec environ la moitié du coût initial de pré-entraînement. *Branch-Train-MiX* (Sukhbaatar et al., 2024) copie un modèle, entraîne des experts en parallèle, puis réunit leurs couches feed-forward en experts d'un MoE (les autres paramètres sont moyennés) et ajuste le routage. `mergekit-moe` prend l'attention et les normalisations d'un modèle de base et les MLP des modèles experts ; ses portes (`gate_mode`) valent `hidden` (meilleure qualité, beaucoup de VRAM), `cheap_embed` ou `random` (qui exige un fine-tuning) ; sa doc ne chiffre aucun gain. Que Mixtral soit un *upcycling* de Mistral 7B n'est pas écrit dans la source lue : non affirmé.

### Dans les laboratoires

- **Command A** (Cohere, 2025). Six experts SFT sont fusionnés en une « soupe SFT », puis six experts de préférence en une « soupe » de préférence ; fusion **linéaire** à poids cherchés à la main et par force brute. L'équipe écrit que SLERP et les vecteurs de tâche n'ont donné aucune amélioration significative, pour une complexité accrue. Face aux experts, la fusion perd 1,8 % en moyenne, la plupart des métriques restant à moins de 2,5 % du meilleur expert ; le code est le domaine le moins bien préservé. Fusionner est bon marché, évaluer chaque fusion ne l'est pas.
- **Olmo 3** (Team Olmo, décembre 2025). Au 32B, la fusion de deux runs de mid-training à graines différentes gagne environ un point sur le groupe MCSTEM et est retenue ; l'essai sur le 7B n'a pas donné de gains similaires. L'extension de contexte moyenne les trois derniers checkpoints ; le checkpoint SFT de raisonnement final est une fusion linéaire pondérée de deux checkpoints, faite avec mergekit.
- **Pré-entraînement** : ByteDance Seed (2025, résumé lu) rapporte que fusionner des checkpoints entraînés à taux d'apprentissage constant améliore la performance et aide à prédire l'état après décroissance.

### Outils

- **mergekit** (Goddard et al., EMNLP 2024 industrie, Arcee). Recettes YAML ; calcul « *out-of-core* » avec chargement paresseux des tenseurs, qui permet de fusionner sur un portable sans GPU. Méthodes listées au README (lu le 2026-10-02) : `linear`, `slerp`, `nuslerp`, `multislerp`, `karcher`, `task_arithmetic`, `ties`, `dare_linear` et `dare_ties`, `della`, `breadcrumbs`, `sce`, `model_stock`, `nearswap`, `arcee_fusion`, `passthrough`. Outils annexes : `mergekit-moe`, `mergekit-extract-lora` (approximation de bas rang d'un modèle ajusté), `mergekit-multi`, `mergekit-pytorch`, `mergekit-tokensurgeon` (greffe de tokenizer). Licence du dépôt : **LGPL-3.0** (cela concerne l'outil, pas les modèles produits). Dernière version : v0.1.4 (31 octobre 2025) ; dépôt actif (dernier push le 12 septembre 2026). Il n'y a pas de brique mergekit dans le brain à ce jour.
- **PEFT** (Hugging Face) fusionne des adaptateurs LoRA par `add_weighted_adapter`, avec `combination_type` valant `ties` ou `dare_ties` entre autres (doc « model merging »). [[LLaMA-Factory]] (`llamafactory-cli export`) et [[Axolotl]] (`axolotl merge-lora`) fusionnent un adaptateur dans le modèle de base.
- **Bancs d'essai** : FusionBench (Tang et al., 2024) et MergeBench (He et al., NeurIPS 2025 jeux de données, résumés lus).

### Quand ça marche, quand ça échoue

- **Conditions** : même modèle de base et même architecture (écrit par Task Arithmetic, TIES, Model soups et mergekit). Pour le tokenizer, mergekit offre une option d'union et un outil de greffe ; aucune étude chiffrée sur ce point n'a été trouvée. La doc PEFT et Command A avertissent de fusionner les embeddings de jetons spéciaux avec soin.
- **À l'échelle.** Yadav et al. (Google, 2024 ; PaLM-2 de 1 à 64 Md, jusqu'à 8 experts, modèle fermé donc non reproductible hors de Google) : la fusion marche mieux avec de bons modèles de base instruits ; les grands modèles fusionnent plus facilement ; avec 8 grands experts, le modèle fusionné généralise souvent mieux que le modèle multitâche sur des tâches non vues ; les méthodes se comportent de façon très similaire aux grandes échelles. MergeBench trouve que la fusion marche mieux sur de meilleurs modèles de base, avec un retard persistant sur l'entraînement multitâche. Une analyse théorique (Wang et al., 2025) et une loi d'échelle (2025) annoncent des rendements décroissants avec le nombre d'experts (résumés lus).
- **Sur des modèles « sauvages »** (Hitit, Girrbach, Akata, TMLR 2026 ; 4 LLM, 12 checkpoints hétérogènes, 16 benchmarks) : seule la task arithmetic apporte des gains fiables ; les méthodes plus sophistiquées sont en retrait (résumé lu).
- **Langues** (Gain et al., 2026, modèles de traduction) : la fusion réussit mieux quand les langues cibles sont communes et échoue sinon, sans égaler les checkpoints par langue (résumé lu).
- **Sécurité.** Hammoud et al. (Findings EMNLP 2024) : les méthodes de fusion propagent le désalignement, et un seul expert mal aligné peut dominer le comportement de sécurité du modèle fusionné. En sens inverse, fusionner les poids avant et après un ajustement atténue la perte de sécurité (Farn et al., 2025) ou une fusion sélective par couche la préserve (SafeMERGE). Des attaques existent : *Merge Hijacking* (ACL 2025) transmet une porte dérobée d'un modèle publié au modèle fusionné de sa victime ; TrojanMerge (avril 2026) construit des modèles individuellement sûrs dont la fusion est désalignée (résumés lus). L'OWASP (LLM03:2025, chaîne d'approvisionnement) cite la fusion de modèles et un service de fusion de Hugging Face parmi les surfaces d'attaque. Voir [[AI security]].
- **Leaderboards et contamination.** Des fusions ont dominé l'Open LLM Leaderboard : le papier DARE revendique le rang 1 pour *supermario v2* au 28 janvier 2024 (moyenne 75,49), et Labonne, dans son billet sur mergekit (janvier 2024), écrit que sa fusion *Marcoro14-7B-slerp* est contaminée et recommande de ne partir que de modèles non fusionnés. Un utilisateur a estimé à 5-8 points le gonflement « additif » des fusions : c'est une estimation, sans protocole publié. Les mainteneurs ont répondu que détecter la contamination est un problème non trivial et ont masqué les fusions par défaut, au motif d'une lignée opaque et de résultats académiques qui se transposent mal. Le classement a été clos le 13 mars 2025. Aucune mesure publiée du surplus de score dû aux fusions n'a été trouvée.
- **Désaccords laissés tels quels.**
  - TIES annonce de meilleurs résultats que la task arithmetic ; Yadav et al. (2024) trouvent des méthodes très semblables à grande échelle ; Hitit et al. ne trouvent de gain fiable que pour la task arithmetic ; Command A ne trouve aucun gain à SLERP ou aux vecteurs de tâche face à la fusion linéaire.
  - Fusion contre entraînement multitâche : Yadav et al. la voient souvent meilleure hors tâches ; TIES (annexe) et MergeBench la voient en retard.
  - Sécurité : propagée ou restaurée selon les montages (Hammoud, Farn, SafeMERGE) ; ces résultats portent sur des montages différents.

### Licences d'un modèle fusionné

- Un modèle fusionné est un dérivé de **chacun** de ses parents : leurs licences s'accumulent. Les clauses de dérivé, de redistribution et de seuil sont dans [[Licences de modèles open weights]] ; aucun texte de licence lu ne mentionne la fusion explicitement, et aucune analyse juridique solide sur la fusion comme œuvre dérivée n'a été trouvée.
- **Cas documenté** : Akiba et al. (annexe B) notent que l'un de leurs modèles sources, WizardMath-7B-v1.1, est sous une licence Microsoft de recherche non commerciale ; leur modèle fusionné est donc publié sous licence non commerciale. Ils ont refait la fusion avec des sources MIT et Apache seulement, ce qui donne une variante publiée sous Apache 2.0. Appliquer la clause la plus restrictive des parents est une **inférence** de cette page (le cas Sakana va dans ce sens), pas un énoncé d'un texte de licence.

## Les maths, simplement

- **Soupe uniforme** : $\theta = \frac{1}{N}\sum_{i=1}^{N}\theta_i$, avec $\theta_i$ les poids de $N$ modèles ajustés depuis le même point.
- **Vecteur de tâche et somme** : $\tau_k = \theta_k - \theta_0$, puis $\theta = \theta_0 + \lambda \sum_k \tau_k$. Nier un vecteur revient à utiliser $-\tau_k$. Le coefficient $\lambda$ se règle sur un jeu de validation.
- **SLERP** (formule classique) : $\text{slerp}(p, q; t) = \frac{\sin((1-t)\Omega)}{\sin\Omega}\,p + \frac{\sin(t\Omega)}{\sin\Omega}\,q$, où $\Omega$ est l'angle entre $p$ et $q$ ; $t \in [0,1]$ choisit le point sur l'arc plutôt que sur la corde.
- **DARE** : $\tilde\tau = \frac{m \odot \tau}{1-p}$ avec $m_j \sim \text{Bernoulli}(1-p)$ ; l'espérance de $\tilde\tau$ est $\tau$, c'est pourquoi le rééchelonnage préserve l'effet moyen des deltas.
- **TIES** : $s_j = \text{sign}\big(\sum_k \tau_{k,j}\big)$ (ce signe pèse l'amplitude totale), puis $\tau_j = \text{moyenne}\{\tau_{k,j} : \text{sign}(\tau_{k,j}) = s_j\}$ après avoir gardé les 20 % de plus grandes amplitudes.

## En pratique

- **Partir d'un même modèle de base** et de la même architecture ; vérifier tokenizer et jetons spéciaux.
- **Commencer simple** : moyenne linéaire ou task arithmetic, puis TIES ou DARE si des interférences se voient. Les sources ne s'accordent pas sur la supériorité des méthodes complexes.
- **Régler coefficients et densité sur un jeu de validation** de la tâche visée ; garder un jeu de test à part pour juger la fusion retenue.
- **Évaluer chaque candidat** : la fusion se calcule en minutes, l'évaluation coûte davantage (Command A). Contrôler aussi le refus, la sécurité et les capacités générales, que la spécialisation ou la fusion peuvent faire bouger.
- **Relire la licence de chaque parent** avant de publier ou de livrer (voir [[Licences de modèles open weights]]) et noter la lignée.
- **Ne pas se fier aux classements** de modèles fusionnés pour choisir : lignée opaque et contamination possible.
- **Vérifier la provenance** d'un adaptateur ou d'un modèle tiers avant de le fusionner : une fusion peut transmettre une porte dérobée.

## Approches voisines & alternatives

- [[Distillation]] — transférer un comportement par entraînement d'un élève, là où la fusion combine des poids existants sans entraînement.
- [[PEFT]] — la famille des ajustements légers dont les adaptateurs se fusionnent ensuite.
- [[LoRA et QLoRA]] — fusionner $\Delta W$ dans $W$ est le cas le plus simple de la fusion ; l'extraction de LoRA d'un modèle ajusté en est l'inverse.
- [[Fine-tuning]], [[SFT]] — ce qui produit les modèles ajustés que l'on fusionne ensuite.
- [[Mixture of Experts]] — construire un MoE à partir de modèles denses (upcycling, Branch-Train-MiX, mergekit-moe).
- [[Licences de modèles open weights]] — ce qu'un modèle dérivé hérite de ses parents.
- [[AI security]] — chaîne d'approvisionnement : la provenance d'un modèle ou d'un adaptateur fusionné.
- [[Quantification des LLM - GGUF, AWQ, GPTQ]] — la compression après fusion, à évaluer à part.
- Briques : [[LLaMA-Factory]], [[Axolotl]] — export et fusion d'un adaptateur LoRA dans le modèle de base. mergekit n'a pas de brique dans le brain.

## Pour aller plus loin

- Wortsman et al. (2022, ICML) — *Model soups* ; arXiv 2203.05482.
- Ilharco et al. (2022, ICLR 2023) — *Editing Models with Task Arithmetic* ; arXiv 2212.04089.
- Yadav et al. (2023, NeurIPS) — *TIES-Merging* ; arXiv 2306.01708.
- Yu et al. (2023, ICML 2024) — *Language Models are Super Mario* (DARE) ; arXiv 2311.03099.
- Goddard et al. (2024, EMNLP industrie) — *Arcee's MergeKit* ; arXiv 2403.13257 ; dépôt `arcee-ai/mergekit`.
- Akiba et al. (2024, *Nature Machine Intelligence* 2025) — *Evolutionary Optimization of Model Merging Recipes* ; arXiv 2403.13187.
- Yadav et al. (2024) — *What Matters for Model Merging at Scale?* ; arXiv 2410.03617.
- Hammoud et al. (2024, Findings EMNLP) — *Model Merging and Safety Alignment: One Bad Model Spoils the Bunch* ; arXiv 2406.14563.
- Hitit, Girrbach, Akata (2025, TMLR 2026) — *A Systematic Study of In-the-Wild Model Merging for Large Language Models* ; arXiv 2511.21437.
- Ainsworth et al. (2022, ICLR 2023) — *Git Re-Basin* ; arXiv 2209.04836. Kim et al. (2023, NAACL 2024) — *SOLAR 10.7B* ; arXiv 2312.15166. Komatsuzaki et al. (2022, ICLR 2023) — *Sparse Upcycling* ; arXiv 2212.05055. Sukhbaatar et al. (2024) — *Branch-Train-MiX* ; arXiv 2403.07816.
- Cohere (2025) — *Command A* ; arXiv 2504.00698. Team Olmo (2025) — *Olmo 3* ; arXiv 2512.13961.
- Labonne (janvier 2024) — *Merge Large Language Models with mergekit*, blog Hugging Face. OWASP — *LLM03:2025 Supply Chain*. Discussions du dépôt Open LLM Leaderboard (n° 472, 544, 629, 510).
- Lus au résumé seulement : Neyshabur et al. (2008.11687), Frankle et al. (1912.05671), DELLA (2406.11617), Model Breadcrumbs (2312.06795), Model Stock (2403.19522), Fisher (2111.09832), RegMean (2212.09849), WARM (2401.12187), FusionBench (2406.03280), MergeBench (2505.10833), Wang et al. (2505.21226), scaling laws (2509.24244), ByteDance Seed (2505.12082), Gain et al. (2604.02881), Farn et al. (2412.19512), SafeMERGE (2503.17239), Merge Hijacking (2505.23561), TrojanMerge (2604.00627). Non ouverts : le billet de bloc97 et l'article de Shoemake (1985).
