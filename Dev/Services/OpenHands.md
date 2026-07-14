---
galaxie: dev
type: service
nom: OpenHands
alias: [openhands, opendevin, open-devin]
pitch: "Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: "Python, TypeScript"
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [llm, agents, tool-use, code-generation]
url_docs: https://docs.all-hands.dev/
url_repo: https://github.com/OpenHands/OpenHands
---

# OpenHands

## Pourquoi

Plateforme d'**agent de développement autonome** (ex-**OpenDevin**, portée par **All Hands AI**). À la différence des frameworks pour *construire* des agents, OpenHands **est** l'agent : il interagit avec le monde comme un développeur humain — il **écrit et modifie du code** dans un dépôt, **exécute des commandes** dans un shell, lance des tests et **navigue le web**. On lui donne une tâche (fonctionnalité, refactor, correction de bug), il planifie et applique les changements de bout en bout dans un environnement d'exécution conteneurisé. Cœur sous licence **MIT** (le dossier `enterprise/` est source-available). Modèle conseillé : Claude (Anthropic), mais n'importe quel fournisseur via une clé API.

## Quand l'utiliser

- Déléguer des **tâches d'ingénierie complètes** à un agent : créer un projet, ajouter une feature, refactorer, débugger.
- Tâches **greenfield** ou bien cadrées où l'agent peut itérer seul (écrire → exécuter → corriger).
- Vouloir une alternative **open-source et self-hostable** aux agents de code propriétaires (Devin, etc.).

## Quand NE PAS l'utiliser

- **Construire son propre agent** sur mesure (logique métier, multi-agents) → frameworks comme [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/smolagents|smolagents]].
- Tâches exigeant un **contrôle fin** du flux d'état et du human-in-the-loop programmable → [[Dev/Services/LangGraph|LangGraph]].
- Contexte sensible sans **isolation** : l'agent exécute des commandes arbitraires — sandboxer et restreindre les accès.

## Déploiement & coût

- Cœur open-source (MIT), gratuit ; lancement le plus simple via **Docker** (runtime d'exécution conteneurisé).
- **OpenHands Cloud** : offre managée (agent hébergé, intégrations) ; **OpenHands Enterprise** source-available (au-delà d'un mois d'usage, licence à acheter).
- Coût réel dominé par les appels **LLM** d'un agent qui boucle longtemps sur une tâche.

## Pièges

- **Exécution arbitraire** : l'agent lance des commandes shell et modifie des fichiers — toujours en conteneur isolé, jamais sur un environnement de prod ou un dépôt non sauvegardé.
- **Coût/dérive** : les tâches longues enchaînent de nombreux appels LLM ; cadrer le périmètre et surveiller la dépense.
- Performance **dépendante du modèle** : un LLM faible donne un agent qui tourne en rond — privilégier un modèle de pointe.

## Alternatives

<!-- OpenHands est un agent de dev autonome (produit), pas un framework pour bâtir des agents : pas d'alternative directe dans le brain. -->
- Pour **construire** un agent sur mesure plutôt que d'en utiliser un clé en main, voir les frameworks d'agents : [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/smolagents|smolagents]].

## Liens

- Catégorie **agent de code autonome** — distinct des frameworks d'agents généralistes ([[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/Agno|Agno]]) qui servent à *bâtir* des agents.
- Concepts : [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.all-hands.dev/
