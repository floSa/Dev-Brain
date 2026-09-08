---
role: brique
nom: Dify
alias: [dify, dify.ai, langgenius-dify]
pitch: "Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud."
categorie: llm/low-code
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Langflow]]", "[[Flowise]]"]
complements: []
tags: [llm, low-code, agents, rag]
url_docs: https://docs.dify.ai/
url_repo: https://github.com/langgenius/dify
---

# Dify

<!-- AUTO:BANDEAU:START -->
> Plateforme LLMOps low-code (source-available, LangGenius) — interface visuelle qui combine workflows agentiques, pipelines RAG, gestion de modèles et observabilité, du prototype à la production ; self-host Docker ou Dify Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | source-available | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-01 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme LLMOps low-code de LangGenius, plus large qu'un simple constructeur de flux : une
console visuelle qui réunit **workflows agentiques**, **pipelines RAG**, gestion
multi-fournisseurs des modèles, datasets, **observabilité** et exposition en API — du
prototype à la production dans un seul outil. Backend Python, frontend Next.js/TypeScript. La
contrepartie de cette couverture est double : la stack est lourde — API, worker, sandbox,
base, plusieurs conteneurs à faire tourner —, et le verrouillage guette dès que toute la
logique métier vit dans la console plutôt que dans du code portable.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir une plateforme et pas seulement un éditeur de flux : RAG, agents, gestion des modèles, logs et monitoring au même endroit | Un simple canvas de flux exportable en code suffit → [[Langflow]], [[Flowise]] |
| Livrer une app LLM self-host clé en main, avec console d'admin, datasets et suivi d'usage | L'orchestration doit être fine, versionnée en code → [[LangGraph]], [[LangChain]] |
| Outiller une petite équipe produit ou ops autour d'un backend LLM commun, sans tout coder | La clause anti-multi-tenant et l'obligation d'afficher le logo bloquent l'usage produit visé : il faut alors une licence Apache ou MIT pure |
| | Simple POC : plusieurs conteneurs à opérer pour un flux, ce n'est pas le choix le plus léger |

## Mise en œuvre

- Installation — Docker Compose pour le self-host, ou Dify Cloud pour le managé
- Point d'entrée — console web : workflows, datasets, gestion des modèles, logs ; chaque app s'expose en API
- Prérequis — plusieurs conteneurs (API, worker, sandbox, base de données)
- Exécution — self-hébergé ou Dify Cloud ; mono-nœud par défaut, la montée en charge se paie en effort d'infra
- Coût — gratuit à l'usage, mais la licence — une Apache 2.0 **modifiée** — exige un accord commercial pour revendre un service multi-tenant ou retirer le logo et le copyright de la console ; le coût réel est dominé par les appels LLM

## Écosystème

### Alternatives

- [[Langflow]] — Constructeur visuel low-code d'applications agentiques et RAG (MIT, Langflow/IBM-DataStax) — canvas drag-and-drop de composants connectés, exposable en API ou exportable en code Python ; self-host ou Langflow Desktop/cloud.
- [[Flowise]] — Constructeur visuel d'agents et de chaînes LLM (Apache-2.0, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; self-host ou Flowise Cloud.

## Ressources

- Documentation — https://docs.dify.ai/
- Dépôt — https://github.com/langgenius/dify

## Voir aussi

- [[Agent patterns]] — la notion : les formes d'agent que ses workflows assemblent
- [[Advanced RAG]] — la notion : ce que ses pipelines de récupération mettent en œuvre
- [[Context engineering]] — la notion du dossier
- Routage multi-fournisseurs possible via [[LiteLLM]] ou [[OpenRouter]]
- [[LLM & IA générative]] — le hub du domaine
