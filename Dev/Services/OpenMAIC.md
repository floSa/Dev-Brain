---
galaxie: dev
type: service
nom: OpenMAIC
alias: [openmaic, maic, open-multi-agent-interactive-classroom]
pitch: "Application de classe virtuelle multi-agents (MIT, THU-MAIC / Tsinghua) — transforme un sujet ou un document en cours interactif : slides narrées, quiz, simulations HTML, professeur et camarades IA qui parlent et dessinent au tableau ; export PPTX/HTML, hébergé ou auto-déployé."
categorie: llm/app
famille: application
licence_type: open-source
hosted: both
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [llm, agents, multi-agent, education, self-hosted]
url_docs: https://github.com/THU-MAIC/OpenMAIC
url_repo: https://github.com/THU-MAIC/OpenMAIC
---

# OpenMAIC

## Pourquoi

« Open Multi-Agent Interactive Classroom », issu de l'équipe **THU-MAIC** de l'université **Tsinghua**. Prend en entrée un sujet ou un document et produit une **classe complète** : suites de slides avec narration, quiz interactifs, simulations HTML, séquences de projet. Des **agents enseignant et camarades** animent la séance — ils parlent en synthèse vocale, débattent, écrivent formules et schémas au tableau blanc.

Cette fiche porte la catégorie `llm/app` — et c'est le point à retenir. `llm/framework` désigne les briques et SDK **avec lesquels on construit** un système d'agents ; `llm/app` désigne une **application prête à déployer et à utiliser telle quelle**. OpenMAIC n'est pas un framework d'agents : c'est un produit qui en **consomme** un, [[Dev/Services/LangGraph|LangGraph]], pour orchestrer sa classe. On l'installe et on s'en sert ; on n'assemble rien.

Conséquence pratique : la comparaison pertinente n'est pas « OpenMAIC ou CrewAI » mais « OpenMAIC ou construire soi-même cette application ». Le coût d'entrée est celui d'un déploiement, pas celui d'un développement.

Stack Next.js / React / TypeScript, agnostique du fournisseur de modèle (OpenAI, Anthropic, Gemini, DeepSeek, Azure, Bedrock et une dizaine d'autres), avec une voie **entièrement locale** possible pour LLM, TTS et ASR. Licence **MIT** (une dépendance de conversion de formules en LGPL-3.0). v1.0.0 publiée fin août 2026 — projet très visible mais **jeune**.

## Quand l'utiliser

- Produire du matériel pédagogique interactif à partir de documents existants, sans le construire à la main.
- Besoin d'une classe **animée** (voix, tableau, échanges entre agents) plutôt que d'un simple générateur de slides.
- Exigence de **souveraineté** : déploiement sur son infrastructure, avec des modèles locaux si besoin.
- Récupérer les livrables hors de l'outil : export PPTX, HTML, ou paquet de classe hors-ligne.

## Quand NE PAS l'utiliser

- Construire une **application d'agents** propre : c'est un framework qu'il faut, pas ce produit → [[Dev/Services/LangGraph|LangGraph]], [[Dev/Services/PraisonAI|PraisonAI]], [[Dev/Services/CrewAI|CrewAI]].
- Besoin d'un simple générateur de présentations : la classe multi-agents est un surcoût inutile.
- Plateforme d'apprentissage avec suivi des apprenants, inscriptions, notation : ce n'est pas un LMS.
- Contexte où le contenu généré doit être **certifié exact** sans relecture humaine (cf. Pièges).

## Déploiement & coût

- Open-source (MIT), gratuit ; démo hébergée par le projet, ou auto-déploiement.
- Auto-déploiement : Docker Compose, Vercel, ou développement local — Node.js ≥ 20 et pnpm ≥ 10 requis.
- Persistance en navigateur par défaut ; PostgreSQL optionnel pour un stockage côté serveur.
- Coût dominé par les appels **LLM** et la **synthèse vocale** : une séance génère beaucoup de tokens et d'audio.
- Voie locale possible (LLM, TTS, ASR) pour supprimer la dépense par appel au prix du matériel.

## Pièges

- Contenu pédagogique **généré** : erreurs factuelles, formules approximatives et raccourcis sont à relire avant diffusion.
- La démo hébergée envoie sujets et documents chez un tiers — bannir pour du matériel confidentiel.
- Le coût de la **TTS** est facilement sous-estimé face à celui du texte.
- Projet **jeune** (v1.0.0 datant de quelques jours), à forte cadence : épingler une version pour tout usage suivi.
- Empilement Next.js 16 / React 19 récent : les contraintes de build et d'hébergement sont serrées.

## Alternatives

Aucune application équivalente n'est référencée dans le brain à ce jour : la catégorie `llm/app` est neuve et OpenMAIC y est seul.

## Liens

- Orchestre ses agents via [[Dev/Services/LangGraph|LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.
- Intégration messagerie annoncée avec [[Dev/Services/OpenClaw|OpenClaw]] (Feishu, Slack, Telegram, Discord).
- [[Multi-agent systems]] — concept : plusieurs agents en interaction, le cœur du dispositif
- [[Agent patterns]] — concept : les schémas d'agents mobilisés
- Repo : https://github.com/THU-MAIC/OpenMAIC
