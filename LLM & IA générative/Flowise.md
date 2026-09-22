---
role: brique
nom: Flowise
alias: [flowise, flowiseai]
pitch: "Constructeur visuel d'agents et de chaînes LLM (Apache-2.0 hors dossier enterprise, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; dépôt archivé depuis le 2026-08-13, sans correctifs à attendre."
categorie: llm/low-code
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: deprecated
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
> Constructeur visuel d'agents et de chaînes LLM (Apache-2.0 hors dossier enterprise, FlowiseAI, bâti sur LangChain.js) — drag-and-drop de nœuds sur un canvas pour assembler chatbots, RAG et agents, exposés en API ; dépôt archivé depuis le 2026-08-13, sans correctifs à attendre.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme TypeScript | open-core | self-hébergé ou managé · mono-nœud | deprecated | dépôt archivé · 2026-08-13 |
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

**État du projet : archivé.** Le dépôt est en lecture seule depuis le **2026-08-13** (gel du code le 2026-07-29, fin de la présence de l'équipe sur GitHub et Discord le 2026-08-31) ; le README renvoie à une annonce « Future of Flowise » qui invite à forker ou migrer. Dernière version : **3.1.4** du 2026-07-29, 55 490 étoiles constatées le 2026-09-30. Workday avait annoncé le rachat de Flowise en août 2025 ; l'annonce d'archivage ne lie pas les deux faits et ne dit rien de Flowise Cloud. Des avis de sécurité critiques (évasion de bac à sable, exécution de code) datent du 2026-07-29, et des avis élevés publiés fin août et en septembre 2026 n'ont plus de mainteneur officiel pour les corriger. **Successeurs dans le brain : [[Langflow]] et [[Dify]].**

**Licence.** Le cœur est sous Apache-2.0, mais le dossier `packages/server/src/enterprise` est sous licence commerciale : la production y exige un abonnement Enterprise, et il n'est ni redistribuable ni revendable. SSO (Azure, Google, Auth0, OIDC), espaces de travail, organisations et rôles n'existent que dans l'offre Enterprise ou Cloud. Une ESN peut déployer le cœur Apache-2.0 chez un client, le forker et changer la marque ; elle ne peut pas reprendre le dossier enterprise.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Reprendre un déploiement existant en attendant une migration, ou forker le cœur Apache-2.0 en assumant seul la maintenance et les correctifs de sécurité | Tout nouveau projet : le dépôt est archivé, plus aucun correctif officiel → [[Langflow]] ou [[Dify]] |
| Stack Python où l'on veut exporter le flux en code → [[Langflow]] |
| Rester dans l'écosystème Node.js/JavaScript : intégration front, déploiement serverless JS | Besoin d'une plateforme complète — gestion des modèles, observabilité, datasets → [[Dify]] |
| Donner un outil no-code ou low-code à des profils non-Python pour itérer sur des flux LLM | Orchestration stateful complexe, versionnée en code → [[LangGraph]] |
| | Le partage entre l'édition Community et l'édition Enterprise est un préalable : SSO, RBAC et espaces de travail ne sont pas dans le cœur libre |

## Mise en œuvre

- Installation — npm ou Docker pour le self-host, ou Flowise Cloud pour le managé
- Point d'entrée — canvas web de nœuds ; le flux se publie en API REST ou en widget de chat
- Prérequis — Node.js ; la logique repose sur LangChain.js, dont il suit les versions ; SQLite par défaut, PostgreSQL en option, Redis seulement en mode file d'attente
- Exécution — self-hébergé ou Flowise Cloud ; mono-nœud par défaut
- Coût — cœur Apache-2.0 gratuit, dossier enterprise sous licence commerciale (SSO, RBAC, espaces de travail) — un open-core ; le coût réel vient des appels LLM des flux, puis de la dette de sécurité d'un dépôt sans mainteneur

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
- [[Comparatif - Plateformes LLM auto-hébergées]] — le comparatif qui situe les interfaces de chat, le moteur RAG et les constructeurs visuels
- Routage multi-fournisseurs possible via [[OpenRouter]] ou [[LiteLLM]]
- [[LLM & IA générative]] — le hub du domaine
