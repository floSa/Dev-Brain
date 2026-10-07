---
role: brique
nom: Sphinx
alias: [sphinx-doc, sphinx-build, reStructuredText]
pitch: "Outil en ligne de commande (BSD-2-Clause, Python) : générateur de documentation écrit en reStructuredText, qui sort HTML, PDF, EPUB et pages de manuel avec renvois sémantiques et index automatiques — le Markdown passe par l'extension MyST-Parser."
categorie: devtools/documentation
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[MkDocs]]", "[[Docusaurus]]", "[[Zensical]]"]
complements: []
tags: [documentation]
url_docs: https://www.sphinx-doc.org/
url_repo: https://github.com/sphinx-doc/sphinx
---

# Sphinx

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de documentation vieux de près de vingt ans (copyright de l'équipe depuis 2007), très employé pour les bibliothèques Python. Les sources sont en **reStructuredText**, analysé par Docutils ; Sphinx y ajoute des renvois **sémantiques** (vers une fonction, une classe, un terme de glossaire) liés automatiquement, une arborescence de documents, un index général et un index de modules, et la coloration du code par Pygments. La même source produit **HTML, PDF, texte, EPUB, TeX et pages de manuel**, ce que les autres générateurs du dossier ne proposent pas nativement aujourd'hui (la sortie PDF figure sur la feuille de route de [[Zensical]], pas dans ses versions).

L'écosystème d'extensions fait l'essentiel de sa force : `autodoc` documente un module depuis ses docstrings, `intersphinx` renvoie vers l'inventaire d'un autre projet, d'autres extensions gèrent C, C++, JavaScript, les mathématiques ou les notebooks Jupyter. Le Markdown n'est pas natif : Sphinx s'appuie sur **MyST-Parser** (`pip install myst-parser`, puis `myst_parser` dans la liste `extensions`), qui lit la variante CommonMark.

Version 9.1.0 du 2025-12-31 (Python ≥ 3.12), dernier commit le 2026-10-05, licence BSD-2-Clause lue dans le fichier `LICENSE.rst` du dépôt (le champ de licence détecté par GitHub reste « non déterminé » parce que ce fichier mêle plusieurs notices ; le texte principal est bien la BSD à deux clauses). Environ 8,1 k étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Documentation d'une bibliothèque Python avec référence d'API complète (`autodoc`) et renvois vers d'autres projets (`intersphinx`) | Équipe qui écrit en Markdown et veut un site en dix minutes → [[MkDocs]] ou [[Zensical]] |
| Livrable en **PDF**, EPUB ou page de manuel en plus du HTML | Site vitrine avec blog, composants React ou traductions pilotées par la plateforme → [[Docusaurus]] |
| Projet multi-langage (C, C++, JavaScript) documenté dans un même ensemble | Syntaxe à apprendre : reStructuredText est plus strict que Markdown, et le Markdown reste un ajout (MyST) |
| Écosystème de thèmes et d'extensions éprouvé depuis des années | Python ≥ 3.12 exigé par la version 9.1 : un environnement ancien se cale sur une version plus ancienne de Sphinx |

## Mise en œuvre

- Installation — `uv add --dev sphinx` (ou `pip install -U sphinx`)
- Point d'entrée — `sphinx-quickstart` crée `conf.py` et `index.rst` ; `sphinx-build -b html docs docs/_build` construit le site
- Prérequis — Python ≥ 3.12 pour la 9.1 ; LaTeX pour la sortie PDF par TeX
- Exécution — sur le poste et en CI ; site statique, rien à héberger côté serveur
- Coût — gratuit, BSD-2-Clause

## Écosystème

### Alternatives

- [[MkDocs]] — Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10.
- [[Docusaurus]] — Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions et composants MDX — il demande Node et son écosystème.
- [[Zensical]] — Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — encore en versions 0.0.x, avec des remplaçants de plugins MkDocs en cours d'écriture.

## Ressources

- Documentation — https://www.sphinx-doc.org/
- Dépôt — https://github.com/sphinx-doc/sphinx
- Markdown avec Sphinx — https://www.sphinx-doc.org/en/master/usage/markdown.html

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — ce qu'il faut écrire, et comment le garder à jour
- [[Comparatif - Générateurs de documentation]] — ce qui départage les générateurs du dossier
- [[Outils de développement]] — le hub du domaine
