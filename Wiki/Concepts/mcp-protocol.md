---
galaxie: wiki
type: concept
nom: mcp-protocol
alias: [MCP, Model Context Protocol, protocole MCP]
categorie: concept/llm
domaines: [ai-eng]
tags: [mcp, tool-use, llm]
---

# mcp-protocol

## Aperçu

- **Model Context Protocol** (Anthropic, fin 2024) : standard ouvert pour connecter un LLM à des outils, des données et des prompts via une architecture **client-serveur**.
- Idée : remplacer les intégrations sur mesure « un connecteur par couple (app, outil) » par un protocole unique — le « USB-C des applications IA ».

## Concepts clés

### Architecture host / client / serveur
- Un **host** (l'app IA : IDE, agent, app desktop) lance un ou plusieurs **clients** ; chaque client parle à un **serveur** MCP qui expose des capacités. Un serveur = une intégration (fichiers, GitHub, Postgres…).

### Primitives serveur
- **Tools** (fonctions appelables — cf. [[tool-use]]), **Resources** (données contextuelles adressables par URI), **Prompts** (gabarits réutilisables). Le serveur annonce ses capacités, le client les découvre.

### Primitives client
- **Sampling** (le serveur peut demander une complétion au modèle de l'host), **Roots** (périmètre de fichiers autorisé), **Elicitation** (demander une info à l'utilisateur). Le flux n'est pas à sens unique.

### Transport & format
- Messages en **JSON-RPC 2.0**. Deux transports standard : **stdio** (serveur lancé en sous-processus, échange par stdin/stdout) et **Streamable HTTP** (serveurs distants, streaming par SSE). *(Streamable HTTP a remplacé l'ancien HTTP+SSE en 2025.)*

### Sécurité
- Un serveur MCP exécute du code et accède à des données : confiance du serveur, périmètre des *roots*, consentement utilisateur sur les outils à effet de bord. Surface d'attaque réelle (injection via *resources*, outils malveillants).

## Les maths, simplement

- Sans standard, $M$ apps × $N$ outils = $M \times N$ connecteurs à écrire et maintenir.
- Avec un protocole commun, chaque app parle MCP une fois et chaque outil l'expose une fois → $M + N$. C'est tout l'argument économique du standard.

## En pratique

- Utiliser MCP quand plusieurs apps doivent partager les mêmes outils, ou pour brancher un agent sur un écosystème de serveurs existants sans recâbler.
- Pour un seul agent maison avec 2-3 outils, le [[tool-use|function calling]] direct reste plus simple — MCP ajoute une couche serveur à faire tourner.
- Côté clients : Claude Desktop/Code, et un nombre croissant de frameworks d'agents ([[Dev/Services/LangGraph|LangGraph]], [[Dev/Services/PydanticAI|PydanticAI]]) consomment des serveurs MCP.
- Côté serveurs : [[Dev/Services/fastmcp|fastmcp]] construit serveurs et clients MCP en Python (décorateurs, génération depuis OpenAPI/FastAPI) ; [[Dev/Services/mcpjam|mcpjam]] les **inspecte et débogue** (« Postman pour MCP »).
- Traiter un serveur tiers comme du **code non fiable** : permissions minimales, validation des entrées, garde-fous sur les outils sensibles (cf. [[Reliability patterns]]).

## Approches voisines & alternatives

- [[tool-use]] — MCP **standardise** l'exposition des outils que le function calling appelle.
- [[Tool use patterns]] — les patrons d'appel d'outils s'appliquent aux outils servis par MCP.
- [[Agent memory]] — les *resources* MCP sont une voie d'alimentation du contexte/mémoire.
- [[Context engineering]] — MCP est un canal d'assemblage du contexte (resources, prompts).
- Alternative : **function calling câblé en dur** (SDK fournisseur) — moins de pièces mobiles sur un périmètre fermé, mais pas d'interopérabilité.

## Pour aller plus loin

- Anthropic (2024) — *Introducing the Model Context Protocol*.
- Spécification : modelcontextprotocol.io (version 2025-11-25).
