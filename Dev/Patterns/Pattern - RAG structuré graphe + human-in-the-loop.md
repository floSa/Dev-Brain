---
galaxie: dev
type: pattern
contexte: RAG sur connaissance relationnelle (entités liées, multi-hop) où les réponses engagent et passent par une validation humaine aux points sensibles.
created: 2026-06-11
modified: 2026-06-11
services_cles: [Neo4j, LangGraph, sentence-transformers, Qdrant]
projets_appliques: []
tags: [pattern, rag, knowledge-graph, graph-db, human-in-the-loop, agents]
---

# Pattern — RAG structuré graphe + human-in-the-loop

## Contexte

RAG où la connaissance est **relationnelle** (entités reliées, questions multi-hop) et où les réponses **engagent** (juridique, médical, finance, conformité). Deux exigences : un graphe de connaissances comme source structurée plutôt qu'un simple sac de chunks, et un humain qui valide aux points de décision avant toute action irréversible.

## Stack

- [[Neo4j]] — graphe de connaissances (entités typées, relations)
- [[sentence-transformers]] — embeddings pour la recherche dense
- [[Qdrant]] — index vectoriel, couplé au graphe (recherche hybride)
- [[LangGraph]] — orchestration du flux agent avec interruptions (human-in-the-loop) et reprise d'état
- [[LangChain]] — briques de retrieval / chaînage (optionnel selon l'implémentation)

## Décisions clés

### 1. Graphe **et** vecteurs, pas l'un ou l'autre
Le graphe porte la structure (traversées multi-hop, contraintes, chemins explicites) ; l'index vectoriel porte la similarité sémantique. La recherche hybride combine les deux : on récupère par sens, on raisonne par relations.

### 2. Human-in-the-loop aux points de décision
LangGraph interrompt le graphe **avant** une action engageante (réponse finale, écriture, appel d'outil coûteux). L'humain valide, corrige ou rejette, puis l'état reprend là où il s'était arrêté — pas un re-run complet.

### 3. Construction du graphe en amont
L'extraction d'entités et de relations (NER + relation extraction) se fait hors ligne, sur un pipeline dédié. Le RAG interroge un graphe déjà propre ; il ne le construit pas à la volée.

## Pièges

- **Extraction bruitée** → graphe faux → réponses fausses avec aplomb. La qualité du RAG est plafonnée par la qualité de la construction : valider le graphe.
- **Interruptions sans persistance d'état** → reprise impossible. Le checkpointer de LangGraph est ce qui rend le human-in-the-loop exploitable.
- **Tout passer en graphe** : pour de la similarité pure sans relations, un index vectoriel seul suffit — le graphe est un coût, pas un réflexe.

## Voir aussi

- Services : [[Neo4j]], [[LangGraph]], [[LangChain]], [[Qdrant]], [[sentence-transformers]]
- Concepts : [[GraphRAG]], [[RAG]], [[Advanced RAG]], [[Construction de graphes de connaissances]], [[Human-in-the-loop]], [[Hybrid retrieval]], [[NER et étiquetage de séquence]]
- Comparatifs : [[Comparatif - Bases graphes]], [[Comparatif - Frameworks LLM]]
