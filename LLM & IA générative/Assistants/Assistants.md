---
role: hub
nom: Assistants
alias: [assistants IA, agents applicatifs]
pitch: Les applications d'agent prêtes à déployer — un produit devant un utilisateur, pas une bibliothèque à assembler.
domaines: [ai-eng]
tags: [agents, agent-memory, local-llm, mcp, agent-skill]
---

# Assistants

> Les applications d'agent prêtes à déployer — un produit devant un utilisateur, pas une bibliothèque à assembler.

## Ce qu'il faut comprendre

- Ce dossier se distingue de [[Agents]] et de [[Agents de code]] par **ce qu'on installe** : ici, une application complète avec son interface, sa persistance et ses intégrations. On ne l'assemble pas, on la déploie et on la configure. La conséquence pratique est que le périmètre fonctionnel est celui du produit : on ne l'étend qu'aux endroits prévus — outils, skills, serveurs MCP.
- Le vrai axe de choix est **le canal par lequel l'utilisateur parle à l'agent**, parce que c'est lui qui décide de l'adoption : une messagerie grand public ([[OpenClaw]] — WhatsApp, Telegram, Discord, Signal), une application de bureau ([[LM Studio Bionic]]), une interface web auto-hébergée ([[Hermes Agent]], [[OpenHands]]), ou une classe virtuelle ([[OpenMAIC]]).
- Le second axe est **où tourne l'inférence**, et il n'est pas cosmétique en contexte on-prem : [[LM Studio Bionic]] infère localement par défaut et ne bascule vers un cloud que sur demande ; [[OpenClaw]] et [[Hermes Agent]] tournent sur la machine de l'utilisateur ou son VPS ; [[OpenHands]] existe aussi en cloud managé. C'est ce qui décide si des données sensibles sortent, et c'est à vérifier avant toute autre caractéristique.
- Ces produits sont ceux qui poussent le plus loin la **mémoire persistante** et l'**auto-extension**, parce que c'est ce qu'un usage quotidien exige : [[Hermes Agent]] boucle sur lui-même et se fabrique des skills réutilisables, [[Letta]] est la brique du domaine qui traite ce problème de front. Cf. [[Agent memory]] et [[Agent skills]].
- **Un assistant qui exécute des actions sur la machine de son utilisateur est une surface d'attaque**, et le canal grand public l'élargit : tout message reçu est une entrée non fiable. Cf. [[Prompt injection]], [[Guardrails]] et [[Human-in-the-loop]] — la confirmation avant action irréversible n'est pas une option de confort ici.
- La **gouvernance du projet** mérite un coup d'œil avant de déployer, parce qu'elle prédit la durée de vie : fondation à but non lucratif pour [[OpenClaw]], incubation ASF pour [[Maka]], laboratoire de recherche pour [[Hermes Agent]] et [[OpenMAIC]], éditeur privé pour [[LM Studio Bionic]].

## Choisir

- Un assistant personnel joignable depuis WhatsApp ou Telegram, sur ma machine → [[OpenClaw]].
- Un agent de bureau qui infère en local, projets et transcription inclus → [[LM Studio Bionic]].
- Un agent qui apprend dans la durée et se crée ses propres skills → [[Hermes Agent]].
- Un agent de développement autonome, du shell au navigateur → [[OpenHands]].
- Transformer un document ou un sujet en cours interactif → [[OpenMAIC]].
- Écrire mon propre agent plutôt que déployer le leur → [[Agents]].
- Un agent qui édite du code dans mon dépôt → [[Agents de code]].

<!-- AUTO:START -->
### Briques
- [[Hermes Agent]] — Agent IA auto-hébergé de Nous Research (MIT) doté d'une boucle d'apprentissage fermée — mémoire persistante entre sessions et création autonome de skills réutilisables ; 40+ outils, serveurs MCP et une vingtaine de canaux de discussion, du VPS à 5 $ au cluster GPU.
- [[LM Studio Bionic]] — Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes.
- [[OpenClaw]] — Assistant personnel IA auto-hébergé (MIT, ex-Warelay/Moltbot, gouverné par une fondation à but non lucratif) — agent joignable depuis WhatsApp, Telegram, Discord ou Signal, qui exécute des tâches via outils, skills et serveurs MCP sur la machine de l'utilisateur.
- [[OpenHands]] — Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé.
- [[OpenMAIC]] — Application de classe virtuelle multi-agents (MIT, THU-MAIC / Tsinghua) — transforme un sujet ou un document en cours interactif : slides narrées, quiz, simulations HTML, professeur et camarades IA qui parlent et dessinent au tableau ; export PPTX/HTML, hébergé ou auto-déployé.
<!-- AUTO:END -->
