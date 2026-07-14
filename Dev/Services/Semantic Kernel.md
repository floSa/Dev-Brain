---
galaxie: dev
type: service
nom: Semantic Kernel
alias: [semantic-kernel, SK]
pitch: "SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: "C#, Python, Java"
scaling: single-node
alternatives: ["[[Dev/Services/LangChain|LangChain]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use]
url_docs: https://learn.microsoft.com/semantic-kernel/
url_repo: https://github.com/microsoft/semantic-kernel
---

# Semantic Kernel

## Pourquoi

SDK d'orchestration LLM de **Microsoft**, pensé pour intégrer l'IA dans des applications **d'entreprise** existantes plutôt que pour prototyper en notebook. Son modèle : un *kernel* central auquel on greffe des **plugins** (fonctions natives ou prompts) que le LLM appelle par **function calling**, plus des **planificateurs** qui décomposent un objectif en étapes. Particularité notable : la **parité multi-langage** — mêmes concepts en **C#/.NET**, **Python** et **Java**, ce qui en fait le choix naturel d'un écosystème .NET/JVM. Licence **MIT**.

⚠️ **Statut 2026** : Microsoft a annoncé que *« Semantic Kernel is now Microsoft Agent Framework »*. **Microsoft Agent Framework (MAF)** — qui fusionne Semantic Kernel et [[Dev/Services/AutoGen|AutoGen]] — est positionné comme le **successeur prêt pour la production** (v1.0, APIs stables, support long terme). Semantic Kernel reste activement maintenu, mais tout **nouveau projet** devrait évaluer MAF en premier.

## Quand l'utiliser

- Application **.NET / Java** où l'on veut une intégration LLM idiomatique (et non un pont vers du Python).
- Contexte **entreprise** : besoin de plugins, function calling, et d'un éditeur unique (Microsoft) avec support.
- Réutiliser des compétences across-langage : même architecture côté C#, Python et Java.

## Quand NE PAS l'utiliser

- **Nouveau** projet agentique sans contrainte d'historique : partir directement sur **Microsoft Agent Framework**, le successeur.
- Écosystème **Python pur** avec un large besoin d'intégrations tierces → [[Dev/Services/LangChain|LangChain]].
- Orchestration multi-agents avec contrôle explicite du flux → [[Dev/Services/AutoGen|AutoGen]] / [[Dev/Services/CrewAI|CrewAI]] / [[Dev/Services/LangGraph|LangGraph]].

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée dans l'app (NuGet / `pip` / Maven), aucune infra propre.
- Coût réel dominé par les appels aux **LLM** sous-jacents (Azure OpenAI, OpenAI, etc.), pas par le SDK.
- Scaling = celui de l'application hôte (single-node par défaut).

## Pièges

- **Risque de successeur** : bâtir du neuf sur Semantic Kernel alors que Microsoft pousse Agent Framework — vérifier le guide de migration avant d'investir.
- **Abstractions « planner »** historiquement instables (plusieurs refontes) ; privilégier le function calling explicite.
- Documentation et exemples parfois **en retard** sur l'une des trois implémentations (la parité C#/Python/Java n'est pas toujours synchrone).

## Alternatives

- [[Dev/Services/LangChain|LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.

## Liens

- **Successeur** : Microsoft Agent Framework (MAF) — fusion de Semantic Kernel et [[Dev/Services/AutoGen|AutoGen]] ; nouveau socle Microsoft pour agents et workflows multi-agents.
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://learn.microsoft.com/semantic-kernel/
