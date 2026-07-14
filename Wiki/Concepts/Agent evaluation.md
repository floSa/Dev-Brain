---
galaxie: wiki
type: concept
nom: Agent evaluation
alias: [évaluation d'agents, agent evaluation, agent eval]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm-eval, llm]
---

# Agent evaluation

## Aperçu

- Mesurer si un **agent LLM** accomplit réellement sa tâche — pas la qualité d'une réponse isolée, mais une trajectoire entière d'étapes, d'appels d'outils et de décisions.
- Plus dur que l'éval d'un LLM seul : non-déterminisme, erreurs qui se composent sur plusieurs tours, coût et latence à compter parmi les métriques.

## Concepts clés

### Outcome vs trajectory
- **Outcome** (résultat final) : la tâche est-elle réussie ? Binaire ou par rubrique. Simple, mais aveugle au « comment » — réussite par chance incluse.
- **Trajectory** (trajectoire) : juger la suite d'étapes (bons outils, bon ordre, pas de détours). Capte les régressions qu'un bon résultat masque.

### Métriques d'agent
- **Task success rate** (taux de réussite), **tool-call accuracy** (bon outil, bons arguments), nombre d'étapes, coût/latence par run. Le coût n'est pas un détail : un agent qui réussit en 40 appels n'est pas viable.

### Step-level vs end-to-end
- **End-to-end** : on note la sortie finale. **Step-level** : on note chaque décision (l'outil appelé à l'étape *t* était-il le bon ?). Le step-level localise la panne mais exige des traces annotées.

### LLM-as-judge sur traces
- Un LLM note la trajectoire selon une rubrique (plan cohérent ? bon contexte récupéré ?). Cf. [[LLM-as-judge]]. Indispensable quand il n'existe pas de vérité-terrain unique.

### Benchmarks d'agents
- **τ-bench** (tool-agent-user, service client), **SWE-bench** (résolution de bugs réels), **WebArena** / **GAIA** (tâches multi-étapes ancrées). Cf. [[LLM benchmarks]].

## Les maths, simplement

- Taux de réussite : $\text{SR} = \frac{1}{N}\sum_{i=1}^{N} \mathbb{1}[\text{succès}_i]$ sur $N$ tâches — à reporter avec un intervalle de confiance, $N$ étant souvent petit.
- Erreur composée : si chaque étape réussit avec probabilité $p$ indépendamment, une trajectoire de $k$ étapes réussit avec $p^k$. À $p=0{,}95$ et $k=10$, on tombe à $\approx 0{,}60$ — d'où l'enjeu de fiabilité par étape ([[Reliability patterns]]).

## En pratique

- Se construire un **jeu de tâches** représentatif, avec critère de succès explicite, *avant* d'optimiser quoi que ce soit ; sans lui, toute amélioration est une impression.
- Logger les **traces complètes** (pensées, appels, observations) — l'éval d'agent sans traçage est aveugle : [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/LangSmith|LangSmith]], [[Dev/Services/Phoenix Arize|Phoenix Arize]].
- Frameworks d'assertion : [[Dev/Services/DeepEval|DeepEval]] (métriques agents en CI), [[Dev/Services/Ragas|Ragas]] (volet tool-use/agent), [[Dev/Services/TruLens|TruLens]] (feedback functions sur traces).
- Rejouer chaque cas **plusieurs fois** : le non-déterminisme fait varier le résultat ; une seule passe ne prouve rien.
- Piège : optimiser le résultat final en laissant filer coût et latence — fixer un budget d'étapes dans la métrique.

## Approches voisines & alternatives

- [[LLM eval metrics]] — l'éval d'agent réutilise ces métriques, appliquées au niveau de chaque étape.
- [[RAG eval]] — cas particulier quand l'agent récupère du contexte (faithfulness, context precision).
- [[Agent patterns]] / [[agent-loops]] — ce qu'on évalue ; la boucle produit la trajectoire notée.
- [[Multi-agent systems]] — l'éval se complique : à qui imputer l'échec dans une équipe d'agents ?
- [[LLM observability]] — l'observabilité de prod alimente l'éval (cas réels → jeux de tests).

## Pour aller plus loin

- Yao et al. (2024) — *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*.
- Jimenez et al. (2023) — *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*.
- Mialon et al. (2023) — *GAIA: a Benchmark for General AI Assistants*.
