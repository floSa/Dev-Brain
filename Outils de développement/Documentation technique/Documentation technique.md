---
role: hub
nom: Documentation technique
alias: [documentation de projet, générateurs de documentation, docs-as-code, static site generator documentation]
pitch: Documenter un projet logiciel dans son dépôt — quoi écrire, et avec quel générateur fabriquer et publier le site.
domaines: [data-sci, data-eng, mlops, ml-eng, ai-eng]
tags: [documentation]
---

# Documentation technique

> Documenter un projet logiciel dans son dépôt — quoi écrire, et avec quel générateur fabriquer et publier le site.

## Ce qu'il faut comprendre

- Deux questions, qui ne se confondent pas. **Quoi écrire** : la réponse est une méthode, [[Diátaxis et docs-as-code]] — quatre types de pages (tutoriel, guide pratique, référence, explication), écrits avec les outils du code. **Avec quoi le fabriquer** : un générateur de site statique, qui lit des fichiers texte et produit un site publiable sur n'importe quel serveur de fichiers.
- Le choix du générateur se joue d'abord sur le **langage d'écriture** et la **chaîne technique** : Markdown et Python pour [[MkDocs]] et [[Zensical]], reStructuredText (et Markdown par une extension) pour [[Sphinx]], Markdown et MDX sur Node et React pour [[Docusaurus]].
- La **référence d'API** se génère : [[mkdocstrings]] la tire des docstrings dans un site MkDocs ou Zensical ; `autodoc` fait de même côté Sphinx. C'est la partie de la documentation qui ne doit jamais s'écrire à la main.
- **La santé du projet compte plus que d'habitude en 2026.** [[MkDocs]] n'a plus de version stable depuis 2024-08 ni de commit depuis 2025-10 ; l'équipe du thème Material, qui l'a rendu populaire, a basculé vers [[Zensical]], encore en versions 0.0.x, et prolongé le support de Material jusqu'au 2027-05-05. Les deux fiches donnent les dates.
- Les schémas qui illustrent la documentation relèvent d'un autre sous-domaine : [[Diagrammes]] ([[Mermaid]] est rendu nativement ; [[LikeC4]] tient un modèle d'architecture en code). La conduite du projet qui produit cette documentation est dans [[Gestion de projet]].

## Choisir

- Savoir quoi écrire et comment ranger les pages → [[Diátaxis et docs-as-code]].
- Un site simple en Markdown, existant et fonctionnel → rester sur [[MkDocs]], en préparant la suite ; nouveau site Markdown → [[Zensical]] si les plugins nécessaires sont repris.
- Une bibliothèque Python avec une référence d'API fournie, ou une sortie PDF → [[Sphinx]].
- Un site de produit avec blog, versions et traductions → [[Docusaurus]].
- La référence d'API Python générée depuis le code, dans un site MkDocs → [[mkdocstrings]].
- Le détail de ce qui départage les générateurs → [[Comparatif - Générateurs de documentation]].

<!-- AUTO:START -->
<!-- AUTO:END -->
