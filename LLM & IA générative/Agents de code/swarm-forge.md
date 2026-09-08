---
role: brique
nom: swarm-forge
alias: [unclebob/swarm-forge, swarm]
pitch: "Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée."
categorie: llm/agent-de-code
famille: cli
licence_type: 
os: "Linux, macOS, Windows (WSL)"
langage: Clojure
alternatives: ["[[CrewAI]]", "[[AutoGen]]"]
complements: []
tags: [multi-agent, agents, code-assistant, cli, version-control]
url_docs: https://github.com/unclebob/swarm-forge
url_repo: https://github.com/unclebob/swarm-forge
---

# swarm-forge

<!-- AUTO:BANDEAU:START -->
> Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Clojure | — | en ligne de commande, rien à héberger | — | à jour · 2026-08-30 |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche d'orchestration légère, bâtie sur **tmux**, qui fait travailler plusieurs agents de code
en parallèle. Deux idées la structurent. D'abord l'**isolation par git worktree** : chaque agent
a son rôle et son propre worktree, donc ses propres fichiers — les agents ne se marchent pas
dessus, et le résultat de chacun se relit comme une branche. Ensuite la **communication
asynchrone par handoff** : un démon `handoffd.bb` route les messages entre boîtes d'entrée et de
sortie, via trois scripts (`swarm_handoff.sh`, `ready_for_next.sh`, `done_with_current.sh`), et
une porte d'audit interdit de resoumettre deux fois un handoff inchangé — garde-fou contre les
boucles stériles. Écrit par Robert C. Martin en Clojure (scripts Babashka `bb`) et shell zsh ;
le dashboard s'ouvre dans le navigateur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Découper une tâche large entre plusieurs agents de code sans qu'ils se disputent l'arbre de travail | **Contexte professionnel : le dépôt ne déclare aucune licence.** Un dépôt public sans fichier LICENSE n'accorde aucun droit d'usage, de modification ni de redistribution — à réserver à l'exploration personnelle tant que ce n'est pas corrigé |
| Rester en terminal, sur sa machine, sans plateforme ni service tiers | Construire une application multi-agents : ce n'est pas un framework, on n'écrit rien avec — on orchestre des CLI tierces déjà installées → [[CrewAI]], [[AutoGen]] |
| Étudier une approche d'orchestration en essaim minimaliste, lisible de bout en bout | Sans tmux, ou avec une exigence d'interface graphique : la dépendance est forte, et le copier-coller comme la navigation entre panes déroutent quand plusieurs agents parlent en même temps |
| | Besoin de déploiement ou de reprise après incident : local uniquement, mono-machine |
| | Exigence de stabilité : ni versioning, ni release, ni documentation au-delà du README et d'`AGENTS.md`, aucune roadmap publiée |
| | Quota d'abonnement serré : l'outil consomme autant de quota que d'agents lancés en parallèle, et la dépense n'est visible nulle part |

## Mise en œuvre

- Installation — télécharger le script `get-swarm-forge` dans le PATH, l'exécuter dans un dossier « forge », puis lancer `./swarm` ; aucun gestionnaire de paquets
- Point d'entrée — session tmux avec un pane par agent, plus un dashboard dans le navigateur
- Prérequis — `zsh`, `git`, `tmux`, Babashka, et au moins un backend IA configuré (claude, codex, copilot, grok)
- Exécution — sur le poste, mono-machine ; macOS, Linux, Windows via WSL. Empêcher la veille avec `caffeinate` sous macOS, `systemd-inhibit` sous Linux
- Coût — pas de prix affiché, mais **pas de droit d'usage non plus** : `licence_type` est laissé vide ici volontairement, le déclarer `open-source` serait faux. La dépense réelle est celle des agents pilotés, multipliée par leur nombre

## Écosystème

### Alternatives

- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).

## Ressources

- Documentation — https://github.com/unclebob/swarm-forge (README et `AGENTS.md` du dépôt, rien d'autre)
- Dépôt — https://github.com/unclebob/swarm-forge

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[agent-loops]] — la boucle perception / action d'un agent
