---
galaxie: dev
type: service
nom: Docling
alias: [docling, docling-project]
pitch: "Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local."
categorie: data/parsing
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Unstructured|Unstructured]]", "[[Dev/Services/LlamaParse|LlamaParse]]", "[[Dev/Services/Marker|Marker]]"]
remplace_par: []
status: actif
tags: [document-parsing, rag, table-extraction, layout-analysis]
url_docs: https://docling-project.github.io/docling/
url_repo: https://github.com/docling-project/docling
---

# Docling

## Pourquoi

Docling est une bibliothèque **open-source (MIT)** de l'équipe *AI for Knowledge* d'IBM Research Zurich, désormais hébergée par la **LF AI & Data Foundation**. Elle convertit des documents (PDF, DOCX, PPTX, XLSX, HTML, images) en une représentation unifiée (`DoclingDocument`), puis exporte en **Markdown, HTML, JSON lossless ou DocTags**. Sa force : la **compréhension de la mise en page et des tableaux** via des modèles maison légers (layout, TableFormer) exécutables **en local sur CPU**, sans appel cloud. Intégrations natives LangChain / LlamaIndex pour le RAG.

## Quand l'utiliser

- Convertir des PDF/Office en Markdown structuré **en local**, sans envoyer les documents à un tiers.
- Extraction de **tableaux** et de structure de document de bonne qualité, gratuitement.
- Pipeline RAG **souverain / on-prem** (données sensibles).
- Intégration directe avec LangChain / LlamaIndex.

## Quand NE PAS l'utiliser

- Juste le texte brut d'un PDF simple, sans modèles → [[Dev/Services/PyMuPDF|PyMuPDF]] / [[Dev/Services/pdfplumber|pdfplumber]].
- Qualité maximale sur PDF très complexes sans gérer GPU/infra → [[Dev/Services/LlamaParse|LlamaParse]].
- Parc multi-format très large avec connecteurs d'ingestion clés en main → [[Dev/Services/Unstructured|Unstructured]].

## Déploiement & coût

- Bibliothèque Python (`pip install docling`). MIT, gratuite ; les modèles (layout, TableFormer) se téléchargent et tournent en local (CPU correct, GPU accélère).
- Modèle compagnon **Granite-Docling** (VLM) sous Apache-2.0 pour une extraction de bout en bout.
- Single-node ; rien à héberger.

## Pièges

- Premier run : **téléchargement des modèles** (latence + espace disque).
- Le traitement de gros PDF reste coûteux en CPU sans GPU.
- Projet jeune à évolution rapide : épingler la version.

## Alternatives

- [[Dev/Services/Unstructured|Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Dev/Services/LlamaParse|LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Dev/Services/Marker|Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Étage bas niveau complémentaire : [[Dev/Services/PyMuPDF|PyMuPDF]] / [[Dev/Services/pdfplumber|pdfplumber]] pour l'extraction brute.
- Doc : https://docling-project.github.io/docling/
