---
role: brique
nom: Claude Agent SDK
alias: [claude-agent-sdk, Claude Code SDK, claude-code-sdk]
pitch: "SDK d'Anthropic qui expose la boucle d'agent de Claude Code comme bibliothèque (Python, TypeScript) — outils intégrés (fichiers, shell, web), sous-agents, hooks, permissions, sessions, MCP, skills ; réservé aux modèles Claude, sous conditions commerciales d'Anthropic."
categorie: llm/agents
famille: paquet
domaines: [ai-eng]
licence_type: open-core
maturite: beta
langage: Python, TypeScript
alternatives: ["[[Deep Agents]]"]
complements: []
tags: [llm, agents, multi-agent, tool-use, mcp]
url_docs: https://code.claude.com/docs/en/agent-sdk/overview
url_repo: https://github.com/anthropics/claude-agent-sdk-python
---

# Claude Agent SDK

<!-- AUTO:BANDEAU:START -->
> SDK d'Anthropic qui expose la boucle d'agent de Claude Code comme bibliothèque (Python, TypeScript) — outils intégrés (fichiers, shell, web), sous-agents, hooks, permissions, sessions, MCP, skills ; réservé aux modèles Claude, sous conditions commerciales d'Anthropic.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python, TypeScript | open-core | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Le **Claude Code SDK, rebaptisé** : la même boucle d'agent que Claude Code, programmable depuis
Python ou TypeScript. La bibliothèque pilote le binaire Claude Code, livré dans le paquet, et
hérite de ses capacités — lire, écrire et éditer des fichiers, lancer des commandes, chercher sur
le web, plus les **sous-agents**, les **hooks** (du code exécuté à des points fixes du cycle), les
permissions, les sessions reprenables, [[mcp-protocol|MCP]], les skills et la mémoire `CLAUDE.md`
chargés depuis `.claude/`. Ce n'est pas un framework de graphes : on ne câble pas la boucle, on
configure un agent déjà complet. Le prix est un couplage total à Claude et à l'outillage
d'Anthropic. Les sous-agents et leur isolation sont détaillés dans
[[Sous-agents et isolation du contexte]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Embarquer l'agent de Claude Code dans sa propre application : outils, permissions, sessions et hooks sont déjà là | Modèle autre que Claude : le SDK est conçu autour de Claude, aucun autre fournisseur n'est documenté |
| Agent qui travaille sur des fichiers et un shell — revue de code, migration, analyse d'un dépôt — sans réécrire les outils | Environnement isolé du réseau : un accès à l'API Claude est indispensable, pas d'exécution hors ligne ni air-gap |
| Déléguer à des sous-agents à outils restreints, avec plafonds de profondeur, de concurrence et de budget | Revendre un produit sans avoir lu les conditions : l'usage est régi par les conditions commerciales d'Anthropic, y compris pour les produits qu'on propose à ses clients |
| Réutiliser tels quels ses skills, serveurs MCP et fichiers `.claude/` | API à figer : version 0.x classée Alpha sur PyPI, publiée à un rythme très soutenu (0.2.162 en septembre 2026, un an et demi après la création du dépôt) — épingler |

## Mise en œuvre

- Installation — `pip install claude-agent-sdk` (Python ≥ 3.10) ou `npm install @anthropic-ai/claude-agent-sdk` ; le binaire Claude Code est fourni dans le paquet
- Point d'entrée — `query(prompt=…, options=ClaudeAgentOptions(…))` ; sous-agents passés en `agents={"nom": AgentDefinition(description, prompt, tools, model)}`, appelés par l'outil `Agent`
- Prérequis — une clé d'API Anthropic ; la connexion claude.ai n'est pas autorisée pour un produit tiers, sauf accord préalable
- Exécution — en bibliothèque dans l'application hôte, qui lance le binaire en sous-processus
- Coût — SDK gratuit ; tokens Claude facturés, sous-agents compris — plafonner avec `max_budget_usd`, la profondeur d'imbrication (3 par défaut) et la concurrence (20 par défaut)

## Écosystème

### Alternatives

- [[Deep Agents]] — Harnais d'agent « batteries incluses » de l'équipe LangChain (MIT), construit sur LangGraph — système de fichiers à backends interchangeables, sous-agents à contexte isolé (outil `task`), résumé et déport du contexte sur disque, planification en option (`write_todos`) ; agnostique du modèle, Python et TypeScript. — même famille de harnais, sans verrou de modèle : à prendre dès que le fournisseur doit pouvoir changer.
- [[OpenAI Agents SDK]] — voisin : le SDK équivalent côté OpenAI, mais minimal — des primitives (agents, handoffs, guardrails), pas de harnais avec fichiers et shell fournis.

## Ressources

- Documentation — https://code.claude.com/docs/en/agent-sdk/overview
- Documentation — https://code.claude.com/docs/en/agent-sdk/subagents
- Dépôt — https://github.com/anthropics/claude-agent-sdk-python
- Dépôt — https://github.com/anthropics/claude-agent-sdk-typescript

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Sous-agents et isolation du contexte]] — l'isolation, le retour d'un seul message, les plafonds
- [[Harnais d'agent]] — ce que ce SDK fournit tout fait
- [[Agent skills]] — les skills chargés depuis `.claude/`
- [[mcp-protocol]] — le protocole des outils externes
- [[Context engineering]] — le budget de contexte, géré par le binaire
