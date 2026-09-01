---
role: notion
nom: mcp-protocol
alias: [MCP, Model Context Protocol, protocole MCP, MCP Apps, MCP Tasks, MRTR, spec 2026-07-28, Agentic AI Foundation]
categorie: concept/llm
domaines: [ai-eng]
tags: [mcp, tool-use, llm, agents]
---

# mcp-protocol

## Aperçu

- **Model Context Protocol** (Anthropic, fin 2024 ; gouvernance transférée à l'**Agentic AI Foundation** / Linux Foundation en 2026) : standard ouvert pour connecter un LLM à des outils, des données et des prompts via une architecture **client-serveur**.
- Idée : remplacer les intégrations sur mesure « un connecteur par couple (app, outil) » par un protocole unique — le « USB-C des applications IA ».
- **Révision majeure du 28 juillet 2026** : le protocole devient **stateless**, gagne un framework d'**extensions** (Tasks, MCP Apps, autorisation managée) et durcit son modèle d'autorisation. C'est une rupture, pas un ajout — plusieurs primitives de la version 2025 sont dépréciées (voir *Ce qui a changé*).

## Concepts clés

### Architecture host / client / serveur

- Un **host** (l'app IA : IDE, agent, app desktop) lance un ou plusieurs **clients** ; chaque client parle à un **serveur** MCP qui expose des capacités. Un serveur = une intégration (fichiers, GitHub, Postgres…).

### Primitives serveur

- **Tools** (fonctions appelables — cf. [[tool-use]]), **Resources** (données contextuelles adressables par URI), **Prompts** (gabarits réutilisables). Le serveur annonce ses capacités, le client les découvre.
- Depuis 2026-07-28, les réponses de `tools/list`, `prompts/list`, `resources/list` et `resources/read` portent des champs **`ttlMs`** et **`cacheScope`** : le client sait combien de temps il peut mettre la liste en cache. Fini le rechargement systématique du catalogue à chaque session.

### Transport & format

- Messages en **JSON-RPC 2.0**. Deux transports : **stdio** (serveur lancé en sous-processus, échange par stdin/stdout) et **Streamable HTTP** (serveurs distants). L'ancien transport HTTP+SSE est **déprécié**.
- Les requêtes HTTP portent désormais des en-têtes **`Mcp-Method`** et **`Mcp-Name`** : une passerelle, un WAF ou un compteur de quota peuvent router et facturer **sans lire le corps JSON**. C'est le changement qui rend MCP opérable en entreprise.

### Ce qui a changé en 2026-07-28

- **Cœur stateless** — la poignée de main `initialize` / `initialized` et l'en-tête `Mcp-Session-Id` **disparaissent**. Chaque requête porte elle-même sa version de protocole, son identité client et ses capacités dans un champ `_meta`. Un `server/discover` optionnel permet de découvrir les capacités en amont.
  - Conséquence opérationnelle, et c'est tout le point : un serveur distant qui exigeait des sessions collantes, un magasin de sessions partagé et de l'inspection de paquets à la passerelle tourne maintenant derrière un simple **round-robin**. C'est ce qui rend MCP déployable comme n'importe quel service HTTP.
- **MRTR (Multi Round-Trip Requests)** — remplace les appels **initiés par le serveur** (`elicitation/create`, `sampling/createMessage`, `roots/list`) qui imposaient de tenir un flux ouvert. Un outil qui a besoin d'une information en cours d'exécution renvoie `resultType: "input_required"` ; le client relance l'appel avec `inputResponses`. Le protocole redevient purement requête/réponse.
- **Extensions** — framework formel. Trois extensions officielles : **Tasks** (`io.modelcontextprotocol/tasks`, travaux longs par `tasks/get` / `tasks/update` et un flux unique `subscriptions/listen`), **MCP Apps** (interfaces **rendues par le serveur** — un serveur peut livrer de l'UI, pas seulement des données) et **EMA** (autorisation managée en entreprise).
- **Autorisation durcie** — le serveur d'autorisation doit renvoyer le paramètre `iss` (RFC 9207) et le client doit le **valider** avant d'échanger le code, ce qui ferme les attaques de type *OAuth mixup* (SEP-2468). Les identifiants client sont **liés à l'émetteur** qui les a créés : plus de réutilisation d'un serveur à l'autre. Le *Dynamic Client Registration* est déprécié au profit des **CIMD** (Client ID Metadata Documents).
- **Politique de dépréciation** — minimum **12 mois** entre annonce et retrait. Déjà dépréciés : Roots, Sampling, Logging, et le transport HTTP+SSE.
- Les cinq SDK (TypeScript, Python, Go, C#, Rust en bêta) suivent la nouvelle spec.

### Ce qui casse concrètement

- Toute implémentation qui s'appuyait sur l'identifiant de session, sur du **streaming serveur → client** (sampling, elicitation en flux tenu) ou sur DCR doit être reprise. Ce n'est pas un ajustement de dépendance : c'est une refonte du cycle de vie de la connexion.
- Point de vigilance pratique : les serveurs MCP en circulation (dépôts publics, outils internes) ne migreront pas tous. Prévoir de cohabiter avec des serveurs en spec 2025 pendant la fenêtre de dépréciation.

### Sécurité

- Un serveur MCP exécute du code et accède à des données : confiance du serveur, périmètre autorisé, consentement utilisateur sur les outils à effet de bord. Surface d'attaque réelle (injection via *resources*, outils malveillants) — cf. [[Prompt injection]].
- Le durcissement 2026 porte sur l'**authentification** (OAuth), pas sur la confiance dans le contenu renvoyé par un serveur. Un serveur authentifié peut toujours renvoyer une charge d'injection : les garde-fous applicatifs restent indispensables.

## Les maths, simplement

- Sans standard, $M$ apps × $N$ outils = $M \times N$ connecteurs à écrire et maintenir.
- Avec un protocole commun, chaque app parle MCP une fois et chaque outil l'expose une fois → $M + N$. C'est tout l'argument économique du standard.
- Le passage au stateless change une autre échelle, celle de l'exploitation : avec sessions collantes, servir $R$ requêtes concurrentes demande un routage qui mémorise $O(R)$ associations session→instance ; sans état, c'est $O(1)$ — n'importe quelle requête sur n'importe quelle instance.

## En pratique

- Utiliser MCP quand plusieurs apps doivent partager les mêmes outils, ou pour brancher un agent sur un écosystème de serveurs existants sans recâbler.
- Pour un seul agent maison avec 2-3 outils, le [[tool-use|function calling]] direct reste plus simple — MCP ajoute une couche serveur à faire tourner.
- **Vérifier la version de spec** avant de promettre une intégration : `2026-07-28` (stateless, extensions) et `2025-11-25` (stateful, sessions) ne se comportent pas pareil côté déploiement. C'est la première question à poser sur un serveur tiers.
- Côté clients : Claude Desktop/Code, un nombre croissant de frameworks d'agents ([[Dev/Services/LangGraph|LangGraph]], [[Dev/Services/PydanticAI|PydanticAI]]), et les agents auto-hébergés prêts à l'emploi ([[Dev/Services/OpenClaw|OpenClaw]], [[Dev/Services/Hermes Agent|Hermes Agent]]) consomment des serveurs MCP — pour ces derniers, MCP remplace les intégrations ad hoc, une par service.
- Côté serveurs : [[Dev/Services/fastmcp|fastmcp]] construit serveurs et clients MCP en Python (décorateurs, génération depuis OpenAPI/FastAPI) ; [[Dev/Services/mcpjam|mcpjam]] les **inspecte et débogue** (« Postman pour MCP »).
- Traiter un serveur tiers comme du **code non fiable** : permissions minimales, validation des entrées, garde-fous sur les outils sensibles (cf. [[Reliability patterns]]).

## Approches voisines & alternatives

- [[tool-use]] — MCP **standardise** l'exposition des outils que le function calling appelle.
- [[a2a-protocol]] — le pendant **horizontal** : MCP relie un agent à ses outils, A2A relie des agents entre eux. Complémentaires, un même agent expose souvent les deux.
- [[Agent skills]] — MCP fournit les **outils**, un skill fournit la **méthode** pour s'en servir.
- [[Tool use patterns]] — les patrons d'appel d'outils s'appliquent aux outils servis par MCP.
- [[agent-loops]] — l'extension Tasks règle un problème précis de la boucle d'agent : les travaux qui dépassent la durée d'un appel.
- [[Agent memory]] — les *resources* MCP sont une voie d'alimentation du contexte/mémoire.
- [[Context engineering]] — MCP est un canal d'assemblage du contexte (resources, prompts) ; `ttlMs` en devient un paramètre de coût.
- [[Prompt injection]] — la surface d'attaque que l'authentification ne couvre pas.
- Alternative : **function calling câblé en dur** (SDK fournisseur) — moins de pièces mobiles sur un périmètre fermé, mais pas d'interopérabilité.

## Pour aller plus loin

- Anthropic (2024) — *Introducing the Model Context Protocol*.
- Spécification : modelcontextprotocol.io — révision courante **2026-07-28**, précédente 2025-11-25.
- Blog MCP (28/07/2026) — *The 2026-07-28 Specification* (cœur stateless, MRTR, extensions, autorisation).
- Agentic AI Foundation (Linux Foundation) — gouvernance et processus SEP (Specification Enhancement Proposal).
