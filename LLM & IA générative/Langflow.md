---
role: brique
nom: Langflow
alias: [langflow, langflow-ai]
pitch: "Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud."
categorie: llm/low-code
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dify]]", "[[Flowise]]"]
complements: []
tags: [llm, low-code, agents, rag]
url_docs: https://docs.langflow.org/
url_repo: https://github.com/langflow-ai/langflow
---

# Langflow

<!-- AUTO:BANDEAU:START -->
> Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Constructeur **visuel low-code** d'applications agentiques et RAG : on relie des composants
— modèles, prompts, vector stores, outils, boucles d'agent — sur un **canvas
drag-and-drop**, sans écrire le code de plomberie. Chaque flux s'expose ensuite en
**endpoint REST** ou s'**exporte en code Python**, ce qui évite l'effet boîte noire — même
si une app de production gagne souvent à être réécrite proprement plutôt que générée.
Backend Python, frontend TypeScript/React. Projet de la société Langflow, passée chez
DataStax, rachetée par IBM en 2025 ; il reste ouvert et intégré à l'écosystème watsonx. Le
visuel masque la complexité jusqu'à un certain point : au-delà, les flux deviennent
illisibles et il faut basculer en code.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototyper vite un agent ou un pipeline RAG en visuel, sans démarrer un projet de code | Logique d'orchestration complexe, stateful, versionnée en code → [[LangGraph]], [[LangChain]] |
| Faire collaborer profils techniques et non techniques sur la même chaîne : le canvas sert de langage commun | Plateforme LLMOps complète — gestion de modèles, observabilité, équipes — plutôt qu'un éditeur de flux → [[Dify]] |
| Partir du visuel puis récupérer le code Python pour industrialiser dans une app classique | Simple appel LLM ou extraction structurée dans du code → [[Instructor]], [[PydanticAI]] |
| Exposer un flux en API pour le brancher à un front ou à un autre service | Composants renommés ou déplacés d'une version à l'autre : épingler la version, se méfier des tutoriels datés |

## Mise en œuvre

- Installation — `pip`/`uv` ou Docker pour le self-host, Langflow Desktop en local, déployable sur les grands clouds
- Point d'entrée — canvas web ; chaque flux s'expose en endpoint REST ou s'exporte en code Python
- Prérequis — Python pour le backend ; les composants viennent de l'écosystème [[LangChain]]
- Exécution — self-hébergé, en desktop, ou via l'offre managée côté DataStax/IBM ; mono-nœud
- Coût — gratuit sous MIT ; le coût réel est dominé par les appels LLM des flux, pas par l'outil

## Écosystème

### Alternatives

- [[Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.
- [[Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.

## Ressources

- Documentation — https://docs.langflow.org/
- Dépôt — https://github.com/langflow-ai/langflow

## Voir aussi

- [[Agent patterns]] — la notion : les formes d'agent que ses composants assemblent
- [[Advanced RAG]] — la notion : ce que ses pipelines de récupération mettent en œuvre
- [[Context engineering]] — la notion du dossier
- Routage multi-fournisseurs possible via [[LiteLLM]] ou [[OpenRouter]]
- [[LLM & IA générative]] — le hub du domaine
