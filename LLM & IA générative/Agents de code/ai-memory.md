---
role: brique
nom: ai-memory
alias: [akitaonrails/ai-memory]
pitch: "Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code."
categorie: llm/agent-de-code
famille: plateforme
domaines: [ai-eng]
licence_type: open-source
os: "Linux, macOS, Windows (WSL2)"
langage: Rust
alternatives: ["[[Graphify]]", "[[OpenViking]]"]
complements: []
tags: [agent-memory, mcp, context-engineering, code-assistant, retrieval]
url_docs: https://github.com/akitaonrails/ai-memory
url_repo: https://github.com/akitaonrails/ai-memory
---

# ai-memory

<!-- AUTO:BANDEAU:START -->
> Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Rust | open-source | — | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur MCP et HTTP qui capture les prompts, les appels d'outils et les bornes de session des
CLI de code, puis les consolide en **pages markdown de type wiki, versionnées par git** : la
mémoire produite est lisible par un humain et diffable, pas seulement récupérable par un modèle.
L'argument central est le **passage de relais entre outils** — quitter Claude Code au milieu
d'une tâche et reprendre sous Codex ou Cursor dans le même répertoire, sans réexpliquer
l'architecture. Stockage SQLite avec FTS5 et un seul writer sérialisé ; recherche par plein
texte, matching d'entités et classement vectoriel optionnel. Le corollaire du versionnement :
cette mémoire grossit et peut contenir des extraits de code sensibles — elle se traite comme le
dépôt lui-même.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Alterner entre plusieurs CLI d'agents sur le même dépôt et vouloir un contexte partagé entre elles | Windows natif : le support est expérimental, WSL2 est la voie recommandée |
| Garder une trace inspectable de ce que les agents ont appris d'un projet, sous forme de fichiers markdown versionnés | Mémoire d'un agent applicatif que l'on construit, plutôt que d'une CLI de code : ce n'est pas la cible → [[Letta]], [[OpenViking]] |
| Éviter de réexpliquer la même architecture à chaque nouvelle session | Contexte multi-utilisateur ou multi-instance : un seul serveur par répertoire de données, jamais deux en concurrence, et l'authentification demande une configuration soignée |
| | Débit d'écriture élevé : l'auteur mesure un plafond de l'ordre de 700 écritures par seconde |
| | Aucune sortie de données tolérée : le classement vectoriel, s'il est activé, implique un fournisseur d'embeddings |

## Mise en œuvre

- Installation — binaires natifs prébuild pour Linux et macOS (voie recommandée), images Docker amd64 et arm64, paquets AUR sous Arch, ou build depuis les sources avec `cargo` (Rust 1.95+)
- Point d'entrée — serveur MCP ou hooks selon l'agent ; certains agents ne supportent que l'un des deux, vérifier la matrice avant de compter sur une capture complète
- Prérequis — un répertoire de données par serveur ; un fournisseur d'embeddings seulement si l'on active le classement vectoriel (OpenAI, Voyage, Gemini ou tout endpoint compatible)
- Exécution — self-hébergé, mono-nœud, sur le poste ou en conteneur ; une vingtaine d'intégrations annoncées (Claude Code, Codex, Cursor, Gemini CLI, OpenCode…), matrice mouvante
- Coût — gratuit, MIT ; seule dépense possible, les embeddings si le classement vectoriel est activé

## Écosystème

### Alternatives

- [[Graphify]] — Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

## Ressources

- Documentation — https://github.com/akitaonrails/ai-memory (pas de site dédié : README et matrice de support vivent dans le dépôt)
- Dépôt — https://github.com/akitaonrails/ai-memory

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Agent memory]] — mémoire persistante d'agent
- [[Context engineering]] — composition et budget du contexte
- [[mcp-protocol]] — le protocole d'exposition d'outils et de ressources
- [[Hybrid retrieval]] — combinaison recherche lexicale et dense
