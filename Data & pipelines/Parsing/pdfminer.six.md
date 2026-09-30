---
role: brique
nom: pdfminer.six
alias: [pdfminer, pdfminer six]
pitch: "Bibliothèque Python pure sous MIT qui analyse la mise en page d'un PDF (caractères, mots, lignes, boîtes via LAParams) et en extrait texte et positions ; base de pdfplumber, lecture seule, sans OCR, lente et à maintenance ralentie."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[pypdf]]", "[[PyMuPDF]]", "[[pypdfium2]]"]
complements: ["[[pdfplumber]]"]
tags: [pdf, document-parsing, layout-analysis]
url_docs: https://pdfminersix.readthedocs.io/
url_repo: https://github.com/pdfminer/pdfminer.six
---

# pdfminer.six

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python pure sous MIT qui analyse la mise en page d'un PDF (caractères, mots, lignes, boîtes via LAParams) et en extrait texte et positions ; base de pdfplumber, lecture seule, sans OCR, lente et à maintenance ralentie.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Fork maintenu par la communauté de PDFMiner, l'ancien outil de Yusuke Shinyama. Il **convertit
les objets d'un PDF en objets Python** puis en reconstruit la structure : l'**analyse de mise en
page** regroupe les caractères en mots et en lignes, les lignes en boîtes, les boîtes en
hiérarchie, selon les paramètres de `LAParams` (`char_margin`, `line_margin`, `word_margin`,
`detect_vertical`). Il rend le texte avec sa position, sa police et sa couleur, extrait images,
table des matières et formulaires AcroForm, et gère le texte vertical et les polices CJK. La doc
reconnaît la limite de l'exercice : les caractères d'un paragraphe ne se distinguent pas de ceux
d'un tableau ou d'un pied de page, le regroupement est donc **heuristique**. Il ne lit que, n'écrit
pas de PDF, et ne fait pas d'OCR. C'est la couche sur laquelle repose [[pdfplumber]].

*Constat du 2026-09-30 :* dernière version 20260107, publiée le 2026-01-07, qui corrige
CVE-2025-64512 (exécution de code arbitraire par désérialisation pickle des CMap, remplacée par
du JSON) ; environ 7 k étoiles GitHub, dernier commit le 2026-03-13, aucune release depuis neuf
mois. Dans le banc `py-pdf/benchmarks`, publié par les mainteneurs de [[pypdf]] et pour des
versions de mi-2025, il prend 5,8 s en moyenne pour 89 % de qualité d'extraction de texte.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Accéder à la géométrie et à la hiérarchie de mise en page d'un PDF natif : boîtes, lignes, positions, polices | Lent : 5,8 s en moyenne dans le banc des mainteneurs de pypdf, contre 0,1 s pour [[PyMuPDF]] et [[pypdfium2]] |
| Pur Python sous MIT, sans binaire système, avec une CLI `pdf2txt.py` et `dumppdf.py` pour inspecter un fichier | Maintenance ralentie : « community maintained », mainteneurs peu disponibles, aucune release depuis janvier 2026 |
| Base d'une extraction sur mesure : c'est la couche que [[pdfplumber]] enveloppe | Pas de tableaux en tant que tels, pas d'OCR : inopérant sur du scanné → [[pdfplumber]] pour les tableaux, [[Tesseract]] pour le scan |
| Texte vertical et polices CJK gérés | Certains PDF n'ont pas de table Unicode complète et rendent des identifiants de caractères au lieu du texte : à tester par copier-coller dans un lecteur |
| | Lecture seule : aucune modification de PDF → [[pypdf]] |

## Mise en œuvre

- Installation — `pip install pdfminer.six`
- Point d'entrée — `from pdfminer.high_level import extract_text` ; `extract_pages` pour les objets de mise en page ; commande `pdf2txt.py` pour un usage occasionnel
- Prérequis — Python 3.10 ou plus ; `charset-normalizer` et `cryptography` en dépendances, Pillow en option pour les images
- Exécution — en process, mono-nœud, sans binaire système
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[pypdf]] — Bibliothèque Python pure sous BSD-3 pour lire, fusionner, découper, chiffrer, annoter et remplir des PDF, avec extraction de texte (modes plain et layout) ; aucune dépendance obligatoire, ni OCR ni rendu d'image.
- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pypdfium2]] — Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page.

### Compléments

- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT. — la couche au-dessus, qui ajoute les tableaux et le débogage visuel.

## Ressources

- Documentation — https://pdfminersix.readthedocs.io/
- Dépôt — https://github.com/pdfminer/pdfminer.six
- Article — https://github.com/py-pdf/benchmarks (banc des mainteneurs de pypdf : vitesse et qualité d'extraction de texte, PDF natifs seulement)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
