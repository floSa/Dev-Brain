---
role: brique
nom: Serena
alias: [serena, oraios/serena, serena-agent]
pitch: "Serveur MCP (GPL-3.0-or-later, Python) qui donne à un agent de code des outils au niveau du symbole — chercher, renommer, remplacer le corps d'une fonction — appuyés par défaut sur des serveurs de langage, plus de 40 langages — mais l'agent et son modèle restent à fournir, et le renommage par serveur de langage ne vise que les symboles."
categorie: devtools/projet
famille: plateforme
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Python
hosted: [self]
scaling: single-node
alternatives: ["[[Repomix]]", "[[DeepWiki-Open]]"]
complements: []
tags: [mcp, agents, context-engineering]
url_docs: https://oraios.github.io/serena
url_repo: https://github.com/oraios/serena
---

# Serena

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur MCP qui s'ajoute à un client d'agent de code déjà en place et lui prête des outils proches de ceux d'un IDE : trouver un symbole, lister les symboles d'un fichier, trouver ses références, renommer, remplacer ou compléter le corps d'une fonction. L'agent travaille sur des symboles et non sur des numéros de ligne ou des motifs de recherche, ce qui épargne des lectures de fichiers entiers. Serena ne contient pas de modèle : le README le dit, un LLM est nécessaire pour orchestrer les outils. Deux moteurs d'analyse existent : des **serveurs de langage** (LSP), choisis par défaut, libres, pour plus de 40 langages ; et un **greffon JetBrains payant** (essai gratuit), qui ajoute le déplacement, l'inlining et la recherche dans les dépendances. Un système de mémoire, désactivable, garde des connaissances entre sessions, utilisateurs et projets ; le README note que des utilisateurs le combinent avec les fichiers de contexte de leur agent (`AGENTS.md`).

**Licence.** Le fichier LICENSE du dépôt est un résumé par composant : SolidLSP sous MIT, l'application Serena sous **GPL-3.0-or-later**. Le paquet `serena-agent`, qui les combine, est donc soumis à la GPL-3.0-or-later dans son ensemble. À signaler pour un usage en ESN : une copie modifiée distribuée à un client porte la GPL.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un dépôt trop gros pour être lu d'un bloc : l'agent va chercher le symbole utile au lieu de lire des fichiers entiers | Un petit dépôt qu'un seul fichier empaqueté suffit à décrire : [[Repomix]] est plus simple |
| Renommer ou retrouver les références à travers plusieurs fichiers, avec un serveur de langage plutôt qu'un chercher-remplacer | Un déplacement de symbole ou un inlining : le README réserve ces opérations au greffon JetBrains payant, le moteur libre ne les fournit pas |
| Un client MCP déjà choisi (terminal, extension d'IDE, application de bureau) : Serena s'y branche sans le remplacer | Un livrable redistribué sous une autre licence : la GPL-3.0-or-later s'applique au paquet combiné |
| Une mémoire qui survit aux sessions, en complément de `AGENTS.md` : le système de mémoire de Serena le permet et se désactive si un autre est préféré | Un wiki ou une documentation lisible par un humain : [[DeepWiki-Open]] |

## Mise en œuvre

- Installation — `uv tool install -p 3.13 serena-agent`, puis `serena init` ; le README demande de ne pas passer par une place de marché de MCP ou de greffons, dont les commandes d'installation seraient périmées
- Point d'entrée — la commande `serena`, donnée au client MCP comme commande de lancement ; ou un serveur lancé en mode HTTP dont le client reçoit l'URL
- Prérequis — [[uv]] ; selon le langage, un serveur de langage à installer à part
- Exécution — sur le poste, lancé par le client MCP ou à part en mode HTTP ; le modèle vient du client. Version 1.7.0 du 2026-08-09, dépôt poussé le 2026-10-06
- Coût — gratuit en moteur LSP ; le greffon JetBrains est payant, hors du périmètre du brain

## Écosystème

### Alternatives

- [[Repomix]] — Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion. — le dépôt d'un bloc, sans serveur ni serveur de langage.
- [[DeepWiki-Open]] — Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes, codemap — avec le modèle au choix (Google, OpenAI, OpenRouter, Azure, Bedrock, Ollama en local) — mais aucune release publiée, et le README renvoie vers une suite « 2.0 », Grok Wiki, qui est une autre application. — un wiki pour l'humain ; Serena sert l'agent pendant qu'il travaille.
- voisin : [[Graphify]] — carte du dépôt en graphe de connaissances, lue par l'assistant avant de chercher ; une autre manière de donner la structure, sans serveur de langage.
- voisin : Context7 — serveur MCP sous licence MIT, mais son index de documentation de bibliothèques est un service hébergé fermé (Upstash), sans auto-hébergement ; sans page dans le brain (règle 15). Il donne la documentation des bibliothèques, Serena le code du projet.

## Ressources

- Documentation — https://oraios.github.io/serena
- Dépôt — https://github.com/oraios/serena

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[mcp-protocol]] — le protocole par lequel l'agent appelle les outils de Serena
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Context engineering]] — composer et borner le contexte donné au modèle
- [[Outils de développement]] — le hub du domaine
