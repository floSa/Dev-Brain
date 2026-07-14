---
galaxie: dev
type: service
nom: mcpjam
alias: [MCPJam, MCPJam Inspector, mcpjam inspector]
pitch: "« Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM."
categorie: tooling/test
licence_type: open-source
hosted: both
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [mcp, testing, tool-use]
url_docs: https://www.mcpjam.com
url_repo: https://github.com/MCPJam/inspector
---

# mcpjam

## Pourquoi

Banc d'essai pour le [[mcp-protocol|Model Context Protocol]] : on y branche un serveur MCP et on **exécute ses outils, resources, resource templates, prompts et flux d'elicitation à la main**, avec une **observabilité JSON-RPC complète** (messages bruts dans les deux sens). Un **playground LLM** permet de discuter contre le serveur avec plusieurs modèles côte à côte pour voir comment un agent appellerait réellement les outils. **Fork de l'inspecteur MCP officiel** d'Anthropic, lancé parce que ses mainteneurs trouvaient l'amont trop lent ; écrit en **TypeScript** (Node 20+). Tourne en **web hébergé** (app.mcpjam.com), **app desktop** Mac/Windows, ou **terminal** (`npx @mcpjam/inspector@latest`). Inclut un **debugger OAuth**, un cadre d'**évals** et un **CLI/SDK** pour la CI/CD. Licence **Apache-2.0**.

## Quand l'utiliser

- **Développer / déboguer un serveur MCP** (p. ex. bâti avec [[Dev/Services/fastmcp|fastmcp]]) : voir les schémas annoncés, appeler un outil, lire la réponse JSON-RPC.
- Reproduire le comportement d'un **agent** : tester l'enchaînement d'appels d'outils dans le playground LLM avant de câbler l'app.
- Vérifier les **transports** (stdio, HTTP/S) et le flux **OAuth** d'un serveur distant.
- Intégrer des **évals** d'outils MCP en CI via le CLI.

## Quand NE PAS l'utiliser

- Tests automatisés du code du serveur lui-même → framework de tests classique ([[Dev/Services/pytest|pytest]] côté Python) ; mcpjam est un **inspecteur interactif**, pas un test runner unitaire.
- Besoin de rester sur l'outil de référence strict → **MCP Inspector officiel** (`@modelcontextprotocol/inspector`).

## Déploiement & coût

- Open-source (Apache-2.0), gratuit. Usage zéro-install via le **web hébergé**, ou **local** (desktop / `npx` / Docker) pour garder les serveurs et secrets sur sa machine.
- Outil de **développement**, single-node ; les appels LLM du playground passent par les clés du fournisseur choisi (coût = ces appels).

## Pièges

- Jeune **fork** en évolution rapide : surface et flags bougent d'une version à l'autre — épingler la version dans les scripts CI.
- Le **web hébergé** parle à un serveur local via un pont : attention à ce qu'on expose (secrets, outils à effet de bord) ; préférer le desktop/terminal pour un serveur sensible.
- Playground LLM ≠ garantie de production : il **illustre** le comportement d'un agent, il ne le **certifie** pas.

## Alternatives

- **MCP Inspector officiel** ([[mcp-protocol]], `modelcontextprotocol/inspector`) — l'amont dont mcpjam est issu : plus minimaliste, sans playground LLM ni évals. *(Page dédiée non créée.)*

## Liens

- Inspecte / débogue des serveurs [[mcp-protocol]], notamment ceux bâtis avec [[Dev/Services/fastmcp|fastmcp]].
- Pour les tests unitaires du serveur côté Python : [[Dev/Services/pytest|pytest]].
- Doc : https://www.mcpjam.com
