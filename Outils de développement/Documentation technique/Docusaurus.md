---
role: brique
nom: Docusaurus
alias: [docusaurus, Docusaurus 3]
pitch: "Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions et composants MDX — il demande Node et son écosystème."
categorie: devtools/documentation
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[MkDocs]]", "[[Sphinx]]", "[[Zensical]]"]
complements: []
tags: [documentation]
url_docs: https://docusaurus.io/
url_repo: https://github.com/facebook/docusaurus
---

# Docusaurus

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions et composants MDX — il demande Node et son écosystème.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de sites de documentation de **Meta**, conçu pour ses propres projets et ouvert aux autres. La documentation le décrit comme un générateur de sites statiques qui produit une **application monopage** : navigation côté client, et toute la puissance de **React** pour les pages interactives. On y écrit en Markdown, avec **MDX** (du JSX dans le Markdown) quand il faut un composant. Il apporte d'origine une page d'accueil, une section de documentation, un **blog** et des pages libres, plus des fonctions que les autres générateurs du dossier traitent en plugin ou pas du tout : **versions de la documentation**, **traduction** (support de la localisation fourni, via Crowdin) et recherche.

Le prix est l'écosystème : Node.js et npm, un projet JavaScript à côté d'un dépôt Python ou data, et une mise à jour de dépendances à tenir. Version 3.10.2 du 2026-07-10 (Node ≥ 20), dernier commit le 2026-10-05, environ 66,4 k étoiles. Les fichiers `.md` du dossier `docs/` du dépôt suivent une licence Creative Commons distincte du code (fichier `LICENSE-docs`).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Site de produit ou de projet avec documentation, blog, versions et langues multiples | Documentation interne d'un dépôt Python ou data, sans besoin de React → [[MkDocs]] ou [[Zensical]] |
| Pages interactives ou composants React dans la documentation (MDX) | Référence d'API Python générée depuis les docstrings → [[Sphinx]] ou [[mkdocstrings]] |
| Équipe déjà à l'aise avec JavaScript et TypeScript | Poste ou chaîne CI sans Node : l'outil l'exige, et son arbre de dépendances est large |
| Documentation versionnée par numéro de version du produit | Sortie PDF ou EPUB native : le rendu est un site web |

## Mise en œuvre

- Installation — `npx create-docusaurus@latest mon-site classic`
- Point d'entrée — `npx docusaurus start` pour prévisualiser, `npx docusaurus build` pour produire le site statique
- Prérequis — Node.js ≥ 20 (moteur déclaré par le paquet `@docusaurus/core`)
- Exécution — sur le poste et en CI ; le site produit est statique, publiable sur n'importe quel serveur de fichiers
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[MkDocs]] — Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10.
- [[Sphinx]] — Outil en ligne de commande (BSD-2-Clause, Python) : générateur de documentation écrit en reStructuredText, qui sort HTML, PDF, EPUB et pages de manuel avec renvois sémantiques et index automatiques — le Markdown passe par l'extension MyST-Parser.
- [[Zensical]] — Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — encore en versions 0.0.x, avec des remplaçants de plugins MkDocs en cours d'écriture.

## Ressources

- Documentation — https://docusaurus.io/docs
- Dépôt — https://github.com/facebook/docusaurus

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — ce qu'il faut écrire, et comment le garder à jour
- [[Mermaid]] — le diagramme en texte, que les générateurs du dossier savent rendre
- [[Comparatif - Générateurs de documentation]] — ce qui départage les générateurs du dossier
- [[Outils de développement]] — le hub du domaine
