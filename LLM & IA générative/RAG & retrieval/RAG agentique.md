---
role: notion
nom: RAG agentique
alias: [agentic RAG, RAG agentique, récupération adaptative, adaptive retrieval, Self-RAG, corrective RAG, recherche agentique, agentic search, active retrieval, FLARE, IRCoT, Search-R1]
categorie: llm/rag
domaines: [ai-eng]
tags: [rag, agents, retrieval, llm]
---

# RAG agentique

## Aperçu

- Un **RAG agentique** laisse le modèle conduire la récupération : décider **s'il faut chercher**, **quoi** chercher, relancer avec une autre requête, vérifier ce qu'il a trouvé, et **s'arrêter**. Dans un [[RAG]] ou un [[Advanced RAG]] classique, ces étapes sont fixées dans le code.
- Le terme couvre un spectre : une décision de récupération par requête (récupération adaptative), une boucle recherche-lecture (récupération itérative), un agent à plusieurs outils et sources, jusqu'à la [[Deep research]] qui produit un rapport. Les sources lues ne l'emploient pas toujours au même sens.
- Ce que l'on gagne : de meilleurs résultats sur des questions à plusieurs sauts ou mal formulées. Ce que l'on paie : jetons, latence, et des modes d'échec propres (boucles, sur-recherche, dérive de la requête). Plusieurs études de 2026 trouvent qu'un RAG bien réglé rattrape souvent l'agent.

## Concepts clés

### Du pipeline à l'agent

