---
galaxie: wiki
type: concept
nom: Query transformations
alias: [query transformation, réécriture de requête, query rewriting, query expansion, query decomposition, multi-query, HyDE, step-back prompting]
categorie: concept/llm
domaines: [ai-eng]
tags: [query-transformation, rag, retrieval, llm]
---

# Query transformations

## Aperçu

- Transformer la requête **avant** le retrieval : la question telle que posée n'est pas toujours la meilleure clé de recherche (trop courte, ambiguë, multi-hop, dépendante du contexte conversationnel).
- C'est l'étage **pré-retrieval** de l'[[Advanced RAG]] : on travaille la requête pour améliorer rappel et précision en amont, sans toucher à l'index.

## Concepts clés

### Réécriture & expansion
- Reformuler une requête mal posée, corriger les fautes, résoudre les références (« et lui ? » → l'entité visée) à partir de l'historique.
- Expansion : enrichir de synonymes ou de termes voisins pour élargir le rappel.

### Décomposition (multi-query, sous-questions)
- Casser une question complexe en plusieurs sous-questions, récupérer pour chacune, puis fusionner les passages.
- Indispensable pour le **multi-hop** (la réponse exige de croiser plusieurs documents).

### HyDE (Hypothetical Document Embeddings)
- Générer une réponse **hypothétique** à la question, puis chercher avec l'[[embeddings|embedding]] de cette réponse.
- Intuition : l'embedding d'une réponse plausible ressemble davantage aux documents cibles que celui d'une question nue.

### Step-back prompting
- Remonter à une question plus générale (« quels sont les principes de… ») pour récupérer des fondements, puis répondre à la question précise.

### Couplage avec le routage
- Une fois la requête transformée, il reste à l'envoyer au bon index ou au bon outil → [[Routing and cascading]].

## Les maths, simplement

- Multi-query : on génère $m$ variantes, chaque retrieval rend $k$ candidats, qu'on fusionne par **Reciprocal Rank Fusion** $\text{RRF}(d) = \sum_i \dfrac{1}{r + r_i(d)}$ ($r_i(d)$ = rang de $d$ dans la liste $i$, $r$ une constante).
- Le coût suit : $m$ variantes ⇒ ~$m$ appels LLM de transformation **et** $m$ retrievals. La latence se paie à chaque requête utilisateur.

## En pratique

- Gains réels surtout sur requêtes **courtes / ambiguës** ou **multi-hop** ; sur des questions déjà bien formulées, la transformation n'apporte rien et ajoute du coût.
- Toujours mesurer : une transformation mal calibrée **dégrade** le retrieval. C'est typiquement ce que tranche le [[RAG eval]].
- Outillage : [[Dev/Services/LlamaIndex|LlamaIndex]] (query engines, sub-question / multi-step) et [[Dev/Services/LangChain|LangChain]] (MultiQueryRetriever) exposent ces briques.
- Arbitrer comme tout l'[[Advanced RAG]] : n'empiler que si la mesure montre un gain net.

## Approches voisines & alternatives

- [[Advanced RAG]] — le cadre dont ceci est l'étage pré-retrieval.
- [[RAG]] — le socle ; la transformation agit sur sa phase requête.
- [[Hybrid retrieval]] — autre levier de rappel, au moment du retrieval plutôt qu'avant.
- [[Reranking]] — le pendant **post**-retrieval : on filtre après, là où la transformation agit avant.
- [[Routing and cascading]] — souvent enchaîné : transformer puis aiguiller.
- [[RAG eval]] — pour décider si une transformation aide vraiment.
- [[embeddings]] — ce que HyDE manipule (embedding d'une réponse hypothétique).

## Pour aller plus loin

- Gao et al. (2022) — *Precise Zero-Shot Dense Retrieval without Relevance Labels* (HyDE).
- Zheng et al. (2023) — *Take a Step Back: Evoking Reasoning via Abstraction* (step-back prompting).
- Gao et al. (2023) — *RAG for LLMs: A Survey* (taxonomie pré/post-retrieval).
