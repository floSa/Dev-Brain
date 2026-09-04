---
role: brique
nom: OpenHands
alias: [openhands, opendevin, open-devin]
pitch: "Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé."
categorie: llm/assistant
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: "Python, TypeScript"
scaling: single-node
alternatives: ["[[Maka]]"]
complements: []
tags: [llm, agents, tool-use, code-generation]
url_docs: https://docs.all-hands.dev/
url_repo: https://github.com/OpenHands/OpenHands
---

# OpenHands

<!-- AUTO:BANDEAU:START -->
> Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python, TypeScript | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'agent de développement autonome, ex-**OpenDevin**, portée par **All Hands AI**. À
la différence des bibliothèques avec lesquelles on *construit* un agent, OpenHands **est**
l'agent : il interagit avec le monde comme un développeur — il écrit et modifie du code dans un
dépôt, exécute des commandes dans un shell, lance des tests et navigue le web. On lui confie
une tâche — fonctionnalité, refactor, correction de bug — et il planifie puis applique les
changements de bout en bout, dans un environnement d'exécution conteneurisé. Le cœur est sous
MIT ; le dossier `enterprise/` est source-available.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déléguer des tâches d'ingénierie complètes : créer un projet, ajouter une fonctionnalité, refactorer, débugger | **Exécution arbitraire** : l'agent lance des commandes shell et modifie des fichiers — toujours en conteneur isolé, jamais sur de la production ni sur un dépôt non sauvegardé |
| Tâches greenfield ou bien cadrées, où l'agent peut itérer seul : écrire, exécuter, corriger | **Coût et dérive** : une tâche longue enchaîne beaucoup d'appels LLM ; cadrer le périmètre et surveiller la dépense |
| Vouloir une alternative open-source et auto-hébergeable aux agents de code propriétaires | Performance **dépendante du modèle** : un LLM faible donne un agent qui tourne en rond |
| | Construire son propre agent sur mesure — logique métier, multi-agents → [[OpenAI Agents SDK]], [[CrewAI]], [[smolagents]] |
| | Contrôle fin du flux d'état et human-in-the-loop programmable → [[LangGraph]] |

## Mise en œuvre

- Installation — image Docker, le chemin le plus simple ; le runtime d'exécution est lui-même conteneurisé
- Point d'entrée — l'interface de l'agent : on lui décrit une tâche, il écrit le code, lance les commandes et les tests, et navigue le web
- Prérequis — une clé API de fournisseur de modèle ; Claude est conseillé, mais tout fournisseur convient
- Exécution — mono-nœud en self-host ; **OpenHands Cloud** pour la version managée, avec ses intégrations
- Coût — cœur gratuit sous MIT ; **OpenHands Enterprise** est source-available et sa licence s'achète au-delà d'un mois d'usage. La dépense dominante reste les appels LLM d'un agent qui boucle longtemps

## Écosystème

### Alternatives

- [[Maka]] — Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.

## Ressources

- Documentation — https://docs.all-hands.dev/
- Dépôt — https://github.com/OpenHands/OpenHands

## Voir aussi

- [[Assistants]] — le hub du dossier : ce qui distingue une application d'agent d'une bibliothèque
- [[OpenClaw]] · [[Hermes Agent]] — les voisins généralistes du dossier, là où celui-ci est spécialisé sur le développement
- [[Sandboxing de code généré]] — l'isolation sans laquelle l'exécution arbitraire n'est pas défendable
- [[Agent patterns]] · [[agent-loops]] · [[Tool use patterns]] · [[Agent memory]] — les schémas qu'il met en œuvre
- [[AutoGen]] · [[Agno]] — des bibliothèques pour *bâtir* un agent, la catégorie opposée
