---
galaxie: wiki
type: concept
nom: Construction de graphes de connaissances
alias: [knowledge graph construction, KG construction, extraction d'entités et de relations, knowledge graph building, peuplement de graphe de connaissances]
categorie: concept/llm
domaines: [ai-eng]
tags: [knowledge-graph, relation-extraction, ner, llm]
---

# Construction de graphes de connaissances

## Aperçu

- Transformer du texte non structuré en **graphe de connaissances** : un ensemble de **triplets** `(entité, relation, entité)` formant des nœuds typés reliés par des arêtes sémantiques.
- Brique amont du [[GraphRAG]] et des moteurs de raisonnement : la qualité du graphe plafonne celle de tout ce qui l'interroge.

## Concepts clés

### Le pipeline d'extraction
1. **Extraction d'entités** ([[NER et étiquetage de séquence|NER]]) : repérer et typer les mentions (personnes, organisations, produits, concepts métier).
2. **Extraction de relations** : déterminer quel lien unit deux entités co-occurrentes → produit le triplet `(sujet, relation, objet)`.
3. **Résolution d'entités** (*entity resolution*) : fusionner les mentions qui désignent le même réel (« IBM » = « International Business Machines ») pour ne pas dupliquer les nœuds.
4. **Liage à une ontologie** (optionnel) : rattacher entités et relations à un schéma / des types canoniques.

### Schéma libre vs ontologie imposée
- **Schéma ouvert** : laisser émerger les types d'entités et de relations du texte. Souple, rapide, mais bruité et hétérogène.
- **Ontologie cadrée** : imposer en amont la liste des types et relations autorisés. Plus propre et requêtable, au prix d'un travail de modélisation.

### Extraction par LLM
- Approche dominante aujourd'hui : un LLM lit un chunk et renvoie les triplets en **sortie structurée** (cf. [[Structured outputs]]), guidé par un schéma cible. Couvre des relations variées sans modèle dédié.
- Rançon : coût (un appel par chunk sur tout le corpus), **hallucination de relations**, et incohérences de nommage d'un chunk à l'autre — d'où l'étape de résolution.

### Extraction supervisée / classique
- Avant les LLM : [[NER et étiquetage de séquence|NER]] supervisé pour les entités + un classifieur de relations sur les paires. Plus précis et moins cher à grande échelle sur un domaine fermé, mais nécessite des données annotées.

## Les maths, simplement

- Extraction de relations vue comme une **classification** : pour une paire d'entités $(e_1, e_2)$ dans un contexte $c$, prédire $\hat r = \arg\max_{r \in R} P(r \mid e_1, e_2, c)$ où $R$ inclut une classe « pas de relation ».
- Coût de couverture : extraire toutes les paires d'un chunk à $n$ entités, c'est $\binom{n}{2}$ candidats — quadratique. On élague par fenêtre de co-occurrence ou par filtrage de types avant de lancer le classifieur / le LLM.

## En pratique

- Outillage entités : [[Dev/Services/spaCy|spaCy]] (NER industriel rapide), [[Dev/Services/GLiNER|GLiNER]] (NER zero-shot sur types décrits en langage naturel). Pour l'extraction LLM de triplets : [[Dev/Services/LlamaIndex|LlamaIndex]] (*KnowledgeGraphIndex* / *property graph*) et [[Dev/Services/LangChain|LangChain]] (*LLMGraphTransformer*).
- Stockage : ranger les triplets dans une base de graphes — [[Dev/Services/Neo4j|Neo4j]] (Cypher, contraintes d'unicité pour la déduplication).
- Verrou qualité : la **résolution d'entités**. Sans elle, le graphe se fragmente en doublons et les parcours multi-hop cassent.
- Contraindre l'extraction LLM par un **schéma** (liste fermée de types de relations) réduit le bruit et facilite l'interrogation aval.
- Pièges : ontologie trop fine (ingérable) ou trop floue (inutile) ; relations hallucinées non vérifiées ; reconstruire tout le graphe à chaque mise à jour des données (coûteux) au lieu d'un peuplement incrémental.

## Approches voisines & alternatives

- [[GraphRAG]] — le consommateur direct : interroge le graphe construit ici.
- [[NER et étiquetage de séquence]] — l'étape d'extraction d'entités, en amont des relations.
- [[Structured outputs]] — le mécanisme qui contraint la sortie LLM en triplets valides.
- [[Dev/Services/Neo4j|Neo4j]] — où vit le graphe produit.
- [[embeddings]] — la résolution d'entités s'appuie souvent sur la similarité d'embeddings pour repérer les doublons.
- Alternative : ne pas construire de graphe et rester en [[RAG]] vectoriel — préférable si les questions ne sont pas relationnelles et que le coût de construction ne se justifie pas.

## Pour aller plus loin

- Edge et al. (2024, Microsoft Research) — *From Local to Global: A Graph RAG Approach…* (pipeline d'extraction LLM → graphe → résumés).
- Sujets liés : [[GraphRAG]], [[NER et étiquetage de séquence]], [[Recherche d'information]].
