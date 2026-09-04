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
langage: JavaScript
alternatives: ["[[Spec Kit]]"]
complements: ["[[Aider]]", "[[Cline]]", "[[Continue]]"]
tags: [agent-skill, code-assistant, agents, multi-agent, code-generation]
url_docs: https://docs.bmad-method.org/
url_repo: https://github.com/bmad-code-org/BMAD-METHOD
---

# BMAD

<!-- AUTO:BANDEAU:START -->
> Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Extension JavaScript | open-source | dans le moteur hôte, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

*Breakthrough Method for Agile AI-Driven Development* — une méthode de développement assisté
par IA outillée sous forme d'agents nommés installés dans l'outil de codage, que le paquet npm
`bmad-method` injecte comme skills et commandes. Le flux est explicitement agile : l'**analyst**
produit un Project Brief, le **PM** un PRD, l'**architect** le design et une revue
d'Implementation Readiness, puis le travail se déroule **story par story**, chaque story isolée
dans un chat neuf et son fichier servant de paquet de handoff entre les rôles. BMAD ne code pas :
il pilote l'agent qui code. Le module BMM porte neuf agents, le module CIS six autres, aux côtés
des modules core, BMad Builder, Game Dev Studio et Test Architect — les chiffres qui circulent
(« 19 agents, 50+ workflows ») viennent de sources secondaires, pas d'une page officielle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir une trace structurée intention → PRD → architecture → stories, révisable, plutôt qu'un enchaînement de prompts | Petite tâche ou correctif : le cérémonial coûte plus cher que le travail |
| Travail découpé en incréments livrables, contexte remis à zéro à chaque story pour éviter la dérive | Outil de codage autre que Claude Code ou Cursor : la documentation officielle ne cite explicitement que ces deux-là |
| Besoin de rôles explicites (produit, architecture, dev, test) même en travaillant seul | Chaîne d'outils qu'on veut garder mince : depuis la v6.11, les skills rendus exigent `uv` et Python 3.11+ **en plus** de Node ≥ 20.12 |
| | Churn important entre versions : v4 et v6 sont incompatibles — verrouiller une version, ne pas suivre la tête aveuglément. La v6.11 déprécie `bmad-create-story` et `bmad-dev-story` (réduits à des shims), consolide `bmad-quick-dev` en `bmad-build` comme seule voie officielle d'implémentation, ramène les skills core de 14 à 8 et unifie `bmad-review` avec des « lentilles » configurables |
| | Nom à réutiliser pour un dérivé : la licence est MIT mais le fichier LICENSE réserve les marques BMad™, BMad Method™ et BMad Core™ à BMad Code, LLC — d'où le `NOASSERTION` renvoyé par l'API GitHub |

## Mise en œuvre

- Installation — `npx bmad-method install` : l'installeur écrit les skills et commandes dans l'outil de codage cible ; version courante v6.11.0, la v4 restant en maintenance pour les seuls correctifs critiques
- Point d'entrée — les agents nommés (`pm`, `analyst`, `architect`, `dev`, `ux-designer`, `tech-writer`, `sm`, `tea`, `quick-flow-solo-dev`) et leurs commandes, injectés dans Claude Code ou Cursor ; configuration en TOML par couches
- Prérequis — Node ≥ 20.12.0 ; depuis la v6.11, également `uv` et Python 3.11+ pour les skills rendus
- Exécution — dans l'outil de codage hôte, sur le poste ; multiplateforme (Node)
- Coût — gratuit, MIT, mais avec une clause de marque ; la dépense réelle est celle du LLM de l'agent piloté

## Écosystème

### Alternatives

- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).

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
- [[Agent skills]] — compétences packagées d'un agent
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[Context engineering]] — composition et budget du contexte
