---
role: brique
nom: Vespa
alias: [vespa, vespa.ai, vespa-engine]
pitch: "Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java/C++
scaling: distributed
alternatives: ["[[Elasticsearch]]", "[[txtai]]", "[[Marqo]]"]
complements: []
tags: [search, vector-db, hybrid-search, ranking, distributed]
url_docs: https://docs.vespa.ai/
url_repo: https://github.com/vespa-engine/vespa
---

# Vespa

<!-- AUTO:BANDEAU:START -->
> Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java/C++ | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche et de serving IA issu de Yahoo. Dans un même système, Vespa indexe et
interroge **texte (BM25), vecteurs (ANN), tenseurs et données structurées**, puis applique un
**ranking par modèles ML** — ONNX, XGBoost, fonctions de score — directement dans la couche de
serving, en plusieurs phases. Il est pensé pour le gros volume mutable : milliards de
documents, milliers de requêtes par seconde, latence sous 100 ms, avec des mises à jour en
continu. C'est le seul du dossier à faire le retrieval et le reclassement au même endroit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Combiner retrieval (lexical + dense) et ranking ML multi-phases dans un seul moteur, sans pipeline externe | Complexité opérationnelle réelle : modèle de déploiement, schémas et ranking profiles sont à maîtriser avant la mise en production |
| Très grande échelle, données qui changent en continu, contraintes de latence fortes | Configuration verbeuse (schémas, services) : chaque itération passe par un redéploiement |
| Exécuter un modèle de ranking, ou de la late-interaction, dans le serving et non après coup | Surdimensionné pour un besoin de recherche basique — ce n'est pas un moteur à prendre « par défaut » |
| Late-interaction : tenseurs multi-vecteurs (ColBERT) et MaxSim supportés nativement | |

## Mise en œuvre

- Installation — conteneurs Docker, ou cluster déployé par l'outillage Vespa ; managé via Vespa Cloud
- Point d'entrée — API HTTP de feed et de requête ; schémas et ranking profiles déclarés dans un application package
- Prérequis — un schéma et des ranking profiles écrits avant toute indexation ; une équipe qui assume l'ops
- Exécution — self-hébergé ou managé, distribué : sharding et réplication des nœuds de contenu
- Coût — gratuit sous Apache-2.0 en self-host, Vespa Cloud facturé à l'usage ; la dépense est la RAM/CPU des nœuds de contenu et le calcul de ranking, que la quantification des vecteurs allège

## Écosystème

### Alternatives

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.

## Ressources

- Documentation — https://docs.vespa.ai/
- Dépôt — https://github.com/vespa-engine/vespa

## Voir aussi

- [[Recherche d'information]] — le cadre (lexical / dense / hybride / ranking) que Vespa réunit dans un seul moteur
- [[Bases de données vectorielles]] — le versant vectoriel
- [[Hybrid retrieval]] — la combinaison lexical + dense, native ici
- [[Late-interaction retrieval]] — supporté nativement : tenseurs multi-vecteurs, MaxSim, ColBERT
- [[Reranking]] — fait dans la couche de serving, en multi-phase ranking
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
