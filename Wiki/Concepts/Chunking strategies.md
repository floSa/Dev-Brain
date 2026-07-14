---
galaxie: wiki
type: concept
nom: Chunking strategies
alias: [chunking, découpage de documents, stratégies de découpage, text splitting]
categorie: concept/llm
domaines: [ai-eng]
tags: [rag, chunking, retrieval]
---

# Chunking strategies

## Aperçu

- Découper les documents en fragments (**chunks**) avant indexation : c'est l'unité que le [[RAG]] récupère puis injecte dans le prompt.
- Décision parmi les plus rentables du pipeline : un chunk mal taillé casse le contexte ou noie le signal, avant même tout retrieval.

## Concepts clés

### Taille et recouvrement
- **Taille** (en tokens) : petit = précis mais contexte fragmenté ; grand = contexte riche mais bruité et coûteux.
- **Overlap** : recouvrir les chunks voisins (10-20 %) pour ne pas trancher une idée à la frontière.

### Familles de découpage
- **Fixe** : par nombre de caractères/tokens. Simple, ignore la structure.
- **Récursif** : couper d'abord aux séparateurs forts (titres, paragraphes), puis descendre. Bon défaut.
- **Par structure** : suivre le Markdown/HTML, les sections, les tableaux, le code (dépend du parsing en amont).
- **Sémantique** : couper là où le sens change (rupture de similarité entre phrases voisines).

### Au-delà du chunk plat
- **Parent-child / small-to-big** : indexer de petits chunks, mais fournir au LLM le chunk parent plus large.
- **Late chunking** : encoder le document long d'un bloc, puis dériver les embeddings de chunks — préserve le contexte global.

## Les maths, simplement

- Nombre de chunks d'un document de $N$ tokens, taille $s$, overlap $o$ : $\big\lceil \frac{N - o}{s - o} \big\rceil$. Plus l'overlap monte, plus on multiplie les chunks (et le coût d'indexation).

## En pratique

- Démarrer **récursif**, ~256-512 tokens, overlap ~15 %, puis mesurer le rappel et ajuster.
- Caler la taille de chunk sur le **modèle d'embedding** (fenêtre utile) et sur le coût de génération (tokens injectés).
- Parser proprement avant de découper : [[Dev/Services/Docling|Docling]], [[Dev/Services/Unstructured|Unstructured]], [[Dev/Services/LlamaParse|LlamaParse]] gèrent tableaux et mise en page.
- Conserver des **métadonnées** par chunk (source, titre, page) pour filtrer et citer.
- Pièges : chunk à cheval sur deux sujets ; tableau ou code coupé en plein milieu ; structure d'un PDF ignorée.

## Approches voisines & alternatives

- [[RAG]] — le chunk en est l'unité de récupération.
- [[embeddings]] — chaque chunk devient un vecteur ; la taille de chunk conditionne la qualité de l'embedding.
- [[Advanced RAG]] — parent-child et compression de contexte prolongent le chunking.
- [[Hybrid retrieval]], [[Reranking]] — en aval, sur les chunks récupérés.

## Pour aller plus loin

- Günther et al. (2024) — *Late Chunking* (Jina AI).
- Doc des text splitters de [[Dev/Services/LangChain|LangChain]] et des node parsers de [[Dev/Services/LlamaIndex|LlamaIndex]].
