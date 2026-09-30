---
role: notion
nom: RAG documentaire on-prem - clé en main ou assemblé
alias: [RAG documentaire on-prem, RAG on-prem, "RAG documentaire on-prem : clé en main ou assemblé", moteur RAG clé en main, RAG clé en main ou assemblé, RAG interne]
categorie: llm/rag
domaines: [ai-eng]
tags: [rag, llm, retrieval, local-llm, self-hosted]
---

# RAG documentaire on-prem - clé en main ou assemblé

> Notion de décision, datée du 2026-09-30 : les versions et les comptes de services citent les sources lues ce jour-là. Le principe du RAG, le découpage, la recherche hybride et l'évaluation sont dans [[RAG]], [[Advanced RAG]], [[Chunking strategies]] et [[RAG eval]] ; cette page ne les répète pas.

## Aperçu

- Le besoin récurrent en contexte industriel ou ESN : un assistant interne branché sur des modèles locaux et sur les documents du client, avec l'authentification d'entreprise et sans envoi de données à l'extérieur. Deux façons d'y répondre : une **plateforme clé en main** (parsing, index, chat et droits livrés ensemble) ou un **assemblage** (une bibliothèque d'orchestration, une base vectorielle, un reranker, un parseur, et une interface à fournir).
- L'arbitrage ne porte pas sur la qualité de réponse — elle dépend du découpage, de la récupération et du parsing, quelle que soit la forme — mais sur **ce qu'on accepte d'opérer et de figer**.

## Concepts clés

### Ce qu'un moteur clé en main apporte
- **Une chaîne complète déjà câblée** : dépôt de fichiers, extraction du texte, découpage, embeddings, index, chat avec citations, comptes utilisateurs, console d'administration. Un pilote tient en une journée.
- **Les droits et le multi-utilisateur livrés** : [[Open WebUI]] (rôles, groupes, collections de connaissances soumises aux permissions), [[AnythingLLM]] (trois rôles, espaces de travail), [[LibreChat]] (panneau d'administration, agents partagés par groupe), [[RAGFlow]] (équipes, partage des bases de connaissances, permissions sur les documents).
- **Un parsing plus ou moins poussé selon le moteur** : [[RAGFlow]] analyse la mise en page (DeepDoc : structure, OCR, tables) et des modèles de découpage par type de document ; [[Open WebUI]] délègue l'extraction à un moteur au choix (Tika, [[Docling]], [[MinerU]]…) ; [[AnythingLLM]] embarque des lecteurs de fichiers simples.

### Ce qu'il fige
- **Le pipeline est une liste d'options**, pas du code. Changer de stratégie de découpage, insérer une étape de réécriture de requête ou un reranker qui n'est pas prévu oblige à attendre le moteur ou à le forker. Les réglages existent, l'étape inédite n'existe pas.
- **Les composants sont choisis par le moteur** : la base vectorielle par défaut (LanceDB pour [[AnythingLLM]], Chroma sur SQLite pour [[Open WebUI]], qui n'est pas sûr en multi-instance), le service RAG de [[LibreChat]] sur PostgreSQL et pgvector, le moteur de documents de [[RAGFlow]]. On change de base vectorielle quand le moteur la supporte, pas quand on le décide.
- **La licence et la roadmap sont celles de l'éditeur.** Clause de marque pour [[Open WebUI]], SSO réservé à l'offre payante pour [[AnythingLLM]], rachat par ClickHouse pour [[LibreChat]], réécriture en Go en candidate de publication pour [[RAGFlow]] : voir [[Comparatif - Plateformes LLM auto-hébergées]].
- **L'évaluation reste extérieure.** Aucune des quatre lectures n'a relevé d'outil d'évaluation intégré de la récupération : il faut constituer un jeu de questions et le rejouer par l'API, comme pour n'importe quelle boîte noire.

### Ce qu'un assemblage apporte
- **Chaque pièce se choisit et se teste** : parseur ([[Docling]], [[MinerU]], [[Marker]]), découpage, embeddings ([[sentence-transformers]], [[Text Embeddings Inference]], [[bge-m3]]), base ([[Qdrant]], [[Milvus]], [[pgvector]], [[Elasticsearch]]), reranker ([[bge-reranker]]), orchestration ([[LlamaIndex]] ou [[Haystack]]).
- **La récupération se règle étage par étage**, et chaque étage se mesure séparément avec [[RAG eval]] ; c'est ce qui permet d'aller au-delà des options d'un moteur.
- **Le prix** : l'interface, l'authentification, les droits, l'administration et les mises à jour de sécurité sont à fournir — ou à brancher sur une interface de chat ([[Open WebUI]], [[LibreChat]]) qui appelle le pipeline comme un modèle ou un outil.

### Droits d'accès aux documents
- **Le risque est documenté** : l'OWASP classe en LLM08:2025 (*Vector and Embedding Weaknesses*) l'accès non autorisé et la fuite de données par des contrôles d'accès insuffisants ou mal alignés sur les embeddings — un document que l'utilisateur ne peut pas ouvrir ne doit pas pouvoir remonter dans le contexte.
- **La règle tient à un endroit** : le filtre par utilisateur ou par groupe s'applique à la **récupération**, côté serveur, sur des métadonnées posées à l'indexation — jamais dans le prompt. Les moteurs clés en main le font à la granularité de leur objet : la collection de connaissances pour [[Open WebUI]], l'espace de travail pour [[AnythingLLM]] (la granularité au document ou à l'utilisateur dans un espace n'a pas été trouvée), la base de connaissances et le document pour [[RAGFlow]]. Un assemblage doit l'écrire lui-même.
- **Synchroniser les droits avec l'annuaire** est un second problème : quand un utilisateur quitte un groupe, l'index ne le sait pas tant que rien ne met à jour les métadonnées. [[Keycloak]] ou [[Authentik]] authentifient ; ils ne propagent pas les droits sur les documents.

### Mise à jour de l'index
- **Un document modifié, renommé ou supprimé doit sortir de l'index** ; sinon l'assistant cite une version périmée ou un fichier retiré. Changer de modèle d'embedding impose de tout réindexer.
- **Clé en main** : la mise à jour passe par la console ou l'API du moteur ; [[RAGFlow]] annonce un service de synchronisation dans sa version 1.0 en candidate de publication. La couverture des sources de fichiers réelles (partages réseau, GED) est à vérifier moteur par moteur.
- **Assemblé** : [[LlamaIndex]] tient une table identifiant → empreinte de document (avec un docstore) et ne retraite que ce qui a changé ; [[Haystack]] gère les doublons par une politique d'écriture (ignorer ou écraser). La suppression des documents disparus reste à coder.

### Coût d'exploitation d'une plateforme à maintenir
- **Services à opérer**, d'après les déploiements officiels lus : [[AnythingLLM]], un conteneur avec SQLite et LanceDB ; [[Open WebUI]], un conteneur par défaut, puis [[Postgres]], Redis, une base vectorielle externe et un stockage partagé en multi-instance ; [[LibreChat]], [[MongoDB]] obligatoire, plus un service RAG sur [[pgvector]] ; [[RAGFlow]], MySQL, [[MinIO]], un cache et un moteur de documents, pour 4 cœurs, 16 Go de RAM et 50 Go de disque au minimum conseillé.
- **Sécurité** : les quatre dépôts publient des avis en nombre (une centaine pour Open WebUI entre mai et septembre 2026, dont un critique, 29 pour LibreChat, une trentaine pour AnythingLLM, sept pour RAGFlow dont cinq critiques). Une plateforme à maintenir est une plateforme à mettre à jour : épingler les versions, suivre les avis, couper l'inscription libre.
- **La version compte** : RAGFlow est en 1.0.0-rc1 depuis le 2026-09-29, avec une migration irréversible depuis la ligne 0.27 ; LibreChat n'a que des préversions sur GitHub. Ne pas prendre la dernière étiquette sans la lire.

## En pratique

- **Pilote ou moins de quelques dizaines d'utilisateurs, documents courants** → un clé en main : [[AnythingLLM]] pour aller vite, [[Open WebUI]] ou [[LibreChat]] quand le SSO et les groupes comptent (voir leurs licences).
- **Documents à mise en page difficile (scans, tableaux, rapports)** → [[RAGFlow]], ou un parseur ([[Docling]], [[MinerU]]) placé devant n'importe quel moteur.
- **Récupération à optimiser, droits fins au document, sources multiples** → un assemblage, derrière une interface de chat existante.
- **Commencer clé en main, prévoir la sortie** : garder les documents sources et leurs métadonnées hors du moteur, et consigner les réglages de découpage ; un moteur qu'on quitte se remplace alors par un assemblage sans tout reconstruire.
- **ESN** : avant de livrer chez un client, relire la licence de la plateforme (clause de marque, multi-tenant, SSO payant) et celle du modèle ([[Licences de modèles open weights]]).

## Approches voisines & alternatives

- [[Open WebUI]] · [[LibreChat]] · [[AnythingLLM]] · [[RAGFlow]] — les quatre moteurs clé en main lus pour cette page.
- [[Dify]] · [[Langflow]] — constructeurs visuels dont la base de connaissances couvre le même besoin ; [[Flowise]] est archivé.
- [[LlamaIndex]] · [[Haystack]] — l'assemblage en bibliothèque.
- [[Comparatif - Plateformes LLM auto-hébergées]] — ce que chaque plateforme permet, licence et SSO compris.
- [[Reranking]] · [[Hybrid retrieval]] · [[GraphRAG]] — ce qu'un assemblage peut ajouter et qu'un moteur propose ou non.

## Pour aller plus loin

- OWASP GenAI Security Project, *LLM08:2025 Vector and Embedding Weaknesses* — https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
- LlamaIndex, *Ingestion Pipeline — Document Management* — https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/
- Haystack, *Document Store — DuplicatePolicy* — https://docs.haystack.deepset.ai/docs/document-store
- RAGFlow, dépôt et README — https://github.com/infiniflow/ragflow
- Open WebUI, documentation — https://docs.openwebui.com/
