---
role: brique
nom: DeepWiki-Open
alias: [deepwiki-open, AsyncFuncAI/deepwiki-open, Open DeepWiki]
pitch: "Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes, codemap — avec le modèle au choix (Google, OpenAI, OpenRouter, Azure, Bedrock, Ollama en local) — mais aucune release publiée, et le README renvoie vers une suite « 2.0 », Grok Wiki, qui est une autre application."
categorie: devtools/projet
famille: application
domaines: [ai-eng]
licence_type: open-source
maturite: beta
os: "Linux, macOS, Windows (Docker)"
langage: Python
hosted: [self]
scaling: single-node
alternatives: ["[[Repomix]]", "[[Serena]]"]
complements: []
tags: [documentation, rag, self-hosted]
url_docs: https://github.com/AsyncFuncAI/deepwiki-open
url_repo: https://github.com/AsyncFuncAI/deepwiki-open
---

# DeepWiki-Open

<!-- AUTO:BANDEAU:START -->
> Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes, codemap — avec le modèle au choix (Google, OpenAI, OpenRouter, Azure, Bedrock, Ollama en local) — mais aucune release publiée, et le README renvoie vers une suite « 2.0 », Grok Wiki, qui est une autre application.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web, à héberger soi-même, qui lit un dépôt et en tire un wiki : analyse de la structure du code, documentation rédigée par un modèle, diagrammes, et une carte du code (*codemap*) pour des visites guidées. Le README la présente comme l'implémentation de DeepWiki par son auteur ; le code d'ici est un service d'API Python et une interface Next.js, lancés ensemble par `docker compose` (ports 8001 pour l'API et 3000 pour l'interface). Le modèle de génération se règle dans `api/config/generator.json` : Google (Gemini par défaut), OpenAI, OpenRouter, Azure OpenAI, AWS Bedrock, DashScope et **Ollama** pour un modèle local ; des plongements existent pour OpenAI, Google, Ollama et Bedrock. Le dépôt contient un guide pour Ollama, et des profils pour une passerelle LiteLLM.

**À savoir avant de s'y fier.** Le dépôt n'a ni tag ni release. Son README, réduit à une page, annonce « Deepwiki-Open 2.0 » sous le nom **Grok Wiki** (grok-wiki.com) : d'après son site, une application de bureau qui délègue les appels de modèle aux agents en ligne de commande de l'utilisateur. Ce n'est pas le code de ce dépôt, et sa licence n'a pas été vérifiée. Le dépôt lui-même reste actif : dernier push le 2026-09-03.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comprendre un dépôt inconnu à partir d'un wiki navigable, avec des diagrammes, plutôt que de lire les sources | Donner le dépôt à un agent : un wiki n'est pas une entrée de modèle, c'est [[Repomix]] (un fichier) ou [[Serena]] (des outils) |
| Garder le code et les questions sur le réseau interne : un modèle local par Ollama évite tout appel externe | Une documentation de référence écrite à la main : le wiki est généré par un modèle, à relire (cf. [[Diátaxis et docs-as-code]]) |
| Un service qu'on déploie une fois pour l'équipe, par Docker | Un projet qui attend des versions numérotées et un suivi de sécurité : le dépôt ne publie aucune release |
| Les dépôts GitHub, GitLab et Bitbucket comme sources | Une machine modeste : le fichier `docker-compose.yml` réserve 2 Go et plafonne à 6 Go de mémoire |

## Mise en œuvre

- Installation — cloner le dépôt, renseigner un fichier `.env` (clés des fournisseurs choisis), puis lancer le `docker-compose.yml` fourni (le README actuel ne donne plus ces étapes ; elles se lisent dans les fichiers du dépôt)
- Point d'entrée — l'interface web sur le port 3000 : saisir l'adresse d'un dépôt
- Prérequis — Docker ; une clé d'API pour un fournisseur, ou un serveur Ollama avec ses modèles de génération et de plongement
- Exécution — un seul conteneur (API et interface), les dépôts et plongements gardés dans `~/.adalflow` ; mémoire réservée 2 Go, plafond 6 Go
- Coût — gratuit sous licence MIT ; la dépense est celle du modèle, nulle avec Ollama

## Écosystème

### Alternatives

- [[Repomix]] — Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion. — pour un modèle, pas pour un lecteur.
- [[Serena]] — Serveur MCP (GPL-3.0-or-later, Python) qui donne à un agent de code des outils au niveau du symbole — chercher, renommer, remplacer le corps d'une fonction — appuyés par défaut sur des serveurs de langage, plus de 40 langages — mais l'agent et son modèle restent à fournir, et le renommage par serveur de langage ne vise que les symboles. — l'outillage de l'agent pendant qu'il modifie le code.
- voisin : [[Graphify]] — transforme un dépôt en graphe de connaissances interrogeable ; une carte du code comme ici, mais lue par l'assistant.
- voisin : Context7 — serveur MCP sous licence MIT, mais son index de documentation de bibliothèques est un service hébergé fermé (Upstash), sans auto-hébergement ; sans page dans le brain (règle 15). Il décrit les bibliothèques, pas le dépôt.

## Ressources

- Dépôt — https://github.com/AsyncFuncAI/deepwiki-open

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — documenter un projet, et ce qu'un wiki généré ne remplace pas
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Ollama]] — le serveur de modèles locaux que DeepWiki-Open sait appeler
- [[Outils de développement]] — le hub du domaine
