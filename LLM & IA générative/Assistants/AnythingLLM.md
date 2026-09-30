---
role: brique
nom: AnythingLLM
alias: [anythingllm, anything-llm, Mintplex AnythingLLM]
pitch: "Application de chat et de RAG par espaces de travail (MIT, Mintplex Labs) — bureau en un clic ou Docker multi-utilisateur, LanceDB embarqué, nombreux fournisseurs de modèles locaux, agents et MCP ; le SSO standard n'existe que dans l'offre Enterprise."
categorie: llm/assistant
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: JavaScript
scaling: single-node
alternatives: ["[[Open WebUI]]", "[[LibreChat]]"]
complements: ["[[Ollama]]", "[[LM Studio]]", "[[LiteLLM]]", "[[LanceDB]]", "[[Qdrant]]"]
tags: [llm, local-llm, rag, agents, mcp, self-hosted]
url_docs: https://docs.anythingllm.com/
url_repo: https://github.com/Mintplex-Labs/anything-llm
---

# AnythingLLM

<!-- AUTO:BANDEAU:START -->
> Application de chat et de RAG par espaces de travail (MIT, Mintplex Labs) — bureau en un clic ou Docker multi-utilisateur, LanceDB embarqué, nombreux fournisseurs de modèles locaux, agents et MCP ; le SSO standard n'existe que dans l'offre Enterprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript | open-source | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application de chat et de **RAG** organisée en **espaces de travail** : on y dépose des documents, on choisit un modèle, on discute. Trois formes à ne pas confondre : l'**application de bureau** (gratuite, un utilisateur, installation en un clic), l'**image Docker** (MIT, multi-utilisateur, widget embarquable, apparence personnalisable) et l'**offre hébergée** de Mintplex (Basic 50 $/mois, Pro 99 $/mois, Enterprise sur devis). Base vectorielle **LanceDB** embarquée par défaut, avec une dizaine d'autres au choix (Qdrant, pgvector, Milvus, Weaviate, Chroma…), et de nombreux fournisseurs de modèles locaux (Ollama, LM Studio, LocalAI, llama.cpp, LiteLLM). Agents avec compétences intégrées et flux, serveurs MCP. Backend Node.js, interface React. Version **v1.16.2** du 2026-09-22, 66 628 étoiles le 2026-09-30.

**Licence : MIT**, relue dans le dépôt, sans clause de marque ; l'apparence se personnalise dans l'image Docker. Une ESN peut déployer chez un client, changer la marque et redistribuer. Ce qui est réservé au payant : le **SSO**. Le mode Docker n'offre qu'un « Simple SSO passthrough » — une application tierce émet un jeton à usage unique de 10 minutes — et non OIDC, SAML ou LDAP ; ceux-ci ne sont cités que dans l'offre Enterprise hébergée ou sur site.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un RAG documentaire prêt en une heure, avec des espaces de travail par équipe et trois rôles (admin, manager, utilisateur) | L'annuaire d'entreprise (OIDC, SAML, LDAP) doit authentifier les utilisateurs sans payer → [[LibreChat]] ou [[Open WebUI]] |
| Un poste isolé ou un petit groupe, en bureau ou en Docker, sur des modèles locaux | Les droits doivent descendre au document ou à l'utilisateur dans un même espace : la granularité est l'espace de travail |
| Une licence MIT sans condition de marque pour l'installer chez un client | La base de données doit être PostgreSQL : SQLite est le défaut, et le schéma PostgreSQL n'est qu'un bloc commenté |
| Des modèles locaux variés sans passerelle | Le parsing de documents doit gérer des mises en page complexes → [[RAGFlow]], ou [[Docling]] en amont |

## Mise en œuvre

- Installation — application de bureau, ou image Docker `mintplexlabs/anythingllm` (amd64 et arm64, port 3001, volume de stockage, `JWT_SECRET` requis)
- Point d'entrée — interface web ; API documentée en Swagger sur `/api/docs`, clés d'API par compte
- Prérequis — 2 Go de RAM au minimum conseillés ; SQLite et LanceDB embarqués, aucun service externe obligatoire
- Exécution — mono-nœud ; le passage en mode multi-utilisateur est irréversible ; la télémétrie est active par défaut et se coupe avec `DISABLE_TELEMETRY=true`
- Coût — gratuit en bureau et en Docker ; l'offre hébergée et le SSO sont payants ; une trentaine d'avis de sécurité publiés, dont des contournements d'isolation entre utilisateurs en septembre 2026

## Écosystème

### Alternatives

- [[Open WebUI]] — Interface web de chat auto-hébergée pour modèles locaux (Ollama) et API OpenAI-compatibles, licence propre à clause de marque (BSD-3 + interdiction de retirer le nom et le logo au-delà de 50 utilisateurs, non OSI) — RAG, rôles et groupes, LDAP et OIDC, extensible par outils et fonctions Python.
- [[LibreChat]] — Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB.

### Compléments

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.

## Ressources

- Documentation — https://docs.anythingllm.com/
- Dépôt — https://github.com/Mintplex-Labs/anything-llm
- Documentation — offres et tarifs : https://anythingllm.com/pricing

## Voir aussi

- [[RAG documentaire on-prem - clé en main ou assemblé]] — la notion : ce que fige un RAG intégré
- [[Comparatif - Plateformes LLM auto-hébergées]] — le comparatif qui la situe
- [[Chunking strategies]] — la notion : le découpage que ses espaces de travail appliquent
- [[Assistants]] — le hub du dossier
