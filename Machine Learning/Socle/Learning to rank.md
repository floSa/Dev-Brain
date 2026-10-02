---
role: notion
nom: Learning to rank
alias: [LTR, Apprentissage du classement, Classement supervisé, LambdaMART, LambdaRank, RankNet, ListNet, RankSVM, pointwise, pairwise, listwise, Unbiased learning to rank, ULTR]
categorie: ml/socle
domaines: [data-sci, ml-eng]
tags: [supervised, ranking, information-retrieval, recommender-systems]
---

# Learning to rank

## Aperçu

- Apprentissage supervisé d'une **fonction de score** $f(q, d)$ dont le tri décroissant sur une liste de candidats donne le bon ordre. Ce qui compte n'est pas la valeur prédite mais l'**ordre** des items d'une même requête.
- La donnée est groupée : une **requête** (ou un utilisateur, un contexte), une liste de documents candidats décrits par des features, et un **jugement de pertinence** par document. Le modèle est évalué par une métrique de classement ([[Ranking metrics]]), pas par une erreur de régression.
- Cette page traite l'**apprentissage** du classement. La mesure vit dans [[Ranking metrics]], le second étage neuronal d'un moteur dans [[Reranking]], le contexte dans [[Recherche d'information]].

## Concepts clés

### Le problème et ses trois familles
- Les trois familles se distinguent par ce qu'une perte regarde à la fois (Liu, 2009).
- **Pointwise** : un document à la fois, traité comme une régression ou une classification de sa pertinence. Simple, mais la perte ignore l'ordre relatif et la structure par requête : les requêtes à nombreux documents dominent la perte, et rien ne distingue une erreur en tête de liste d'une erreur en queue (Liu, 2009, §2.4.2).
- **Pairwise** : une paire de documents d'une même requête ; la perte pénalise les paires mal ordonnées. Le nombre de paires par requête est très inégal, ce qui biaise l'entraînement vers les requêtes riches en paires (Liu, 2009 ; Cao et al., 2007).
- **Listwise** : la liste entière, soit par une perte définie sur des permutations (ListNet, ListMLE), soit par des gradients dérivés d'une métrique de liste (LambdaRank, LambdaMART).
- Dans les trois cas, la **sortie du modèle** est un score ; seule la **perte** change.

### RankNet : le pairwise différentiable
- Burges et al. (ICML 2005). Pour deux documents $i, j$ de scores $s_i, s_j$, la probabilité que $i$ soit mieux classé est $P_{ij} = 1/(1 + e^{-\sigma(s_i - s_j)})$ ; la perte est l'entropie croisée, soit $C = \log(1 + e^{-\sigma(s_i - s_j)})$ quand $i$ doit passer devant $j$ (Burges, 2010, §2).
- Le modèle peut être n'importe quelle fonction différentiable : réseau de neurones à l'origine, arbres boostés ensuite.
- Observation de Burges (2010, §2.1) : les gradients se **factorisent** par document, $\lambda_i = \sum_j \lambda_{ij} - \sum_j \lambda_{ji}$. L'entraînement passe d'un coût proche du quadratique en nombre de documents par requête à un coût proche du linéaire. C'est l'idée qui mène à LambdaRank.

### LambdaRank et LambdaMART : optimiser la métrique sans la dériver
- Les métriques de classement (NDCG, MAP, MRR) sont, en fonction des scores, **plates ou discontinues** : leur gradient est nul presque partout (Burges, 2010, §3).
- **LambdaRank** (Burges, Ragno & Le, NIPS 2006) contourne le problème en spécifiant directement les gradients après tri, sans coût explicite. Pour NDCG, le gradient de RankNet est multiplié par la variation de la métrique si l'on échange les deux documents : $|\lambda_{ij}| = \sigma\,|\Delta \mathrm{NDCG}_{ij}| \,/\, (1 + e^{\sigma(s_i - s_j)})$ (au signe près selon la convention). Une erreur en tête de liste pèse plus qu'en queue.
- **LambdaMART** (Burges, 2010, §5) : ces $\lambda$ comme gradients d'un boosting d'arbres (MART). Wu, Burges, Svore et Gao ont écrit la méthode (rapport technique MSR-TR-2008-109, « Ranking, Boosting, and Model Adaptation », 2008 ; version publiée dans *Information Retrieval* 13(3), 2010). Burges (2010) rappelle qu'elle a gagné un concours d'ensembles au Yahoo! Learning To Rank Challenge 2010.
- Burges (2010, §4.2) établit l'optimalité de NDCG **empiriquement**, par un test de Monte Carlo : condition nécessaire, pas suffisante. Pour MAP ou MRR, on remplace $|\Delta\mathrm{NDCG}|$ par la variation de la mesure choisie.

### Listwise par la perte : ListNet, ListMLE, XE-NDCG
- **ListNet** (Cao, Qin, Liu, Tsai & Li, ICML 2007) : à chaque liste de scores, une probabilité « top-one » $P_s(j) = e^{s_j} / \sum_k e^{s_k}$ ; la perte est l'entropie croisée entre les distributions cible et prédite. Elle évite les $n!$ permutations et se calcule en $O(n)$ par liste.
- **ListMLE** : log-vraisemblance négative de la permutation de référence sous un modèle de Plackett-Luce ; il suppose un ordre total de référence (décrit d'après Liu, 2009, §4.2.2 ; l'article d'origine, Xia et al. 2008, n'a pas été ouvert).
- **XE-NDCG** (Bruch, WWW 2021) : une borne convexe d'une version transformée de NDCG, proche de la perte de ListNet ; dans la doc LightGBM, `rank_xendcg` est annoncé plus rapide que `lambdarank` pour une performance similaire.

### Jugements de pertinence et biais de position
- Les jugements viennent d'**annotateurs** (coûteux, cohérents) ou de **clics** (gratuits, bruités, biaisés). Un clic n'est pas une pertinence : l'utilisateur voit mieux le haut de la liste, donc le biais de présentation fait cliquer ce qui est bien placé.
- Joachims (2002) tire des préférences de paires depuis les clics (document cliqué préféré aux documents sautés plus haut) et entraîne un SVM sur ces contraintes : le **RankSVM**. Joachims, Swaminathan & Schnabel (2017) jugent ces préférences précises mais biaisées : elles contredisent l'ordre présenté.
- **Apprentissage non biaisé** : Joachims et al. (2017) corrigent par *propension inverse* (IPS). Chaque clic est pondéré par l'inverse de la probabilité d'avoir examiné sa position ; l'estimateur est non biaisé si cette probabilité est strictement positive pour tout rang. Les propensions s'estiment par **intervention** (échanger des résultats entre rangs). À petit échantillon la variance de l'IPS est forte ; on écrête les propensions pour échanger biais contre variance.
- **Unbiased LambdaMART** (Hu, Wang, Peng & Li, WWW 2019) étend la correction au pairwise en estimant conjointement le biais aux positions cliquées et non cliquées. XGBoost l'implémente (`lambdarank_unbiased`, présenté comme expérimental) ; LightGBM a ajouté `lambdarank_position_bias_regularization` en 4.1.0.

## Les maths, simplement

- Score $s_i = f(x_i)$ ; tri décroissant. Le gain d'un document de pertinence $l_i$ vaut $2^{l_i} - 1$ ; $\mathrm{DCG@}T = \sum_{i=1}^{T} (2^{l_i} - 1)/\log(1 + i)$ et $\mathrm{NDCG@}T = \mathrm{DCG@}T / \mathrm{maxDCG@}T$ (Burges, 2010, éq. 5).
- Pairwise, perte logistique : $C_{ij} = \log\big(1 + e^{-\sigma (s_i - s_j)}\big)$ pour $i \succ j$.
- Gradient par document, forme lambda : $\lambda_i = \sum_{j : i \succ j} \lambda_{ij} - \sum_{j : j \succ i} \lambda_{ji}$ avec $\lambda_{ij} = -\sigma |\Delta Z_{ij}| / (1 + e^{\sigma(s_i - s_j)})$, où $\Delta Z_{ij}$ est la variation de métrique si $i$ et $j$ échangent leur place.
- LambdaMART fait un pas de Newton par feuille : $\gamma = \sum \partial C/\partial s_i \,/\, \sum \partial^2 C/\partial s_i^2$ (Burges, 2010, §7).
- Estimateur IPS : chaque clic sur un document au rang $r$ est pondéré par $1/p_r$, avec $p_r$ la probabilité d'examiner le rang $r$ (Joachims et al., 2017, §5).

## En pratique

- **Le défaut sur features tabulaires est un GBDT à objectif lambda.** XGBoost : `rank:ndcg` (« LambdaMART », défaut du tutoriel), `rank:map` (pertinence binaire), `rank:pairwise` (perte RankNet, sans pondération par la métrique). LightGBM : `lambdarank` (avec `label_gain` pour fixer le gain de chaque niveau de pertinence) et `rank_xendcg`. [[CatBoost]] propose `PairLogit`, `YetiRank`, `LambdaMart`, `StochasticRank` et `QuerySoftMax` (documentation CatBoost, pertes de classement). Voir [[XGBoost]], [[LightGBM]] et [[CatBoost]].
- **Format d'entrée** : une matrice de features, des labels de pertinence, et un identifiant de groupe (`qid` trié chez XGBoost) qui dit quelles lignes forment une liste.
- **Paramètres de paires** (XGBoost) : `lambdarank_pair_method` (`topk` par défaut, ou `mean`) et `lambdarank_num_pair_per_sample`. La doc conseille, pour un jeu **grand**, l'objectif aligné sur la métrique cible avec `topk`, et, pour un jeu **petit**, NDCG ou RankNet avec `mean`. MRR n'est pas implémenté car il génère peu de « paires effectives ».
- **Troncature** (LightGBM) : `lambdarank_truncation_level` (30 par défaut) fixe combien de résultats de tête comptent à l'entraînement ; la doc suggère un peu au-dessus du $k$ évalué. `lambdarank_norm` (vrai par défaut) normalise les lambdas entre requêtes.
- **Défauts qui bougent entre versions** (XGBoost : méthode de paires et normalisations changées entre 1.7, 2.0 et 3.0) : fixer la version et relire la page *Learning to Rank* avant de comparer deux runs.
- Évaluer **par requête** avec la métrique visée ([[Ranking metrics]]), jamais par l'erreur quadratique des scores.
- Découper train et test **par requête**, jamais par ligne : des documents d'une même requête de part et d'autre de la coupure font fuiter l'information ([[Data leakage]]). Raisonnement de la page, sans source lue.

## Limites et débats

- **Perte et métrique ne coïncident pas.** Liu (2009, §5.2 et §5.4) montre que beaucoup de pertes pairwise (hinge, exponentielle, logistique) majorent une perte « essentielle » qui majore elle-même $1 - \mathrm{NDCG}$ ; mais être une borne supérieure ne suffit pas, l'optimum de la perte pouvant différer de celui de la mesure.
- **Que dit-on de la perte de LambdaRank ?** Wang et al. (LambdaLoss, CIKM 2018) écrivent que la perte sous-jacente à LambdaRank « reste inconnue » et en proposent un cadre probabiliste qui la définit, optimisé par EM. Bruch (2021) écrit au contraire que la perte de LambdaMART est construite heuristiquement et que celle de LambdaLoss n'est pas différentiable. Les deux lectures coexistent ; la doc XGBoost qualifie de « still up for debate » l'intérêt de pondérer par la métrique. Wang et al. observent aussi qu'une borne plus serrée peut **sur-apprendre**.
- **Les réseaux battent-ils les arbres ?** Qin et al. (ICLR 2021) montrent que la plupart des rankers neuronaux récents sont, de loin, inférieurs au meilleur GBDT public sur les benchmarks à features numériques, et que les comparaisons antérieures se faisaient contre un LambdaMART faible. Leur modèle neuronal enrichi (auto-attention sur la liste, augmentation de données) revient au niveau du GBDT, sans le dépasser nettement partout. Lyzhin et al. (arXiv:2204.01500) comparent LambdaMART, YetiRank et StochasticRank entre GBDT et proposent une variante améliorée de YetiRank. Portée : features numériques et jugements humains ; sur du texte brut, les modèles neuronaux dominent (Qin et al., §6).
- **L'apprentissage non biaisé tient-il hors simulation ?** Zou et al. (NeurIPS 2022) publient le jeu Baidu-ULTR (1,2 milliard de sessions, 7 008 requêtes annotées par des experts) et y évaluent ces méthodes. Hager et al. (SIGIR 2024) reprennent ces données et concluent que les techniques d'ULTR améliorent la **prédiction de clics** mais peinent à améliorer le classement mesuré sur des annotations d'experts : la perte et les features pèsent plus que le débiaisage. Les deux lectures divergent sur ce que montrent les résultats d'origine (Zou et al. : le modèle DLA se détache ; Hager et al. : aucune méthode ne bat nettement le naïf en classement) et les conclusions dépendent de la métrique choisie.
- **Un biais de position mal identifié.** Zhang et al. (KDD 2023) montrent que, dans les modèles à deux tours (pertinence + biais), la tour de biais peut être confondue avec la tour de pertinence quand la politique de journalisation corrèle position et pertinence.
- **Travaux récents** (résumés lus seulement, non vérifiés dans le corps) : Yu et al., arXiv:2511.06635 (nov. 2025, révisé août 2026), comparent des étiquettes de LLM et des clics comme supervision — les clics gagnent sur les requêtes fréquentes, les étiquettes de LLM sur les requêtes de fréquence moyenne et basse. Aucune réplication récente de la comparaison GBDT contre réseaux de Qin et al. n'a été trouvée.

## Place des cross-encoders et des rerankers actuels

- **Un cross-encoder est un ranker pointwise.** Nogueira & Cho (2019) classent chaque passage avec BERT, indépendamment, par une entropie croisée binaire ; ils annoncent +27 % relatif sur le MRR@10 de MS MARCO face à l'état de l'art d'alors (résumé de l'article). [[bge-reranker]] est un cross-encoder de ce type ; [[Jina Reranker]] propose des modèles listwise (v3) comme des cross-encoders (v2) ; [[Cohere Rerank]] est servi par API.
- **Un étage de plus, pas un remplaçant.** Dans une pile de recherche, le LTR sur features (BM25, signaux, popularité) et le cross-encoder sur texte brut jouent des rôles différents ; la page [[Reranking]] traite le second. Ce rapprochement est un raisonnement de la page, non une conclusion d'une source lue.
- **Rerankers à base de LLM** : RankGPT (Sun et al., arXiv:2304.09542) classe en génération de permutation par fenêtre glissante ; GPT-4 y dépasse monoT5-3B de 2,7 points de nDCG@10 en moyenne sur TREC. L'article note une forte sensibilité à l'ordre initial des passages et distille un modèle de 435 M de paramètres avec une **perte de type RankNet**, qui bat monoT5-3B de 1,67 nDCG sur BEIR : le LTR classique reste le mécanisme d'entraînement.
- **Généralisation mesurée** : Abdallah et al. (Findings of EMNLP 2025), 22 méthodes et 40 variantes, observent que les rerankers à base de LLM excellent sur les requêtes familières mais généralisent de façon inégale aux requêtes nouvelles, tandis que des modèles légers offrent des compromis comparables en coût.

## Approches voisines & alternatives

- [[Ranking metrics]] — ce que le modèle cherche à maximiser et ce qui l'évalue ; le NDCG y est défini.
- [[Reranking]] — le second étage neuronal d'un moteur ; un cross-encoder est un ranker pointwise.
- [[Recherche d'information]] — le contexte d'usage historique : le jugement de pertinence y est un objet de première classe.
- [[BM25]] — le signal lexical, entrée habituelle d'un LTR sur features.
- [[Systèmes de recommandation]] — l'autre usage : classer des items pour un utilisateur, avec des clics pour supervision.
- [[Gradient Boosting (GBDT)]] — le moteur de LambdaMART ; les objectifs de classement sont des pertes de plus dans XGBoost, LightGBM et CatBoost.
- [[XGBoost]], [[LightGBM]], [[CatBoost]] — les implémentations ; leurs objectifs sont décrits plus haut.
- [[Classification]] — le LTR pointwise en est un cas.
- [[Multi-armed bandits]] — l'apprentissage en ligne à partir de clics en est la version interactive ; la correction de biais ci-dessus traite le cas hors ligne.

## Pour aller plus loin

- Burges (2010) — *From RankNet to LambdaRank to LambdaMART: An Overview*, MSR-TR-2010-82. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf
- Burges et al. (2005) — *Learning to Rank using Gradient Descent*, ICML. https://www.microsoft.com/en-us/research/wp-content/uploads/2005/08/icml_ranking.pdf
- Burges, Ragno, Le (2006) — *Learning to Rank with Nonsmooth Cost Functions*, NIPS 19. https://papers.nips.cc/paper_files/paper/2006/file/af44c4c56f385c43f2529f9b1b018f6a-Paper.pdf
- Cao, Qin, Liu, Tsai, Li (2007) — *Learning to Rank: From Pairwise Approach to Listwise Approach*, ICML (lu : rapport technique MSR-TR-2007-40). https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-40.pdf
- Liu (2009) — *Learning to Rank for Information Retrieval*, Foundations and Trends in IR 3(3) : 225-331. DOI 10.1561/1500000016
- Joachims (2002) — *Optimizing Search Engines using Clickthrough Data*, KDD. https://www.cs.cornell.edu/people/tj/publications/joachims_02c.pdf
- Joachims, Swaminathan, Schnabel (2017) — *Unbiased Learning-to-Rank with Biased Feedback*, WSDM (lu : arXiv v1). https://arxiv.org/abs/1608.04468
- Hu, Wang, Peng, Li (2019) — *Unbiased LambdaMART*, WWW. https://arxiv.org/abs/1809.05818
- Wang, Li, Golbandi, Bendersky, Najork (2018) — *The LambdaLoss Framework for Ranking Metric Optimization*, CIKM. https://storage.googleapis.com/gweb-research2023-media/pubtools/4591.pdf
- Bruch (2021) — *An Alternative Cross Entropy Loss for Learning-to-Rank*, WWW. https://arxiv.org/abs/1911.09798
- Qin, Yan, Zhuang, Tay, Pasumarthi, Wang, Bendersky, Najork (2021) — *Are Neural Rankers still Outperformed by Gradient Boosted Decision Trees?*, ICLR. https://research.google/pubs/are-neural-rankers-still-outperformed-by-gradient-boosted-decision-trees/
- Lyzhin, Ustimenko, Gulin, Prokhorenkova — *Which Tricks Are Important for Learning to Rank?* https://arxiv.org/abs/2204.01500
- Zou et al. (2022) — *A Large Scale Search Dataset for Unbiased Learning to Rank* (Baidu-ULTR), NeurIPS. https://arxiv.org/abs/2207.03051
- Hager, Deffayet, Renders, Zoeter, de Rijke (2024) — *Unbiased Learning to Rank Meets Reality: Lessons from Baidu's Large-Scale Search Dataset*, SIGIR. https://arxiv.org/abs/2404.02543
- Zhang et al. (2023) — *Towards Disentangling Relevance and Bias in Unbiased Learning to Rank*, KDD. https://arxiv.org/abs/2212.13937
- Nogueira, Cho (2019) — *Passage Re-ranking with BERT*. https://arxiv.org/abs/1901.04085
- Sun et al. — *Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents*. https://arxiv.org/abs/2304.09542
- Abdallah et al. (2025) — *How Good are LLM-based Rerankers?*, Findings of EMNLP. https://aclanthology.org/2025.findings-emnlp.305/
- Documentation XGBoost — *Learning to Rank* (https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) et LightGBM — *Parameters* (https://lightgbm.readthedocs.io/en/latest/Parameters.html).
- **Non ouvert** : Xia et al. (2008, ListMLE) ; Wang et al. (SIGIR 2016, WSDM 2018) et Ai et al. (2018, 2020) lus par résumé seulement. L'attribution de dates entre 2006/2007 (LambdaRank) et 2007/2010 (LambdaMART) diffère entre sources : Burges (2010) date le papier de Wu et al. de 2007, les autres sources de 2010.
