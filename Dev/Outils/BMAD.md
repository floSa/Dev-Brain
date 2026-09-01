---
galaxie: dev
type: outil
nom: BMAD
alias: [BMAD-METHOD, bmad-method, Breakthrough Method for Agile AI-Driven Development]
pitch: "Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story."
categorie: tooling/code-assistant
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: JavaScript
status: actif
alternatives: ["[[Dev/Outils/Spec Kit|Spec Kit]]"]
tags: [agent-skill, code-assistant, agents, multi-agent, code-generation]
url_docs: https://docs.bmad-method.org/
url_repo: https://github.com/bmad-code-org/BMAD-METHOD
---

# BMAD

## Pourquoi

BMAD — *Breakthrough Method for Agile AI-Driven Development* — outille une méthode de développement assisté par IA sous forme d'agents nommés installés dans l'outil de codage. Le paquet npm `bmad-method` injecte des skills et des commandes que l'agent exécute étape par étape.

Le flux est explicitement agile : l'**analyst** produit un Project Brief, le **PM** un PRD, l'**architect** le design et une revue d'Implementation Readiness, puis le travail se déroule **story par story**, chaque story isolée dans un chat neuf, son fichier servant de paquet de handoff entre les rôles. Le module BMM porte neuf agents (`pm`, `analyst`, `architect`, `dev`, `ux-designer`, `tech-writer`, `sm`, `tea`, `quick-flow-solo-dev`), le module CIS six autres, aux côtés des modules core, BMad Builder, Game Dev Studio et Test Architect.

Version courante v6.11.0. La v4 reste en maintenance, uniquement pour les correctifs critiques.

Dépôt canonique : `bmad-code-org/BMAD-METHOD`. Les nombreux dépôts homonymes sont des forks.

## Quand l'utiliser

- Projet où l'on veut une trace structurée intention → PRD → architecture → stories, révisable, plutôt qu'un enchaînement de prompts.
- Travail découpé en incréments livrables, avec un contexte remis à zéro à chaque story pour éviter la dérive.
- Besoin de rôles explicites (produit, architecture, dev, test) même en travaillant seul.

## Quand NE PAS l'utiliser

- Petite tâche ou correctif : le cérémonial coûte plus cher que le travail.
- BMAD ne **remplace pas** l'agent qui code — il le pilote. L'exécution reste chez [[Dev/Outils/Aider|Aider]], [[Dev/Outils/Cline|Cline]] ou [[Dev/Outils/Continue|Continue]].
- Outil de codage autre que Claude Code ou Cursor : la documentation officielle ne cite explicitement que ces deux-là.
- Chaîne d'outils qu'on veut garder mince : depuis la v6.11, les skills rendus exigent `uv` et Python 3.11+ **en plus** de Node ≥ 20.12.

## Installation & plateformes

- `npx bmad-method install` — l'installeur écrit les skills et commandes dans l'outil de codage cible.
- Node ≥ 20.12.0 ; depuis la v6.11, également `uv` et Python 3.11+ pour les skills rendus. Configuration en TOML par couches.
- Multiplateforme (Node). Documentation officielle sur `docs.bmad-method.org`.

## Pièges

- **Churn important entre versions.** v4 et v6 sont incompatibles : verrouiller une version et ne pas suivre la tête aveuglément.
- La v6.11 déprécie `bmad-create-story` et `bmad-dev-story` (réduits à des shims), consolide `bmad-quick-dev` en `bmad-build` comme seule voie officielle d'implémentation, ramène les skills core de 14 à 8, et unifie `bmad-review` avec des « lentilles » configurables.
- **Clause de marque** : la licence est MIT mais le fichier LICENSE réserve les marques BMad™, BMad Method™ et BMad Core™ à BMad Code, LLC. Interdiction d'utiliser le nom pour un dérivé — d'où le `NOASSERTION` renvoyé par l'API GitHub.
- Les chiffres qui circulent (« 19 agents, 50+ workflows ») viennent de sources secondaires, pas d'une page officielle.

## Alternatives

- [[Dev/Outils/Spec Kit|Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Agent skills]] — concept : compétences packagées d'un agent
- [[Multi-agent systems]] — concept : systèmes à plusieurs agents coopérants
- [[Agent patterns]] — concept : patrons d'architecture d'agents
- [[Context engineering]] — concept : composition et budget du contexte
- Docs : https://docs.bmad-method.org/ · Repo : https://github.com/bmad-code-org/BMAD-METHOD
