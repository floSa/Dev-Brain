---
role: hub
nom: LLM & IA générative
alias: [genai, ia générative, applications LLM]
pitch: Construire avec des modèles de langage — les faire tourner, les brancher sur de la donnée, leur donner des outils, et mesurer ce qu'ils valent.
domaines: [ai-eng]
tags: [llm, rag, agents, llm-eval, llm-observability, mcp, structured-output, llm-gateway]
---

# LLM & IA générative

> Construire avec des modèles de langage — les faire tourner, les brancher sur de la donnée, leur donner des outils, et mesurer ce qu'ils valent.

## Ce qu'il faut comprendre

- Les six sous-dossiers sont **six métiers distincts**, pas six étages du même : où le modèle s'exécute ([[Runtimes]]), la bibliothèque avec laquelle on écrit un agent ([[Agents]]), l'agent déjà écrit qui édite du code ([[Agents de code]]), l'application prête à déployer devant un utilisateur ([[Assistants]]), l'ajustement des poids ([[Fine-tuning]]), et la seule verticale assez fournie pour tenir son propre dossier ([[Text-to-SQL]]). Ce qui reste au niveau du domaine est ce qui **traverse** ces six : le socle de framework, le RAG, la sortie structurée, la passerelle, l'éval, l'observabilité, la mémoire, MCP, le low-code.
- L'arbitrage qui vient en premier, et qui est presque toujours mal posé : **prompt, RAG ou fine-tune**. Le prompt change le comportement, le RAG change les connaissances disponibles, le fine-tune change les deux au prix d'une chaîne d'entraînement à tenir. La question n'est pas « lequel est le meilleur » mais « qu'est-ce qui manque au modèle » — de l'instruction ([[Prompt engineering]]), du fait ([[RAG]]), ou de la forme ([[SFT]]). Se tromper de levier coûte des semaines.
- Un LLM ne voit que des **tokens**, et plusieurs surprises d'usage viennent de là : [[Tokenization]] explique pourquoi un modèle compte mal les lettres d'un mot et pourquoi une facture n'est pas proportionnelle au nombre de mots. Ce qu'il produit, token par token, dépend d'une [[Decoding strategies|stratégie de décodage]] ; sa qualité intrinsèque se mesure encore par la [[Perplexity]] — utile pour comparer deux modèles sur un corpus, inutile pour juger une application. Ce que la taille achète, et ce qu'elle n'achète pas, est décrit par les [[Scaling laws]] ; leur revers est tout l'intérêt des [[Small Language Models]].
- Le **contexte est la vraie interface** du modèle, pas le prompt. [[Prompt engineering]] est l'artisanat de la formulation ; [[Context engineering]] est la gestion d'un budget — quoi charger, quand, dans quel ordre, et quoi jeter. C'est là que se joue le coût réel d'une application, avec le [[prompt-caching]] côté fournisseur et le [[LLM caching]] côté application. Faire raisonner explicitement ([[Chain-of-Thought]]) est un choix de contexte ; les [[Reasoning models]] l'internalisent et déplacent le coût vers la génération.
- **Deux façons de faire sortir autre chose que du texte**, régulièrement confondues. La [[Structured outputs|sortie structurée]] contraint la génération à respecter un schéma : c'est du décodage, et ça garantit une **forme** ([[Instructor]], [[Outlines]], [[Guidance]]). Le [[tool-use|tool use]] laisse le modèle demander qu'on exécute une fonction : c'est un protocole d'échange, et ça déclenche un **effet**. La première ne fait rien arriver, le second n'assure aucune forme.
- Le **RAG est un problème de recherche** avant d'être un problème de LLM, et son plafond de qualité est celui du retrieval, pas celui du modèle. [[RAG]] pose le principe et [[Advanced RAG]] ce qu'on lui ajoute quand la version naïve plafonne : [[Chunking strategies]] décide de ce qui est indexable, [[Hybrid retrieval]] combine dense et lexical parce que ni l'un ni l'autre ne suffit seul, [[Reranking]] et [[Late-interaction retrieval]] rattrapent la précision perdue au premier passage, [[Query transformations]] traite les questions mal posées, [[Routing and cascading]] envoie chaque requête au bon index et au bon modèle. Quand la réponse exige de relier des faits épars, on passe au graphe : [[GraphRAG]] et [[Construction de graphes de connaissances]].
- **Sans éval, il n'y a pas de progrès mesurable** — c'est la faiblesse la plus répandue des applications LLM, et elle ne se voit pas de l'intérieur. [[LLM eval metrics]] et [[LLM benchmarks]] jugent le modèle, [[RAG eval]] et [[RAG benchmarks]] jugent le pipeline, [[LLM-as-judge]] permet de noter à l'échelle — en assumant qu'un juge est lui-même un modèle biaisé, à calibrer contre des annotations humaines.
- L'**observabilité** n'est pas l'éval : elle regarde la production, pas un jeu de tests. [[LLM observability]] — traces imbriquées d'appels et d'outils, latence, tokens, coût par requête. Le premier critère de choix entre les plateformes est l'auto-hébergement, le second l'attachement à un framework.
- Une application qui parle à un seul fournisseur est un point de rupture unique. La **passerelle** unifie le format d'appel, route, et permet le repli : c'est le préalable matériel des [[Reliability patterns]], au même titre que les délais, les reprises et la dégradation gracieuse. Et l'action irréversible se fait valider par quelqu'un — [[Human-in-the-loop]].
- La **mémoire** est le manque structurel du modèle : son contexte s'arrête à la fin de la conversation. [[Agent memory]] décrit ce qu'on remet en jeu d'une session à l'autre, et les trois briques du domaine attaquent le problème par trois bouts : [[Letta]] en fait une hiérarchie que l'agent s'auto-édite, [[Headroom]] comprime le contexte de façon réversible, [[OpenViking]] l'expose en système de fichiers parcourable.
- **MCP est devenu la prise standard** entre un modèle et des outils, et c'est ce qui rend un outil réutilisable d'un agent à l'autre : [[mcp-protocol]] pour le protocole, [[fastmcp]] pour écrire un serveur, [[mcpjam]] pour le déboguer.
- Fabriquer ses données d'entraînement avec un modèle est devenu la norme du post-training : [[Synthetic data generation]], à lire avec [[Fine-tuning]].
- La **sécurité de ces systèmes** est un sujet entier, et ses notions portent encore `concept/ai` : [[Prompt injection]], [[Jailbreaking and defenses]], [[Guardrails]] et [[AI security]] sont dans la liste « Hors arbre » de l'arborescence v3 et relèvent du lot 4. Cf. [[Sécurité]], qui le dit dans l'autre sens.

