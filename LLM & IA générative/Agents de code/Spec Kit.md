---
role: brique
nom: Spec Kit
alias: [spec-kit, specify, specify-cli, spec-driven development, SDD]
pitch: "CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement)."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
alternatives: ["[[BMAD]]"]
complements: ["[[Aider]]", "[[Cline]]", "[[Continue]]"]
tags: [code-assistant, code-generation, agents, cli]
url_docs: https://github.com/github/spec-kit
url_repo: https://github.com/github/spec-kit
---

# Spec Kit

<!-- AUTO:BANDEAU:START -->
> CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Python | open-source | dans le moteur hôte, rien à héberger | — | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Outillage du **spec-driven development**, maintenu par GitHub : au lieu d'écrire du code puis de
le documenter, on rédige une **spécification exécutable** qui devient la source de vérité et
pilote un agent de codage IA, du cahier des charges jusqu'à l'implémentation. La CLI `specify`
scaffolde le projet et installe une série de commandes slash (`/speckit.*`) que l'agent exécute
étape par étape, plus une « constitution » de principes qu'il doit respecter. C'est un **cadre
méthodologique**, pas un assistant de code : il ne remplace pas l'agent qui écrit, il le
contraint. Compatible avec 30+ agents (Copilot, Claude, Cursor, Gemini CLI…), et très actif —
~122k stars, releases fréquentes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cadrer un projet greenfield ou une fonctionnalité avec un cahier des charges explicite **avant** de laisser l'IA coder | Petite édition ponctuelle : le workflow SDD, six à sept étapes, est surdimensionné |
| Vouloir une trace structurée intention → plan → tâches → implémentation, révisable en équipe | Garbage-in : une spec bâclée produit un plan et un code bâclés — l'effort se déplace vers l'amont, il ne disparaît pas |
| Imposer des garde-fous : une « constitution » de principes que l'agent doit respecter | Projet à figer : jeune et mouvant (nombreuses releases, commandes qui évoluent) — verrouiller une version |
| | La qualité finale dépend encore de l'agent de codage sous-jacent, que Spec Kit ne remplace pas |

## Mise en œuvre

- Installation — `uv tool install specify-cli` (ou `pipx`), puis `specify init <projet> --integration <agent>`
- Point d'entrée — les commandes slash `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`, plus les optionnelles `clarify`, `analyze`, `checklist`, `taskstoissues`
- Prérequis — Python 3.11+ et git ; un agent de codage supporté (`specify integration list` en donne la liste)
- Exécution — sur le poste, en ligne de commande ; Windows, macOS, Linux
- Coût — gratuit, MIT ; la dépense réelle est celle du LLM de l'agent piloté

## Écosystème

### Alternatives

- [[BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story.

### Compléments

- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur. — l'un des agents que la spec pilote.
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe. — idem, côté éditeur.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API). — idem, avec le modèle de son choix.

## Ressources

- Documentation — https://github.com/github/spec-kit
- Dépôt — https://github.com/github/spec-kit

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
