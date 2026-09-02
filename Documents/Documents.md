---
role: hub
nom: Documents
alias: [documents, pdf]
pitch: Manipuler des documents comme des documents — un PDF qu'on découpe, une page web qu'on rapatrie en Markdown.
domaines: [data-eng]
tags: [pdf, markdown-conversion, ocr, web-scraping]
---

# Documents

> Manipuler des documents comme des documents — un PDF qu'on découpe, une page web qu'on rapatrie en Markdown.

## Ce qu'il faut comprendre

- Deux briques, deux gestes, et un point commun : elles traitent le **document entier**, pas son contenu structuré. Découper un PDF, en tourner les pages, l'OCRiser ([[Stirling PDF]]) ; ramener une page web en Markdown lisible ([[Page to Markdown]]).
- La frontière avec le **parsing** est ce qu'il faut tenir. Extraire les tableaux d'un PDF pour les charger dans un pipeline est un problème de parsing de documents, et ses briques sont dans « Data & pipelines » — voir [[Comparatif - Parsing de documents]]. Ici, on transforme un document en un autre document.
- Le geste de [[Page to Markdown]] mérite d'être vu pour ce qu'il est : la **capture manuelle** d'une source, à un lien à la fois. C'est ce dont on a besoin pour alimenter un brain ou un corpus d'un article lu ; ce n'est pas du [[Web scraping]], qui automatise et passe à l'échelle.
- [[Stirling PDF]] s'auto-héberge, et c'est l'argument : la manipulation de PDF est exactement le cas où l'on ne veut pas déposer le document sur un service en ligne — contrats, pièces d'identité, dossiers clients.

## Choisir

- Fusionner, découper, convertir, OCRiser un PDF, sans l'envoyer ailleurs → [[Stirling PDF]].
- Rapatrier une page web en Markdown propre depuis le navigateur → [[Page to Markdown]].
- Extraire le contenu structuré d'un document pour un pipeline → « Data & pipelines », pas ce domaine.

<!-- AUTO:START -->
### Briques
- [[Page to Markdown]] — Extension Chrome qui convertit une page web ou une sélection en Markdown propre, entièrement dans le navigateur, avec copie au presse-papiers ou téléchargement .md.
- [[Stirling PDF]] — Plateforme PDF web auto-hébergeable au cœur MIT : plus de 50 opérations (fusion, découpe, rotation, conversion, OCR, signature, rédaction, compression) exécutées sur son propre serveur, avec API REST et pipelines no-code ; SSO, audit et déploiement air-gapped réservés aux modules propriétaires.
<!-- AUTO:END -->