## Choisir

- Faire tourner un modèle ouvert, en local ou sur GPU → [[Runtimes]].
- Écrire un agent en Python → [[Agents]].
- Un agent qui édite déjà du code dans mon dépôt → [[Agents de code]].
- Une application conversationnelle prête à déployer → [[Assistants]].
- Ajuster les poids d'un modèle sur mon domaine → [[Fine-tuning]].
- Interroger une base relationnelle en langage naturel → [[Text-to-SQL]].
- Le socle générique pour composer chaînes et agents → [[LangChain]] ; optimiser les prompts au lieu de les écrire → [[DSPy]].
- Brancher un LLM sur mes documents → [[LlamaIndex]], ou [[Haystack]] pour des pipelines explicites ; du ColBERT dans le pipeline → [[RAGatouille]].
- Garantir un objet typé en sortie → [[Instructor]] si Pydantic suffit, [[Outlines]] pour une grammaire ou une regex, [[Guidance]] pour entrelacer contrôle et génération.
- Appeler plusieurs fournisseurs derrière une API unique → [[LiteLLM]] en self-host, [[OpenRouter]] en managé, [[OmniRoute]] si le repli sur quota est le besoin principal.
- Mesurer un pipeline RAG → [[Ragas]] ; en faire des tests exécutés en CI → [[DeepEval]] ; comparer des prompts et chercher les failles → [[promptfoo]] ; instrumenter un stack existant → [[TruLens]].
- Voir ce qui se passe en production → [[Langfuse]] (open-core, self-host), [[Phoenix Arize]] (OpenTelemetry), [[LangSmith]] (managé, écosystème LangChain), [[Helicone]] (proxy — mais en maintenance).
- Assembler un workflow sans écrire de code → [[Dify]] pour la plateforme complète, [[Langflow]] ou [[Flowise]] pour un canvas exportable.
- Exposer mes outils à n'importe quel agent → [[fastmcp]], puis [[mcpjam]] pour vérifier.
- Garder de la mémoire entre les sessions → [[Letta]] ; réduire le contexte sans le perdre → [[Headroom]].
- Savoir quel modèle local tient sur ma machine → [[llmfit]].
- Entraîner un modèle depuis zéro, ou produire autre chose que du texte → [[Machine Learning]], pas ce domaine.

<!-- AUTO:START -->
### Sous-domaines
- [[Agents]] · [[Agents de code]] · [[Assistants]] · [[Fine-tuning]] · [[Runtimes]] · [[Text-to-SQL]]

### Briques
- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.
- [[fastmcp]] — La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma.
- [[Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.
- [[Guidance]] — Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[Headroom]] — Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande.
- [[Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.
- [[Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[llmfit]] — CLI Rust (MIT) qui détecte le matériel — RAM, CPU, GPU, VRAM, backend d'accélération — puis classe des centaines de modèles locaux sur quatre axes : tenue en mémoire, vitesse estimée, qualité et contexte ; TUI interactive, mode script et benchmarks communautaires.
- [[mcpjam]] — « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM.
- [[OmniRoute]] — Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.
- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.
- [[Outlines]] — Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas.
- [[Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.
- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[RAGatouille]] — Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025).
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

### Comparatifs
- [[Comparatif - Frameworks LLM]]
- [[Comparatif - Observabilité LLM]]
- [[Comparatif - Évaluation LLM]]
<!-- AUTO:END -->
