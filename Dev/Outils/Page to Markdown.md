---
role: brique
nom: Page to Markdown
alias: [page-to-markdown, page to markdown by starterbuild]
pitch: "Extension Chrome qui convertit une page web ou une sélection en Markdown propre, entièrement dans le navigateur, avec copie au presse-papiers ou téléchargement .md."
categorie: docs/capture
famille: extension
domaines: [ai-eng]
licence_type: proprietary
os: "Chrome (Windows, macOS, Linux, ChromeOS)"
langage: 
alternatives: []
complements: []
tags: [browser-extension, markdown-conversion, note-taking, privacy]
url_docs: https://starterbuild.com/page-to-markdown/
url_repo: 
---

# Page to Markdown

## Pourquoi

Geste à l'unité : une page de documentation lue dans le navigateur, un thread, un article — récupérés en Markdown structuré en deux clics, pour les coller dans un prompt, une note Obsidian ou une doc de projet. Le copier-coller brut d'un navigateur perd la hiérarchie de titres, casse les blocs de code et embarque la navigation du site ; c'est ce trou que l'extension comble.

L'éditeur (StarterBuild) annonce trois modes : page nettoyée (la navigation et l'habillage sont retirés), page complète, et sélection seule — accessible aussi par le menu contextuel. La conversion préserve titres, liens, images, listes, citations, tableaux, blocs de code délimités et blocs dépliants (`details`). Sortie au choix : presse-papiers ou fichier `.md`.

Point qui compte pour un usage professionnel : **la conversion s'exécute localement dans Chrome**. L'éditeur déclare que le contenu de la page n'est envoyé ni à StarterBuild ni à un tiers. Déclaration non vérifiable de l'extérieur, l'extension n'étant pas open-source — à peser selon la sensibilité des pages consultées.

Utile comme complément d'un pipeline d'ingestion : ce que le scraping programmatique fait à l'échelle, cette extension le fait sur la page qu'on a déjà sous les yeux.

## Quand l'utiliser

- Nourrir un prompt ou un contexte LLM avec une page de doc, en gardant la structure exploitable.
- Alimenter des notes ou un wiki personnel à partir de lectures ponctuelles.
- Récupérer un extrait de page — un tableau, un bloc de code — sans passer par un script.
- Contexte où le contenu de la page ne doit pas transiter par un service distant (sous réserve de faire confiance à la déclaration de l'éditeur).

## Quand NE PAS l'utiliser

- Extraction à l'échelle, planifiée ou automatisée sur des milliers d'URL → [[Dev/Services/Firecrawl|Firecrawl]], [[Dev/Services/Maxun|Maxun]].
- Conversion de PDF ou de documents bureautiques : hors périmètre, c'est une extension de navigateur → [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]], [[Dev/Services/Docling|Docling]].
- Exigence de code auditable ou d'auto-hébergement : l'extension est propriétaire et sans dépôt public.
- Navigateur autre que Chrome : seul Chrome est annoncé.

## Installation & plateformes

- Installation depuis le Chrome Web Store (identifiant `abpdjempcbodkeajhfhblcajghbgbdae`), présentation et lien sur `starterbuild.com/page-to-markdown/`.
- Gratuite. Aucun compte ni clé d'API annoncés.
- Chrome uniquement d'après l'éditeur ; la compatibilité avec les autres navigateurs Chromium (Edge, Brave, Vivaldi) n'est pas documentée.
- Aucune version Firefox ou Safari annoncée. Pas de code source publié, donc pas de build maison possible.

## Pièges

- **Extension propriétaire sans dépôt** : le « tout local » repose sur la parole de l'éditeur. Sur des pages internes ou sous authentification, vérifier les permissions demandées dans le Chrome Web Store avant d'installer.
- Une extension gratuite d'un petit éditeur peut changer de modèle économique ou de mainteneur : ne pas en faire une dépendance de production.
- Le mode « page nettoyée » applique une heuristique : sur des mises en page atypiques, il peut retirer du contenu utile. Comparer avec le mode page complète en cas de doute.
- Les pages entièrement rendues côté client peuvent être capturées incomplètement si la conversion a lieu avant la fin du chargement.
- Nombre d'utilisateurs, note et date de dernière mise à jour non vérifiés : la fiche du Chrome Web Store n'a pas pu être consultée.

## Alternatives

Aucune autre page de la catégorie `tooling/capture` dans le brain à ce jour. Le voisinage fonctionnel est ailleurs : le scraping programmatique dans `data/scraping`, et le parsing de documents dans `data/parsing`.

## Liens

- [[Dev/Services/Firecrawl|Firecrawl]] — équivalent programmatique et à l'échelle, côté scraping web.
- [[Comparatif - Scraping]] — comparatif de la famille scraping.
- [[Comparatif - Parsing de documents]] — comparatif de la famille parsing, pour les documents plutôt que les pages web.
- Site : https://starterbuild.com/page-to-markdown/
