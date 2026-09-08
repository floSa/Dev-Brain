---
role: brique
nom: fastmcp
alias: [FastMCP]
pitch: "La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma."
categorie: llm/protocole
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[mcpjam]]"]
tags: [mcp, tool-use, agents]
url_docs: https://gofastmcp.com
url_repo: https://github.com/PrefectHQ/fastmcp
---

# fastmcp

<!-- AUTO:BANDEAU:START -->
> La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-05 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework Python de référence pour exposer des outils, des ressources et des prompts via le
Model Context Protocol **sans écrire la plomberie JSON-RPC**. On décore une fonction
(`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`) et FastMCP **génère le schéma** depuis les
annotations de type, négocie le **transport** (stdio ou Streamable HTTP) et gère le cycle de
vie du protocole. Créé par Jeremiah Lowin, le dépôt est maintenu sous l'organisation
PrefectHQ. Point de vigilance permanent : **FastMCP 1.0 a été intégré au SDK MCP Python
officiel**, et les majeures suivantes — celles de ce dépôt — sont développées à part et vont
bien au-delà du protocole de base : bibliothèque cliente, proxying et composition de
serveurs, génération automatique depuis OpenAPI ou FastAPI, authentification, tests et outils
de déploiement. La 4.0 est passée GA le 31 août 2026 (4.0.1 le 1er septembre) ; la 3.x est en
maintenance.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exposer une API, des données ou des fonctions maison à un agent ou à un IDE comme serveur MCP propre, en Python | Un seul agent maison avec deux ou trois fonctions : le function calling direct du SDK fournisseur suffit, sans serveur à faire tourner → [[tool-use]] |
| Transformer une app **FastAPI** ou une spec **OpenAPI** existante en serveur MCP quasi gratuitement | Stack non-Python : pour TypeScript, c'est le SDK MCP officiel qu'il faut |
| Écrire un client MCP programmatique — tester, orchestrer, brancher plusieurs serveurs — sans implémenter le protocole | Un serveur MCP **exécute du code et accède à des données** : outils à effet de bord à encadrer, et surface d'injection par les *resources* → [[Guardrails]] |
| Composer ou **proxifier** plusieurs serveurs MCP derrière une seule façade | La génération de schéma dépend des annotations de type : signatures floues, schémas d'outils approximatifs pour le LLM |

## Mise en œuvre

- Installation — `uv add fastmcp` ou `pip install fastmcp`
- Point d'entrée — décorateurs `@mcp.tool`, `@mcp.resource`, `@mcp.prompt` côté serveur ; une bibliothèque dédiée côté client
- Prérequis — Python ; viser la **4.x** pour les fonctionnalités récentes — la montée 3 → 4 se fait sans changement de code pour la plupart des applications, mais des points dépréciés y ont été retirés
- Exécution — un serveur stdio est lancé en sous-processus, sans infra ; un serveur HTTP distant est à héberger soi-même (process et port), mono-nœud par serveur
- Coût — gratuit

## Écosystème

### Alternatives

- **SDK MCP Python officiel** (`mcp`) — implémentation de référence ; FastMCP 1.0 y est intégré, les majeures suivantes ajoutent la couche haut niveau. *(Page dédiée non créée.)*

### Compléments

- [[mcpjam]] — « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM — pour exécuter les outils du serveur à la main et lire le JSON-RPC brut.

## Ressources

- Documentation — https://gofastmcp.com
- Dépôt — https://github.com/PrefectHQ/fastmcp

## Voir aussi

- [[mcp-protocol]] — la notion : le protocole qu'il implémente, côté serveur comme côté client
- [[PydanticAI]], [[LangGraph]] — des frameworks d'agents qui le consomment
- [[LLM & IA générative]] — le hub du domaine
