---
galaxie: dev
type: service
nom: Hermes Agent
alias: [hermes-agent, nous-hermes-agent]
pitch: "Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: "Python, TypeScript"
scaling: single-node
alternatives: ["[[Dev/Services/OpenClaw|OpenClaw]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, mcp]
url_docs: https://hermes-agent.nousresearch.com/docs/
url_repo: https://github.com/NousResearch/hermes-agent
---

# Hermes Agent

## Pourquoi

Agent auto-hébergé publié par **Nous Research** en février 2026. Son parti pris tient en une phrase : l'agent est censé **s'améliorer à l'usage**, via une boucle fermée à quatre temps — mémoire curée par l'agent lui-même, **création autonome de skills** après une tâche complexe, raffinement de ces skills à la réutilisation, et rappel inter-sessions par recherche plein texte (SQLite FTS5) doublée de résumés par LLM. S'y ajoute une modélisation de l'utilisateur (Honcho) qui se construit au fil des échanges.

Sur le plan pratique : plus de 40 outils intégrés, support de serveurs **MCP**, et une vingtaine de canaux d'accès (CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams) derrière une passerelle de messagerie unique. L'exécution de commandes passe par six backends au choix — local, Docker, SSH, Singularity, Modal, Daytona — dont deux serverless qui ne coûtent presque rien à l'arrêt. Le modèle de langage est externe et libre : Nous Portal, OpenRouter, OpenAI, Anthropic ou tout endpoint compatible. Licence **MIT**.

## Quand l'utiliser

- Vouloir un assistant qui **capitalise** : la mémoire et les skills accumulés sont le produit, pas un effet de bord.
- Disposer d'un **serveur permanent** (VPS, machine perso, cluster) et vouloir y garder l'exécution.
- Avoir besoin de **backends d'exécution variés** — bac à sable Docker pour le risque, SSH pour une machine distante, serverless pour ne payer qu'à l'usage.

## Quand NE PAS l'utiliser

- Construire un agent **dans sa propre application** : c'est un agent fini, pas une bibliothèque → [[Dev/Services/Agno|Agno]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/LangGraph|LangGraph]].
- Vouloir la **mémoire comme primitive exposée par API**, réutilisable dans un produit tiers → [[Dev/Services/Letta|Letta]].
- Tâche **ponctuelle et sans état** : la boucle d'apprentissage n'a rien à capitaliser → [[Dev/Services/smolagents|smolagents]].

## Déploiement & coût

- Auto-hébergé : Linux, macOS, WSL2, Termux, et Windows natif (installateur PowerShell).
- Fonctionne sur un **VPS à 5 $** comme sur un cluster GPU ; architecture **mono-nœud**, l'échelle se joue sur le backend d'exécution.
- Gratuit (MIT) ; le coût réel est celui des **appels au modèle**, auxquels s'ajoutent les appels de curation de mémoire et de création de skills.

## Pièges

- **Skills auto-créés non relus** : l'agent écrit lui-même du code réutilisable ensuite en boucle. Un skill erroné se rejoue indéfiniment — les relire comme du code de production. Cf. [[Agent skills]].
- **Mémoire qui enfle et dérive** : sans invalidation, les souvenirs s'accumulent (bruit, coût, contexte saturé) et les faits périmés survivent — cf. [[Agent memory]].
- **Injection de prompt** : agent connecté à des messageries ouvertes et doté d'un shell ; cloisonner via un backend Docker plutôt que local. Cf. [[Prompt injection]].
- Versions **0.x** et rythme de publication rapide (v0.20.0 début août 2026) — épingler la version.

## Alternatives

- [[Dev/Services/OpenClaw|OpenClaw]] — Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.

## Liens

- Même famille d'**agents prêts à l'emploi** que [[Dev/Services/OpenClaw|OpenClaw]] (assistant généraliste sur messageries) et [[Dev/Services/OpenHands|OpenHands]] (agent de développement) — par opposition aux bibliothèques d'agents ([[Dev/Services/Agno|Agno]], [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/smolagents|smolagents]]).
- Partage avec [[Dev/Services/Letta|Letta]] l'idée de **mémoire persistante comme primitive** ; Letta l'expose en API pour d'autres produits, Hermes la garde interne à son propre agent.
- Consomme des serveurs [[mcp-protocol|MCP]] pour son outillage — cf. [[Dev/Services/fastmcp|fastmcp]] pour en écrire — et implémente [[a2a-protocol|A2A]] v1.0 depuis la v0.20.0 pour dialoguer avec des agents tiers.
- Backends d'exécution : local et Docker, puis les bacs à sable managés [[Dev/Services/Modal|Modal]] et [[Dev/Services/Daytona|Daytona]] — cf. [[Sandboxing de code généré]].
- Concepts : [[Agent memory]], [[Agent skills]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]].
- Sécurité : [[Prompt injection]], [[AI security]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://hermes-agent.nousresearch.com/docs/
