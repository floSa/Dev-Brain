---
role: brique
nom: pdf-inspector
alias: [firecrawl/pdf-inspector, pdf2md, detect-pdf]
pitch: "Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: beta
langage: Rust
alternatives: ["[[Dev/Services/PyMuPDF|PyMuPDF]]", "[[Dev/Services/pdfplumber|pdfplumber]]", "[[Dev/Services/Docling|Docling]]", "[[Dev/Services/Marker|Marker]]", "[[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]]"]
complements: []
tags: [pdf, document-parsing, ocr, markdown-conversion, layout-analysis]
url_docs: https://firecrawl.github.io/pdf-inspector/
url_repo: https://github.com/firecrawl/pdf-inspector
---

# pdf-inspector

## Pourquoi

Étage de **tri** en amont d'un pipeline documentaire. pdf-inspector classe un PDF en `TextBased`, `Scanned`, `ImageBased` ou `Mixed` en **10 à 50 ms** : il parse la xref et le page tree sans charger tous les objets, puis scanne les opérateurs `Tj`/`TJ` (texte) et `Do` (image) des content streams. Il renvoie un score de confiance et un **routage OCR page par page**, pas seulement un verdict global.

Le point clé est ce qu'il ne fait pas par défaut : **pas d'OCR**. L'OCR est opt-in au build (feature flag) et exige PDFium et ONNX Runtime installés à part ; seules les pages classées comme nécessitant une reconnaissance y passent. L'argument de l'éditeur est économique — une bonne part des PDF n'a pas besoin d'OCR, on extrait en local et on n'envoie au service payant que le reste.

L'extraction restitue le texte avec sa position (police, coordonnées) et le convertit en Markdown : titres déduits du ratio de taille de police, listes, blocs de code par polices monospace, tables en double mode (rectangles puis heuristique), colonnes multiples, RTL, polices CID Type0/Identity-H.

Écrit en Rust par Firecrawl, sous MIT.

## Quand l'utiliser

- Trier un gros corpus hétérogène avant traitement : savoir en quelques millisecondes ce qui mérite un pipeline lourd.
- Réduire une facture d'OCR en n'envoyant que les pages réellement scannées.
- Extraire du texte PDF rapidement, sans modèle et sans GPU, depuis Rust, Python, Node ou le navigateur.

## Quand NE PAS l'utiliser

- Compréhension fine de la mise en page et des tableaux complexes : ce n'est pas son métier → [[Dev/Services/Docling|Docling]], [[Dev/Services/Marker|Marker]].
- Manipulation du PDF (rendu, annotations, découpe, modèle objet) → [[Dev/Services/PyMuPDF|PyMuPDF]].
- Débogage visuel de l'extraction, objet par objet → [[Dev/Services/pdfplumber|pdfplumber]].
- Besoin d'OCR clé en main : il faut fournir soi-même PDFium et ONNX Runtime, ce qui frotte sous Windows et WSL.

## Déploiement & coût

- Rust : `cargo add pdf-inspector` comme bibliothèque, `cargo install pdf-inspector` pour les CLI `pdf2md` et `detect-pdf`.
- Aussi `pip install pdf-inspector`, `npm install @firecrawl/pdf-inspector`, et une cible WebAssembly pour le navigateur.
- Multiplateforme de fait via Rust et ses bindings. Gratuit, mono-nœud, sans service à déployer.

## Pièges

- **Benchmarks auto-déclarés** : sur le corpus opendataloader-bench (200 PDF, juillet 2026), le projet annonce un score global de 0,875, un reading order de 0,915, des tables à 0,814 et 0,470 s pour le corpus, devant liteparse, [[Dev/Services/OpenDataLoader PDF|opendataloader]], pymupdf4llm et markitdown. Chiffres du projet, non reproduits ici.
- Les tables sont extraites par heuristique : fiables sur les grilles nettes, à vérifier sur les mises en page libres.
- L'API bouge encore (projet de sept mois, backlog d'issues nourri) : verrouiller la version.
- Fraîcheur des paquets PyPI et npm par rapport au crate non vérifiée — se fier au crate en cas de doute.

## Alternatives

- [[Dev/Services/PyMuPDF|PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[Dev/Services/pdfplumber|pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[Dev/Services/Docling|Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Dev/Services/Marker|Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie
- [[OCR]] — concept : reconnaissance optique de caractères
- [[Chunking strategies]] — concept : découpage de documents en aval
- [[RAG]] — concept : génération augmentée par récupération
- [[Dev/Services/Firecrawl|Firecrawl]] — même éditeur, côté scraping web
- Docs : https://firecrawl.github.io/pdf-inspector/ · Repo : https://github.com/firecrawl/pdf-inspector
