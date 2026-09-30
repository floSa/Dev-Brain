---
role: brique
nom: Docling
alias: [docling, docling-project]
pitch: "Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Unstructured]]", "[[LlamaParse]]", "[[Marker]]", "[[pdf-inspector]]", "[[OpenDataLoader PDF]]", "[[MinerU]]", "[[olmOCR]]"]
complements: ["[[PyMuPDF]]", "[[pdfplumber]]", "[[Tesseract]]", "[[EasyOCR]]"]
tags: [document-parsing, rag, table-extraction, layout-analysis]
url_docs: https://docling-project.github.io/docling/
url_repo: https://github.com/docling-project/docling
---

# Docling

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de conversion de documents née dans l'équipe *AI for Knowledge* d'IBM Research
Zurich, désormais hébergée par la **LF AI & Data Foundation**. Elle convertit PDF, DOCX, PPTX,
XLSX, HTML et images en une représentation unifiée, le `DoclingDocument`, puis exporte en
**Markdown, HTML, JSON lossless ou DocTags**. Sa force est la **compréhension de la mise en
page et des tableaux**, portée par des modèles maison légers — layout, TableFormer —
exécutables **en local sur CPU**, sans aucun appel cloud. Un modèle compagnon,
**Granite-Docling** (VLM, Apache-2.0), couvre l'extraction de bout en bout. Intégrations
natives LangChain et LlamaIndex pour le RAG.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Convertir des PDF ou de l'Office en Markdown structuré en local, sans envoyer les documents à un tiers | |
| Extraction de tableaux et de structure de document de bonne qualité, gratuitement | Le traitement d'un gros PDF reste coûteux en CPU sans GPU |
| Pipeline RAG souverain ou on-prem, sur données sensibles | Projet jeune à évolution rapide : épingler la version |
| Intégration directe avec LangChain ou LlamaIndex | |

## Mise en œuvre

- Installation — `pip install docling` ; les modèles layout et TableFormer se téléchargent au premier usage
- Point d'entrée — conversion vers `DoclingDocument`, puis export Markdown, HTML, JSON lossless ou DocTags
- Prérequis — Python ; un CPU correct suffit, un GPU accélère ; de l'espace disque pour les modèles, que le premier run télécharge, d'où sa latence
- Exécution — en process, mono-nœud, rien à héberger
- Coût — gratuit, MIT ; le modèle compagnon Granite-Docling est sous Apache-2.0

## Écosystème

### Alternatives

- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.
- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.
- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — l'étage bas niveau, pour l'extraction brute en amont.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT. — l'étage bas niveau, pour l'extraction brute en amont.
- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux. — un des moteurs OCR que Docling sait brancher, en ligne de commande ou via tesserocr.
- [[EasyOCR]] — Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024. — un autre moteur OCR branchable, pour les scans et les images.

## Ressources

- Documentation — https://docling-project.github.io/docling/
- Dépôt — https://github.com/docling-project/docling

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
