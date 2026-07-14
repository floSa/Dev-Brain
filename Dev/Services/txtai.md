---
galaxie: dev
type: service
nom: txtai
alias: [txtai, neuml-txtai]
pitch: "Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI."
categorie: database/search
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Vespa|Vespa]]", "[[Dev/Services/Marqo|Marqo]]", "[[Dev/Services/Elasticsearch|Elasticsearch]]"]
remplace_par: []
status: actif
tags: [search, semantic-search, embeddings, rag, vector-db]
url_docs: https://neuml.github.io/txtai/
url_repo: https://github.com/neuml/txtai
---

# txtai

## Pourquoi

**Base d'embeddings tout-en-un** en Python (Apache-2.0, NeuML). Un même index combine **recherche vectorielle** (sémantique), **filtres SQL** sur métadonnées et **graphe** de connaissances ; par-dessus, txtai orchestre des **pipelines et workflows LLM** (RAG, agents, extraction, traduction…). Bâti sur [[Dev/Services/HuggingFace|Transformers]], [[Dev/Services/sentence-transformers|sentence-transformers]] et [[Dev/Services/FastAPI|FastAPI]]. S'utilise **embarqué** (import Python, du notebook au script) ou exposé en **service API** (FastAPI, conteneur), avec des bindings JavaScript / Java / Rust / Go.

## Quand l'utiliser

- Monter une **recherche sémantique** ou un **[[RAG]]** en Python sans déployer une base vectorielle séparée.
- Besoin d'un **index unifié** vecteur + SQL + graphe, plutôt que d'assembler plusieurs briques.
- Du prototype embarqué à une petite/moyenne mise en production exposée en API.
- Orchestrer des **workflows LLM** (pipelines, agents) au plus près de l'index.

## Quand NE PAS l'utiliser

- Très grande échelle distribuée, milliards de documents, ranking ML en serving → [[Dev/Services/Vespa|Vespa]] ou [[Dev/Services/Elasticsearch|Elasticsearch]].
- Stack non-Python où l'on veut le moteur comme service indépendant et costaud (les bindings restent secondaires).
- Base vectorielle managée clé en main → [[Dev/Services/Pinecone|Pinecone]] ; ou base dédiée à fort filtrage → [[Dev/Services/Qdrant|Qdrant]].

## Déploiement & coût

- `uv add txtai` (extras selon les pipelines voulus) ; Apache-2.0, gratuit.
- **Single-node** : index en mémoire/disque local ; GPU recommandé pour encoder du volume.
- Self-host en service via l'API FastAPI intégrée (conteneur) ; pas d'offre managée éditeur.

## Pièges

- **Single-node** : monte en charge verticalement, pas un moteur distribué — anticiper la limite de volume.
- Tire un **écosystème HuggingFace** lourd selon les extras installés (taille d'image, dépendances).
- Choisir un modèle d'embedding adapté à la **langue** et au domaine ; rester cohérent index/requête.
- Retours d'expérience détaillés : `Dev/REX/REX - txtai.md`.

## Alternatives

- [[Dev/Services/Vespa|Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[Dev/Services/Marqo|Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

## Liens

- [[Recherche d'information]] — le cadre (lexical / dense / hybride) que txtai met en œuvre.
- [[Bases de données vectorielles]] · [[embeddings]] — ce qu'il stocke et recherche.
- [[RAG]] — usage phare (workflows et pipelines intégrés).
- [[Dev/Services/sentence-transformers|sentence-transformers]] — socle d'embeddings sous-jacent.
- [[Comparatif - Moteurs de recherche]] — comparatif de la catégorie.
- Doc : https://neuml.github.io/txtai/
