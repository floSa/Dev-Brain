---
role: brique
nom: Graphify
alias: [graphify, graphifyy]
pitch: "Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
alternatives: ["[[ai-memory]]"]
complements: []
tags: [code-assistant, knowledge-graph, mcp, context-engineering]
url_docs: https://github.com/safishamsi/graphify
url_repo: https://github.com/safishamsi/graphify
---

# Graphify

<!-- AUTO:BANDEAU:START -->
> Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Indexe un dossier — code, SQL, scripts, docs, papers, images, vidéos — en un **knowledge graph
persistant** interrogeable : extraction structurelle par Tree-sitter, graphe NetworkX, détection
de communautés par clustering Leiden. Il fait émerger ce qu'un grep ne voit pas — dépendances
entre fonctions, modules centraux (*god nodes*), regroupements de fichiers par domaine. Il
n'écrit pas de code : il fournit à l'assistant la carte du dépôt avant que celui-ci ne fouille
fichier par fichier, d'où l'économie de contexte annoncée (jusqu'à ~49×). Sortie compatible
Obsidian dans `graphify-out/`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner à un assistant IA la structure d'un dépôt sans lui faire grep toute la base : lecture du graphe d'abord, économie de contexte | Petit projet où un grep suffit : le coût d'indexation ne se rentabilise pas |
| Naviguer un gros codebase inconnu : repérer god nodes et communautés, tracer un chemin de dépendances entre deux symboles | Base qui bouge vite : le graphe est un artefact à régénérer, et périmé il induit l'assistant en erreur |
| Indexer un corpus hétérogène (code + docs + schémas SQL + diagrammes) en un seul graphe interrogeable | Gros dépôt à indexer souvent : l'indexation prend du temps et de la mémoire, et l'extraction sémantique par LLM a un coût |

## Mise en œuvre

- Installation — `uv tool install graphifyy` (double y sur PyPI ; `pipx` ou `pip` sinon), puis `graphify install` pour l'enregistrer comme skill — qui écrit aussi un bloc dans `~/.claude/CLAUDE.md` en plus du skill dans `~/.claude/skills/`
- Point d'entrée — commande `graphify` et serveur `graphify-mcp` (`query_graph`, `get_node`, `get_neighbors`, `shortest_path`) ; skill `/graphify` pour Claude Code, Cursor, Codex, Gemini CLI — sous Windows/PowerShell, appeler `graphify .` et non `/graphify .`, le `/` étant un séparateur de chemin
- Prérequis — Python 3.10+ ; un LLM seulement pour l'extraction sémantique fine, l'extraction structurelle s'en passe
- Exécution — sur le poste, en ligne de commande ; Windows, macOS, Linux
- Coût — gratuit, MIT ; la seule dépense est celle de l'extraction sémantique quand on l'active

## Écosystème

### Alternatives

- [[ai-memory]] — Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.
- Pas d'autre équivalent direct fiché dans le brain à ce jour ; voisin fonctionnel non documenté : code-review-graph / CRG.

## Ressources

- Documentation — https://github.com/safishamsi/graphify
- Dépôt — https://github.com/safishamsi/graphify

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Construction de graphes de connaissances]] — bâtir un graphe de connaissances interrogeable
