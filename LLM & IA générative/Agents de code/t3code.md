---
role: brique
nom: t3code
alias: [t3, T3 Code, t3.codes]
pitch: "Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM."
categorie: llm/agent-de-code
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux, iOS, Android"
langage: TypeScript
alternatives: ["[[Cline]]", "[[Aider]]", "[[Continue]]", "[[Maka]]"]
complements: []
tags: [code-assistant, agents, code-generation]
url_docs: https://github.com/pingdotgg/t3code/tree/main/docs
url_repo: https://github.com/pingdotgg/t3code
---

# t3code

<!-- AUTO:BANDEAU:START -->
> Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript | open-source | Windows, macOS, Linux, iOS, Android | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Ce n'est pas un assistant de codage, c'est une **surface de contrôle au-dessus d'assistants** —
*agent harness control surface*, dit le README. t3code ne se connecte à aucun LLM : il pilote des
CLI d'agents déjà installées sur la machine (Claude Code, Codex, Cursor, OpenCode, Grok). Son
intérêt est la supervision — lancer, suivre et reprendre plusieurs sessions d'agents depuis une
interface unique, en desktop, en web local, ou depuis les applications iOS et Android. Corollaire
direct : qualité, coût et confidentialité restent **entièrement** ceux de la CLI sous-jacente.
Sur la taxonomie du brain, la catégorie `llm/agent-de-code` est retenue faute de case
« orchestration / supervision d'agents » : c'est le rangement le moins faux, pas le rangement
juste — la refonte des domaines a précisé la nature, pas le sujet.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Piloter plusieurs agents de code hétérogènes depuis une seule interface, au lieu d'un terminal par agent | Vouloir un agent qui édite le code lui-même : t3code n'en édite aucun, il supervise ceux qui le font |
| Suivre ou reprendre une session d'agent depuis un téléphone pendant qu'elle tourne sur le poste de travail | Vouloir brancher un LLM auto-hébergé : t3code ne parle à aucun modèle, et la seule voie est **indirecte**, via une CLI qui le fait à sa place — OpenCode dans la liste supportée |
| Rester sur ses abonnements existants : t3code n'ajoute aucune facturation par-dessus | Environnement qui exige de la stabilité : « We are very very early in this project. Expect bugs. », dépôt créé le 2026-02-08, peu de recul terrain, périmètre susceptible de bouger vite |
| | Dépendance à un correctif externe : contributions « mostly not accepting » pour l'instant |
| | Usage hors LAN : l'accès distant depuis mobile expose une surface de contrôle sur une machine de dev — à cadrer réseau avant |

## Mise en œuvre

- Installation — `npx t3@latest` démarre le backend et l'application web en local, sans rien installer ; sinon `winget install T3Tools.T3Code` (Windows), `brew install --cask t3-code` (macOS), `yay -S t3code-bin` (Arch), ou les installeurs desktop des GitHub Releases
- Point d'entrée — application desktop, web local, ou applications clientes iOS et Android
- Prérequis — Node 22.16+, 23.11+ ou 24.10+ ; les agents pilotés doivent être installés et authentifiés séparément — t3code ne les fournit pas
- Exécution — sur le poste ; Windows, macOS, Linux, plus iOS et Android en clients distants
- Coût — gratuit sans réserve, MIT : pas de revente de tokens, pas de palier payant. Le coût reste celui des abonnements agents déjà souscrits

## Écosystème

### Alternatives

Aucune des pages ci-dessous n'est un équivalent : t3code se place **au-dessus** de ces outils,
pas à côté d'eux.

- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Maka]] — Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.

## Ressources

- Documentation — https://github.com/pingdotgg/t3code/tree/main/docs
- Documentation — https://t3.codes (site du projet)
- Dépôt — https://github.com/pingdotgg/t3code

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
