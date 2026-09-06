---
role: brique
nom: txtai
alias: [txtai, neuml-txtai]
pitch: "Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI."
categorie: database/recherche
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Vespa]]", "[[Marqo]]", "[[Elasticsearch]]"]
complements: ["[[sentence-transformers]]"]
tags: [search, semantic-search, embeddings, rag, vector-db]
url_docs: https://neuml.github.io/txtai/
url_repo: https://github.com/neuml/txtai
---

# txtai

<!-- AUTO:BANDEAU:START -->
> Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base d'embeddings tout-en-un. Un même index combine **recherche vectorielle**, **filtres SQL**
sur les métadonnées et **graphe** de connaissances ; par-dessus, txtai orchestre des pipelines
et des workflows LLM — RAG, agents, extraction, traduction. Le socle est
[[HuggingFace|Transformers]], sentence-transformers et [[FastAPI]]. Il s'utilise **embarqué**,
du notebook au script, ou exposé en **service API** dans un conteneur, avec des bindings
JavaScript, Java, Rust et Go.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Monter une recherche sémantique ou un RAG sans déployer de base vectorielle séparée | Mono-nœud : la montée en charge est verticale, il n'y a pas de moteur distribué — la limite de volume s'anticipe |
| Un index unifié vecteur + SQL + graphe, plutôt que d'assembler plusieurs briques | Tire un écosystème HuggingFace lourd selon les extras installés (taille d'image, dépendances) |
| Du prototype embarqué à une mise en production modeste exposée en API | Le modèle d'embedding est à choisir selon la langue et le domaine, et à garder cohérent entre index et requête |
| Orchestrer des workflows LLM (pipelines, agents) au plus près de l'index | Stack non-Python où le moteur doit être un service indépendant : les bindings restent secondaires |
| | Base vectorielle managée clé en main → [[Pinecone]] ; fort filtrage sur une base dédiée → [[Qdrant]] |

## Mise en œuvre

- Installation — `uv add txtai`, avec les extras correspondant aux pipelines voulus
- Point d'entrée — import Python embarqué, ou API FastAPI intégrée exposée en conteneur ; bindings JavaScript, Java, Rust et Go
- Prérequis — un modèle d'embedding à télécharger ; GPU recommandé pour encoder du volume
- Exécution — mono-nœud, index en mémoire ou sur disque local ; pas d'offre managée éditeur
- Coût — gratuit sous Apache-2.0 ; la dépense est le calcul d'embedding et la RAM de l'index

## Écosystème

### Alternatives

- [[Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — le socle d'embeddings sous-jacent

## Ressources

- Documentation — https://neuml.github.io/txtai/
- Dépôt — https://github.com/neuml/txtai

## Voir aussi

- [[Recherche d'information]] — le cadre (lexical / dense / hybride) que txtai met en œuvre
- [[Bases de données vectorielles]] — ce qu'il stocke et recherche
- [[embeddings]] — la représentation qu'il indexe
- [[RAG]] — son usage phare, avec workflows et pipelines intégrés
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
