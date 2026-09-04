---
role: brique
nom: Semantic Kernel
alias: [semantic-kernel, SK]
pitch: "SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: "C#, Python, Java"
alternatives: ["[[LangChain]]"]
complements: []
tags: [llm, agents, tool-use]
url_docs: https://learn.microsoft.com/semantic-kernel/
url_repo: https://github.com/microsoft/semantic-kernel
---

# Semantic Kernel

<!-- AUTO:BANDEAU:START -->
> SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C#, Python, Java | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

SDK d'orchestration LLM de **Microsoft**, pensé pour intégrer l'IA dans des applications
**d'entreprise** existantes plutôt que pour prototyper en notebook. Son modèle : un *kernel*
central auquel on greffe des **plugins** — fonctions natives ou prompts — que le LLM appelle par
**function calling**, plus des **planificateurs** qui décomposent un objectif en étapes. Sa
particularité est la **parité multi-langage** : mêmes concepts en C#/.NET, Python et Java, ce qui
en fait le choix naturel d'un écosystème .NET ou JVM. Microsoft a depuis annoncé que *« Semantic
Kernel is now Microsoft Agent Framework »* — **MAF**, fusion de Semantic Kernel et de
[[AutoGen]], est positionné comme le successeur prêt pour la production (v1.0, APIs stables,
support long terme). Semantic Kernel reste activement maintenu.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Application .NET ou Java où l'on veut une intégration LLM idiomatique, et non un pont vers du Python | Nouveau projet agentique sans contrainte d'historique : partir directement sur Microsoft Agent Framework, le successeur — et vérifier le guide de migration avant d'investir ici |
| Contexte entreprise : besoin de plugins, de function calling, et d'un éditeur unique avec support | Compter sur les « planners » : ces abstractions ont été refondues plusieurs fois et sont historiquement instables — privilégier le function calling explicite |
| Réutiliser des compétences d'un langage à l'autre : même architecture côté C#, Python et Java | S'appuyer sur les exemples : documentation et échantillons sont parfois en retard sur l'une des trois implémentations, la parité C#/Python/Java n'étant pas toujours synchrone |

## Mise en œuvre

- Installation — bibliothèque importée dans l'application : NuGet pour .NET, `pip` pour Python, Maven pour Java
- Point d'entrée — le *kernel*, ses plugins (fonctions natives ou prompts) et le function calling ; planificateurs en option
- Prérequis — .NET, Python ou Java, et un accès LLM (Azure OpenAI, OpenAI, etc.)
- Exécution — en bibliothèque dans l'application hôte, aucune infra propre ; le scaling est celui de l'hôte, mono-nœud par défaut
- Coût — gratuit, MIT ; la dépense réelle est celle des LLM sous-jacents, pas du SDK

## Écosystème

### Alternatives

- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.

## Ressources

- Documentation — https://learn.microsoft.com/semantic-kernel/
- Dépôt — https://github.com/microsoft/semantic-kernel

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Tool use patterns]] — patrons d'appel d'outils, dont le function calling des plugins
