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

- Les **douze sous-dossiers sont douze métiers distincts**, pas douze étages du même — et ils se lisent en trois groupes. **Le modèle** : ce qu'il est ([[Modèles de langage]]), où il s'exécute ([[Runtimes]]), comment on l'ajuste ([[Fine-tuning]]). **Ce qu'on construit avec** : la bibliothèque avec laquelle on écrit un agent ([[Agents]]), l'agent déjà écrit qui édite du code ([[Agents de code]]), l'application prête à déployer ([[Assistants]]), l'ancrage sur des documents ([[RAG & retrieval]]), la contrainte de forme ([[Sortie typée]]), l'API unique devant les fournisseurs ([[Passerelles]]), et la seule verticale assez fournie pour tenir son propre dossier ([[Text-to-SQL]]). **Ce qui dit si ça marche** : le jeu de tests ([[Évaluation]]) et la production ([[Observabilité des LLM]]). Ce qui reste au niveau du domaine est ce qui **traverse** ces douze : le socle de framework, le prompt et le contexte, la mémoire, les protocoles, le low-code, l'outillage de choix de modèle.
- L'arbitrage qui vient en premier, et qui est presque toujours mal posé : **prompt, RAG ou fine-tune**. Le prompt change le comportement, le RAG change les connaissances disponibles, le fine-tune change les deux au prix d'une chaîne d'entraînement à tenir. La question n'est pas « lequel est le meilleur » mais « qu'est-ce qui manque au modèle » — de l'instruction ([[Prompt engineering]]), du fait ([[RAG]]), ou de la forme ([[SFT]]). Se tromper de levier coûte des semaines.
- Un LLM ne voit que des **tokens**, et plusieurs surprises d'usage viennent de là — les six pages de ce paragraphe vivent dans [[Modèles de langage]] : [[Tokenization]] explique pourquoi un modèle compte mal les lettres d'un mot et pourquoi une facture n'est pas proportionnelle au nombre de mots. Ce qu'il produit, token par token, dépend d'une [[Decoding strategies|stratégie de décodage]] ; sa qualité intrinsèque se mesure encore par la [[Perplexity]] — utile pour comparer deux modèles sur un corpus, inutile pour juger une application. Ce que la taille achète, et ce qu'elle n'achète pas, est décrit par les [[Scaling laws]] ; leur revers est tout l'intérêt des [[Small Language Models]].
- Le **contexte est la vraie interface** du modèle, pas le prompt. [[Prompt engineering]] est l'artisanat de la formulation ; [[Context engineering]] est la gestion d'un budget — quoi charger, quand, dans quel ordre, et quoi jeter. C'est là que se joue le coût réel d'une application, avec le [[prompt-caching]] côté fournisseur et le [[LLM caching]] côté application. Faire raisonner explicitement ([[Chain-of-Thought]]) est un choix de contexte ; les [[Reasoning models]] l'internalisent et déplacent le coût vers la génération.
- **Deux façons de faire sortir autre chose que du texte**, régulièrement confondues. La [[Structured outputs|sortie structurée]] contraint la génération à respecter un schéma : c'est du décodage, et ça garantit une **forme** ([[Instructor]], [[Outlines]], [[Guidance]]). Le [[tool-use|tool use]] laisse le modèle demander qu'on exécute une fonction : c'est un protocole d'échange, et ça déclenche un **effet**. La première ne fait rien arriver, le second n'assure aucune forme.
- Le **RAG est un problème de recherche** avant d'être un problème de LLM, et son plafond de qualité est celui du retrieval, pas celui du modèle. [[RAG]] pose le principe et [[Advanced RAG]] ce qu'on lui ajoute quand la version naïve plafonne : [[Chunking strategies]] décide de ce qui est indexable, [[Hybrid retrieval]] combine dense et lexical parce que ni l'un ni l'autre ne suffit seul, [[Reranking]] et [[Late-interaction retrieval]] rattrapent la précision perdue au premier passage, [[Query transformations]] traite les questions mal posées, [[Routing and cascading]] envoie chaque requête au bon index et au bon modèle. Quand la réponse exige de relier des faits épars, on passe au graphe : [[GraphRAG]] et [[Construction de graphes de connaissances]].
- **Sans éval, il n'y a pas de progrès mesurable** — c'est la faiblesse la plus répandue des applications LLM, et elle ne se voit pas de l'intérieur. [[LLM eval metrics]] et [[LLM benchmarks]] jugent le modèle, [[RAG eval]] et [[RAG benchmarks]] jugent le pipeline, [[LLM-as-judge]] permet de noter à l'échelle — en assumant qu'un juge est lui-même un modèle biaisé, à calibrer contre des annotations humaines.
- L'**observabilité** n'est pas l'éval : elle regarde la production, pas un jeu de tests. [[LLM observability]] — traces imbriquées d'appels et d'outils, latence, tokens, coût par requête. Le premier critère de choix entre les plateformes est l'auto-hébergement, le second l'attachement à un framework.
- Une application qui parle à un seul fournisseur est un point de rupture unique. La **passerelle** unifie le format d'appel, route, et permet le repli : c'est le préalable matériel des [[Reliability patterns]], au même titre que les délais, les reprises et la dégradation gracieuse. Et l'action irréversible se fait valider par quelqu'un — [[Human-in-the-loop]].
- La **mémoire** est le manque structurel du modèle : son contexte s'arrête à la fin de la conversation. [[Agent memory]] décrit ce qu'on remet en jeu d'une session à l'autre, et les trois briques du domaine attaquent le problème par trois bouts : [[Letta]] en fait une hiérarchie que l'agent s'auto-édite, [[Headroom]] comprime le contexte de façon réversible, [[OpenViking]] l'expose en système de fichiers parcourable.
- **MCP est devenu la prise standard** entre un modèle et des outils, et c'est ce qui rend un outil réutilisable d'un agent à l'autre : [[mcp-protocol]] pour le protocole, [[fastmcp]] pour écrire un serveur, [[mcpjam]] pour le déboguer. Le pendant entre agents est [[a2a-protocol]] — découverte et délégation entre agents construits séparément. Les deux portent `llm/protocole`, ouverte au lot 4 : `llm/mcp` nommait un protocole et ne pouvait pas accueillir le second.
- Fabriquer ses données d'entraînement avec un modèle est devenu la norme du post-training : [[Synthetic data generation]], à lire avec [[Fine-tuning]].
- La **sécurité de ces systèmes** est un sujet entier, et elle n'est pas rangée ici : [[AI security]], [[Prompt injection]], [[Jailbreaking and defenses]], [[Guardrails]] et [[Sandboxing de code généré]] sont descendues dans [[Sécurité]] au lot 4, où elles tiennent désormais leur propre dossier — [[Systèmes IA]]. L'arbitrage tient en une phrase — la sécurité est une pratique qui traverse les modèles, pas un sous-sujet de l'IA générative — et il va contre l'ordre de l'arbre de décision du domaine, où D1 (« a besoin d'un LLM ») passe avant D9 (« porte sur la sécurité »). Ce qui reste ici est l'**outillage** que ces notions emploient : [[Guardrails|la validation de sortie]] par [[Instructor]] et [[Outlines]], les garde-fous de passerelle de [[LiteLLM]], la détection d'abus par [[LLM observability]].

