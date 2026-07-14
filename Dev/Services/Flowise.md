---
galaxie: dev
type: service
nom: Flowise
alias: [flowise, flowiseai]
pitch: "Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/Langflow|Langflow]]", "[[Dev/Services/Dify|Dify]]"]
remplace_par: []
status: actif
tags: [llm, low-code, agents, rag]
url_docs: https://docs.flowiseai.com/
url_repo: https://github.com/FlowiseAI/Flowise
---

# Flowise

## Pourquoi

Constructeur **visuel low-code** d'agents, de chatbots et de chaînes LLM : on glisse-dépose des **nœuds** (modèles, vector stores, outils, mémoire) sur un **canvas** pour assembler une app, exposée ensuite en **API** ou en widget de chat. Écrit en **TypeScript/Node.js** et **bâti sur LangChain.js** (l'équivalent JS de [[Dev/Services/LangChain|LangChain]]), c'est le pendant côté écosystème **JavaScript** des builders Python. Cœur **Apache-2.0** ; une **édition Enterprise** commerciale ajoute SSO, RBAC et fonctions d'équipe.

## Quand l'utiliser

- Prototyper **visuellement** un chatbot ou un agent RAG et l'exposer en **API/widget** en quelques minutes.
- Rester dans l'écosystème **Node.js/JavaScript** (intégration front, déploiement serverless JS).
- Donner un **outil no/low-code** à des profils non-Python pour itérer sur des flux LLM.

## Quand NE PAS l'utiliser

- Stack **Python** où l'on veut exporter le flux en code → [[Dev/Services/Langflow|Langflow]].
- Besoin d'une **plateforme** complète (gestion modèles, observabilité, datasets) → [[Dev/Services/Dify|Dify]].
- Orchestration **stateful complexe** versionnée en code → [[Dev/Services/LangGraph|LangGraph]].

## Déploiement & coût

- Cœur **Apache-2.0**, gratuit : **self-host** (npm/Docker) ou **Flowise Cloud** managé (`hosted: both`).
- **Édition Enterprise** payante pour SSO, RBAC, espaces de travail — modèle open-core de fait.
- Coût réel dominé par les appels **LLM** des flux ; déploiement single-node par défaut.

## Pièges

- Bien distinguer ce qui est **Apache-2.0 (Community)** de ce qui relève de l'**Enterprise** commerciale.
- Comme tout builder visuel : les flux **non triviaux** deviennent vite difficiles à maintenir et à versionner.
- Dépendance à **LangChain.js** : suivre ses ruptures d'API et l'écart de fonctionnalités avec la version Python.

## Alternatives

- [[Dev/Services/Langflow|Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Dev/Services/Dify|Dify]] — Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.

## Liens

- Même famille de **builders visuels** que [[Dev/Services/Langflow|Langflow]] et [[Dev/Services/Dify|Dify]] ; côté **JS**, contrairement aux deux (Python).
- Bâti sur **LangChain.js** (cf. [[Dev/Services/LangChain|LangChain]]).
- Peut consommer de multiples fournisseurs, dont via [[Dev/Services/OpenRouter|OpenRouter]] / [[Dev/Services/LiteLLM|LiteLLM]].
- Concepts : [[Agent patterns]], [[Advanced RAG]], [[Context engineering]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.flowiseai.com/
