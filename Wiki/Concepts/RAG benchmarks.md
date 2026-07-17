---
galaxie: wiki
type: concept
nom: RAG benchmarks
alias: [benchmarks RAG, bancs d'essai RAG, RGB, CRAG, RAGBench, TRACe, RAGTruth, FRAMES, TREC RAG, robustesse RAG, noise robustness, negative rejection]
categorie: concept/llm
domaines: [ai-eng]
tags: [benchmark, rag-eval, rag, retrieval, llm-eval]
---

# RAG benchmarks

## Aperçu

- Un benchmark RAG = un **jeu de questions + corpus + réponses/annotations de référence**, qui met à l'épreuve un pipeline [[RAG]] sur une base commune. C'est la maille au-dessus du [[RAG eval]] : les mêmes métriques, appliquées à une suite figée et partagée.
- Utilité : comparer des architectures ([[Advanced RAG]]), stresser les **modes de défaillance** (bruit, désinformation, questions multi-hop) qu'une éval maison sur golden set ne couvre pas.

## Concepts clés

### Les quatre dimensions de robustesse (RGB)
- **Noise robustness** : garder la bonne réponse quand des passages non pertinents polluent le contexte.
- **Negative rejection / abstention** : refuser de répondre (« information insuffisante ») quand aucun passage ne contient la réponse — l'inverse de l'hallucination par complaisance.
- **Information integration** : agréger des faits dispersés sur **plusieurs documents** (questions multi-hop).
- **Counterfactual robustness** : résister à la **désinformation** présente dans les documents récupérés, plutôt que la recopier.

### Les suites phares
- **RGB** — le banc d'essai des quatre dimensions ci-dessus, en anglais et chinois.
- **CRAG** (Meta) — large et unifiant : questions simples, multi-hop, à agrégation, et **dynamiques** (réponse qui change dans le temps) ; teste aussi l'usage d'API de recherche.
- **FRAMES** — combine **factualité + retrieval + raisonnement** multi-hop en une seule tâche end-to-end.
- **TREC RAG Track** (depuis 2024) — venue académique de référence, évaluée par [[RAG eval|nuggets]] (AutoNuggetizer).

### RAGBench & le cadre TRACe
- **RAGBench** : ~100k exemples issus de 5 domaines (biomédical, juridique, finance, client…), avec labels explicables.
- **TRACe** = trois dimensions interprétables du générateur : **Utilization** (part du contexte réellement exploitée), **Adherence** (fidélité / absence d'hallucination vis-à-vis du contexte), **Completeness** (couverture de l'information pertinente).

### RAGTruth : l'hallucination au niveau span
- ~18k réponses annotées **au niveau du passage fautif** (span), pas seulement globalement.
- Quatre types : conflit évident / subtil (contredit le contexte), et information sans fondement évidente / subtile (inventée). Sert à entraîner et jauger les **détecteurs d'hallucination**.

## Les maths, simplement

- Taux d'abstention correcte (*negative rejection rate*) $= \dfrac{\#\,\text{abstentions quand le contexte est insuffisant}}{\#\,\text{cas sans réponse dans le contexte}}$ — élevé = le système sait se taire.
- TRACe — **Adherence** $\approx$ faithfulness au niveau claim ; **Completeness** $\approx \dfrac{\#\,\text{claims pertinents couverts}}{\#\,\text{claims pertinents attendus}}$ ; **Utilization** $= \dfrac{\#\,\text{phrases de contexte réellement utilisées}}{\#\,\text{phrases de contexte fournies}}$.

## En pratique

- Un benchmark public **ne remplace pas** un golden set maison sur son corpus métier : il révèle des faiblesses génériques (robustesse au bruit, abstention), pas la performance sur *ses* documents. Les deux sont complémentaires.
- Prioriser les dimensions selon le risque métier : abstention critique en réglementé/médical, counterfactual robustness dès que le corpus peut contenir des sources contradictoires ou datées.
- Attention à la **contamination** : les corpus publics fuitent dans les données d'entraînement des LLM récents → un score flatteur sur CRAG/RGB ne garantit rien sur un corpus privé.
- Les benchmarks d'hallucination (RAGTruth) servent surtout à choisir/calibrer un **détecteur** de groundedness, brique de la [[LLM observability]] en production.

## Approches voisines & alternatives

- [[RAG eval]] — les métriques et la méthodologie que ces suites appliquent à un jeu figé ; ce dont les benchmarks sont l'agrégation standardisée.
- [[RAG]] — le système mis à l'épreuve.
- [[Advanced RAG]] — les techniques dont ces benchmarks mesurent l'apport réel (et parfois l'absence).
- [[LLM benchmarks]] — l'équivalent pour les LLM seuls ; même distinction métriques ↔ suites standardisées.
- [[LLM-as-judge]] — moteur des scores automatiques de la plupart de ces benchmarks.

## Pour aller plus loin

- Chen et al. (2024) — *Benchmarking Large Language Models in Retrieval-Augmented Generation* (RGB).
- Yang et al. (2024) — *CRAG: Comprehensive RAG Benchmark*.
- Friel et al. (2024) — *RAGBench: Explainable Benchmark for RAG* (cadre TRACe).
- Niu et al. (2024) — *RAGTruth: A Hallucination Corpus for Developing Trustworthy RAG*.
- Pradeep et al. (2024) — *Initial Nugget Evaluation Results for the TREC 2024 RAG Track* (AutoNuggetizer).
