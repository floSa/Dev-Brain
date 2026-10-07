---
role: comparatif
nom: Comparatif - Générateurs de documentation
categorie: devtools/documentation
tags: [documentation]
---

# Comparatif - Générateurs de documentation

> On tranche sur : le **langage d'écriture** (Markdown, reStructuredText ou MDX), la **chaîne technique** exigée (Python, ou Node et React), la **référence d'API** générée depuis le code, et — en 2026 — la **santé du projet** : [[MkDocs]] n'a plus de commit depuis 2025-10, et son successeur [[Zensical]] n'est qu'en versions 0.0.x.

![[Comparatif - Générateurs de documentation.base]]

## Ce qui départage

- [[MkDocs]] — le plus simple : Markdown, un seul `mkdocs.yml`, un site statique en deux commandes. **Plus de version stable depuis 2024-08 ni de commit depuis 2025-10** ; une version 2 annoncée comme réécriture, un fork communautaire (ProperDocs) évoqué dans une discussion du dépôt. Utilisable pour un site existant, risqué pour un projet neuf.
- [[mkdocstrings]] — n'est **pas un générateur** mais le plugin qui lui manque : il produit la référence d'API depuis les docstrings par la balise `:::`. Il figure au tableau parce qu'il est de la même catégorie, mais il ne se compare pas aux autres lignes : il s'ajoute à [[MkDocs]] ou à [[Zensical]], et l'équivalent de [[Sphinx]] est son extension `autodoc`.
- [[Sphinx]] — le plus complet : reStructuredText, renvois sémantiques, `autodoc` et `intersphinx`, sorties HTML, PDF, EPUB et pages de manuel. Le Markdown passe par MyST-Parser. Python ≥ 3.12 pour la version 9.1 ; la syntaxe est la plus exigeante à apprendre.
- [[Docusaurus]] — le plus « site web » : application React monopage, MDX, blog, versions et traductions intégrés. Il exige Node ≥ 20 et un projet JavaScript à côté du code, et ne produit pas de PDF. À choisir pour un site de produit, pas pour la documentation interne d'un dépôt de données.
- [[Zensical]] — le **remplaçant annoncé** de Material for MkDocs, par la même équipe : lit les `mkdocs.yml` existants et garde l'apparence de Material. Versions 0.0.x (0.0.68 le 2026-10-05), plugins MkDocs repris en partie. Licence MIT ; l'éditeur vend à côté des produits optionnels (Studio, Spark), non fichés.
- *Non fichés, cités en texte simple* (dépôts relevés le 2026-10-07, tous actifs et non archivés ; aucun n'a été relu en détail pour ce comparatif). **VitePress** (MIT, générateur propulsé par Vite et Vue). **Starlight** (MIT, thème de documentation du framework Astro). **mdBook** (MPL-2.0, écrit en Rust : fabrique un livre depuis des fichiers Markdown). **pdoc** (MIT-0, référence d'API de projets Python).

## Choisir vite

- Une bibliothèque Python avec une référence d'API et peut-être un PDF → [[Sphinx]].
- Une documentation Markdown de dépôt, sur un site existant bâti avec [[MkDocs]] → le garder, préparer [[Zensical]] avant la fin du support de Material (2027-05-05).
- Un nouveau site de documentation Markdown à fonder maintenant → [[Zensical]] si les plugins nécessaires y sont repris, sinon [[Sphinx]] avec MyST.
- Un site de produit avec blog, versions et traductions → [[Docusaurus]].

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — quoi écrire, quel que soit l'outil
- [[Kroki]] — le serveur qui rend les diagrammes en texte (PlantUML, Mermaid, D2…) d'une documentation, sans installer chaque moteur ; il ne remplace aucun générateur ci-dessus.
- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
