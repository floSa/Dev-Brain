---
galaxie: dev
type: service
nom: Vespa
alias: [vespa, vespa.ai, vespa-engine]
pitch: "Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms."
categorie: database/search
licence_type: open-source
hosted: both
maturite: production
langage: Java/C++
scaling: distributed
alternatives: ["[[Dev/Services/Elasticsearch|Elasticsearch]]", "[[Dev/Services/txtai|txtai]]", "[[Dev/Services/Marqo|Marqo]]"]
remplace_par: []
status: actif
tags: [search, vector-db, hybrid-search, ranking, distributed]
url_docs: https://docs.vespa.ai/
url_repo: https://github.com/vespa-engine/vespa
---

# Vespa

## Pourquoi

Moteur de **recherche et de serving IA** open-source (Apache-2.0), issu de Yahoo. Dans un même système distribué, Vespa indexe et interroge **texte (BM25), vecteurs (ANN), tenseurs et données structurées**, puis applique un **ranking par modèles ML** (ONNX, XGBoost, fonctions de score) directement dans la couche de serving. Pensé pour le gros volume mutable : milliards de documents, milliers de requêtes/s, latence sous 100 ms. Écrit en Java (conteneur de requêtes) et C++ (couche de contenu).

## Quand l'utiliser

- Combiner dans un seul moteur **retrieval** (lexical + dense) **et ranking** ML multi-phases, sans pipeline externe.
- Très grande échelle, données qui changent en continu, contraintes de latence fortes.
- Exécuter un modèle de ranking (ou de la late-interaction) **dans le serving**, pas après coup.
- [[Late-interaction retrieval]] : Vespa supporte nativement les **tenseurs multi-vecteurs** (ColBERT) et le MaxSim.

## Quand NE PAS l'utiliser

- Petit corpus, besoin simple → la complexité opérationnelle est disproportionnée ; [[Dev/Services/Elasticsearch|Elasticsearch]] ou une base vectorielle dédiée ([[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]]) suffisent.
- Prototype Python embarqué → [[Dev/Services/txtai|txtai]] ou un index [[Dev/Services/Faiss|Faiss]] en mémoire.
- Équipe sans appétence pour l'ops : la courbe d'apprentissage (schéma, ranking profiles, déploiement) est raide.

## Déploiement & coût

- Self-host : conteneurs, cluster distribué (sharding + réplication des nœuds de contenu) ; gratuit, Apache-2.0.
- Managé : **Vespa Cloud** (offre commerciale de Vespa.ai), facturation à l'usage.
- Coût dominé par la RAM/CPU des nœuds de contenu et le calcul de ranking ; la quantification des vecteurs allège l'empreinte.

## Pièges

- **Complexité opérationnelle** réelle : modèle de déploiement, schémas, ranking profiles à maîtriser.
- Configuration verbeuse (schémas, services) ; itérer demande des redéploiements.
- Surdimensionné pour un besoin de recherche basique — ne pas y aller « par défaut ».
- Retours d'expérience détaillés : `Dev/REX/REX - Vespa.md`.

## Alternatives

- [[Dev/Services/Elasticsearch|Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[Dev/Services/txtai|txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Dev/Services/Marqo|Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.

## Liens

- [[Recherche d'information]] — le cadre (lexical / dense / hybride / ranking) que Vespa réunit dans un seul moteur.
- [[Bases de données vectorielles]] · [[Hybrid retrieval]] — le versant vectoriel et hybride.
- [[Late-interaction retrieval]] — supporté nativement (tenseurs multi-vecteurs, MaxSim, ColBERT).
- [[Reranking]] — Vespa fait le reclassement ML dans la couche de serving (multi-phase ranking).
- [[Comparatif - Moteurs de recherche]] — comparatif de la catégorie.
- Doc : https://docs.vespa.ai/
