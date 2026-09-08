---
role: brique
nom: Cline
alias: [cline]
pitch: "Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[Continue]]", "[[Aider]]", "[[freebuff]]", "[[t3code]]", "[[pi]]"]
complements: ["[[Spec Kit]]", "[[BMAD]]"]
tags: [code-assistant, code-generation, llm, agents, mcp]
url_docs: https://docs.cline.bot/
url_repo: https://github.com/cline/cline
---

# Cline

<!-- AUTO:BANDEAU:START -->
> Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension TypeScript | open-source | dans le moteur hôte, rien à héberger | — | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de code autonome qui s'exécute dans l'IDE, le terminal ou comme SDK : on lui confie une
tâche et il l'exécute — il édite, lance des commandes, lit les résultats et itère. Son
différenciateur est la boucle **Plan/Act** : en Plan il lit le dépôt et raisonne sur une
stratégie, en Act il l'exécute avec une approbation demandée à chaque étape. Second
différenciateur, un support **MCP de première classe** — marketplace de serveurs, transports
stdio et SSE — pour brancher bases, observabilité et outils internes sur l'agent. Le contrôle
humain pas-à-pas en fait un agent prudent par défaut, au prix d'un aller-retour permanent.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déléguer une tâche multi-étapes à un agent qui édite, lance des commandes terminal et itère, sous contrôle humain pas-à-pas | L'agent lance des commandes : hors environnement isolé, chaque action est à revoir avant approbation |
| Tirer parti de l'écosystème MCP : connecter facilement des outils externes à l'agent | Brancher des serveurs MCP tiers élargit d'autant la surface d'exécution — vérifier ce qu'on connecte |
| Rester dans VS Code (aussi JetBrains, Cursor, Windsurf, Zed, Neovim ; CLI en préversion) | Budget d'API serré : les boucles agent longues multiplient les appels LLM |

## Mise en œuvre

- Installation — extension d'éditeur ; également une CLI (préversion macOS/Linux) et un SDK
- Point d'entrée — panneau de l'IDE, avec la bascule Plan/Act ; serveurs MCP déclarés à côté
- Prérequis — un éditeur supporté (VS Code, JetBrains, Cursor, Windsurf, Zed, Neovim) et un accès LLM
- Exécution — sur le poste, dans le processus de l'éditeur ; Windows, macOS, Linux
- Coût — outil gratuit sous Apache 2.0 ; la dépense réelle est celle du LLM, et elle monte vite sur les boucles agent longues

## Écosystème

### Alternatives

- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.
- [[t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.

### Compléments

- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement). — se pose au-dessus de Cline : la spec dit quoi faire, Cline l'exécute.
- [[BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story. — même étage que Spec Kit : il pilote, l'exécution reste chez Cline.

## Ressources

- Documentation — https://docs.cline.bot/
- Dépôt — https://github.com/cline/cline

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
