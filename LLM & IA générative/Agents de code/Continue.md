---
role: brique
nom: Continue
alias: [continue, continue.dev, continuedev]
pitch: "Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API)."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript, Kotlin
alternatives: ["[[Aider]]", "[[Cline]]", "[[freebuff]]", "[[t3code]]", "[[pi]]"]
complements: ["[[Spec Kit]]", "[[BMAD]]"]
tags: [code-assistant, code-generation, llm, agents]
url_docs: https://docs.continue.dev/
url_repo: https://github.com/continuedev/continue
---

# Continue

<!-- AUTO:BANDEAU:START -->
> Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension TypeScript, Kotlin | open-source | dans le moteur hôte, rien à héberger | — | à jour · 2026-06-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

Assistant de codage intégré à VS Code et à JetBrains, qui couvre quatre usages dans le même
outil : Chat (aide sans quitter l'éditeur), Autocomplete (suggestions inline en temps réel),
Edit (modifications ciblées) et Agent (changements à l'échelle du dépôt). Sa particularité est
le *bring your own model* — on branche un modèle local (Ollama, llama.cpp) ou une clé d'API
(Anthropic, OpenAI…), sans verrouillage fournisseur : qualité, coût et confidentialité suivent
alors entièrement le modèle choisi. Cœur et GUI en TypeScript ; l'extension JetBrains est en
Kotlin, désormais maintenue par la communauté, le développement actif se déplaçant vers la
**Continue CLI** (checks de code versionnés, exécutables en CI).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rester dans son IDE (VS Code ou JetBrains) avec un assistant ouvert et configurable | Modèle local faible : la qualité et le coût dépendent entièrement du modèle branché, l'outil n'y peut rien |
| Brancher librement le modèle voulu — local (Ollama, llama.cpp) ou API — pour la confidentialité ou le coût | Dépendance forte au plugin JetBrains : il est passé en maintenance communautaire, l'éditeur poussant vers la CLI — surveiller la direction du produit |
| Besoin d'autocomplétion inline en plus du chat et de l'édition | |

## Mise en œuvre

- Installation — extension VS Code ou JetBrains ; une CLI existe pour les checks versionnés
- Point d'entrée — panneau de l'éditeur : chat, autocomplétion, édition ciblée, mode agent
- Prérequis — VS Code ou JetBrains, et un modèle : serveur local (Ollama, llama.cpp) ou clé d'API
- Exécution — sur le poste, dans l'éditeur ; Windows, macOS, Linux ; la CLI s'exécute aussi en CI
- Coût — outil gratuit sous Apache 2.0 ; nul avec un modèle local, sinon celui de l'API branchée

## Écosystème

### Alternatives

- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.
- [[t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.

### Compléments

- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement). — se pose au-dessus de Continue : la spec dit quoi faire, Continue l'exécute.
- [[BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story. — même étage que Spec Kit : il pilote, l'exécution reste chez Continue.

## Ressources

- Documentation — https://docs.continue.dev/
- Dépôt — https://github.com/continuedev/continue

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
