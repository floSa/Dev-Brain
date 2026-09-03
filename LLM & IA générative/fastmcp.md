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
complements: []
tags: [mcp, tool-use, agents]
url_docs: https://gofastmcp.com
url_repo: https://github.com/PrefectHQ/fastmcp
---

# fastmcp

## Pourquoi

Framework Python de référence pour exposer des outils, ressources et prompts via le [[mcp-protocol|Model Context Protocol]] **sans écrire la plomberie JSON-RPC**. On décore une fonction (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`) et FastMCP **génère le schéma** depuis les annotations de type, négocie le **transport** (stdio / Streamable HTTP) et gère le cycle de vie du protocole. Créé par **Jeremiah Lowin**, le dépôt est passé sous l'organisation **PrefectHQ** (`PrefectHQ/fastmcp`), où le projet est maintenu. FastMCP **1.0** a été intégré au SDK MCP Python officiel ; les majeures suivantes sont développées à part et vont bien au-delà du protocole de base : **bibliothèque cliente**, **proxying** et composition de serveurs, génération automatique depuis **OpenAPI / FastAPI**, authentification, tests et outils de déploiement. La **4.0** est passée GA le 31 août 2026 (4.0.1 le 1er septembre) ; la **3.x** est en maintenance. Très diffusé (~1M téléchargements/jour, « powers 70% of MCP servers »). Licence **Apache-2.0**.

## Quand l'utiliser

- Exposer une API, des données ou des fonctions maison à un agent / IDE comme **serveur MCP** propre, en Python.
- Transformer une app **FastAPI** ou une spec **OpenAPI** existante en serveur MCP quasi gratuitement.
- Écrire un **client MCP** programmatique (tester, orchestrer, brancher plusieurs serveurs) sans implémenter le protocole.
- Composer / **proxifier** plusieurs serveurs MCP derrière une seule façade.

## Quand NE PAS l'utiliser

- Un seul agent maison avec 2-3 fonctions : le [[tool-use|function calling]] direct du SDK fournisseur suffit, sans couche serveur à faire tourner (cf. [[mcp-protocol]]).
- Stack non-Python : FastMCP est spécifique à Python (pour TS, utiliser le SDK MCP officiel).

## Déploiement & coût

- Dépendance `pip` / `uv add fastmcp`, Apache-2.0, gratuit. Aucune infra pour un serveur stdio (lancé en sous-processus).
- Un serveur **HTTP distant** est à héberger soi-même (process + port) ; scaling = single-node par serveur.

## Pièges

- Un serveur MCP **exécute du code et accède à des données** : traiter les outils à effet de bord avec consentement et garde-fous (cf. [[Guardrails]]), surface d'injection via *resources*.
- FastMCP 1.0 (dans le SDK officiel) ≠ les majeures suivantes (**ce dépôt**) : viser la **4.x** pour les fonctionnalités récentes ; vérifier la version dans la doc. La montée 3 → 4 se fait sans changement de code pour la plupart des applications, mais des points dépréciés y ont été retirés.
- La génération de schéma **dépend des annotations de type** : signatures floues → schémas d'outils approximatifs pour le LLM.

## Alternatives

- **SDK MCP Python officiel** (`mcp`) — implémentation de référence ; FastMCP 1.0 y est intégré, FastMCP 2.0 ajoute la couche haut niveau. *(Page dédiée non créée.)*

## Liens

- Implémente le [[mcp-protocol]] (serveur + client) côté Python.
- Se teste / se débogue avec [[mcpjam]] (inspecteur MCP).
- Consommé par des frameworks d'agents comme [[PydanticAI]] et [[LangGraph]].
- Doc : https://gofastmcp.com
