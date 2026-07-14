---
galaxie: dev
type: outil
nom: Graphify
alias: [graphify, graphifyy]
pitch: "Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP."
categorie: tooling/code-assistant
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
status: actif
alternatives: []
tags: [code-assistant, knowledge-graph, mcp, context-engineering]
url_docs: https://github.com/safishamsi/graphify
url_repo: https://github.com/safishamsi/graphify
---

# Graphify

## Pourquoi

Graphify (MIT, Python) indexe un dossier — code, SQL, scripts, docs, papers, images, vidéos — en un **knowledge graph persistant** interrogeable. Extraction structurelle via Tree-sitter, graphe via NetworkX, détection de communautés par clustering Leiden. Il fait émerger ce qu'un grep ne voit pas : dépendances entre fonctions, modules centraux (*god nodes*), regroupements de fichiers par domaine (*communities*). Objectif : l'assistant IA lit la carte du code avant de fouiller fichier par fichier — moins de tokens, plus de justesse (réduction annoncée jusqu'à ~49x). Sortie compatible Obsidian dans `graphify-out/`. S'installe comme skill (`/graphify`) pour Claude Code, Cursor, Codex, Gemini CLI, et expose un serveur MCP (`query_graph`, `get_node`, `get_neighbors`, `shortest_path`).

## Quand l'utiliser

- Donner à un assistant IA la structure d'un dépôt sans lui faire grep toute la base : lecture du graphe d'abord, économie de contexte.
- Naviguer un gros codebase inconnu : repérer god nodes et communautés, tracer un chemin de dépendances entre deux symboles.
- Indexer un corpus hétérogène (code + docs + schémas SQL + diagrammes) en un seul graphe interrogeable.

## Quand NE PAS l'utiliser

- Écrire ou éditer du code : Graphify n'est pas un assistant de codage → [[Dev/Outils/Cline|Cline]], [[Dev/Outils/Aider|Aider]], [[Dev/Outils/Continue|Continue]].
- Petit projet où un grep suffit : le coût d'indexation ne se rentabilise pas.

## Bases & plateformes

- Open-source MIT, écrit en Python (requiert Python 3.10+). Multiplateforme (Windows, macOS, Linux).
- Distribué sur PyPI sous le nom `graphifyy` (double y) ; commande `graphify` + serveur `graphify-mcp`. Install recommandée `uv tool install graphifyy` (ou pipx/pip), puis `graphify install` pour l'enregistrer comme skill.
- L'extraction structurelle repose sur Tree-sitter + NetworkX ; l'extraction sémantique fine peut s'appuyer sur un LLM.

## Pièges

- Le graphe est un artefact à régénérer : sur une base qui bouge, un graphe périmé induit l'assistant en erreur (relancer l'indexation).
- Indexer de gros dépôts prend du temps et de la mémoire ; l'extraction sémantique LLM a un coût.
- `graphify install` écrit aussi un bloc dans `~/.claude/CLAUDE.md` en plus du skill dans `~/.claude/skills/` — à connaître si l'on soigne ses fichiers de config globaux.
- Sous Windows/PowerShell : appeler `graphify .` et non `/graphify .` (le `/` est un séparateur de chemin).

## Alternatives

- Pas d'équivalent direct fiché dans le brain à ce jour (voisin fonctionnel non documenté : code-review-graph / CRG). À ne pas confondre avec les assistants de code — [[Dev/Outils/Aider|Aider]], [[Dev/Outils/Cline|Cline]], [[Dev/Outils/Continue|Continue]] — de fonction différente.

## Liens

- [[Construction de graphes de connaissances]] — concept : bâtir un graphe de connaissances interrogeable
- Repo & doc : https://github.com/safishamsi/graphify
