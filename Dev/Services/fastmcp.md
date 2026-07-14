---
galaxie: dev
type: service
nom: fastmcp
alias: [FastMCP, fastmcp 2.0]
pitch: "La façon rapide et pythonique de construire des serveurs (et clients) MCP : on décore une fonction, FastMCP gère le protocole, le transport et la génération de schéma."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [mcp, tool-use, agents]
url_docs: https://gofastmcp.com
url_repo: https://github.com/jlowin/fastmcp
---

# fastmcp

## Pourquoi

Framework Python de référence pour exposer des outils, ressources et prompts via le [[mcp-protocol|Model Context Protocol]] **sans écrire la plomberie JSON-RPC**. On décore une fonction (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`) et FastMCP **génère le schéma** depuis les annotations de type, négocie le **transport** (stdio / Streamable HTTP) et gère le cycle de vie du protocole. Créé par **Jeremiah Lowin** (désormais maintenu sous **Prefect**). FastMCP **1.0** a été intégré au SDK MCP Python officiel ; **FastMCP 2.0** est la version activement développée — elle va bien au-delà du protocole de base : **bibliothèque cliente**, **proxying** et composition de serveurs, génération automatique depuis **OpenAPI / FastAPI**, authentification, tests et outils de déploiement. Très diffusé (~1M téléchargements/jour, « powers 70% of MCP servers »). Licence **Apache-2.0**.

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
- FastMCP 1.0 (dans le SDK officiel) ≠ **FastMCP 2.0** (ce dépôt) : viser la 2.x pour les fonctionnalités récentes ; vérifier la version dans la doc.
- La génération de schéma **dépend des annotations de type** : signatures floues → schémas d'outils approximatifs pour le LLM.

## Alternatives

- **SDK MCP Python officiel** (`mcp`) — implémentation de référence ; FastMCP 1.0 y est intégré, FastMCP 2.0 ajoute la couche haut niveau. *(Page dédiée non créée.)*

## Liens

- Implémente le [[mcp-protocol]] (serveur + client) côté Python.
- Se teste / se débogue avec [[Dev/Services/mcpjam|mcpjam]] (inspecteur MCP).
- Consommé par des frameworks d'agents comme [[Dev/Services/PydanticAI|PydanticAI]] et [[Dev/Services/LangGraph|LangGraph]].
- Doc : https://gofastmcp.com
