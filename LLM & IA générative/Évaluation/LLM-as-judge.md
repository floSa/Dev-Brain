---
role: notion
nom: LLM-as-judge
alias: [LLM as a judge, LLM juge, LLM évaluateur, G-Eval, pairwise comparison, reference-free evaluation, MT-Bench]
categorie: llm/eval
domaines: [ai-eng]
tags: [llm-as-judge, llm-eval, llm]
---

# LLM-as-judge

## Aperçu

- Utiliser un LLM (souvent fort) pour **noter la sortie** d'un autre, selon des critères en langage naturel. Réponse à un problème dur : évaluer du texte libre à grande échelle, sans réponse de référence ni annotateurs humains.
- C'est le moteur des métriques **sans référence** (cf. [[RAG eval]], [[LLM eval metrics]]) et des arènes de [[LLM benchmarks]].

## Concepts clés

### Trois protocoles
- **Pointwise** : noter une sortie seule sur une échelle (1-5) ou un critère binaire.
- **Pairwise** : préférer A ou B — plus fiable que l'absolu ; base des arènes type Chatbot Arena.
- **Reference-guided** : juger en fournissant une réponse de référence au juge.

### Avec ou sans grille
- **G-Eval** : le juge produit d'abord les étapes d'évaluation ([[Chain-of-Thought]]) puis la note → plus stable.
- **Rubriques** : critères explicites (exactitude, complétude, ton) notés séparément, plutôt qu'un score global flou.

### Les biais (le point sensible)
- **Position** : préférence pour la 1ʳᵉ (ou 2ᵉ) réponse en pairwise → permuter et moyenner. Wang et al. (2023) montrent que le classement de deux candidats peut être retourné par le seul changement d'ordre. Trois atténuations proposées : faire écrire au juge ses justifications **avant** la note, agréger les verdicts sur les ordres permutés, et faire relire par un humain les cas où le verdict dépend de l'ordre (repérés par une entropie de diversité).
- **Verbosité** : biais pour les réponses longues. AlpacaEval en souffrait ; sa version *length-controlled* (Dubois et al., 2024) ajuste les préférences par un modèle linéaire généralisé, pour estimer ce qu'elles seraient à longueur égale — la corrélation (Spearman) avec Chatbot Arena passe de 0,94 à 0,98. Sans cette correction : borner la longueur dans la consigne.
- **Auto-préférence** (*self-enhancement* chez Zheng et al.) : un juge préfère les sorties du même modèle / style. Panickssery et al. (2024) mesurent une corrélation linéaire entre la capacité d'un modèle à reconnaître ses propres sorties et la force de ce biais. Conséquence pratique (déduite, pas un résultat de l'article) : ne pas juger avec le modèle — ni la famille — qui a généré.
- **Raisonnement limité** : Zheng et al. (2023) le rangent parmi les limites du juge. Sur des paires à correction objective et difficile (savoirs, raisonnement, maths, code), JudgeBench (Tan et al., 2024) trouve que plusieurs modèles forts (ex. GPT-4o) ne font guère mieux que le hasard. Quand le résultat s'exécute, exécuter plutôt que juger ([[Code and math benchmarks]]).
- **Sensibilité** au format et au prompt de jugement — mesurée en chiffres plus bas (*Limites*).

### Juges spécialisés (modèles entraînés pour juger)
- **Principe** : affiner un modèle ouvert, plus petit, sur des jugements (souvent produits par un juge fort) pour remplacer le juge propriétaire — moins cher, exécutable en local, figé donc comparable dans le temps.
- **Prometheus** (Kim et al., 2023) : modèle 13B entraîné sur la *Feedback Collection* (1 000 rubriques, 20 000 instructions, 100 000 réponses avec retours générés par GPT-4) ; la rubrique est fournie à l'inférence. Les auteurs rapportent une corrélation de Pearson de 0,897 avec des humains sur rubriques personnalisées, contre 0,882 pour GPT-4.
- **Prometheus 2** ([[Prometheus-Eval]], Kim et al., 2024) : notation directe **et** pairwise selon des critères définis par l'utilisateur ; les auteurs rapportent la meilleure corrélation et le meilleur accord avec les humains et les juges propriétaires parmi les évaluateurs ouverts testés, sur huit benchmarks. Poids 7B (base Mistral) et 8x7B ; dépôt `prometheus-eval` et carte du modèle sous Apache-2.0.
- **JudgeLM** (Zhu et al.) : 7B, 13B, 33B. Traite explicitement trois biais du juge affiné — position, connaissance, format — par *swap augmentation*, *reference support* et *reference drop*. L'accord de plus de 90 % annoncé est mesuré **avec GPT-4, son professeur**, pas avec des humains. Poids sous licence LLaMA.
- **Selene Mini** (Atla) : 8B sur base Llama 3.1, carte du modèle sous Apache-2.0. Annoncé par l'éditeur comme meilleur modèle génératif 8B sur RewardBench.
- **GLIDER** (Patronus AI) : petit modèle (≈4B, base Phi-3.5-mini) à critères et échelles libres (binaire, Likert) ; sort les raisons du score et les passages décisifs. Licence **CC-BY-NC-4.0** : usage non commercial, donc bloquant pour une livraison chez un client sans accord.
- **Juge ou reward model ?** Un juge spécialisé produit une critique et une note sur un critère explicite ; un [[Reward modeling|reward model]] produit un scalaire appris sur des comparaisons. Les deux se recouvrent : Prometheus 2 se présente comme utilisable pour les deux, et RewardBench (Lambert et al., 2024) sert à comparer les reward models sur chat, raisonnement et sécurité.
- **Garde-fou** : un juge spécialisé reste calibré sur la distribution de ses données d'entraînement. Il se valide sur son propre échantillon humain avant usage (cf. ci-dessous).

