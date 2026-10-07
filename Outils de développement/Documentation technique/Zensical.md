---
role: brique
nom: Zensical
alias: [zensical, Material for MkDocs 2]
pitch: "Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — encore en versions 0.0.x, avec des remplaçants de plugins MkDocs en cours d'écriture."
categorie: devtools/documentation
famille: cli
licence_type: open-source
maturite: beta
langage: Rust
alternatives: ["[[MkDocs]]", "[[Sphinx]]", "[[Docusaurus]]"]
complements: ["[[mkdocstrings]]"]
tags: [documentation]
url_docs: https://zensical.org/docs/
url_repo: https://github.com/zensical/zensical
---

# Zensical

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de sites statiques de documentation, écrit en **Rust et Python** et publié comme paquet Python (`pip install zensical`, Python ≥ 3.11). Il est construit par les auteurs de Material for MkDocs, dont il prend les principes : tout inclus, simple à démarrer, très personnalisable. Son point fort est la **reprise de l'existant** : il construit un projet [[MkDocs]] sans le modifier (même `mkdocs.yml`, même arborescence, Python Markdown et ses extensions), accepte les réglages de Material for MkDocs et fournit une variante « classique » du thème qui en garde l'apparence. Les commandes ont la même forme (`serve`, `build`), avec quelques différences.

**État le 2026-10-07 — à lire avant de s'y engager :**

- Versions **0.0.x** : 0.0.68 publiée le 2026-10-05. Une bannière du site annonce le lancement de la 0.1.0 pour un 5 novembre. Dépôt actif (dernier commit le 2026-10-07).
- Les **plugins MkDocs** ne sont pas tous repris : l'équipe écrit des remplaçants pour les plus populaires. Déjà disponibles d'après la feuille de route : blog, rss, social, exclude ; en cours : optimize. Un plugin hors de cette liste ne fonctionne pas forcément. La documentation d'API passe par [[mkdocstrings]], que la feuille de route dit déjà pris en charge.
- Mode lien symbolique de uv non pris en charge (limite connue dans la documentation d'installation).
- **Modèle économique** : le générateur est sous licence MIT (fichier `LICENSE.md` lu), « gratuit pour toujours » selon le dépôt. L'éditeur, Zensical LLC, propose à côté deux produits **optionnels et payants ou sur adhésion** : Zensical Studio (environnement de rédaction) et Zensical Spark (accès anticipé à des fonctions, assistance). Des fonctions de la feuille de route sont d'abord réservées aux membres de Spark. Ces produits ne sont pas fichés ici.

Pourquoi il existe : l'équipe de Material for MkDocs a annoncé le 2025-11-05 que ce thème entrait en **maintenance** (correctifs critiques et de sécurité seulement), puis a repoussé la fin de ce support au **2027-05-05**. Elle juge MkDocs 1.x non maintenu et la version 2 de MkDocs risquée pour les sites existants — avis d'une partie prenante, voir la fiche [[MkDocs]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Site MkDocs ou Material for MkDocs existant, avec une issue de secours à préparer avant 2027-05-05 | Site de production dépendant de plugins MkDocs sans remplaçant annoncé : tester la construction sur une copie avant de décider |
| Nouveau site Markdown en Python, avec un outil dont l'équipe est active | Besoin de sortie PDF ou EPUB native : prévu à la feuille de route, absent aujourd'hui → [[Sphinx]] |
| Reprise sans réécriture d'un `mkdocs.yml`, avec [[mkdocstrings]] pour l'API | Intolérance à une version 0.0.x : l'API de configuration et les plugins peuvent encore bouger |
| Rendu moderne sans chaîne Node | Composants React, blog, versions et langues intégrés dès maintenant → [[Docusaurus]] |

## Mise en œuvre

- Installation — `uv add --dev zensical` (ou `pip install zensical` dans un environnement virtuel) ; image Docker officielle pour la prévisualisation et la construction
- Point d'entrée — `zensical new`, puis `zensical serve` et `zensical build` (sur un projet MkDocs : la même arborescence)
- Prérequis — Python ≥ 3.11 ; un `mkdocs.yml` existant se réutilise tel quel
- Exécution — sur le poste et en CI ; site statique, rien à héberger côté serveur
- Coût — gratuit, MIT ; Studio et Spark en option payante

## Écosystème

### Alternatives

- [[MkDocs]] — Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version stable depuis 2024-08 ni commit depuis 2025-10.
- [[Sphinx]] — Outil en ligne de commande (BSD-2-Clause, Python) : générateur de documentation écrit en reStructuredText, qui sort HTML, PDF, EPUB et pages de manuel avec renvois sémantiques et index automatiques — le Markdown passe par l'extension MyST-Parser.
- [[Docusaurus]] — Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions et composants MDX — il demande Node et son écosystème.

### Compléments

- [[mkdocstrings]] — Plugin MkDocs (ISC, Python) : génère la documentation d'API depuis les docstrings et le code source par une simple balise ::: dans le Markdown, avec renvois entre pages et entre projets — un gestionnaire par langage, celui de Python étant le plus employé. — pris en charge selon la feuille de route de Zensical.

## Ressources

- Documentation — https://zensical.org/docs/
- Dépôt — https://github.com/zensical/zensical
- Compatibilité avec MkDocs — https://zensical.org/docs/compatibility/mkdocs/
- Feuille de route — https://zensical.org/roadmap/
- Annonce de la maintenance de Material for MkDocs — https://github.com/squidfunk/mkdocs-material/issues/8523

## Voir aussi

- [[Documentation technique]] — le hub du sous-domaine
- [[Diátaxis et docs-as-code]] — ce qu'il faut écrire, et comment le garder à jour
- [[Comparatif - Générateurs de documentation]] — ce qui départage les générateurs du dossier
- [[Outils de développement]] — le hub du domaine
