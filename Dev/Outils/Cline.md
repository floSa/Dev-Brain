---
galaxie: dev
type: outil
nom: Cline
alias: [cline]
pitch: "Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe."
categorie: tooling/code-assistant
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
status: actif
alternatives: ["[[Dev/Outils/Continue|Continue]]", "[[Dev/Outils/Aider|Aider]]"]
tags: [code-assistant, code-generation, llm, agents, mcp]
url_docs: https://docs.cline.bot/
url_repo: https://github.com/cline/cline
---

# Cline

## Pourquoi

Agent de code autonome (Apache 2.0) qui s'exécute dans l'IDE, le terminal ou comme SDK : on choisit une tâche et il l'exécute. Différenciateur clé : la boucle **Plan/Act** — Plan lit et raisonne sur une stratégie, Act l'exécute avec approbation à chaque étape — et un support **MCP de première classe** (marketplace de serveurs, stdio/SSE) pour brancher bases, observabilité et outils internes.

## Quand l'utiliser

- Déléguer une tâche multi-étapes à un agent qui édite, lance des commandes terminal et itère, sous contrôle humain pas-à-pas.
- Tirer parti de l'écosystème MCP : connecter facilement des outils externes à l'agent.
- Rester dans VS Code (aussi JetBrains, Cursor, Windsurf, Zed, Neovim ; CLI en préversion).

## Quand NE PAS l'utiliser

- Autocomplétion inline et assistant léger dans l'IDE → [[Dev/Outils/Continue|Continue]].
- Workflow terminal pur avec commits git atomiques automatiques → [[Dev/Outils/Aider|Aider]].

## Bases & plateformes

- Open-source Apache 2.0, écrit en TypeScript. Disponible en extension IDE, CLI (préversion macOS/Linux) et SDK.
- Multiplateforme. Le contrôle humain à chaque étape (Plan/Act) en fait un agent prudent par défaut.

## Pièges

- Agent autonome qui lance des commandes : revoir chaque action avant approbation, surtout hors environnement isolé.
- Coût d'API potentiellement élevé sur les boucles agent longues (nombreux appels LLM).
- Le branchement de serveurs MCP tiers élargit la surface d'exécution : vérifier ce qu'on connecte.

## Alternatives

- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif des assistants IA de code
- Doc : https://docs.cline.bot/