### Calibrer contre des annotations humaines
- **Le plafond est l'accord humain ↔ humain, pas 100 %.** Zheng et al. (2023) rapportent que GPT-4 atteint plus de 80 % d'accord avec les préférences humaines, le niveau d'accord observé entre humains.
- **Ne pas généraliser une calibration.** JUDGE-BENCH (Bavaresco et al., 20 jeux de données NLP) trouve des juges fiables sur certaines tâches, mais très variables selon la propriété évaluée, le niveau d'expertise des annotateurs et le caractère humain ou généré du texte. Conclusion des auteurs : valider le juge contre des jugements humains avant usage. D'où une calibration **par critère et par type de contenu**, pas une fois pour toutes.
- **Préférer une étiquette objective à une préférence** quand la correction est vérifiable : JudgeBench note que la préférence humaine issue du crowdsourcing est un mauvais indicateur de correction factuelle ou logique.
- **Procédure minimale** (pratique, pas une prescription des articles) : échantillon annoté stratifié par critère → κ par critère → jeu tenu à part → **re-mesure à chaque changement** de modèle juge ou de prompt de jugement → relecture humaine des cas où le verdict bascule selon l'ordre. Pour le RAG, [[RAG eval]] cite ARES, qui calibre ses juges sur ~150 annotations humaines.

### Juger des agents et des trajectoires
- L'objet jugé change : non plus une réponse, mais une **suite d'étapes, d'appels d'outils et d'artefacts**. Le cadre (résultat vs trajectoire, step-level vs end-to-end) est dans [[Agent evaluation]] ; ici, ce que le juge y ajoute et y coûte.
- **Agent-as-a-Judge** (Zhuge et al., 2024) : un système agentique évalue un système agentique et fournit un retour **intermédiaire** sur tout le processus, pas seulement sur le résultat. Sur DevAI (55 tâches de génération de code, 365 exigences hiérarchiques), les auteurs rapportent qu'il surpasse nettement LLM-as-a-Judge et qu'il est aussi fiable que leur évaluation humaine de référence. Le dépôt (MIT) annonce 97,7 % de temps et 97,6 % de coût économisés face à des experts humains — chiffres des auteurs.
- **Juge de trajectoire, à l'usage** (déduit, pas issu d'une source) : donner au juge les **observations** des outils, pas seulement les « pensées » de l'agent ; noter chaque étape contre une rubrique (bon outil ? bons arguments ? information réellement utilisée ?) ; ne pas confier le jugement à la famille de modèle qui a produit la trajectoire (auto-préférence) ; garder en tête que le score mesure le couple modèle + [[Harnais d'agent|harnais]].
- **Le vérifiable d'abord** : si un test, une exécution ou un état final tranche, il prime sur le juge, qui garde le reste.

