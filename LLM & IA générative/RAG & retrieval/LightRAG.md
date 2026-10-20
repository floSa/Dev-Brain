---
role: brique
nom: LightRAG
alias: [lightrag-hku, HKUDS/LightRAG, LightRAG Server]
pitch: "Framework RAG sur graphe (HKUDS, MIT) — extraction d'entités et de relations par LLM, récupération à deux niveaux (détails et concepts) sur graphe et vecteurs, ajout et suppression incrémentaux de documents ; serveur avec interface web et API, v1.5.7 en septembre 2026."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Microsoft GraphRAG]]"]
tags: [rag, knowledge-graph, retrieval, graph-db, llm]
url_docs: https://github.com/HKUDS/LightRAG
url_repo: https://github.com/HKUDS/LightRAG
---

# LightRAG

<!-- AUTO:BANDEAU:START -->
> Framework RAG sur graphe (HKUDS, MIT) — extraction d'entités et de relations par LLM, récupération à deux niveaux (détails et concepts) sur graphe et vecteurs, ajout et suppression incrémentaux de documents ; serveur avec interface web et API, v1.5.7 en septembre 2026.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Une bibliothèque Python et un **serveur** (interface web et API REST) de RAG sur graphe, de l'équipe HKUDS (Université de Hong Kong), décrits par l'article *LightRAG: Simple and Fast Retrieval-Augmented Generation* (arXiv 2410.05779, EMNLP 2025 d'après le dépôt). Un LLM extrait les **entités et les relations** de chaque morceau de texte et en tire un graphe de connaissances ; le graphe et les vecteurs forment un index à deux étages. La récupération est à **deux niveaux** : des détails (entités, relations) et des concepts (thèmes), combinés avec les passages sources. Le dépôt s'oppose à [[Microsoft GraphRAG]] : **pas de communautés ni de rapports de communautés**, donc moins d'appels de modèle à l'indexation et à la requête selon le dépôt, et un algorithme d'**ajout incrémental** qui évite de reconstruire l'index. Licence MIT, version 1.5.7 sur PyPI (`lightrag-hku`, 2026-09-02), dernier push 2026-10-15.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un corpus qui **change** : ajout de documents sans reconstruire l'index, suppression d'un document avec régénération des seuls nœuds touchés (via le cache LLM de l'indexation) | Un corpus **stable** à interroger surtout par des questions de synthèse sur tout le corpus : [[Microsoft GraphRAG]] a des rapports de communauté pour cela |
| Un **serveur prêt** : interface web, API REST, déploiement Docker, assistant de configuration, mode hors-ligne documenté | Un serveur exposé sans réglage : par défaut, il **écoute sur toutes les interfaces** et, sans clé ou compte configuré, **chaque point d'accès est public** (avertissement du README) |
| Du **graphe et du vectoriel** dans un même outil, avec reranker, citations et évaluation (RAGAS, Langfuse) | Un **LLM d'extraction faible** : l'extraction d'entités et de relations exige plus du modèle qu'un RAG classique ; le README recommande un modèle sans raisonnement et, en local, au moins un Qwen3-30B-A3B-Instruct |
| Des documents riches (images, tableaux, formules) : parseurs MinerU, Docling ou natif | La **production avec les stockages par défaut** : mémoire et fichiers locaux, « pas pour la production » ; PostgreSQL recommandé |

## Mise en œuvre

- Installation — `uv tool install "lightrag-hku[api]"` pour le serveur ; `uv add lightrag-hku` pour la bibliothèque ; Docker Compose depuis le dépôt
- Point d'entrée — `lightrag-server` (après un fichier `.env` : LLM, embeddings, reranker) ; l'assistant `make env-base` génère la configuration
- Prérequis — quatre rôles de modèle configurables séparément : extraction (`EXTRACT`), requête (`QUERY`), mots-clés (`KEYWORDS`), vision (`VLM`) ; un modèle d'embedding ; une authentification (`LIGHTRAG_API_KEY` ou comptes) avant toute exposition réseau
- Exécution — local ou sur site ; stockages au choix : PostgreSQL (recommandé), Neo4j, MongoDB, OpenSearch, Milvus ; parseurs [[Docling]] et [[MinerU]]
- Coût — gratuit sous MIT ; le coût est celui des appels de modèle à l'indexation (une extraction par morceau)

## Limites à connaître

- **Gains annoncés par l'éditeur** : le dépôt et l'article affirment un meilleur rapport qualité-coût que GraphRAG de Microsoft ; **aucune mesure indépendante** n'est retenue ici, et aucun classement avec [[Microsoft GraphRAG]] n'est établi.
- **Qualité d'extraction** : elle dépend du modèle d'extraction ; une relation extraite à tort entre dans le graphe. Aucun taux d'erreur publié.
- **Un graphe n'est pas toujours utile** : une étude tierce (Xiang et al., arXiv 2506.05690) rapporte qu'un RAG sur graphe sous-performe souvent un RAG vectoriel sur des tâches réelles ([[GraphRAG]]) ; mesurer sur ses questions.
- **Rythme de changement** : le journal du dépôt est dense (nouveautés mensuelles en 2026) ; épingler la version et relire les notes avant une mise à jour.

## Écosystème

### Alternatives

- [[Microsoft GraphRAG]] — Bibliothèque Python de recherche (Microsoft, MIT) qui extrait un graphe d'un corpus par LLM, le découpe en communautés avec un rapport par communauté, puis répond en recherche locale, globale ou DRIFT ; projet en mode maintenance (corrections et mises à jour de dépendances seulement), v3.3.0 en octobre 2026. — avec communautés et rapports (donc la recherche globale), mais indexation plus lourde et projet figé.

## Ressources

- Documentation — dépôt et README : https://github.com/HKUDS/LightRAG
- Article — Guo et al., *LightRAG: Simple and Fast Retrieval-Augmented Generation*, arXiv 2410.05779 : https://arxiv.org/abs/2410.05779
- Paquet — https://pypi.org/project/lightrag-hku/
- Vidéo — « RAG vs GRAPH RAG. Lequel choisir ? », Benoit Ferrere, 2 min 46 : https://www.youtube.com/watch?v=ZaOMbq3c0Jg (frameworks et bases de graphes à 1 min 56)

## Voir aussi

- [[GraphRAG]] — la notion : ce qu'est un RAG sur graphe, local et global
- [[Construction de graphes de connaissances]] — l'extraction d'entités et de relations
- [[RAG & retrieval]] — le hub du dossier, avec la comparaison des deux frameworks de graphe
- [[Graphe de connaissances]] — ce qu'est le graphe qu'on construit
