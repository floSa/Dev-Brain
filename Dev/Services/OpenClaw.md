---
galaxie: dev
type: service
nom: OpenClaw
alias: [openclaw, clawdbot, moltbot, warelay]
pitch: "Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur."
categorie: llm/framework
famille: plateforme
licence_type: open-source
hosted: self
maturite: production
langage: "TypeScript, Swift"
scaling: single-node
alternatives: ["[[Dev/Services/Hermes Agent|Hermes Agent]]", "[[Dev/Services/LM Studio Bionic|LM Studio Bionic]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, mcp]
url_docs: https://docs.openclaw.ai/
url_repo: https://github.com/openclaw/openclaw
---

# OpenClaw

## Pourquoi

Assistant personnel IA **auto-hébergé** dont l'interface principale n'est pas une application dédiée mais les **messageries déjà utilisées** : WhatsApp, Telegram, Discord, Signal, Slack, iMessage. Un composant central, le **Gateway**, tient les sessions, le routage et les connexions de canaux ; l'agent y branche des outils, des **skills** communautaires et des **serveurs MCP**. Le modèle de langage reste externe (Claude, GPT, DeepSeek, ou un modèle local), mais l'exécution et les données restent sur la machine.

Le projet est né **Warelay** en novembre 2025 (Peter Steinberger), renommé **Moltbot** puis **OpenClaw** fin janvier 2026 après une plainte sur la marque. Depuis février 2026, son créateur ayant rejoint OpenAI, le développement est piloté par la **OpenClaw Foundation**, structure à but non lucratif. Licence **MIT**.

## Quand l'utiliser

- Vouloir un assistant personnel **joignable là où les conversations ont déjà lieu**, sans imposer une nouvelle application.
- Garder l'**exécution et les données chez soi** (machine perso, VPS) plutôt que dans un service managé.
- Brancher un parc d'outils hétérogènes via **MCP** sans écrire une intégration par service.

## Quand NE PAS l'utiliser

- Construire un agent **dans sa propre application** : c'est un produit fini, pas une bibliothèque → [[Dev/Services/Agno|Agno]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/LangGraph|LangGraph]].
- Agent de **développement** qui écrit du code et exécute des commandes sur un dépôt → [[Dev/Services/OpenHands|OpenHands]].
- Contexte où l'agent manipulerait des **données sensibles ou réglementées** : la surface d'attaque documentée (cf. *Pièges*) rend l'exercice difficile à défendre.

## Déploiement & coût

- Auto-hébergé uniquement côté projet : installateurs macOS / Linux / WSL2 / Windows, Docker, ou Nix. Runtime Node.js (22+).
- Tourne sans difficulté sur un poste perso ou un petit VPS ; l'architecture reste **mono-nœud**.
- Gratuit (MIT) ; le coût réel est celui des **appels au modèle** choisi. Des hébergeurs tiers non officiels proposent du managé.

## Pièges

- **Injection de prompt** : c'est la faiblesse structurelle du produit — l'agent lit des messages entrants non fiables et dispose d'outils réels. Cf. [[Prompt injection]] et [[AI security]].
- **Permissions trop larges** : accès mail, calendrier et messagerie demandés d'un bloc ; le périmètre accordé est rarement réduit ensuite.
- **Skills tiers non audités** : des cas d'**exfiltration de données** via des skills communautaires ont été documentés (Cisco, 2026). Traiter un skill comme du code non fiable — cf. [[Agent skills]].
- Usage **restreint par certaines administrations** (Chine, mars 2026, pour les entités publiques) — vérifier le cadre avant tout déploiement professionnel.
- Rythme de publication très soutenu et **renommages successifs** : épingler une version, et se méfier de la documentation tierce périmée.

## Alternatives

- [[Dev/Services/Hermes Agent|Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.
- [[Dev/Services/LM Studio Bionic|LM Studio Bionic]] — Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes.

## Liens

- Même famille d'**agents prêts à l'emploi** que [[Dev/Services/Hermes Agent|Hermes Agent]] (assistant généraliste) et [[Dev/Services/OpenHands|OpenHands]] (agent de développement) — par opposition aux bibliothèques d'agents ([[Dev/Services/Agno|Agno]], [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/smolagents|smolagents]]).
- Consomme des serveurs [[mcp-protocol|MCP]] pour son outillage — cf. [[Dev/Services/fastmcp|fastmcp]] pour en écrire.
- C'est un **harnais** au sens de [[Harnais d'agent]] : le modèle reste interchangeable derrière.
- [[Pattern - Agent sur LLM auto-hébergé]] — le brancher sur un modèle local ; attention à l'endpoint natif d'Ollama.
- Concepts : [[Agent skills]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- Sécurité : [[Prompt injection]], [[AI security]], [[Guardrails]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.openclaw.ai/
