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
alternatives: ["[[Unstructured]]", "[[LlamaParse]]", "[[Marker]]", "[[pdf-inspector]]", "[[OpenDataLoader PDF]]"]
complements: ["[[PyMuPDF]]", "[[pdfplumber]]"]
tags: [document-parsing, rag, table-extraction, layout-analysis]
url_docs: https://docling-project.github.io/docling/
url_repo: https://github.com/docling-project/docling
---

# Docling

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
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

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — l'étage bas niveau, pour l'extraction brute en amont.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT. — l'étage bas niveau, pour l'extraction brute en amont.

## Ressources

- Documentation — https://docling-project.github.io/docling/
- Dépôt — https://github.com/docling-project/docling

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
