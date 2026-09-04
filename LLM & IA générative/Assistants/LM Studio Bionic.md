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
complements: ["[[LM Studio]]"]
tags: [llm, agents, local-llm, mcp, code-generation]
url_docs: https://lmstudio.ai/docs/bionic
url_repo: 
---

# LM Studio Bionic

<!-- AUTO:BANDEAU:START -->
> Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application | propriétaire | self-hébergé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de bureau publié le **16 juillet 2026**, présenté comme « l'agent IA fait pour les
modèles ouverts ». C'est une **application distincte** de LM Studio, et non un mode de
celle-ci : LM Studio reste l'outil de configuration fine du runtime, Bionic est la couche
agentique posée dessus. Le travail s'y organise en **projets** de deux types — *Work*
(recherche, rédaction, analyse, documents, PDF, tableurs, présentations) et *Code* (dépôt
local, avec accès fichiers, recherche, Git et shell, diffs en ligne et points de restauration
automatiques). S'y ajoutent une **transcription vocale hors ligne** via Voxtral, la recherche
web, et l'installation de serveurs MCP. L'inférence est **locale par défaut** ; deux autres
origines de modèle cohabitent — une autre machine du réseau (**LM Link**), ou **LM Studio
Secure Cloud** pour les modèles ouverts de frontière sur les tâches lourdes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un agent **local d'abord**, sur modèles ouverts, avec une interface graphique plutôt qu'un serveur à administrer | **Produit très jeune** : moins d'un mois d'existence à l'été 2026, tarification cloud encore mouvante — pas de flux critique sans réversibilité |
| Travail sur documents et fichiers autant que sur du code : le périmètre revendiqué est plus large que celui d'un assistant de codage | **Fermé** : aucun audit possible de la couche agent, sur un composant qui a pourtant accès au shell et aux fichiers |
| Exigence de confidentialité : transcription vocale et inférence restent sur la machine tant que le cloud n'est pas sollicité | La bascule vers le cloud est le point à surveiller : la rétention zéro est une promesse contractuelle, pas une garantie technique — pour un secret industriel, seul le tout-local se défend |
| Poste déjà équipé de LM Studio : runtime, modèles téléchargés et quantizations sont réutilisés | Un projet *Code* donne à l'agent fichiers, Git et shell sur un dépôt réel ; les points de restauration limitent la casse, ils ne la préviennent pas |
| | Serveurs MCP tiers à traiter comme du **code non fiable** : ils élargissent la surface d'attaque de l'agent |
| | Pas de version serveur ni headless : c'est la contrepartie de la GUI → [[OpenClaw]] pour un agent résident joignable depuis une messagerie |
| | Vouloir un agent qui capitalise entre les sessions — mémoire persistante, skills auto-créés — sur un serveur → [[Hermes Agent]] |
| | Exigence d'open-source ou d'auditabilité de l'agent → [[OpenHands]] |
| | Intégrer l'agent dans sa propre application : c'est un produit fini → [[Agno]], [[OpenAI Agents SDK]] |

## Mise en œuvre

- Installation — application de bureau, **macOS et Windows** uniquement
- Point d'entrée — l'interface graphique, ses projets *Work* et *Code*, et les serveurs MCP qu'on y installe
- Prérequis — le runtime LM Studio pour l'inférence locale ; assez de VRAM pour le modèle visé, sans quoi il bascule en RAM et l'agent devient lent
- Exécution — mono-nœud, éventuellement épaulé par une autre machine du réseau via LM Link (jusqu'à 5 appareils)
- Coût — trois paliers : **gratuit** pour tout l'usage local (agent, modèles llama.cpp et MLX, transcription hors ligne, recherche web, LM Link) ; **pay as you go** au token pour le cloud, de ~0,13 $/M en entrée (DeepSeek V4 Flash) à ~15 $/M en sortie (Kimi K3), inférence aux États-Unis ; **Bionic Pass**, abonnement annoncé sans grille publiée

## Écosystème

### Alternatives

- [[OpenClaw]] — Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.
- [[Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.

### Compléments

- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit. — le runtime du même éditeur sur lequel Bionic est posé.

## Ressources

- Documentation — https://lmstudio.ai/docs/bionic

## Voir aussi

- [[Assistants]] — le hub du dossier : ce qui distingue une application d'agent d'une bibliothèque
- [[Pattern - Agent sur LLM auto-hébergé]] — le montage complet et ses pièges
- [[Harnais d'agent]] — la catégorie : le seul fermé du brain, et le seul à ne pas accepter d'endpoint arbitraire
- [[mcp-protocol|MCP]] · [[fastmcp]] — les serveurs d'outils qu'il consomme, et de quoi en écrire
- [[Agent patterns]] · [[agent-loops]] · [[Tool use patterns]] — les schémas qu'il met en œuvre
- [[Small Language Models]] — la famille de modèles que l'inférence locale rend praticable
- [[Prompt injection]] · [[AI security]] · [[Sandboxing de code généré]] — la surface d'attaque d'un agent qui tient le shell
