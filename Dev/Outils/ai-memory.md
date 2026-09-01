---
galaxie: dev
type: outil
nom: ai-memory
alias: [akitaonrails/ai-memory]
pitch: "Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code."
categorie: tooling/code-assistant
famille: plateforme
domaines: [ai-eng]
licence_type: open-source
os: "Linux, macOS, Windows (WSL2)"
langage: Rust
status: actif
alternatives: ["[[Dev/Outils/Graphify|Graphify]]", "[[Dev/Services/OpenViking|OpenViking]]"]
tags: [agent-memory, mcp, context-engineering, code-assistant, retrieval]
url_docs: https://github.com/akitaonrails/ai-memory
url_repo: https://github.com/akitaonrails/ai-memory
---

# ai-memory

## Pourquoi

Serveur MCP et HTTP écrit en Rust qui capture les prompts, les appels d'outils et les bornes de session des CLI de code, puis les consolide en **pages markdown de type wiki, versionnées par git**. La mémoire produite est lisible par un humain et diffable, pas seulement récupérable par un modèle.

L'argument central est le **passage de relais entre outils** : quitter Claude Code au milieu d'une tâche et reprendre sous Codex ou Cursor dans le même répertoire, sans réexpliquer l'architecture du projet. C'est ce qui le distingue d'une mémoire propre à un assistant.

Stockage SQLite avec FTS5, un seul writer sérialisé. Recherche par plein texte, matching d'entités, et classement vectoriel optionnel (OpenAI, Voyage, Gemini ou tout endpoint compatible).

## Quand l'utiliser

- Alterner entre plusieurs CLI d'agents sur le même dépôt et vouloir un contexte partagé entre elles.
- Garder une trace inspectable de ce que les agents ont appris d'un projet, sous forme de fichiers markdown versionnés.
- Éviter de réexpliquer la même architecture à chaque nouvelle session.

## Quand NE PAS l'utiliser

- Windows natif : le support est expérimental, WSL2 est la voie recommandée.
- Besoin de mémoire pour un agent applicatif que l'on construit, pas pour une CLI de code → [[Dev/Services/Letta|Letta]] ou [[Dev/Services/OpenViking|OpenViking]].
- Contexte multi-utilisateur ou multi-instance : un seul serveur par répertoire de données, et l'authentification demande une configuration soignée.
- Besoin d'un débit d'écriture élevé : l'auteur mesure un plafond de l'ordre de 700 écritures par seconde.

## Installation & plateformes

- Binaires natifs prébuild pour Linux et macOS (voie recommandée), images Docker amd64 et arm64, paquets AUR sous Arch, ou build depuis les sources avec `cargo` (Rust 1.95+).
- Se branche aux agents par MCP ou par hooks selon l'outil. Une vingtaine d'intégrations sont annoncées (Claude Code, Codex, Cursor, Gemini CLI, OpenCode…) ; la matrice bouge vite, se référer au dépôt plutôt qu'à une liste figée.
- Pas de site de documentation : README et matrice de support vivent dans le dépôt.

## Pièges

- Certains agents ne supportent que MCP **ou** les hooks, pas les deux : vérifier la matrice avant de compter sur une capture complète.
- Un serveur par répertoire de données, jamais deux en concurrence sur le même — le writer est unique et sérialisé.
- Le classement vectoriel est optionnel mais implique un fournisseur d'embeddings, donc une sortie de données si l'on choisit un service cloud.
- La mémoire est versionnée par git : elle grossit, et elle peut contenir des extraits de code sensibles. À traiter comme le dépôt lui-même.

## Alternatives

- [[Dev/Outils/Graphify|Graphify]] — Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.
- [[Dev/Services/OpenViking|OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Agent memory]] — concept : mémoire persistante d'agent
- [[Context engineering]] — concept : composition et budget du contexte
- [[mcp-protocol]] — concept : le protocole d'exposition d'outils et de ressources
- [[Hybrid retrieval]] — concept : combinaison recherche lexicale et dense
- Repo : https://github.com/akitaonrails/ai-memory
