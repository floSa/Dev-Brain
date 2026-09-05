---
role: brique
nom: Flowise
alias: [flowise, flowiseai]
pitch: "Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud."
categorie: llm/low-code
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Langflow]]", "[[Dify]]"]
complements: []
tags: [llm, low-code, agents, rag]
url_docs: https://docs.flowiseai.com/
url_repo: https://github.com/FlowiseAI/Flowise
---

# Flowise

<!-- AUTO:BANDEAU:START -->
> Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Constructeur **visuel low-code** d'agents, de chatbots et de chaînes LLM : on glisse-dépose
des **nœuds** — modèles, vector stores, outils, mémoire — sur un **canvas**, et le flux
s'expose ensuite en **API** ou en widget de chat. Écrit en TypeScript/Node.js et bâti sur
**LangChain.js**, c'est le seul constructeur de sa catégorie à vivre dans l'écosystème
JavaScript, les autres étant en Python. Cette filiation est aussi sa dépendance : les
ruptures d'API de LangChain.js le traversent, et son périmètre fonctionnel reste en retrait
de la version Python. Comme tout constructeur visuel, les flux non triviaux y deviennent
vite difficiles à maintenir et à versionner.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototyper visuellement un chatbot ou un agent RAG et l'exposer en API ou en widget en quelques minutes | Stack Python où l'on veut exporter le flux en code → [[Langflow]] |
| Rester dans l'écosystème Node.js/JavaScript : intégration front, déploiement serverless JS | Besoin d'une plateforme complète — gestion des modèles, observabilité, datasets → [[Dify]] |
| Donner un outil no-code ou low-code à des profils non-Python pour itérer sur des flux LLM | Orchestration stateful complexe, versionnée en code → [[LangGraph]] |
| | Le partage entre l'édition Community et l'édition Enterprise est un préalable : SSO, RBAC et espaces de travail ne sont pas dans le cœur libre |

## Mise en œuvre

- Installation — npm ou Docker pour le self-host, ou Flowise Cloud pour le managé
- Point d'entrée — canvas web de nœuds ; le flux se publie en API REST ou en widget de chat
- Prérequis — Node.js ; la logique repose sur LangChain.js, dont il suit les versions
- Exécution — self-hébergé ou Flowise Cloud ; mono-nœud par défaut
- Coût — cœur Apache-2.0 gratuit, édition Enterprise payante (SSO, RBAC, espaces de travail) — un open-core de fait ; le coût réel vient des appels LLM des flux

## Écosystème

### Alternatives

- [[Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.

## Ressources

- Documentation — https://docs.flowiseai.com/
- Dépôt — https://github.com/FlowiseAI/Flowise

## Voir aussi

- [[LangChain]] — l'équivalent Python de la bibliothèque sur laquelle il est bâti
- [[Agent patterns]] — la notion : les formes d'agent que ses nœuds assemblent
- [[Advanced RAG]] — la notion : ce que ses flux de récupération mettent en œuvre
- [[Context engineering]] — la notion du dossier
- Routage multi-fournisseurs possible via [[OpenRouter]] ou [[LiteLLM]]
- [[LLM & IA générative]] — le hub du domaine
