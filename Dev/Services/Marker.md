---
galaxie: dev
type: service
nom: Marker
alias: [marker, marker-pdf, datalab-marker]
pitch: "Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte."
categorie: data/parsing
licence_type: source-available
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Unstructured|Unstructured]]", "[[Dev/Services/Docling|Docling]]", "[[Dev/Services/LlamaParse|LlamaParse]]"]
remplace_par: []
status: actif
tags: [document-parsing, pdf, ocr, markdown-conversion, rag]
url_docs: https://github.com/datalab-to/marker
url_repo: https://github.com/datalab-to/marker
---

# Marker

## Pourquoi

Marker (datalab.to, créé par Vik Paruchuri) convertit des PDF — et désormais Office, images, EPUB — en **Markdown, JSON, HTML ou chunks**, rapidement et avec une bonne fidélité (formules, tableaux, ordre de lecture). C'est un **pipeline vision multi-étapes** bâti sur la famille de modèles **OCR Surya** (détection, reconnaissance, analyse de layout). Nuance de licence majeure : le **code est en GPL-3.0**, mais les **poids des modèles** suivent une licence OpenRAIL-M modifiée, gratuite seulement pour la recherche, l'usage perso et les structures sous **2 M$** de revenus/financement — au-delà, licence commerciale Datalab requise.

## Quand l'utiliser

- Convertir en lot des PDF en **Markdown propre** pour le RAG, en self-host avec GPU.
- Documents riches (formules, tableaux, multi-colonnes) où la qualité de conversion compte.
- **Débit élevé** recherché (Marker est optimisé pour des dizaines de pages/seconde sur GPU).
- Documents **scannés** : l'OCR Surya est intégré.

## Quand NE PAS l'utiliser

- Usage commercial au-dessus du seuil de 2 M$ sans payer la licence → [[Dev/Services/Docling|Docling]] (MIT) / [[Dev/Services/Unstructured|Unstructured]] (Apache-2.0).
- Pas de GPU disponible → outils CPU ([[Dev/Services/pdfplumber|pdfplumber]], [[Dev/Services/Docling|Docling]]) ou service managé [[Dev/Services/LlamaParse|LlamaParse]].
- Simple extraction de texte brut, sans modèles → [[Dev/Services/PyMuPDF|PyMuPDF]].

## Déploiement & coût

- Self-host : `pip install marker-pdf`, modèles Surya téléchargés ; **GPU fortement recommandé**.
- Managé : **API Datalab** (payante) pour le même moteur sans infra.
- **Code GPL-3.0** + **poids OpenRAIL-M** restreints → vérifier l'éligibilité avant tout usage commercial.
- Single-node (par instance GPU).

## Pièges

- **Double licence** à surveiller : le code GPL *et* la restriction sur les poids de modèles.
- Sans GPU, le débit s'effondre.
- L'aspect GPL peut contaminer une distribution propriétaire — bien isoler.

## Alternatives

- [[Dev/Services/Unstructured|Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Dev/Services/Docling|Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Dev/Services/LlamaParse|LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Moteur OCR sous-jacent : Surya (même éditeur, Datalab).
- Doc : https://github.com/datalab-to/marker
