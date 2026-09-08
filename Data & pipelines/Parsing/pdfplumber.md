---
role: brique
nom: pdfplumber
alias: [pdfplumber, jsvine-pdfplumber]
pitch: "Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyMuPDF]]", "[[pdf-inspector]]"]
complements: ["[[Docling]]", "[[Unstructured]]", "[[OpenDataLoader PDF]]"]
tags: [pdf, table-extraction, document-parsing]
url_docs: https://github.com/jsvine/pdfplumber
url_repo: https://github.com/jsvine/pdfplumber
---

# pdfplumber

<!-- AUTO:BANDEAU:START -->
> Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-15 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bâti sur **pdfminer.six**, pdfplumber expose pour chaque page un **accès détaillé à chaque
objet** — caractères, lignes, rectangles, courbes — avec ses coordonnées. Au-dessus de cette
couche, des méthodes de haut niveau extraient le texte et surtout les **tableaux**, avec des
stratégies de détection configurables — lignes explicites contre alignement de texte — et un
**débogage visuel** qui rend la page avec les objets et les tableaux détectés. Pur Python,
sans binaire système ni contrainte de licence. Il n'embarque aucun OCR : son terrain est le
PDF **natif**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraction de tableaux de PDF natifs avec réglage fin : stratégies, tolérances | Pas d'OCR : inopérant sur des PDF scannés |
| Contrôle précis sur la position des objets — coordonnées, géométrie | Nettement plus lent que les moteurs C sur de gros volumes |
| Débogage visuel pour comprendre une mise en page récalcitrante | L'extraction de tableaux demande souvent du tuning : stratégies `lines` ou `text`, tolérances |
| Pur Python, sans binaire système ni contrainte de licence | |

## Mise en œuvre

- Installation — `pip install pdfplumber`
- Point d'entrée — API Python : la page et ses objets géométriques, l'extraction de texte et de tableaux, le rendu de débogage
- Prérequis — Python ; pdfminer.six en dépendance, aucune dépendance système
- Exécution — en process, mono-nœud ; léger, mais plus lent que les moteurs C
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.

### Compléments

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local. — l'étage de conversion structurée, en aval de l'extraction brute.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG. — le pipeline d'ingestion qui appelle l'extraction brute.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA. — l'étage d'analyse de mise en page au-dessus de l'extraction brute.

## Ressources

- Documentation — https://github.com/jsvine/pdfplumber
- Dépôt — https://github.com/jsvine/pdfplumber

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
