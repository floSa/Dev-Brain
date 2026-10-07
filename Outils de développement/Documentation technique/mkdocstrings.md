---
role: brique
nom: mkdocstrings
alias: [mkdocstrings-python, mkdocs-strings]
pitch: "Plugin MkDocs (ISC, Python) : génère la documentation d'API depuis les docstrings et le code source par une simple balise ::: dans le Markdown, avec renvois entre pages et entre projets — un gestionnaire par langage, celui de Python étant le plus employé."
categorie: devtools/documentation
famille: extension
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[MkDocs]]", "[[Zensical]]"]
tags: [documentation]
url_docs: https://mkdocstrings.github.io/
url_repo: https://github.com/mkdocstrings/mkdocstrings
---

# mkdocstrings

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Plugin qui fabrique la **référence d'API** d'un projet à partir du code, au lieu de la recopier à la main. Dans une page Markdown, une ligne `::: paquet.module.Classe`, suivie au besoin d'un bloc YAML d'options à quatre espaces, est remplacée à la construction par la documentation de l'objet : signature, docstring, membres. Les docstrings écrites dans le code deviennent la page de référence, et celle-ci ne diverge plus du code — c'est la règle « la référence se génère » de [[Diátaxis et docs-as-code]].

Le paquet `mkdocstrings` ne comprend aucun langage : chaque langage a un **gestionnaire** (`handler`). Le dépôt cite C, Crystal, GitHub Actions, Python, MATLAB, TypeScript, VBA et le shell. Le gestionnaire Python s'installe avec `pip install 'mkdocstrings[python]'`. Versions relevées le 2026-10-07 : mkdocstrings 1.0.6 (2026-07-11) et mkdocstrings-python 2.0.9 (2026-09-22), toutes deux sous licence ISC, Python ≥ 3.10.

Fonctions que le dépôt met en avant : renvois d'une page à l'autre par `[identifiant][]`, renvois **vers d'autres projets** grâce à leur inventaire d'objets (le même principe que l'extension `intersphinx` de [[Sphinx]]), options globales dans `mkdocs.yml` ou locales à chaque balise, thème Material pris en charge ainsi que, plus sommairement, ceux de MkDocs et de Read the Docs pour le gestionnaire Python.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un paquet Python documenté par des docstrings, sur un site [[MkDocs]] ou [[Zensical]] | Site bâti sur [[Sphinx]] : son extension `autodoc` fait le même travail sans plugin supplémentaire |
| Une page de référence qui ne doit jamais diverger du code | Docstrings absentes ou pauvres : l'outil expose ce qu'elles contiennent, rien de plus |
| Renvois vers la documentation d'autres bibliothèques par inventaire | Pas de dépendance à MkDocs voulue : le plugin n'existe que dans cet écosystème |

## Mise en œuvre

- Installation — `uv add --dev "mkdocstrings[python]"`
- Point d'entrée — déclarer `mkdocstrings` dans la liste `plugins:` de `mkdocs.yml`, puis écrire `::: mon_paquet.mon_module` dans une page
- Prérequis — [[MkDocs]] (ou [[Zensical]], dont la feuille de route précise qu'il « supporte déjà » la documentation d'API par mkdocstrings) ; le paquet à documenter importable ou lisible
- Exécution — à la construction du site ; rien à héberger
- Coût — gratuit, ISC

## Écosystème

### Alternatives

- *Aucune alternative déclarée pour ce dossier.* L'équivalent côté [[Sphinx]] est une extension (`autodoc`), pas une brique à part.

### Compléments

- [[MkDocs]] — Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10. — c'est le programme hôte : sans lui, le plugin n'a rien à brancher.
- [[Zensical]] — Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — encore en versions 0.0.x, avec des remplaçants de plugins MkDocs en cours d'écriture. — sa feuille de route indique qu'il prend en charge la documentation d'API par mkdocstrings.

## Ressources

- Documentation — https://mkdocstrings.github.io/
- Dépôt — https://github.com/mkdocstrings/mkdocstrings

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — la référence se génère, le reste s'écrit
- [[Comparatif - Générateurs de documentation]] — ce qui départage les générateurs du dossier
- [[Outils de développement]] — le hub du domaine
