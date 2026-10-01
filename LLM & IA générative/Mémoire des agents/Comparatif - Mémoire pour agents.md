---
role: comparatif
nom: Comparatif - Mémoire pour agents
categorie: llm/memoire
tags: [agent-memory, agents, retrieval]
---

# Comparatif - Mémoire pour agents

> On tranche sur : le modèle de mémoire — liste de faits, graphe daté, blocs que l'agent réécrit, arborescence de contexte, compression — puis sur ce qui reste à la charge de l'opérateur (stockage, cloisonnement des utilisateurs, exploitation) et sur la licence, car trois outils sur six ont une offre cloud qui concentre une partie des fonctions. Un membre du lot ne retient rien : [[Headroom]] comprime ce qui part vers le modèle.

![[Comparatif - Mémoire pour agents.base]]

## Ce qui départage

- [[Cognee]] — **le seul qui mêle mémoire et connaissance documentaire, avec droits par jeu de données** : graphe construit par LLM ou GLiNER, index vectoriel, et authentification, rôles et permissions actifs par défaut. Pile locale sans clé possible (SQLite, LanceDB, Kuzu, FastEmbed), mais Kuzu est jugé non recommandé en production par sa propre doc, et l'adaptateur Postgres de production est un produit sous licence. Beta, une version par semaine. Apache-2.0.
- [[Graphiti]] — **le seul à faits datés** : chaque fait porte `valid_at` et `invalid_at`, un fait contredit est invalidé et non supprimé, chaque fait renvoie à son épisode. Un moteur, pas une plateforme : la Community Edition de Zep est arrêtée. Exige une base de graphes (Neo4j, FalkorDB, Neptune), plusieurs appels LLM par épisode et un modèle à sortie structurée. Beta. Apache-2.0.
- [[Headroom]] — **ne mémorise rien** : couche de compression, locale et réversible, entre l'application et le modèle ; l'original reste en local et le modèle le redemande par `headroom_retrieve`. À poser à côté d'un des autres, pas à leur place. Beta. Apache-2.0.
- [[Letta]] — **la mémoire que l'agent édite lui-même** : blocs de mémoire et skills réécrits par l'agent, système de fichiers versionné par git. C'est un harnais d'agents complet (CLI, bureau, serveur d'application), pas une brique à brancher. Cloud par défaut, mode local sans compte avec Ollama, LM Studio, llama.cpp. Le serveur d'API V1 est retiré. Apache-2.0.
- [[Mem0]] — **le plus simple à brancher** : faits extraits en un appel LLM, rangés par `user_id`, `agent_id` ou `run_id`, `add` et `search`. Vector store au choix (Qdrant par défaut, pgvector, Milvus, Weaviate…), serveur Docker avec clés par utilisateur. **Open-core** : la mémoire graphe est retirée de l'édition libre, et le serveur MCP officiel est hébergé. Apache-2.0.
- [[OpenViking]] — **le seul à contexte en arborescence** : mémoires, documents et skills exposés en système de fichiers `viking://`, chargés à trois niveaux de détail (L0, L1, L2). Beta, voire alpha d'après PyPI. **AGPL-3.0** : le seul du lot à licence copyleft réseau, donc à lire avant d'offrir le service à un tiers.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
