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
alternatives: ["[[PyMuPDF]]", "[[pdfplumber]]", "[[Docling]]", "[[Marker]]", "[[OpenDataLoader PDF]]"]
complements: []
tags: [pdf, document-parsing, ocr, markdown-conversion, layout-analysis]
url_docs: https://firecrawl.github.io/pdf-inspector/
url_repo: https://github.com/firecrawl/pdf-inspector
---

# pdf-inspector

<!-- AUTO:BANDEAU:START -->
> Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Étage de **tri** en amont d'un pipeline documentaire. pdf-inspector classe un PDF en
`TextBased`, `Scanned`, `ImageBased` ou `Mixed` en **10 à 50 ms** : il parse la xref et le
page tree sans charger tous les objets, puis scanne les opérateurs `Tj`/`TJ` (texte) et `Do`
(image) des content streams, et rend un score de confiance avec un **routage OCR page par
page**, pas un simple verdict global. Le point clé est ce qu'il ne fait pas par défaut :
**pas d'OCR**. Celui-ci est opt-in au build et exige PDFium et ONNX Runtime installés à part ;
l'argument est économique — on extrait en local et on n'envoie au service payant que les pages
réellement scannées. L'extraction restitue le texte avec sa position (police, coordonnées) et
le convertit en Markdown : titres déduits du ratio de taille de police, listes, blocs de code
par polices monospace, tables en double mode, colonnes multiples, RTL, polices CID
Type0/Identity-H.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Trier un gros corpus hétérogène avant traitement : savoir en quelques millisecondes ce qui mérite un pipeline lourd | Pas d'OCR clé en main : PDFium et ONNX Runtime sont à fournir soi-même, ce qui frotte sous Windows et WSL |
| Réduire une facture d'OCR en n'envoyant au service payant que les pages réellement scannées | Les tables sont extraites par heuristique : fiables sur les grilles nettes, à vérifier sur les mises en page libres |
| Extraire du texte PDF rapidement, sans modèle ni GPU, depuis Rust, Python, Node ou le navigateur | L'API bouge encore — projet de sept mois, backlog d'issues nourri : verrouiller la version |
| | Benchmarks auto-déclarés (0,875 global sur le corpus opendataloader-bench, 200 PDF, juillet 2026), chiffres du projet non reproduits ici et difficiles à croiser avec ceux des concurrents mesurés sur le même corpus |
| | Fraîcheur des paquets PyPI et npm non vérifiée par rapport au crate : se fier au crate en cas de doute |

## Mise en œuvre

- Installation — `cargo add pdf-inspector` en bibliothèque, `cargo install pdf-inspector` pour les CLI ; aussi `pip install pdf-inspector` et `npm install @firecrawl/pdf-inspector`
- Point d'entrée — bibliothèque Rust, bindings Python, Node et WASM, plus les CLI `pdf2md` et `detect-pdf`
- Prérequis — aucun pour le tri et l'extraction ; l'OCR opt-in exige PDFium et ONNX Runtime installés à part
- Exécution — en process, mono-nœud, sans GPU ni service à déployer ; multiplateforme de fait via Rust et ses bindings
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

## Ressources

- Documentation — https://firecrawl.github.io/pdf-inspector/
- Dépôt — https://github.com/firecrawl/pdf-inspector

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : reconnaissance optique de caractères
- [[Chunking strategies]] — la notion : découpage de documents en aval
- [[RAG]] — la notion : génération augmentée par récupération
- [[Firecrawl]] — même éditeur, côté scraping web
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
