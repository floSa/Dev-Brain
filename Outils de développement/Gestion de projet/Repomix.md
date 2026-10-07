---
role: brique
nom: Repomix
alias: [repomix, yamadashy/repomix]
pitch: "Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Serena]]", "[[DeepWiki-Open]]", "[[Gitingest]]"]
complements: []
tags: [context-engineering, token-optimization, mcp]
url_docs: https://repomix.com
url_repo: https://github.com/yamadashy/repomix
---

# Repomix

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui lit un dépôt et l'écrit dans **un seul fichier**, structuré pour qu'un modèle de langage le lise d'un coup : résumé du fichier, arborescence, puis le contenu de chaque fichier. La sortie par défaut est un `repomix-output.xml` ; les formats Markdown, JSON et texte brut se choisissent par `--style`. Il compte les jetons de chaque fichier et du dépôt entier, respecte `.gitignore`, `.ignore` et `.repomixignore`, et passe [Secretlint](https://github.com/secretlint/secretlint) pour écarter les fichiers qui ressemblent à des identifiants connus. L'option `--compress` réduit le code à ses classes, fonctions et interfaces par analyse Tree-sitter. Version 1.18.1 du 2026-09-21, licence MIT lue dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner un dépôt entier à un modèle depuis un chat qui n'a pas accès au disque : un fichier à coller ou à téléverser | Le dépôt dépasse la fenêtre du modèle : le compte de jetons le dira, `--compress` ne garde que la structure, et le détail est perdu. [[Serena]] lit le code symbole par symbole, à la demande |
| Préparer une revue, une documentation ou des tests : le README propose des exemples de requêtes pour chacun | Un contexte maintenu à jour pendant la session : le fichier produit est une photo du dépôt, à regénérer après chaque changement |
| Scripter l'empaquetage : `--include`, `--ignore`, fichiers listés sur l'entrée standard, sortie JSON lisible par `jq` | Un dépôt qui contient des secrets sous un format que Secretlint ne reconnaît pas : relire le fichier produit avant de l'envoyer à un service tiers |
| Empaqueter un dépôt distant sans le cloner à la main : `repomix --remote <utilisateur>/<dépôt>` | Une documentation lisible par un humain : c'est [[DeepWiki-Open]] qui produit un wiki, Repomix produit une entrée de modèle |

## Mise en œuvre

- Installation — `npx repomix@latest` sans installer, ou `npm install -g repomix`, `yarn global add`, `bun add -g`, `brew install repomix`
- Point d'entrée — la commande `repomix` dans le dépôt, qui écrit `repomix-output.xml` ; `--style markdown|json|plain` change le format, `--compress` réduit le code
- Prérequis — Node.js pour l'installation par npm ; une image Docker existe (`ghcr.io/yamadashy/repomix`)
- Exécution — sur le poste ou en conteneur ; le mode `--mcp` lance Repomix comme serveur MCP, avec `--sandbox` pour confiner ses outils de fichiers à un répertoire. Un site web, une extension de navigateur et une extension VS Code existent aussi
- Coût — gratuit sous licence MIT ; dépôt poussé le 2026-10-03

## Écosystème

### Alternatives

- [[Serena]] — Serveur MCP (GPL-3.0-or-later, Python) qui donne à un agent de code des outils au niveau du symbole — chercher, renommer, remplacer le corps d'une fonction — appuyés par défaut sur des serveurs de langage, plus de 40 langages — mais l'agent et son modèle restent à fournir, et le renommage par serveur de langage ne vise que les symboles. — là où Repomix donne tout le dépôt d'un bloc, Serena laisse l'agent aller chercher le seul symbole utile.
- [[DeepWiki-Open]] — Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes, codemap — avec le modèle au choix (Google, OpenAI, OpenRouter, Azure, Bedrock, Ollama en local) — mais aucune release publiée, et le README renvoie vers une suite « 2.0 », Grok Wiki, qui est une autre application. — un wiki à lire par un humain, au lieu d'un fichier à donner à un modèle.
- [[Gitingest]] — Outil en ligne de commande et bibliothèque Python (MIT) qui transforme un dépôt Git ou un dossier en un texte unique pour un modèle de langage, avec arborescence et compte de jetons, et un site (gitingest.com) où remplacer « hub » par « ingest » dans une URL GitHub — mais le site est un service tiers, et le tri des fichiers reste à régler par motifs. — là où Repomix compresse, filtre et sert de serveur MCP, Gitingest se lance par une URL et s'appelle depuis Python.
- voisin : Context7 — serveur MCP sous licence MIT, mais son index de documentation de bibliothèques est un service hébergé fermé (Upstash), sans auto-hébergement ; sans page dans le brain (règle 15). Pour donner de la documentation à jour plutôt que le code du projet.

## Ressources

- Documentation — https://repomix.com
- Dépôt — https://github.com/yamadashy/repomix

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Context engineering]] — composer et borner le contexte donné au modèle
- [[Outils de développement]] — le hub du domaine
