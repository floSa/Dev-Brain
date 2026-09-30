---
role: brique
nom: pypdfium2
alias: [pypdfium, PDFium Python, pypdfium2-team]
pitch: "Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyMuPDF]]", "[[pypdf]]", "[[pdfminer.six]]"]
complements: ["[[Tesseract]]", "[[EasyOCR]]"]
tags: [pdf, document-parsing]
url_docs: https://pypdfium2.readthedocs.io/
url_repo: https://github.com/pypdfium2-team/pypdfium2
---

# pypdfium2

<!-- AUTO:BANDEAU:START -->
> Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Binding Python de **PDFium**, le moteur de rendu PDF de Chromium, appelé par ctypes. Il
**rend les pages en image** — bitmap convertible en Pillow, NumPy ou OpenCV —, extrait le texte
par page, par zone ou par plage de caractères, lit les objets de page (texte, images, tracés), la
table des matières, les métadonnées et les pièces jointes, et sait créer un document ou en
réordonner les pages. Une **CLI** `pypdfium2` couvre le rendu, l'extraction et la fusion. Les
roues précompilées embarquent PDFium : aucune dépendance système. Son README revendique d'être
l'une des rares bibliothèques Python de rendu PDF libres de tout copyleft fort. Il ne fait
**ni OCR ni analyse de mise en page** ; son rôle dans une chaîne OCR est de rendre la page en
image avant le moteur.

*Constat du 2026-09-30 :* dernière version 5.13.0, publiée le 2026-08-13 ; environ 830 étoiles
GitHub, dernier push le 2026-09-28, équipe de maintenance restreinte. Dans le banc
`py-pdf/benchmarks`, publié par les mainteneurs de [[pypdf]] et pour des versions de mi-2025,
il obtient le meilleur score d'extraction de texte, 97 %, à 0,1 s en moyenne — comme PyMuPDF.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rendre des pages PDF en image, vite, avant un OCR ou un modèle de vision | Pas thread-safe : aucun appel simultané entre threads, même sur des documents distincts ; il faut des processus ou des verrous |
| Extraction de texte rapide et de bonne qualité sur PDF natifs, sans la clause réseau de l'AGPL de [[PyMuPDF]] | Durée de vie des objets : un oubli de `close()` peut planter ou corrompre la mémoire avec le ramasse-miettes |
| Roues précompilées sur de très nombreuses plateformes, licence permissive | Aucun accès à la structure PDF brute, manipulation limitée → [[PyMuPDF]] ou [[pypdf]] |
| CLI pour convertir ou inspecter des PDF en shell | Ni tableaux, ni ordre de lecture, ni OCR → [[pdfplumber]], [[Docling]] ou [[Tesseract]] |
| | Interface « support model » encore en bêta, donc susceptible de changer |

## Mise en œuvre

- Installation — `python -m pip install -U pypdfium2`, roues précompilées embarquant PDFium ; Pillow, NumPy et OpenCV en option
- Point d'entrée — `import pypdfium2 as pdfium` puis `pdfium.PdfDocument(...)` ; commande `pypdfium2` avec `render`, `extract-text`, `extract-images`, `toc`, `arrange`
- Prérequis — aucune dépendance obligatoire ; Python 3 sur de très nombreuses plateformes
- Exécution — en process, mono-nœud, un thread à la fois
- Coût — gratuit ; binding sous Apache-2.0 ou BSD-3-Clause, PDFium sous licence de style BSD, avec les textes de licence des dépendances livrés dans les roues

## Écosystème

### Alternatives

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pypdf]] — Bibliothèque Python pure sous BSD-3 pour lire, fusionner, découper, chiffrer, annoter et remplir des PDF, avec extraction de texte (modes plain et layout) ; aucune dépendance obligatoire, ni OCR ni rendu d'image.
- [[pdfminer.six]] — Bibliothèque Python pure sous MIT qui analyse la mise en page d'un PDF (caractères, mots, lignes, boîtes via LAParams) et en extrait texte et positions ; base de pdfplumber, lecture seule, sans OCR, lente et à maintenance ralentie.

### Compléments

- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux. — un moteur qui lit des images : pypdfium2 rend la page en amont.
- [[EasyOCR]] — Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024. — idem, il lit des images, pas des PDF.

## Ressources

- Documentation — https://pypdfium2.readthedocs.io/
- Dépôt — https://github.com/pypdfium2-team/pypdfium2
- Article — https://github.com/py-pdf/benchmarks (banc des mainteneurs de pypdf : vitesse et qualité d'extraction de texte, PDF natifs seulement)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
