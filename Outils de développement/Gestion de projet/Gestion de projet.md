---
role: hub
nom: Gestion de projet
alias: [project management, conduite de projet, cycle de vie logiciel, méthodes de projet]
pitch: Conduire un projet de développement, avec ou sans agent — cycle de vie, spécification, backlog, décisions, contexte, revue, versions, mesure.
domaines: [data-sci, data-eng, mlops, ml-eng, ai-eng]
tags: [project-management, spec-driven, adr, skills]
---

# Gestion de projet

> Conduire un projet de développement, avec ou sans agent — cycle de vie, spécification, backlog, décisions, contexte, revue, versions, mesure.

## Ce qu'il faut comprendre

- Ce dossier range d'abord des **méthodes** (des notions), puis les **outils qui les servent autour de l'agent** : contexte du dépôt, agents en parallèle, revue, versions et changelog, commandes du projet. Une méthode ou un outil de conduite de projet reste ici même quand il suppose un agent de code (règle D-R13 de la taxonomie) ; l'agent lui-même, le produit qu'on installe, est dans [[Agents de code]], et l'outil de documentation du dépôt a sa page voisine ci-dessous.
- Le fil conducteur est [[Cycle de vie d'un projet assisté par agent]] : cadrer, spécifier, planifier, implémenter, vérifier, documenter, livrer. Chaque autre page détaille une étape ou une porte de décision de ce cycle.
- Deux écoles se croisent. Celle qui **écrit d'abord** : spécification, PRD, ADR ([[Développement piloté par la spécification]], [[PRD et user stories]], [[ADR et design docs]]). Celle qui **boucle sur du vérifiable** : tests, revue, boucle courte ([[Revue, tests et définition de terminé avec un agent]], [[Boucle de Ralph]]). Les deux se combinent ; la première coûte du temps de rédaction, la seconde de la rigueur sur les tests.
- Un agent ne remplace pas la méthode : il en amplifie les défauts. Le contraste est posé dans [[Vibe coding contre ingénierie agentique]].
- La documentation du projet a sa page voisine, hors de ce dossier : [[Diátaxis et docs-as-code]].

## Choisir

- Démarrer un projet avec un agent et ne pas savoir par où commencer → [[Cycle de vie d'un projet assisté par agent]], puis la page de l'étape qui bloque.
- Une fonctionnalité floue à cadrer → [[PRD et user stories]] ; une fois cadrée, la spécification exécutable : [[Développement piloté par la spécification]], avec [[Spec Kit]] (spécification, plan, tâches) ou [[BMAD]] (un jeu d'agents et de workflows qui couvre tout le cycle, jusqu'aux stories).
- Organiser le travail, seul ou en petite équipe → [[Backlog, Kanban, Scrum et Shape Up]] : en solo, un backlog et un tableau suffisent.
- Une décision d'architecture à garder → [[ADR et design docs]] ; la structure du système à dessiner → [[Modèle C4]], avec [[Mermaid]], [[Excalidraw]], [[draw.io]] ou [[GitDiagram]] (un schéma d'un dépôt existant).
- Donner à l'agent ce qu'il ne peut pas deviner → [[Fichiers de contexte pour agents]], avec [[Context engineering]] et [[Agent skills]] pour le mécanisme ; [[i-have-adhd]] n'en contraint que le format de sortie ; [[Graphify]] et [[ai-memory]] fournissent la carte du dépôt et la mémoire entre sessions.
- Donner à l'agent le code du projet, ou à un humain le moyen de le lire → [[Repomix]] (le dépôt en un seul fichier, pour un modèle), [[Serena]] (des outils au niveau du symbole, appelés par l'agent ; GPL-3.0-or-later), [[DeepWiki-Open]] (un wiki généré, pour un lecteur). La documentation à jour des bibliothèques se sert par Context7, serveur MCP sous licence MIT dont l'index est un service hébergé fermé (Upstash), sans auto-hébergement : cité ici sans page, règle 15 du chantier ; les trois outils libres ci-dessus couvrent le besoin voisin, le code du projet lui-même.
- Une tâche longue, bien bornée et vérifiable par test → [[Boucle de Ralph]]. Plusieurs agents en parallèle sur le même dépôt → [[Branches courtes et worktrees pour agents]] (voir aussi [[swarm-forge]] et [[t3code]]) ; pour piloter ces agents depuis un tableau Kanban, une carte par agent, [[Vibe Kanban]] (la société qui l'éditait a fermé en 2026-04, le projet est tenu par la communauté). Claude Squad, Ruflo et Crystal font la même chose et n'ont pas de page.
- Savoir si le travail de l'agent est « terminé » → [[Revue, tests et définition de terminé avec un agent]], avec [[pytest]], [[Hypothesis]], [[testcontainers]] et [[pre-commit]] ; une première relecture automatique des pull requests, avant la revue humaine : [[PR-Agent]], auto-hébergeable, avec un modèle local possible.
- Nommer les commits, numéroter les versions, tenir le changelog → [[Commits conventionnels, versions et changelog]], sur une forge comme [[Forgejo]] ou [[GitLab CE]]. Les outils : [[Commitizen]] (commits guidés, version, tag, journal par commande), [[git-cliff]] (le journal et le numéro, à la forme voulue) et [[release-please]] (la release par pull request, sur GitHub) — départagés dans [[Comparatif - Versions et changelog]]. Les commandes du projet, que l'agent comme l'humain lance, s'écrivent une fois dans un `justfile` ([[just]]) ; les versions d'outils et les tâches d'un projet multi-langage dans un `mise.toml` ([[mise]]).
- Mesurer si l'ensemble marche, et ce que coûtent les agents → [[Mesurer un projet - DORA, coût des agents et temps passé]].

<!-- AUTO:START -->
### Notions
- [[ADR et design docs]] — domaines : ai-eng, mlops
- [[Backlog, Kanban, Scrum et Shape Up]] — domaines : ai-eng, data-eng, mlops
- [[Boucle de Ralph]] — domaines : ai-eng
- [[Branches courtes et worktrees pour agents]] — domaines : ai-eng, mlops
- [[Commits conventionnels, versions et changelog]] — domaines : ai-eng, mlops
- [[Cycle de vie d'un projet assisté par agent]] — domaines : ai-eng, ml-eng
- [[Développement piloté par la spécification]] — domaines : ai-eng
- [[Fichiers de contexte pour agents]] — domaines : ai-eng
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — domaines : mlops, ai-eng
- [[Modèle C4]] — domaines : ai-eng, mlops, data-eng
- [[PRD et user stories]] — domaines : ai-eng, data-eng
- [[Revue, tests et définition de terminé avec un agent]] — domaines : ai-eng, ml-eng, mlops
- [[Vibe coding contre ingénierie agentique]] — domaines : ai-eng, ml-eng

### Briques
- [[Commitizen]] — Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` — mais tout repose sur des messages de commit conformes, que seul le hook de validation impose.
- [[DeepWiki-Open]] — Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes, codemap — avec le modèle au choix (Google, OpenAI, OpenRouter, Azure, Bedrock, Ollama en local) — mais aucune release publiée, et le README renvoie vers une suite « 2.0 », Grok Wiki, qui est une autre application.
- [[git-cliff]] — Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas.
- [[just]] — Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre recettes et chargement de `.env` — mais un lanceur seulement, pas un système de build.
- [[PR-Agent]] — Outil de revue automatique de pull requests (MIT, Python), auto-hébergeable : commandes /describe, /review, /improve et /ask, en GitHub Action, en ligne de commande, en conteneur ou en webhook, pour GitHub, GitLab, Bitbucket, Azure DevOps et Gitea — mais le modèle est à fournir (clé d'API ou modèle local par LiteLLM), et le projet est un héritage de Qodo tenu par la communauté, distinct de l'offre commerciale de Qodo.
- [[release-please]] — Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets.
- [[Repomix]] — Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion.
- [[Serena]] — Serveur MCP (GPL-3.0-or-later, Python) qui donne à un agent de code des outils au niveau du symbole — chercher, renommer, remplacer le corps d'une fonction — appuyés par défaut sur des serveurs de langage, plus de 40 langages — mais l'agent et son modèle restent à fournir, et le renommage par serveur de langage ne vise que les symboles.
- [[Vibe Kanban]] — Application locale (Apache-2.0, Rust) : un tableau Kanban où chaque carte lance un agent de code dans un espace de travail isolé — branche, terminal, serveur de développement — avec revue de diff commentée et création de pull request — mais la société bloop qui la portait a fermé le 2026-04-10 et le projet vit en maintenance communautaire.

### Comparatifs
- [[Comparatif - Versions et changelog]]
<!-- AUTO:END -->
