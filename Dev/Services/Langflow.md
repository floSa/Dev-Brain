---
galaxie: dev
type: service
nom: Langflow
alias: [langflow, langflow-ai]
pitch: "Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Dify|Dify]]", "[[Dev/Services/Flowise|Flowise]]"]
remplace_par: []
status: actif
tags: [llm, low-code, agents, rag]
url_docs: https://docs.langflow.org/
url_repo: https://github.com/langflow-ai/langflow
---

# Langflow

## Pourquoi

Constructeur **visuel low-code** d'applications LLM **agentiques et RAG** : on assemble des composants (modèles, prompts, vector stores, outils, boucles d'agent) en les reliant sur un **canvas drag-and-drop**, sans écrire le code de plomberie. Chaque flux est ensuite **exposable en API** (endpoint REST) ou **exportable en code Python**, ce qui évite l'effet boîte noire. **Backend Python**, frontend TypeScript/React, licence **MIT**. Projet de la société **Langflow**, passée chez **DataStax** (rachetée par **IBM** en 2025) ; reste open-source et intégré à l'écosystème watsonx.

## Quand l'utiliser

- **Prototyper vite** un agent ou un pipeline RAG en visuel, sans démarrer un projet de code.
- Faire **collaborer** profils techniques et non-techniques sur la même chaîne (le canvas sert de langage commun).
- Partir du visuel puis **récupérer le code Python** pour industrialiser dans une app classique.
- Exposer un flux en **API** pour le brancher à un front ou un autre service.

## Quand NE PAS l'utiliser

- Logique d'orchestration **complexe, stateful, versionnée en code** → [[Dev/Services/LangGraph|LangGraph]] / [[Dev/Services/LangChain|LangChain]] directement.
- Plateforme **LLMOps complète** (gestion de modèles, observabilité, équipes) plutôt qu'un éditeur de flux → [[Dev/Services/Dify|Dify]].
- Simple **appel LLM** ou extraction structurée dans du code → [[Dev/Services/Instructor|Instructor]] / [[Dev/Services/PydanticAI|PydanticAI]].

## Déploiement & coût

- Open-source (MIT), gratuit : **self-host** Docker/pip ou **Langflow Desktop**, déployable sur les grands clouds (`hosted: both`).
- Une offre **managée** existe côté DataStax/IBM (canvas hébergé) pour qui ne veut pas opérer l'infra.
- Coût réel dominé par les appels **LLM** des flux, pas par l'outil.

## Pièges

- Le visuel **masque la complexité** jusqu'à un certain point : les flux non triviaux deviennent vite illisibles — basculer en code quand ça dépasse.
- API en **évolution rapide** (composants renommés/déplacés) : épingler la version, attention aux tutoriels datés.
- L'**export Python** facilite la sortie, mais une app de prod gagne souvent à être réécrite proprement plutôt que générée.

## Alternatives

- [[Dev/Services/Dify|Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.
- [[Dev/Services/Flowise|Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.

## Liens

- Même famille de **builders visuels** que [[Dev/Services/Flowise|Flowise]] (Node.js) et [[Dev/Services/Dify|Dify]] (plateforme).
- S'appuie sur l'écosystème [[Dev/Services/LangChain|LangChain]] (composants Python) ; flux exportables en code.
- Peut router ses appels multi-fournisseurs via [[Dev/Services/LiteLLM|LiteLLM]] ou [[Dev/Services/OpenRouter|OpenRouter]].
- Concepts : [[Agent patterns]], [[Advanced RAG]], [[Context engineering]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.langflow.org/
