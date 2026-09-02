---
role: brique
nom: LM Studio Bionic
alias: [Bionic, lm studio bionic, LM Studio Secure Cloud, LM Link]
pitch: "Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes."
categorie: llm/assistant
famille: application
licence_type: proprietary
hosted: [self]
maturite: production
langage: 
scaling: single-node
alternatives: ["[[OpenClaw]]", "[[Hermes Agent]]"]
complements: []
tags: [llm, agents, local-llm, mcp, code-generation]
url_docs: https://lmstudio.ai/docs/bionic
url_repo: 
---

# LM Studio Bionic

## Pourquoi

Agent de bureau publié par LM Studio le **16 juillet 2026**, présenté comme « l'agent IA fait pour les modèles ouverts ». C'est une **application distincte** de [[LM Studio]], et non un mode de celle-ci : LM Studio reste l'outil de configuration fine du runtime, Bionic est la couche agentique posée dessus.

Le travail s'organise en **projets**, de deux types : *Work* (recherche, rédaction, analyse, documents, PDF, tableurs, présentations) et *Code* (dépôt local, avec accès fichiers, recherche, Git et shell, diffs en ligne et points de restauration automatiques). S'y ajoutent une **transcription vocale hors ligne** via Voxtral, la recherche web, et l'installation de **serveurs [[mcp-protocol|MCP]]** pour étendre l'outillage au-delà du système de fichiers.

L'inférence est **locale par défaut**, via le runtime LM Studio ; trois origines de modèle cohabitent : local, distant sur une autre machine du réseau (**LM Link**), ou **LM Studio Secure Cloud** pour les modèles ouverts de frontière (GLM, Kimi) sur les tâches lourdes, avec rétention zéro annoncée. L'application est **propriétaire**, gratuite en usage local ; le cloud fonctionne au crédit.

## Quand l'utiliser

- Vouloir un agent **local d'abord**, sur modèles ouverts, avec une interface graphique plutôt qu'un serveur à administrer.
- Travail sur **documents et fichiers** autant que sur du code — c'est le périmètre revendiqué, plus large que celui d'un assistant de codage.
- Exigence de **confidentialité** : la transcription vocale et l'inférence restent sur la machine tant que le cloud n'est pas sollicité.
- Poste déjà équipé de LM Studio : le runtime, les modèles téléchargés et les quantizations sont réutilisés.

## Quand NE PAS l'utiliser

- Vouloir un agent **résident et joignable en permanence** depuis une messagerie : Bionic est une application de bureau, sans WhatsApp ni Telegram → [[OpenClaw]].
- Vouloir un agent qui **capitalise entre les sessions** (mémoire persistante, skills auto-créés) sur un serveur → [[Hermes Agent]].
- Exigence d'**open-source** ou d'auditabilité de l'agent : l'application est fermée → [[OpenHands]].
- Intégrer l'agent **dans sa propre application** : c'est un produit fini → [[Agno]], [[OpenAI Agents SDK]].

## Déploiement & coût

- Application de bureau, **macOS et Windows**. Pas de version serveur ni headless — la contrepartie de la GUI.
- Trois paliers annoncés :
  - **Gratuit (0 $)** — l'agent, les modèles locaux (llama.cpp et MLX), la transcription vocale hors ligne, la recherche web, et LM Link jusqu'à 5 appareils. Aucune donnée ne quitte la machine.
  - **Pay as you go** — crédits pour le cloud, facturés au token : de ~0,13 $ / M tokens en entrée (DeepSeek V4 Flash) à ~15 $ / M en sortie (Kimi K3). Inférence aux États-Unis, rétention zéro par défaut.
  - **Bionic Pass** — abonnement annoncé, grille non publiée à ce stade.
- Le gratuit couvre donc tout l'usage **local** ; seul l'appel aux modèles de frontière hébergés est payant.
- Scaling **single-node** : une machine, éventuellement épaulée par une autre du réseau via LM Link.
- Le matériel commande la qualité : un modèle qui dépasse la VRAM bascule en RAM et l'agent devient lent, exactement comme sous LM Studio.

## Pièges

- **Produit très jeune** : moins d'un mois d'existence à l'été 2026, tarification cloud encore mouvante — ne pas bâtir un flux de travail critique dessus sans réversibilité.
- **Propriétaire et fermé** : pas d'audit possible de la couche agent, dépendance à l'éditeur — le même reproche qu'à [[LM Studio]], sur un composant qui a cette fois accès au shell et aux fichiers.
- La bascule vers le cloud est **le point à surveiller** : la rétention zéro est une promesse contractuelle, pas une garantie technique. Pour un secret industriel, le seul mode défendable est le tout-local.
- Un projet *Code* donne à l'agent **fichiers, Git et shell** sur un dépôt réel. Les points de restauration limitent la casse, ils ne la préviennent pas — cf. [[Sandboxing de code généré]].
- Serveurs MCP tiers à traiter comme du **code non fiable** : ils élargissent la surface d'attaque de l'agent. Cf. [[Prompt injection]].

## Alternatives

- [[OpenClaw]] — Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.
- [[Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.

## Liens

- Couche agentique posée sur le runtime de [[LM Studio]] — même éditeur, applications distinctes.
- Même famille d'**agents prêts à l'emploi** que [[OpenClaw]], [[Hermes Agent]] et [[OpenHands]] — mais seul à être une application de bureau fermée, les trois autres étant auto-hébergés et open-source.
- Consomme des serveurs [[mcp-protocol|MCP]] — cf. [[fastmcp]] pour en écrire.
- C'est un **harnais** au sens de [[Harnais d'agent]] — le seul fermé du brain, et le seul à ne pas accepter d'endpoint arbitraire.
- [[Pattern - Agent sur LLM auto-hébergé]] — le montage complet et ses pièges.
- Concepts : [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Small Language Models]].
- Sécurité : [[Prompt injection]], [[AI security]], [[Sandboxing de code généré]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://lmstudio.ai/docs/bionic
