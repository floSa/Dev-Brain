---
galaxie: wiki
type: concept
nom: GraphRAG
alias: [graph RAG, knowledge graph RAG, RAG sur graphe, RAG augmenté par graphe de connaissances]
categorie: concept/llm
domaines: [ai-eng]
tags: [rag, knowledge-graph, graph-db, retrieval, llm]
---

# GraphRAG

## Aperçu

- Variante de [[Advanced RAG|RAG avancé]] où le retrieval s'appuie sur un **graphe de connaissances** (entités typées reliées par des relations) plutôt que sur un simple index de chunks plats.
- Vise les questions que le RAG vectoriel rate : **multi-hop** (relier des faits dispersés) et **globales** (« quels sont les grands thèmes du corpus ? »), en exploitant la structure explicite des liens.

## Concepts clés

### Pourquoi un graphe plutôt que des chunks plats
- Le RAG vectoriel récupère des passages **isolés** par similarité ; il ne sait pas relier deux faits situés dans des documents différents. Le graphe matérialise ces liens (`Entité A —relation→ Entité B`), donc le parcours traverse plusieurs sauts.
- La structure porte du **sens** réutilisable : filtrer par type d'entité, suivre une relation précise, agréger un voisinage.

### Retrieval local vs global
- **Local** : partir des entités mentionnées dans la question, parcourir leur voisinage à N sauts, assembler le contexte. Répond aux questions ciblées multi-hop.
- **Global** : pré-calculer des **communautés** du graphe (détection de clusters) et leurs **résumés** ; la réponse agrège les résumés pertinents. Répond aux questions de synthèse sur tout le corpus, hors de portée du top-k vectoriel.

### Construction du graphe en amont
- GraphRAG suppose un graphe ; sa qualité plafonne la qualité finale. Ce graphe est bâti par [[Construction de graphes de connaissances]] (extraction d'entités et de relations), souvent par LLM.

### Hybridation avec le vectoriel
- En pratique on combine : embeddings **sur les nœuds/relations** pour l'entrée dans le graphe, puis parcours structurel. Le graphe ne remplace pas le retrieval dense — il l'**oriente**.

## Les maths, simplement

- Voisinage à $k$ sauts d'une entité $v$ : ensemble des nœuds atteignables par un chemin de longueur $\le k$ depuis $v$. Le contexte récupéré croît vite avec $k$ (degré moyen $\bar d$ → $\approx \bar d^{\,k}$ nœuds), d'où la nécessité de **borner** $k$ et de filtrer par type de relation.
- Détection de communautés (global) : partitionner le graphe en groupes densément connectés en maximisant la **modularité** $Q$, qui compare la densité intra-groupe à celle d'un graphe aléatoire de même degré.

## En pratique

- Quand le sortir : corpus riche en **entités et relations** (rapports, dossiers, normes, bases métier), questions multi-hop ou de synthèse globale. Pour du Q&A factuel passage-par-passage, le [[RAG]] vectoriel suffit et coûte moins cher.
- Coût : la phase de construction (extraction LLM sur tout le corpus + résumés de communautés) est **lourde et à refaire** quand les données changent — à arbitrer contre le gain.
- Stockage : un graphe se range dans une base de graphes comme [[Dev/Services/Neo4j|Neo4j]] (Cypher, algos de graphe GDS) ; [[Dev/Services/LlamaIndex|LlamaIndex]] et [[Dev/Services/LangChain|LangChain]] exposent des *property graph index* / *graph retrievers*.
- Mesurer comme tout RAG : faithfulness, context precision/recall (cf. [[RAG eval]]) — un graphe mal construit dégrade silencieusement le retrieval.
- Piège : croire que le graphe dispense d'évaluer ; et sur-investir dans la construction avant d'avoir prouvé qu'un RAG vectoriel ne suffisait pas.

## Approches voisines & alternatives

- [[Advanced RAG]] — GraphRAG est l'un de ses patrons (à côté de self-RAG, agentic RAG).
- [[RAG]] — le socle vectoriel ; GraphRAG s'y ajoute quand la structure relationnelle compte.
- [[Construction de graphes de connaissances]] — la brique amont qui produit le graphe interrogé ici.
- [[Hybrid retrieval]] — combiner dense + structurel relève de la même logique d'hybridation.
- [[Bases de données vectorielles]] / [[Dev/Services/Neo4j|Neo4j]] — les deux mémoires interrogeables (vecteurs vs graphe), souvent associées.
- Alternative : rester en [[RAG]] vectoriel + [[Reranking|reranking]] — plus simple et moins cher quand les questions ne sont pas relationnelles.

## Pour aller plus loin

- Edge et al. (2024, Microsoft Research) — *From Local to Global: A Graph RAG Approach to Query-Focused Summarization* (retrieval local vs global, résumés de communautés).
- Sujets liés : [[Construction de graphes de connaissances]], [[Query transformations]], [[RAG eval]].
