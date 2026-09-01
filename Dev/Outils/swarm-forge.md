---
role: brique
nom: swarm-forge
alias: [unclebob/swarm-forge, swarm]
pitch: "Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: 
os: "Linux, macOS, Windows (WSL)"
langage: Clojure
alternatives: ["[[Dev/Services/CrewAI|CrewAI]]", "[[Dev/Services/AutoGen|AutoGen]]"]
complements: []
tags: [multi-agent, agents, code-assistant, cli, version-control]
url_docs: https://github.com/unclebob/swarm-forge
url_repo: https://github.com/unclebob/swarm-forge
---

# swarm-forge

## Pourquoi

Couche d'orchestration légère, bâtie sur **tmux**, qui fait travailler plusieurs agents de code en parallèle. Deux idées structurent l'outil.

D'abord l'**isolation par git worktree** : chaque agent a son rôle et son propre worktree, donc ses propres fichiers. Les agents ne se marchent pas dessus, et le résultat de chacun se relit comme une branche.

Ensuite la **communication asynchrone par handoff** : un démon `handoffd.bb` route les messages entre boîtes d'entrée et de sortie, via trois scripts (`swarm_handoff.sh`, `ready_for_next.sh`, `done_with_current.sh`). Une porte d'audit interdit de resoumettre deux fois un handoff inchangé — garde-fou contre les boucles stériles.

Écrit en Clojure (scripts Babashka `bb`) et shell zsh, par Robert C. Martin. Le dashboard s'ouvre dans le navigateur.

## Quand l'utiliser

- Découper une tâche large entre plusieurs agents de code sans qu'ils se disputent l'arbre de travail.
- Rester en terminal, sur sa machine, sans plateforme ni service tiers.
- Étudier une approche d'orchestration en essaim minimaliste, lisible de bout en bout.

## Quand NE PAS l'utiliser

- **En contexte professionnel : le dépôt ne déclare aucune licence.** Un dépôt public sans fichier LICENSE n'accorde aucun droit d'usage, de modification ni de redistribution. Tant que ce n'est pas corrigé, l'outil est à réserver à l'exploration personnelle.
- Pour construire une application multi-agents : ce n'est pas un framework, on n'écrit rien avec — on orchestre des CLI tierces → [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]].
- Sans tmux, ou si l'on tient à une interface graphique confortable.
- En attendant une garantie de stabilité : ni versioning, ni release, ni documentation au-delà du README.

## Installation & plateformes

- Télécharger le script `get-swarm-forge` dans le PATH, l'exécuter dans un dossier « forge », puis lancer `./swarm`. Aucun gestionnaire de paquets.
- Prérequis : `zsh`, `git`, `tmux`, Babashka, et au moins un backend IA configuré (claude, codex, copilot, grok).
- macOS, Linux, Windows via WSL. Empêcher la veille avec `caffeinate` sous macOS, `systemd-inhibit` sous Linux.

## Pièges

- **Licence absente** — le champ `licence_type` est laissé vide ici volontairement : le déclarer `open-source` serait faux.
- Dépendance forte à tmux : le copier-coller et la navigation entre panes déroutent quand plusieurs agents parlent en même temps.
- Local uniquement, mono-machine : pas de déploiement, pas de reprise après incident.
- Aucune documentation hors README et `AGENTS.md` ; aucune roadmap publiée.
- Consomme autant de quota que d'agents lancés en parallèle — le coût monte vite sans être visible.

## Alternatives

- [[Dev/Services/CrewAI|CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Dev/Services/AutoGen|AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Multi-agent systems]] — concept : systèmes à plusieurs agents coopérants
- [[Agent patterns]] — concept : patrons d'architecture d'agents
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[agent-loops]] — concept : la boucle perception / action d'un agent
- Repo : https://github.com/unclebob/swarm-forge
