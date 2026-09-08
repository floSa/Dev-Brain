---
role: brique
nom: OpenViking
alias: [openviking, viking]
pitch: "Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens."
categorie: llm/memoire
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Letta]]", "[[Hermes Agent]]", "[[ai-memory]]"]
complements: []
tags: [agent-memory, rag, context-engineering, agents, retrieval, mcp]
url_docs: https://docs.openviking.ai/
url_repo: https://github.com/volcengine/OpenViking
---

# OpenViking

<!-- AUTO:BANDEAU:START -->
> Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · mono-nœud | beta | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de contexte pour agents, publié par Volcengine (ByteDance), qui fusionne trois
briques habituellement séparées : mémoire long terme, recherche documentaire et skills
dynamiques. Le parti pris est structurel — au lieu d'un index vectoriel opaque interrogé en
aveugle, il présente mémoires, ressources et skills comme un **système de fichiers virtuel**
`viking://` que l'agent parcourt avec `ls`, `tree` et `find` : la recherche vectorielle sert
à trouver le bon répertoire, ensuite l'agent descend, et la trajectoire devient observable
donc débogable, ce qu'un top-k de similarité ne permet pas. Chaque contenu est pré-découpé en
**trois niveaux** chargés à la demande — L0, résumé d'une centaine de tokens ; L1, environ
2 000 ; L2, le brut —, ce qui fait du budget de contexte un choix explicite et non un effet
de bord du chunking. La mémoire long terme est extraite automatiquement des sessions, ce qui
suppose un fournisseur LLM et embeddings externe : le serveur n'est pas autonome. Python
principalement, avec des composants Rust.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner à un agent une mémoire persistante dont on peut **auditer les accès**, et pas seulement mesurer la pertinence | Produit fermé ou service réseau propriétaire : le cœur est en AGPL-3.0 et le copyleft s'étend à l'usage en service → [[Letta]], sous Apache-2.0 |
| Maîtriser finement le budget de tokens sur un gros corpus : charger un résumé, puis descendre seulement si nécessaire | Besoin d'une base vectorielle brute, sans couche de mémoire par-dessus → [[Qdrant]], [[pgvector]] |
| Unifier mémoire, RAG et skills derrière un seul serveur, au lieu d'assembler trois systèmes | API et formats de données encore mouvants — la 0.3.x l'annonce elle-même : verrouiller la version |
| | Aucune offre managée et pas de chemin d'installation clé en main : tout est à exploiter soi-même |

## Mise en œuvre

- Installation — `pip install openviking`, puis `openviking-server init` et `openviking-server doctor` ; image Docker officielle et CLI standalone
- Point d'entrée — serveur exposant l'arborescence `viking://` ; intégrations annoncées avec Claude Code, Codex, Cursor, OpenCode, LangChain/LangGraph et MCP
- Prérequis — Python 3.10+ ; Linux, macOS (ARM et Intel), Windows x64 ; une application desktop compagnon est en beta
- Exécution — self-hébergé uniquement, mono-nœud : aucune offre managée n'est documentée dans le dépôt, malgré l'éditeur
- Coût — gratuit ; le coût réel est l'infrastructure, plus les appels au fournisseur LLM et embeddings choisi, ou un [[Ollama]] local

## Écosystème

### Alternatives

- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.
- [[ai-memory]] — Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.

## Ressources

- Documentation — https://docs.openviking.ai/
- Dépôt — https://github.com/volcengine/OpenViking

## Voir aussi

- [[Agent memory]] — la notion : mémoire persistante d'agent
- [[Context engineering]] — la notion : composition et budget du contexte
- [[RAG]] — la notion : génération augmentée par récupération
- [[Agent skills]] — la notion : compétences packagées d'un agent
- [[LLM & IA générative]] — le hub du domaine
