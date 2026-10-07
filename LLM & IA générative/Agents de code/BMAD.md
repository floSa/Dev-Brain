---
role: brique
nom: BMAD
alias: [BMAD-METHOD, bmad-method, Breakthrough Method for Agile AI-Driven Development]
pitch: "Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
alternatives: ["[[Spec Kit]]", "[[OpenSpec]]"]
complements: ["[[Aider]]", "[[Cline]]", "[[Continue]]"]
tags: [agent-skill, code-assistant, agents, multi-agent, code-generation]
url_docs: https://docs.bmad-method.org/
url_repo: https://github.com/bmad-code-org/BMAD-METHOD
---

# BMAD

<!-- AUTO:BANDEAU:START -->
> Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Python | open-source | dans le moteur hôte, rien à héberger | — | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

BMAD (*Breakthrough Method for Agile AI-Driven Development*, aussi écrit *BMad Method*) est un **jeu de skills** qu'on installe dans un agent de code pour mener un projet de la première idée au code relu : agents nommés, workflows de planification et de construction, tickets. Il ne code pas lui-même : il pilote l'agent hôte, qui code. Le README le décrit comme une méthode agile dont les décisions restent explicites, dont le contexte se reporte d'une étape à l'autre, et dont la profondeur de planification se règle sur la taille du travail : un petit changement va droit à `bmad-build`, un chantier complexe passe par spécification, architecture et découpage en stories.

Le principe, les rôles et les artefacts sont dans [[BMAD - la méthode]] ; chaque skill, agent, commande et module officiel est dans [[BMAD - tour complet des skills]].

Deux états coexistent au 2026-10-07 : la dernière **release** (v6.12.1, 2026-10-04, paquet npm `bmad-method`) s'installe par `npx bmad-method install` ; la **branche `main`**, que décrit la documentation en ligne, s'installe par `npx skills add bmad-code-org/BMAD-METHOD` puis `bmad setup`, avec un skill concentrateur `bmad` et `bmad-ticket` pour le découpage. Le module de base porte cinq agents (Mary l'analyste, John le chef de produit, Winston l'architecte, Sally l'UX, Amelia la développeuse) ; les modules officiels à part sont Builder, Creative Intelligence Suite (six agents), Test Architect, Loop et Game Dev Studio. Les chiffres qui circulent (« 19 agents, 50+ workflows ») viennent de sources secondaires, pas d'une page officielle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir une trace structurée intention → spécification → architecture → stories, révisable, plutôt qu'un enchaînement de prompts | Petite tâche ou correctif évident : la doc elle-même dit qu'on n'a pas besoin de BMAD pour une retouche triviale |
| Travail découpé en unités d'une session (environ 500 lignes hors tests), chacune dans une conversation neuve pour éviter la dérive | Un cadre plus mince suffit : [[OpenSpec]] ou [[Spec Kit]] gardent la spécification sans les rôles ni le suivi |
| Besoin de rôles explicites (produit, architecture, UX, développement) et de points de validation, même en travaillant seul | Chaîne d'outils qu'on veut garder mince : `uv` est requis pour les scripts et le setup, en plus de Node.js pour l'installation |
| Code existant : `bmad-build` lit le dépôt d'abord, `bmad-project-context` pose les règles dans `AGENTS.md` | Churn important : la v4 et la v6 sont incompatibles, des skills ont été renommés ou fondus (`bmad-quick-dev` devenu `bmad-build`, trois skills de recherche fondus en `bmad-deep-recon`), et `main` n'est pas publié ; verrouiller une version |
| Un outil de codage qui gère les skills : Claude Code, Cursor, Cline, Codex, Windsurf, Amp, Antigravity et d'autres, listés par la doc | Réutiliser le nom pour un dérivé : la licence est MIT, mais le fichier LICENSE réserve les marques BMad™, BMad Method™ et BMad Core™ à BMad Code, LLC (d'où le `NOASSERTION` renvoyé par l'API GitHub) ; `TRADEMARK.md` interdit un nom confusément proche |

## Mise en œuvre

- Installation — sur `main` : `npx skills add bmad-code-org/BMAD-METHOD`, ou la place de marché de plugins (`/plugin marketplace add bmad-code-org/bmad-plugins` dans Claude Code), puis, dans l'outil, demander au skill `bmad` de lancer `bmad setup` (`bmad status` vérifie les versions) ; sur la release v6.12.1 : `npx bmad-method install`, qui écrit les skills dans le dossier de l'outil choisi
- Point d'entrée — `bmad` pour savoir quoi faire, puis `bmad-build` avec ce qu'on veut changer ; les agents nommés (`bmad-agent-analyst`, `-pm`, `-architect`, `-ux-designer`, `-dev`) et leurs codes de menu ; surcharge en TOML par couches sous `_bmad/custom/`
- Prérequis — `uv` pour le setup et les scripts Python ; Node.js, npm et Git pour la CLI de skills ; sur la release v6.12.1, le README donne Node 20.12 ou plus et Python 3.10 ou plus
- Exécution — dans l'outil de codage hôte, sur le poste ; le modèle est celui de l'outil (usage avec un modèle local non vérifié)
- Coût — gratuit, MIT, avec une clause de marque ; la dépense réelle est celle du LLM de l'agent piloté, et les relectures `thorough` en consomment beaucoup

## Écosystème

### Alternatives

- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).
- [[OpenSpec]] — Outil libre (MIT, TypeScript, paquet npm `@fission-ai/openspec`) de spécification dans le dépôt : un dossier `openspec/` garde les specs de ce qui est vrai et un dossier par changement (proposition, specs en delta, design, tâches) que l'agent de code rédige, implémente puis archive.

### Compléments

- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur. — l'un des agents qui exécutent ce que BMAD planifie.
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe. — idem, côté éditeur.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API). — idem, avec le modèle de son choix.

## Ressources

- Documentation — https://docs.bmad-method.org/
- Dépôt — https://github.com/bmad-code-org/BMAD-METHOD (dépôt canonique `bmad-code-org/BMAD-METHOD` ; les nombreux homonymes sont des forks)

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[BMAD - la méthode]] — le principe, la boucle de livraison, les rôles, Scrum en parallèle
- [[BMAD - tour complet des skills]] — chaque skill, agent et commande, et une session complète
- [[Agent skills]] — compétences packagées d'un agent
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[Context engineering]] — composition et budget du contexte
