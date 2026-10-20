---
role: brique
nom: Ollama
alias: [ollama]
pitch: "Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]"]
complements: ["[[Open WebUI]]", "[[LibreChat]]", "[[AnythingLLM]]", "[[RAGFlow]]", "[[Mem0]]", "[[Graphiti]]", "[[Cognee]]"]
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://docs.ollama.com/
url_repo: https://github.com/ollama/ollama
---

# Ollama

<!-- AUTO:BANDEAU:START -->
> Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | à jour · 2026-09-05 |
<!-- AUTO:BANDEAU:END -->

## Définition

Runtime local qui enveloppe llama.cpp et lui ajoute ce qui manquait pour s'en servir sans y
penser : un registre de modèles (`ollama.com/library`), des **Modelfiles** à la Dockerfile
— modèle de base, paramètres, *system prompt* —, et un démon qui expose une **API REST**
native doublée d'un endpoint OpenAI-compatible sous `/v1`. `ollama run llama3` télécharge un
modèle quantifié et ouvre une session, sans configuration. Il utilise le GPU s'il en trouve un
(Metal, CUDA, ROCm) et retombe sur le CPU sinon — silencieusement, ce qui est sa principale
source de surprise.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Poste de dev ou prototypage : un LLM open qui tourne en une commande | Un modèle qui dépasse la VRAM bascule en RAM/CPU et ralentit fortement, sans erreur claire |
| Brancher une app sur un LLM local par l'API OpenAI-compatible, sans dépendre d'un fournisseur cloud | Contexte par défaut de 4 096 tokens, très en dessous de ce qu'exige un agent — à relever explicitement |
| Données sensibles à garder sur la machine, sans appel réseau | L'endpoint `/v1` casse le *tool calling* avec certains harnais : passer par l'API native |
| Comparer plusieurs modèles open rapidement, un `pull` par modèle | Modèles quantifiés par défaut, souvent en Q4 : la qualité est en retrait du poids plein si l'on ne choisit pas un tag plus précis |

## Mise en œuvre

- Installation — binaire macOS/Linux/Windows ou conteneur ; `ollama pull <modèle>` pour les poids
- Point d'entrée — la commande `ollama run`, et un démon HTTP sur `localhost:11434` (API native, plus `/v1` OpenAI-compatible)
- Prérequis — aucun au-delà du binaire ; le GPU est utilisé s'il est présent, sinon repli CPU
- Exécution — une instance par machine, mono-nœud, sans sharding multi-GPU ; une offre managée, Ollama Cloud, décharge les gros modèles
- Coût — gratuit, licence MIT ; seul Ollama Cloud est facturé à l'usage

## Écosystème

### Alternatives

- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

### Compléments

- [[Open WebUI]] — Interface web de chat auto-hébergée pour modèles locaux (Ollama) et API OpenAI-compatibles, licence propre à clause de marque (BSD-3 + interdiction de retirer le nom et le logo au-delà de 50 utilisateurs, non OSI) — RAG, rôles et groupes, LDAP et OIDC, extensible par outils et fonctions Python.
- [[LibreChat]] — Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB.
- [[AnythingLLM]] — Application de chat et de RAG par espaces de travail (MIT, Mintplex Labs) — bureau en un clic ou Docker multi-utilisateur, LanceDB embarqué, nombreux fournisseurs de modèles locaux, agents et MCP ; le SSO standard n'existe que dans l'offre Enterprise.
- [[RAGFlow]] — Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.
- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[Graphiti]] — Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.

## Ressources

- Documentation — https://docs.ollama.com/
- Dépôt — https://github.com/ollama/ollama

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que le moteur optimise
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Pattern - Agent sur LLM auto-hébergé]] — le montage complet, d'où viennent les deux bornes `/v1` et 4 096 tokens
- [[HuggingFace]] — d'où viennent les poids, convertis en GGUF
- [[Contexte long]] — le coût mémoire du cache KV par séquence et ce que valent les longueurs annoncées
- [[Quantification des LLM - GGUF, AWQ, GPTQ]] — formats, matériel pris en charge et pièges de la quantification pour servir un LLM
