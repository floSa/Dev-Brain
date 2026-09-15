---
role: brique
nom: pypdf
alias: [PyPDF2, py-pdf]
pitch: "Bibliothèque Python pure sous BSD-3 pour lire, fusionner, découper, chiffrer, annoter et remplir des PDF, avec extraction de texte (modes plain et layout) ; aucune dépendance obligatoire, ni OCR ni rendu d'image."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyMuPDF]]", "[[pdfplumber]]", "[[pypdfium2]]", "[[pdfminer.six]]"]
complements: []
tags: [pdf, document-parsing]
url_docs: https://pypdf.readthedocs.io/
url_repo: https://github.com/py-pdf/pypdf
---

# pypdf

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python pure sous BSD-3 pour lire, fusionner, découper, chiffrer, annoter et remplir des PDF, avec extraction de texte (modes plain et layout) ; aucune dépendance obligatoire, ni OCR ni rendu d'image.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque **Python pure**, héritière de pyPdf (2005) et de son fork PyPDF2, que Martin Thoma a
repris en 2022 avant de la renommer `pypdf`. Elle est d'abord un outil de **manipulation** :
fusion, découpe, recadrage et rotation de pages, chiffrement et déchiffrement, métadonnées,
signets, pièces jointes, annotations, remplissage et aplatissement de formulaires, extraction
d'images. L'**extraction de texte** en est une fonction parmi d'autres, en deux modes : `plain`
par défaut, et `layout`, que la doc signale expérimental. Elle n'a **aucune dépendance
obligatoire**, ce qui en fait la plus simple à embarquer. La doc est franche sur ses bornes : « pypdf
is not OCR software », et une page faite d'une seule image rend un texte vide ou presque.

*Constat du 2026-09-30 :* dernière version 6.19.0, publiée le 2026-09-16, avec une release toutes
les une à deux semaines, surtout du durcissement face aux PDF malformés ; environ 10,2 k étoiles
GitHub, dernier push le 2026-09-29. Dans le banc `py-pdf/benchmarks`, publié par l'organisation
qui maintient pypdf, sur 14 PDF natifs et pour des versions de mi-2025, l'extraction de texte
de pypdf prend 3,5 s en moyenne pour 96 % de qualité, contre 0,1 s pour PyMuPDF et pypdfium2.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Manipuler des PDF — fusionner, découper, chiffrer, remplir des formulaires — sans dépendance ni licence copyleft | Extraction de texte sur gros volume : environ trente-cinq fois plus lent que PyMuPDF et pypdfium2 dans le banc de ses propres mainteneurs → [[PyMuPDF]] (AGPL) ou [[pypdfium2]] |
| Extraire le texte de PDF natifs simples, en pur Python, dans une image Docker minimale | PDF scanné : aucune prise en charge de l'OCR → [[Tesseract]], [[docTR]] ou [[PaddleOCR]] |
| Licence BSD-3, sans la clause réseau de l'AGPL de [[PyMuPDF]] | Tableaux, ordre de lecture, positions fiables : le mode `layout` est expérimental et les coordonnées peuvent être fausses sur des PDF complexes → [[pdfplumber]] |
| Durcissement : les versions récentes corrigent surtout des cas de PDF malformés, de boucles infinies et de limites de taille | Rendu de page en image : hors périmètre → [[pypdfium2]] ou [[PyMuPDF]] |
| | Champs XFA non gérés, polices non modifiables, environ 10 Go de RAM observés pour un flux de 300 Mo |

## Mise en œuvre

- Installation — `pip install pypdf` ; extras `[crypto]` (AES), `[image]` (Pillow), `[full]` ; JBIG2 demande le paquet système `jbig2dec`
- Point d'entrée — API Python : `PdfReader`, `PdfWriter`, puis `page.extract_text()`
- Prérequis — Python 3.9 ou plus ; aucune dépendance obligatoire hors `typing_extensions` avant Python 3.11
- Exécution — en process, mono-nœud, sans binaire système
- Coût — gratuit, BSD-3-Clause

## Écosystème

### Alternatives

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[pypdfium2]] — Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page.
- [[pdfminer.six]] — Bibliothèque Python pure sous MIT qui analyse la mise en page d'un PDF (caractères, mots, lignes, boîtes via LAParams) et en extrait texte et positions ; base de pdfplumber, lecture seule, sans OCR, lente et à maintenance ralentie.

## Ressources

- Documentation — https://pypdf.readthedocs.io/
- Documentation — https://pypdf.readthedocs.io/en/stable/user/extract-text.html
- Dépôt — https://github.com/py-pdf/pypdf
- Article — https://github.com/py-pdf/benchmarks (banc des mainteneurs : vitesse et qualité d'extraction de texte, PDF natifs seulement)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
