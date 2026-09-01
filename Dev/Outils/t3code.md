---
galaxie: dev
type: outil
nom: t3code
alias: [t3, T3 Code, t3.codes]
pitch: "Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM."
categorie: llm/agent-de-code
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux, iOS, Android"
langage: TypeScript
status: en-eval
alternatives: ["[[Dev/Outils/Cline|Cline]]", "[[Dev/Outils/Aider|Aider]]", "[[Dev/Outils/Continue|Continue]]", "[[Dev/Outils/Maka|Maka]]"]
tags: [code-assistant, agents, code-generation]
url_docs: https://github.com/pingdotgg/t3code/tree/main/docs
url_repo: https://github.com/pingdotgg/t3code
---

# t3code

## Pourquoi

t3code (MIT, TypeScript) n'est pas un assistant de codage : c'est une **surface de contrôle au-dessus d'assistants**. Le README parle d'*agent harness control surface*. Il ne se connecte à aucun LLM directement — il pilote des CLI d'agents déjà installées sur la machine : Claude Code, Codex, Cursor, OpenCode, Grok. L'intérêt est la supervision : lancer, suivre et reprendre plusieurs sessions d'agents depuis une interface unique, en desktop Electron, en web local, ou depuis les applications iOS et Android (accès distant décrit dans la doc). Gratuit sans réserve : pas de revente de tokens, pas de palier payant — le coût reste celui des abonnements agents déjà souscrits.

Sur la taxonomie du brain, la catégorie retenue est `llm/agent-de-code` faute de case « orchestration / supervision d'agents » : c'est le rangement le moins faux, pas le rangement juste. La réserve tient toujours après la refonte des domaines — c'est la nature qui a gagné en précision (`famille: application`), pas le sujet.

## Quand l'utiliser

- Piloter plusieurs agents de code hétérogènes depuis une seule interface, au lieu d'un terminal par agent.
- Suivre ou reprendre une session d'agent depuis un téléphone pendant qu'elle tourne sur le poste de travail.
- Rester sur ses abonnements existants : t3code n'ajoute aucune facturation par-dessus.

## Quand NE PAS l'utiliser

- Vouloir un agent qui édite le code lui-même → [[Dev/Outils/Cline|Cline]], [[Dev/Outils/Aider|Aider]], [[Dev/Outils/Continue|Continue]].
- Vouloir brancher un LLM auto-hébergé : t3code ne parle à aucun modèle. La seule voie est **indirecte**, via une CLI qui le fait à sa place — OpenCode dans la liste supportée.
- Environnement qui exige de la stabilité : le projet s'annonce lui-même comme très précoce.

## Installation & plateformes

- Lancement sans installation : `npx t3@latest` démarre le backend et l'application web en local. Node requis en 22.16+, 23.11+ ou 24.10+.
- Paquets système : `winget install T3Tools.T3Code` (Windows), `brew install --cask t3-code` (macOS), `yay -S t3code-bin` (Arch).
- Installeurs desktop distribués via les GitHub Releases ; applications clientes iOS et Android en complément.
- Les agents pilotés doivent être installés et authentifiés séparément — t3code ne les fournit pas.

## Pièges

- Avertissement du README, textuel : « We are very very early in this project. Expect bugs. » D'où le `status: en-eval` retenu ici plutôt qu'`actif`.
- Contributions « mostly not accepting » pour l'instant : dépendance à un projet encore fermé aux correctifs externes.
- Aucun accès direct à un modèle : la qualité, le coût et la confidentialité restent entièrement ceux de la CLI d'agent sous-jacente.
- L'accès distant depuis mobile expose une surface de contrôle sur une machine de dev — à cadrer réseau avant usage hors LAN.
- Créé le 2026-02-08 : peu de recul terrain, périmètre susceptible de bouger vite.

## Alternatives

Aucune des pages ci-dessous n'est un équivalent : t3code se place **au-dessus** de ces outils, pas à côté d'eux.

- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/Maka|Maka]] — Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif des assistants IA de code
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[Agent patterns]] — concept : patrons d'architecture d'agents
- [[agent-loops]] — concept : la boucle perception / action d'un agent
- Doc : https://github.com/pingdotgg/t3code/tree/main/docs
- Site : https://t3.codes