- **Workflow ou agent.** Anthropic (« Building effective agents », décembre 2024) oppose les *workflows* (chemins de code prédéfinis) aux *agents* (le modèle dirige son processus) et écrit que les systèmes agentiques échangent latence et coût contre de meilleures performances ; il recommande des conditions d'arrêt comme un nombre maximal d'itérations. Voir [[Agent patterns]].
- **Taxonomie.** La revue de Singh, Ehtesham, Kumar, Khoei et Vasilakos (arXiv 2501.09136, v4 d'avril 2026) distingue les architectures à agent unique (un routeur), multi-agents, hiérarchiques, **corrective**, **adaptative** et à graphe. Elle est conceptuelle, sans expérience. Ses « leçons » (v4) : l'agentique n'est pas le bon défaut, la qualité de la récupération reste le goulot, l'autonomie doit être bornée (horizon de planification, critères d'arrêt, outils prédéfinis) et l'évaluation doit porter sur le **processus**. Le texte se contredit sur la latence : réduite par des workflows optimisés (§2.4.3), mais accrue par l'agentique (§10.1).
- **Autres revues.** Li et al. (arXiv 2507.09477, juillet 2025) classent en RAG renforcé par le raisonnement, raisonnement renforcé par le RAG et synergie des deux ; Lin et al. (arXiv 2510.16724, octobre 2025) se centrent sur la recherche agentique entraînée par renforcement.

### Boucles de récupération : les méthodes fondatrices

- **ReAct** (Yao et al., ICLR 2023) : raisonnement et actions entrelacés, par exemple des appels à une API Wikipédia pour limiter l'hallucination. C'est le socle de la plupart des agents de recherche.
- **IRCoT** (Trivedi, Balasubramanian, Khot, Sabharwal ; arXiv décembre 2022, ACL 2023) : alterner une phrase de raisonnement en chaîne et une récupération dont la phrase sert de requête, jusqu'à la réponse. BM25, code-davinci-002 et Flan-T5, sur HotpotQA, 2WikiMultihopQA, MuSiQue et IIRC. Annonce : +11 à +21 points de rappel face à une récupération en une étape, jusqu'à +15 de F1, et Flan-T5-XL (3 Md) avec IRCoT dépasse GPT-3 avec récupération simple. Limite : un appel au modèle par phrase de raisonnement ; code-davinci-002 est déprécié, d'où une reproduction difficile.
- **FLARE** (Jiang et al., EMNLP 2023) : générer une phrase provisoire ; si un de ses jetons a une probabilité sous un seuil θ, s'en servir comme requête (jetons faibles masqués) puis régénérer. Sans entraînement. Sur 2WikiMultihopQA (EM/F1) : FLARE 51,0/59,7 contre 39,4/48,8 pour une seule récupération et 28,2/36,8 sans récupération ; la variante « phrase précédente », proche d'IRCoT dans leur réimplémentation, fait 39,0/49,2. La récupération se déclenche pour 30 à 60 % des phrases selon le jeu ; pas de gain notable sur Wizard of Wikipedia ni ELI5.
- **Self-RAG** (Asai, Wu, Wang, Sil, Hajishirzi ; arXiv 2310.11511, ICLR 2024) : le modèle est **entraîné** à émettre des jetons de réflexion — *Retrieve* (oui, non, continuer), *ISREL* (le passage est-il pertinent), *ISSUP* (la phrase est-elle soutenue : totalement, partiellement, pas du tout), *ISUSE* (utilité de 1 à 5). Entraînement sur 150 000 paires instruction-sortie, Llama 2 7B et 13B pour le générateur et un critique de 7B. À l'inférence, un seuil règle la fréquence de récupération. Résultats : Self-RAG 7B et 13B dépassent ChatGPT sur PubHealth, PopQA, les biographies et ASQA, mais pas sur TriviaQA ni ARC ; les ablations sans récupérateur, sans critique ou en forçant toujours la récupération dégradent. L'article ne mesure aucun coût.
- **CRAG, Corrective RAG** (Yan, Gu, Zhu, Ling ; arXiv 2401.15884, 2024) : un évaluateur (T5-large fine-tuné, 0,77 Md) note chaque passage et déclenche une action : *Correct* (raffiner par décomposition puis recomposition des passages), *Incorrect* (écarter et chercher sur le web après réécriture en mots-clés) ou *Ambiguous* (combiner les deux). Marges sur le RAG de base : +7,0 (PopQA), +14,9 (FactScore des biographies), +36,6 (PubHealth), +15,4 (ARC) avec le générateur de Self-RAG ; précision de l'évaluateur sur PopQA 84,3 contre 58,0 pour ChatGPT. Limites : il faut fine-tuner un évaluateur externe, les jeux sont centrés sur Wikipédia, et il n'y a qu'une passe de correction, pas de boucle. À ne pas confondre avec **CRAG, le banc d'essai de Meta** (Yang et al., NeurIPS 2024, arXiv 2406.04744, 4 409 questions) : seul le sigle est commun.
- **Adaptive-RAG** (Jeong, Baek, Cho, Hwang, Park, NAACL 2024) : un classifieur (T5-large) estime la complexité de la requête et choisit entre pas de récupération, une étape ou plusieurs étapes. Sur FLAN-T5-XL (moyenne des jeux) : sans récupération 14,87 EM ; une étape 34,83 ; Adaptive-RAG 37,17 (temps relatif 3,60) ; multi-étapes 39,00 (8,81), la récupération en une étape valant 1,00. Les étiquettes d'entraînement sont obtenues automatiquement, donc bruitées.
- **Estimer l'incertitude plutôt que d'entraîner un contrôleur** (Moskvoretskii et al., 2025) : sur 35 méthodes de récupération adaptative (dont FLARE, Adaptive-RAG, IRCoT) et 6 jeux, avec un seul modèle (Llama 3.1 8B Instruct), de simples estimateurs d'incertitude égalent les pipelines complexes en questions-réponses, pour moins de calcul.

### Apprendre à chercher par renforcement

- **Search-R1** (Jin, Zeng, Yue et al. ; arXiv 2503.09516, COLM 2025) : le modèle apprend, par RL, à alterner `<think>`, `<search>`, `<information>` et `<answer>` ; les jetons récupérés sont **masqués** dans la perte ; récompense réduite à l'exact-match ; budget de 4 actions ; Qwen 2.5 3B et 7B ; récupérateur E5 sur Wikipédia 2018. Sur sept jeux (EM moyen, 7B) : Search-R1 0,431 contre RAG 0,304 et IRCoT 0,239. Le papier donne deux gains relatifs : 41 % dans l'introduction et 24 % dans le résumé et la section des résultats (les deux comparent à des références différentes).
- **R1-Searcher** (Song et al., 2025) : RL en deux étapes (récompense de récupération puis de réponse) ; un détournement de récompense (le modèle saute la récupération) a été corrigé par des contraintes de format plus strictes. **ReSearch** (Chen et al., NeurIPS 2025) : entraîné sur MuSiQue seul. **DeepResearcher** (Zheng et al., 2025) : RL avec recherche web réelle (API Serper, cluster de CPU de 50 nœuds pour absorber les requêtes) ; annonce jusqu'à +28,9 points face aux agents à base de prompts et soutient que l'environnement réel est déterminant. Le **Tongyi DeepResearch** (Alibaba, 30,5 Md de paramètres dont 3,3 Md actifs) rapporte 43,4 sur BrowseComp et 32,9 sur Humanity's Last Exam (rapport technique). Voir [[RL for LLMs]] et [[GRPO]].
- **Désaccord** : Search-R1 et ReSearch s'entraînent sur un Wikipédia figé avec un récupérateur dense ; DeepResearcher affirme que seul le web réel suffit. Aucune comparaison à budget égal n'a été lue.

### Routage entre sources et outils

- Le routeur d'agent unique de la revue de Singh et al. choisit entre texte-vers-SQL, recherche vectorielle, web et recommandation ; l'exemple y est descriptif, sans mesure. « Learning to Route » (Bai et al., 2025, résumé lu) observe que combiner naïvement bases relationnelles et documents ajoute bruit et coût sans gain constant, et que choisir la source par requête est décisif. Voir [[Routing and cascading]] et [[Tool use patterns]].
- La spécification MCP (page « Tools », lue en septembre 2026) décrit les outils comme pilotés par le modèle, avec une erreur d'exécution renvoyée au modèle pour qu'il se corrige : c'est un transport générique d'outils, rien n'y est propre à la récupération ([[mcp-protocol]]).

### Évaluer un système multi-étapes

- **Jeux multi-sauts** : HotpotQA (EMNLP 2018, 113 000 paires), 2WikiMultiHopQA (COLING 2020), MuSiQue (TACL 2022, 2 à 4 sauts). **FRAMES** (Krishna et al., NAACL 2025, 824 questions) : Gemini-Pro-1.5 passe de 0,408 sans récupération à 0,474 avec 4 documents BM25, 0,66 avec un pipeline multi-étapes et 0,729 avec les bons documents ; le pipeline coûte six appels non parallélisables par question. **BrowseComp** (Wei et al., OpenAI, 2025, 1 266 questions) : GPT-4o 0,6 % (1,9 % avec navigation), o1 9,9 %, Deep Research 51,5 % ; des humains en deux heures résolvent 29,2 % des problèmes. **BrowseComp-Plus** (Chen et al., 2025) fige le corpus (100 195 documents) pour comparer agents et récupérateurs à armes égales. Voir [[RAG benchmarks]].
- **Juger la trajectoire, pas seulement la réponse** ([[Agent evaluation]]). Liu et al. (2026) sur six agents de recherche : l'effort de recherche et la qualité de la réponse sont faiblement alignés, la précision suit mieux le **rappel cumulé** des preuves, les preuves utiles arrivent tôt et les agents prolongent par une longue queue d'étapes peu productives. SearchAuditor (Liang et al., 2026, 1 243 échecs, huit modèles) : seulement 22,8 % des échecs viennent d'une couverture de recherche insuffisante, 77,2 % du traitement des preuves, et dans 25 % des échecs la bonne réponse figure mot pour mot dans le contenu récupéré.
- **Coût et latence** :
  - Ferrazzi et al. (2026) comparent un agent à un seul outil à un RAG « amélioré » (routeur sémantique, HyDE, reranker) sur quatre jeux : l'agent consomme en moyenne 3,3 fois plus de jetons d'entrée, 1,9 fois plus de sortie et 1,5 fois plus de temps.
  - Adaptive-RAG : 3,60 fois (adaptatif) et 8,81 fois (multi-étapes) le temps d'une récupération simple.
  - LatentRAG (Zheng et Worring, mai 2026) mesure, pour Search-R1 sur HotpotQA, 16 à 22 fois le temps d'un RAG naïf, dont environ 90 % dans la génération des pensées et sous-requêtes.
  - Ordre de grandeur côté multi-agents : voir [[Deep research]].

### Pièges

- **Sur-recherche et sous-recherche.** Wu et al. (« Search Wisely », 2025) : sur Search-R1 et R1-Searcher, un modèle aurait pu se passer de recherche dans 27,7 % de ses pas de recherche ; leur β-GRPO gagne 4 % d'EM moyen sur un modèle 3B. SAAS (Tang et al., 2026) note que le RL à récompense sur le seul résultat fait chuter presque à zéro les trajectoires sans recherche et monter les recherches redondantes (résumé lu).
- **Boucles et arrêt.** L'absence de critère d'arrêt explicite ou de plafond fait boucler. Tian, Ganguly, Macdonald (CIKM 2026) forcent une réponse après chaque itération : la qualité plafonne souvent avant la fin naturelle, et un arrêt précoce économise environ 11 % d'itérations pour environ 98 % de la qualité finale. Liu et al. proposent des critères d'arrêt fondés sur la **suffisance des preuves**. Pour les règles de plafond en pratique : [[Reliability patterns]].
- **Dérive de la requête.** « Plan Before Search » (Qian et al., 2026, résumé lu) : sans plan, chaque requête se forme à partir de documents partiellement pertinents et s'éloigne de la question. « Lost in the Maze » (Yen et al., 2025) : le contexte d'un agent de recherche s'accumule en contenu bruité ; résumer périodiquement la trajectoire (SLIM) donne 56 % sur BrowseComp et 33 % sur HLE avec o3. Voir [[Contexte long]] et [[Context engineering]].
- **Évaluateurs de récupération.** Aucune étude dédiée à la fiabilité d'un évaluateur de type CRAG n'a été trouvée ; celui de CRAG est fine-tuné sur PopQA et l'article ne le teste pas hors de ce cadre, hors une annexe non lue.
- **Sécurité.** Korn (2026, auteur unique) mesure, sur 921 questions, une attaque d'empoisonnement de la base qui réussit 81,9 % du temps contre un RAG simple et nettement moins contre un RAG agentique (environ 44 %), avec une latence médiane de 11,0 s contre 6,4 s ; l'agentique est moins vulnérable, pas immunisé. Voir [[AI security]].
- **Désaccords laissés tels quels.**
  - *Itérer sert-il ?* FRAMES : le multi-étapes monte de 0,408 à 0,66. Ferrazzi et al. : quand l'agent relance (10 % des cas), 53 % des documents sont identiques et rien n'est gagné ; un RAG amélioré suffit souvent. Cadres différents.
  - *Coût de Self-RAG.* Ses auteurs présentent la récupération à la demande comme un levier d'efficacité, sans mesure ; CRAG estime 26,5 à 132,4 TFLOP par jeton contre 26,5 pour un RAG simple.
  - *Récupération entrelacée.* IRCoT annonce de gros gains ; la réimplémentation de FLARE ne trouve que 39,0 contre 39,4 de EM pour la récupération simple (modèles et prompts différents).
  - *Où est le goulot.* Singh et al. v4 : la récupération ; SearchAuditor : l'usage des preuves.
  - *Contrôleur entraîné ou incertitude.* Adaptive-RAG et Self-RAG entraînent un contrôleur ; Moskvoretskii et al. trouvent des estimateurs simples aussi bons.
  - *L'agentique bat-il le RAG simple ?* SagaScale (2025) trouve le RAG agentique meilleur que le RAG naïf presque partout sur des romans entiers ; Ferrazzi et al. trouvent l'inverse face à un RAG bien optimisé.

## Les maths, simplement

- **Coût d'une boucle.** Si chaque étape relit le contexte accumulé : avec un contexte initial $c_0$ et $r$ jetons récupérés par étape, le coût en jetons d'entrée sur $T$ étapes vaut $\sum_{t=1}^{T} (c_0 + t\,r) = T c_0 + r\,T(T+1)/2$, soit **quadratique** en $T$. Calcul de cette page, sans source : il explique pourquoi résumer ou purger le contexte, et plafonner $T$, pèsent autant.
- **Déclencheur de FLARE** : récupérer si $\min_j p(\text{jeton}_j) < \theta$ sur la phrase provisoire.
- **Actions de CRAG** : un passage au-dessus d'un seuil haut donne *Correct* ; tous sous un seuil bas donnent *Incorrect* ; les autres cas, *Ambiguous*. Les valeurs numériques des seuils n'ont pas été retrouvées.
- **Self-RAG, sélection d'un segment** : score du segment = probabilité du segment + somme pondérée des notes des jetons de critique ; les poids se règlent à l'inférence.

## En pratique

- **Commencer par un RAG bien réglé** (récupération hybride, reranking, transformation de requête : [[Advanced RAG]], [[Hybrid retrieval]], [[Reranking]], [[Query transformations]]) et l'évaluer ; n'ajouter la boucle que si les questions multi-sauts ou mal posées l'exigent et que le gain se mesure.
- **Borner l'agent** : nombre maximal d'étapes et d'appels, critère d'arrêt sur la suffisance des preuves, réponse de repli forcée à la fin ; écrire la règle d'effort dans le prompt.
- **Limiter l'accumulation de contexte** : résumer ou purger les résultats déjà exploités.
- **Évaluer le résultat, la trajectoire et le coût** (jetons, appels, latence) sur un jeu figé ; rejouer en CI ([[RAG eval]], [[Agent evaluation]]).
- **Router explicitement** quand plusieurs sources existent, et tester avec des sources bruitées ou empoisonnées.
- **Tracer chaque étape** pour comprendre une trajectoire en échec ; les échecs viennent souvent du traitement des preuves, pas de la recherche.
- **Garder un chemin sans agent** : une question simple n'a pas à payer la boucle (Adaptive-RAG).

## Approches voisines & alternatives

- [[RAG]] et [[Advanced RAG]] — le pipeline fixe dont ceci est le prolongement ; l'alternative quand la requête est simple.
- [[Query transformations]] — réécriture, décomposition, HyDE : la version sans boucle de la reformulation.
- [[Hybrid retrieval]], [[Reranking]], [[GraphRAG]] — des remèdes statiques aux mêmes lacunes de rappel et de multi-saut.
- [[Agent patterns]] — le patron général que cette notion applique à la récupération.
- [[Deep research]] — le même mécanisme à l'échelle d'un rapport, avec sous-agents et budgets.
- [[Agent evaluation]], [[RAG eval]], [[RAG benchmarks]] — mesurer les trajectoires, la fidélité et les jeux multi-sauts.
- [[Routing and cascading]], [[Tool use patterns]] — choisir la source ou l'outil.
- [[Reliability patterns]] — plafonds, arrêts et repli quand l'agent boucle.
- [[Context engineering]], [[Contexte long]], [[Sous-agents et isolation du contexte]] — garder le contexte d'une longue recherche exploitable.
- [[Reasoning models]], [[RL for LLMs]], [[GRPO]] — le raisonnement et l'entraînement par renforcement qui rendent le modèle capable de chercher.
- [[Hallucinations des LLM]] — une récupération réussie ne supprime pas l'hallucination.
- Briques : [[LangGraph]] (graphes cycliques à état, adaptés à une boucle récupérer-évaluer-relancer : raisonnement de cette page), [[Qdrant]] (la base interrogée), [[Ragas]] et [[DeepEval]] (mesurer fidélité et pertinence des étapes), [[Langfuse]] (tracer les trajectoires).

## Pour aller plus loin

- Asai, Wu, Wang, Sil, Hajishirzi (2023, ICLR 2024) — *Self-RAG* ; arXiv 2310.11511.
- Yan, Gu, Zhu, Ling (2024) — *Corrective Retrieval Augmented Generation* ; arXiv 2401.15884.
- Jiang et al. (2023, EMNLP) — *Active Retrieval Augmented Generation* (FLARE) ; arXiv 2305.06983.
- Trivedi et al. (2022, ACL 2023) — *Interleaving Retrieval with Chain-of-Thought Reasoning…* (IRCoT) ; arXiv 2212.10509.
- Jeong et al. (2024, NAACL) — *Adaptive-RAG* ; arXiv 2403.14403. Yao et al. (2022, ICLR 2023) — *ReAct* ; arXiv 2210.03629.
- Singh et al. (2025, v4 2026) — *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG* ; arXiv 2501.09136. Li et al. (2025) — *Towards Agentic RAG with Deep Reasoning* ; arXiv 2507.09477.
- Jin et al. (2025, COLM) — *Search-R1* ; arXiv 2503.09516. Song et al. (2025) — *R1-Searcher* ; arXiv 2503.05592. Zheng et al. (2025) — *DeepResearcher* ; arXiv 2504.03160. Chen et al. (2025) — *ReSearch* ; arXiv 2503.19470.
- Krishna et al. (2024, NAACL 2025) — *Fact, Fetch, and Reason* (FRAMES) ; arXiv 2409.12941. Wei et al. (2025) — *BrowseComp* ; arXiv 2504.12516. Yang et al. (2024) — *CRAG – Comprehensive RAG Benchmark* ; arXiv 2406.04744.
- Ferrazzi et al. (2026) — *Is Agentic RAG worth it? An experimental comparison of RAG approaches* ; arXiv 2601.07711. Moskvoretskii et al. (2025) — *Adaptive Retrieval Without Self-Knowledge?* ; arXiv 2501.12835.
- Liu et al. (2026) — *Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents* ; arXiv 2608.01913. Liang et al. (2026) — *SearchAuditor* ; arXiv 2608.05212. Tian et al. (2026) — *Predicting Partial Answer Quality and Utility in Agentic RAG* ; arXiv 2609.16453. Wu et al. (2025) — *Search Wisely* ; arXiv 2505.17281.
- Anthropic (19 décembre 2024) — *Building effective agents*. Spécification MCP, page « Tools ».
- Lus au résumé ou à l'introduction seulement : ReAct, Learning to Route (2510.02388), SAAS (2605.29796), Plan Before Search (2605.28354), Lost in the Maze (2510.18939), LatentRAG (2605.06285), Korn (2605.05632), BrowseComp-Plus (2508.06600), Tongyi DeepResearch (2510.24701), SagaScale (2601.09723), les revues de Li et Lin (2507.09477, 2510.16724), HotpotQA, 2WikiMultiHopQA, MuSiQue.
