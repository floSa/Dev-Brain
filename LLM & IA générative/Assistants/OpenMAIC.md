---
role: brique
nom: OpenMAIC
alias: [openmaic, maic, open-multi-agent-interactive-classroom]
pitch: "Application de classe virtuelle multi-agents (MIT, THU-MAIC / Tsinghua) — transforme un sujet ou un document en cours interactif : slides narrées, quiz, simulations HTML, professeur et camarades IA qui parlent et dessinent au tableau ; export PPTX/HTML, hébergé ou auto-déployé."
categorie: llm/assistant
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: []
complements: []
tags: [llm, agents, multi-agent, education, self-hosted]
url_docs: https://github.com/THU-MAIC/OpenMAIC
url_repo: https://github.com/THU-MAIC/OpenMAIC
---

# OpenMAIC

<!-- AUTO:BANDEAU:START -->
> Application de classe virtuelle multi-agents (MIT, THU-MAIC / Tsinghua) — transforme un sujet ou un document en cours interactif : slides narrées, quiz, simulations HTML, professeur et camarades IA qui parlent et dessinent au tableau ; export PPTX/HTML, hébergé ou auto-déployé.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé · mono-nœud | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

« Open Multi-Agent Interactive Classroom », issu de l'équipe **THU-MAIC** de l'université
**Tsinghua**. Il prend en entrée un sujet ou un document et produit une **classe complète** :
suites de slides narrées, quiz interactifs, simulations HTML, séquences de projet. Des agents
**enseignant et camarades** animent la séance — ils parlent en synthèse vocale, débattent,
écrivent formules et schémas au tableau blanc. Ce n'est pas une bibliothèque d'agents : c'est
un produit qui en **consomme** une, [[LangGraph]], pour orchestrer sa classe — la comparaison
pertinente n'est donc pas « OpenMAIC ou tel framework » mais « OpenMAIC ou construire soi-même
cette application ». Stack Next.js / React, agnostique du fournisseur de modèle, avec une voie
entièrement locale possible pour le LLM, la synthèse et la reconnaissance vocales.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Produire du matériel pédagogique interactif à partir de documents existants, sans le construire à la main | Contenu **généré** : erreurs factuelles, formules approximatives et raccourcis sont à relire avant diffusion — le contexte qui exige un contenu certifié exact sans relecture humaine est exclu |
| Vouloir une classe **animée** — voix, tableau, échanges entre agents — plutôt qu'un simple générateur de slides | La démo hébergée envoie sujets et documents chez un tiers : à bannir pour du matériel confidentiel |
| Exigence de souveraineté : déploiement sur son infrastructure, avec des modèles locaux si besoin | Le coût de la **synthèse vocale** est facilement sous-estimé face à celui du texte |
| Récupérer les livrables hors de l'outil : export PPTX, HTML, ou paquet de classe hors-ligne | Projet **jeune** — v1.0.0 fin août 2026 — à forte cadence : épingler une version pour tout usage suivi |
| | Empilement Next.js 16 / React 19 récent : contraintes de build et d'hébergement serrées |
| | Simple générateur de présentations : la classe multi-agents est un surcoût inutile |
| | Plateforme d'apprentissage avec suivi des apprenants, inscriptions et notation : ce n'est pas un LMS |
| | Construire une application d'agents propre : c'est une bibliothèque qu'il faut → [[PraisonAI]], [[CrewAI]] |

## Mise en œuvre

- Installation — Docker Compose, Vercel, ou développement local ; une démo est aussi hébergée par le projet
- Point d'entrée — l'application web : on lui donne un sujet ou un document, elle rend une classe
- Prérequis — Node.js ≥ 20 et pnpm ≥ 10 ; un fournisseur de modèle parmi une dizaine (OpenAI, Anthropic, Gemini, DeepSeek, Azure, Bedrock…), ou une voie entièrement locale
- Exécution — mono-nœud ; persistance en navigateur par défaut, PostgreSQL optionnel pour un stockage côté serveur
- Coût — gratuit, licence MIT, une dépendance de conversion de formules en LGPL-3.0. La dépense est dominée par les appels LLM **et la synthèse vocale** : une séance génère beaucoup de tokens et d'audio. La voie locale la supprime, au prix du matériel

## Écosystème

### Alternatives

Aucune application équivalente n'est référencée dans le brain à ce jour : le domaine
`llm/assistant` ne compte pas d'autre produit pédagogique.

## Ressources

- Dépôt — https://github.com/THU-MAIC/OpenMAIC

## Voir aussi

- [[Assistants]] — le hub du dossier : ce qui distingue une application d'agent d'une bibliothèque
- [[OpenClaw]] — le voisin du dossier avec qui une intégration messagerie est annoncée (Feishu, Slack, Telegram, Discord)
- [[Multi-agent systems]] — la notion : plusieurs agents en interaction, le cœur du dispositif
- [[Agent patterns]] — les schémas d'agents mobilisés
