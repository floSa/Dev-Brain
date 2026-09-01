---
galaxie: dev
type: service
nom: OpenViking
alias: [openviking, viking]
pitch: "Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Letta|Letta]]", "[[Dev/Services/Hermes Agent|Hermes Agent]]", "[[Dev/Outils/ai-memory|ai-memory]]"]
remplace_par: []
status: actif
tags: [agent-memory, rag, context-engineering, agents, retrieval, mcp]
url_docs: https://docs.openviking.ai/
url_repo: https://github.com/volcengine/OpenViking
---

# OpenViking

## Pourquoi

Serveur de contexte pour agents, publié par Volcengine (ByteDance), qui fusionne trois briques habituellement séparées : mémoire long terme, recherche documentaire et skills dynamiques.

Le parti pris est structurel. Au lieu d'exposer un index vectoriel opaque que l'agent interroge en aveugle, OpenViking présente mémoires, ressources et skills comme un **système de fichiers virtuel** `viking://` que l'agent parcourt avec `ls`, `tree` et `find`. La recherche vectorielle sert à trouver le bon répertoire ; ensuite l'agent descend. La trajectoire est observable, donc débogable — ce qu'un top-k de similarité ne permet pas.

Chaque contenu est pré-découpé en **trois niveaux** chargés à la demande : L0, résumé d'une centaine de tokens ; L1, environ 2 000 tokens ; L2, le brut. Le budget de contexte devient un choix explicite plutôt qu'un effet de bord du chunking. La mémoire long terme est extraite automatiquement des sessions.

Langage principal Python, avec des composants Rust (`crates/ov_cli`, sous Apache-2.0). Intégrations annoncées : Claude Code, Codex, Cursor, OpenCode, LangChain/LangGraph et MCP.

## Quand l'utiliser

- Donner à un agent une mémoire persistante dont on peut **auditer les accès**, et pas seulement mesurer la pertinence.
- Maîtriser finement le budget de tokens sur un gros corpus : charger un résumé, puis descendre seulement si nécessaire.
- Unifier mémoire, RAG et skills derrière un seul serveur au lieu d'assembler trois systèmes.

## Quand NE PAS l'utiliser

- **Produit fermé ou service réseau propriétaire** : le cœur est en AGPL-3.0. Le copyleft s'étend à l'usage en service — contrainte rédhibitoire pour un éditeur logiciel. Préférer [[Dev/Services/Letta|Letta]] (Apache-2.0).
- Besoin d'une base vectorielle brute, sans couche de mémoire par-dessus → [[Dev/Services/Qdrant|Qdrant]] ou [[Dev/Services/pgvector|pgvector]].
- Recherche d'une API stable : la version 0.3.x annonce elle-même des formats en mouvement.
- Pas d'offre managée : tout est à exploiter soi-même.

## Déploiement & coût

- `pip install openviking`, puis `openviking-server init` et `openviking-server doctor`. Python 3.10+.
- Image Docker officielle, CLI standalone. Linux, macOS (ARM et Intel), Windows x64. Application desktop compagnon en beta.
- `hosted: self` : aucune offre managée documentée dans le dépôt, malgré l'éditeur.
- Mono-nœud. Coût réel = l'infrastructure plus les appels au fournisseur LLM et embeddings choisi (ou un [[Dev/Services/Ollama|Ollama]] local).

## Pièges

- Dépendance à un fournisseur LLM et embeddings externe pour l'extraction de mémoire et l'indexation — le serveur n'est pas autonome.
- Configuration self-host manuelle, sans chemin d'installation clé en main.
- API et formats de données encore mouvants en 0.3.x : verrouiller la version.
- L'AGPL contamine tout service réseau construit dessus. À vérifier avec le juridique avant tout usage professionnel.

## Alternatives

- [[Dev/Services/Letta|Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[Dev/Services/Hermes Agent|Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.
- [[Dev/Outils/ai-memory|ai-memory]] — Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.

## Liens

- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- [[Agent memory]] — concept : mémoire persistante d'agent
- [[Context engineering]] — concept : composition et budget du contexte
- [[RAG]] — concept : génération augmentée par récupération
- [[Agent skills]] — concept : compétences packagées d'un agent
- Docs : https://docs.openviking.ai/ · Repo : https://github.com/volcengine/OpenViking
