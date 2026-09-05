---
role: brique
nom: PyMuPDF
alias: [pymupdf, fitz, MuPDF]
pitch: "Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: C / Python
alternatives: ["[[pdfplumber]]", "[[pdf-inspector]]"]
complements: ["[[Docling]]", "[[Marker]]", "[[Unstructured]]", "[[OpenDataLoader PDF]]"]
tags: [pdf, document-parsing]
url_docs: https://pymupdf.readthedocs.io/
url_repo: https://github.com/pymupdf/PyMuPDF
---

# PyMuPDF

<!-- AUTO:BANDEAU:START -->
> Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C / Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Binding Python de **MuPDF**, le moteur C de rendu et d'analyse de documents d'Artifex —
importé `pymupdf`, alias historique `fitz`. C'est la **référence de vitesse** de l'écosystème
Python : extraction de texte, d'images, de tableaux, d'annotations, de champs de formulaire et
de métadonnées, rendu en image, et surtout un **accès bas niveau au modèle objet PDF** —
blocs, spans, coordonnées — sur lequel bâtir son propre pipeline de parsing. Il gère aussi
XPS, EPUB et CBZ. Sa vraie frontière n'est pas technique mais juridique : c'est le seul du
dossier dont l'usage libre est conditionné par une licence à double détente.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire vite du texte et des images d'un gros volume de PDF | AGPL-3.0 : un service réseau ou un produit fermé déclenche l'obligation de divulgation du code, sinon la licence commerciale Artifex, payante — le piège juridique du SaaS |
| Manipuler le PDF : découper, fusionner, caviarder, annoter, rendre en image, lire les formulaires | Double nommage de l'API, `fitz` puis `pymupdf` selon les versions |
| Accès fin aux objets — blocs, spans, coordonnées — pour bâtir son propre pipeline de parsing | Extraction de tableaux moins fine que celle d'un outil spécialisé sur les mises en page tordues |

## Mise en œuvre

- Installation — `pip install pymupdf`, roues précompilées embarquant MuPDF
- Point d'entrée — API Python `pymupdf` (alias historique `fitz`) : le document, la page, puis le modèle objet PDF
- Prérequis — aucune dépendance système
- Exécution — en process, mono-nœud ; extrêmement rapide et léger
- Coût — gratuit sous AGPL-3.0 ; licence commerciale Artifex, payante, pour les usages propriétaires

## Écosystème

### Alternatives

- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.

### Compléments

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local. — l'étage de conversion structurée, en aval de l'extraction brute.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte. — l'autre étage de conversion structurée, quand un GPU est disponible.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG. — le pipeline d'ingestion qui appelle l'extraction brute.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA. — l'étage d'analyse de mise en page au-dessus de l'extraction brute.

## Ressources

- Documentation — https://pymupdf.readthedocs.io/
- Dépôt — https://github.com/pymupdf/PyMuPDF

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
