---
role: brique
nom: RAGFlow
alias: [ragflow, infiniflow-ragflow, ragflow.io]
pitch: "Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache."
categorie: llm/rag
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: "Go, Python"
scaling: single-node
alternatives: ["[[LlamaIndex]]", "[[Haystack]]"]
complements: ["[[Elasticsearch]]", "[[MinIO]]", "[[MinerU]]", "[[Docling]]", "[[Ollama]]", "[[Text Embeddings Inference]]"]
tags: [llm, rag, retrieval, chunking, document-parsing, self-hosted]
url_docs: https://ragflow.io/docs
url_repo: https://github.com/infiniflow/ragflow
---

# RAGFlow

<!-- AUTO:BANDEAU:START -->
> Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go, Python | open-source | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Moteur RAG** livré comme un service complet : on dépose des documents, le moteur les **analyse par mise en page** (DeepDoc : détection de la structure, OCR, reconnaissance de tables), les découpe par **modèles de chunking** adaptés au type de document (général, Q&R, article, livre, tableau, présentation…), les indexe, puis répond avec des citations. S'y ajoutent la recherche hybride avec reranking, GraphRAG et RAPTOR, un canvas d'agents et de flux, un serveur MCP exposant l'outil `retrieve`, et une API. Le moteur de documents est configurable : Elasticsearch par défaut, Infinity, OpenSearch ou d'autres. Le consommateur nominal est autant un programme qu'une personne (API, SDK, MCP), d'où la famille `plateforme`.

Version **v1.0.0-rc1** du 2026-09-29, candidate de publication annoncée comme une réécriture en Go (API, administration, ingestion et synchronisation dans un service unique ; Redis remplacé par Kvrocks et NATS JetStream) ; la dernière ligne 0.x est la v0.27. La migration automatique depuis la v0.27.2 est irréversible. 91 554 étoiles le 2026-09-30.

**Licence : Apache-2.0**, relue dans le dépôt, sans clause de marque ni restriction multi-tenant. Une ESN peut déployer chez un client, retirer la marque et redistribuer. Un service payant existe (RAGFlow Cloud, plans de 0 à 259 $/mois et Enterprise sur devis), mais aucune édition sur site réservée n'a été trouvée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des documents à mise en page difficile (PDF scannés, tableaux, rapports) où la qualité du découpage décide de tout | Un simple chat sur quelques fichiers → [[AnythingLLM]] ou [[Open WebUI]] |
| Un moteur RAG à interroger par API depuis d'autres applications, sous Apache-2.0 | La machine dispose de moins de 4 cœurs, 16 Go de RAM et 50 Go de disque, le minimum conseillé |
| Des droits de partage par équipe sur des bases de connaissances | Un SSO d'entreprise complet : OIDC et OAuth2 sont des blocs de configuration, SAML et LDAP n'ont pas été trouvés |
| Un pipeline figé à faire évoluer peu, sans écrire de code d'assemblage | Une chaîne que l'on veut maîtriser brique par brique → [[LlamaIndex]], [[Haystack]] |

## Mise en œuvre

- Installation — Docker Compose à partir du dépôt, image unique par version ; aucun chart Helm officiel trouvé
- Point d'entrée — interface web pour les bases de connaissances et les agents ; API HTTP, SDK Python et serveur MCP
- Prérequis — MySQL, [[MinIO]], un cache (Redis, ou Kvrocks et NATS depuis la 1.0) et un moteur de documents, [[Elasticsearch]] par défaut (`vm.max_map_count` ≥ 262144)
- Exécution — mono-nœud ; modèles d'embedding et de langage à part ([[Ollama]], [[Text Embeddings Inference]]) ; [[MinerU]] ou [[Docling]] en service séparé pour le parsing
- Coût — gratuit en auto-hébergement ; le coût réel est celui de la machine et de l'exploitation ; 7 avis de sécurité, dont cinq critiques (injection de gabarit, exécution de code), et l'inscription libre est active par défaut : à désactiver derrière un SSO

## Écosystème

### Alternatives

- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[Dify]] — voisin : constructeur low-code dont la base de connaissances couvre le même besoin, dans une plateforme plus large.

### Compléments

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026.

## Ressources

- Documentation — https://ragflow.io/docs
- Dépôt — https://github.com/infiniflow/ragflow
- Dépôt — avis de sécurité : https://github.com/infiniflow/ragflow/security/advisories

## Voir aussi

- [[RAG documentaire on-prem - clé en main ou assemblé]] — la notion : ce qu'un moteur clé en main apporte et fige
- [[Comparatif - Plateformes LLM auto-hébergées]] — le comparatif qui la situe
- [[Chunking strategies]] — la notion : le découpage que ses modèles de chunking mettent en œuvre
- [[Hybrid retrieval]] — la notion : la recherche hybride qu'il active
- [[RAG & retrieval]] — le hub du dossier
