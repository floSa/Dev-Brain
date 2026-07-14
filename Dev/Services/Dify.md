---
galaxie: dev
type: service
nom: Dify
alias: [dify, dify.ai, langgenius-dify]
pitch: "Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud."
categorie: llm/framework
licence_type: source-available
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Langflow|Langflow]]", "[[Dev/Services/Flowise|Flowise]]"]
remplace_par: []
status: actif
tags: [llm, low-code, agents, rag]
url_docs: https://docs.dify.ai/
url_repo: https://github.com/langgenius/dify
---

# Dify

## Pourquoi

**Plateforme LLMOps low-code** (éditeur **LangGenius**), plus large qu'un simple builder de flux : une interface visuelle qui combine **workflows agentiques**, **pipelines RAG**, **gestion de modèles** multi-fournisseurs, **observabilité** et exposition en API, pour aller du **prototype à la production** dans un seul outil. **Backend Python**, frontend Next.js/TypeScript. Licence **« Dify Open Source License »** : Apache 2.0 **modifiée** avec conditions additionnelles — interdiction d'en faire un **service multi-tenant** managé sans licence commerciale, et interdiction de **retirer le logo/copyright** de la console. Donc *source-available*, pas open-source OSI au sens strict.

## Quand l'utiliser

- Vouloir **une plateforme** (et pas seulement un éditeur de flux) : RAG, agents, gestion des modèles, logs et monitoring au même endroit.
- Livrer une app LLM **self-host** clé en main avec console d'admin, datasets et suivi d'usage.
- Outiller une **petite équipe** produit/ops autour d'un backend LLM commun, sans tout coder.

## Quand NE PAS l'utiliser

- Besoin d'un simple **canvas de flux** exportable en code → [[Dev/Services/Langflow|Langflow]] (MIT) / [[Dev/Services/Flowise|Flowise]].
- Projet où la **licence restrictive** (pas de multi-tenant, logo imposé) pose problème → préférer une option MIT/Apache pure.
- Orchestration **fine en code** versionnée → [[Dev/Services/LangGraph|LangGraph]] / [[Dev/Services/LangChain|LangChain]].

## Déploiement & coût

- **Self-host** via Docker Compose (gratuit), ou **Dify Cloud** managé (offre SaaS de l'éditeur) — d'où `hosted: both`.
- Le cœur est *source-available* : usage commercial possible **sauf** revente en service multi-tenant et retrait du logo, qui exigent une **licence commerciale**.
- Coût réel dominé par les appels **LLM** ; le déploiement Docker reste single-node par défaut (scalable au prix d'efforts d'infra).

## Pièges

- **Licence à lire** avant tout usage produit : la clause anti-multi-tenant et l'obligation de logo surprennent ceux qui croient à de l'Apache pur.
- Stack relativement **lourde** (plusieurs conteneurs : API, worker, sandbox, base) — pas le choix le plus léger pour un simple POC.
- Couvre beaucoup de terrain : risque de **verrouillage** dans la plateforme si toute la logique vit dans Dify plutôt que dans du code portable.

## Alternatives

- [[Dev/Services/Langflow|Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Dev/Services/Flowise|Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.

## Liens

- Même famille de **builders LLM low-code** que [[Dev/Services/Langflow|Langflow]] et [[Dev/Services/Flowise|Flowise]], en plus *plateforme* (LLMOps).
- Gère nativement de multiples fournisseurs ; peut aussi router via [[Dev/Services/LiteLLM|LiteLLM]] / [[Dev/Services/OpenRouter|OpenRouter]].
- Concepts : [[Agent patterns]], [[Advanced RAG]], [[Context engineering]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.dify.ai/
