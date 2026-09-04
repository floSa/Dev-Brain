---
role: brique
nom: OpenClaw
alias: [openclaw, clawdbot, moltbot, warelay]
pitch: "Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur."
categorie: llm/assistant
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: "TypeScript, Swift"
scaling: single-node
alternatives: ["[[Hermes Agent]]", "[[LM Studio Bionic]]"]
complements: []
tags: [llm, agents, tool-use, mcp]
url_docs: https://docs.openclaw.ai/
url_repo: https://github.com/openclaw/openclaw
---

# OpenClaw

<!-- AUTO:BANDEAU:START -->
> Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript, Swift | open-source | self-hébergé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Assistant personnel auto-hébergé dont l'interface n'est pas une application dédiée mais les
**messageries déjà utilisées** : WhatsApp, Telegram, Discord, Signal, Slack, iMessage. Un
composant central, le **Gateway**, tient les sessions, le routage et les connexions de canaux ;
l'agent y branche des outils, des **skills** communautaires et des serveurs MCP. Le modèle de
langage reste externe — Claude, GPT, DeepSeek, ou un modèle local — mais l'exécution et les
données restent sur la machine. Le projet est né **Warelay** en novembre 2025 (Peter
Steinberger), renommé **Moltbot** puis **OpenClaw** fin janvier 2026 après une plainte sur la
marque ; depuis février 2026, son créateur ayant rejoint OpenAI, il est piloté par la
**OpenClaw Foundation**, à but non lucratif.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un assistant joignable **là où les conversations ont déjà lieu**, sans imposer une application de plus | **Injection de prompt** : c'est la faiblesse structurelle du produit — l'agent lit des messages entrants non fiables et dispose d'outils réels |
| Garder l'exécution et les données chez soi, machine perso ou VPS, plutôt que dans un service managé | **Skills tiers non audités** : des cas d'exfiltration de données via des skills communautaires ont été documentés (Cisco, 2026) |
| Brancher un parc d'outils hétérogènes par MCP, sans écrire une intégration par service | **Permissions trop larges** : accès mail, calendrier et messagerie demandés d'un bloc, et le périmètre accordé est rarement réduit ensuite |
| | Usage **restreint par certaines administrations** (Chine, mars 2026, pour les entités publiques) : vérifier le cadre avant tout déploiement professionnel |
| | Rythme de publication très soutenu et renommages successifs : épingler une version, et se méfier de la documentation tierce périmée |
| | Construire un agent dans sa propre application : c'est un produit fini, pas une bibliothèque → [[Agno]], [[OpenAI Agents SDK]], [[LangGraph]] |
| | Agent de **développement** qui écrit du code et exécute des commandes sur un dépôt → [[OpenHands]] |

## Mise en œuvre

- Installation — installateurs macOS, Linux, WSL2 et Windows, image Docker, ou Nix
- Point d'entrée — le Gateway, et les canaux de messagerie qu'il expose : WhatsApp, Telegram, Discord, Signal, Slack, iMessage
- Prérequis — un runtime Node.js 22 ou plus, et un endpoint de modèle externe (Claude, GPT, DeepSeek, ou un modèle local)
- Exécution — mono-nœud, sur un poste perso comme sur un petit VPS ; des hébergeurs tiers non officiels proposent du managé
- Coût — gratuit, licence MIT ; la dépense réelle est celle des appels au modèle choisi

## Écosystème

### Alternatives

- [[Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.
- [[LM Studio Bionic]] — Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes.

## Ressources

- Documentation — https://docs.openclaw.ai/
- Dépôt — https://github.com/openclaw/openclaw

## Voir aussi

- [[Assistants]] — le hub du dossier : ce qui distingue une application d'agent d'une bibliothèque
- [[Pattern - Agent sur LLM auto-hébergé]] — le brancher sur un modèle local, et l'écueil de l'endpoint natif d'Ollama
- [[Harnais d'agent]] — la catégorie : le modèle reste interchangeable derrière
- [[mcp-protocol|MCP]] · [[fastmcp]] — les serveurs d'outils qu'il consomme, et de quoi en écrire
- [[OpenMAIC]] — l'application de classe virtuelle du dossier, avec qui une intégration messagerie est annoncée (Feishu, Slack, Telegram, Discord)
- [[Agent skills]] · [[Agent memory]] — les deux primitives qu'il expose, et leurs risques propres
- [[Agent patterns]] · [[agent-loops]] · [[Tool use patterns]] — les schémas qu'il met en œuvre
- [[Prompt injection]] · [[AI security]] · [[Guardrails]] — la surface d'attaque, et de quoi la réduire