### Limites : coût et non-déterminisme
- **Coût** : chaque verdict est un appel (voir *Les maths*) ; permuter les positions, répéter les essais et noter chaque critère séparément multiplient la facture. Un juge fort peut coûter plus que la génération évaluée.
- **Instabilité d'un essai à l'autre.** *The Coin Flip Judge?* (Yagubyan, avril 2026, préprint) : sur essais répétés, les préférences pairwise changent en moyenne 13,6 % du temps, et 28 % des questions dépassent 20 % de bascule ; des prompts sémantiquement équivalents modifient le verdict dans 25 % des cas ; l'accord entre juges n'est que de 76 %. Les auteurs concluent qu'un juge à essai unique est souvent trop bruité pour un enjeu élevé, et recommandent d'agréger plusieurs essais et de randomiser les positions.
- **`temperature=0` ne suffit pas.** Tamba (juin 2026, préprint) : un harnais qui ne fixait pas la température laissait le fournisseur appliquer sa valeur par défaut (1,0), et des items limites basculaient entre exécutions identiques (jusqu'à ~50 % de désaccord par item sur 20 exécutions) ; même en décodage glouton forcé (690 appels, deux fournisseurs), 1 à 2 items limites sur 7 restent non reproductibles. Recommandation : traiter le **désaccord du juge** comme une métrique de santé, à côté des scores.
- **À relativiser** : ces deux études sont des préprints à un seul auteur et à petit échantillon. Elles vont dans le sens de la fragilité déjà documentée (Zheng et al.), mais l'ordre de grandeur se **mesure sur son propre jeu**, avec son propre juge.

## Les maths, simplement

- Accord juge ↔ humain mesuré par un **κ de Cohen** : $\kappa = \dfrac{p_o - p_e}{1 - p_e}$ ($p_o$ = accord observé, $p_e$ = accord attendu par hasard). Tant que κ n'est pas validé sur un échantillon humain, les scores du juge ne valent rien.
- En pairwise → **win rate** = part des comparaisons gagnées ; agrégé en classement (ex. Elo dans les arènes).
- **Cohérence sous permutation** : $C = \dfrac{1}{N}\sum_{i=1}^{N} \mathbb{1}\big[\text{gagnant}_i(A,B) = \text{gagnant}_i(B,A)\big]$ — part des paires dont le verdict survit à l'échange des positions ; $1-C$ mesure l'instabilité de position.
- **Taux de bascule** sur $n$ essais répétés : $f = \dfrac{1}{N}\sum_{i=1}^{N} \mathbb{1}\big[\text{les } n \text{ verdicts de l'item } i \text{ ne sont pas tous identiques}\big]$ — définition de travail du vault, pas celle d'un article.
- **Volume d'appels** $= N \times P \times E \times K$ ($N$ items, $P$ permutations — 2 en pairwise —, $E$ essais, $K$ critères notés séparément) ; coût $\approx$ volume $\times$ coût moyen d'un appel juge.

## En pratique

- **Calibrer avant de croire** : aligner le juge sur 30-50 jugements humains, mesurer l'accord, puis seulement automatiser.
- **Mesurer la stabilité avant l'accord** : cohérence sous permutation et taux de bascule sur un échantillon. Un juge instable ne se calibre pas, il se corrige d'abord.
- **Préférer le pairwise** au scoring absolu quand c'est possible (plus stable).
- **Neutraliser les biais** : permuter les positions, borner la longueur, fixer un modèle juge précis (versionné) pour la comparabilité dans le temps, choisir un juge d'une autre famille que le générateur.
- **Fixer la température explicitement** dans le harnais d'éval au lieu de compter sur le défaut du fournisseur ; répéter les items limites et trancher au vote.
- **Publier la variance** avec le score : taux de bascule et accord humain à côté de la moyenne.
- **Choisir le juge** : un modèle propriétaire fort (précis, mais coûteux, opaque, sujet à mise à jour silencieuse) ou un juge spécialisé ouvert (local, figé, moins cher — **lire la licence** : GLIDER est non commercial).
- Coût et latence non négligeables : un juge fort par requête peut coûter plus que la génération évaluée.
- Outiller : [[DeepEval]] (G-Eval), [[Ragas]] (métriques reference-free), [[TruLens]] (feedback functions), [[Inspect AI]] (scorers notés par un modèle), [[Langfuse]] (évals en ligne).

## Approches voisines & alternatives

- [[LLM eval metrics]] — le juge est une famille de métriques (sans référence) parmi d'autres.
- [[RAG eval]] — applique directement le LLM-as-judge (faithfulness, answer relevancy).
- [[Agent evaluation]] — le cadre de l'éval d'agent ; le juge de trajectoire s'y branche (Agent-as-a-Judge).
- [[Reward modeling]] — un juge et un reward model se recouvrent ; en RLAIF, le juge produit les préférences qui entraînent le RM.
- [[Code and math benchmarks]] — quand le résultat s'exécute, l'exécution remplace le juge.
- [[LLM benchmarks]] — MT-Bench et les arènes reposent sur le jugement (LLM ou humain).
- [[LLM observability]] — le juge sert aussi à scorer en ligne le trafic de production.
- [[Chain-of-Thought]] — G-Eval fait raisonner le juge avant qu'il note.

## Pour aller plus loin

- Zheng et al. (2023) — *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Liu et al. (2023) — *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*.
- Wang et al. (2023) — *Large Language Models are not Fair Evaluators* (biais de position et calibrations).
- Panickssery, Bowman, Feng (2024) — *LLM Evaluators Recognize and Favor Their Own Generations*.
- Dubois et al. (2024) — *Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators*.
- Kim et al. (2023) — *Prometheus: Inducing Fine-grained Evaluation Capability in Language Models*.
- Kim et al. (2024) — *Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models*.
- Zhu, Wang, Wang (2023) — *JudgeLM: Fine-tuned Large Language Models are Scalable Judges*.
- Tan et al. (2024) — *JudgeBench: A Benchmark for Evaluating LLM-based Judges*.
- Lambert et al. (2024) — *RewardBench: Evaluating Reward Models for Language Modeling*.
- Bavaresco et al. (2024) — *LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks*.
- Zhuge et al. (2024) — *Agent-as-a-Judge: Evaluate Agents with Agents*.
- Gu et al. (2024) — *A Survey on LLM-as-a-Judge* (panorama, révisé en 2025).
- Yagubyan (2026) — *The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation* (préprint).
- Tamba (2026) — *Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations* (préprint).
