---
role: brique
nom: Gitingest
alias: [gitingest, coderamp-labs/gitingest]
pitch: "Outil en ligne de commande et bibliothèque Python (MIT) qui transforme un dépôt Git ou un dossier en un texte unique pour un modèle de langage, avec arborescence et compte de jetons, et un site (gitingest.com) où remplacer « hub » par « ingest » dans une URL GitHub — mais le site est un service tiers, et le tri des fichiers reste à régler par motifs."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Repomix]]"]
complements: []
tags: [context-engineering, token-optimization]
url_docs: https://gitingest.com
url_repo: https://github.com/coderamp-labs/gitingest
---

# Gitingest

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande et bibliothèque Python (MIT) qui transforme un dépôt Git ou un dossier en un texte unique pour un modèle de langage, avec arborescence et compte de jetons, et un site (gitingest.com) où remplacer « hub » par « ingest » dans une URL GitHub — mais le site est un service tiers, et le tri des fichiers reste à régler par motifs.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil qui lit un dépôt Git (par son URL, y compris un sous-dossier) ou un dossier local et en tire **un seul texte** à donner à un modèle : un résumé, l'arborescence, puis le contenu des fichiers, avec la taille de l'extrait et le nombre de jetons. Il s'utilise de trois façons : la commande `gitingest` (qui écrit `digest.txt`, ou la sortie standard avec `-o -`), la bibliothèque Python (`ingest()` et `ingest_async()` rendent le résumé, l'arbre et le contenu), et le site gitingest.com, où l'on remplace `hub` par `ingest` dans une URL GitHub pour obtenir le même résumé. Les fichiers du `.gitignore` sont ignorés par défaut ; un dépôt privé demande un jeton GitHub ; les sous-modules s'ajoutent par `--include-submodules`.

Le site est un service hébergé par l'éditeur : pour ne pas envoyer un dépôt interne chez un tiers, la commande locale suffit, et l'image Docker du dépôt (`docker build`, port 8000) permet d'héberger l'application web chez soi. La télémétrie (Sentry, métriques Prometheus) ne s'active que par variables d'environnement d'après le README. Dernière release v0.3.1 du 2025-07-31, dépôt poussé le 2026-10-06, licence MIT lue dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner un dépôt public à un modèle en changeant une URL, sans rien installer | Le dépôt est interne : la commande locale, ou l'image Docker hébergée chez soi, mais pas le site public |
| Appeler l'extraction depuis du code Python : `ingest()` rend trois chaînes, prêtes à passer dans un prompt | Des options de compression fines, un format XML, un serveur MCP : [[Repomix]] en offre plus |
| Piloter par la sortie standard dans un script : `gitingest . -o -` | Un contexte tenu à jour pendant la session : le texte est une photo du dépôt, à regénérer |
| Un compte de jetons avant d'envoyer le texte | Un dépôt qui dépasse la fenêtre du modèle : le compte le montre, le tri est à faire par motifs d'inclusion et d'exclusion |

## Mise en œuvre

- Installation — `pipx install gitingest` (recommandé par le README) ou `pip install gitingest` ; `gitingest[server]` ajoute les dépendances de l'application web
- Point d'entrée — `gitingest <dossier ou URL>` ; `--token` ou `GITHUB_TOKEN` pour un dépôt privé
- Prérequis — Python 3.8 ou plus
- Exécution — sur le poste ; le site est un service tiers, l'application web s'auto-héberge par Docker ou Compose
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[Repomix]] — Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers ressemblant à des secrets écartés, code réductible à sa structure par Tree-sitter — mais le tri de ce qui compte reste à faire par motifs d'inclusion et d'exclusion. — là où Gitingest s'écrit pour Python et se lance par une URL, Repomix compresse, filtre et sert aussi de serveur MCP.
- voisin : [[DeepWiki-Open]] — un wiki à lire par un humain, au lieu d'un texte à donner à un modèle.

## Ressources

- Documentation — https://gitingest.com
- Dépôt — https://github.com/coderamp-labs/gitingest

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Context engineering]] — composer et borner le contexte donné au modèle
- [[Outils de développement]] — le hub du domaine