## Choisir

- Faire tourner un modèle ouvert, en local ou sur GPU → [[Runtimes]].
- Écrire un agent en Python → [[Agents]].
- Un agent qui édite déjà du code dans mon dépôt → [[Agents de code]].
- Une application conversationnelle prête à déployer → [[Assistants]].
- Ajuster les poids d'un modèle sur mon domaine → [[Fine-tuning]].
- Interroger une base relationnelle en langage naturel → [[Text-to-SQL]].
- Comprendre le modèle lui-même — tokens, décodage, taille, raisonnement → [[Modèles de langage]].
- Ancrer les réponses sur mes documents → [[RAG & retrieval]].
- Garantir la forme de ce qui sort → [[Sortie typée]].
- Une seule API devant plusieurs fournisseurs, du routage, du cache → [[Passerelles]].
- Savoir ce que vaut mon système avant la production → [[Évaluation]] ; après → [[Observabilité des LLM]].
- Le socle générique pour composer chaînes et agents → [[LangChain]] ; optimiser les prompts au lieu de les écrire → [[DSPy]].
- Assembler un workflow sans écrire de code → [[Dify]] pour la plateforme complète, [[Langflow]] ou [[Flowise]] pour un canvas exportable.
- Exposer mes outils à n'importe quel agent → [[fastmcp]], puis [[mcpjam]] pour vérifier.
- Garder de la mémoire entre les sessions → [[Letta]] ; réduire le contexte sans le perdre → [[Headroom]].
- Savoir quel modèle local tient sur ma machine → [[llmfit]].
- Entraîner un modèle depuis zéro, ou produire autre chose que du texte → [[Machine Learning]], pas ce domaine.

<!-- AUTO:START -->
### Sous-domaines
- [[Agents]] · [[Agents de code]] · [[Assistants]] · [[Fine-tuning]] · [[Modèles de langage]] · [[Observabilité des LLM]] · [[Passerelles]] · [[RAG & retrieval]] · [[Runtimes]] · [[Sortie typée]] · [[Text-to-SQL]] · [[Évaluation]]

### Notions
- [[a2a-protocol]] — domaines : ai-eng
- [[Agent memory]] — domaines : ai-eng
- [[Chain-of-Thought]] — domaines : ai-eng
- [[Context engineering]] — domaines : ai-eng
- [[mcp-protocol]] — domaines : ai-eng
- [[Prompt engineering]] — domaines : ai-eng

### Briques
- [[Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.
- [[fastmcp]] — La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma.
- [[Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.
- [[Headroom]] — Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande.
- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[llmfit]] — CLI Rust (MIT) qui détecte le matériel — RAM, CPU, GPU, VRAM, backend d'accélération — puis classe des centaines de modèles locaux sur quatre axes : tenue en mémoire, vitesse estimée, qualité et contexte ; TUI interactive, mode script et benchmarks communautaires.
- [[mcpjam]] — « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

### Comparatifs
- [[Comparatif - Frameworks LLM]]
<!-- AUTO:END -->
