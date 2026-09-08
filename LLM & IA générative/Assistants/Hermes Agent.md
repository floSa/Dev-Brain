---
role: brique
nom: Hermes Agent
alias: [hermes-agent, nous-hermes-agent]
pitch: "Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU."
categorie: llm/assistant
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: "Python, TypeScript"
scaling: single-node
alternatives: ["[[OpenClaw]]", "[[LM Studio Bionic]]", "[[OpenViking]]"]
complements: []
tags: [llm, agents, tool-use, mcp]
url_docs: https://hermes-agent.nousresearch.com/docs/
url_repo: https://github.com/NousResearch/hermes-agent
---

# Hermes Agent

<!-- AUTO:BANDEAU:START -->
> Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python, TypeScript | open-source | self-hébergé · mono-nœud | production | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent auto-hébergé publié par **Nous Research** en février 2026, dont le parti pris tient en
une phrase : il est censé **s'améliorer à l'usage**. La boucle est fermée et a quatre temps —
mémoire curée par l'agent lui-même, **création autonome de skills** après une tâche complexe,
raffinement de ces skills à la réutilisation, et rappel inter-sessions par recherche plein
texte (SQLite FTS5) doublée de résumés par LLM ; s'y ajoute une modélisation de l'utilisateur
(Honcho) qui se construit au fil des échanges. Côté outillage : plus de 40 outils intégrés, des
serveurs MCP, une vingtaine de canaux d'accès derrière une passerelle de messagerie unique, et
six backends d'exécution au choix. Le modèle de langage, lui, reste externe et interchangeable.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un assistant qui **capitalise** : la mémoire et les skills accumulés sont le produit, pas un effet de bord | Construire un agent dans sa propre application : c'est un agent fini, pas une bibliothèque → [[Agno]], [[OpenAI Agents SDK]], [[LangGraph]] |
| Disposer d'un serveur permanent — VPS, machine perso, cluster — et vouloir y garder l'exécution | Vouloir la mémoire comme primitive exposée par API, réutilisable dans un produit tiers → [[Letta]] |
| Avoir besoin de backends d'exécution variés : Docker pour le risque, SSH pour une machine distante, serverless pour ne payer qu'à l'usage | Tâche ponctuelle et sans état : la boucle d'apprentissage n'a rien à capitaliser → [[smolagents]] |
| Joindre l'agent depuis les messageries déjà en place, derrière une passerelle unique | **Skills auto-créés non relus** : l'agent écrit du code réutilisé ensuite en boucle, et un skill erroné se rejoue indéfiniment |
| | **Mémoire qui enfle et dérive** : sans invalidation, les souvenirs s'accumulent — bruit, coût, contexte saturé — et les faits périmés survivent |
| | **Injection de prompt** : messageries ouvertes d'un côté, shell de l'autre ; cloisonner par un backend Docker plutôt que local |
| | Versions **0.x** et rythme de publication rapide (v0.20.0 début août 2026) : épingler la version |

## Mise en œuvre

- Installation — Linux, macOS, WSL2, Termux, et Windows natif par installateur PowerShell
- Point d'entrée — une CLI, plus une vingtaine de canaux de messagerie derrière la passerelle : Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams
- Prérequis — un endpoint de modèle externe (Nous Portal, OpenRouter, OpenAI, Anthropic ou tout endpoint compatible), avec **64 k de contexte minimum**
- Exécution — mono-nœud, du VPS à 5 $ au cluster GPU ; l'échelle se joue sur le backend d'exécution — local, Docker, SSH, Singularity, Modal, Daytona
- Coût — gratuit, licence MIT ; la dépense réelle est celle des appels au modèle, curation de mémoire et création de skills comprises

## Écosystème

### Alternatives

- [[OpenClaw]] — Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.
- [[LM Studio Bionic]] — Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

## Ressources

- Documentation — https://hermes-agent.nousresearch.com/docs/
- Dépôt — https://github.com/NousResearch/hermes-agent

## Voir aussi

- [[Assistants]] — le hub du dossier : ce qui distingue une application d'agent d'une bibliothèque
- [[OpenHands]] — le voisin du dossier spécialisé sur le développement
- [[Pattern - Agent sur LLM auto-hébergé]] — le brancher sur un modèle local, et les 64 k de contexte exigés
- [[Agent memory]] · [[Agent skills]] — les deux primitives sur lesquelles repose sa boucle d'apprentissage
- [[Agent patterns]] · [[agent-loops]] · [[Tool use patterns]] — les schémas qu'il met en œuvre
- [[Harnais d'agent]] — la catégorie : le modèle reste interchangeable derrière
- [[mcp-protocol|MCP]] · [[fastmcp]] — les serveurs d'outils qu'il consomme, et de quoi en écrire
- [[a2a-protocol|A2A]] — le protocole v1.0 qu'il implémente depuis la v0.20.0 pour dialoguer avec des agents tiers
- [[Modal]] · [[Daytona]] · [[Sandboxing de code généré]] — les bacs à sable managés de ses backends d'exécution
- [[Prompt injection]] · [[AI security]] — la surface d'attaque à traiter avant tout déploiement
