---
galaxie: wiki
type: concept
nom: Tool use patterns
alias: [patrons d'appel d'outils, tool use patterns, function calling patterns]
categorie: concept/llm
domaines: [ai-eng]
tags: [tool-use, agents, llm]
---

# Tool use patterns

## Aperçu

- Comment un LLM **agit sur le monde** : il choisit une fonction (outil) et produit ses arguments, un exécuteur l'appelle, le résultat revient dans le contexte.
- C'est l'étape « action » de la boucle d'agent ([[agent-loops]]) ; sans outils, un LLM ne fait que générer du texte.

## Concepts clés

### Function calling
- Chaque outil est déclaré par un **schéma** (nom, description, paramètres typés). Le modèle émet un appel **structuré** (JSON conforme au schéma) — d'où le lien fort avec les [[Structured outputs|sorties structurées]].

### Sélection d'outil
- Le bon choix dépend de **descriptions claires** et d'un nombre d'outils raisonnable. Trop d'outils, ou des frontières qui se recouvrent → confusion et mauvais appels.

### Robustesse : erreurs & retries
- Arguments invalides, outil qui échoue, résultat inattendu → **valider les arguments**, borner les retries, réinjecter l'erreur pour que le modèle se corrige.

### Parallélisme
- Plusieurs appels indépendants dans un même tour (*parallel tool calls*) réduisent la latence ; à n'utiliser que si les appels ne dépendent pas l'un de l'autre.

### Garde-fous
- Les outils à **effet de bord** (écriture, paiement, mail) exigent validation et permissions — un outil mal cadré transforme une hallucination en action réelle.

## Les maths, simplement

- Sélection d'outil vue comme un argmax : $\hat{a} = \arg\max_{a \in \mathcal{A}} p_\theta\big(a \mid \text{contexte}, \text{schémas}\big)$, où $\mathcal{A}$ est l'ensemble des outils disponibles.
- La qualité chute quand $|\mathcal{A}|$ grandit ou que les descriptions se recouvrent — réduire et désambiguïser le catalogue améliore directement le taux de bon appel.

## En pratique

- **Peu d'outils, bien décrits**, aux frontières nettes ; un schéma de paramètres strict (types, énumérations) vaut mieux qu'une description floue.
- Valider les arguments avant exécution — [[Dev/Services/Instructor|Instructor]] / [[Dev/Services/PydanticAI|PydanticAI]] pour des sorties typées et validées.
- Isoler les outils dangereux (bac à sable, permissions) ; tout effet de bord passe par un garde-fou.
- Le **MCP** standardise l'exposition d'outils à un agent (protocole client-serveur) — cf. [[mcp-protocol]].
- Outillage : [[Dev/Services/LangGraph|LangGraph]], [[Dev/Services/LangChain|LangChain]], [[Dev/Services/CrewAI|CrewAI]] gèrent la déclaration et la boucle d'appel d'outils.

## Approches voisines & alternatives

- [[agent-loops]] — l'appel d'outil est l'action de la boucle.
- [[Agent patterns]] — ReAct repose entièrement sur l'usage d'outils.
- [[Multi-agent systems]] — un agent peut être exposé comme un outil à un autre.
- [[RAG]] — la récupération est souvent branchée comme un outil de l'agent (agentic RAG, cf. [[Advanced RAG]]).
- [[tool-use]] — le mécanisme (function calling) que ces patrons exploitent.
- [[mcp-protocol]] — standardise la mise à disposition des outils (client-serveur).
- [[Reliability patterns]] — fiabiliser les appels d'outils (retries, garde-fous, effets de bord).
- [[Structured outputs|Sorties structurées sans exécution]] — quand on veut seulement un objet typé du modèle, sans action sur le monde.

## Pour aller plus loin

- Schick et al. (2023) — *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic — documentation *tool use* / function calling.
