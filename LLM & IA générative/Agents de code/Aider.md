---
role: brique
nom: Aider
alias: [aider]
pitch: "Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
alternatives: ["[[Continue]]", "[[Cline]]", "[[freebuff]]", "[[t3code]]", "[[pi]]"]
complements: ["[[Spec Kit]]", "[[BMAD]]"]
tags: [code-assistant, code-generation, llm, version-control]
url_docs: https://aider.chat/docs/
url_repo: https://github.com/Aider-AI/aider
---

# Aider

<!-- AUTO:BANDEAU:START -->
> Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Pair-programmeur qui vit dans le terminal et relie un LLM au dépôt git local : il édite les
fichiers, en crée, refactore, et **commite chaque changement** — un commit atomique par édition,
donc annulable une par une. Il construit une *repo map* de toute la base de code pour garder le
contexte sur les gros projets. Agnostique de l'éditeur : aucun plugin à installer, aucune
intégration IDE à maintenir. Tout passe par git, ce qui est à la fois son mécanisme de
traçabilité et sa condition d'entrée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Travailler depuis le terminal, sans dépendre d'un IDE ni d'un plugin | Le dépôt n'est pas initialisé, ou l'arbre de travail est sale : le suivi des commits automatiques s'y perd |
| Vouloir un historique git propre : un commit atomique par édition de l'IA | Aucune interface graphique — la prise en main suppose l'aisance en ligne de commande |
| Refactors et changements multi-fichiers sur un dépôt existant, la *repo map* servant de contexte | Gros dépôt et budget d'API serré : la *repo map* envoyée en contexte fait grimper la facture |

## Mise en œuvre

- Installation — paquet Python, installé sur le poste ; aucun plugin d'éditeur
- Point d'entrée — CLI interactive lancée dans le dépôt ; le chat pilote les éditions
- Prérequis — Python 3.9+, git, un dépôt initialisé, et un accès LLM (clé d'API ou modèle local)
- Exécution — sur le poste, en ligne de commande ; Windows, macOS, Linux
- Coût — outil gratuit sous Apache 2.0 ; la dépense réelle est celle du LLM, et la *repo map* la fait monter avec la taille du dépôt

## Écosystème

### Alternatives

- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.
- [[t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.

### Compléments

- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement). — se pose au-dessus d'Aider : la spec dit quoi faire, Aider l'exécute.
- [[BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story. — même étage que Spec Kit : il pilote, l'exécution reste chez Aider.

## Ressources

- Documentation — https://aider.chat/docs/
- Dépôt — https://github.com/Aider-AI/aider

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
