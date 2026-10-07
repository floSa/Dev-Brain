---
role: brique
nom: MkDocs
alias: [mkdocs, MkDocs 1.x]
pitch: "Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10."
categorie: devtools/documentation
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Sphinx]]", "[[Docusaurus]]", "[[Zensical]]"]
complements: ["[[mkdocstrings]]"]
tags: [documentation]
url_docs: https://www.mkdocs.org/
url_repo: https://github.com/mkdocs/mkdocs
---

# MkDocs

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de sites statiques pensé pour la documentation d'un projet. Les sources sont des fichiers **Markdown** rangés dans un dossier `docs/`, la configuration tient dans un seul fichier **`mkdocs.yml`** (navigation, thème, extensions), et deux commandes suffisent : `mkdocs serve` pour prévisualiser avec rechargement, `mkdocs build` pour produire le site, que n'importe quel serveur de fichiers statiques peut publier. Thèmes, plugins et extensions Markdown tierces l'étendent ; le catalogue communautaire recense ceux qui existent.

C'est la base d'un écosystème : le thème Material for MkDocs, [[mkdocstrings]] pour la documentation d'API et des centaines de plugins s'y greffent. Version 1.6.1 du 2024-08-30, environ 22,5 k étoiles le 2026-10-07, licence BSD-2-Clause.

## Où en est le projet — à lire avant de le choisir

Le projet **ralentit nettement**, et c'est le critère décisif en 2026. Relevé le 2026-10-07 sur le dépôt :

- Dernière version publiée : 1.6.1, le **2024-08-30**. Dernier commit sur la branche principale : le **2025-10-20**, soit un an sans aucun commit.
- Discussions du dépôt : « Is mkdocs still under maintenance? » (2025-11-10, « no commits for a year or so »), puis « Version 2 » (2026-01-21) où le mainteneur annonce une version 2 avec une documentation préliminaire, **dépôt privé**, puis « Reviving the maintenance of MkDocs » (2026-03-09), qui renvoie vers l'organisation GitHub **ProperDocs**, une reprise communautaire de la ligne 1.x. Ce fork n'est pas fiché ici : aucun avis de fond dessus.
- L'équipe de Material for MkDocs écrit (billet du 2026-02-18, mis à jour jusqu'au 2026-10-02) que MkDocs 1.x est **non maintenu**, et que MkDocs 2.0, une réécriture complète encore en pré-version, apporte des ruptures potentielles. Cette équipe est **partie prenante** : elle développe [[Zensical]], le remplaçant. Le constat de l'absence de version se vérifie, le jugement sur la version 2 se lit comme un avis.

Conséquence pratique : MkDocs 1.6.1 fonctionne et reste utilisable pour un site existant, mais un nouveau projet prend le risque d'un outil sans correctifs de sécurité annoncés. Le choix se fait alors entre [[Zensical]] (qui lit le même `mkdocs.yml`) et un outil à direction stable.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un site de documentation Python simple, en Markdown, publiable sur un simple serveur statique, y compris sans accès à internet | Nouveau projet à durée de vie longue : aucun commit depuis 2025-10, aucune version stable depuis 2024-08 |
| Un site existant déjà bâti sur MkDocs et Material, qu'il n'y a aucune urgence à migrer | Documentation d'API multi-langages ou sortie PDF native → [[Sphinx]] |
| Un `mkdocs.yml` que [[Zensical]] sait aussi construire : l'issue de secours est connue | Site à composants React, blog, versions et traductions intégrés → [[Docusaurus]] |
| Documentation d'API Python générée depuis les docstrings avec [[mkdocstrings]] | MkDocs 2.0 : version annoncée comme réécriture, avec ruptures possibles pour les plugins et thèmes (avis de l'équipe de Material) |

## Mise en œuvre

- Installation — `pip install mkdocs` (Python ≥ 3.8), ou `uv add --dev mkdocs`
- Point d'entrée — `mkdocs new .`, puis `mkdocs serve` pour prévisualiser et `mkdocs build` pour produire le dossier `site/`
- Prérequis — Python ; un thème tiers (Material for MkDocs, en maintenance depuis 2025-11-05) pour un rendu moderne
- Exécution — sur le poste et en CI ; le site produit est statique, rien à héberger côté serveur applicatif
- Coût — gratuit, BSD-2-Clause

## Écosystème

### Alternatives

- [[Sphinx]] — Outil en ligne de commande (BSD-2-Clause, Python) : générateur de documentation écrit en reStructuredText, qui sort HTML, PDF, EPUB et pages de manuel avec renvois sémantiques et index automatiques — le Markdown passe par l'extension MyST-Parser.
- [[Docusaurus]] — Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions et composants MDX — il demande Node et son écosystème.
- [[Zensical]] — Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — encore en versions 0.0.x, avec des remplaçants de plugins MkDocs en cours d'écriture.

### Compléments

- [[mkdocstrings]] — Plugin MkDocs (ISC, Python) : génère la documentation d'API depuis les docstrings et le code source par une simple balise ::: dans le Markdown, avec renvois entre pages et entre projets — un gestionnaire par langage, celui de Python étant le plus employé. — plugin MkDocs : l'identifiant d'un objet Python (`::: paquet.module.Classe`) placé dans une page Markdown est remplacé par sa documentation.

## Ressources

- Documentation — https://www.mkdocs.org/
- Dépôt — https://github.com/mkdocs/mkdocs
- Article — discussions du dépôt citées : https://github.com/mkdocs/mkdocs/discussions/4063, /4077 et /4089
- Article — avis de l'équipe Material, partie prenante : https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — ce qu'il faut écrire, et comment le garder à jour
- [[Comparatif - Générateurs de documentation]] — ce qui départage les générateurs du dossier
- [[Outils de développement]] — le hub du domaine
