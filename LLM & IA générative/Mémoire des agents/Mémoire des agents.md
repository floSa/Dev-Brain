---
role: hub
nom: Mémoire des agents
alias: [mémoire des agents, mémoire d'agent persistante]
pitch: Garder ce qu'un agent a appris d'une session à l'autre — faits, graphe daté, contexte comprimé — sans envoyer les données chez un tiers.
domaines: [ai-eng]
tags: [agent-memory, agents, context-engineering, retrieval, knowledge-graph]
---

# Mémoire des agents

> Garder ce qu'un agent a appris d'une session à l'autre — faits, graphe daté, contexte comprimé — sans envoyer les données chez un tiers.

## Ce qu'il faut comprendre

- Un outil de mémoire fait deux métiers, et le dossier les sépare : **retenir** (extraire des faits d'une conversation et les ranger) et **rendre** (choisir ce qui revient dans la fenêtre de contexte). [[Agent memory]] pose la distinction ; [[Headroom]] n'est que le second métier, la compression.
- Presque tous **appellent un LLM à l'écriture**. [[Mem0]], [[Graphiti]] et [[Cognee]] extraient faits, entités ou graphe avec un modèle : le coût d'ingestion est un coût d'inférence, et la qualité dépend de la taille du modèle local. [[Graphiti]] en demande le plus (plusieurs appels par épisode, sortie structurée).
- La mémoire est un **modèle de données** avant d'être une base : une liste de faits par utilisateur ([[Mem0]]), un graphe où chaque fait a une fenêtre de validité ([[Graphiti]]), un graphe plus un index sur des documents ([[Cognee]]), des blocs que l'agent réécrit lui-même ([[Letta]]), un système de fichiers de contexte ([[OpenViking]]).
- **L'édition open source n'est pas la plateforme.** [[Mem0]] a retiré la mémoire graphe de son édition libre ; la Community Edition de Zep est arrêtée, [[Graphiti]] restant seul ; [[Letta]] a retiré son serveur d'API V1 et fait du Cloud son mode par défaut. Lire ce que le dépôt fait aujourd'hui, pas ce que la marque annonce.
- Le cloisonnement par utilisateur est **à la charge de qui exploite**, sauf pour [[Cognee]], qui l'intègre (jeux de données, rôles, permissions). Une mémoire qui fuit d'un client à l'autre est le risque d'une ESN.
- Deux licences à lire de près : [[OpenViking]] est sous **AGPL-3.0** (obligations de réciprocité si le service est offert à des tiers), et plusieurs outils envoient de la **télémétrie par défaut** (Mem0, Graphiti, Cognee) — à couper et à vérifier côté réseau.

## Choisir

- Retenir des préférences et des faits par utilisateur, en quelques lignes de code → [[Mem0]].
- Des faits qui changent dans le temps, avec leur provenance → [[Graphiti]], en acceptant d'exploiter une base de graphes.
- Mémoire et documents dans un même moteur, avec droits par jeu de données → [[Cognee]].
- Un agent qui apprend et réécrit sa propre mémoire → [[Letta]].
- Un contexte unifié, mémoires et skills en arborescence → [[OpenViking]].
- Réduire ce qui part vers le modèle sans rien perdre → [[Headroom]].
- Départager les six sur le stockage, les modèles locaux et la licence → [[Comparatif - Mémoire pour agents]].
- Une mémoire partagée entre CLI de code → [[ai-memory]], rangé dans les agents de code.

<!-- AUTO:START -->
### Notions
- [[Agent memory]] — domaines : ai-eng

### Briques
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.
- [[Graphiti]] — Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.
- [[Headroom]] — Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande.
- [[Letta]] — Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte.
- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

### Comparatifs
- [[Comparatif - Mémoire pour agents]]
<!-- AUTO:END -->
