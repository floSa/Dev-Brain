---
role: brique
nom: mcpjam
alias: [MCPJam, MCPJam Inspector, mcpjam inspector]
pitch: "« Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM."
categorie: llm/protocole
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: []
complements: ["[[fastmcp]]"]
tags: [mcp, testing, tool-use]
url_docs: https://www.mcpjam.com
url_repo: https://github.com/MCPJam/inspector
---

# mcpjam

<!-- AUTO:BANDEAU:START -->
> « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé · mono-nœud | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Banc d'essai pour le Model Context Protocol : on y branche un serveur MCP et on **exécute ses
outils, resources, resource templates, prompts et flux d'elicitation à la main**, avec une
**observabilité JSON-RPC complète** — les messages bruts dans les deux sens. Un **playground
LLM** permet de discuter contre le serveur avec plusieurs modèles côte à côte, pour voir
comment un agent appellerait réellement les outils : il *illustre* ce comportement, il ne le
*certifie* pas. C'est un **fork de l'inspecteur MCP officiel** d'Anthropic, lancé parce que
ses mainteneurs trouvaient l'amont trop lent, écrit en TypeScript. Il embarque un debugger
OAuth, un cadre d'**évals** et un CLI/SDK pour la CI.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Développer ou déboguer un serveur MCP : voir les schémas annoncés, appeler un outil, lire la réponse JSON-RPC | Tests automatisés du code du serveur lui-même : c'est un inspecteur interactif, pas un test runner unitaire → [[pytest]] côté Python |
| Reproduire le comportement d'un agent : tester l'enchaînement d'appels d'outils avant de câbler l'app | Besoin de rester sur l'outil de référence strict : c'est le MCP Inspector officiel, dont il est le fork |
| Vérifier les transports (stdio, HTTP/S) et le flux OAuth d'un serveur distant | Jeune fork en évolution rapide : surface et flags bougent d'une version à l'autre, épingler la version dans les scripts CI |
| Intégrer des évals d'outils MCP en CI via le CLI | Le web hébergé parle à un serveur local via un pont : pour un serveur sensible, ou des outils à effet de bord, préférer le desktop ou le terminal |

## Mise en œuvre

- Installation — `npx @mcpjam/inspector@latest` en terminal, app desktop Mac et Windows, Docker, ou l'instance web hébergée (app.mcpjam.com)
- Point d'entrée — interface d'inspection : outils, resources, resource templates, prompts, elicitation ; plus un playground LLM et un debugger OAuth
- Prérequis — Node 20+ pour l'exécution locale ; les appels du playground consomment les clés du fournisseur choisi
- Exécution — outil de développement, mono-nœud : en local pour garder serveurs et secrets sur la machine, ou en web hébergé pour un usage zéro-install
- Coût — gratuit ; le seul coût est celui des appels LLM du playground

## Écosystème

### Alternatives

- **MCP Inspector officiel** (`modelcontextprotocol/inspector`) — l'amont dont mcpjam est issu : plus minimaliste, sans playground LLM ni évals. *(Page dédiée non créée.)*

### Compléments

- [[fastmcp]] — La façon rapide et pythonique de construire des serveurs (et clients) MCP — les serveurs qu'il inspecte le plus souvent.

## Ressources

- Documentation — https://www.mcpjam.com
- Dépôt — https://github.com/MCPJam/inspector

## Voir aussi

- [[mcp-protocol]] — la notion : le protocole des serveurs qu'il inspecte
- [[LLM & IA générative]] — le hub du domaine
