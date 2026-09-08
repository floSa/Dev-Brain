---
role: brique
nom: OpenAI Agents SDK
alias: [openai-agents-sdk, openai-agents, agents-sdk, swarm]
pitch: "SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: "Python, TypeScript"
alternatives: ["[[CrewAI]]", "[[AutoGen]]", "[[Agno]]", "[[smolagents]]", "[[Letta]]"]
complements: []
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://openai.github.io/openai-agents-python/
url_repo: https://github.com/openai/openai-agents-python
---

# OpenAI Agents SDK

<!-- AUTO:BANDEAU:START -->
> SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python, TypeScript | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

SDK d'agents **léger** d'OpenAI, qui reprend et pérennise **Swarm**, son framework
expérimental de 2024. Son pari est la **minimalité** : peu de primitives, mais suffisantes — un
**Agent** (LLM + instructions + outils), des **handoffs** par lesquels un agent passe la main à
un autre, base du multi-agents, des **guardrails** de validation en entrée et en sortie, des
**sessions** à historique persistant, et un **tracing intégré** pour visualiser et déboguer les
exécutions. Les fonctions Python deviennent des outils par introspection, schémas générés et
validés par Pydantic. **Agnostique du fournisseur** : OpenAI par défaut, mais 100+ modèles via
l'API Chat Completions ou [[LiteLLM]]. Disponible en Python et en TypeScript.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un framework d'agent minimal et explicite, sans abstractions lourdes à apprendre | Le **tracing part par défaut vers le tableau de bord OpenAI** — vérifier la conformité données, et le désactiver ou le rediriger vers un processor tiers pour rester self-contained |
| Schémas multi-agents par handoffs (triage → spécialistes) avec garde-fous et traçabilité | Minimalisme assumé : au-delà des primitives, la robustesse — retries, fallback, timeouts — reste entièrement à câbler |
| Écosystème OpenAI, sans exclusivité, et besoin d'un tracing prêt à l'emploi | Projet à figer : sorti en 2025, l'API est encore mouvante — épingler les versions |
| | **Mémoire persistante** longue durée comme primitive centrale → [[Letta]] |

## Mise en œuvre

- Installation — SDK `pip` / `uv` pour Python, npm pour TypeScript, importé dans l'application
- Point d'entrée — API : Agent, handoffs, guardrails, sessions ; les fonctions Python deviennent des outils par introspection
- Prérequis — Python ou TypeScript, et un accès LLM (OpenAI par défaut, ou tout fournisseur via Chat Completions / LiteLLM)
- Exécution — en bibliothèque dans l'application hôte, aucune infra propre ; le tracing est un service externe, désactivable
- Coût — gratuit, MIT ; la dépense réelle est celle des LLM, et les handoffs multiplient les tours — borner

## Écosystème

### Alternatives

- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

## Ressources

- Documentation — https://openai.github.io/openai-agents-python/
- Dépôt — https://github.com/openai/openai-agents-python (successeur de `openai/swarm`, expérimental)

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
