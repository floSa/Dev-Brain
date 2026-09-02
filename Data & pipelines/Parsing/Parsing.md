---
role: hub
nom: Parsing
alias: [parsing de documents]
pitch: Extraire du contenu structuré depuis des documents — PDF, Office, scans — pour le rendre lisible par une machine.
domaines: [data-eng, ai-eng]
tags: [document-parsing, pdf, ocr, markdown-conversion]
---

# Parsing

> Extraire du contenu structuré depuis des documents — PDF, Office, scans — pour le rendre lisible par une machine.

## Ce qu'il faut comprendre

- Un PDF ne contient pas de texte structuré : il contient des instructions de dessin. Il n'y a ni paragraphe, ni tableau, ni ordre de lecture — tout cela est **reconstruit par inférence**, et c'est pourquoi deux outils donnent deux résultats sur le même fichier. C'est la difficulté centrale du domaine, pas un défaut d'implémentation.
- Le clivage qui décide de tout est **le PDF porte-t-il du texte natif ou une image**. Natif, l'extraction est déterministe et rapide ([[PyMuPDF]], [[pdfplumber]]). Scanné, il faut de l'[[OCR]] ([[docTR]]) et le résultat devient probabiliste. Un corpus réel est mixte, d'où l'intérêt de **classer avant de router** ([[pdf-inspector]]) : ne payer l'OCR que sur les pages qui en ont besoin.
- Les **tableaux** sont le point où les outils se séparent vraiment. Le texte, tout le monde le sort ; une structure de lignes et de colonnes fidèle, presque personne. C'est le critère à tester sur ses propres fichiers avant de choisir, et non à lire dans une documentation.
- Un second clivage traverse le domaine : **quelle sortie**. Un accès objet par objet, pour piloter l'extraction soi-même ([[pdfplumber]], [[PyMuPDF]]) ; ou du Markdown prêt à découper et embarquer pour un RAG ([[Marker]], [[Docling]], [[Unstructured]]). Cf. [[Chunking strategies]].
- La **licence** est ici un critère de premier rang, plus que dans le reste du brain : [[PyMuPDF]] est AGPL ou commerciale, [[Marker]] est GPL avec des poids à licence restreinte, [[LlamaParse]] n'est pas ouvert du tout. Sur un projet client, ce point se règle avant le benchmark.

## Choisir

- PDF à texte natif, priorité à la vitesse, accès bas niveau → [[PyMuPDF]] (attention à l'AGPL).
- Tableaux à extraire finement, avec débogage visuel, sous licence MIT → [[pdfplumber]].
- Trier un corpus mixte et ne router vers l'OCR que le nécessaire → [[pdf-inspector]].
- Scans et images, pipeline OCR clé en main → [[docTR]].
- Documents variés (PDF, Office, HTML, e-mails) à partitionner pour un RAG → [[Unstructured]].
- Mise en page et tableaux complexes, exécution locale, Apache/MIT → [[Docling]].
- Markdown de haute qualité, GPU disponible, licence GPL acceptée → [[Marker]].
- Sortie déterministe à bounding boxes, ou PDF à baliser pour l'accessibilité, sous Apache 2.0 → [[OpenDataLoader PDF]].
- Rien à héberger, PDF complexes, budget par crédits → [[LlamaParse]].

<!-- AUTO:START -->
### Briques
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.

### Comparatifs
- [[Comparatif - Parsing de documents]]
<!-- AUTO:END -->
